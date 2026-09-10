# PATCH — proposed trunk integration

This lane made no trunk edits. Apply by content copy and anchored replacements;
do not use line numbers. The checker does not change claim status.

## 1. Install the two checker artifacts

Copy exact contents:

- `theory/lanes/phantasm-stage1/egorov-checker/egorov_tensor_check.py`
  to `theory/checks/phantasm_egorov_check.py`;
- `theory/lanes/phantasm-stage1/egorov-checker/EXPECTATIONS.md`
  to `theory/checks/phantasm_egorov_EXPECTATIONS.md`.

The destination checker auto-discovers the repository from its parent path
and imports `GF` and `CycRing` from the existing adjacent
`theory/checks/wh_kappa_check.py`. In the lane it also accepts `--root`.

## 2. Update the SP-EGOROV DAG record

Within the section anchored by `## SP-EGOROV`, replace the exact field

    - Checks: none

with

    - Checks: theory/checks/phantasm_egorov_check.py

and replace

    - Evidence: planned

with

    - Evidence: draft

Replace the paragraph beginning with the exact anchor
`**Falsifier scope.** Enumerate the affine group on F3^2` by:

    **Falsifier scope.** Implemented: phantasm_egorov_check.py E1--E8
    enumerates all 216 affine symplectic arrows on F3^2, checks identities,
    inverses and all 46,656 ordered products pointwise, checks the induced
    Weyl-algebra action and independently checks translation, Fourier and
    shear operator covariance. It includes the zero space and a nonstandard
    additive character over F9. Exact finite success is not a proof of the
    arbitrary-rank or projective-implementation statement.

The existing required-mutations sentence may remain; the checker includes
the semidirect-order and translated-phase/sign defects plus gate-specific
controls listed in its adjacent expectations file.

## 3. Update the SP-TENSOR DAG record

Within the section anchored by `## SP-TENSOR`, replace

    - Checks: theory/checks/phantasm_reuse_check.py

with

    - Checks: theory/checks/phantasm_reuse_check.py,theory/checks/phantasm_egorov_check.py

Replace the paragraph beginning with the exact anchor
`**Falsifier scope.** Implemented: phantasm_reuse_check.py R5` by:

    **Falsifier scope.** Implemented: phantasm_reuse_check.py R5 checks the
    transported product against independently tensored inherited operators,
    including a zero factor. phantasm_egorov_check.py E7 and E9 check the
    literal rank-zero unit, all 81 rank-two operator/tensor and symmetry
    comparisons over F3, and all 3,779,136 factorwise affine naturality cases.
    The written arbitrary-rank and projective-coherence argument is still owed.

## 4. Update the canonical claim evidence columns without promotion

In `claims/CLAIMS.md`, use the row beginning with ``| `SP-EGOROV` |`` as the
anchor. Replace its final cell

    `claims/PHANTASM-DAG.md` (proposed falsifier only; none run)

with

    `theory/checks/phantasm_egorov_check.py` (exact finite scope only; see DAG)

In the row beginning with ``| `SP-TENSOR` |``, replace its final cell

    `theory/checks/phantasm_reuse_check.py` (finite bridge scope only; see DAG)

with

    `theory/checks/phantasm_reuse_check.py`, `theory/checks/phantasm_egorov_check.py` (finite bridge and affine-naturality scopes only; see DAG)

Keep both statuses `SKETCH` unless the separate proof/review/adjudication
contract is satisfied.

## 5. Update the labbook provenance descriptions

In `labbook/sections/symplectic_phantasm_contracts.tex`, replace the exact
SP-EGOROV provenance line

    \provenance{SP-EGOROV}{Inherited: F1-REAL; remaining comparison in the DAG}{Proposed falsifier only}{SKETCH; promotion review pending}

with

    \provenance{SP-EGOROV}{Inherited: F1-REAL; remaining comparison in the DAG}{Exact F3/F9 affine and generator falsifier at its declared finite scope}{SKETCH; promotion review pending}

Replace the exact SP-TENSOR provenance line

    \provenance{SP-TENSOR}{Inherited: F1-FUNCT; remaining comparison in the DAG}{Finite reuse probe at its declared scope}{SKETCH; promotion review pending}

with

    \provenance{SP-TENSOR}{Inherited: F1-FUNCT; remaining comparison in the DAG}{Finite reuse probe plus exact F3 rank-two affine naturality control}{SKETCH; promotion review pending}

## 6. Coordinator verification after integration

Run the installed checker green and all nine `--help`-advertised red modes,
then run `python3 theory/checks/phantasm_contract_check.py` and the ordinary
labbook/session-close gates. If a contract mutation list requires registering
the new checker path or evidence wording, amend it in the coordinator lane;
this checker lane deliberately did not touch concurrently edited contract
files.
