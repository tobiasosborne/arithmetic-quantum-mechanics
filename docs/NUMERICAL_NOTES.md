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

The symplectic CSS bridge run is
`runs/2026-05-24-symplectic-css-bridge/data/symplectic_css_bridge_summary.csv`.
It validates the oriented toric boundary matrices over `F_2`, `F_3`, and
`F_5`, checking both `partial_1 partial_2=0` and isotropy of the induced CSS
subspace in the Pauli symplectic module.

The CSS supercharge/symplectic dictionary run is
`runs/2026-05-24-css-supercharge-symplectic-dictionary/data/css_supercharge_symplectic_dictionary.csv`.
It validates the generator-ghost and logical-symplectic dimension counts for
the Steane CSS code over `F_2` and a qutrit CSS toy code over `F_3`.

The Steane molecular supercharge run is
`runs/2026-05-24-steane-supercharge-molecular/`. It records the sourced
Gottesman-table binary spaces, `L`, `L^perp`, logical representatives, and the
full six-ghost cohomology dimensions `2,12,30,40,30,12,2`.

The Steane Clifford/Koszul morphism run is
`runs/2026-05-24-steane-clifford-koszul-morphisms/`. It validates that
transversal Hadamard is an exact automorphism of the same six-ghost
supercharge after ghost swapping, while transversal phase is a chain
isomorphism to a changed generator presentation and compares back by the common
syndrome-sector homotopy retract.

## Commands

```bash
make check-report-shards
make report
julia --project=. -e 'using Pkg; Pkg.test()'
julia --project=. scripts/run_all.jl --fast
```
