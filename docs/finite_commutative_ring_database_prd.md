# Finite Commutative Ring Database PRD

Status: planning artifact. The PRD, schema-only smoke build, audit gate, and
in-memory MVP review exports exist; a populated/audited ring database remains
pending, and no completeness claim is made.

Primary sources:
`references/finite_ring_database/SOURCES.md`,
`CONVENTIONS.md` convention `(an)`, and the existing finite-ring quantum-field
conventions `(u)`, `(aa)`, `(ab)`, and `(af)`.

## 1. Objective

Build a reproducible local database of finite commutative rings up to
isomorphism, then attach the arithmetic-quantum-field data already developed
in the lab book to every certified ring entry.

The database must distinguish:

- ring catalogue data: what finite commutative unital ring is represented;
- source and construction data: where the presentation came from;
- isomorphism evidence: why two presentations are or are not the same ring;
- completeness evidence: what enumeration scope a run certifies;
- quantisation data: residue-qudit and thickened Weyl/Frobenius structures.

No row may be treated as canonical merely because a presentation string or
invariant hash matches another row. Isomorphism is a mathematical claim and
therefore requires a stored certificate.

## 2. Scope

The first database scope is finite, commutative, associative rings with
identity. Nonunital rings are out of scope for the first implementation.

In scope:

- presentations from local sources, CAS-generated examples, and direct product
  closure;
- exact invariant computation for finite rings;
- isomorphism deduplication with certificates;
- SQLite storage in a run bundle;
- CSV or JSONL exports for small curated views;
- programmatic quantisation records for every certified ring.

Out of scope for the first implementation:

- claims of complete classification beyond explicitly certified finite bounds;
- remote automation;
- dense Weyl matrices for large rings;
- noncommutative rings;
- nonunital rngs;
- Magma-dependent required workflows.

## 3. Source-Grounded Constraints

Nowicki's table is useful seed material for finite commutative local unital
rings of selected small prime-power orders, but its license is not recorded in
the local file. It must be used as a verification source unless a row-import
license policy is recorded.

Behboodi--Beyranvand--Hashemi--Khabazian provide a source for finite-ring
classification by finite abelian groups, quasi bases, structure constants, and
isomorphism criteria. This should guide the presentation layer and the small
custom isomorphism checker.

GAP is a small-order oracle, not a complete database engine: the registered
GAP manual snapshot states that the built-in small-ring library covers rings
of order up to 15 and documents `SmallRing` and `NumberSmallRings`.

Sage, OSCAR, Nemo, AbstractAlgebra, and FLINT are construction and exact
algebra backends. No registered source currently shows that any one of them
provides complete finite commutative ring enumeration and ring-isomorphism
deduplication out of the box.

FLINT modular matrix routines require care over composite moduli: the local
FLINT source marks several routines as prime-modulus routines, while Howell
form is the relevant composite-modulus path.

SQLite is the storage target because the registered SQLite source describes a
self-contained, serverless, zero-configuration single-file database.

By `CONVENTIONS.md` convention `(an)`, the finite-ring database includes the
one-element zero ring: GAP allows a ring-with-one to have zero equal to
identity, GAP's small-ring example records one stored ring of order `1`, and
the Stacks algebra convention states that the zero ring is a ring.

## 4. Product Requirements

### PRD-FR-001: Source Registry

Every external catalogue, theorem source, documentation snapshot, or algorithm
source used by the database must have a manifest row in
`references/finite_ring_database/SOURCES.md` before use.

Each imported ring row must store `source_id`, locator, import method, and
license status.

### PRD-FR-002: Run-Bundle Database Builds

The canonical generated database file must be written under a run bundle:

```text
runs/<YYYY-MM-DD>-finite-ring-database/data/finite_rings.sqlite
```

The run bundle must have a README before any script writes output. The README
must record hypothesis, command line, tool versions, scope bounds, headline
counts, failed checks, and next steps.

Generated SQLite files follow:

```text
finite_ring_db.sqlite_commit_policy = local_run_artifact_until_release_policy
finite_ring_db.sqlite_build_rerun_policy = fail_existing_sqlite_unless_force
```

That is, `finite_rings.sqlite` is an ordinary local run artifact and should
not be committed in normal development until a release artifact policy is
recorded. Source manifests, run READMEs, audit outputs, and review-sized
exports remain commit candidates.

Build reruns are no-append by default for the MVP. If
`runs/<slug>/data/finite_rings.sqlite` already exists, the build CLI must fail
before schema migration or inserts with a clear no-overwrite error. An explicit
`--force` may remove only that SQLite file and rebuild `schema` plus
`build_run`; it must preserve the run directory, run README, and sibling files.

### PRD-FR-003: Ring Identity Contract

A database ring is a finite commutative unital ring up to unital ring
isomorphism.

Two presentations are the same database ring only after a certificate proves a
unital ring isomorphism between them or a trusted local oracle gives a
versioned canonical identifier for the exact same scope.

### PRD-FR-004: Presentation Model

Every presentation must be convertible to at least one of:

- finite additive abelian group plus multiplication structure constants;
- quotient of a polynomial or residue ring by a finitely generated ideal;
- finite product of other database rings;
- source-table presentation string with a parsed or manually certified model.

The structure-constant normal form is the cross-tool interchange format. It
records an additive decomposition

```text
G = Z/d_1 Z direct_sum ... direct_sum Z/d_r Z
```

with ordered generators `e_1,...,e_r`, a distinguished identity vector, and
products

```text
e_i * e_j = sum_k c_ijk e_k,    c_ijk in Z/d_k Z.
```

### PRD-FR-005: Invariant Stack

Each certified ring must compute and store, where applicable:

- order and characteristic;
- additive group invariant factors;
- whether the row is local, reduced, a field, a product, or unknown;
- Jacobson/nilradical size when computed;
- nilpotency index of the nilradical or maximal ideal when computed;
- maximal ideals and residue field sizes when computed;
- idempotent decomposition when computed;
- ideal count or ideal-lattice fingerprint when computed;
- unit-group order or invariant factors when computed;
- socle size or socle dimension when computed;
- Frobenius/generating-character status for Weyl quantisation.

These invariants are filters and audit data. They are not isomorphism proofs.

### PRD-FR-006: Deduplication Pipeline

The deduplication pipeline is:

1. Parse or construct presentations.
2. Compute cheap invariants.
3. Bucket candidates by invariant signature.
4. Search for unital ring isomorphisms only inside compatible buckets.
5. Store a certificate for every merge or every exhausted non-isomorphism
   check that is used to justify a completeness claim.
6. Choose a canonical representative by deterministic policy.

The first custom certificate format is:

```text
source_presentation_id
target_presentation_id
additive_generator_image_matrix
identity_preserved
addition_preserved
multiplication_preserved
bijective_additive_map
tool
tool_version
checker_hash
```

For small orders, a verifier must independently check the map by evaluating
all additive basis products or all element products.

### PRD-FR-007: Enumeration and Completeness

Completeness is per batch, never global unless proved for that batch.

An enumeration batch must state:

- ring scope, e.g. finite commutative unital rings;
- order set, e.g. `n <= 15`, `p^e` for listed `p,e`, or a finite source table;
- source of completeness, e.g. GAP small-ring library, Nowicki table, or a
  local exhaustive generator;
- row count before deduplication;
- row count after deduplication;
- unresolved collision count;
- source count reconciliation.

If a batch cannot certify completeness, its status is `partial`.

### PRD-FR-008: Quantisation Layers

Each ring must receive one or more quantisation records:

`residue`
: The reduced residue-qudit layer from conventions `(u)` and `(y)`.

`thickened_frobenius`
: The nilpotent-sensitive finite Frobenius-ring Weyl layer from convention
  `(ab)` or the finite Frobenius-ring Pauli layer from `AQM-31`, when a
  generating character is certified.

`blocked`
: A record explaining why quantisation was not produced, for example missing
  maximal-ideal decomposition, missing residue-field computation, or missing
  generating character.

For a finite ring `R`, the residue layer records:

```text
MaxSpec(R) = {m_1,...,m_s}
k_i = R/m_i
residue_qudit_dims = [|k_1|,...,|k_s|]
E_res(R) = direct_sum_i k_i^2
H_res(R) = tensor_i ell^2(k_i)
A_res(R) = tensor_i End_C(ell^2(k_i))
```

For a certified finite Frobenius ring with generating character `chi`, the
thickened layer records:

```text
H_thick(R) = ell^2(R)
E_thick(R) = R x R
T(q)|s> = |s + q>
Rop(p)|s> = chi(p*s)|s>
W(q,p) = T(q) Rop(p)
commutator((q,p),(q',p')) = chi(p*q' - p'*q)
```

If `R = product_i R_i` and each `R_i` has a certified thickened layer, the
global thickened layer is the tensor product of the local layers.

### PRD-FR-009: Matrix Storage Policy

The database stores construction recipes and certificates by default, not full
operator matrices.

Dense Weyl matrices may be materialized only when:

- `|R| <= matrix_dump_threshold`;
- the run README records the threshold;
- the matrix artifact path is content-addressed;
- unitarity, multiplication, commutator, and Hilbert-Schmidt orthogonality are
  checked exactly or with a declared exact cyclotomic representation.

### PRD-FR-010: Tooling Architecture

Implementation is Julia-first, with optional external oracles.

Required project additions for implementation:

- `scripts/arithmetic/finite_ring_db_build.jl`
- `scripts/arithmetic/finite_ring_db_quantize.jl`
- `scripts/arithmetic/finite_ring_db_audit.jl`
- source code under `src/ArithmeticQuantumMechanics/FiniteRingDatabase.jl`
- registration in `scripts/run_all.jl`
- schema documentation in `data/SCHEMA.md`
- run-bundle registration in `INDEX.md`

Optional wrappers:

- GAP smoke tests for `SmallRing` and `NumberSmallRings`;
- Sage cross-checks for quotient-ring examples;
- OSCAR/Nemo constructors for polynomial quotient and residue rings;
- Magma only as an optional non-required oracle when a license exists.

### PRD-FR-011: CLI Contract

The first implementation should expose:

```bash
julia --project=. scripts/arithmetic/finite_ring_db_build.jl \
  --run runs/<date>-finite-ring-database \
  --max-order 15 \
  --sources gap-small,manual-examples \
  [--force]

julia --project=. scripts/arithmetic/finite_ring_db_quantize.jl \
  --run runs/<date>-finite-ring-database \
  --db runs/<date>-finite-ring-database/data/finite_rings.sqlite

julia --project=. scripts/arithmetic/finite_ring_db_audit.jl \
  --db runs/<date>-finite-ring-database/data/finite_rings.sqlite
```

Optional tools must skip explicitly or fail before partial writes, following
`CONVENTIONS.md` convention `(f)`.

### PRD-FR-012: Exports

The SQLite database is the canonical run artifact.

CSV exports are allowed only for review-sized views, for example:

- `rings_summary.csv`
- `ring_presentations.csv`
- `ring_isomorphism_certificates.csv`
- `ring_quantization_summary.csv`
- `ring_quantization_obstruction.csv`

Every CSV export must have sentinel-row handling documented in `data/SCHEMA.md`.

## 5. Proposed SQLite Schema

Column types are SQLite storage classes. JSON columns use canonical UTF-8 JSON
with sorted object keys; canonical JSON validity is audited rather than
enforced by JSON1 schema constraints in this MVP.

```sql
CREATE TABLE source (
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

CREATE TABLE build_run (
  run_id TEXT PRIMARY KEY,
  run_path TEXT NOT NULL,
  git_commit TEXT,
  command_line TEXT NOT NULL,
  tool_versions_json TEXT NOT NULL,
  created_utc TEXT NOT NULL,
  scope_json TEXT NOT NULL
);

CREATE TABLE presentation (
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

CREATE TABLE ring (
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

CREATE TABLE ring_presentation_link (
  ring_id TEXT NOT NULL,
  presentation_id TEXT NOT NULL,
  link_status TEXT NOT NULL,
  certificate_id TEXT,
  PRIMARY KEY(ring_id, presentation_id),
  FOREIGN KEY(ring_id) REFERENCES ring(ring_id),
  FOREIGN KEY(presentation_id) REFERENCES presentation(presentation_id),
  FOREIGN KEY(certificate_id) REFERENCES isomorphism_certificate(certificate_id)
);

CREATE TABLE invariant (
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

CREATE TABLE isomorphism_certificate (
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

CREATE TABLE enumeration_batch (
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

CREATE TABLE quantization (
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

CREATE TABLE matrix_artifact (
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

CREATE TABLE finite_ring_database_schema_version (
  component TEXT PRIMARY KEY,
  version INTEGER NOT NULL
);
```

Schema integrity follows
`finite_ring_db.schema_integrity_policy = relational_checks_in_schema_json_and_open_enums_in_audit`.
The SQLite schema owns the certificate-link foreign key, the invariant
ring-or-presentation anchor, and the `0`/`1` checks for `ring.is_commutative`
and `ring.has_one`. The later audit gate owns canonical JSON validity and the
open/evolving status-token vocabulary until producers freeze those
vocabularies. No JSON1 `json_valid` schema constraints are part of this MVP,
and the migration remains schema version `1`.

## 6. Canonical IDs

Use opaque stable IDs, not presentation strings:

```text
presentation_id = pres:<sha256 of canonical presentation payload>
certificate_id  = iso:<sha256 of ordered certificate payload>
ring_id         = ring:<sha256 of canonical representative payload plus scope>
quantization_id = quant:<ring_id>:<layer>:<version>
```

The ID hash is a locator, not a proof. The proof is the certificate row and the
checker result.

## 7. MVP Dataset

MVP-1 must include:

- the one-element zero ring;
- prime fields `F_2`, `F_3`, `F_5`;
- `Z/4Z`, `Z/6Z`, `Z/8Z`, `Z/9Z`;
- `F_2[e]/(e^2)`, `F_3[e]/(e^2)`;
- `F_2 x F_2`, `F_2 x F_3`, `F_3 x F_3`;
- GAP small-ring rows for orders `1..15` when GAP is installed, filtered to
  commutative unital rings by explicit predicates.

Zero-ring invariant policy is fixed by `CONVENTIONS.md` convention `(an)`:

```text
finite_ring_db.zero_ring_characteristic_exact = 1
finite_ring_db.zero_ring_residue_field_sizes_json = []
finite_ring_db.zero_ring_quantization_policy = not_applicable_until_layer_semantics
```

Here `characteristic_exact` is the local database invariant defined as the
additive order of the stored identity coordinate vector in the
structure-constant model. For the one-element zero ring `1=0`, so this stores
`characteristic_exact = 1`. Because the local Stacks source says the zero ring
has no prime ideal, zero-ring maximal/residue data are empty. Quantisation
implementation is still deferred: zero-ring quantisation rows must be explicit
`not_applicable_until_layer_semantics` obstruction records until a later
quantisation bead defines layer semantics, and no Hilbert-space claim is made
here.

The first completeness claim should be limited to the GAP-backed order range
that the implementation can filter and audit. Any Nowicki ingestion should be
a later milestone after license and transcription checks.

## 8. Validation Plan

Small exact tests:

- `Z/4Z` is not isomorphic to `F_2[e]/(e^2)` because the additive groups differ.
- `F_2[x]/(x^2)` is isomorphic to `F_2[e]/(e^2)` by generator rename.
- `F_2[x]/(x^2+x)` has two idempotent factors and matches `F_2 x F_2`.
- `Z/6Z` matches `F_2 x F_3` by Chinese remainder data and must dedup.
- `F_3[e]/(e^2)` is not reduced and must not merge with `F_3 x F_3`.
- GAP `NumberSmallRings(n)` must reconcile for any audited order `n <= 15`
  where GAP is installed and the ring-scope filter is recorded.

Quantisation tests:

- For every residue layer, `hilbert_dim_exact` equals the product of residue
  field sizes.
- For every thickened Frobenius layer, `hilbert_dim_exact = |R|`,
  `label_group_order_exact = |R|^2`, and
  `observable_basis_dim_exact = |R|^2`.
- For materialized matrices, verify translation law, modulation law,
  commutator law, unitarity, and Hilbert-Schmidt orthogonality.
- Existing examples from `AQM-23`, `AQM-34`, `AQM-36`, and `AQM-40` must be
  reproducible from database records.

Repository validation for implementation PRs:

```bash
make check-report-shards
make report
julia --project=. -e 'using Pkg; Pkg.test()'
julia --project=. scripts/run_all.jl --fast
make ci-before-push
```

For a PRD-only change, `git diff --check` is sufficient.

## 9. Milestones

M0: Planning and sources
: PRD, convention, and finite-ring source manifest.

M1: Empty database and schema
: SQLite schema migration, source table loader, run README template, and audit
  command.

M2: Hand examples
: Manual constructors for the MVP rings, invariant computation, and direct
  isomorphism certificates.

M3: GAP small-order oracle
: Optional GAP importer for orders up to 15, with scope filtering and count
  reconciliation.

M4: Polynomial quotient constructors
: Sage/OSCAR/Nemo-backed constructors for quotient rings used by the report.

M5: Dedup engine
: Additive-group automorphism search for small rings and certificate verifier.

M6: Quantisation engine
: Residue and thickened-Frobenius quantisation records with exact tests.

M7: Report integration
: A new report shard only after a successful run bundle exists.

## 10. Risks

The word "ring" is overloaded across sources. Every import must record whether
it is unital, associative, commutative, and whether its one-element-ring policy
matches convention `(an)`.

Finite-ring isomorphism can be expensive. The implementation must make
completeness claims only within certified bounds.

Dense Weyl matrices grow as `|R|^2` operators on a `|R|`-dimensional Hilbert
space. Storing recipes and certificates is the default.

Composite-modulus linear algebra is not field linear algebra. RREF over a
prime field must not be silently used over `Z/nZ`.

Nowicki and DML source access terms require caution. Use as provenance and
verification until row-import rights are explicit.

## 11. Open Decisions

- The exact `matrix_dump_threshold`.
- Whether SQLite access is implemented through Julia `SQLite.jl`, Python's
  standard `sqlite3`, or a tiny SQL emitter plus `sqlite3` CLI.
- Whether Magma will be supported as an optional oracle.
- Which exact local source will justify a general finite local/product
  decomposition theorem for report-level prose beyond the PRD.

## 12. Acceptance Criteria

The first implementation is acceptable when:

- a fresh clone can run the fast database build without optional tools;
- optional GAP/Sage/OSCAR paths skip explicitly when absent;
- the database contains the MVP rings with no duplicate isomorphism classes;
- every merge has a certificate checked by local code;
- every completeness claim has an enumeration-batch row;
- every ring has either a quantisation row or a concrete obstruction row;
- `scripts/run_all.jl --fast` exercises the smoke build;
- `data/SCHEMA.md`, `INDEX.md`, and the run README are updated in the same
  change as the scripts.
