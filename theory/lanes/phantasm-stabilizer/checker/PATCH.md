# PATCH — proposed trunk integration

This lane made no trunk edits.  Apply by exact content copy and anchored
replacement; do not use line numbers.  Installing the finite checker does not
promote SP-STAB-REL.

## 1. Install checker artifacts

Copy exact contents:

- `theory/lanes/phantasm-stabilizer/checker/phantasm_stabilizer_check.py`
  to `theory/checks/phantasm_stabilizer_check.py`;
- `theory/lanes/phantasm-stabilizer/checker/EXPECTATIONS.md`
  to `theory/checks/phantasm_stabilizer_EXPECTATIONS.md`.

Install `theory/checks/phantasm_relations_check.py` first.  In the destination
layout this checker imports the adjacent exact classical API and
`wh_kappa_check.py`; its lane-only fallback path is then unused.  Help
advertises eighteen concrete `--red-*` modes and no generic red placeholder.

## 2. Record finite evidence in the SP-STAB-REL DAG block

Within the block anchored by the exact heading `## SP-STAB-REL`, replace:

    - Checks: none

with:

    - Checks: theory/checks/phantasm_stabilizer_check.py

and replace:

    - Evidence: planned

with:

    - Evidence: draft

Replace the paragraph beginning with the exact anchor
`**Falsifier scope.** Check the source generators for p=3,5` by:

    **Falsifier scope.** Implemented: phantasm_stabilizer_check.py S1--S5
    independently generates 216 qutrit projective Clifford matrices, 12
    qutrit stabilizer-state rays and 360 nonzero one-register amplitude
    classes. It compares these with all 389 zero/one-register affine
    relations through D1715's exact all-origin group-average equations,
    including rank-one projector certificates, zero, states and effects. It
    checks all 140,101 typed F3 compositions, all 389 daggers, 338
    state/effect tensors, 144 selected mixed tensors, exact cup/cap scalars,
    and a limited 30-state F5 convention control. Projective equality uses
    exact entry cross-products and keeps zero separate. This finite census
    does not prove the general presentation, fullness or equivalence.

The existing required-mutations sentence may remain.  Both of its defects are
implemented as `zero-collapse` and `phase-only`; the adjacent expectations
register eleven additional convention, construction and coherence controls.

## 3. Update the canonical tested-in cell without promotion

In `claims/CLAIMS.md`, use the row beginning with ``| `SP-STAB-REL` |`` as the
anchor.  Replace its final cell

    `claims/PHANTASM-DAG.md` (proposed finite controls only; none run)

with

    `theory/checks/phantasm_stabilizer_check.py` (exact finite scope only; see DAG)

Keep the status `SKETCH` until the proof, blind review and adjudication
requirements are separately satisfied.

## 4. Update labbook provenance

In `labbook/sections/symplectic_phantasm_contracts.tex`, replace the exact line

    \provenance{SP-STAB-REL}{Weyl-intertwiner construction; source comparison pending}{Proposed finite controls}{SKETCH; proof and review pending}

with

    \provenance{SP-STAB-REL}{Weyl-intertwiner construction; source comparison pending}{Exact F3 relation/amplitude census and limited F5 controls at their declared scope}{SKETCH; proof and review pending}

## 5. Coordinator verification

Run the installed checker green and all eighteen `--help`-advertised reds,
then run `python3 theory/checks/phantasm_contract_check.py` and the ordinary
labbook/session-close gates.  The checker path records draft finite evidence
only; admission still requires the proof/review/adjudication paths.
