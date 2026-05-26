using Test
using ArithmeticQuantumMechanics

function _sqlite3_test_result(sqlite3_path, db_path, sql)
    stdout = IOBuffer()
    stderr = IOBuffer()
    ok = success(
        pipeline(
            Cmd([String(sqlite3_path), String(db_path)]);
            stdin=IOBuffer(sql),
            stdout=stdout,
            stderr=stderr,
        ),
    )
    return (; ok, stdout=String(take!(stdout)), stderr=String(take!(stderr)))
end

function _sqlite3_test_output(sqlite3_path, db_path, sql)
    result = _sqlite3_test_result(sqlite3_path, db_path, sql)
    result.ok || error("sqlite3 test query failed: $(strip(result.stderr))")
    return result.stdout
end

function _sqlite3_test_tables(sqlite3_path, db_path)
    output = _sqlite3_test_output(
        sqlite3_path,
        db_path,
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;",
    )
    return Set(filter(!isempty, split(chomp(output), '\n')))
end

function _frdb_build_cli_result(args...)
    stdout = IOBuffer()
    stderr = IOBuffer()
    julia_path = first(Base.julia_cmd().exec)
    script = joinpath("scripts", "arithmetic", "finite_ring_db_build.jl")
    cmd = Cmd(Cmd([julia_path, "--project=.", script, String.(args)...]); dir=project_root())
    ok = try
        success(pipeline(cmd; stdout=stdout, stderr=stderr))
    catch err
        print(stderr, sprint(showerror, err))
        false
    end
    return (; ok, stdout=String(take!(stdout)), stderr=String(take!(stderr)))
end

function _frdb_audit_cli_result(args...)
    stdout = IOBuffer()
    stderr = IOBuffer()
    julia_path = first(Base.julia_cmd().exec)
    script = joinpath("scripts", "arithmetic", "finite_ring_db_audit.jl")
    cmd = Cmd(Cmd([julia_path, "--project=.", script, String.(args)...]); dir=project_root())
    ok = try
        success(pipeline(cmd; stdout=stdout, stderr=stderr))
    catch err
        print(stderr, sprint(showerror, err))
        false
    end
    return (; ok, stdout=String(take!(stdout)), stderr=String(take!(stderr)))
end

function _frdb_temp_slug(label)
    return "2099-01-01-frdb-cli-$(label)-$(getpid())-$(time_ns())"
end

function _frdb_sql_text(value)
    return "'" * replace(String(value), "'" => "''") * "'"
end

function _frdb_sql_json(value)
    return _frdb_sql_text(finite_ring_database_canonical_json(value))
end

@testset "scaffold paths" begin
    root = project_root()
    @test isfile(joinpath(root, "report.tex"))
    @test isdir(joinpath(root, "report", "sections"))
    @test run_bundle_path("2099-01-01-example") ==
          joinpath(root, "runs", "2099-01-01-example")
end

@testset "finite ring database export producer registration" begin
    root = project_root()
    run_slug = "2026-05-26-finite-ring-database"
    run_path = "runs/$(run_slug)"
    finite_ring_csvs = [
        "ring_summary.csv",
        "ring_presentations.csv",
        "ring_isomorphism_certificates.csv",
        "ring_quantization_summary.csv",
        "ring_quantization_obstruction.csv",
    ]

    run_all = read(joinpath(root, "scripts", "run_all.jl"), String)
    readme = read(joinpath(root, run_path, "README.md"), String)
    schema = read(joinpath(root, "data", "SCHEMA.md"), String)
    index = read(joinpath(root, "INDEX.md"), String)
    prd = read(joinpath(root, "docs", "finite_commutative_ring_database_prd.md"), String)

    @test occursin("finite_ring_db_exports", run_all)
    @test occursin("arithmetic/finite_ring_db_exports.jl", run_all)
    @test occursin("ring_summary.csv", readme)
    @test occursin("ring_quantization_obstruction.csv", readme)
    @test occursin("Twenty-two CSV outputs exist.", schema)
    @test occursin(
        "| `scripts/arithmetic/finite_ring_db_exports.jl` | Julia | `$(run_path)/` |",
        index,
    )
    @test occursin(
        "schema-only smoke build, audit gate, and in-memory MVP review exports exist",
        index,
    )
    @test !occursin(
        "No database, producer script, or generated run bundle exists yet.",
        prd,
    )

    for csv in finite_ring_csvs
        @test occursin("## $(csv)", schema)
        @test occursin("`data/$(csv)`", index)
        @test occursin(
            "| `$(run_path)/data/$(csv)` | `scripts/arithmetic/finite_ring_db_exports.jl` | `$(csv)` |",
            index,
        )
    end
end

@testset "finite ring database planning policies" begin
    root = project_root()
    conventions = read(joinpath(root, "CONVENTIONS.md"), String)
    prd = read(joinpath(root, "docs", "finite_commutative_ring_database_prd.md"), String)
    plan = read(
        joinpath(root, "docs", "finite_commutative_ring_database_implementation_plan.md"),
        String,
    )
    schema_integrity_marker =
        "finite_ring_db.schema_integrity_policy = relational_checks_in_schema_json_and_open_enums_in_audit"

    @test occursin("finite_ring_db.zero_ring_policy = include", conventions)
    @test occursin("finite_ring_db.zero_ring_characteristic_exact = 1", conventions)
    @test occursin("finite_ring_db.zero_ring_residue_field_sizes_json = []", conventions)
    @test occursin(
        "finite_ring_db.zero_ring_quantization_policy = not_applicable_until_layer_semantics",
        conventions,
    )
    @test occursin("finite_ring_db.unimplemented_invariant_status = unknown", conventions)
    @test occursin("invariant-factor form", conventions)
    @test occursin("dml_behboodi_finite_rings.pdf", conventions)
    @test occursin("primary cyclic groups", conventions)
    @test occursin("literal string sentinel `unknown`", conventions)
    @test occursin("`finite_ring_dual_numbers(p)` uses ordered\nbasis `[1,e]`", conventions)
    @test occursin("`finite_ring_product` preserves argument\norder", conventions)
    @test occursin("concatenates factor coordinate blocks", conventions)
    @test occursin("finite_ring_db.zero_ring_characteristic_exact = 1", prd)
    @test occursin("finite_ring_db.zero_ring_residue_field_sizes_json = []", prd)
    @test occursin(
        "finite_ring_db.zero_ring_quantization_policy = not_applicable_until_layer_semantics",
        prd,
    )
    @test occursin("finite_ring_db.zero_ring_characteristic_exact = 1", plan)
    @test occursin("finite_ring_db.zero_ring_residue_field_sizes_json = []", plan)
    @test occursin(
        "finite_ring_db.zero_ring_quantization_policy =\nnot_applicable_until_layer_semantics",
        plan,
    )
    @test occursin(
        "finite_ring_db.sqlite_commit_policy = local_run_artifact_until_release_policy",
        conventions,
    )
    @test occursin(
        "finite_ring_db.sqlite_build_rerun_policy = fail_existing_sqlite_unless_force",
        conventions,
    )
    @test occursin(schema_integrity_marker, conventions)
    @test occursin(schema_integrity_marker, prd)
    @test occursin("certificate-link foreign key", prd)
    @test occursin("invariant\nring-or-presentation anchor", prd)
    @test occursin("canonical JSON validity", prd)
    @test occursin("open/evolving status-token vocabulary", conventions)
    @test occursin("No JSON1 `json_valid` schema checks", conventions)
    @test occursin("No JSON1 `json_valid` schema constraints", prd)
    @test isfile(joinpath(root, "scripts", "arithmetic", "finite_ring_db_audit.jl"))
    @test occursin("finite_ring_db_audit.jl", prd)
    @test occursin(
        "finite_ring_db.thickened_frobenius_quantization_helper_scope = mvp_source_backed_only",
        conventions,
    )
    @test occursin(
        "finite_ring_db.gap_small_ring_import_helper_scope = installed_tool_reconciliation_metadata_only",
        conventions,
    )
    @test !occursin(
        "The one-element zero ring is an open decision. Do not include it until",
        prd,
    )
    @test !occursin("tracked separately by\n`aqm-3cm`", prd)
    @test !occursin("Which zero-ring characteristic, residue, and quantisation fields", prd)
    @test !occursin("is not decided by\n  `aqm-pa0`; `aqm-3cm` tracks it", plan)
    @test occursin("- the one-element zero ring;", prd)
    @test occursin(
        "finite_ring_db.sqlite_commit_policy = local_run_artifact_until_release_policy",
        prd,
    ) || occursin("local run artifact", prd)
    @test occursin(
        "finite_ring_db.sqlite_build_rerun_policy = fail_existing_sqlite_unless_force",
        prd,
    )
end

@testset "finite ring database ground-truth preflight" begin
    sources = finite_ring_database_source_preflight()

    @test count(row -> row.kind == :tracked, sources) == 15
    @test count(row -> row.kind == :ignored_pdf, sources) == 2
    @test all(row -> row.ok, sources)
    @test all(row -> row.existence_required, filter(row -> row.kind == :tracked, sources))
    @test all(row -> !row.existence_required, filter(row -> row.kind == :ignored_pdf, sources))

    tools = finite_ring_database_tool_preflight()
    @test [row.name for row in tools] ==
          ["julia", "gap", "sage", "python", "sqlite3", "Oscar", "Nemo"]
    @test all(row -> row.status in (:available, :missing), tools)
    @test all(row -> row.status == :available || row.skip_reason !== nothing, tools)
    @test all(row -> :version in propertynames(row), tools)
    executable_tools = filter(row -> row.name in ("julia", "python", "sqlite3"), tools)
    @test all(
        row -> row.status != :available ||
               (row.version isa AbstractString && !isempty(row.version)),
        executable_tools,
    )
    @test all(
        row -> row.status != :missing ||
               (row.version === nothing && row.skip_reason !== nothing),
        tools,
    )

    preflight = finite_ring_database_preflight()
    @test propertynames(preflight) == (:sources, :tools)
    @test length(preflight.sources) == length(sources)
    @test length(preflight.tools) == length(tools)
end

@testset "finite ring database GAP small-ring import status" begin
    root = project_root()
    conventions = read(joinpath(root, "CONVENTIONS.md"), String)
    @test occursin(
        "finite_ring_db.gap_small_ring_import_helper_scope = installed_tool_reconciliation_metadata_only",
        conventions,
    )
    @test occursin("certifies_completeness=false", conventions)
    @test occursin("imports no presentations", conventions)
    @test occursin("`SmallRing(1,1)` is counted", conventions)
    @test occursin("`--bare -q`", conventions)

    skipped = finite_ring_gap_small_ring_import_status(3; gap_path=nothing)
    @test skipped.status == "skipped"
    @test skipped.reason == "gap_not_available"
    @test skipped.requested_max_order == 3
    @test skipped.tool_status == "missing"
    @test isempty(skipped.rows)
    @test isempty(skipped.imported_presentations)
    @test skipped.certifies_completeness == false
    @test occursin("references/finite_ring_database/SOURCES.md", skipped.source_locator)
    @test occursin("gap_rings_chapter_56.html", skipped.source_locator)

    mktempdir() do dir
        missing = finite_ring_gap_small_ring_import_status(2; gap_path=joinpath(dir, "gap"))
        @test missing.status == "skipped"
        @test missing.reason == "gap_not_available"
        @test isempty(missing.rows)
        @test isempty(missing.imported_presentations)
    end

    @test_throws ArgumentError finite_ring_gap_small_ring_import_status(0; gap_path=nothing)
    @test_throws ArgumentError finite_ring_gap_small_ring_import_status(16; gap_path=nothing)

    gap_command = ArithmeticQuantumMechanics._frdb_gap_small_ring_command("gap")
    @test gap_command.exec == ["gap", "--bare", "-q"]

    gap_script = ArithmeticQuantumMechanics._frdb_gap_small_ring_status_script(2)
    @test occursin("missing_unital_predicate|IsRingWithOne", gap_script)
    @test occursin("if s = 1 and i = 1 then", gap_script)
    @test occursin("elif IsRingWithOne(R) and IsCommutative(R) then", gap_script)

    parse_status =
        ArithmeticQuantumMechanics._frdb_parse_gap_small_ring_status_output
    parse_row = ArithmeticQuantumMechanics._frdb_parse_gap_small_ring_row

    @test_throws ErrorException parse_status(
        "AQM_FRDB_ERROR|missing_commutativity_predicate|IsCommutative\n",
        "",
        1,
    )
    @test_throws ErrorException parse_row("AQM_FRDB_ROW|1|1")
    @test_throws ErrorException parse_row("AQM_FRDB_ROW|1|1|1|extra")
    @test_throws ErrorException parse_row("AQM_FRDB_ROW|1|0|1")
    @test_throws ErrorException parse_row("AQM_FRDB_ROW|1|1|-1")
    @test_throws ErrorException parse_status("AQM_FRDB_ROW|1|1|1\n", "", 1)
    @test_throws ErrorException parse_status(
        "AQM_FRDB_GAP_VERSION|4.14\nAQM_FRDB_ROW|1|1|1\n",
        "",
        2,
    )

    gap_path = Sys.which("gap")
    if gap_path === nothing
        @test_skip gap_path !== nothing
    else
        status = finite_ring_gap_small_ring_import_status(1; gap_path=gap_path)
        @test status.status == "reconciled"
        @test status.tool_status == "available"
        @test status.requested_max_order == 1
        @test status.small_ring_library_max_order == 15
        @test length(status.rows) == 1
        @test status.rows[1].order == 1
        @test status.rows[1].total_count == 1
        @test status.rows[1].scoped_commutative_unital_count == 1
        @test status.certifies_completeness == false
        @test isempty(status.imported_presentations)
        @test status.tool_version isa AbstractString
        @test !isempty(status.tool_version)
        @test occursin("references/finite_ring_database/SOURCES.md", status.source_locator)
        @test occursin("gap_rings_chapter_56.html", status.source_locator)
    end
end

@testset "finite ring database quotient constructor status" begin
    root = project_root()
    conventions = read(joinpath(root, "CONVENTIONS.md"), String)
    @test occursin(
        "finite_ring_db.quotient_constructor_helper_scope = mvp_exact_in_memory_local_core_status_only",
        conventions,
    )
    @test occursin("not a general quotient-ring\nengine", conventions)

    status = finite_ring_quotient_constructor_status()
    @test status.certifies_backend_completeness == false
    @test [row.name for row in status.quotient_examples] ==
          ["F_2[x]/(x^2+x)", "F_3[e]/(e^2)", "Z/6Z"]

    expected = Dict(
        "F_2[x]/(x^2+x)" => (order=4, characteristic=2),
        "F_3[e]/(e^2)" => (order=9, characteristic=3),
        "Z/6Z" => (order=6, characteristic=6),
    )
    examples = Dict(row.name => row for row in status.quotient_examples)
    for row in status.quotient_examples
        wanted = expected[row.name]
        @test row.status == "available"
        @test row.backend == "local_core"
        @test row.expected_order == wanted.order
        @test row.expected_characteristic == wanted.characteristic
        @test finite_ring_order(row.ring) == wanted.order
        @test finite_ring_characteristic_exact(row.ring) == wanted.characteristic
        @test occursin("finite_commutative_ring_database_prd.md", row.source_locator)
        @test occursin("CONVENTIONS.md (an)", row.source_locator)
    end

    f2_product = finite_ring_product(finite_ring_prime_field(2), finite_ring_prime_field(2))
    f2_certificate = finite_ring_find_isomorphism_certificate(
        examples["F_2[x]/(x^2+x)"].ring,
        f2_product,
    )
    @test f2_certificate !== nothing
    @test finite_ring_verify_isomorphism_certificate(
        examples["F_2[x]/(x^2+x)"].ring,
        f2_product,
        f2_certificate,
    ).ok

    @test finite_ring_verify_isomorphism_certificate(
        examples["F_3[e]/(e^2)"].ring,
        finite_ring_dual_numbers(3),
        [1 0; 0 1],
    ).ok

    f2xf3 = finite_ring_product(finite_ring_prime_field(2), finite_ring_prime_field(3))
    z6_certificate = finite_ring_find_isomorphism_certificate(examples["Z/6Z"].ring, f2xf3)
    @test z6_certificate !== nothing
    @test finite_ring_verify_isomorphism_certificate(
        examples["Z/6Z"].ring,
        f2xf3,
        z6_certificate,
    ).ok
    z6_dedup = finite_ring_deduplicate_small_rings(["Z/6Z" => examples["Z/6Z"].ring, "F_2xF_3" => f2xf3])
    @test length(z6_dedup.merges) == 1
    @test only(z6_dedup.merges).certificate_check.ok

    skipped = finite_ring_quotient_constructor_status(
        sage_path=nothing,
        oscar_available=false,
        nemo_available=false,
    )
    @test [row.backend for row in skipped.optional_backend_rows] == ["sage", "Oscar", "Nemo"]
    @test all(row -> row.status == "skipped", skipped.optional_backend_rows)
    @test all(row -> row.reason == "tool_not_available", skipped.optional_backend_rows)
    @test all(row -> row.certifies_completeness == false, skipped.optional_backend_rows)
end

@testset "finite ring database schema migration" begin
    prd_tables = finite_ring_database_prd_table_names()
    version_table = "finite_ring_database_schema_version"
    sql = finite_ring_database_schema_sql()

    @test finite_ring_database_schema_version() == 1
    @test prd_tables == (
        "source",
        "build_run",
        "presentation",
        "ring",
        "ring_presentation_link",
        "invariant",
        "isomorphism_certificate",
        "enumeration_batch",
        "quantization",
        "matrix_artifact",
    )
    @test occursin("PRAGMA foreign_keys=ON;", sql)
    for table in prd_tables
        @test occursin("CREATE TABLE IF NOT EXISTS $(table)", sql)
    end
    @test occursin("CREATE TABLE IF NOT EXISTS $(version_table)", sql)
    @test occursin("VALUES ('finite_ring_database', 1)", sql)
    @test occursin(
        "FOREIGN KEY(certificate_id) REFERENCES isomorphism_certificate(certificate_id)",
        sql,
    )
    @test occursin("CHECK(ring_id IS NOT NULL OR presentation_id IS NOT NULL)", sql)
    @test occursin("is_commutative INTEGER NOT NULL CHECK(is_commutative IN (0, 1))", sql)
    @test occursin("has_one INTEGER NOT NULL CHECK(has_one IN (0, 1))", sql)
    @test !occursin("json_valid", lowercase(sql))

    err = try
        migrate_finite_ring_database_schema!(tempname(); sqlite3_path=nothing)
        nothing
    catch caught
        caught
    end
    @test err isa ErrorException
    @test occursin("sqlite3", sprint(showerror, err))

    sqlite3_path = Sys.which("sqlite3")
    if sqlite3_path === nothing
        @test_skip sqlite3_path !== nothing
    else
        mktempdir() do dir
            db_path = joinpath(dir, "finite_rings.sqlite")
            before_tables = _sqlite3_test_tables(sqlite3_path, db_path)
            expected_tables = Set((prd_tables..., version_table))

            @test isempty(intersect(Set(prd_tables), before_tables))
            @test !(version_table in before_tables)

            migration = migrate_finite_ring_database_schema!(
                db_path;
                sqlite3_path=sqlite3_path,
            )
            @test migration.status == :ok
            @test migration.db_path == abspath(db_path)
            @test migration.schema_version == 1
            @test Set(migration.tables) == expected_tables

            after_tables = _sqlite3_test_tables(sqlite3_path, db_path)
            @test issubset(expected_tables, after_tables)
            @test strip(
                _sqlite3_test_output(
                    sqlite3_path,
                    db_path,
                    """
                    SELECT version
                    FROM finite_ring_database_schema_version
                    WHERE component='finite_ring_database';
                    """,
                ),
            ) == "1"

            migration_again = migrate_finite_ring_database_schema!(
                db_path;
                sqlite3_path=sqlite3_path,
            )
            @test migration_again == migration
            @test _sqlite3_test_tables(sqlite3_path, db_path) == after_tables
            @test strip(
                _sqlite3_test_output(
                    sqlite3_path,
                    db_path,
                    "SELECT COUNT(*) FROM finite_ring_database_schema_version;",
                ),
            ) == "1"

            invalid_insert = _sqlite3_test_result(
                sqlite3_path,
                db_path,
                """
                PRAGMA foreign_keys=ON;
                INSERT INTO ring_presentation_link
                  (ring_id, presentation_id, link_status, certificate_id)
                VALUES ('missing-ring', 'missing-presentation', 'invalid', 'missing-cert');
                """,
            )
            @test !invalid_insert.ok
            @test strip(
                _sqlite3_test_output(
                    sqlite3_path,
                    db_path,
                    "SELECT COUNT(*) FROM ring_presentation_link;",
                ),
            ) == "0"

            fixture_insert = _sqlite3_test_result(
                sqlite3_path,
                db_path,
                """
                PRAGMA foreign_keys=ON;
                INSERT INTO build_run
                  (run_id, run_path, command_line, tool_versions_json, created_utc, scope_json)
                VALUES ('run:test', 'runs/test', 'cmd', '{}', '2099-01-01T00:00:00Z', '{}');
                INSERT INTO presentation
                  (presentation_id, run_id, presentation_type, parsed_status)
                VALUES ('pres:test', 'run:test', 'manual', 'parsed');
                INSERT INTO ring
                  (ring_id, canonical_presentation_id, order_exact, characteristic_exact,
                   additive_invariants_json, is_commutative, has_one, local_status,
                   reduced_status, field_status, frobenius_status,
                   generating_character_status, audit_status)
                VALUES ('ring:test', 'pres:test', '1', '1', '[]', 1, 1, 'unknown',
                        'unknown', 'unknown', 'unknown', 'unknown', 'pending');
                """,
            )
            @test fixture_insert.ok

            missing_certificate = _sqlite3_test_result(
                sqlite3_path,
                db_path,
                """
                PRAGMA foreign_keys=ON;
                INSERT INTO ring_presentation_link
                  (ring_id, presentation_id, link_status, certificate_id)
                VALUES ('ring:test', 'pres:test', 'canonical', 'iso:missing');
                """,
            )
            @test !missing_certificate.ok
            @test strip(
                _sqlite3_test_output(
                    sqlite3_path,
                    db_path,
                    "SELECT COUNT(*) FROM ring_presentation_link;",
                ),
            ) == "0"

            nullable_certificate = _sqlite3_test_result(
                sqlite3_path,
                db_path,
                """
                PRAGMA foreign_keys=ON;
                INSERT INTO ring_presentation_link
                  (ring_id, presentation_id, link_status)
                VALUES ('ring:test', 'pres:test', 'canonical');
                """,
            )
            @test nullable_certificate.ok

            unanchored_invariant = _sqlite3_test_result(
                sqlite3_path,
                db_path,
                """
                INSERT INTO invariant
                  (invariant_id, invariant_name, invariant_value_json, method)
                VALUES ('inv:unanchored', 'order', '1', 'test');
                """,
            )
            @test !unanchored_invariant.ok

            invalid_commutative_boolean = _sqlite3_test_result(
                sqlite3_path,
                db_path,
                """
                PRAGMA foreign_keys=ON;
                INSERT INTO ring
                  (ring_id, canonical_presentation_id, order_exact, characteristic_exact,
                   additive_invariants_json, is_commutative, has_one, local_status,
                   reduced_status, field_status, frobenius_status,
                   generating_character_status, audit_status)
                VALUES ('ring:bad-commutative', 'pres:test', '1', '1', '[]', 2, 1,
                        'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'pending');
                """,
            )
            @test !invalid_commutative_boolean.ok

            invalid_has_one_boolean = _sqlite3_test_result(
                sqlite3_path,
                db_path,
                """
                PRAGMA foreign_keys=ON;
                INSERT INTO ring
                  (ring_id, canonical_presentation_id, order_exact, characteristic_exact,
                   additive_invariants_json, is_commutative, has_one, local_status,
                   reduced_status, field_status, frobenius_status,
                   generating_character_status, audit_status)
                VALUES ('ring:bad-has-one', 'pres:test', '1', '1', '[]', 1, -1,
                        'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'pending');
                """,
            )
            @test !invalid_has_one_boolean.ok
        end
    end
end

@testset "finite ring database canonical IDs" begin
    left = Dict(
        "presentation_type" => "quotient",
        "generators" => ["x"],
        "relations" => ["x^2"],
        "metadata" => Dict(:has_one => true, "source_rank" => 2, :note => nothing),
    )
    right = Dict(
        :metadata => Dict("source_rank" => 2, :note => nothing, "has_one" => true),
        :relations => ("x^2",),
        :generators => ["x"],
        :presentation_type => "quotient",
    )

    @test finite_ring_database_canonical_json(left) ==
          finite_ring_database_canonical_json(right)
    @test finite_ring_database_canonical_json((b=1, a=["q", false, nothing])) ==
          "{\"a\":[\"q\",false,null],\"b\":1}"

    presentation_id = finite_ring_presentation_id(left)
    @test presentation_id == finite_ring_presentation_id(right)
    @test startswith(presentation_id, "pres:")
    @test length(presentation_id) == length("pres:") + 64
    @test presentation_id != finite_ring_presentation_id(merge(left, Dict("relations" => ["x^3"])))

    certificate_id = finite_ring_certificate_id((map=[1, 2], verdict="isomorphic"))
    @test startswith(certificate_id, "iso:")
    @test length(certificate_id) == length("iso:") + 64

    representative = (presentation_id=presentation_id, additive_invariants=[2, 2])
    scope = (commutative=true, unital=true, zero_ring_policy="include")
    ring_id = finite_ring_id(representative, scope)
    @test startswith(ring_id, "ring:")
    @test length(ring_id) == length("ring:") + 64
    @test ring_id == finite_ring_id(
        Dict(:additive_invariants => [2, 2], "presentation_id" => presentation_id),
        Dict("zero_ring_policy" => "include", :unital => true, :commutative => true),
    )
    @test ring_id != finite_ring_id(
        representative,
        (commutative=true, unital=true, zero_ring_policy="exclude"),
    )

    @test finite_ring_quantization_id(ring_id, "residue", "v1") ==
          "quant:$(ring_id):residue:v1"
    @test_throws ArgumentError finite_ring_database_canonical_json((a=1.5,))
    @test_throws ArgumentError finite_ring_database_canonical_json(Dict(1 => "unsupported key"))
    @test_throws ArgumentError finite_ring_database_canonical_json(Dict(:a => 1, "a" => 2))
    @test_throws ArgumentError finite_ring_quantization_id(ring_id, "bad:layer", "v1")
end

@testset "finite ring database structure constants" begin
    z4_products = reshape([1], 1, 1, 1)
    z4 = finite_ring_structure_constants([4], [1], z4_products)
    @test finite_ring_order(z4) == 4
    @test finite_ring_zero(z4) == [0]
    @test finite_ring_one(z4) == [1]
    @test finite_ring_add(z4, [3], [2]) == [1]
    @test finite_ring_neg(z4, [3]) == [1]
    @test finite_ring_mul(z4, [2], [3]) == [2]
    @test finite_ring_elements(z4) == [[0], [1], [2], [3]]

    dual_products = zeros(Int, 2, 2, 2)
    dual_products[1, 1, 1] = 1
    dual_products[1, 2, 2] = 1
    dual_products[2, 1, 2] = 1
    dual = finite_ring_structure_constants([2, 2], [1, 0], dual_products)
    @test finite_ring_order(dual) == 4
    @test finite_ring_add(dual, [1, 1], [0, 1]) == [1, 0]
    @test finite_ring_mul(dual, [1, 1], [1, 1]) == [1, 0]
    @test finite_ring_mul(dual, [0, 1], [0, 1]) == [0, 0]
    @test length(finite_ring_elements(dual)) == 4

    noncommutative = zeros(Int, 3, 3, 3)
    noncommutative[1, 1, 1] = 1
    for i in 2:3
        noncommutative[1, i, i] = 1
        noncommutative[i, 1, i] = 1
    end
    noncommutative[3, 2, 2] = 1
    @test_throws ArgumentError finite_ring_structure_constants(
        [2, 2, 2],
        [1, 0, 0],
        noncommutative,
    )

    nonassociative = zeros(Int, 3, 3, 3)
    nonassociative[1, 1, 1] = 1
    for i in 2:3
        nonassociative[1, i, i] = 1
        nonassociative[i, 1, i] = 1
    end
    nonassociative[2, 2, 3] = 1
    nonassociative[2, 3, 1] = 1
    nonassociative[3, 2, 1] = 1
    @test_throws ArgumentError finite_ring_structure_constants(
        [2, 2, 2],
        [1, 0, 0],
        nonassociative,
    )

    @test_throws ArgumentError finite_ring_structure_constants([2], [2], reshape([1], 1, 1, 1))
    @test_throws ArgumentError finite_ring_structure_constants([4], [0], z4_products)

    incompatible = zeros(Int, 2, 2, 2)
    incompatible[1, 2, 2] = 1
    @test_throws ArgumentError finite_ring_structure_constants([2, 4], [0, 0], incompatible)
end

@testset "finite ring database manual MVP constructors" begin
    expected = [
        "zero_ring" => (order=1, characteristic=1),
        "F_2" => (order=2, characteristic=2),
        "F_3" => (order=3, characteristic=3),
        "F_5" => (order=5, characteristic=5),
        "Z/4Z" => (order=4, characteristic=4),
        "Z/6Z" => (order=6, characteristic=6),
        "Z/8Z" => (order=8, characteristic=8),
        "Z/9Z" => (order=9, characteristic=9),
        "F_2[e]/(e^2)" => (order=4, characteristic=2),
        "F_3[e]/(e^2)" => (order=9, characteristic=3),
        "F_2xF_2" => (order=4, characteristic=2),
        "F_2xF_3" => (order=6, characteristic=6),
        "F_3xF_3" => (order=9, characteristic=3),
    ]

    examples = finite_ring_mvp_examples()
    @test first.(examples) == first.(expected)
    @test length(examples) == 13
    by_name = Dict(examples)

    for (name, invariants) in expected
        R = by_name[name]
        @test finite_ring_order(R) == invariants.order
        @test finite_ring_characteristic_exact(R) == invariants.characteristic
    end

    z6 = finite_ring_zn(6)
    @test finite_ring_one(z6) == [1]
    @test finite_ring_mul(z6, [4], [5]) == [2]

    dual_f3 = finite_ring_dual_numbers(3)
    @test finite_ring_mul(dual_f3, [0, 1], [0, 1]) == [0, 0]
    @test finite_ring_mul(dual_f3, [2, 1], [2, 2]) == [1, 0]

    f2xf3 = finite_ring_product(finite_ring_prime_field(2), finite_ring_prime_field(3))
    @test finite_ring_order(f2xf3) == 6
    @test finite_ring_characteristic_exact(f2xf3) == 6
    @test finite_ring_mul(f2xf3, [1, 2], [1, 2]) == [1, 1]
    @test finite_ring_mul(f2xf3, [1, 0], [0, 1]) == [0, 0]

    @test_throws ArgumentError finite_ring_prime_field(4)
    @test_throws ArgumentError finite_ring_dual_numbers(1)
end

@testset "finite ring database basic invariants" begin
    expected = [
        "zero_ring" => (order=1, characteristic=1, additive=Int[]),
        "F_2" => (order=2, characteristic=2, additive=[2]),
        "F_3" => (order=3, characteristic=3, additive=[3]),
        "F_5" => (order=5, characteristic=5, additive=[5]),
        "Z/4Z" => (order=4, characteristic=4, additive=[4]),
        "Z/6Z" => (order=6, characteristic=6, additive=[6]),
        "Z/8Z" => (order=8, characteristic=8, additive=[8]),
        "Z/9Z" => (order=9, characteristic=9, additive=[9]),
        "F_2[e]/(e^2)" => (order=4, characteristic=2, additive=[2, 2]),
        "F_3[e]/(e^2)" => (order=9, characteristic=3, additive=[3, 3]),
        "F_2xF_2" => (order=4, characteristic=2, additive=[2, 2]),
        "F_2xF_3" => (order=6, characteristic=6, additive=[6]),
        "F_3xF_3" => (order=9, characteristic=3, additive=[3, 3]),
    ]

    examples = Dict(finite_ring_mvp_examples())
    @test length(examples) == 13
    for (name, wanted) in expected
        invariants = finite_ring_basic_invariants(examples[name])
        @test invariants.order_exact == wanted.order
        @test invariants.characteristic_exact == wanted.characteristic
        @test invariants.additive_invariant_factors == wanted.additive
        @test finite_ring_additive_invariant_factors(examples[name]) == wanted.additive
        @test invariants.local_status == "unknown"
        @test invariants.reduced_status == "unknown"
        @test invariants.field_status == "unknown"
        @test invariants.product_status == "unknown"
        @test invariants.frobenius_status == "unknown"
        @test invariants.generating_character_status == "unknown"
    end

    z0 = finite_ring_basic_invariants(examples["zero_ring"])
    @test z0.maximal_ideals == []
    @test z0.residue_field_sizes == Int[]

    nonzero = finite_ring_basic_invariants(examples["F_2"])
    @test nonzero.maximal_ideals == :unknown
    @test nonzero.residue_field_sizes == :unknown
end

@testset "finite ring database isomorphism certificates" begin
    root = project_root()
    conventions = read(joinpath(root, "CONVENTIONS.md"), String)
    @test occursin("`additive_generator_image_matrix`, rows are\nsource additive generators", conventions)
    @test occursin("Row `i` is the\ncanonical target coordinate vector", conventions)
    @test occursin("first local deduplication search is a bounded MVP", conventions)
    @test occursin("deterministic input order", conventions)

    dual_f2 = finite_ring_dual_numbers(2)
    identity_dual = [[1, 0], [0, 1]]
    dual_check = finite_ring_verify_isomorphism_certificate(dual_f2, dual_f2, identity_dual)
    @test dual_check.ok
    @test dual_check.well_defined_additive_map
    @test dual_check.bijective_additive_map
    @test dual_check.identity_preserved
    @test dual_check.multiplication_preserved
    @test isempty(dual_check.failure_reasons)
    @test finite_ring_apply_generator_image_matrix(dual_f2, dual_f2, identity_dual, [1, 1]) ==
          [1, 1]

    z6 = finite_ring_zn(6)
    f2xf3 = finite_ring_product(finite_ring_prime_field(2), finite_ring_prime_field(3))
    crt_matrix = [1 1]
    crt_check = finite_ring_verify_isomorphism_certificate(z6, f2xf3, crt_matrix)
    @test crt_check.ok
    @test finite_ring_apply_generator_image_matrix(z6, f2xf3, crt_matrix, [5]) == [1, 2]

    bad_additive = finite_ring_verify_isomorphism_certificate(
        finite_ring_zn(2),
        finite_ring_zn(4),
        [1;;],
    )
    @test !bad_additive.ok
    @test !bad_additive.well_defined_additive_map
    @test occursin("not well-defined", join(bad_additive.failure_reasons, "; "))

    non_bijective = finite_ring_verify_isomorphism_certificate(
        dual_f2,
        dual_f2,
        [[1, 0], [0, 0]],
    )
    @test !non_bijective.ok
    @test non_bijective.well_defined_additive_map
    @test !non_bijective.bijective_additive_map
    @test non_bijective.identity_preserved

    moves_one = finite_ring_verify_isomorphism_certificate(
        dual_f2,
        dual_f2,
        [[1, 1], [0, 1]],
    )
    @test !moves_one.ok
    @test moves_one.bijective_additive_map
    @test !moves_one.identity_preserved

    breaks_multiplication = finite_ring_verify_isomorphism_certificate(
        dual_f2,
        dual_f2,
        [[1, 0], [1, 1]],
    )
    @test !breaks_multiplication.ok
    @test breaks_multiplication.bijective_additive_map
    @test breaks_multiplication.identity_preserved
    @test !breaks_multiplication.multiplication_preserved

    noncanonical_row = finite_ring_verify_isomorphism_certificate(
        finite_ring_zn(2),
        finite_ring_zn(2),
        [2;;],
    )
    @test !noncanonical_row.ok
    @test occursin("canonical coordinate", join(noncanonical_row.failure_reasons, "; "))
end

@testset "finite ring database small-ring dedup search" begin
    z6 = finite_ring_zn(6)
    f2xf3 = finite_ring_product(finite_ring_prime_field(2), finite_ring_prime_field(3))
    certificate = finite_ring_find_isomorphism_certificate(z6, f2xf3)
    @test certificate !== nothing
    @test finite_ring_verify_isomorphism_certificate(z6, f2xf3, certificate).ok

    dedup = finite_ring_deduplicate_small_rings(finite_ring_mvp_examples())
    merge_pairs = Set((merge.source_name, merge.target_name) for merge in dedup.merges)
    @test merge_pairs == Set([("F_2xF_3", "Z/6Z")])
    @test length(dedup.representatives) == length(finite_ring_mvp_examples()) - 1
    @test all(merge -> merge.certificate_check.ok, dedup.merges)

    representative_names = first.(dedup.representatives)
    @test "Z/4Z" in representative_names
    @test "F_2[e]/(e^2)" in representative_names
    @test "F_3[e]/(e^2)" in representative_names
    @test "F_3xF_3" in representative_names

    examples = Dict(finite_ring_mvp_examples())
    @test finite_ring_find_isomorphism_certificate(
        examples["F_3[e]/(e^2)"],
        examples["F_3xF_3"],
    ) === nothing
    @test finite_ring_find_isomorphism_certificate(
        examples["Z/4Z"],
        examples["F_2[e]/(e^2)"],
    ) === nothing
    @test_throws ArgumentError finite_ring_find_isomorphism_certificate(
        finite_ring_zn(8),
        finite_ring_zn(8);
        max_order=7,
    )
end

@testset "finite ring database residue quantization records" begin
    root = project_root()
    conventions = read(joinpath(root, "CONVENTIONS.md"), String)
    @test occursin(
        "finite_ring_db.residue_quantization_helper_scope = mvp_source_backed_only",
        conventions,
    )
    @test occursin("this helper is not a general maximal-ideal algorithm", conventions)

    records = Dict(finite_ring_mvp_residue_quantization_records())
    @test Set(keys(records)) == Set(first.(finite_ring_mvp_examples()))

    f3 = records["F_3"]
    @test f3.layer == "residue"
    @test f3.status == "available"
    @test f3.residue_qudit_dims == [3]
    @test f3.hilbert_dim_exact == 3
    @test f3.label_group_order_exact == 9
    @test f3.observable_basis_dim_exact == 9
    @test occursin("CONVENTIONS.md (u)", f3.source_locator)

    z6 = records["Z/6Z"]
    @test z6.residue_qudit_dims == [2, 3]
    @test z6.hilbert_dim_exact == 6
    @test z6.label_group_order_exact == 36
    @test z6.observable_basis_dim_exact == 36
    @test occursin("23_spec_z6_residue_qudit_factorisation.tex", z6.source_locator)

    f3xf3 = records["F_3xF_3"]
    @test f3xf3.residue_qudit_dims == [3, 3]
    @test f3xf3.hilbert_dim_exact == 9
    @test f3xf3.label_group_order_exact == 81
    @test f3xf3.observable_basis_dim_exact == 81
    @test occursin("40_product_field_spectrum_qudit_stabilizers.tex", f3xf3.source_locator)

    zero = records["zero_ring"]
    @test zero.status == "not_applicable_until_layer_semantics"
    @test zero.layer == "residue"
    @test !(:residue_qudit_dims in propertynames(zero))
    @test !(:hilbert_dim_exact in propertynames(zero))
    @test occursin("zero_ring_quantization_policy", zero.obstruction)

    blocked = records["Z/4Z"]
    @test blocked.status == "blocked"
    @test !(:residue_qudit_dims in propertynames(blocked))
    @test !(:hilbert_dim_exact in propertynames(blocked))
    @test blocked.obstruction == "missing_certified_maximal_ideal_decomposition_in_this_slice"

    dual_blocked = records["F_3[e]/(e^2)"]
    @test dual_blocked.status == "blocked"
    @test !(:residue_qudit_dims in propertynames(dual_blocked))
    @test !(:hilbert_dim_exact in propertynames(dual_blocked))

    @test_throws ArgumentError finite_ring_residue_quantization_record(
        "empty",
        Int[];
        source_locator="CONVENTIONS.md (u)",
    )
    @test_throws ArgumentError finite_ring_blocked_residue_quantization_record(
        "bad",
        "obstruction";
        status="available",
    )
end

@testset "finite ring database thickened Frobenius quantization records" begin
    root = project_root()
    conventions = read(joinpath(root, "CONVENTIONS.md"), String)
    @test occursin(
        "finite_ring_db.thickened_frobenius_quantization_helper_scope = mvp_source_backed_only",
        conventions,
    )
    @test occursin("Frobenius-ring recognizer", conventions)

    records = Dict(finite_ring_mvp_thickened_frobenius_quantization_records())
    @test Set(keys(records)) == Set(first.(finite_ring_mvp_examples()))

    dual_f3 = records["F_3[e]/(e^2)"]
    @test dual_f3.name == "F_3[e]/(e^2)"
    @test dual_f3.layer == "thickened_frobenius"
    @test dual_f3.status == "available"
    @test dual_f3.hilbert_dim_exact == 9
    @test dual_f3.label_group_order_exact == 81
    @test dual_f3.observable_basis_dim_exact == 81
    @test occursin("36_nilpotent_thickening_weyl_fields.tex", dual_f3.source_locator)
    @test occursin("AQM-36", dual_f3.source_locator)

    z9 = records["Z/9Z"]
    @test z9.layer == "thickened_frobenius"
    @test z9.status == "blocked"
    @test z9.obstruction == "missing_certified_generating_character_in_this_slice"
    @test !(:hilbert_dim_exact in propertynames(z9))
    @test !(:label_group_order_exact in propertynames(z9))
    @test !(:observable_basis_dim_exact in propertynames(z9))

    z4 = records["Z/4Z"]
    @test z4.status == "blocked"
    @test !(:hilbert_dim_exact in propertynames(z4))
    @test !(:label_group_order_exact in propertynames(z4))
    @test !(:observable_basis_dim_exact in propertynames(z4))

    f3 = records["F_3"]
    @test f3.status == "blocked"
    @test f3.obstruction == "missing_thickened_frobenius_policy_in_this_slice"
    @test !(:hilbert_dim_exact in propertynames(f3))

    zero = records["zero_ring"]
    @test zero.status == "not_applicable_until_layer_semantics"
    @test zero.layer == "thickened_frobenius"
    @test !(:hilbert_dim_exact in propertynames(zero))
    @test !(:label_group_order_exact in propertynames(zero))
    @test !(:observable_basis_dim_exact in propertynames(zero))
    @test occursin("zero_ring_quantization_policy", zero.obstruction)

    @test_throws ArgumentError finite_ring_thickened_frobenius_quantization_record(
        "bad",
        1;
        source_locator="report/sections/36_nilpotent_thickening_weyl_fields.tex",
    )
    @test_throws ArgumentError finite_ring_thickened_frobenius_quantization_record(
        "bad",
        9;
        source_locator="",
    )
    @test_throws ArgumentError finite_ring_thickened_frobenius_quantization_record(
        "",
        9;
        source_locator="report/sections/36_nilpotent_thickening_weyl_fields.tex",
    )
    @test_throws ArgumentError finite_ring_thickened_frobenius_quantization_record(
        "bad",
        9;
        source_locator="report/sections/36_nilpotent_thickening_weyl_fields.tex",
        construction="",
    )
    @test_throws ArgumentError finite_ring_blocked_thickened_frobenius_quantization_record(
        "bad",
        "",
    )
    @test_throws ArgumentError finite_ring_blocked_thickened_frobenius_quantization_record(
        "bad",
        "obstruction";
        status="available",
    )
end

@testset "finite ring database prime-field Weyl matrix artifacts" begin
    root = project_root()
    conventions = read(joinpath(root, "CONVENTIONS.md"), String)
    @test occursin(
        "finite_ring_db.prime_field_weyl_matrix_materialization_helper_scope",
        conventions,
    )

    source = "report/sections/22_prime_field_arithmetic_fields_qudit_paulis.tex (AQM-22 L3)"
    artifact = finite_ring_prime_field_weyl_matrix_materialization(
        3;
        matrix_dump_threshold=3,
        source_locator=source,
    )

    @test artifact.layer == "matrix_artifact"
    @test artifact.status == "available"
    @test artifact.base_layer == "residue"
    @test artifact.field_size == 3
    @test artifact.hilbert_dim_exact == 3
    @test artifact.matrix_count_exact == 9
    @test artifact.cyclotomic_encoding == "zero_or_exponent_mod_p"
    @test length(artifact.matrix_payload.matrices) == 9
    @test all(getfield(artifact.checks, key) for key in keys(artifact.checks))
    @test startswith(artifact.artifact_id, "matrix_artifact:")
    @test startswith(artifact.artifact_path, "matrix_artifacts/")
    @test endswith(artifact.artifact_path, ".json")
    @test artifact.artifact_path ==
          finite_ring_prime_field_weyl_matrix_materialization(
        3;
        matrix_dump_threshold=3,
        source_locator=source,
    ).artifact_path

    w10 = only(filter(
        matrix -> matrix.q == 1 && matrix.m == 0,
        artifact.matrix_payload.matrices,
    ))
    @test w10.row_index_by_column == [2, 3, 1]

    w01 = only(filter(
        matrix -> matrix.q == 0 && matrix.m == 1,
        artifact.matrix_payload.matrices,
    ))
    @test w01.row_index_by_column == [1, 2, 3]
    @test w01.phase_exponent_by_column == [0, 1, 2]

    blocked = finite_ring_prime_field_weyl_matrix_materialization(
        5;
        matrix_dump_threshold=3,
        source_locator=source,
    )
    @test blocked.status == "blocked"
    @test blocked.obstruction == "matrix_dump_threshold_exceeded"
    @test blocked.checks == (threshold=false,)
    @test !(:matrix_payload in propertynames(blocked))
    @test !(:matrices in propertynames(blocked))
    @test !(:artifact_path in propertynames(blocked))

    @test_throws ArgumentError finite_ring_prime_field_weyl_matrix_materialization(
        4;
        matrix_dump_threshold=4,
        source_locator=source,
    )
    @test_throws ArgumentError finite_ring_prime_field_weyl_matrix_materialization(
        3;
        matrix_dump_threshold=1,
        source_locator=source,
    )
end

@testset "finite ring database build CLI argument validation" begin
    help = _frdb_build_cli_result("--help")
    @test help.ok
    @test occursin("Usage:", help.stdout)
    @test occursin("--force", help.stdout)
    @test occursin("no-overwrite", help.stdout)

    unknown = _frdb_build_cli_result("--unknown")
    @test !unknown.ok
    @test occursin("unknown flag", unknown.stderr)

    positional = _frdb_build_cli_result("runs/not-a-flag")
    @test !positional.ok
    @test occursin("positional arguments are not accepted", positional.stderr)
end

@testset "finite ring database build CLI run-bundle guard" begin
    root = project_root()
    slug = _frdb_temp_slug("missing-readme")
    run_dir = joinpath(root, "runs", slug)
    db_path = joinpath(run_dir, "data", "finite_rings.sqlite")

    try
        mkpath(run_dir)
        result = _frdb_build_cli_result("--run", "runs/$(slug)")
        @test !result.ok
        @test occursin("missing run bundle README", result.stderr)
        @test !isdir(joinpath(run_dir, "data"))
        @test !isfile(db_path)
    finally
        rm(run_dir; recursive=true, force=true)
    end
end

@testset "finite ring database build CLI valid run" begin
    sqlite3_path = Sys.which("sqlite3")
    if sqlite3_path === nothing
        @test_skip sqlite3_path !== nothing
    else
        root = project_root()
        slug = _frdb_temp_slug("valid")
        run_dir = joinpath(root, "runs", slug)
        db_path = joinpath(run_dir, "data", "finite_rings.sqlite")

        try
            mkpath(run_dir)
            write(joinpath(run_dir, "README.md"), "# Temporary finite-ring CLI test\n")

            result = _frdb_build_cli_result(
                "--run", "runs/$(slug)",
                "--max-order", "15",
                "--sources", "manual-examples",
            )
            @test result.ok
            if result.ok
                @test isfile(db_path)
                @test strip(
                    _sqlite3_test_output(
                        sqlite3_path,
                        db_path,
                        "SELECT COUNT(*) FROM build_run;",
                    ),
                ) == "1"
                @test strip(
                    _sqlite3_test_output(
                        sqlite3_path,
                        db_path,
                        "SELECT COUNT(*) FROM ring;",
                    ),
                ) == "0"
                @test strip(
                    _sqlite3_test_output(
                        sqlite3_path,
                        db_path,
                        "SELECT run_id || '|' || run_path FROM build_run;",
                    ),
                ) == "$(slug)|runs/$(slug)"
            end
        finally
            rm(run_dir; recursive=true, force=true)
        end
    end
end

@testset "finite ring database build CLI rerun policy" begin
    sqlite3_path = Sys.which("sqlite3")
    if sqlite3_path === nothing
        @test_skip sqlite3_path !== nothing
    else
        root = project_root()
        slug = _frdb_temp_slug("rerun-policy")
        run_dir = joinpath(root, "runs", slug)
        db_path = joinpath(run_dir, "data", "finite_rings.sqlite")
        readme_path = joinpath(run_dir, "README.md")
        keep_path = joinpath(run_dir, "data", "keep.txt")

        try
            mkpath(run_dir)
            write(readme_path, "# Temporary finite-ring rerun policy test\n")

            first = _frdb_build_cli_result("--run", "runs/$(slug)")
            @test first.ok
            if first.ok
                @test isfile(db_path)
                @test strip(
                    _sqlite3_test_output(
                        sqlite3_path,
                        db_path,
                        "SELECT COUNT(*) FROM build_run WHERE run_id='$(slug)';",
                    ),
                ) == "1"
            end

            write(keep_path, "preserve sibling data artifact\n")

            second = _frdb_build_cli_result("--run", "runs/$(slug)")
            @test !second.ok
            @test occursin("existing SQLite database", second.stderr)
            @test occursin("no-overwrite", second.stderr)
            @test strip(
                _sqlite3_test_output(
                    sqlite3_path,
                    db_path,
                    "SELECT COUNT(*) FROM build_run WHERE run_id='$(slug)';",
                ),
            ) == "1"

            forced = _frdb_build_cli_result("--run", "runs/$(slug)", "--force")
            @test forced.ok
            if forced.ok
                @test isfile(db_path)
                @test isfile(readme_path)
                @test read(keep_path, String) == "preserve sibling data artifact\n"
                @test strip(
                    _sqlite3_test_output(
                        sqlite3_path,
                        db_path,
                        "SELECT COUNT(*) FROM build_run;",
                    ),
                ) == "1"
                @test strip(
                    _sqlite3_test_output(
                        sqlite3_path,
                        db_path,
                        "SELECT COUNT(*) FROM build_run WHERE run_id='$(slug)';",
                    ),
                ) == "1"
            end
        finally
            rm(run_dir; recursive=true, force=true)
        end
    end
end

@testset "finite ring database audit CLI argument validation" begin
    help = _frdb_audit_cli_result("--help")
    @test help.ok
    @test occursin("Usage:", help.stdout)
    @test occursin("--db", help.stdout)

    missing = _frdb_audit_cli_result()
    @test !missing.ok
    @test occursin("--db <path> is required", missing.stderr)

    positional = _frdb_audit_cli_result("runs/not-a-flag")
    @test !positional.ok
    @test occursin("positional arguments are not accepted", positional.stderr)
end

@testset "finite ring database audit CLI canonical JSON checks" begin
    sqlite3_path = Sys.which("sqlite3")
    if sqlite3_path === nothing
        @test_skip sqlite3_path !== nothing
    else
        root = project_root()
        slug = _frdb_temp_slug("audit-json")
        run_dir = joinpath(root, "runs", slug)
        db_path = joinpath(run_dir, "data", "finite_rings.sqlite")

        try
            mkpath(run_dir)
            write(joinpath(run_dir, "README.md"), "# Temporary finite-ring audit CLI test\n")

            build = _frdb_build_cli_result("--run", "runs/$(slug)")
            @test build.ok
            if build.ok
                pass = _frdb_audit_cli_result("--db", db_path)
                @test pass.ok
                @test occursin("finite_ring_db_audit.jl: ok", pass.stdout)
                @test occursin("json_cells=2", pass.stdout)

                malformed_update = _sqlite3_test_result(
                    sqlite3_path,
                    db_path,
                    """
                    UPDATE build_run
                    SET scope_json = '{"a":';
                    """,
                )
                @test malformed_update.ok
                malformed = _frdb_audit_cli_result("--db", db_path)
                @test !malformed.ok
                @test occursin("build_run", malformed.stderr)
                @test occursin("scope_json", malformed.stderr)
                @test occursin("malformed JSON", malformed.stderr)

                noncanonical_update = _sqlite3_test_result(
                    sqlite3_path,
                    db_path,
                    """
                    UPDATE build_run
                    SET scope_json = '{"b":1,"a":2}';
                    """,
                )
                @test noncanonical_update.ok
                noncanonical = _frdb_audit_cli_result("--db", db_path)
                @test !noncanonical.ok
                @test occursin("build_run", noncanonical.stderr)
                @test occursin("scope_json", noncanonical.stderr)
                @test occursin("noncanonical JSON", noncanonical.stderr)
                @test occursin("expected canonical form", noncanonical.stderr)
            end
        finally
            rm(run_dir; recursive=true, force=true)
        end
    end
end

@testset "finite ring database audit semantic populated checks" begin
    sqlite3_path = Sys.which("sqlite3")
    if sqlite3_path === nothing
        @test_skip sqlite3_path !== nothing
    else
        empty_object = _frdb_sql_json(Dict{String,Any}())
        empty_array = _frdb_sql_json(Any[])

        function audit_fixture(sql)
            mktempdir() do dir
                db_path = joinpath(dir, "finite_rings.sqlite")
                migrate_finite_ring_database_schema!(db_path; sqlite3_path=sqlite3_path)
                insert = _sqlite3_test_result(sqlite3_path, db_path, "PRAGMA foreign_keys=ON;\n$(sql)")
                @test insert.ok
                insert.ok || error("fixture insert failed: $(insert.stderr)")
                return _frdb_audit_cli_result("--db", db_path)
            end
        end

        build_run_sql = """
        INSERT INTO build_run
          (run_id, run_path, command_line, tool_versions_json, created_utc, scope_json)
        VALUES ('run:test', 'runs/test', 'cmd', $(empty_object), '2099-01-01T00:00:00Z', $(empty_object));
        """
        source_sql = """
        INSERT INTO source
          (source_id, citation_key, local_path, retrieved_date, license_status)
        VALUES ('src:test', 'Fixture source', 'references/finite_ring_database/SOURCES.md',
                '2099-01-01', 'local_fixture');
        """
        presentation_sql = """
        INSERT INTO presentation
          (presentation_id, source_id, run_id, presentation_type, payload_json, parsed_status)
        VALUES ('pres:canonical', 'src:test', 'run:test', 'manual', $(empty_object), 'parsed');
        """
        ring_sql = """
        INSERT INTO ring
          (ring_id, canonical_presentation_id, order_exact, characteristic_exact,
           additive_invariants_json, is_commutative, has_one, local_status,
           reduced_status, field_status, frobenius_status,
           generating_character_status, audit_status)
        VALUES ('ring:test', 'pres:canonical', '2', '2', $(empty_array), 1, 1,
                'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'pending');
        INSERT INTO ring_presentation_link
          (ring_id, presentation_id, link_status)
        VALUES ('ring:test', 'pres:canonical', 'canonical');
        """
        partial_batch_sql = """
        INSERT INTO enumeration_batch
          (batch_id, run_id, source_id, scope_json, completeness_status,
           input_count_exact, certified_ring_count_exact, unresolved_count_exact)
        VALUES ('batch:test', 'run:test', 'src:test', $(empty_object), 'partial', '1', '1', '0');
        """
        available_quantization_sql = """
        INSERT INTO quantization
          (quantization_id, ring_id, layer, status, hilbert_dim_exact,
           label_group_order_exact, observable_basis_dim_exact)
        VALUES ('quant:test', 'ring:test', 'residue', 'available', '2', '4', '4');
        """

        function populated_fixture_sql(; batch_sql=partial_batch_sql, quantization_sql=available_quantization_sql, extra_sql="")
            return build_run_sql * source_sql * presentation_sql * ring_sql *
                   batch_sql * quantization_sql * extra_sql
        end

        missing_source = audit_fixture(
            build_run_sql *
            """
            INSERT INTO presentation
              (presentation_id, run_id, presentation_type, payload_json, parsed_status)
            VALUES ('pres:missing-source', 'run:test', 'manual', $(empty_object), 'parsed');
            """,
        )
        @test !missing_source.ok
        @test occursin("presentation", missing_source.stderr)
        @test occursin("source_id", missing_source.stderr)

        invalid_source = audit_fixture(
            build_run_sql *
            """
            INSERT INTO source
              (source_id, citation_key, retrieved_date, license_status)
            VALUES ('src:bad', 'Fixture source', '2099-01-01', '');
            """,
        )
        @test !invalid_source.ok
        @test occursin("source", invalid_source.stderr)
        @test occursin("license_status", invalid_source.stderr)

        no_cert = audit_fixture(
            populated_fixture_sql(
                extra_sql="""
                INSERT INTO presentation
                  (presentation_id, source_id, run_id, presentation_type, payload_json, parsed_status)
                VALUES ('pres:duplicate', 'src:test', 'run:test', 'manual', $(empty_object), 'parsed');
                INSERT INTO ring_presentation_link
                  (ring_id, presentation_id, link_status)
                VALUES ('ring:test', 'pres:duplicate', 'merged');
                """,
            ),
        )
        @test !no_cert.ok
        @test occursin("ring_presentation_link", no_cert.stderr)
        @test occursin("certificate_id", no_cert.stderr)

        bad_cert = audit_fixture(
            populated_fixture_sql(
                extra_sql="""
                INSERT INTO presentation
                  (presentation_id, source_id, run_id, presentation_type, payload_json, parsed_status)
                VALUES ('pres:bad-cert', 'src:test', 'run:test', 'manual', $(empty_object), 'parsed');
                INSERT INTO isomorphism_certificate
                  (certificate_id, presentation_id_a, presentation_id_b, verdict,
                   certificate_type, certificate_json, tool, checked_by, checker_result)
                VALUES ('iso:bad', 'pres:canonical', 'pres:bad-cert', 'unknown',
                        'fixture', $(empty_object), 'test', 'test', 'failed');
                INSERT INTO ring_presentation_link
                  (ring_id, presentation_id, link_status, certificate_id)
                VALUES ('ring:test', 'pres:bad-cert', 'merged', 'iso:bad');
                """,
            ),
        )
        @test !bad_cert.ok
        @test occursin("checker_result=ok", bad_cert.stderr)
        @test occursin("verdict=isomorphic", bad_cert.stderr)

        no_quantization = audit_fixture(populated_fixture_sql(quantization_sql=""))
        @test !no_quantization.ok
        @test occursin("quantization", no_quantization.stderr)

        no_batch = audit_fixture(populated_fixture_sql(batch_sql=""))
        @test !no_batch.ok
        @test occursin("enumeration_batch", no_batch.stderr)

        blocked_without_obstruction = audit_fixture(
            populated_fixture_sql(
                quantization_sql="""
                INSERT INTO quantization
                  (quantization_id, ring_id, layer, status)
                VALUES ('quant:blocked', 'ring:test', 'residue', 'blocked');
                """,
            ),
        )
        @test !blocked_without_obstruction.ok
        @test occursin("quantization", blocked_without_obstruction.stderr)
        @test occursin("obstruction", blocked_without_obstruction.stderr)

        available_missing_dims = audit_fixture(
            populated_fixture_sql(
                quantization_sql="""
                INSERT INTO quantization
                  (quantization_id, ring_id, layer, status, hilbert_dim_exact,
                   label_group_order_exact)
                VALUES ('quant:missing-dims', 'ring:test', 'residue', 'available', '2', '4');
                """,
            ),
        )
        @test !available_missing_dims.ok
        @test occursin("quantization", available_missing_dims.stderr)
        @test occursin("hilbert_dim_exact", available_missing_dims.stderr)

        incomplete_claim = audit_fixture(
            populated_fixture_sql(
                batch_sql="""
                INSERT INTO enumeration_batch
                  (batch_id, run_id, source_id, scope_json, completeness_status,
                   input_count_exact, certified_ring_count_exact, unresolved_count_exact,
                   reconciliation_json)
                VALUES ('batch:complete', 'run:test', 'src:test', $(empty_object),
                        'complete', '1', '1', '1', $(empty_object));
                """,
            ),
        )
        @test !incomplete_claim.ok
        @test occursin("enumeration_batch", incomplete_claim.stderr)
        @test occursin("unresolved_count_exact", incomplete_claim.stderr)

        valid = audit_fixture(populated_fixture_sql())
        @test valid.ok
        @test occursin("finite_ring_db_audit.jl: ok", valid.stdout)
    end
end

@testset "finite ring database smoke build registration" begin
    root = project_root()
    run_slug = "2026-05-26-finite-ring-database"
    run_path = "runs/$(run_slug)"
    audit_db_path = "$(run_path)/data/finite_rings.sqlite"

    run_all = read(joinpath(root, "scripts", "run_all.jl"), String)
    @test occursin("finite_ring_db_build_smoke", run_all)
    @test occursin("finite_ring_db_audit_smoke", run_all)
    @test occursin("arithmetic/finite_ring_db_audit.jl", run_all)
    @test occursin(audit_db_path, run_all)
    @test occursin(run_path, run_all)
    @test occursin("--force", run_all)

    index = read(joinpath(root, "INDEX.md"), String)
    @test occursin("`$(run_path)/`", index)
    @test occursin("scripts/arithmetic/finite_ring_db_build.jl", index)
    @test occursin("scripts/arithmetic/finite_ring_db_audit.jl", index)
    @test occursin("writes local `data/finite_rings.sqlite`", index)

    readme = read(joinpath(root, run_path, "README.md"), String)
    @test occursin("finite_rings.sqlite", readme)
    @test occursin("finite_ring_db_audit.jl", readme)
    @test occursin("canonical JSON", readme)
    @test occursin("schema-only", readme)

    gitignore = read(joinpath(root, ".gitignore"), String)
    @test occursin("runs/**/data/finite_rings.sqlite", gitignore)
end

@testset "algebraic toric-code ghost boundary supercharge" begin
    for k in 2:4
        summary = toric_supercharge_summary(k)
        @test summary.nqubits == 2k^2
        @test summary.nchecks == 2k^2
        @test summary.max_check_weight == 4
        @test summary.all_projectors_commute
        @test summary.all_checks_square_to_identity
        @test summary.stabilizer_rank == 2k^2 - 2
        @test summary.independent_check_relations == 2
        @test summary.logical_qubits == 2
        @test summary.code_dim_exact == "4"
        @test summary.h0_dim_exact == "4"
        @test summary.q_square_certificate
        @test summary.anticommutator_certificate
        @test summary.degree_zero_homology_matches_code
    end
end

@testset "toric chain complex and ghost checks agree" begin
    for k in 2:4
        summary = toric_chain_ghost_unification_summary(k)
        @test summary.nvertices == k^2
        @test summary.nedges == 2k^2
        @test summary.nfaces == k^2
        @test summary.boundary_square_zero
        @test summary.star_masks_match_boundary_one
        @test summary.plaquette_masks_match_boundary_two
        @test summary.rank_boundary_one == k^2 - 1
        @test summary.rank_boundary_two == k^2 - 1
        @test summary.h1_dim == 2
        @test summary.code_dim_from_h1_exact == "4"
        @test summary.cellular_supercharge_square_zero
        @test summary.cellular_middle_cohomology_dim == 2
        @test summary.cellular_middle_cohomology_basis_count_exact == "4"
        @test summary.cochain_cocycle_count_exact == string(BigInt(1) << (2k^2 - (k^2 - 1)))
        @test summary.cochain_coboundary_count_exact == string(BigInt(1) << (k^2 - 1))
        @test summary.css_commutation_from_boundary
        @test summary.ghost_checks_from_chain_complex
    end
end

@testset "symplectic CSS bridge over prime fields" begin
    for k in 2:4, p in (2, 3, 5)
        boundary_one, boundary_two = oriented_toric_boundary_matrices(k, p)
        @test all(==(0), matmul_modp(boundary_one, boundary_two, p))
        @test css_symplectic_isotropic(boundary_one, boundary_two, p)

        summary = symplectic_css_bridge_summary(k, p)
        @test summary.boundary_square_zero
        @test summary.css_isotropic
        @test summary.rank_boundary_one == k^2 - 1
        @test summary.rank_boundary_two == k^2 - 1
        @test summary.h1_dim == 2
        @test summary.symplectic_stabilizer_rank == 2k^2 - 2
        @test summary.encoded_qudits == 2
        @test summary.encoded_hilbert_dimension_exact == string(BigInt(p)^2)
        @test summary.chain_count_matches_symplectic_count
    end
end

@testset "CSS supercharge symplectic dictionary" begin
    hx, hz = steane_css_matrices()
    steane = css_supercharge_dictionary_summary(hx, hz, 2)
    @test steane.css_isotropic
    @test steane.n == 7
    @test steane.rank_x == 3
    @test steane.rank_z == 3
    @test steane.stabilizer_rank == 6
    @test steane.encoded_qudits == 1
    @test steane.code_dimension_exact == "2"
    @test steane.logical_symplectic_dimension == 2
    @test steane.l_perp_dimension == 8
    @test steane.generator_ghost_count == 6
    @test steane.basis_free_projective_ghost_count_exact == "63"
    @test steane.q_square_certificate
    @test steane.anticommutator_certificate
    @test steane.h0_matches_stabilizer_code

    hx3, hz3 = qutrit_css_toy_matrices()
    qutrit = css_supercharge_dictionary_summary(hx3, hz3, 3)
    @test qutrit.css_isotropic
    @test qutrit.n == 3
    @test qutrit.stabilizer_rank == 2
    @test qutrit.encoded_qudits == 1
    @test qutrit.code_dimension_exact == "3"
    @test qutrit.logical_symplectic_dimension == 2
    @test qutrit.basis_free_projective_ghost_count_exact == "4"
end

@testset "Steane molecular supercharge data" begin
    data = steane_binary_space_rows()
    h = data.h
    @test h == [
        1 1 1 1 0 0 0
        1 1 0 0 1 1 0
        1 0 1 0 1 0 1
    ]
    @test all(==(0), matmul_modp(h, transpose(h), 2))
    @test length(data.d_space) == 8
    @test length(data.c_space) == 16
    @test data.logical_word == [0, 0, 0, 0, 1, 1, 1]

    summary = steane_molecular_summary()
    @test summary.d_subset_c
    @test summary.logical_word_in_c
    @test summary.logical_word_not_in_d
    @test summary.stabilizer_rank == 6
    @test summary.l_dim == 6
    @test summary.l_size == 64
    @test summary.l_perp_dim == 8
    @test summary.l_perp_size == 256
    @test summary.logical_symplectic_dim == 2
    @test summary.logical_pauli_classes == 4
    @test summary.logical_pairing_x_z == 1
    @test summary.physical_hilbert_dim == 128
    @test summary.ghost_fock_dim == 64
    @test summary.full_ghost_hilbert_dim == 8192
    @test summary.code_dim == 2
    @test summary.syndrome_count == 64
    @test summary.nonzero_syndrome_count == 63
    @test summary.syndrome_block_dim == 2
    @test summary.full_q_cohomology_dim == 128
    @test summary.degree_zero_cohomology_dim == 2
    @test summary.q_square_certificate
    @test summary.anticommutator_certificate
    @test summary.codewords_match_two_cosets

    @test [row.cohomology_dim for row in steane_cohomology_by_degree()] ==
          [2, 12, 30, 40, 30, 12, 2]
end

@testset "Steane Clifford Koszul morphisms" begin
    summary = steane_clifford_morphism_summary()
    @test summary.hadamard_maps_l_to_l
    @test summary.hadamard_image_rank == 6
    @test summary.hadamard_exact_same_q_after_ghost_swap
    @test summary.hadamard_logical_x_image == "Zbar"
    @test summary.hadamard_logical_z_image == "Xbar"
    @test summary.phase_maps_l_to_l
    @test summary.phase_image_rank == 6
    @test summary.phase_chain_isomorphism_to_image_presentation
    @test summary.phase_same_q_only_after_homotopy_retract
    @test summary.phase_logical_x_image == "Xbar+Zbar"
    @test summary.phase_logical_z_image == "Zbar"
    @test summary.nonzero_syndrome_blocks == 63
    @test summary.nonzero_syndrome_blocks_contractible
    @test summary.zero_syndrome_cohomology_dim_by_degree == "2;12;30;40;30;12;2"
    @test summary.physical_h0_dim == 2
    @test summary.full_cohomology_dim == 128

    rows = steane_clifford_morphism_rows()
    @test length(rows) == 12
    @test rows[1].morphism == "transversal_H"
    @test rows[1].source == "X1"
    @test rows[1].image == "0000000|1111000"
    @test rows[1].image_basis_coordinates == "Z1"
    @test rows[2].morphism == "transversal_P"
    @test rows[2].source == "X1"
    @test rows[2].image == "1111000|1111000"
    @test rows[2].image_basis_coordinates == "X1+Z1"
end

@testset "Steane all-Clifford ghost Gaussian theorem data" begin
    summary = steane_all_clifford_generator_summary()
    @test summary.standard_clifford_generator_gates == 56
    @test summary.hadamard_generator_gates == 7
    @test summary.phase_generator_gates == 7
    @test summary.cnot_generator_gates == 42
    @test summary.generator_image_rows == 336
    @test summary.all_generator_images_rank_six
    @test summary.rank_six_gate_count == 56
    @test summary.all_generator_images_isotropic
    @test summary.isotropic_gate_count == 56
    @test summary.transported_presentation_chain_map == "U_tensor_identity_on_ghosts"
    @test summary.theorem_extends_to_all_clifford_words_by_generation
    @test summary.elementary_gl6_ghost_generators == 45
    @test summary.row_swap_ghost_generators == 15
    @test summary.row_shear_ghost_generators == 30
    @test summary.shear_projector_identities_checked == 1920
    @test summary.shear_projector_identities_hold
    @test summary.presentation_change_requires_operator_coefficients
    @test summary.zero_syndrome_shear_reduces_to_scalar_exterior_gl
    @test summary.no_bogoliubov_mixing_needed

    images = steane_all_clifford_generator_rows()
    @test length(images) == 336
    @test images[1].gate == "H1"
    @test images[1].source == "X1"
    @test images[1].signed_image == "+0111000|1000000"
    @test all(row -> row.image_list_rank == 6, images)
    @test all(row -> row.image_list_isotropic, images)

    ghosts = steane_ghost_gaussian_elementary_rows()
    @test length(ghosts) == 45
    @test count(row -> row.operation == "row_swap", ghosts) == 15
    @test count(row -> row.operation == "row_shear", ghosts) == 30
    @test all(row -> row.identity_holds, ghosts)
    @test any(row -> row.operation == "row_shear" &&
                     row.projector_identity == "P(S1*S2)=P(S1)+S1*P(S2)",
              ghosts)
end

@testset "Arithmetic quantum field examples" begin
    rows = arithmetic_quantum_field_summary_rows()
    by_name = Dict(row.example => row for row in rows)
    @test length(rows) == 11

    finite = by_name["finite_set_3_full"]
    @test finite.scalar_basis_dim == 3
    @test finite.scalar_pairing_rank == 3
    @test finite.field_phase_dim == 6
    @test finite.radical_dim == 0
    @test finite.reduced_weyl_labels_exact == "729"
    @test finite.hilbert_dim_exact == "27"
    @test finite.observable_basis_dim_exact == "729"
    @test finite.nondegenerate

    linear = by_name["vector_space_F3_linear"]
    @test linear.scalar_basis_dim == 1
    @test linear.scalar_pairing_rank == 1
    @test linear.reduced_weyl_labels_exact == "9"
    @test linear.hilbert_dim_exact == "3"

    affine = by_name["vector_space_F3_affine"]
    @test affine.scalar_basis_dim == 2
    @test affine.scalar_pairing_rank == 1
    @test affine.field_phase_dim == 4
    @test affine.radical_dim == 2
    @test affine.radical_labels_exact == "9"
    @test !affine.nondegenerate

    plane = by_name["affine_plane_F3_linear"]
    @test plane.scalar_pairing_rank == 0
    @test plane.symplectic_rank == 0
    @test plane.radical_dim == 4
    @test plane.reduced_weyl_labels_exact == "1"
    @test !plane.nondegenerate

    parabola = by_name["parabola_F3_degree_le_1"]
    @test parabola.scalar_basis_dim == 3
    @test parabola.scalar_pairing_rank == 3
    @test parabola.field_phase_dim == 6
    @test parabola.reduced_weyl_labels_exact == "729"
    @test parabola.nondegenerate

    basis_rows = arithmetic_quantum_field_basis_rows()
    @test any(row -> row.example == "parabola_F3_degree_le_1" &&
                     row.row_kind == "basis_values" &&
                     row.label == "y" &&
                     row.values == "0 1 1",
              basis_rows)
    @test any(row -> row.example == "vector_space_F3_affine" &&
                     row.row_kind == "scalar_gram_row" &&
                     row.label == "1" &&
                     row.values == "0 0",
              basis_rows)
end

@testset "Projective-line sheaf field examples" begin
    @test p1_rational_point_labels(3) == ["[1:0]", "[0:1]", "[1:1]", "[2:1]"]
    @test p1_od_basis_labels(2) == ["X^2", "XY", "Y^2"]
    @test p1_od_evaluation_matrix(2, 3) == [
        1 0 1 1
        0 0 1 2
        0 1 1 1
    ]

    rows = projective_line_sheaf_field_summary_rows(; p=3, max_degree=4)
    by_degree = Dict(row.d => row for row in rows)
    @test length(rows) == 5

    @test by_degree[0].scalar_section_dim == 1
    @test by_degree[0].scalar_pairing_rank == 1
    @test by_degree[0].nondegenerate

    @test by_degree[1].evaluation_rank == 2
    @test by_degree[1].scalar_pairing_rank == 0
    @test by_degree[1].radical_dim == 4
    @test by_degree[1].reduced_weyl_labels_exact == "1"
    @test !by_degree[1].nondegenerate

    @test by_degree[2].scalar_section_dim == 3
    @test by_degree[2].scalar_pairing_rank == 3
    @test by_degree[2].hilbert_dim_exact == "27"
    @test by_degree[2].nondegenerate

    @test by_degree[4].scalar_section_dim == 5
    @test by_degree[4].evaluation_rank == 4
    @test by_degree[4].evaluation_kernel_dim == 1
    @test by_degree[4].radical_dim == 2
    @test by_degree[4].evaluation_kernel_labels_exact == "9"
    @test !by_degree[4].nondegenerate

    basis_rows = projective_line_sheaf_field_basis_rows(; p=3, max_degree=4)
    @test any(row -> row.example == "P1_F3_O2" &&
                     row.row_kind == "scalar_gram_row" &&
                     row.label == "XY" &&
                     row.values == "0 2 0",
              basis_rows)

    stalk_rows = projective_line_stalk_rows(; p=3, max_degree=4)
    @test length(stalk_rows) == 60
    point_labels = p1_rational_point_labels(3)
    stalk_by_key = Dict((row.d, row.basis_label, row.point_label) => row for row in stalk_rows)
    for d in 0:4
        values = p1_od_evaluation_matrix(d, 3)
        for (basis_index, basis_label) in enumerate(p1_od_basis_labels(d))
            for (point_index, point_label) in enumerate(point_labels)
                row = stalk_by_key[(d, basis_label, point_label)]
                @test row.residue_value == values[basis_index, point_index]
            end
        end
    end
    @test any(row -> row.d == 2 &&
                     row.point_label == "[1:0]" &&
                     row.local_ring == "F3[u]_(u)" &&
                     row.basis_label == "XY" &&
                     row.germ_in_frame == "u*e_X^(2)" &&
                     row.residue_value == 0,
              stalk_rows)
    @test any(row -> row.d == 4 &&
                     row.point_label == "[2:1]" &&
                     row.homogeneous_prime == "(X-2Y)=(X+Y)" &&
                     row.local_ring == "F3[v]_(v-2)" &&
                     row.basis_label == "X^3Y" &&
                     row.germ_in_frame == "v^3*e_Y^(4)" &&
                     row.residue_value == 2,
              stalk_rows)
end
