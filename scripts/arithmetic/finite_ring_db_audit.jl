using ArithmeticQuantumMechanics

const FINITE_RING_DB_AUDIT_JSON_COLUMNS = (
    ("build_run", "tool_versions_json"),
    ("build_run", "scope_json"),
    ("presentation", "payload_json"),
    ("ring", "additive_invariants_json"),
    ("ring", "identity_vector_json"),
    ("ring", "product_decomposition_json"),
    ("ring", "maximal_ideals_json"),
    ("ring", "residue_field_sizes_json"),
    ("invariant", "invariant_value_json"),
    ("isomorphism_certificate", "certificate_json"),
    ("enumeration_batch", "scope_json"),
    ("enumeration_batch", "reconciliation_json"),
    ("quantization", "qudit_dims_json"),
    ("quantization", "phase_character_json"),
    ("quantization", "symplectic_form_json"),
    ("quantization", "construction_json"),
    ("matrix_artifact", "threshold_json"),
    ("matrix_artifact", "verification_json"),
)

struct AuditOptions
    db_path::String
end

mutable struct CanonicalJsonParser
    chars::Vector{Char}
    index::Int
end

CanonicalJsonParser(text::AbstractString) = CanonicalJsonParser(collect(text), 1)

function usage()
    return """
    Usage:
      julia --project=. scripts/arithmetic/finite_ring_db_audit.jl --db <path>

    Options:
      --db <path>   Required SQLite database file to audit.
      --help        Print this help text.

    Checks:
      Verifies the finite-ring database schema tables, schema version 1, at
      least one build_run row, and canonical JSON in all finite-ring database
      JSON columns covered by the PRD schema. For populated rows, also checks
      provenance links, canonical ring links, certified merge links,
      quantization-or-obstruction coverage, and completeness-claim evidence.
    """
end

function parse_args(args::Vector{String})
    "--help" in args && return :help

    db_path = nothing
    index = firstindex(args)
    while index <= lastindex(args)
        arg = args[index]
        if arg == "--db"
            value, index = require_flag_value(args, index, arg)
            db_path !== nothing && error("duplicate --db")
            db_path = value
        elseif startswith(arg, "--")
            error("unknown flag: $(arg)")
        else
            error("positional arguments are not accepted: $(arg)")
        end
        index += 1
    end

    db_path === nothing && error("--db <path> is required")
    isempty(String(db_path)) && error("--db value must be a database path")
    return AuditOptions(String(db_path))
end

function require_flag_value(args::Vector{String}, index::Int, flag::String)
    index == lastindex(args) && error("missing value for $(flag)")
    value = args[index + 1]
    startswith(value, "--") && error("missing value for $(flag)")
    return value, index + 1
end

function sqlite_identifier(name::AbstractString)
    occursin(r"^[A-Za-z_][A-Za-z0-9_]*$", name) ||
        error("unsafe SQLite identifier in audit contract: $(name)")
    return "\"" * String(name) * "\""
end

function sqlite_literal(value::AbstractString)
    return "'" * replace(String(value), "'" => "''") * "'"
end

function sqlite_query(sqlite3_path::String, db_path::String, sql::AbstractString)
    stdout = IOBuffer()
    stderr = IOBuffer()
    ok = try
        success(
            pipeline(
                Cmd([sqlite3_path, "-batch", "-noheader", "-separator", "\t", db_path]);
                stdin=IOBuffer(sql),
                stdout=stdout,
                stderr=stderr,
            ),
        )
    catch err
        error("sqlite3 query failed for $(db_path): $(sprint(showerror, err))")
    end
    ok && return String(take!(stdout))

    details = strip(String(take!(stderr)))
    isempty(details) && (details = strip(String(take!(stdout))))
    isempty(details) && (details = "sqlite3 exited with a nonzero status")
    error("sqlite3 query failed for $(db_path): $(details)")
end

function output_lines(output::AbstractString)
    stripped = chomp(output)
    isempty(stripped) && return String[]
    return String.(split(stripped, '\n'))
end

function sqlite_table_names(sqlite3_path::String, db_path::String)
    output = sqlite_query(
        sqlite3_path,
        db_path,
        "SELECT name FROM sqlite_master WHERE type='table';",
    )
    return Set(output_lines(output))
end

function sqlite_table_columns(sqlite3_path::String, db_path::String, table::String)
    output = sqlite_query(sqlite3_path, db_path, "PRAGMA table_info($(sqlite_identifier(table)));")
    columns = Set{String}()
    for line in output_lines(output)
        fields = split(line, '\t')
        length(fields) >= 2 || continue
        push!(columns, String(fields[2]))
    end
    return columns
end

function sqlite_count(sqlite3_path::String, db_path::String, sql::AbstractString)
    value = strip(sqlite_query(sqlite3_path, db_path, sql))
    isempty(value) && error("count query returned no rows")
    return parse(Int, value)
end

function decode_sqlite_hex_text(hex::AbstractString)
    iseven(length(hex)) || error("SQLite hex text has odd length")
    bytes = Vector{UInt8}(undef, length(hex) ÷ 2)
    for index in eachindex(bytes)
        offset = 2index - 1
        bytes[index] = parse(UInt8, hex[offset:offset + 1]; base=16)
    end
    text = String(bytes)
    isvalid(text) || error("JSON column text is not valid UTF-8")
    return text
end

function json_at_end(parser::CanonicalJsonParser)
    return parser.index > length(parser.chars)
end

function json_peek(parser::CanonicalJsonParser)
    json_at_end(parser) && json_parse_error(parser, "unexpected end of input")
    return parser.chars[parser.index]
end

function json_advance!(parser::CanonicalJsonParser)
    char = json_peek(parser)
    parser.index += 1
    return char
end

function json_parse_error(parser::CanonicalJsonParser, message::AbstractString)
    throw(ArgumentError("at character $(parser.index): $(message)"))
end

function json_skip_whitespace!(parser::CanonicalJsonParser)
    while !json_at_end(parser) && parser.chars[parser.index] in (' ', '\n', '\r', '\t')
        parser.index += 1
    end
    return nothing
end

function parse_canonical_json_contract(text::AbstractString)
    parser = CanonicalJsonParser(text)
    json_skip_whitespace!(parser)
    value = json_parse_value!(parser)
    json_skip_whitespace!(parser)
    json_at_end(parser) || json_parse_error(parser, "trailing data after JSON value")
    return value
end

function json_parse_value!(parser::CanonicalJsonParser)
    json_skip_whitespace!(parser)
    char = json_peek(parser)
    char == '{' && return json_parse_object!(parser)
    char == '[' && return json_parse_array!(parser)
    char == '"' && return json_parse_string!(parser)
    char == 't' && return json_parse_literal!(parser, "true", true)
    char == 'f' && return json_parse_literal!(parser, "false", false)
    char == 'n' && return json_parse_literal!(parser, "null", nothing)
    (char == '-' || isdigit(char)) && return json_parse_integer!(parser)
    json_parse_error(parser, "expected JSON value")
end

function json_parse_object!(parser::CanonicalJsonParser)
    json_advance!(parser)
    result = Dict{String,Any}()
    json_skip_whitespace!(parser)
    if !json_at_end(parser) && json_peek(parser) == '}'
        json_advance!(parser)
        return result
    end

    while true
        json_skip_whitespace!(parser)
        json_peek(parser) == '"' || json_parse_error(parser, "expected object string key")
        key = json_parse_string!(parser)
        haskey(result, key) && json_parse_error(parser, "duplicate object key: $(key)")
        json_skip_whitespace!(parser)
        json_advance!(parser) == ':' || json_parse_error(parser, "expected ':' after object key")
        result[key] = json_parse_value!(parser)
        json_skip_whitespace!(parser)
        separator = json_advance!(parser)
        if separator == '}'
            return result
        elseif separator != ','
            json_parse_error(parser, "expected ',' or '}' after object value")
        end
    end
end

function json_parse_array!(parser::CanonicalJsonParser)
    json_advance!(parser)
    result = Any[]
    json_skip_whitespace!(parser)
    if !json_at_end(parser) && json_peek(parser) == ']'
        json_advance!(parser)
        return result
    end

    while true
        push!(result, json_parse_value!(parser))
        json_skip_whitespace!(parser)
        separator = json_advance!(parser)
        if separator == ']'
            return result
        elseif separator != ','
            json_parse_error(parser, "expected ',' or ']' after array value")
        end
    end
end

function json_parse_string!(parser::CanonicalJsonParser)
    json_advance!(parser) == '"' || json_parse_error(parser, "expected string")
    buffer = IOBuffer()
    while true
        json_at_end(parser) && json_parse_error(parser, "unterminated string")
        char = json_advance!(parser)
        if char == '"'
            return String(take!(buffer))
        elseif char == '\\'
            print(buffer, json_parse_escape!(parser))
        elseif Int(char) < 0x20
            json_parse_error(parser, "unescaped control character in string")
        else
            print(buffer, char)
        end
    end
end

function json_parse_escape!(parser::CanonicalJsonParser)
    json_at_end(parser) && json_parse_error(parser, "unterminated escape sequence")
    char = json_advance!(parser)
    char == '"' && return '"'
    char == '\\' && return '\\'
    char == '/' && return '/'
    char == 'b' && return '\b'
    char == 'f' && return '\f'
    char == 'n' && return '\n'
    char == 'r' && return '\r'
    char == 't' && return '\t'
    char == 'u' && return json_parse_unicode_escape!(parser)
    json_parse_error(parser, "unsupported string escape: \\$(char)")
end

function json_parse_unicode_escape!(parser::CanonicalJsonParser)
    parser.index + 3 <= length(parser.chars) ||
        json_parse_error(parser, "short unicode escape")
    digits = parser.chars[parser.index:parser.index + 3]
    all(isxdigit, digits) || json_parse_error(parser, "invalid unicode escape")
    parser.index += 4
    codepoint = parse(Int, String(digits); base=16)
    0xD800 <= codepoint <= 0xDFFF &&
        json_parse_error(parser, "surrogate unicode escapes are unsupported")
    return Char(codepoint)
end

function json_parse_literal!(parser::CanonicalJsonParser, literal::String, value)
    for expected in literal
        json_at_end(parser) && json_parse_error(parser, "expected literal $(literal)")
        actual = json_advance!(parser)
        actual == expected || json_parse_error(parser, "expected literal $(literal)")
    end
    return value
end

function json_parse_integer!(parser::CanonicalJsonParser)
    start = parser.index
    if json_peek(parser) == '-'
        json_advance!(parser)
        json_at_end(parser) && json_parse_error(parser, "expected digit after '-'")
    end

    if json_peek(parser) == '0'
        json_advance!(parser)
        if !json_at_end(parser) && isdigit(json_peek(parser))
            json_parse_error(parser, "leading zero in integer")
        end
    else
        isdigit(json_peek(parser)) || json_parse_error(parser, "expected integer digit")
        while !json_at_end(parser) && isdigit(json_peek(parser))
            json_advance!(parser)
        end
    end

    if !json_at_end(parser) && json_peek(parser) in ('.', 'e', 'E')
        json_parse_error(parser, "floats and exponents are unsupported by the canonical JSON contract")
    end

    token = String(parser.chars[start:parser.index - 1])
    return parse(BigInt, token)
end

function json_excerpt(value::AbstractString; limit::Int=160)
    length(value) <= limit && return value
    return first(value, limit) * "..."
end

function audit_json_cell!(
    failures::Vector{String},
    table::String,
    rowid::AbstractString,
    column::String,
    text::String,
)
    location = "$(table) rowid=$(rowid) column=$(column)"
    value = try
        parse_canonical_json_contract(text)
    catch err
        push!(failures, "$(location): malformed JSON: $(sprint(showerror, err))")
        return nothing
    end

    canonical = try
        finite_ring_database_canonical_json(value)
    catch err
        push!(failures, "$(location): canonical JSON re-emit failed: $(sprint(showerror, err))")
        return nothing
    end

    if text != canonical
        push!(
            failures,
            "$(location): noncanonical JSON; expected canonical form $(json_excerpt(canonical))",
        )
    end
    return nothing
end

function audit_json_columns!(
    failures::Vector{String},
    sqlite3_path::String,
    db_path::String,
    table_names::Set{String},
    columns_by_table::Dict{String,Set{String}},
)
    audited_cells = 0
    for (table, column) in FINITE_RING_DB_AUDIT_JSON_COLUMNS
        if !(table in table_names)
            continue
        end
        columns = get(columns_by_table, table, Set{String}())
        if !(column in columns)
            push!(failures, "schema table=$(table) column=$(column): missing required JSON column")
            continue
        end

        sql = """
        SELECT rowid, hex($(sqlite_identifier(column)))
        FROM $(sqlite_identifier(table))
        WHERE $(sqlite_identifier(column)) IS NOT NULL
        ORDER BY rowid;
        """
        output = try
            sqlite_query(sqlite3_path, db_path, sql)
        catch err
            push!(
                failures,
                "schema table=$(table) column=$(column): sqlite3 JSON scan failed: $(sprint(showerror, err))",
            )
            continue
        end

        for line in output_lines(output)
            fields = split(line, '\t'; limit=2)
            if length(fields) != 2
                push!(failures, "schema table=$(table) column=$(column): malformed sqlite3 output")
                continue
            end
            rowid = String(fields[1])
            hex_text = fields[2]
            text = try
                decode_sqlite_hex_text(hex_text)
            catch err
                push!(
                    failures,
                    "$(table) rowid=$(rowid) column=$(column): invalid JSON text encoding: $(sprint(showerror, err))",
                )
                continue
            end
            audited_cells += 1
            audit_json_cell!(failures, table, rowid, column, text)
        end
    end
    return audited_cells
end

function audit_failure_query!(
    failures::Vector{String},
    sqlite3_path::String,
    db_path::String,
    context::String,
    sql::AbstractString,
)
    output = try
        sqlite_query(sqlite3_path, db_path, sql)
    catch err
        push!(failures, "$(context): sqlite3 semantic query failed: $(sprint(showerror, err))")
        return 0
    end

    rows = output_lines(output)
    append!(failures, rows)
    return length(rows)
end

function audit_semantic_contracts!(
    failures::Vector{String},
    sqlite3_path::String,
    db_path::String,
    table_names::Set{String},
)
    semantic_tables = (
        "source",
        "presentation",
        "ring",
        "ring_presentation_link",
        "isomorphism_certificate",
        "enumeration_batch",
        "quantization",
    )
    all(table -> table in table_names, semantic_tables) || return 0

    semantic_failures = 0
    semantic_failures += audit_failure_query!(
        failures,
        sqlite3_path,
        db_path,
        "presentation provenance",
        """
        SELECT 'presentation rowid=' || rowid ||
               ' presentation_id=' || COALESCE(presentation_id, '<null>') ||
               ': source_id must be non-null'
        FROM presentation
        WHERE source_id IS NULL
        ORDER BY rowid;
        """,
    )
    semantic_failures += audit_failure_query!(
        failures,
        sqlite3_path,
        db_path,
        "source provenance",
        """
        SELECT 'source rowid=' || rowid ||
               ' source_id=' || COALESCE(source_id, '<null>') ||
               ': license_status must be nonempty and at least one locator local_path/url/doi must be nonempty'
        FROM source
        WHERE NULLIF(TRIM(license_status), '') IS NULL
           OR COALESCE(
                NULLIF(TRIM(local_path), ''),
                NULLIF(TRIM(url), ''),
                NULLIF(TRIM(doi), '')
              ) IS NULL
        ORDER BY rowid;
        """,
    )
    semantic_failures += audit_failure_query!(
        failures,
        sqlite3_path,
        db_path,
        "ring canonical presentation link",
        """
        SELECT 'ring rowid=' || r.rowid ||
               ' ring_id=' || COALESCE(r.ring_id, '<null>') ||
               ': canonical_presentation_id=' || COALESCE(r.canonical_presentation_id, '<null>') ||
               ' is missing matching ring_presentation_link link_status=canonical'
        FROM ring AS r
        WHERE NOT EXISTS (
            SELECT 1
            FROM ring_presentation_link AS l
            WHERE l.ring_id = r.ring_id
              AND l.presentation_id = r.canonical_presentation_id
              AND l.link_status = 'canonical'
        )
        ORDER BY r.rowid;
        """,
    )
    semantic_failures += audit_failure_query!(
        failures,
        sqlite3_path,
        db_path,
        "ring presentation merge certificate",
        """
        SELECT 'ring_presentation_link ring_id=' || COALESCE(ring_id, '<null>') ||
               ' presentation_id=' || COALESCE(presentation_id, '<null>') ||
               ' link_status=' || COALESCE(link_status, '<null>') ||
               ': noncanonical link_status requires non-null certificate_id'
        FROM ring_presentation_link
        WHERE link_status <> 'canonical'
          AND certificate_id IS NULL
        ORDER BY ring_id, presentation_id;
        """,
    )
    semantic_failures += audit_failure_query!(
        failures,
        sqlite3_path,
        db_path,
        "isomorphism certificate result",
        """
        SELECT 'ring_presentation_link ring_id=' || COALESCE(l.ring_id, '<null>') ||
               ' presentation_id=' || COALESCE(l.presentation_id, '<null>') ||
               ' certificate_id=' || COALESCE(l.certificate_id, '<null>') ||
               ': certificate must reference checker_result=ok and verdict=isomorphic'
        FROM ring_presentation_link AS l
        LEFT JOIN isomorphism_certificate AS c
          ON c.certificate_id = l.certificate_id
        WHERE l.certificate_id IS NOT NULL
          AND (
              c.certificate_id IS NULL
              OR c.checker_result IS NULL OR c.checker_result <> 'ok'
              OR c.verdict IS NULL OR c.verdict <> 'isomorphic'
          )
        ORDER BY l.ring_id, l.presentation_id;
        """,
    )
    semantic_failures += audit_failure_query!(
        failures,
        sqlite3_path,
        db_path,
        "ring quantization coverage",
        """
        SELECT 'ring rowid=' || r.rowid ||
               ' ring_id=' || COALESCE(r.ring_id, '<null>') ||
               ': populated ring requires at least one quantization row'
        FROM ring AS r
        WHERE NOT EXISTS (
            SELECT 1
            FROM quantization AS q
            WHERE q.ring_id = r.ring_id
        )
        ORDER BY r.rowid;
        """,
    )
    semantic_failures += audit_failure_query!(
        failures,
        sqlite3_path,
        db_path,
        "quantization obstruction",
        """
        SELECT 'quantization rowid=' || rowid ||
               ' quantization_id=' || COALESCE(quantization_id, '<null>') ||
               ' ring_id=' || COALESCE(ring_id, '<null>') ||
               ': status!=''available'' requires nonempty obstruction'
        FROM quantization
        WHERE status <> 'available'
          AND (obstruction IS NULL OR NULLIF(TRIM(obstruction), '') IS NULL)
        ORDER BY rowid;
        """,
    )
    semantic_failures += audit_failure_query!(
        failures,
        sqlite3_path,
        db_path,
        "available quantization dimensions",
        """
        SELECT 'quantization rowid=' || rowid ||
               ' quantization_id=' || COALESCE(quantization_id, '<null>') ||
               ' ring_id=' || COALESCE(ring_id, '<null>') ||
               ': available quantization requires hilbert_dim_exact, label_group_order_exact, and observable_basis_dim_exact'
        FROM quantization
        WHERE status = 'available'
          AND (
              hilbert_dim_exact IS NULL
              OR label_group_order_exact IS NULL
              OR observable_basis_dim_exact IS NULL
          )
        ORDER BY rowid;
        """,
    )
    semantic_failures += audit_failure_query!(
        failures,
        sqlite3_path,
        db_path,
        "enumeration batch completeness",
        """
        SELECT 'enumeration_batch rowid=' || rowid ||
               ' batch_id=' || COALESCE(batch_id, '<null>') ||
               ': completeness claim requires unresolved_count_exact=''0'' and nonempty reconciliation_json'
        FROM enumeration_batch
        WHERE completeness_status IN ('complete', 'certified', 'certified_complete')
          AND (
              unresolved_count_exact IS NULL
              OR unresolved_count_exact <> '0'
              OR reconciliation_json IS NULL
              OR NULLIF(TRIM(reconciliation_json), '') IS NULL
          )
        ORDER BY rowid;
        """,
    )
    semantic_failures += audit_failure_query!(
        failures,
        sqlite3_path,
        db_path,
        "populated ring enumeration provenance",
        """
        SELECT 'ring/enumeration_batch: populated ring rows require at least one enumeration_batch provenance row'
        WHERE EXISTS (SELECT 1 FROM ring)
          AND NOT EXISTS (SELECT 1 FROM enumeration_batch);
        """,
    )

    return semantic_failures
end

function audit_database(options::AuditOptions)
    db_path = options.db_path
    isfile(db_path) || error("database file does not exist: $(db_path)")

    sqlite3_path = Sys.which("sqlite3")
    sqlite3_path === nothing && error("sqlite3 executable not found; install sqlite3")
    sqlite3_path = String(sqlite3_path)

    failures = String[]
    required_tables = Set((
        finite_ring_database_prd_table_names()...,
        "finite_ring_database_schema_version",
    ))

    table_names = try
        sqlite_table_names(sqlite3_path, db_path)
    catch err
        error("failed to inspect SQLite tables: $(sprint(showerror, err))")
    end

    for table in sort(collect(setdiff(required_tables, table_names)))
        push!(failures, "schema table=$(table): missing required table")
    end

    schema_version = nothing
    if "finite_ring_database_schema_version" in table_names
        version_output = try
            sqlite_query(
                sqlite3_path,
                db_path,
                """
                SELECT version
                FROM finite_ring_database_schema_version
                WHERE component=$(sqlite_literal("finite_ring_database"));
                """,
            )
        catch err
            push!(failures, "schema version: sqlite3 query failed: $(sprint(showerror, err))")
            ""
        end
        version_lines = output_lines(version_output)
        if length(version_lines) != 1
            push!(failures, "schema version: expected one finite_ring_database version row, found $(length(version_lines))")
        else
            schema_version = strip(version_lines[1])
            if schema_version != string(finite_ring_database_schema_version())
                push!(
                    failures,
                    "schema version: expected $(finite_ring_database_schema_version()), found $(schema_version)",
                )
            end
        end
    end

    build_run_count = 0
    if "build_run" in table_names
        try
            build_run_count = sqlite_count(sqlite3_path, db_path, "SELECT COUNT(*) FROM build_run;")
            build_run_count >= 1 ||
                push!(failures, "build_run: expected at least one row, found 0")
        catch err
            push!(failures, "build_run: count query failed: $(sprint(showerror, err))")
        end
    end

    columns_by_table = Dict{String,Set{String}}()
    for table in intersect(required_tables, table_names)
        columns_by_table[table] = try
            sqlite_table_columns(sqlite3_path, db_path, table)
        catch err
            push!(failures, "schema table=$(table): column inspection failed: $(sprint(showerror, err))")
            Set{String}()
        end
    end

    json_cells = audit_json_columns!(
        failures,
        sqlite3_path,
        db_path,
        table_names,
        columns_by_table,
    )
    semantic_failures = audit_semantic_contracts!(
        failures,
        sqlite3_path,
        db_path,
        table_names,
    )

    return (;
        failures,
        schema_version,
        build_run_count,
        table_count=length(intersect(required_tables, table_names)),
        required_table_count=length(required_tables),
        json_cells,
        semantic_failures,
    )
end

function main(args::Vector{String}=ARGS)
    parsed = parse_args(args)
    if parsed === :help
        print(usage())
        return true
    end

    result = audit_database(parsed)
    if isempty(result.failures)
        println(
            "finite_ring_db_audit.jl: ok db=$(parsed.db_path) " *
            "tables=$(result.table_count)/$(result.required_table_count) " *
            "schema_version=$(result.schema_version) " *
            "build_runs=$(result.build_run_count) json_cells=$(result.json_cells)",
        )
        return true
    end

    println(stderr, "finite_ring_db_audit.jl: failed with $(length(result.failures)) audit failure(s)")
    for failure in result.failures
        println(stderr, "- ", failure)
    end
    return false
end

if abspath(PROGRAM_FILE) == @__FILE__
    try
        ok = main(ARGS)
        ok || exit(1)
    catch err
        println(stderr, "ERROR: ", sprint(showerror, err))
        exit(1)
    end
end
