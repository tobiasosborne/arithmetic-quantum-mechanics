using ArithmeticQuantumMechanics

const PROJECT_ROOT = project_root()
const DEFAULT_MAX_ORDER = 15
const DEFAULT_SOURCES = "gap-small,manual-examples"

struct BuildOptions
    run_slug::String
    run_path::String
    max_order::Int
    sources::Vector{String}
    force::Bool
end

function usage()
    return """
    Usage:
      julia --project=. scripts/arithmetic/finite_ring_db_build.jl --run runs/<slug> [--max-order <n>] [--sources <csv>] [--force]

    Options:
      --run <path>      Required project-relative run bundle path runs/<slug>.
      --max-order <n>   Positive integer order bound. Default: $(DEFAULT_MAX_ORDER).
      --sources <csv>   Comma-separated nonempty source tokens. Default: $(DEFAULT_SOURCES).
      --force           Remove only data/finite_rings.sqlite before rebuilding.
      --help            Print this help text.

    Rerun policy:
      The default no-overwrite policy refuses an existing
      runs/<slug>/data/finite_rings.sqlite. Use --force to rebuild that SQLite
      artifact while preserving the run bundle README and sibling files.
    """
end

function parse_args(args::Vector{String})
    "--help" in args && return :help

    run_path = nothing
    max_order = DEFAULT_MAX_ORDER
    sources = parse_sources(DEFAULT_SOURCES)
    force = false

    index = firstindex(args)
    while index <= lastindex(args)
        arg = args[index]
        if arg == "--run"
            value, index = require_flag_value(args, index, arg)
            run_path !== nothing && error("duplicate --run")
            run_path = value
        elseif arg == "--max-order"
            value, index = require_flag_value(args, index, arg)
            max_order = parse_max_order(value)
        elseif arg == "--sources"
            value, index = require_flag_value(args, index, arg)
            sources = parse_sources(value)
        elseif arg == "--force"
            force && error("duplicate --force")
            force = true
        elseif startswith(arg, "--")
            error("unknown flag: $(arg)")
        else
            error("positional arguments are not accepted: $(arg)")
        end
        index += 1
    end

    run_path === nothing && error("--run runs/<slug> is required")
    run_slug, normalized_run_path = parse_run_path(String(run_path))
    return BuildOptions(run_slug, normalized_run_path, max_order, sources, force)
end

function require_flag_value(args::Vector{String}, index::Int, flag::String)
    index == lastindex(args) && error("missing value for $(flag)")
    value = args[index + 1]
    startswith(value, "--") && error("missing value for $(flag)")
    return value, index + 1
end

function parse_run_path(value::String)
    isempty(value) && error("--run value must be runs/<slug>")
    isabspath(value) && error("--run must be project-relative, got absolute path: $(value)")

    parts = filter(!isempty, split(value, '/'))
    if length(parts) != 2 || parts[1] != "runs"
        error("--run must be an immediate child path of runs/: $(value)")
    end

    slug = parts[2]
    if slug == "." || slug == ".." || occursin('\\', slug)
        error("--run slug is invalid: $(slug)")
    end

    normalized = normpath(value)
    norm_parts = splitpath(normalized)
    if length(norm_parts) != 2 || norm_parts[1] != "runs" || norm_parts[2] != slug
        error("--run must normalize to runs/<slug>: $(value)")
    end

    return slug, joinpath("runs", slug)
end

function parse_max_order(value::String)
    parsed = try
        parse(Int, value)
    catch
        error("--max-order must be a positive integer: $(value)")
    end
    parsed > 0 || error("--max-order must be positive: $(value)")
    return parsed
end

function parse_sources(value::String)
    tokens = strip.(split(value, ','))
    if isempty(tokens) || any(isempty, tokens)
        error("--sources must be a comma-separated list of nonempty tokens")
    end
    return collect(String.(tokens))
end

function require_run_readme(options::BuildOptions)
    run_dir = joinpath(PROJECT_ROOT, options.run_path)
    readme = joinpath(run_dir, "README.md")
    isfile(readme) || error("missing run bundle README: $(readme)")
    return run_dir
end

function git_commit_or_null()
    stdout = IOBuffer()
    stderr = IOBuffer()
    ok = try
        success(
            pipeline(
                Cmd(["git", "-C", PROJECT_ROOT, "rev-parse", "HEAD"]);
                stdout=stdout,
                stderr=stderr,
            ),
        )
    catch
        false
    end
    ok || return nothing
    commit = strip(String(take!(stdout)))
    return isempty(commit) ? nothing : commit
end

function observed_command_line(args::Vector{String})
    julia_exe = first(Base.julia_cmd().exec)
    return join(shell_word.([julia_exe, PROGRAM_FILE, args...]), " ")
end

function shell_word(value::AbstractString)
    isempty(value) && return "''"
    if occursin(r"[^A-Za-z0-9_@%+=:,./-]", value)
        return "'" * replace(value, "'" => "'\\''") * "'"
    end
    return value
end

function utc_timestamp()
    seconds = Ref{Int64}(floor(Int64, time()))
    tm = Ref(Base.Libc.TmStruct())
    result = ccall(
        :gmtime_r,
        Ptr{Base.Libc.TmStruct},
        (Ref{Int64}, Ref{Base.Libc.TmStruct}),
        seconds,
        tm,
    )
    result == C_NULL && error("failed to convert current time to UTC")
    return Base.Libc.strftime("%Y-%m-%dT%H:%M:%SZ", tm[])
end

function tool_versions_json()
    rows = finite_ring_database_tool_preflight()
    return finite_ring_database_canonical_json([
        (;
            name=row.name,
            status=String(row.status),
            command=row.command,
            path=row.path,
            version=row.version,
            skip_reason=row.skip_reason,
        )
        for row in rows
    ])
end

function scope_json(options::BuildOptions)
    return finite_ring_database_canonical_json((
        build_stage="schema_only",
        requested_max_order=options.max_order,
        requested_sources=options.sources,
        ring_scope="finite commutative associative unital",
        zero_ring_policy="include",
        certifies_completeness=false,
        writes_ring_rows=false,
    ))
end

function sql_literal(value)
    value === nothing && return "NULL"
    return "'" * replace(String(value), "'" => "''") * "'"
end

function insert_build_run!(
    sqlite3_path::String,
    db_path::String,
    options::BuildOptions,
    args::Vector{String},
)
    sql = """
    PRAGMA foreign_keys=ON;
    INSERT INTO build_run
      (run_id, run_path, git_commit, command_line, tool_versions_json, created_utc, scope_json)
    VALUES
       ($(sql_literal(options.run_slug)),
       $(sql_literal(options.run_path)),
       $(sql_literal(git_commit_or_null())),
       $(sql_literal(observed_command_line(args))),
       $(sql_literal(tool_versions_json())),
       $(sql_literal(utc_timestamp())),
       $(sql_literal(scope_json(options))));
    """

    stdout = IOBuffer()
    stderr = IOBuffer()
    ok = try
        success(
            pipeline(
                Cmd([sqlite3_path, db_path]);
                stdin=IOBuffer(sql),
                stdout=stdout,
                stderr=stderr,
            ),
        )
    catch err
        error("sqlite3 build_run insert failed for $(db_path): $(sprint(showerror, err))")
    end
    ok && return nothing

    details = strip(String(take!(stderr)))
    isempty(details) && (details = strip(String(take!(stdout))))
    isempty(details) && (details = "sqlite3 exited with a nonzero status")
    error("sqlite3 build_run insert failed for $(db_path): $(details)")
end

function build_database(options::BuildOptions, args::Vector{String})
    run_dir = require_run_readme(options)
    db_path = joinpath(run_dir, "data", "finite_rings.sqlite")
    existing_db = isfile(db_path)
    if existing_db && !options.force
        error(
            "existing SQLite database at $(db_path); default no-overwrite policy " *
            "refuses to rerun. Pass --force to remove only this SQLite artifact " *
            "and rebuild.",
        )
    end

    sqlite3_path = Sys.which("sqlite3")
    sqlite3_path === nothing && error("sqlite3 executable not found; install sqlite3")
    existing_db && options.force && rm(db_path)

    migrate_finite_ring_database_schema!(db_path; sqlite3_path=sqlite3_path)
    insert_build_run!(String(sqlite3_path), db_path, options, args)
    return db_path
end

function main(args::Vector{String}=ARGS)
    parsed = parse_args(args)
    if parsed === :help
        print(usage())
        return nothing
    end

    db_path = build_database(parsed, args)
    println("finite_ring_db_build.jl: initialized schema-only database at ", db_path)
    return db_path
end

if abspath(PROGRAM_FILE) == @__FILE__
    try
        main(ARGS)
    catch err
        println(stderr, "ERROR: ", sprint(showerror, err))
        exit(1)
    end
end
