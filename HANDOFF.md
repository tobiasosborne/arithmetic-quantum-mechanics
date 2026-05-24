# HANDOFF.md

Session-state file for incoming agents. This is not an authoritative source for
mathematical claims; use `report.tex`, `INDEX.md`, `CONVENTIONS.md`, and local
source manifests for that.

## Current Frontier

Initial infrastructure is in place for a lab-book style research workspace
about Weil/zeta functions, arithmetic quantum mechanics, supersymmetric quantum
mechanics, and Kitaev/Levin-Wen/toric-code models. The first checked item is
the ghost-extended local-check supercharge formulation of the toric code in
`AQM-05-TORIC-SUPERCHARGE`.

## Most Recent Session

**2026-05-24 - Lab-book scaffold created.**

- Created the sharded LaTeX master `report.tex` with five initial shards under
  `report/sections/`.
- Added report navigation files, scientific-practice guidance, conventions,
  an index manifest, source/reference placeholders, run-bundle discipline, and
  data/figure placeholders.
- Added a minimal Julia package scaffold, local script runner, report-shard
  checker, Makefile, and local CI script.
- Local tool check found Julia, LaTeX `latexmk`, and `bd`; `sage` and `gap`
  were not on PATH in this shell.

**2026-05-24 - Toric-code ghost supercharge run added.**

- Registered Kitaev's arXiv TeX source bundle under
  `references/toric_code/`.
- Added the convention `Q=sum_i c_i^* P_i`, one auxiliary fermion per local
  stabilizer check, with `P_i=(I-S_i)/2`.
- Implemented an algebraic validator that avoids full Hilbert matrices. For
  `k=4` it checks commuting local stabilizers, rank `2k^2-2`, code dimension
  `4`, and the CAR/projector certificates for `Q^2=0` and
  `{Q,Q^*}=H_TC`.
- Added the boundary-map unification: the chain complex
  `C_2 -> C_1 -> C_0` gives `H_X=partial_1`, `H_Z=partial_2^T`, so
  `partial_1 partial_2=0` is the CSS commutation condition and its rows/columns
  are exactly the ghost-supercharge check supports.
- Added a full proof in `AQM-06-TORIC-CHAIN-GHOST-PROOF`: cellular classes
  `[a] in ker(delta^1)/im(delta^0)` map to normalized orbit sums in the code
  space, and the ghost anticommutator follows from the CAR and commuting
  projectors.

## Next Useful Steps

1. Acquire and register core local sources before adding content claims.
2. Decide first fixed conventions: zeta normalization, Frobenius direction,
   SUSY-QM grading/signs, and lattice-model boundary/orientation conventions.
3. Create the first run bundle only when there is a concrete source-backed
   invariant to compute.
