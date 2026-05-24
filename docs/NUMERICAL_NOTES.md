# Numerical Notes

> Role: session log and computational scratch notes. This file is not the
> authoritative reference for scientific claims.
>
> - Main report: `report.tex`
> - Script/output manifest: `INDEX.md`
> - CSV schemas: `data/SCHEMA.md`
> - Reproducibility driver: `scripts/run_all.jl`
> - Session handoff: `HANDOFF.md`

## 2026-05-24 Scaffold Notes

Local command availability in this shell:

| Tool | Status |
|---|---|
| Julia | Found on PATH. |
| LaTeX `latexmk` | Found on PATH. |
| Beads `bd` | Found on PATH. |
| Sage | Not found on PATH. |
| GAP | Not found on PATH. |

The first algebraic run is
`runs/2026-05-24-toric-supercharge/data/toric_supercharge_summary.csv`. It
does not build full Hilbert matrices; it validates the toric-code ghost
supercharge through binary stabilizer algebra and fermion CAR identities.

The boundary-map unification run is
`runs/2026-05-24-toric-chain-ghost-unification/data/toric_chain_ghost_unification.csv`.
It validates `partial_1 partial_2=0`, the match between boundary-map supports
and stabilizer-check supports, and the homological dimension count `dim H_1=2`.

## Commands

```bash
make check-report-shards
make report
julia --project=. -e 'using Pkg; Pkg.test()'
julia --project=. scripts/run_all.jl --fast
```
