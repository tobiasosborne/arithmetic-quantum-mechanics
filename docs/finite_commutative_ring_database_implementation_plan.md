# Finite Commutative Ring Database Implementation Plan

Status: planning companion to
`docs/finite_commutative_ring_database_prd.md`.

Tracking: each step is registered as a Beads issue. The current repository did
not have `.beads/` initialized before this plan, so Beads was initialized with
prefix `aqm`. The bead IDs below must be filled from `bd` after issue creation.

Principle: every step starts with ground truth, then a failing check, then the
minimal green implementation. No step may add an unsourced mathematical claim.

## Dependency Chain

Each row depends on the previous row. This is stricter than the likely
engineering dependency graph, but it keeps the first pass auditably linear.

| Step | Bead | Title | Depends on |
|---|---|---|---|
| 01 | `aqm-pa0` | Decide finite-ring scope edge cases | none |
| 02 | `aqm-8dl` | Pin source and tool ground truth | `aqm-pa0` |
| 03 | `aqm-4fi` | Add database schema migration | `aqm-8dl` |
| 04 | `aqm-775` | Add run-bundle CLI skeleton | `aqm-4fi` |
| 05 | `aqm-0zl` | Add canonical JSON and ID hashing | `aqm-775` |
| 06 | `aqm-9fy` | Add structure-constant ring model | `aqm-0zl` |
| 07 | `aqm-30c` | Add manual MVP ring constructors | `aqm-9fy` |
| 08 | `aqm-sa4` | Add invariant engine | `aqm-30c` |
| 09 | `aqm-49d` | Add isomorphism certificate verifier | `aqm-sa4` |
| 10 | `aqm-nsi` | Add small-ring dedup search | `aqm-49d` |
| 11 | `aqm-cmj` | Add residue quantisation records | `aqm-nsi` |
| 12 | `aqm-t2y` | Add thickened Frobenius quantisation | `aqm-cmj` |
| 13 | `aqm-1wg` | Add optional Weyl matrix materialisation | `aqm-t2y` |
| 14 | `aqm-ria` | Add optional GAP small-ring importer | `aqm-1wg` |
| 15 | `aqm-71y` | Add optional quotient-ring constructors | `aqm-ria` |
| 16 | `aqm-ykp` | Add exports, schemas, and run_all wiring | `aqm-71y` |
| 17 | `aqm-hay` | Add database audit gate | `aqm-ykp` |
| 18 | `aqm-6t4` | Run acceptance bundle and document outcome | `aqm-hay` |

## Step 01: Decide Finite-Ring Scope Edge Cases

Decision recorded by `aqm-pa0`: include the one-element zero ring in scope and
MVP, and keep generated SQLite files as local run artifacts until a release
artifact policy exists.

Ground truth first:

- Re-read `CONVENTIONS.md` convention `(an)`.
- Re-read `references/finite_ring_database/SOURCES.md` entries for Nowicki,
  GAP, and Behboodi--Beyranvand--Hashemi--Khabazian.
- Verify that `aqm-pa0` records the one-element zero-ring inclusion policy and
  generated-SQLite commit policy in convention `(an)` and the PRD.

Red:

- Add a documentation check that fails if the one-element zero-ring policy or
  generated-SQLite commit policy marker is missing.

Green:

- Keep the policy in `CONVENTIONS.md` and align the PRD MVP dataset and
  generated-database artifact policy with it.

Unclear:

- The remaining implementation-specific zero-ring invariant policy
  (characteristic, residue fields, and quantisation fields) is not decided by
  `aqm-pa0`; `aqm-3cm` tracks it before manual constructors.

## Step 02: Pin Source and Tool Ground Truth

Ground truth first:

- Verify every source path named in
  `references/finite_ring_database/SOURCES.md` exists locally or is explicitly
  ignored as a local-only PDF.
- Capture installed versions for `julia`, `gap`, `sage`, `python`, `sqlite3`,
  and any OSCAR/Nemo availability without making them hard requirements.

Red:

- Add a source/tool preflight test that fails if a registered tracked source is
  missing, if ignored local-only PDFs are not documented, or if optional tools
  do not report either `available` or `missing`.

Green:

- Implement the preflight helper and make missing optional tools produce
  explicit skip records.

Unclear:

- The exact SQLite access layer is undecided. This step should only report
  available choices, not choose the implementation library.

## Step 03: Add Database Schema Migration

Ground truth first:

- Re-read PRD section 5 and SQLite source locators in
  `references/finite_ring_database/SOURCES.md`.

Red:

- Add a test that creates a temporary run directory and asserts that
  `finite_rings.sqlite` does not contain the required tables before migration.
- Add a test that foreign keys are enabled and reject an invalid
  `ring_presentation_link`.

Green:

- Add the minimal schema migration code for the PRD tables.
- Add a schema-version table if needed for deterministic migrations.

## Step 04: Add Run-Bundle CLI Skeleton

Ground truth first:

- Re-read `scripts/_common.jl`, `scripts/run_all.jl`, and `CONVENTIONS.md`
  convention `(d)`.

Red:

- Add a test that `finite_ring_db_build.jl` exits before writing output when
  the target run bundle lacks `README.md`.
- Add a test that a valid run bundle creates a SQLite file with a `build_run`
  row and no ring rows.

Green:

- Add `scripts/arithmetic/finite_ring_db_build.jl` with minimal argument
  parsing and run-bundle checks.

## Step 05: Add Canonical JSON and ID Hashing

Ground truth first:

- Re-read PRD section 6 and convention `(an)`.

Red:

- Add tests showing that differently ordered JSON objects produce the same
  canonical payload and ID.
- Add tests showing that changed scope or presentation payload changes the ID.

Green:

- Implement canonical JSON serialization and ID constructors for
  `presentation`, `ring`, `certificate`, and `quantization`.

## Step 06: Add Structure-Constant Ring Model

Ground truth first:

- Re-read Behboodi--Beyranvand--Hashemi--Khabazian locators for quasi bases
  and structure constants.
- Re-read GAP `RingByStructureConstants` source locator for cross-tool shape.

Red:

- Add tests for invalid multiplication tables: noncommutative, nonassociative,
  no identity, and identity not preserved.
- Add tests for valid `Z/4Z` and `F_2[e]/(e^2)` element operations.

Green:

- Implement a finite additive invariant-factor model, element operations,
  identity checks, associativity checks, and commutativity checks.

## Step 07: Add Manual MVP Ring Constructors

Ground truth first:

- Re-read PRD section 7 and existing report shards `AQM-23`, `AQM-34`,
  `AQM-36`, and `AQM-40`.

Red:

- Add tests that the MVP constructors are absent or fail to produce the
  expected order and characteristic.

Green:

- Implement constructors for prime fields, `Z/nZ` examples, dual-number
  examples, and finite products listed in the PRD MVP dataset.

## Step 08: Add Invariant Engine

Ground truth first:

- Re-read PRD-FR-005 and source locators for the invariant stack.
- Acquire a local source before adding any invariant not already source-backed
  by the PRD or existing report.

Red:

- Add tests for order, characteristic, additive invariant factors, field,
  reduced, local, product, and known residue-field-size cases.

Green:

- Implement exact invariant computation for the MVP constructors.
- Store unknown or unimplemented invariants as explicit `unknown`, not as
  false.

## Step 09: Add Isomorphism Certificate Verifier

Ground truth first:

- Re-read PRD-FR-006 and convention `(an)`.

Red:

- Add tests that a correct certificate for `F_2[x]/(x^2)` versus
  `F_2[e]/(e^2)` verifies.
- Add tests that a bad additive map, a non-bijective map, a map that moves
  `1`, and a multiplication-breaking map are rejected.

Green:

- Implement certificate verification independent of the certificate producer.

## Step 10: Add Small-Ring Dedup Search

Ground truth first:

- Re-read Behboodi--Beyranvand--Hashemi--Khabazian isomorphism-framework
  locators and PRD-FR-006.

Red:

- Add tests that duplicate presentations merge only when a verifier-approved
  certificate exists.
- Add tests that `Z/4Z` does not merge with `F_2[e]/(e^2)` and that
  `F_3[e]/(e^2)` does not merge with `F_3 x F_3`.

Green:

- Implement brute-force or bounded additive-automorphism search for MVP-sized
  rings.

Unclear:

- The efficient general algorithm beyond small rings is not specified. This
  step is only the MVP dedup engine.

## Step 11: Add Residue Quantisation Records

Ground truth first:

- Re-read conventions `(u)`, `(y)`, and PRD-FR-008.
- Re-read report shards `AQM-23` and `AQM-40`.

Red:

- Add tests that `Z/6Z` gives residue qudit dimensions `[2,3]`.
- Add tests that `F_3 x F_3` gives `[3,3]` and that a field gives one qudit.

Green:

- Implement residue quantisation rows from certified maximal ideals and
  residue field sizes for MVP rings.

## Step 12: Add Thickened Frobenius Quantisation

Ground truth first:

- Re-read convention `(ab)` and report shard `AQM-36`.
- Re-read finite Frobenius-ring source locators in
  `references/heisenberg_weil/SOURCES.md`.

Red:

- Add tests that `F_3[e]/(e^2)` produces `hilbert_dim_exact=9`,
  `label_group_order_exact=81`, and `observable_basis_dim_exact=81`.
- Add tests that rings with no certified generating character produce a
  `blocked` quantisation row.

Green:

- Implement thickened Frobenius quantisation records for certified MVP local
  Artin examples.

## Step 13: Add Optional Weyl Matrix Materialisation

Ground truth first:

- Re-read PRD-FR-009 and Weyl operator conventions `(ab)` and `(af)`.

Red:

- Add tests for one tiny odd-characteristic example showing the generated
  matrices fail until multiplication, commutator, unitarity, and
  Hilbert-Schmidt checks are implemented.

Green:

- Implement matrix materialisation under a configurable threshold.
- Store matrix artifact metadata only after all checks pass.

Unclear:

- The exact threshold is still undecided. Use a test-only default until the
  policy is fixed.

## Step 14: Add Optional GAP Small-Ring Importer

Ground truth first:

- Re-read GAP source locators for `SmallRing`, `NumberSmallRings`,
  `IsRingWithOne`, `DirectSum`, and `RingByStructureConstants`.

Red:

- Add tests that the importer records an explicit skip when GAP is missing.
- When GAP is available, add a small order smoke test with count
  reconciliation for the audited scope.

Green:

- Implement `gap-small` import behind optional-tool detection.
- Filter explicitly to finite commutative unital rings before insertion.

Unclear:

- GAP's small-ring library scope must be verified in the installed GAP version
  before claiming completeness for any imported order.

## Step 15: Add Optional Quotient-Ring Constructors

Ground truth first:

- Re-read Sage, OSCAR, Nemo, and FLINT source locators in
  `references/finite_ring_database/SOURCES.md`.

Red:

- Add tests that missing optional tools produce explicit skip rows.
- When tools are available, add cross-checks for `F_2[x]/(x^2+x)`,
  `F_3[e]/(e^2)`, and `Z/6Z`.

Green:

- Implement quotient constructors or wrappers that emit the same
  structure-constant model used by the core database.

Unclear:

- The preferred production backend among Sage, OSCAR/Nemo, and Python is not
  fixed. This step should keep wrappers optional and interoperable.

## Step 16: Add Exports, Schemas, and `run_all` Wiring

Ground truth first:

- Re-read `data/SCHEMA.md`, `INDEX.md`, `scripts/run_all.jl`, and
  `CONVENTIONS.md` conventions `(e)` and `(g)`.

Red:

- Add tests that CSV exports are absent from schema/index and `run_all --fast`
  does not exercise the smoke build.

Green:

- Add CSV schemas, index rows, sentinel handling, and `scripts/run_all.jl`
  registration for the fast smoke build.

## Step 17: Add Database Audit Gate

Ground truth first:

- Re-read PRD acceptance criteria and all implemented schema contracts.

Red:

- Add tests where an intentionally malformed database fails audit: duplicate
  uncertified presentations, missing quantisation or obstruction rows, missing
  source provenance, and unresolved completeness claims.

Green:

- Implement `finite_ring_db_audit.jl` and make it fail loud on every violated
  invariant.

## Step 18: Run Acceptance Bundle and Document Outcome

Ground truth first:

- Re-read the run README and verify every result links to a source, local
  derivation, test, or run artifact.

Red:

- Run the acceptance commands and record any failing command exactly.

Green:

- Produce the first passing run bundle.
- Update `INDEX.md`, `data/SCHEMA.md`, `HANDOFF.md`, and, only if conclusions
  are ready for the lab book, add a report shard.

Unclear:

- Report integration is deferred until a successful run bundle exists. The
  implementation should not create report claims before the database audit
  passes.
