# PATCH — proposed trunk integration

This lane made no trunk edits.  Apply by exact content copy and anchored
replacement; do not use line numbers.  Installing the checker does not promote
SP-SUM.

## 1. Install checker artifacts

Copy exact contents:

- `theory/lanes/phantasm-sum/checker/phantasm_sum_check.py`
  to `theory/checks/phantasm_sum_check.py`;
- `theory/lanes/phantasm-sum/checker/EXPECTATIONS.md`
  to `theory/checks/phantasm_sum_EXPECTATIONS.md`.

The checker locates the repository automatically and imports the adjacent
installed `phantasm_stabilizer_check.py` for U2's optional exact qutrit census.
Install paths and hashes are recorded in `RUNS.md`.  Help advertises ten
concrete red flags and no generic placeholder.

## 2. Record finite evidence in the SP-SUM DAG block

Within the block anchored by `## SP-SUM`, replace:

    - Checks: none

with:

    - Checks: theory/checks/phantasm_sum_check.py

and replace `- Evidence: planned` with `- Evidence: draft`.

Replace the paragraph beginning
`**Falsifier scope.** For H=C plus C^3` by:

    **Falsifier scope.** Implemented: phantasm_sum_check.py U1--U8
    constructs all 169 preparation/adjoint rectangular matrix-unit words for
    p=3 and ranks zero through two; checks D1707 block action, composition and
    dagger on repeated and empty lists with explicit 0xn/nx0 shapes; derives
    coherent/tagged dimensions 16/10, 25/11, 36/18 and 81/81; and checks
    block dephasing on every 4x4 matrix unit, projection completeness,
    unitality, idempotence, exact range and ordinary trace. An imported exact
    qutrit census supplies the finite diag(1,1,0) coherent-sum witness. These
    finite controls do not prove arbitrary ranks or a rig/biproduct theorem.

The existing two required mutation families are covered by `pure-two-unit`
and `coherent-tagged`; adjacent expectations register seven additional
matrix-unit, list, empty-object, projection and trace controls.

## 3. Update the canonical tested-in cell without promotion

In `claims/CLAIMS.md`, use the row beginning ``| `SP-SUM` |`` as anchor.
Replace its final cell

    `claims/PHANTASM-DAG.md` (proposed falsifier only; none run)

with

    `theory/checks/phantasm_sum_check.py` (exact finite scope only; see DAG)

Keep status `SKETCH` until proof/review/adjudication requirements are met.

## 4. Update labbook provenance

In `labbook/sections/symplectic_phantasm_contracts.tex`, replace:

    \provenance{SP-SUM}{Inherited: F1-REAL; remaining comparison in the DAG}{Proposed falsifier only}{SKETCH; promotion review pending}

with:

    \provenance{SP-SUM}{Inherited: F1-REAL; remaining comparison in the DAG}{Exact p=3 coherent/tagged/dephasing controls at their declared finite scope}{SKETCH; promotion review pending}

## 5. Coordinator verification

Run the installed checker green and all ten help-advertised reds, followed by
the Phantasm contract and ordinary labbook/session-close gates.  This patch
records draft finite evidence only.
