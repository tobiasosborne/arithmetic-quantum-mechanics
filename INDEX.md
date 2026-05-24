# INDEX.md - Script, Output, And Report Manifest

This manifest indexes the evidence layer behind the sharded lab book rooted at
`report.tex`. Evidence-producing scripts and run bundles are registered below.

## Run Bundles

Generated data and figures will live under
`runs/<YYYY-MM-DD>-<slug>/{data,figures}/`. Each run must include a
`README.md` with hypothesis, exact command, headline finding, and next steps.

| Run | Topic | What it covers |
|---|---|---|
| `runs/2026-05-24-toric-supercharge/` | Toric code / local-check ghosts | Algebraic validation of the auxiliary-fermion supercharge construction for a `k=4` toric-code instance. |
| `runs/2026-05-24-toric-chain-ghost-unification/` | Toric code / chain complex | Algebraic validation that `C_2 -> C_1 -> C_0` boundary maps determine the same CSS check supports used by the ghost supercharge. |
| `runs/2026-05-24-symplectic-css-bridge/` | Toric code / symplectic CSS bridge | Exact prime-field validation that oriented boundary maps produce an isotropic CSS stabilizer subspace. |
| `runs/2026-05-24-css-supercharge-symplectic-dictionary/` | CSS codes / symplectic supercharge dictionary | Exact validation of the CSS isotropic-subspace to ghost-supercharge dictionary for representative CSS matrices. |
| `runs/2026-05-24-steane-supercharge-molecular/` | Steane code / molecular supercharge | Exact validation of the sourced Steane CSS spaces, logical symplectic quotient, six-fermion supercharge, and cohomology dimensions. |

## Quick Start

```bash
make check-report-shards
make report
julia --project=. -e 'using Pkg; Pkg.test()'
julia --project=. scripts/run_all.jl --fast
```

## Script To Output Manifest

One row per script that writes files. Add rows in the same change that adds a
producer.

| Script | Tool | Run bundle | CSV outputs | Figures | Report shard |
|---|---|---|---|---|---|
| `scripts/lattice_codes/toric_supercharge_validation.jl` | Julia | `runs/2026-05-24-toric-supercharge/` | `data/toric_supercharge_summary.csv` | _none_ | `AQM-05-TORIC-SUPERCHARGE` |
| `scripts/lattice_codes/toric_chain_ghost_unification.jl` | Julia | `runs/2026-05-24-toric-chain-ghost-unification/` | `data/toric_chain_ghost_unification.csv` | _none_ | `AQM-05-TORIC-SUPERCHARGE`, `AQM-06-TORIC-CHAIN-GHOST-PROOF`, `AQM-07-TORIC-OPERATOR-RELATION` |
| `scripts/lattice_codes/symplectic_css_bridge_validation.jl` | Julia | `runs/2026-05-24-symplectic-css-bridge/` | `data/symplectic_css_bridge_summary.csv` | _none_ | `AQM-08-SYMPLECTIC-CSS-BRIDGE` |
| `scripts/lattice_codes/css_supercharge_symplectic_dictionary.jl` | Julia | `runs/2026-05-24-css-supercharge-symplectic-dictionary/` | `data/css_supercharge_symplectic_dictionary.csv` | _none_ | `AQM-09-SYMPLECTIC-SUPERCHARGE-DICTIONARY` |
| `scripts/lattice_codes/steane_supercharge_molecular.jl` | Julia | `runs/2026-05-24-steane-supercharge-molecular/` | `data/steane_molecular_summary.csv`, `data/steane_molecular_vectors.csv`, `data/steane_cohomology_by_degree.csv` | _none_ | `AQM-10-STEANE-SYMPLECTIC-MOLECULAR`, `AQM-11-STEANE-SUPERCHARGE-COHOMOLOGY` |

## CSV Reverse Lookup

Every CSV must be listed here and in `data/SCHEMA.md`.

| CSV path | Producing script | Schema section |
|---|---|---|
| `runs/2026-05-24-toric-supercharge/data/toric_supercharge_summary.csv` | `scripts/lattice_codes/toric_supercharge_validation.jl` | `toric_supercharge_summary.csv` |
| `runs/2026-05-24-toric-chain-ghost-unification/data/toric_chain_ghost_unification.csv` | `scripts/lattice_codes/toric_chain_ghost_unification.jl` | `toric_chain_ghost_unification.csv` |
| `runs/2026-05-24-symplectic-css-bridge/data/symplectic_css_bridge_summary.csv` | `scripts/lattice_codes/symplectic_css_bridge_validation.jl` | `symplectic_css_bridge_summary.csv` |
| `runs/2026-05-24-css-supercharge-symplectic-dictionary/data/css_supercharge_symplectic_dictionary.csv` | `scripts/lattice_codes/css_supercharge_symplectic_dictionary.jl` | `css_supercharge_symplectic_dictionary.csv` |
| `runs/2026-05-24-steane-supercharge-molecular/data/steane_molecular_summary.csv` | `scripts/lattice_codes/steane_supercharge_molecular.jl` | `steane_molecular_summary.csv` |
| `runs/2026-05-24-steane-supercharge-molecular/data/steane_molecular_vectors.csv` | `scripts/lattice_codes/steane_supercharge_molecular.jl` | `steane_molecular_vectors.csv` |
| `runs/2026-05-24-steane-supercharge-molecular/data/steane_cohomology_by_degree.csv` | `scripts/lattice_codes/steane_supercharge_molecular.jl` | `steane_cohomology_by_degree.csv` |

## Report Shards

| Label | Source | Title |
|---|---|---|
| `AQM-00-FRONTMATTER` | `report/sections/00_frontmatter_status.tex` | Frontmatter, Status, and Scope |
| `AQM-01-PROGRAMME-MAP` | `report/sections/01_programme_map.tex` | Programme Map |
| `AQM-02-LAB-LOG` | `report/sections/02_lab_log.tex` | Lab Log |
| `AQM-03-REPRO-MAP` | `report/sections/03_reproducibility_map.tex` | Reproducibility Map |
| `AQM-04-SOURCES-QUESTIONS` | `report/sections/04_source_queue_open_questions.tex` | Source Queue and Open Questions |
| `AQM-05-TORIC-SUPERCHARGE` | `report/sections/05_toric_supercharge_checks.tex` | Toric Code Supercharge From Local Checks |
| `AQM-06-TORIC-CHAIN-GHOST-PROOF` | `report/sections/06_toric_chain_ghost_proof.tex` | Proof of the Toric Chain-to-Ghost Lift |
| `AQM-07-TORIC-OPERATOR-RELATION` | `report/sections/07_toric_operator_relation.tex` | Operator Relation Between Cellular and Ghost Supercharges |
| `AQM-08-SYMPLECTIC-CSS-BRIDGE` | `report/sections/08_symplectic_css_bridge.tex` | Chain Complexes as Symplectic CSS Stabilizers |
| `AQM-09-SYMPLECTIC-SUPERCHARGE-DICTIONARY` | `report/sections/09_symplectic_supercharge_dictionary.tex` | Symplectic Dictionary for CSS Supercharges |
| `AQM-10-STEANE-SYMPLECTIC-MOLECULAR` | `report/sections/10_steane_symplectic_molecular.tex` | Steane Code Symplectic Data in Molecular Detail |
| `AQM-11-STEANE-SUPERCHARGE-COHOMOLOGY` | `report/sections/11_steane_supercharge_cohomology.tex` | Steane Code Fermions, Supercharge, and Cohomology |

## Source Topics

Source manifests should be created under `references/<topic>/SOURCES.md`.

| Topic | Manifest | Status |
|---|---|---|
| Weil conjectures and zeta functions | _pending_ | No sources acquired. |
| Arithmetic quantum mechanics | _pending_ | No sources acquired. |
| Supersymmetric quantum mechanics | _pending_ | No sources acquired. |
| Toric codes and Levin-Wen models | `references/toric_code/SOURCES.md` | Kitaev arXiv source bundle acquired for the toric-code stabilizer convention. |
| Symplectic QECC and stabilizer geometry | `references/symplectic_qecc/SOURCES.md` | Gottesman and Ashikhmin-Knill arXiv source bundles acquired for stabilizer symplectic conventions. |
