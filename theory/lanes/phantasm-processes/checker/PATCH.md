# PATCH — proposed trunk integration

This lane made no trunk edits.  Apply by exact content copy and anchored
replacement; do not use line numbers.  Installing finite controls does not
promote SP-SCALAR or SP-CP.

## 1. Install checker artifacts

Copy exact contents:

- `theory/lanes/phantasm-processes/checker/phantasm_process_check.py`
  to `theory/checks/phantasm_process_check.py`;
- `theory/lanes/phantasm-processes/checker/EXPECTATIONS.md`
  to `theory/checks/phantasm_process_EXPECTATIONS.md`.

The checker is standalone.  Help advertises exactly nineteen concrete
`--red-*` flags and no generic placeholder.

## 2. Record SP-SCALAR finite evidence

Within the block anchored by `## SP-SCALAR`, replace `- Checks: none` with

    - Checks: theory/checks/phantasm_process_check.py

and replace `- Evidence: planned` with `- Evidence: draft`.

Replace the paragraph beginning with
`**Falsifier scope.** Use identity, a rank-one projection` by:

    **Falsifier scope.** Implemented: phantasm_process_check.py P1--P2
    checks the exact one-Kraus scalar modulus law on all qutrit matrix units,
    distinguishes projective representatives from actual CP maps, and compares
    the contraction criterion with exact rank-one probability tests including
    zero. Zero-probability conditioning is rejected as an explicit datum, not
    by division. These finite controls do not prove the arbitrary-dimensional
    statement or select a representative norm.

## 3. Record SP-CP finite evidence

Within the block anchored by `## SP-CP`, replace `- Checks: none` with the same
checker path and replace `- Evidence: planned` with `- Evidence: draft`.

Replace the paragraph beginning with
`**Falsifier scope.** Exact rational Kraus examples` by:

    **Falsifier scope.** Implemented: phantasm_process_check.py P3--P11
    checks exact rational/Gaussian-rational block Kraus action against an
    independent superoperator-coefficient route and Choi positivity from
    actual matrix-unit outputs. It checks ordinary block traces, equality of
    maps rather than Kraus lists, composition/tensor paths, outcome-first
    retained blocks, earlier/later sequential pairs, listed-factor tensor
    outcomes, rectangular ordinary-trace adjoints, the non-TNI discard
    adjoint, and finite D1327 comparisons. This finite scope does not prove
    arbitrary-dimensional Kraus exhaustion or arithmetic-source exhaustion.

## 4. Update canonical tested-in cells without promotion

In `claims/CLAIMS.md`, use the rows beginning ``| `SP-SCALAR` |`` and
``| `SP-CP` |`` as anchors.  Replace each final proposed-falsifier cell with:

    `theory/checks/phantasm_process_check.py` (exact finite scope only; see DAG)

Keep both statuses `SKETCH` until their separate proof/review/adjudication
requirements are satisfied.

## 5. Update labbook provenance

In `labbook/sections/symplectic_phantasm_contracts.tex`, replace:

    \provenance{SP-SCALAR}{Inherited: FRP-CP; remaining comparison in the DAG}{Proposed falsifier only}{SKETCH; promotion review pending}

with:

    \provenance{SP-SCALAR}{Inherited: FRP-CP; remaining comparison in the DAG}{Exact qutrit representative/branch controls at their declared finite scope}{SKETCH; promotion review pending}

Replace:

    \provenance{SP-CP}{Inherited: FRP-CP; remaining comparison in the DAG}{Proposed falsifier only}{SKETCH; promotion review pending}

with:

    \provenance{SP-CP}{Inherited: FRP-CP; remaining comparison in the DAG}{Exact rational block, outcome and adjoint controls at their declared finite scope}{SKETCH; promotion review pending}

## 6. Coordinator verification

Run the installed checker green and all nineteen help-advertised red modes,
then the Phantasm contract and ordinary labbook/session-close gates.  This
patch records draft finite evidence only.
