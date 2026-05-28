# Finite Commutative Ring Database Population Plan

Status: second-pass implementation plan next to
`docs/finite_commutative_ring_database_prd.md`.

Starting boundary: the current run bundle
`runs/2026-05-26-finite-ring-database/` contains a schema-only
`finite_rings.sqlite` with one `build_run` row and zero `ring`,
`presentation`, `source`, `quantization`, and `isomorphism_certificate` rows.
The CSV review exports are in-memory MVP artifacts and do not populate or read
SQLite. This plan starts from that boundary.

Principle: every step is a 50-200 LOC implementation slice unless it discovers
that the scope must be split. Every step starts with local ground truth, then a
failing invariant, then the smallest green implementation. No step may convert
GAP status counts, source summaries, hashes, or bounded searches into a
catalogue or completeness claim without local provenance and audit evidence.

User-facing success target: the first satisfying database milestone is a
deduplicated, audited list of at least 100 finite commutative associative
unital rings under convention `(an)`, with source-backed presentations,
checked isomorphism links, and enough metadata to inspect/query the list. Unless
Step 01 records a different source-backed order, "first" means nondecreasing
cardinality, then stable canonical ring ID as a deterministic tie-breaker.
More than 100 rings is preferred if the same audited source path naturally
produces them.

## Dependency Chain

Each step depends on the previous step. This linear chain is deliberately more
serial than the likely engineering graph so the database content path remains
auditable.

| Step | Bead | Title | Depends on |
|---|---|---|---|
| 01 | `aqm-rnj` | Freeze population scope and source-rights matrix | none |
| 02 | `aqm-c28` | Add SQLite write transaction helpers | `aqm-rnj` |
| 03 | `aqm-jnf` | Populate source rows from registered manifests | `aqm-c28` |
| 04 | `aqm-8nn` | Persist manual MVP presentation rows | `aqm-jnf` |
| 05 | `aqm-6nq` | Persist canonical ring and invariant rows | `aqm-8nn` |
| 06 | `aqm-z0a` | Persist checked isomorphism certificates and links | `aqm-6nq` |
| 07 | `aqm-ap4` | Persist quantization and obstruction rows | `aqm-z0a` |
| 08 | `aqm-y0k` | Harden audit for populated MVP databases | `aqm-ap4` |
| 09 | `aqm-u20` | Add SQLite-backed exports and CSV comparison | `aqm-y0k` |
| 10 | `aqm-ky3` | Persist audit/build evidence artifacts | `aqm-u20` |
| 11 | `aqm-dh4` | Produce the first populated MVP run bundle | `aqm-ky3` |
| 12 | `aqm-ns9` | Document populated-MVP status without completeness claims | `aqm-dh4` |
| 13 | `aqm-0bm` | Acquire missing bounded-catalogue sources | `aqm-ns9` |
| 14 | `aqm-fr1` | Prototype GAP SmallRing presentation extraction | `aqm-0bm` |
| 15 | `aqm-zke` | Add enumeration-batch completeness contract | `aqm-fr1` |
| 16 | `aqm-450` | Populate audited first-100-or-more ring tranche | `aqm-zke` |
| 17 | `aqm-9yp` | Reconcile first-100-or-more tranche across sources | `aqm-450` |
| 18 | `aqm-057` | Promote first-100-or-more catalogue status | `aqm-9yp` |

## Phase A: Populated MVP Database

The goal of Phase A is a populated, audited SQLite database for the current
manual MVP examples only. It must make no bounded-classification completeness
claim.

## Step 01: Freeze Population Scope and Source-Rights Matrix

Ground truth first:

- Re-read `CONVENTIONS.md` convention `(an)`, the PRD acceptance criteria, the
  finite-ring source manifest, and the current run README.
- Fix the operational meaning of "first 100 rings or more": the default is
  finite commutative associative unital rings sorted by nondecreasing
  cardinality, then canonical ring ID, but this may be replaced by a better
  source-backed ordering only if documented here and in convention `(an)`.
- Classify every planned MVP row source as one of:
  `database_import_allowed`, `manual_transcription_allowed`,
  `verification_only`, `status_metadata_only`, or `not_available`.
- Record the exact local source locator required for every source-backed row.

Red:

- Add a lightweight planning-policy test that fails if the population plan or
  PRD does not state that Nowicki/DML-style sources are not bulk-imported
  unless rights are explicit.
- Add a test or doc guard that fails if the MVP population source matrix omits
  the zero ring, prime fields, `Z/nZ`, dual numbers, or finite products already
  emitted by the review exporter.

Green:

- Add a compact source-rights matrix to the plan or PRD.
- State that Phase A manually persists only rows produced by local constructors
  and local certificate checkers; external catalogue sources are provenance and
  verification unless their import rights are explicit.
- Record the first-100 target as the project-facing success milestone, while
  preserving the smaller populated-MVP run as an intermediate engineering
  checkpoint.

Acceptance:

- The source-rights matrix names each MVP row family, its allowed use, and its
  local source/provenance locator.
- The ordering and acceptance boundary for the first-100-or-more target are
  explicit.
- No code path is allowed to import bulk external catalogue rows yet.

## Step 02: Add SQLite Write Transaction Helpers

Ground truth first:

- Re-read `FiniteRingDatabaseSchema.jl`, `finite_ring_db_build.jl`,
  `finite_ring_db_audit.jl`, and the SQLite source locator.
- Confirm the project still uses the external `sqlite3` executable rather than
  a Julia SQLite package.

Red:

- Add tests showing that a multi-table population operation rolls back on a
  deliberately invalid foreign-key insert.
- Add tests showing canonical SQL text or parameter serialization preserves
  canonical JSON byte strings without shell quoting ambiguity.

Green:

- Add a small internal write helper that executes SQL in a transaction through
  `sqlite3`, enables foreign keys, fails loud on stderr, and does not write
  outside the selected run bundle.
- Keep the helper private or narrowly exported until there is a stable access
  layer policy.

Acceptance:

- A temporary database can atomically insert and roll back test rows.
- Existing schema-only build behavior is unchanged.

## Step 03: Populate Source Rows From Registered Manifests

Ground truth first:

- Re-read `references/finite_ring_database/SOURCES.md` and `INDEX.md`.
- Decide which manifest entries are required for Phase A row provenance and
  which remain optional or prospective.

Red:

- Add an audit fixture where a populated `presentation` row references a
  missing `source_id` and audit fails.
- Add a fixture where a `source` row has no local path, hash, or locator and
  audit fails unless the source is explicitly marked prospective.

Green:

- Add a source-row producer for the finite-ring manifest subset used by Phase
  A.
- Populate `source` rows before presentation rows in the build path.

Acceptance:

- The populated MVP build contains source rows for every Phase A presentation,
  certificate, and convention locator.
- Audit rejects orphaned or underspecified source references.

## Step 04: Persist Manual MVP Presentation Rows

Ground truth first:

- Re-read `FiniteRingDatabaseConstructors.jl`, the current review CSV
  `ring_presentations.csv`, and the source-rights matrix from Step 01.
- Verify the one-element zero-ring convention and every manual constructor's
  order and characteristic before writing any database row.

Red:

- Add a populated-build test that expects `presentation` rows for all 13 MVP
  presentations and fails on the current schema-only build.
- Add a fixture that rejects a presentation row with noncanonical presentation
  JSON or missing source locator.

Green:

- Convert the existing in-memory MVP presentations into SQLite `presentation`
  rows with stable IDs, canonical payload JSON, construction class, exact
  order, exact characteristic, additive invariants, and source provenance.
- Write no `ring` rows in this step except test fixtures.

Acceptance:

- A temporary populated build has exactly the MVP presentation row count and
  passes schema-level constraints.
- The run-local schema-only smoke path remains available for fast checks.

## Step 05: Persist Canonical Ring and Invariant Rows

Ground truth first:

- Re-read `FiniteRingDatabaseDedup.jl`, `FiniteRingDatabaseInvariants.jl`, and
  convention `(an)` on hashes and bounded dedup.
- Confirm which semantic predicates remain `unknown` in Phase A.

Red:

- Add a test showing the current build has `ring=0` and then expects the
  deduplicated MVP representative count.
- Add audit fixtures for missing invariant rows and for unsupported false
  values where the correct value is `unknown`.

Green:

- Insert canonical `ring` rows for the deduplicated MVP representatives.
- Insert invariant rows for order, characteristic, additive invariants,
  zero-ring residue data, and any other source-backed exact MVP invariant.
- Keep unimplemented predicates as explicit `unknown` tokens.

Acceptance:

- The populated build contains canonical rings matching the review export
  representative count.
- No invariant row claims field/local/reduced/product/Frobenius status unless
  local code and sources support it.

## Step 06: Persist Checked Isomorphism Certificates and Links

Ground truth first:

- Re-read `FiniteRingDatabaseCertificates.jl`, `FiniteRingDatabaseDedup.jl`,
  and the audit contract for `ring_presentation_link.certificate_id`.
- Verify that the existing `F_2 x F_3` to `Z/6Z` merge certificate is checked
  by local code, not by hash equality.

Red:

- Add tests that noncanonical presentation links fail unless they reference a
  stored, verifier-approved certificate.
- Add a fixture where a certificate row exists but its checker verdict is not
  `ok`; audit must reject it.

Green:

- Insert `isomorphism_certificate` rows for every noncanonical MVP merge.
- Insert `ring_presentation_link` rows for canonical links and certified merge
  links only.
- Store enough certificate payload to rerun the local checker.

Acceptance:

- Every MVP presentation is linked to exactly one canonical ring.
- Every noncanonical link has a stored certificate that the local verifier can
  recompute and accept.

## Step 07: Persist Quantization and Obstruction Rows

Ground truth first:

- Re-read the residue, thickened-Frobenius, and prime-field Weyl matrix helper
  conventions.
- Re-read the CSV review rows for `ring_quantization_summary.csv` and
  `ring_quantization_obstruction.csv`.

Red:

- Add an audit fixture where a populated ring lacks both a quantization row and
  a concrete obstruction row; audit must reject it.
- Add a fixture where a blocked row carries a Hilbert dimension; audit must
  reject it.

Green:

- Insert `quantization` rows for each MVP canonical ring and layer.
- Represent unavailable layers with explicit obstruction codes, not empty
  claims.
- Keep dense matrix artifacts out of the DB unless their local checks pass.

Acceptance:

- Every populated canonical ring has complete Phase A quantization coverage:
  either an available row or a concrete obstruction row for each MVP layer.
- The zero ring uses the recorded
  `not_applicable_until_layer_semantics` marker.

## Step 08: Harden Audit for Populated MVP Databases

Ground truth first:

- Re-read the PRD acceptance criteria and all populated-row producers from
  Steps 03-07.
- List every relation that schema constraints cannot express.

Red:

- Add malformed populated databases for: missing source provenance, unlinked
  presentation, duplicate canonical ring representative, missing invariant,
  missing quantization/obstruction, unresolved noncanonical link, malformed
  certificate payload, and unsupported completeness assertion.

Green:

- Extend `finite_ring_db_audit.jl` to reject each malformed populated case.
- Keep the schema-only smoke database passing because it is a separate smoke
  target, not a populated acceptance artifact.

Acceptance:

- Audit distinguishes `schema_only` and `populated_mvp` build stages.
- The populated MVP build passes only when every row-level evidence chain is
  present.

## Step 09: Add SQLite-Backed Exports and CSV Comparison

Ground truth first:

- Re-read `finite_ring_db_exports.jl`, `data/SCHEMA.md`, and current CSV
  sentinels.
- Decide whether to add `--db` mode to the existing exporter or a new
  `finite_ring_db_sqlite_exports.jl` script.

Red:

- Add a test that the current in-memory exporter cannot be used as evidence
  for populated SQLite content.
- Add a comparison test where SQLite-backed exports must match the existing
  MVP review rows modulo documented sentinel text and row ordering.

Green:

- Add SQLite-backed CSV export for summary, presentations, certificates,
  quantization summary, and obstruction rows.
- Preserve `#` sentinel rows and update schemas to distinguish in-memory
  review exports from SQLite-backed populated exports.

Acceptance:

- CSV outputs can be regenerated from the populated SQLite database.
- `data/SCHEMA.md`, `INDEX.md`, and run README point to the SQLite-backed
  producer for populated artifacts.

## Step 10: Persist Audit/Build Evidence Artifacts

Ground truth first:

- Re-read run-bundle discipline in `AGENTS.md`, `scripts/README.md`, and the
  current run README.
- Decide the exact audit artifact shape: text, JSON, or both.

Red:

- Add a run-bundle test that fails if a populated build records audit success
  only in prose and not as an artifact.
- Add a test that `build_run` command/tool metadata matches the persisted
  evidence file.

Green:

- Make the populated build and audit path write deterministic evidence
  artifacts under the run bundle, for example
  `data/finite_ring_db_audit.json` and
  `data/finite_ring_db_build_summary.json`.
- Register the artifacts in `INDEX.md` and, if CSV/JSON schema is fixed, in
  `data/SCHEMA.md`.

Acceptance:

- A future reviewer can verify build/audit status without trusting README
  prose.
- Artifact hashes or contents are stable enough for meaningful diffs.

## Step 11: Produce the First Populated MVP Run Bundle

Ground truth first:

- Create or reuse a dated run bundle only after Steps 01-10 pass locally.
- Re-read the current run README and decide whether to preserve the
  schema-only bundle as history or create a new populated bundle.

Red:

- Run the populated command sequence and record failures exactly in the run
  README before fixing them.

Green:

- Build the populated MVP SQLite database.
- Run the audit gate.
- Generate SQLite-backed exports.
- Run `scripts/run_all.jl --fast` if the fast path remains appropriate, plus
  any focused populated-run command that is too heavy for fast.

Acceptance:

- The populated run bundle contains SQLite, exports, source rows, audit/build
  evidence, and README headline counts.
- The database has nonzero `ring`, `presentation`, `source`, `quantization`,
  and `ring_presentation_link` rows.
- No completeness claim is present.

## Step 12: Document Populated-MVP Status Without Completeness Claims

Ground truth first:

- Re-read `INDEX.md`, `data/SCHEMA.md`, `HANDOFF.md`, the PRD, and report shard
  rules.
- Confirm the populated MVP audit artifact is passing before changing status
  prose.

Red:

- Add documentation checks that fail if the project still says only
  schema-only SQLite exists after the populated run is accepted.
- Add checks that fail if docs use words like complete or classification for
  the MVP run without an enumeration-batch claim.

Green:

- Update `INDEX.md`, `data/SCHEMA.md`, `HANDOFF.md`, the PRD status paragraph,
  and the populated run README.
- Do not add report mathematical claims yet unless the shard explicitly states
  the populated MVP boundary and cites the audit artifact.

Acceptance:

- Documentation states: populated MVP exists, bounded catalogue completeness is
  still pending, and all claims link to run artifacts.

## Phase B: Bounded Catalogue and Completeness Evidence

Phase B extends beyond the manual MVP. It may import or reconstruct bounded
catalogue data only after local source rights and exact conventions are
registered.

## Step 13: Acquire Missing First-100 Catalogue Sources

Ground truth first:

- Re-read the source gaps in `references/finite_ring_database/SOURCES.md`:
  OEIS snapshot, Magma docs, McDonald, Bini--Flamini, Ganske--McDonald, and
  small-order classification references.
- Determine the smallest source-backed order cutoff expected to contain at
  least 100 finite commutative unital rings under convention `(an)`. Current
  GAP status metadata through order `15` gives fewer than 100 scoped rings, so
  this step must not assume the existing order-15 metadata is enough.
- Prefer lawful source bundles, publisher pages, arXiv, or user-provided
  access. Do not use pirate sources.

Red:

- Add a source-manifest guard that fails if a bounded-catalogue import step is
  enabled while required sources are missing or marked prospective.

Green:

- Acquire and register the minimum sources needed for the first bounded
  catalogue tranche.
- Record retrieval date, access route, SHA256, exact local path, and allowed
  use for each source.

Acceptance:

- The next import step has all local sources and rights needed for a clearly
  bounded target whose expected deduplicated count is at least 100, or a
  documented blocker bead states exactly which source/access gap prevents that
  target.

## Step 14: Prototype GAP SmallRing Presentation Extraction

Ground truth first:

- Re-read GAP source locators for element enumeration, equality,
  multiplication, additive operations, identities, and `SmallRing`.
- Confirm the exact conversion from GAP elements to the local
  structure-constant presentation model.

Red:

- Add GAP-enabled tests that fail until `SmallRing(s,i)` objects for a tiny
  range can be converted into local presentations with exact multiplication
  and addition tables.
- Add skip tests for missing GAP and fail-loud tests for malformed GAP output.

Green:

- Implement a GAP extraction helper for a small bounded range.
- Emit local structure-constant presentations and provenance metadata, but do
  not insert them into the canonical populated DB until audit and dedup are
  ready.

Acceptance:

- Representative GAP `SmallRing` entries round-trip through the local
  structure-constant validators.
- The helper still makes no completeness claim.

## Step 15: Add Enumeration-Batch Completeness Contract

Ground truth first:

- Re-read PRD schema rows for `enumeration_batch`, the audit rules, and the
  newly acquired classification/source locators.
- Decide exactly what a batch can certify: source count reconciliation,
  imported rows, scoped commutative-unital count, or full isomorphism-class
  completeness.

Red:

- Add audit fixtures where `certifies_completeness=true` lacks source locator,
  scope JSON, expected count, observed count, import command, or checker
  artifact.
- Add a fixture where observed/imported counts disagree and audit fails.

Green:

- Insert `enumeration_batch` rows only for locally checked bounded scopes.
- Store scope JSON, expected counts, observed counts, tool versions, source
  locators, and audit artifact links.

Acceptance:

- Completeness claims are impossible without a passing enumeration-batch row.
- Status metadata rows remain clearly separate from completeness-certifying
  batches.

## Step 16: Populate Audited First-100-Or-More Ring Tranche

Ground truth first:

- Choose the smallest bounded tranche supported by Step 13 sources and Step 14
  extraction whose deduplicated finite commutative unital ring count is at
  least 100. If the next natural source-backed tranche produces more than 100,
  keep the larger tranche rather than trimming evidence.
- Confirm whether the tranche target is all finite rings, finite commutative
  rings, or finite commutative unital rings under convention `(an)`.

Red:

- Add an acceptance test where the first-100-or-more tranche is expected but
  fewer than 100 deduplicated canonical ring rows, missing certificates, or
  missing enumeration evidence cause audit failure.

Green:

- Import or reconstruct presentations for the tranche.
- Deduplicate them through local certificates.
- Insert rings, presentations, links, invariants, quantization/obstruction
  rows, and enumeration-batch evidence.

Acceptance:

- The tranche audit passes with at least 100 deduplicated canonical ring rows.
- Each included canonical ring has at least one source-backed presentation and
  a complete local evidence chain.
- Any completeness language is exactly scoped to the certified bounded tranche.

## Step 17: Reconcile First-100-Or-More Tranche Across Sources

Ground truth first:

- Re-read every independent count/source available for the first-100-or-more
  tranche: GAP,
  registered literature tables, OEIS snapshots if acquired, and local
  derivations.
- Identify convention mismatches before comparing counts.

Red:

- Add reconciliation fixtures where count mismatches, convention mismatches,
  or duplicate unresolved presentations cause audit or reconciliation failure.

Green:

- Add a reconciliation report artifact comparing imported/deduplicated counts
  against independent sources.
- Raise follow-up beads for any mismatch rather than smoothing it into prose.

Acceptance:

- The first-100-or-more tranche has a machine-readable reconciliation artifact.
- Any unresolved mismatch blocks report/release promotion.

## Step 18: Promote First-100-Or-More Catalogue Status

Ground truth first:

- Re-read report shard rules, `report/SHARD_CATALOG.md`, the PRD, and the
  passing first-100-or-more tranche artifacts.
- Confirm `report.pdf` rebuild requirements before changing report sources.

Red:

- Add documentation/report checks that fail if the bounded catalogue artifact
  is not indexed or if report prose lacks exact artifact/source locators.

Green:

- Update PRD status, `INDEX.md`, `data/SCHEMA.md`, `HANDOFF.md`, and the
  relevant report shard or a new shard if justified.
- Decide release-artifact policy for `finite_rings.sqlite`; if not ready,
  keep SQLite local/ignored and publish only derived auditable artifacts.

Acceptance:

- The report describes only the certified first-100-or-more bounded scope.
- `report.pdf` is rebuilt if report sources changed.
- Release/local artifact policy is explicit before any SQLite file is treated
  as canonical outside the run bundle.
