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
| `runs/2026-05-24-steane-clifford-koszul-morphisms/` | Steane code / Clifford morphisms | Exact validation of transversal Hadamard and phase as Clifford/Koszul chain maps and homotopy equivalences. |
| `runs/2026-05-24-steane-all-clifford-ghost-gaussians/` | Steane code / Clifford group ghost Gaussians | Exact generator-level validation of arbitrary Clifford covariance and elementary GL6 ghost-Gaussian presentation moves. |
| `runs/2026-05-24-arithmetic-quantum-fields/` | Arithmetic quantum fields / finite function spaces | Exact `F_3` validation of pointwise symplectic function spaces, radicals, reduced Weyl labels, and observable algebra dimensions. |
| `runs/2026-05-24-projective-line-sheaf-fields/` | Projective arithmetic fields / sheaves | Exact `F_3` validation of \(\mathbf P^1\), \(H^0(\mathcal O(d))\otimes\mathbb F_3^2\), finite point evaluations, stalk germs, radicals, and reduced Weyl labels. |

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
| `scripts/lattice_codes/steane_clifford_koszul_morphisms.jl` | Julia | `runs/2026-05-24-steane-clifford-koszul-morphisms/` | `data/steane_clifford_koszul_summary.csv`, `data/steane_clifford_generator_maps.csv` | _none_ | `AQM-12-STEANE-CLIFFORD-KOSZUL-MORPHISMS` |
| `scripts/lattice_codes/steane_all_clifford_ghost_gaussians.jl` | Julia | `runs/2026-05-24-steane-all-clifford-ghost-gaussians/` | `data/steane_all_clifford_generator_summary.csv`, `data/steane_all_clifford_generator_images.csv`, `data/steane_ghost_gaussian_elementaries.csv` | _none_ | `AQM-13-CLIFFORD-GROUP-GHOST-GAUSSIAN-THEOREM` |
| `scripts/bridges/arithmetic_quantum_fields.jl` | Julia | `runs/2026-05-24-arithmetic-quantum-fields/` | `data/arithmetic_quantum_field_examples.csv`, `data/arithmetic_quantum_field_bases.csv` | _none_ | `AQM-14-ARITHMETIC-QUANTUM-FIELDS` |
| `scripts/bridges/projective_line_sheaf_fields.jl` | Julia | `runs/2026-05-24-projective-line-sheaf-fields/` | `data/projective_line_sheaf_field_summary.csv`, `data/projective_line_sheaf_field_basis_rows.csv`, `data/projective_line_stalk_rows.csv` | _none_ | `AQM-15-PROJECTIVE-SHEAF-FIELD-DEFINITIONS`, `AQM-16-PROJECTIVE-LINE-SHEAF-FIELD-CALCULATION`, `AQM-17-PROJECTIVE-LINE-STALKS` |

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
| `runs/2026-05-24-steane-clifford-koszul-morphisms/data/steane_clifford_koszul_summary.csv` | `scripts/lattice_codes/steane_clifford_koszul_morphisms.jl` | `steane_clifford_koszul_summary.csv` |
| `runs/2026-05-24-steane-clifford-koszul-morphisms/data/steane_clifford_generator_maps.csv` | `scripts/lattice_codes/steane_clifford_koszul_morphisms.jl` | `steane_clifford_generator_maps.csv` |
| `runs/2026-05-24-steane-all-clifford-ghost-gaussians/data/steane_all_clifford_generator_summary.csv` | `scripts/lattice_codes/steane_all_clifford_ghost_gaussians.jl` | `steane_all_clifford_generator_summary.csv` |
| `runs/2026-05-24-steane-all-clifford-ghost-gaussians/data/steane_all_clifford_generator_images.csv` | `scripts/lattice_codes/steane_all_clifford_ghost_gaussians.jl` | `steane_all_clifford_generator_images.csv` |
| `runs/2026-05-24-steane-all-clifford-ghost-gaussians/data/steane_ghost_gaussian_elementaries.csv` | `scripts/lattice_codes/steane_all_clifford_ghost_gaussians.jl` | `steane_ghost_gaussian_elementaries.csv` |
| `runs/2026-05-24-arithmetic-quantum-fields/data/arithmetic_quantum_field_examples.csv` | `scripts/bridges/arithmetic_quantum_fields.jl` | `arithmetic_quantum_field_examples.csv` |
| `runs/2026-05-24-arithmetic-quantum-fields/data/arithmetic_quantum_field_bases.csv` | `scripts/bridges/arithmetic_quantum_fields.jl` | `arithmetic_quantum_field_bases.csv` |
| `runs/2026-05-24-projective-line-sheaf-fields/data/projective_line_sheaf_field_summary.csv` | `scripts/bridges/projective_line_sheaf_fields.jl` | `projective_line_sheaf_field_summary.csv` |
| `runs/2026-05-24-projective-line-sheaf-fields/data/projective_line_sheaf_field_basis_rows.csv` | `scripts/bridges/projective_line_sheaf_fields.jl` | `projective_line_sheaf_field_basis_rows.csv` |
| `runs/2026-05-24-projective-line-sheaf-fields/data/projective_line_stalk_rows.csv` | `scripts/bridges/projective_line_sheaf_fields.jl` | `projective_line_stalk_rows.csv` |

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
| `AQM-12-STEANE-CLIFFORD-KOSZUL-MORPHISMS` | `report/sections/12_steane_clifford_koszul_morphisms.tex` | Steane Clifford Morphisms of the Koszul Supercharge |
| `AQM-13-CLIFFORD-GROUP-GHOST-GAUSSIAN-THEOREM` | `report/sections/13_clifford_group_ghost_gaussian_theorem.tex` | Clifford Group Ghost-Gaussian Theorem |
| `AQM-14-ARITHMETIC-QUANTUM-FIELDS` | `report/sections/14_arithmetic_quantum_fields.tex` | Arithmetic Quantum Fields |
| `AQM-15-PROJECTIVE-SHEAF-FIELD-DEFINITIONS` | `report/sections/15_projective_sheaf_fields_definitions.tex` | Projective Sheaf Field Definitions |
| `AQM-16-PROJECTIVE-LINE-SHEAF-FIELD-CALCULATION` | `report/sections/16_projective_line_sheaf_field_calculation.tex` | Projective Line Sheaf Field Calculation |
| `AQM-17-PROJECTIVE-LINE-STALKS` | `report/sections/17_projective_line_stalks.tex` | Projective Line Stalks |

## Source Topics

Source manifests should be created under `references/<topic>/SOURCES.md`.

| Topic | Manifest | Status |
|---|---|---|
| Weil conjectures and zeta functions | _pending_ | No sources acquired. |
| Arithmetic quantum mechanics | _pending_ | No sources acquired. |
| Supersymmetric quantum mechanics | _pending_ | No sources acquired. |
| Toric codes and Levin-Wen models | `references/toric_code/SOURCES.md` | Kitaev arXiv source bundle acquired for the toric-code stabilizer convention. |
| Symplectic QECC and stabilizer geometry | `references/symplectic_qecc/SOURCES.md` | Gottesman and Ashikhmin-Knill arXiv source bundles acquired for stabilizer symplectic conventions. |
| Algebraic geometry and sheaves | `references/algebraic_geometry/SOURCES.md` | Stacks Project TeX snapshot acquired for presheaves, sheaves, Proj, projective space, varieties, twists, and projective-space cohomology. |
