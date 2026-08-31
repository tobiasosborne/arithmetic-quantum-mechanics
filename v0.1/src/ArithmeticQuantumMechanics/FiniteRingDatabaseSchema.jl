const FINITE_RING_DATABASE_SCHEMA_VERSION = 1

const FINITE_RING_DATABASE_SCHEMA_VERSION_TABLE =
    "finite_ring_database_schema_version"

const FINITE_RING_DATABASE_PRD_TABLE_NAMES = (
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

finite_ring_database_schema_version() = FINITE_RING_DATABASE_SCHEMA_VERSION

finite_ring_database_prd_table_names() = FINITE_RING_DATABASE_PRD_TABLE_NAMES

function finite_ring_database_schema_sql()
    return """
    PRAGMA foreign_keys=ON;

    CREATE TABLE IF NOT EXISTS source (
      source_id TEXT PRIMARY KEY,
      citation_key TEXT NOT NULL,
      local_path TEXT,
      url TEXT,
      doi TEXT,
      retrieved_date TEXT NOT NULL,
      sha256 TEXT,
      license_status TEXT NOT NULL,
      notes TEXT
    );

    CREATE TABLE IF NOT EXISTS build_run (
      run_id TEXT PRIMARY KEY,
      run_path TEXT NOT NULL,
      git_commit TEXT,
      command_line TEXT NOT NULL,
      tool_versions_json TEXT NOT NULL,
      created_utc TEXT NOT NULL,
      scope_json TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS presentation (
      presentation_id TEXT PRIMARY KEY,
      source_id TEXT,
      run_id TEXT NOT NULL,
      presentation_type TEXT NOT NULL,
      presentation_text TEXT,
      payload_json TEXT,
      payload_artifact_path TEXT,
      parsed_status TEXT NOT NULL,
      normalized_hash TEXT,
      FOREIGN KEY(source_id) REFERENCES source(source_id),
      FOREIGN KEY(run_id) REFERENCES build_run(run_id)
    );

    CREATE TABLE IF NOT EXISTS ring (
      ring_id TEXT PRIMARY KEY,
      canonical_presentation_id TEXT NOT NULL,
      order_exact TEXT NOT NULL,
      characteristic_exact TEXT NOT NULL,
      additive_invariants_json TEXT NOT NULL,
      is_commutative INTEGER NOT NULL CHECK(is_commutative IN (0, 1)),
      has_one INTEGER NOT NULL CHECK(has_one IN (0, 1)),
      identity_vector_json TEXT,
      local_status TEXT NOT NULL,
      reduced_status TEXT NOT NULL,
      field_status TEXT NOT NULL,
      product_decomposition_json TEXT,
      maximal_ideals_json TEXT,
      residue_field_sizes_json TEXT,
      nilradical_size_exact TEXT,
      nilpotency_index_exact TEXT,
      frobenius_status TEXT NOT NULL,
      generating_character_status TEXT NOT NULL,
      audit_status TEXT NOT NULL,
      FOREIGN KEY(canonical_presentation_id) REFERENCES presentation(presentation_id)
    );

    CREATE TABLE IF NOT EXISTS ring_presentation_link (
      ring_id TEXT NOT NULL,
      presentation_id TEXT NOT NULL,
      link_status TEXT NOT NULL,
      certificate_id TEXT,
      PRIMARY KEY(ring_id, presentation_id),
      FOREIGN KEY(ring_id) REFERENCES ring(ring_id),
      FOREIGN KEY(presentation_id) REFERENCES presentation(presentation_id),
      FOREIGN KEY(certificate_id) REFERENCES isomorphism_certificate(certificate_id)
    );

    CREATE TABLE IF NOT EXISTS invariant (
      invariant_id TEXT PRIMARY KEY,
      ring_id TEXT,
      presentation_id TEXT,
      invariant_name TEXT NOT NULL,
      invariant_value_json TEXT NOT NULL,
      method TEXT NOT NULL,
      certificate_artifact_path TEXT,
      CHECK(ring_id IS NOT NULL OR presentation_id IS NOT NULL),
      FOREIGN KEY(ring_id) REFERENCES ring(ring_id),
      FOREIGN KEY(presentation_id) REFERENCES presentation(presentation_id)
    );

    CREATE TABLE IF NOT EXISTS isomorphism_certificate (
      certificate_id TEXT PRIMARY KEY,
      presentation_id_a TEXT NOT NULL,
      presentation_id_b TEXT NOT NULL,
      verdict TEXT NOT NULL,
      certificate_type TEXT NOT NULL,
      certificate_json TEXT NOT NULL,
      tool TEXT NOT NULL,
      tool_version TEXT,
      checked_by TEXT NOT NULL,
      checker_result TEXT NOT NULL,
      FOREIGN KEY(presentation_id_a) REFERENCES presentation(presentation_id),
      FOREIGN KEY(presentation_id_b) REFERENCES presentation(presentation_id)
    );

    CREATE TABLE IF NOT EXISTS enumeration_batch (
      batch_id TEXT PRIMARY KEY,
      run_id TEXT NOT NULL,
      source_id TEXT,
      scope_json TEXT NOT NULL,
      completeness_status TEXT NOT NULL,
      input_count_exact TEXT NOT NULL,
      certified_ring_count_exact TEXT NOT NULL,
      unresolved_count_exact TEXT NOT NULL,
      reconciliation_json TEXT,
      FOREIGN KEY(run_id) REFERENCES build_run(run_id),
      FOREIGN KEY(source_id) REFERENCES source(source_id)
    );

    CREATE TABLE IF NOT EXISTS quantization (
      quantization_id TEXT PRIMARY KEY,
      ring_id TEXT NOT NULL,
      layer TEXT NOT NULL,
      status TEXT NOT NULL,
      hilbert_dim_exact TEXT,
      label_group_order_exact TEXT,
      observable_basis_dim_exact TEXT,
      qudit_dims_json TEXT,
      phase_character_json TEXT,
      symplectic_form_json TEXT,
      construction_json TEXT,
      certificate_artifact_path TEXT,
      obstruction TEXT,
      FOREIGN KEY(ring_id) REFERENCES ring(ring_id)
    );

    CREATE TABLE IF NOT EXISTS matrix_artifact (
      artifact_id TEXT PRIMARY KEY,
      quantization_id TEXT NOT NULL,
      artifact_path TEXT NOT NULL,
      sha256 TEXT NOT NULL,
      format TEXT NOT NULL,
      matrix_count_exact TEXT NOT NULL,
      threshold_json TEXT NOT NULL,
      verification_json TEXT NOT NULL,
      FOREIGN KEY(quantization_id) REFERENCES quantization(quantization_id)
    );

    CREATE TABLE IF NOT EXISTS finite_ring_database_schema_version (
      component TEXT PRIMARY KEY,
      version INTEGER NOT NULL
    );

    INSERT OR REPLACE INTO finite_ring_database_schema_version (component, version)
    VALUES ('finite_ring_database', 1);
    """
end

function migrate_finite_ring_database_schema!(
    db_path::AbstractString;
    sqlite3_path=Sys.which("sqlite3"),
)
    sqlite3_path === nothing && error(
        "sqlite3 executable not found; pass sqlite3_path or install sqlite3",
    )

    normalized_db_path = abspath(db_path)
    mkpath(dirname(normalized_db_path))
    _run_finite_ring_database_sqlite3!(
        String(sqlite3_path),
        normalized_db_path,
        finite_ring_database_schema_sql(),
    )

    return (;
        status=:ok,
        db_path=normalized_db_path,
        schema_version=finite_ring_database_schema_version(),
        tables=(
            finite_ring_database_prd_table_names()...,
            FINITE_RING_DATABASE_SCHEMA_VERSION_TABLE,
        ),
    )
end

function _run_finite_ring_database_sqlite3!(sqlite3_path, db_path, sql)
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
        error("sqlite3 schema migration failed for $(db_path): $(sprint(showerror, err))")
    end
    ok && return nothing

    details = strip(String(take!(stderr)))
    isempty(details) && (details = strip(String(take!(stdout))))
    isempty(details) && (details = "sqlite3 exited with a nonzero status")
    error("sqlite3 schema migration failed for $(db_path): $(details)")
end
