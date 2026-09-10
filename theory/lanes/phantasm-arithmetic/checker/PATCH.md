# PATCH — proposed trunk integration

This lane made no trunk edits.  Apply by exact content copy and anchored
replacement; do not use line numbers.  Installing finite controls does not
promote SP-TRACE, SP-FROB or SP-SUBSYS.

## 1. Install checker artifacts

Copy exact contents:

- `theory/lanes/phantasm-arithmetic/checker/phantasm_arithmetic_check.py`
  to `theory/checks/phantasm_arithmetic_check.py`;
- `theory/lanes/phantasm-arithmetic/checker/EXPECTATIONS.md`
  to `theory/checks/phantasm_arithmetic_EXPECTATIONS.md`.

The checker imports the exact APIs and versions pinned in `RUNS.md` and leaves
`phantasm_reuse_check.py` unchanged.  Help advertises thirteen concrete red
flags and no generic placeholder.

## 2. Update SP-TRACE finite evidence

Within `claims/PHANTASM-DAG.md` block `## SP-TRACE`, replace:

    - Checks: theory/checks/phantasm_reuse_check.py

with:

    - Checks: theory/checks/phantasm_reuse_check.py,theory/checks/phantasm_arithmetic_check.py

Replace its falsifier paragraph by:

    **Falsifier scope.** Implemented: phantasm_reuse_check.py R6 retains its
    F81/F9 nonstandard-character sample. phantasm_arithmetic_check.py A1--A4
    adds F27/F3 degree-equals-characteristic traces, restricted Gram ranks
    zero/six/twelve, F3/F9/F81 tower transitivity, named-character separation,
    and exact rank-zero/one/two half-form product, star, unit and trace controls.
    These finite fields and sparse labels do not prove arbitrary-rank or
    all-extension statements.

## 3. Update SP-FROB finite evidence

Within block `## SP-FROB`, replace its reuse-only Checks line with the same two
checker paths.  Replace its falsifier paragraph by:

    **Falsifier scope.** Implemented: phantasm_reuse_check.py R6 retains its
    selected F81/F9 relative-power sample. phantasm_arithmetic_check.py A5--A7
    checks F27/F3 cube/order-three and F81/F9 ninth-power/order-two
    K-linearity, trace/character invariance, sparse rank-one/two Weyl
    covariance, rank zero, bijectivity, inverse channel action and ordinary
    trace. A6 asserts its per-field/rank census
    (19683,12393,531441,85293), totaling 648810. No dense F81 rank-two matrix
    is formed, and finite success does not prove arbitrary-rank covariance.

## 4. Update SP-SUBSYS finite evidence

Within block `## SP-SUBSYS`, replace `- Checks: none` by:

    - Checks: theory/checks/phantasm_arithmetic_check.py

and replace `- Evidence: planned` by `- Evidence: draft`.

Replace its falsifier paragraph by:

    **Falsifier scope.** Implemented: phantasm_arithmetic_check.py A8--A12
    checks a non-coordinate F3 symplectic injection/complement, all 729 Weyl
    compatibility actions, ordinary decoder Kraus/index equality and trace
    duality, asymmetric/classically correlated/Bell inputs, Weyl
    characteristic restriction, phase cancellation, and an explicit
    three-register compatible direct/iterated decoder on 729 matrix units and
    three states. The M3 fixture satisfies D1710's explicit compatibility
    equation; it does not establish compatibility for arbitrary chosen data.

## 5. Update canonical tested-in cells without promotion

In `claims/CLAIMS.md`, append
`` `theory/checks/phantasm_arithmetic_check.py` (exact finite scope only; see DAG) ``
to the SP-TRACE and SP-FROB tested-in cells after the existing reuse checker.
Replace SP-SUBSYS's proposed-falsifier cell by that arithmetic-checker wording.
Keep all statuses `SKETCH` until proof/review/adjudication requirements are met.

## 6. Update labbook provenance

In `labbook/sections/symplectic_phantasm_contracts.tex`, replace the exact
SP-TRACE and SP-FROB provenance phrases `Finite reuse probe at its declared
scope` by, respectively:

    Finite reuse probe plus exact F27/F3 and F81/F9 trace/Weyl controls

and

    Finite reuse probe plus exact relative-Frobenius sparse covariance controls

Replace SP-SUBSYS's `Proposed falsifier only` phrase by:

    Exact F3 non-coordinate decoder and compatible-tower controls at their declared scope

## 7. Coordinator verification

Run the installed checker green and all thirteen help-advertised reds, the
unchanged reuse checker at its existing green/red scope, then the Phantasm
contract and ordinary labbook/session-close gates.  This patch records draft
finite evidence only.
