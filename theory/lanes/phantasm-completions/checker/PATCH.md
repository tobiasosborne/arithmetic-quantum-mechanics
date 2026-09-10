# PATCH — proposed trunk integration

This lane made no trunk edits.  Apply by exact content copy and anchored
replacement; do not use line numbers.  Installing finite controls does not
promote SP-FOCK, SP-PRIME or SP-BC-CONTROL.

## 1. Install checker artifacts

Copy exact contents:

- `theory/lanes/phantasm-completions/checker/phantasm_completions_check.py`
  to `theory/checks/phantasm_completions_check.py`;
- `theory/lanes/phantasm-completions/checker/EXPECTATIONS.md`
  to `theory/checks/phantasm_completions_EXPECTATIONS.md`.

The checker uses only the Python standard library.  Help advertises fifteen
concrete red flags and no generic placeholder.

## 2. Record SP-FOCK finite evidence

Within `claims/PHANTASM-DAG.md` block `## SP-FOCK`, replace
`- Checks: none` by:

    - Checks: theory/checks/phantasm_completions_check.py

and `- Evidence: planned` by `- Evidence: draft`.

Replace its falsifier paragraph by:

    **Falsifier scope.** Implemented: phantasm_completions_check.py F1--F3
    checks exact rational symmetrizers through sector four in dimensions
    zero/one/two, sector ranks, vacuum, one-mode factorial normalization, the
    binomial exponential norm square and homogeneous naturality, contraction
    composition, and actual tensor-power growth 1,2,4,8,16 for 2I on
    symmetric test vectors. Bounded extension and the infinite growth
    conclusion remain written-proof obligations.

## 3. Record SP-PRIME finite evidence

Within block `## SP-PRIME`, install the same checker path and draft evidence.
Replace its falsifier paragraph by:

    **Falsifier scope.** Implemented: phantasm_completions_check.py P1--P2
    checks empty/{2}/{3}/{2,3}/{2,3,5} identity-insertion maps for dimensions
    2,3,4, all available triangles, star/product/unit, exact a*a
    characteristic polynomials, faithful and pure compatible product states,
    positivity, GNS Gram ranks 576/192/3, cyclicity and a concrete
    nonseparating pure cyclic vector. Infinite completion and state extension
    remain written-proof obligations; no representation nonfaithfulness or
    factor type is inferred.

## 4. Record SP-BC-CONTROL finite evidence

Within block `## SP-BC-CONTROL`, install the same checker path and draft
evidence.  Replace its falsifier paragraph by:

    **Falsifier scope.** Implemented: phantasm_completions_check.py B1--B4
    uses unbounded symbolic basis indices for semigroup/full adjoint
    divisibility/range laws,
    exact rational phases and root-average divisibility, prime-valuation
    dynamics, symbolic corner homomorphism/compression controls, rational
    b=2,3 integral tail intervals and dyadic b=1 lower witnesses. It uses no
    finite shift truncation. Self-adjointness, continuity and trace class are
    written-proof obligations, and no zeta-zero spectrum is tested.

## 5. Update canonical tested-in cells without promotion

In `claims/CLAIMS.md`, replace the final proposed-falsifier cell in each of the
SP-FOCK, SP-PRIME and SP-BC-CONTROL rows by:

    `theory/checks/phantasm_completions_check.py` (exact finite/symbolic scope only; see DAG)

Keep every status `SKETCH` until its separate proof/review/adjudication
requirements are satisfied.

## 6. Update labbook provenance

In `labbook/sections/symplectic_phantasm_contracts.tex`, replace the
`Proposed falsifier only` phrase for each named provenance row by:

- SP-FOCK: `Exact rational sector/exponential controls at their declared finite scope`;
- SP-PRIME: `Exact finite prime-embedding/product-state/GNS controls at their declared scope`;
- SP-BC-CONTROL: `Exact symbolic semigroup/dynamics and rational tail controls at their declared scope`.

## 7. Coordinator verification

Run the installed checker green and all fifteen help-advertised reds, then
the Phantasm contract and ordinary labbook/session-close gates.  This patch
records draft evidence only.
