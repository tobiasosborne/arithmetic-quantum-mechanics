const FINITE_RING_DATABASE_SOURCES_MANIFEST =
    "references/finite_ring_database/SOURCES.md"

const FINITE_RING_DATABASE_TRACKED_SOURCES = (
    "references/finite_ring_database/dml_behboodi_finite_rings_article.html",
    "references/finite_ring_database/blackburn_mclean_enumeration_finite_rings_2107.13215_abs.html",
    "references/finite_ring_database/blackburn_mclean_enumeration_finite_rings_2107.13215_source.tex.gz",
    "references/finite_ring_database/blackburn_mclean_enumeration_finite_rings_2107_13215_source/enumerating-finite-rings_revised_submission.tex",
    "references/finite_ring_database/aims_alabiad_alkhamees_chain_rings.html",
    "references/finite_ring_database/gap_rings_chapter_56.html",
    "references/finite_ring_database/gap_character_tables_chapter_71.html",
    "references/finite_ring_database/sage_finite_rings_index.html",
    "references/finite_ring_database/sage_quotient_ring.html",
    "references/finite_ring_database/oscar_commutative_algebra_intro.html",
    "references/finite_ring_database/oscar_ideals.html",
    "references/finite_ring_database/oscar_modules_over_multivariate_rings_intro.html",
    "references/finite_ring_database/nemo_residue_rings.html",
    "references/finite_ring_database/flint_fmpz_mod_mat.html",
    "references/finite_ring_database/sqlite_about.html",
)

const FINITE_RING_DATABASE_IGNORED_PDFS = (
    "references/finite_ring_database/nowicki_tables_wayback_20211020.pdf",
    "references/finite_ring_database/dml_behboodi_finite_rings.pdf",
)

const FINITE_RING_DATABASE_IGNORED_POLICY_PHRASES =
    ("ignored by git", "third-party pdf", "local pdf")

const FINITE_RING_DATABASE_VERSION_TIMEOUT_SECONDS = 5

function finite_ring_database_source_preflight(root=project_root())
    manifest_path = _frdb_rooted_path(root, FINITE_RING_DATABASE_SOURCES_MANIFEST)
    manifest_text = isfile(manifest_path) ? read(manifest_path, String) : ""
    rows = NamedTuple[]
    for path in FINITE_RING_DATABASE_TRACKED_SOURCES
        push!(rows, _frdb_source_row(root, manifest_text, path, :tracked))
    end
    for path in FINITE_RING_DATABASE_IGNORED_PDFS
        push!(rows, _frdb_source_row(root, manifest_text, path, :ignored_pdf))
    end
    return rows
end

function finite_ring_database_tool_preflight()
    python_command, python_path = _frdb_python_command_path()
    return [
        _frdb_executable_tool_row("julia", "julia", _frdb_julia_path(), ("--version",)),
        _frdb_executable_tool_row("gap", "gap", Sys.which("gap"), ("-v",)),
        _frdb_executable_tool_row("sage", "sage", Sys.which("sage"), ("--version",)),
        _frdb_executable_tool_row("python", python_command, python_path, ("--version",)),
        _frdb_executable_tool_row("sqlite3", "sqlite3", Sys.which("sqlite3"), ("--version",)),
        _frdb_julia_package_tool_row("Oscar"),
        _frdb_julia_package_tool_row("Nemo"),
    ]
end

function finite_ring_database_preflight(root=project_root())
    return (;
        sources=finite_ring_database_source_preflight(root),
        tools=finite_ring_database_tool_preflight(),
    )
end

function _frdb_source_row(root, manifest_text, path, kind)
    exists = isfile(_frdb_rooted_path(root, path))
    mentions = occursin(path, manifest_text)
    existence_required = kind === :tracked
    policy_documented = existence_required ||
                        _frdb_manifest_documents_ignored_pdf_policy(manifest_text, path)
    ok = existence_required ? (exists && mentions) : (mentions && policy_documented)
    details = ok ? _frdb_source_ok_details(existence_required) :
              _frdb_source_failure_details(existence_required, exists, mentions, policy_documented)
    return (;
        path,
        kind,
        existence_required,
        exists,
        manifest_mentions_path=mentions,
        policy_documented,
        ok,
        details,
    )
end

function _frdb_source_ok_details(existence_required)
    return existence_required ? "" : "ignored/local PDF; existence not required"
end

function _frdb_source_failure_details(existence_required, exists, mentions, policy_documented)
    details = String[]
    mentions || push!(details, "manifest does not mention path")
    existence_required && !exists && push!(details, "missing local file")
    !existence_required && !policy_documented &&
        push!(details, "manifest does not document ignored/local PDF policy")
    return join(details, "; ")
end

function _frdb_rooted_path(root::AbstractString, path::AbstractString)
    return joinpath(root, split(path, '/')...)
end

function _frdb_manifest_documents_ignored_pdf_policy(manifest_text, path)
    context = lowercase(_frdb_manifest_context(manifest_text, path))
    return any(phrase -> occursin(phrase, context), FINITE_RING_DATABASE_IGNORED_POLICY_PHRASES)
end

function _frdb_manifest_context(manifest_text, path)
    lines = split(manifest_text, '\n'; keepempty=true)
    for index in eachindex(lines)
        if occursin(path, lines[index])
            first_line = max(firstindex(lines), index - 3)
            last_line = min(lastindex(lines), index + 3)
            return join(lines[first_line:last_line], "\n")
        end
    end
    return ""
end

function _frdb_julia_path()
    path = Sys.which("julia")
    path !== nothing && return path
    runtime_path = joinpath(Sys.BINDIR, "julia")
    return isfile(runtime_path) ? runtime_path : nothing
end

function _frdb_python_command_path()
    path = Sys.which("python")
    path !== nothing && return "python", path
    path = Sys.which("python3")
    path !== nothing && return "python3", path
    return "python or python3", nothing
end

function _frdb_julia_package_tool_row(name)
    path = Base.find_package(String(name))
    version = path === nothing ? nothing : path
    return _frdb_tool_row(name, "Base.find_package", path; version)
end

function _frdb_executable_tool_row(name, command, path, version_args)
    version = path === nothing ? nothing : _frdb_first_version_line(path, version_args)
    return _frdb_tool_row(name, command, path; version)
end

function _frdb_tool_row(name, command, path; version=nothing)
    status = path === nothing ? :missing : :available
    skip_reason = status === :missing ? _frdb_missing_tool_reason(name, command) : nothing
    return (; name=String(name), status, command=String(command), path, version, skip_reason)
end

function _frdb_first_version_line(path, args)
    output = Pipe()
    command = Cmd([String(path), String.(args)...])
    process = run(
        pipeline(ignorestatus(command), stdout=output, stderr=output);
        wait=false,
    )
    close(output.in)
    timer = Timer(FINITE_RING_DATABASE_VERSION_TIMEOUT_SECONDS) do _
        process_running(process) && kill(process)
    end
    try
        line = try
            readline(output)
        catch err
            err isa EOFError ? "" : rethrow()
        end
        wait(process)
        version = strip(line)
        return isempty(version) ? nothing : version
    catch
        return nothing
    finally
        close(timer)
        process_running(process) && kill(process)
        close(output.out)
    end
end

function _frdb_missing_tool_reason(name, command)
    if command == "Base.find_package"
        return "$(String(name)) is not available to Base.find_package in this Julia environment"
    end
    return "$(String(command)) not found on PATH"
end
