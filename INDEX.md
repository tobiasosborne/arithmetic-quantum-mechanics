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
| `scripts/bridges/projective_line_sheaf_fields.jl` | Julia | `runs/2026-05-24-projective-line-sheaf-fields/` | `data/projective_line_sheaf_field_summary.csv`, `data/projective_line_sheaf_field_basis_rows.csv`, `data/projective_line_stalk_rows.csv` | _none_ | `AQM-15-PROJECTIVE-SHEAF-FIELD-DEFINITIONS`, `AQM-16-PROJECTIVE-LINE-SHEAF-FIELD-CALCULATION`, `AQM-17-PROJECTIVE-LINE-STALKS`, `AQM-18-STALKS-AS-FIELD-GERMS` |

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
| `AQM-18-STALKS-AS-FIELD-GERMS` | `report/sections/18_stalks_as_field_germs.tex` | Stalks as Field Germs |
| `AQM-19-CANONICAL-BOSON-FERMION-FIELD-COMPARISON` | `report/sections/19_canonical_boson_fermion_field_comparison.tex` | Canonical Boson and Fermion Fields as Field-Label Tests |
| `AQM-20-GRASSMANN-WEYL-FERMION-DISPLACEMENTS` | `report/sections/20_grassmann_weyl_fermion_displacements.tex` | Grassmann-Weyl Fermion Displacements |
| `AQM-21-GRASSMANN-WEYL-FERMION-DERIVATIONS` | `report/sections/21_grassmann_weyl_fermion_displacement_derivations.tex` | Grassmann-Weyl Fermion Displacement Derivations |
| `AQM-22-PRIME-FIELD-ARITHMETIC-FIELDS-QUDIT-PAULIS` | `report/sections/22_prime_field_arithmetic_fields_qudit_paulis.tex` | Prime-Field Arithmetic Fields and Qudit Paulis |
| `AQM-23-SPEC-Z6-RESIDUE-QUDIT-FACTORISATION` | `report/sections/23_spec_z6_residue_qudit_factorisation.tex` | Spec Z/6Z and Residue Qudit Factorisation |
| `AQM-24-ZARISKI-OPENS-OBSERVABLE-NETS` | `report/sections/24_zariski_opens_observable_nets.tex` | Zariski Opens and Observable Nets |
| `AQM-25-QUASILOCAL-ZARISKI-ALGEBRA` | `report/sections/25_quasilocal_zariski_algebra.tex` | Quasi-Local Zariski Algebra |
| `AQM-26-PRESHEAVES-COSHEAVES-OBSERVABLE-NETS` | `report/sections/26_presheaves_cosheaves_observable_nets.tex` | Presheaves, Cosheaves, and Observable Nets |
| `AQM-27-STATE-PRESHEAF-QUASILOCAL-ALGEBRA` | `report/sections/27_state_presheaf_quasilocal_algebra.tex` | State Presheaf of the Quasi-Local Algebra |
| `AQM-28-CLOSED-POINT-AFFINE-ARITHMETIC-FIELDS` | `report/sections/28_closed_point_affine_arithmetic_fields.tex` | Closed-Point Affine Arithmetic Fields |
| `AQM-29-SPEC-FQ-T-ARITHMETIC-FIELD` | `report/sections/29_spec_fq_t_arithmetic_field.tex` | The Arithmetic Field on \(\operatorname{Spec}\mathbb F_q[t]\) |
| `AQM-30-SPEC-FQ-XY-ARITHMETIC-FIELD` | `report/sections/30_spec_fq_xy_arithmetic_field.tex` | The Arithmetic Field on \(\operatorname{Spec}\mathbb F_q[x,y]\) |
| `AQM-31-WEYL-HEISENBERG-RESEARCH-STATUS-RINGS` | `report/sections/31_weyl_heisenberg_research_status_over_rings.tex` | Weyl-Heisenberg Representation Status over Rings and LCA Systems |
| `AQM-32-WEYL-HEISENBERG-REPRESENTATIONS-FOR-KT` | `report/sections/32_weyl_heisenberg_representations_for_kt.tex` | Weyl-Heisenberg Representations for \(k(t)\) |
| `AQM-33-FULL-DUAL-LOCAL-MODELS-FOR-KT` | `report/sections/33_full_dual_local_models_for_kt.tex` | Full-Dual and Local Models for \(k(t)\) |
| `AQM-34-F3-POLYNOMIAL-QUOTIENT-ARITHMETIC-FIELDS` | `report/sections/34_f3_polynomial_quotient_arithmetic_fields.tex` | Polynomial-Quotient Arithmetic Fields over \(\mathbb F_3\) |
| `AQM-35-TN-EQUALS-1-F3-ARITHMETIC-FIELD` | `report/sections/35_tn_equals_1_f3_arithmetic_field.tex` | The \(t^n=1\) Arithmetic Field over \(\mathbb F_3\) |
| `AQM-36-NILPOTENT-THICKENING-WEYL-FIELDS` | `report/sections/36_nilpotent_thickening_weyl_fields.tex` | Nilpotent Thickening Weyl Fields |
| `AQM-37-THICKENED-TN-EQUALS-1-EXAMPLES` | `report/sections/37_thickened_tn_equals_1_examples.tex` | Thickened \(t^n=1\) Examples |
| `AQM-38-LAGRANGIAN-STABILIZER-DESCENT` | `report/sections/38_lagrangian_stabilizer_descent.tex` | Lagrangian Stabilizer Descent |
| `AQM-39-TWO-QUTRIT-STABILIZER-DESCENT-COUNTEREXAMPLE` | `report/sections/39_two_qutrit_stabilizer_descent_counterexample.tex` | Two-Qutrit Stabilizer Descent Counterexample |
| `AQM-40-PRODUCT-FIELD-SPECTRUM-QUDIT-STABILIZERS` | `report/sections/40_product_field_spectrum_qudit_stabilizers.tex` | Product-Field Spectra and \(n\)-Qudit Stabilizers |
| `AQM-41-CECH-COHOMOLOGY-QUANTUM-DESCENT` | `report/sections/41_cech_cohomology_quantum_descent.tex` | Cech Cohomology and Quantum Descent |
| `AQM-42-GAUSSIAN-CLIFFORD-DYNAMICS` | `report/sections/42_gaussian_clifford_dynamics.tex` | Gaussian and Clifford Dynamics |
| `AQM-43-FINITE-FIELD-SCALE-CONTINUUM-LIMITS` | `report/sections/43_finite_field_scale_continuum_limits.tex` | Finite-Field Scales and Continuum Limits |
| `AQM-44-TRACE-GAUGES-FULL-CONTINUUM-TOWERS` | `report/sections/44_trace_gauges_full_continuum_towers.tex` | Trace Gauges for Full Continuum Towers |
| `AQM-45-SPEC-Z-ARITHMETIC-QUANTUM-FIELD` | `report/sections/45_spec_z_arithmetic_quantum_field.tex` | The Arithmetic Quantum Field on \(\operatorname{Spec}\mathbb Z\) |
| `AQM-46-AFFINE-LINE-SYMMETRY-WEYL-NET` | `report/sections/46_affine_line_symmetry_weyl_net.tex` | Affine-Line Symmetries and Weyl-Net Automorphisms |
| `AQM-47-F3-AFFINE-LINE-SYMMETRY-EXAMPLE` | `report/sections/47_f3_affine_line_symmetry_example.tex` | The \(\mathbb F_3\) Rational-Support Affine-Line Symmetry Example |
| `AQM-48-F3-FULL-AFFINE-LINE-NET-HILBERT-ACTION` | `report/sections/48_f3_full_affine_line_net_hilbert_action.tex` | The Full \(\mathbb F_3\) Affine-Line Net and Hilbert Action |

## Source Topics

Source manifests should be created under `references/<topic>/SOURCES.md`.

| Topic | Manifest | Status |
|---|---|---|
| Weil conjectures and zeta functions | _pending_ | No sources acquired. |
| Arithmetic quantum mechanics | _pending_ | No sources acquired. |
| Supersymmetric quantum mechanics | _pending_ | No sources acquired. |
| Canonical bosonic and fermionic fields | `references/canonical_fields/SOURCES.md` | Derezinski, Bekka, Bravyi, Keyl-Schlingemann, and Cahill-Glauber sources acquired for CCR, CAR, Fock, Stone-von-Neumann, FLO, GAR, and Grassmann fermion displacement conventions. |
| Toric codes and Levin-Wen models | `references/toric_code/SOURCES.md` | Kitaev arXiv source bundle acquired for the toric-code stabilizer convention. |
| Symplectic QECC and stabilizer geometry | `references/symplectic_qecc/SOURCES.md` | Gottesman, Ashikhmin-Knill, and Gross arXiv source bundles acquired for stabilizer symplectic conventions, qudit error bases, finite Hudson/Gaussian states, and prime-field Pauli comparisons. |
| Weyl-Heisenberg and Weil representations | `references/heisenberg_weil/SOURCES.md` | Prasad, Beny-Crann-Lee-Park-Youn, Bekka, Solomon, Lysenko, Sidana-Kashyap, Gluesing-Luerssen-Pllaha, Trias, Hashimoto-Horibe-Hayashi, Korbelar-Tolar, Galindo, Poonen, and Kudla sources acquired for LCA, ring, finite Frobenius-ring, finite Clifford, local, and adelic Weyl-Heisenberg representation conventions. |
| Algebraic geometry and sheaves | `references/algebraic_geometry/SOURCES.md` | Stacks Project TeX snapshot acquired for spectra, Zariski topology, affine-scheme functoriality, presheaves, sheaves, Proj, projective space, varieties, twists, Cech cohomology, projective-space cohomology, separable trace pairing, and Frobenius. |
| Cosheaves | `references/cosheaves/SOURCES.md` | Curry arXiv source bundle acquired for precosheaf, cosheaf, colimit, and cover-coequalizer conventions. |
