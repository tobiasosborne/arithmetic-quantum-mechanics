# HANDOFF.md

Session-state file for incoming agents. This is not an authoritative source for
mathematical claims; use `report.tex`, `INDEX.md`, `CONVENTIONS.md`, and local
source manifests for that.

## Current Frontier

Initial infrastructure is in place for a lab-book style research workspace
about Weil/zeta functions, arithmetic quantum mechanics, supersymmetric quantum
mechanics, and Kitaev/Levin-Wen/toric-code models.

No sources, mathematical results, scripts, CSVs, or figures have been acquired
or checked yet.

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

## Next Useful Steps

1. Acquire and register core local sources before adding content claims.
2. Decide first fixed conventions: zeta normalization, Frobenius direction,
   SUSY-QM grading/signs, and lattice-model boundary/orientation conventions.
3. Create the first run bundle only when there is a concrete source-backed
   invariant to compute.
