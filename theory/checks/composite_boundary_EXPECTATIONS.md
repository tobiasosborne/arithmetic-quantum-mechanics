# Composite relative boundary: checker expectations

The independent exact checker is `composite_boundary_check.py`.
Its first preregistration is preserved in
`docs/research-drafts/composite-boundary/EXPECTATIONS.md`; the executed
coverage and all scoped limitations are frozen in
`numerics/composite-boundary/results/RESULTS.md`.

Green executes nine gates and 76,584 exact comparisons over F4/F2,
F9/F3, F16/F2, F16/F4, F27/F3 and F8/F2. There is no floating tolerance.
Finite field operations are integer tables; sparse vector probabilities
are rational; Fourier phases are exact cyclotomic coefficients.

| Gate | Principal target | Named red suffixes |
|---|---|---|
| C1 | Hecke composition control and its 1/4 return | collective |
| C2 | Actual multiplication graph and simultaneous invariants | product, diagonal-action |
| C3 | Relative Frobenius matrix units and collective descent | identity, diagonal-relative, separate-descent |
| C4 | Copied preparation, positive reference mass and first grade | drop-grade, reset-reference |
| C5 | Full/identity/dephased probabilities 1/0/1/n | dephase, omit-invariant, normalizer |
| C6 | Coherent sums versus classical tags; retained histories | off-diagonal, omit-outcome |
| C7 | Fixed-base embeddings, twists, towers and J/V comparisons | embedding, wrong-sector |
| C8 | First-register field Fourier phase and retained return | fourier-phase, fourier-outcome |
| C9 | Multiplicity traces and implementer/channel spectra | multiplicity, channel-spectrum |

Every suffix is available as `--red-<suffix>`. Plain `--red` aliases the
actual collective mutation; legacy `--red <suffix>` remains supported.
There are nineteen distinct data mutations and twenty discovered standalone
flags. Each must exit one with JSON status FAIL and its named mathematical
gate; parser failures do not satisfy the mutation contract.

The critic's n=1 scope repair has separate root evidence in
`numerics/composite-boundary/results/ROOT-REPAIRS.json`: the full code and
spectral formulas include n=1, while moving-sector conditioning is absent.
The primary six-fibre suite does not purport to test a nonzero moving
boundary at n=1. General positivity and quantifiers rely on the structured
proofs and capped review, not these finite computations.
