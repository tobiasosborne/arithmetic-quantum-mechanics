# S3 Synthesis

## Inputs

Read the orchestration files `docs/report_mega_review/README.md` and
`docs/report_mega_review/WAVE2_ASSIGNMENTS.md`, Wave 1 reviews R33--R44,
QSA plan material in `docs/quantum_system_associations/PLAN.md`, the report
maps, `CONVENTIONS.md`, `HANDOFF.md`, `INDEX.md`, `data/SCHEMA.md`, and the
finite-ring run/status context in
`runs/2026-05-26-finite-ring-database/README.md`. Cross-read the relevant
report shards AQM-64--AQM-87 and older anchor shards where the Wave 1 reviews
needed local checks. No Julia, tests, producer scripts, or finite-ring database
code internals were run or reviewed.

Primary Wave 1 inputs:

- R33: AQM-64--AQM-65, QSA plan and vocabulary.
- R34--R36: AQM-66--AQM-71, finite-set workflows, AND/OR grammar, and field
  labels.
- R37--R40: AQM-72--AQM-79, boson/fermion, fusion endpoint, point selection,
  cotangent-first, finite phase Weyl, and geometric field spaces.
- R41--R44: AQM-80--AQM-87, finite-ring matrix, residue/nilpotent/product
  rows, infinite boundaries, agreement/degeneracy/gap ledgers.

## High-Priority Findings

1. Major: AQM-79 conflates localized regular functions on an open `D(h)` with
   finite closed-support smearing along `Z_cl(h)`.

   R40's finding is the sharpest mathematical defect in this arc. In
   `report/sections/79_quantum_system_association_geometric_field_hom_x_v.tex:185`
   --206, the same symbol `h` first defines the localization
   `F_q[x]_h` on `D(h)` and then defines the closed support
   `Z_cl(h)={pi : pi | h}` for `W_h^red(F,G)`. The AQM-49 anchor separates the
   roles: localized evaluation on `D(h)` is at closed points with `pi not| h`
   (`report/sections/49_regular_functions_affine_line_weyl_labels.tex:64`--70),
   while reduced smearing uses polynomial pairs in `R^2` reduced at
   `pi | h` (`report/sections/49_regular_functions_affine_line_weyl_labels.tex:140`
   --150). A general element of `R_h` need not be evaluable at the support
   points dividing `h`. This should be fixed before any downstream finite-ring
   or finite-support Weyl table copies the "regular-function profile" wording.

2. Major: AQM-85 imports AQM-84 boundary proposal labels into the QSA status
   vocabulary without a matching convention.

   Convention `(au)` defines table status tokens as lowercase labels such as
   `available`, `agreement`, `inequivalence`, `degenerate`, `zero`, `empty`,
   `blocked`, `unknown`, and `not_applicable`
   (`CONVENTIONS.md:2109`--2129). AQM-84 explicitly says it adds no convention
   entry (`report/sections/84_quantum_system_association_infinite_ring_boundaries.tex:13`
   --16), then defines boundary categories including "Generic-sector proposal"
   and "Completion proposal" at lines 29--47. AQM-85 then inherits those labels
   into the table vocabulary at
   `report/sections/85_quantum_system_association_agreement_inequivalence_table.tex:40`
   --42 and uses "blocked or AQM-84 proposal labels" in a status cell at
   lines 222--226. This is a vocabulary-layer bug, not a mathematical theorem
   error, but it affects the whole agreement/inequivalence ledger.

3. Medium: AQM-76's cotangent-first recipe is base-sensitive in a way the
   displayed notation hides.

   R39 flagged that AQM-76 opens with a "base field or base ring" at
   `report/sections/76_quantum_system_association_cotangent_first.tex:34`,
   but immediately writes `Omega^1_{A/k}` and `T^*_{X/k,x}` at lines 46--52.
   AQM-77 and convention `(av)` show why the base cannot be implicit:
   for `Z/4Z`, intrinsic `m/m^2` gives a nonzero cotangent object, while
   relative cotangent over `Z` vanishes
   (`report/sections/77_quantum_system_association_intrinsic_relative_cotangent.tex:210`
   --229). This should be cleaned before finite-ring-facing rows cite the
   shorter AQM-76 recipe.

4. Medium: AQM-85 over-aggregates generic sectors with completion blockers.

   R43 found that AQM-85 groups `Spec F_q[t]`, `Spec F_q[x,y]`, and `Spec Z`
   together and lists "generic sectors" alongside analytic/local, adelic,
   profinite, `C^*`, and infinite-volume completion blockers
   (`report/sections/85_quantum_system_association_agreement_inequivalence_table.tex:222`
   --226). That hides already recorded algebraic generic layers for
   `F_q(t)` in convention `(z)` (`CONVENTIONS.md:792`--812) and for
   `Q` in AQM-45 (`report/sections/45_spec_z_arithmetic_quantum_field.tex:161`
   --166). The fix is to split algebraic generic-sector availability from
   missing analytic/completed representation conventions.

5. Minor but reproducibility-facing: AQM-86 cites a nonexistent top-level CSV
   path.

   R44 found `\path{data/arithmetic_quantum_field_examples.csv}` at
   `report/sections/86_quantum_system_association_degenerate_overrestrictive_cases.tex:72`
   --75. The indexed artifact is
   `runs/2026-05-24-arithmetic-quantum-fields/data/arithmetic_quantum_field_examples.csv`
   (`INDEX.md:72`), and top-level `data/` contains only `README.md` and
   `SCHEMA.md`.

## Repeated Patterns

- Status vocabulary drift is the dominant cross-shard pattern. It appears as
  AQM-65 allowing "explicit gap label" in the same sentence as comparison
  words, AQM-66 using composite row statuses such as `question / available`,
  AQM-81 using ad hoc forms such as `blocked/database`, `not_claimed`, and
  `available locally`, and AQM-85 importing AQM-84 proposal labels into a
  status table. The causal pattern is mixing row-local planning labels,
  comparison-result tokens, prose boundary categories, and CSV/database
  sentinel vocabulary.

- "Available" often means "there is a local workflow anchor", not "this row
  has an agreement or equivalence result". AQM-66, AQM-80, and AQM-85 mostly
  say this, but the synthesis tables need to keep the distinction visually
  strict.

- Point and base choices are the main convention-sensitive mathematical
  pressure points. AQM-75's point choices, AQM-76/AQM-77's intrinsic-versus-
  relative cotangent distinction, and AQM-84/AQM-85's finite-support versus
  generic/completion boundary all protect against false finite-Weyl carrier
  claims. The review issues arise where shorthand hides the selected row or
  base.

- Several stale catalogue or locator rows lag behind newer shards. AQM-66's
  empty finite-set row still says Step 03 is pending even though AQM-67 has
  fixed the formal carrier and Gram caveat; AQM-75's underlying-set row omits
  AQM-14 as the checked all-map finite-set anchor; AQM-86 has the stale CSV
  path.

- Strict finite tensor notation needs a coherence/strictification sentence.
  AQM-68 writes tensor-by-identity inclusions and composition strictly, while
  the bare finite set supplies no order. AQM-74 has a related precision issue:
  the inverse of `R_G` is described as projection from the degree-one
  distributive expansion even though its domain is already the degree-one
  carrier.

## Cross-Arc Risks

- Finite-set workflows are mostly healthy. R34--R36 found the core
  finite-set, direct-sum, AND/OR, and `Map(X,V)` material aligned with the
  conventions. The risk is downstream overreading: tensor-site strict maps
  should not imply a preferred ordering, and AND/OR particle-count sectors
  should not be read as bosonic, fermionic, para, Fock, or fusion sectors.

- Boson/fermion/fusion boundaries are well guarded, but AQM-74 should make the
  bosonic finite-mode one-particle Fock comparison status explicit. R37 found
  AQM-72 and AQM-73 cleanly defer parafermions and fusion categories. R38's
  question is narrower: Step 10 asked for tensor/Fock sector comparisons under
  choices, while AQM-74 only records a CAR one-particle map and then defers
  CCR/Fock generally.

- Finite-ring database overclaiming is mostly under control. R39, R41, and
  R42 all independently found the schema-only SQLite and in-memory CSV review
  export boundary preserved. The remaining risk is visual/status drift in
  AQM-81 and AQM-85 making blocked database-backed rows look like special
  mathematical statuses.

- Residue-site, nilpotent-sensitive, and product-ring layers are separated
  well. R42 found no definite issue in AQM-82--AQM-83: nilpotents are not
  counted as extra residue points, product-ring tensor factors are limited to
  selected workflows, and arbitrary finite-ring decomposition remains blocked.
  Later edits should preserve that discipline.

- Infinite-boundary categories are useful but need vocabulary placement. AQM-84
  categories such as finite-support, algebraic quasi-local, generic-sector
  proposal, and completion proposal are good prose classifiers. They become
  risky when imported into QSA agreement tables as if they were `(au)` status
  tokens.

No direct contradictions between Wave 1 reviewers were found. The apparent
tension is conceptual rather than reviewer-to-reviewer: AQM-84's proposal
labels are useful boundary prose, while AQM-85 treats them too much like table
statuses. R36, R37, R42, and R44 "no issue" reviews are compatible with the
targeted defects found by R38--R41 and R43.

## Findings To Verify Before Editing

- For AQM-79, verify the intended split of variables before editing:
  use one symbol, e.g. `s`, for `U=D(s)` and localized labels in `R_s^2`, and a
  separate support selector, e.g. `h`, with polynomial labels in `R^2` or
  classes modulo `rad(h)` for `W_h^red`.

- Decide the status-vocabulary policy globally before local table edits:
  either add AQM-84 boundary labels to `CONVENTIONS.md` as sanctioned table
  labels, or keep `(au)` table cells restricted to existing tokens and move
  boundary categories into prose/witness columns.

- For AQM-76, choose whether Step 12 should be explicitly field-base-only or
  should be rewritten uniformly with a named base `B` as
  `T^*_{X/B,x}` / `Omega^1_{A/B}`. Check the rewrite against AQM-77's
  `Z/4Z` and dual-number examples.

- Before changing AQM-74's CCR/Fock language, verify whether AQM-19 already
  supplies a local bosonic one-particle sector map acceptable for the QSA
  evidence contract, or whether AQM-74 should explicitly defer that narrower
  comparison.

- Before changing AQM-66 statuses, decide whether the table should keep a
  single composite status column or split status by workflow. The paired
  AQM-67--AQM-70 shards now close some but not all finite-set boundary cases.

- When repairing AQM-86, verify the cited row names and values against the
  run-bundle CSV, not a top-level `data/` path.

## Recommended Action Order

1. Fix the AQM-79 regular-function/support-selector ambiguity first. It is the
   only issue in this arc that can directly produce a wrong mathematical
   reading of a Weyl operator construction.

2. Normalize QSA status vocabulary in one pass: AQM-65's comparison evidence
   wording, AQM-81's ad hoc markers, and AQM-84/AQM-85's proposal-label
   handling. Treat AQM-66's composite statuses as part of the same cleanup if
   table shape changes are acceptable.

3. Split AQM-85's infinite-boundary row so algebraic generic sectors already
   locally recorded for `F_q(t)` and `Q` are not hidden under completion
   blockers.

4. Clarify base and point-selection dependencies: AQM-76 base notation and
   AQM-75's missing AQM-14 anchor.

5. Clean the smaller precision and reproducibility issues: AQM-86 CSV path,
   AQM-66 stale empty-set status, AQM-68 tensor-product coherence and
   one-point edge case, and AQM-74's `R_G` inverse wording plus bosonic Fock
   status sentence.

6. Preserve the no-overclaim boundaries that Wave 1 found healthy: no populated
   finite-ring database claim, no arbitrary finite-ring classification claim,
   no fusion-category technical construction without sources, no statistics or
   Fock interpretation for the finite AND/OR grammar, and no agreement or
   inequivalence claim without a recorded map, invariant, or obstruction.
