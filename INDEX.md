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
| `runs/2026-05-24-steane-clifford-koszul-morphisms/` | Steane code / Clifford morphisms | Summary/check record for transversal Hadamard and phase Clifford/Koszul morphism hypotheses and consequences. |
| `runs/2026-05-24-steane-all-clifford-ghost-gaussians/` | Steane code / Clifford group ghost Gaussians | Exact generator-level validation of arbitrary Clifford covariance and elementary GL6 ghost-Gaussian presentation moves. |
| `runs/2026-05-24-arithmetic-quantum-fields/` | Arithmetic quantum fields / finite function spaces | Exact `F_3` validation of pointwise symplectic function spaces, radicals, reduced Weyl labels, and observable algebra dimensions. |
| `runs/2026-05-24-projective-line-sheaf-fields/` | Projective arithmetic fields / sheaves | Exact `F_3` validation of \(\mathbf P^1\), \(H^0(\mathcal O(d))\otimes\mathbb F_3^2\), finite point evaluations, stalk germs, radicals, and reduced Weyl labels. |
| `runs/2026-05-26-finite-ring-database/` | Finite commutative ring database | Schema-only SQLite smoke build, audit gate on the schema-only smoke artifact, and in-memory MVP CSV review exports; `finite_rings.sqlite` remains schema-only/local and no populated/audited database is claimed. |

## Quick Start

```bash
make check-report-shards
make report
julia --project=. -e 'using Pkg; Pkg.test()'
julia --project=. scripts/run_all.jl --fast
```

## Script To Output Manifest

One row per script that writes files or gates a run bundle. Add rows in the
same change that adds a producer or gate.

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
| `scripts/arithmetic/finite_ring_db_build.jl` | Julia | `runs/2026-05-26-finite-ring-database/` | _none_ (writes local `data/finite_rings.sqlite`) | _none_ | _pending_ |
| `scripts/arithmetic/finite_ring_db_audit.jl` | Julia | `runs/2026-05-26-finite-ring-database/` | _none_ (audits local `data/finite_rings.sqlite`; writes no artifact in this MVP slice) | _none_ | _pending_ |
| `scripts/arithmetic/finite_ring_db_exports.jl` | Julia | `runs/2026-05-26-finite-ring-database/` | `data/ring_summary.csv`, `data/ring_presentations.csv`, `data/ring_isomorphism_certificates.csv`, `data/ring_quantization_summary.csv`, `data/ring_quantization_obstruction.csv` | _none_ | _pending_ |

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
| `runs/2026-05-26-finite-ring-database/data/ring_summary.csv` | `scripts/arithmetic/finite_ring_db_exports.jl` | `ring_summary.csv` |
| `runs/2026-05-26-finite-ring-database/data/ring_presentations.csv` | `scripts/arithmetic/finite_ring_db_exports.jl` | `ring_presentations.csv` |
| `runs/2026-05-26-finite-ring-database/data/ring_isomorphism_certificates.csv` | `scripts/arithmetic/finite_ring_db_exports.jl` | `ring_isomorphism_certificates.csv` |
| `runs/2026-05-26-finite-ring-database/data/ring_quantization_summary.csv` | `scripts/arithmetic/finite_ring_db_exports.jl` | `ring_quantization_summary.csv` |
| `runs/2026-05-26-finite-ring-database/data/ring_quantization_obstruction.csv` | `scripts/arithmetic/finite_ring_db_exports.jl` | `ring_quantization_obstruction.csv` |

## Planning Documents

| Document | Topic | Status |
|---|---|---|
| `docs/finite_commutative_ring_database_prd.md` | Finite commutative ring database and quantisation pipeline | PRD plus schema-only smoke build, audit gate, and in-memory MVP review exports exist; populated/audited ring database remains pending. |
| `docs/finite_commutative_ring_database_implementation_plan.md` | Red-green implementation chain for the finite commutative ring database | Beads chain `aqm-pa0` through `aqm-6t4`; schema-only smoke build, schema-only/MVP malformed audit gate, and in-memory MVP review exports exist, while populated/audited ring database remains pending. |
| `docs/finite_commutative_ring_database_population_plan.md` | Population and bounded-catalogue plan for the finite commutative ring database | Second-pass bead chain from schema-only SQLite to populated MVP, then a first-100-or-more deduplicated audited catalogue tranche. |
| `docs/quantum_system_associations/PLAN.md` | Quantum-system association meta-plan | User-directed plan and Beads chain `aqm-qsa01` through `aqm-qsa23` for review and new shards comparing finite-set, geometric, finite-ring, residue-field, cotangent, field, nilpotent-sensitive, infinite-boundary, and open-problem association workflows. |

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
| `AQM-49-REGULAR-FUNCTIONS-AFFINE-LINE-WEYL-LABELS` | `report/sections/49_regular_functions_affine_line_weyl_labels.tex` | Regular Functions, Supports, and Weyl Labels on the Affine Line |
| `AQM-50-F3-REGULAR-FUNCTIONS-LINE-BY-LINE` | `report/sections/50_f3_regular_functions_line_by_line.tex` | Regular Functions on \(\mathbb F_3[x]\) Line by Line |
| `AQM-51-REGULAR-FUNCTION-AFFINE-SYMMETRY-ACTION` | `report/sections/51_regular_function_affine_symmetry_action.tex` | Affine Symmetry Action on Regular Functions |
| `AQM-52-F3-REGULAR-FUNCTION-SYMMETRY-LINE-BY-LINE` | `report/sections/52_f3_regular_function_symmetry_line_by_line.tex` | The \(\mathbb F_3\) Regular-Function Symmetry Action Line by Line |
| `AQM-53-MINIMAL-FERMION-GEOMETRY-CATALOGUE` | `report/sections/53_minimal_fermion_geometry_catalogue.tex` | Minimal Fermion Geometry Catalogue |
| `AQM-54-DERIVATIVE-DYNAMICS-F3-EXAMPLES` | `report/sections/54_derivative_dynamics_f3_examples.tex` | Derivative Dynamics from Kähler Differentials over \(\mathbb F_3\) |
| `AQM-55-DERHAM-CSS-MORE-F3-EXAMPLES` | `report/sections/55_derham_css_more_f3_examples.tex` | More \(\mathbb F_3\) Examples for the de Rham CSS Prototype |
| `AQM-56-DERHAM-CSS-F2-QUBIT-EXAMPLES` | `report/sections/56_derham_css_f2_qubit_examples.tex` | \(\mathbb F_2\) Qubit Examples for the de Rham CSS Prototype |
| `AQM-57-DERHAM-CSS-F2-ENTANGLEMENT-CODES` | `report/sections/57_derham_css_f2_entanglement_codes.tex` | Entanglement Inside the \(\mathbb F_2\) de Rham CSS Prototype |
| `AQM-58-PRODUCT-RINGS-REAL-LINE-COTANGENT` | `report/sections/58_product_rings_real_line_cotangent.tex` | Product Rings and the Formal Real Affine Line |
| `AQM-59-FINITE-FIELD-CIRCLE-TANGENT-WEYL-LABELS` | `report/sections/59_finite_field_circle_quantum_space.tex` | The Finite-Field Circle: Tangent-Weyl Labels |
| `AQM-60-TANGENT-WEYL-OPERATOR-PRINCIPLE` | `report/sections/60_tangent_weyl_operator_principle.tex` | Tangent-Weyl Operator Principle and de Rham CSS Prototype |
| `AQM-61-TANGENT-COTANGENT-WEYL-KINEMATICS-EXAMPLES` | `report/sections/61_tangent_cotangent_weyl_kinematics_examples.tex` | Tangent-Cotangent Weyl Kinematics: Recipe and First Examples |
| `AQM-62-TANGENT-COTANGENT-WEYL-KINEMATICS-MORE-EXAMPLES` | `report/sections/62_tangent_cotangent_weyl_kinematics_more_examples.tex` | More Tangent-Cotangent Weyl Kinematical Examples |
| `AQM-63-EVALUATED-DERHAM-CONSTRAINTS-TANGENT-WEYL` | `report/sections/63_evaluated_derham_constraints_tangent_weyl.tex` | Evaluated de Rham Constraints on Tangent-Weyl Kinematics |
| `AQM-64-QUANTUM-SYSTEM-ASSOCIATION-META-PLAN` | `report/sections/64_quantum_system_association_meta_plan.tex` | Quantum-System Association Meta-Plan |
| `AQM-65-QSA-VOCABULARY` | `report/sections/65_quantum_system_association_vocabulary.tex` | Quantum-System Association Vocabulary |
| `AQM-66-QSA-TEST-OBJECT-CATALOGUE` | `report/sections/66_quantum_system_association_test_object_catalogue.tex` | Quantum-System Association Test Object Catalogue |
| `AQM-67-QSA-FINITE-SET-FIRST-ASSOCIATION` | `report/sections/67_quantum_system_association_finite_set_first.tex` | Structureless Finite-Set First Association |
| `AQM-68-QSA-FINITE-SET-TENSOR-SITES` | `report/sections/68_quantum_system_association_finite_set_tensor_sites.tex` | Structureless Finite-Set Tensor-Site Association |
| `AQM-69-QSA-FINITE-SET-DIRECT-SUM-PARTICLE` | `report/sections/69_quantum_system_association_finite_set_direct_sum_particle.tex` | Structureless Finite-Set Direct-Sum Particle Association |
| `AQM-70-QSA-AND-OR-MANY-PARTICLE-GRAMMAR` | `report/sections/70_quantum_system_association_and_or_many_particle_grammar.tex` | AND/OR Many-Particle Grammar |
| `AQM-71-QSA-SYMPLECTIC-FIELD-LABELS-SET` | `report/sections/71_quantum_system_association_symplectic_field_labels_set.tex` | Finite Symplectic Field Labels on a Set |
| `AQM-72-QSA-BOSON-FERMION-LAYER` | `report/sections/72_quantum_system_association_boson_fermion_layer.tex` | Bosonic and Fermionic Association Layer |
| `AQM-73-QSA-FUSION-CATEGORY-ENDPOINT` | `report/sections/73_quantum_system_association_fusion_category_endpoint.tex` | Fusion-Category Endpoint |
| `AQM-74-QSA-SINGLE-PARTICLE-REDUCTION` | `report/sections/74_quantum_system_association_single_particle_reduction.tex` | Single-Particle Reduction |
| `AQM-75-QSA-WHAT-COUNTS-AS-A-POINT` | `report/sections/75_quantum_system_association_what_counts_as_point.tex` | What Counts As A Point |
| `AQM-76-QSA-COTANGENT-FIRST-ASSOCIATION` | `report/sections/76_quantum_system_association_cotangent_first.tex` | Cotangent-Based First Association |
| `AQM-77-QSA-INTRINSIC-RELATIVE-COTANGENT` | `report/sections/77_quantum_system_association_intrinsic_relative_cotangent.tex` | Intrinsic Versus Relative Cotangent Data |
| `AQM-78-QSA-FINITE-PHASE-WEYL-KINEMATICS` | `report/sections/78_quantum_system_association_finite_phase_weyl_kinematics.tex` | Weyl-Heisenberg Kinematics From Finite Phase Spaces |
| `AQM-79-QSA-GEOMETRIC-FIELD-HOM-X-V` | `report/sections/79_quantum_system_association_geometric_field_hom_x_v.tex` | Geometric Field Association Hom(X,V) |
| `AQM-80-QSA-FINITE-RING-EXAMPLE-MATRIX` | `report/sections/80_quantum_system_association_finite_ring_example_matrix.tex` | Finite Ring Example Matrix |
| `AQM-81-QSA-RESIDUE-FIELD-SITE-ASSOCIATION` | `report/sections/81_quantum_system_association_residue_field_site_association.tex` | Residue-Field Site Association for \(\Spec R\) |
| `AQM-82-QSA-NILPOTENT-SENSITIVE-ASSOCIATION` | `report/sections/82_quantum_system_association_nilpotent_sensitive_association.tex` | Nilpotent-Sensitive Association |
| `AQM-83-QSA-PRODUCT-RINGS-TENSOR-FACTORS` | `report/sections/83_quantum_system_association_product_rings_tensor_factors.tex` | Product Rings and Tensor Factors |
| `AQM-84-QSA-INFINITE-RING-BOUNDARIES` | `report/sections/84_quantum_system_association_infinite_ring_boundaries.tex` | Infinite Ring Boundary Cases |
| `AQM-85-QSA-AGREEMENT-INEQUIVALENCE-TABLE` | `report/sections/85_quantum_system_association_agreement_inequivalence_table.tex` | Agreement and Inequivalence Table |
| `AQM-86-QSA-DEGENERATE-OVERRESTRICTIVE-CASES` | `report/sections/86_quantum_system_association_degenerate_overrestrictive_cases.tex` | Degenerate and Over-Restrictive Cases |
| `AQM-87-QSA-OPEN-PROBLEMS-NEXT-TARGETS` | `report/sections/87_quantum_system_association_open_problems_next_targets.tex` | Open Problems and Next Catalogue Targets |
| `AQM-88-DERIVATIVE-CONSTRAINTS-RESIDUE-WEYL` | `report/sections/88_derivative_constraints_residue_weyl.tex` | Derivative Constraints on Residue Weyl-Heisenberg Fields |
| `AQM-89-SCHEME-INCIDENCE-CODE-SOURCES` | `report/sections/89_scheme_incidence_code_sources.tex` | Scheme-Incidence Sources for Code Complexes |
| `AQM-90-ALGEBRAIC-TORUS-QUANT2` | `report/sections/90_algebraic_torus_quant2.tex` | Algebraic Torus Quant2 Test Case |
| `AQM-91-HAAH-LAURENT-TORUS-QUANT2` | `report/sections/91_haah_laurent_torus_quant2.tex` | Haah Laurent Modules and Torus Quant2 |
| `AQM-92-HAAH-DATA-SCHEME-MODULES` | `report/sections/92_haah_data_scheme_modules.tex` | Haah Data over Schemes: Permissive Module Grammar |
| `AQM-93-FINITE-RING-HAAH-LAYERS` | `report/sections/93_finite_ring_haah_layers.tex` | Finite-Ring Haah Layers: Residues, Thickenings, and Blockers |
| `AQM-94-TRANSLATION-ALGEBRA-SPEC` | `report/sections/94_translation_algebra_vs_spec.tex` | Translation Haah Data versus Bare Spectrum |

## Source Topics

Source manifests should be created under `references/<topic>/SOURCES.md`.

| Topic | Manifest | Status |
|---|---|---|
| Weil conjectures and zeta functions | _pending_ | No sources acquired. |
| Arithmetic quantum mechanics | _pending_ | No sources acquired. |
| Supersymmetric quantum mechanics | _pending_ | No sources acquired. |
| Canonical bosonic and fermionic fields | `references/canonical_fields/SOURCES.md` | Derezinski, Bekka, Bravyi, Keyl-Schlingemann, and Cahill-Glauber sources acquired for CCR, CAR, Fock, Stone-von-Neumann, FLO, GAR, and Grassmann fermion displacement conventions. |
| Supergeometry | `references/supergeometry/SOURCES.md` | Witten source bundle acquired for supermanifold coordinates, reduced spaces, parity reversal, and Clifford quantization of odd variables. |
| Spin geometry | `references/spin_geometry/SOURCES.md` | Atiyah PDF and text extraction acquired for Riemann-surface spin structures as square roots of canonical line bundles and spinor-parity statements. |
| Log geometry | `references/log_geometry/SOURCES.md` | Stacks tag 0FMU HTML snapshot acquired for logarithmic differentials, \(d\log\), residues, and the log-pole exact sequence. |
| Toric codes and Levin-Wen models | `references/toric_code/SOURCES.md` | Kitaev, Error Correction Zoo, and Bombin--Martin-Delgado sources acquired for toric-code stabilizers, logical loops/CSS-code data, homological chain-complex conventions, Shor-family locators, and original toric-code family locators. |
| Lattice stabilizer codes and Laurent-polynomial methods | `references/lattice_stabilizer_codes/SOURCES.md` | Haah source bundles acquired for cubic codes, translation-group algebra/free-module Pauli Hamiltonians, lattice-code lecture notes, the 2D prime-qudit toric-code classification theorem, and adjacent Haah--Vijay--Fu fracton polynomial methods. |
| Symplectic QECC and stabilizer geometry | `references/symplectic_qecc/SOURCES.md` | Gottesman, Ashikhmin-Knill, and Gross arXiv source bundles acquired for stabilizer symplectic conventions, qudit error bases, finite Hudson/Gaussian states, and prime-field Pauli comparisons. |
| Weyl-Heisenberg and Weil representations | `references/heisenberg_weil/SOURCES.md` | Prasad, Beny-Crann-Lee-Park-Youn, Bekka, Solomon, Lysenko, Sidana-Kashyap, Gluesing-Luerssen-Pllaha, Trias, Hashimoto-Horibe-Hayashi, Korbelar-Tolar, Galindo, Poonen, and Kudla sources acquired for LCA/ring Weyl-Heisenberg conventions, cocycle normalization, finite symplectic abelian-group and finite Heisenberg anchors, trace/generating-character and Frobenius-ring Pauli conventions, finite Clifford splitting, coefficient-ring Weil anchors, and local/adelic background. |
| Finite commutative ring database | `references/finite_ring_database/SOURCES.md` | Nowicki, Behboodi-Beyranvand-Hashemi-Khabazian, Blackburn-McLean, Alabiad-Alkhamees, GAP, Sage, OSCAR, Nemo, FLINT, and SQLite sources acquired for finite-ring catalogue planning, tooling, and storage choices. |
| Algebraic geometry and sheaves | `references/algebraic_geometry/SOURCES.md` | Stacks Project TeX snapshot acquired for spectra, Zariski topology, product and finite-discrete spectra, Artinian finite-dimensional/zero-dimensional ring anchors, affine-scheme functoriality, presheaves, sheaves, Proj, projective space, varieties, twists, Cech cohomology, projective-space cohomology, separable trace pairing, and Frobenius. |
| Cosheaves | `references/cosheaves/SOURCES.md` | Curry arXiv source bundle acquired for precosheaf, cosheaf, colimit, and cover-coequalizer conventions. |
