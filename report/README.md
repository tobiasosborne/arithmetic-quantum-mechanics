# Report Source Map

Read this file first when navigating the lab-book source. The compiled report
is rooted at `report.tex`, but that file should remain the preamble and include
order only. Body prose lives in `report/sections/*.tex`.

For rapid lookup, use `report/SHARD_CATALOG.md`. It assigns each shard a stable
label, gives 2-3 summary lines, and lists search keywords. The same metadata
appears in a TeX comment header at the top of every shard.

The target shard size is about 200 lines. The local guard allows larger
topic-preserving shards up to `REPORT_SHARD_MAX_LINES` (default 280 lines).
Run `make check-report-shards` after editing report structure and `make report`
before treating report edits as complete.

## Shard Order

| Order | Label | Source | Title |
|---:|---|---|---|
| 0 | `AQM-00-FRONTMATTER` | `report/sections/00_frontmatter_status.tex` | Frontmatter, Status, and Scope |
| 1 | `AQM-01-PROGRAMME-MAP` | `report/sections/01_programme_map.tex` | Programme Map |
| 2 | `AQM-02-LAB-LOG` | `report/sections/02_lab_log.tex` | Lab Log |
| 3 | `AQM-03-REPRO-MAP` | `report/sections/03_reproducibility_map.tex` | Reproducibility Map |
| 4 | `AQM-04-SOURCES-QUESTIONS` | `report/sections/04_source_queue_open_questions.tex` | Source Queue and Open Questions |
| 5 | `AQM-05-TORIC-SUPERCHARGE` | `report/sections/05_toric_supercharge_checks.tex` | Toric Code Supercharge From Local Checks |
| 6 | `AQM-06-TORIC-CHAIN-GHOST-PROOF` | `report/sections/06_toric_chain_ghost_proof.tex` | Proof of the Toric Chain-to-Ghost Lift |
| 7 | `AQM-07-TORIC-OPERATOR-RELATION` | `report/sections/07_toric_operator_relation.tex` | Operator Relation Between Cellular and Ghost Supercharges |
| 8 | `AQM-08-SYMPLECTIC-CSS-BRIDGE` | `report/sections/08_symplectic_css_bridge.tex` | Chain Complexes as Symplectic CSS Stabilizers |
| 9 | `AQM-09-SYMPLECTIC-SUPERCHARGE-DICTIONARY` | `report/sections/09_symplectic_supercharge_dictionary.tex` | Symplectic Dictionary for CSS Supercharges |
| 10 | `AQM-10-STEANE-SYMPLECTIC-MOLECULAR` | `report/sections/10_steane_symplectic_molecular.tex` | Steane Code Symplectic Data in Molecular Detail |
| 11 | `AQM-11-STEANE-SUPERCHARGE-COHOMOLOGY` | `report/sections/11_steane_supercharge_cohomology.tex` | Steane Code Fermions, Supercharge, and Cohomology |
| 12 | `AQM-12-STEANE-CLIFFORD-KOSZUL-MORPHISMS` | `report/sections/12_steane_clifford_koszul_morphisms.tex` | Steane Clifford Morphisms of the Koszul Supercharge |
| 13 | `AQM-13-CLIFFORD-GROUP-GHOST-GAUSSIAN-THEOREM` | `report/sections/13_clifford_group_ghost_gaussian_theorem.tex` | Clifford Group Ghost-Gaussian Theorem |
| 14 | `AQM-14-ARITHMETIC-QUANTUM-FIELDS` | `report/sections/14_arithmetic_quantum_fields.tex` | Arithmetic Quantum Fields |
| 15 | `AQM-15-PROJECTIVE-SHEAF-FIELD-DEFINITIONS` | `report/sections/15_projective_sheaf_fields_definitions.tex` | Projective Sheaf Field Definitions |
| 16 | `AQM-16-PROJECTIVE-LINE-SHEAF-FIELD-CALCULATION` | `report/sections/16_projective_line_sheaf_field_calculation.tex` | Projective Line Sheaf Field Calculation |
| 17 | `AQM-17-PROJECTIVE-LINE-STALKS` | `report/sections/17_projective_line_stalks.tex` | Projective Line Stalks |
| 18 | `AQM-18-STALKS-AS-FIELD-GERMS` | `report/sections/18_stalks_as_field_germs.tex` | Stalks as Field Germs |
| 19 | `AQM-19-CANONICAL-BOSON-FERMION-FIELD-COMPARISON` | `report/sections/19_canonical_boson_fermion_field_comparison.tex` | Canonical Boson and Fermion Fields as Field-Label Tests |
| 20 | `AQM-20-GRASSMANN-WEYL-FERMION-DISPLACEMENTS` | `report/sections/20_grassmann_weyl_fermion_displacements.tex` | Grassmann-Weyl Fermion Displacements |
| 21 | `AQM-21-GRASSMANN-WEYL-FERMION-DERIVATIONS` | `report/sections/21_grassmann_weyl_fermion_displacement_derivations.tex` | Grassmann-Weyl Fermion Displacement Derivations |
| 22 | `AQM-22-PRIME-FIELD-ARITHMETIC-FIELDS-QUDIT-PAULIS` | `report/sections/22_prime_field_arithmetic_fields_qudit_paulis.tex` | Prime-Field Arithmetic Fields and Qudit Paulis |
| 23 | `AQM-23-SPEC-Z6-RESIDUE-QUDIT-FACTORISATION` | `report/sections/23_spec_z6_residue_qudit_factorisation.tex` | Spec Z/6Z and Residue Qudit Factorisation |
| 24 | `AQM-24-ZARISKI-OPENS-OBSERVABLE-NETS` | `report/sections/24_zariski_opens_observable_nets.tex` | Zariski Opens and Observable Nets |
| 25 | `AQM-25-QUASILOCAL-ZARISKI-ALGEBRA` | `report/sections/25_quasilocal_zariski_algebra.tex` | Quasi-Local Zariski Algebra |
| 26 | `AQM-26-PRESHEAVES-COSHEAVES-OBSERVABLE-NETS` | `report/sections/26_presheaves_cosheaves_observable_nets.tex` | Presheaves, Cosheaves, and Observable Nets |
| 27 | `AQM-27-STATE-PRESHEAF-QUASILOCAL-ALGEBRA` | `report/sections/27_state_presheaf_quasilocal_algebra.tex` | State Presheaf of the Quasi-Local Algebra |
| 28 | `AQM-28-CLOSED-POINT-AFFINE-ARITHMETIC-FIELDS` | `report/sections/28_closed_point_affine_arithmetic_fields.tex` | Closed-Point Affine Arithmetic Fields |
| 29 | `AQM-29-SPEC-FQ-T-ARITHMETIC-FIELD` | `report/sections/29_spec_fq_t_arithmetic_field.tex` | The Arithmetic Field on \(\operatorname{Spec}\mathbb F_q[t]\) |
| 30 | `AQM-30-SPEC-FQ-XY-ARITHMETIC-FIELD` | `report/sections/30_spec_fq_xy_arithmetic_field.tex` | The Arithmetic Field on \(\operatorname{Spec}\mathbb F_q[x,y]\) |
| 31 | `AQM-31-WEYL-HEISENBERG-RESEARCH-STATUS-RINGS` | `report/sections/31_weyl_heisenberg_research_status_over_rings.tex` | Weyl-Heisenberg Representation Status over Rings and LCA Systems |
| 32 | `AQM-32-WEYL-HEISENBERG-REPRESENTATIONS-FOR-KT` | `report/sections/32_weyl_heisenberg_representations_for_kt.tex` | Weyl-Heisenberg Representations for \(k(t)\) |
| 33 | `AQM-33-FULL-DUAL-LOCAL-MODELS-FOR-KT` | `report/sections/33_full_dual_local_models_for_kt.tex` | Full-Dual and Local Models for \(k(t)\) |
| 34 | `AQM-34-F3-POLYNOMIAL-QUOTIENT-ARITHMETIC-FIELDS` | `report/sections/34_f3_polynomial_quotient_arithmetic_fields.tex` | Polynomial-Quotient Arithmetic Fields over \(\mathbb F_3\) |
| 35 | `AQM-35-TN-EQUALS-1-F3-ARITHMETIC-FIELD` | `report/sections/35_tn_equals_1_f3_arithmetic_field.tex` | The \(t^n=1\) Arithmetic Field over \(\mathbb F_3\) |
| 36 | `AQM-36-NILPOTENT-THICKENING-WEYL-FIELDS` | `report/sections/36_nilpotent_thickening_weyl_fields.tex` | Nilpotent Thickening Weyl Fields |
| 37 | `AQM-37-THICKENED-TN-EQUALS-1-EXAMPLES` | `report/sections/37_thickened_tn_equals_1_examples.tex` | Thickened \(t^n=1\) Examples |
| 38 | `AQM-38-LAGRANGIAN-STABILIZER-DESCENT` | `report/sections/38_lagrangian_stabilizer_descent.tex` | Lagrangian Stabilizer Descent |
| 39 | `AQM-39-TWO-QUTRIT-STABILIZER-DESCENT-COUNTEREXAMPLE` | `report/sections/39_two_qutrit_stabilizer_descent_counterexample.tex` | Two-Qutrit Stabilizer Descent Counterexample |
| 40 | `AQM-40-PRODUCT-FIELD-SPECTRUM-QUDIT-STABILIZERS` | `report/sections/40_product_field_spectrum_qudit_stabilizers.tex` | Product-Field Spectra and \(n\)-Qudit Stabilizers |
| 41 | `AQM-41-CECH-COHOMOLOGY-QUANTUM-DESCENT` | `report/sections/41_cech_cohomology_quantum_descent.tex` | Cech Cohomology and Quantum Descent |
| 42 | `AQM-42-GAUSSIAN-CLIFFORD-DYNAMICS` | `report/sections/42_gaussian_clifford_dynamics.tex` | Gaussian and Clifford Dynamics |
| 43 | `AQM-43-FINITE-FIELD-SCALE-CONTINUUM-LIMITS` | `report/sections/43_finite_field_scale_continuum_limits.tex` | Finite-Field Scales and Continuum Limits |
| 44 | `AQM-44-TRACE-GAUGES-FULL-CONTINUUM-TOWERS` | `report/sections/44_trace_gauges_full_continuum_towers.tex` | Trace Gauges for Full Continuum Towers |
| 45 | `AQM-45-SPEC-Z-ARITHMETIC-QUANTUM-FIELD` | `report/sections/45_spec_z_arithmetic_quantum_field.tex` | The Arithmetic Quantum Field on \(\operatorname{Spec}\mathbb Z\) |
| 46 | `AQM-46-AFFINE-LINE-SYMMETRY-WEYL-NET` | `report/sections/46_affine_line_symmetry_weyl_net.tex` | Affine-Line Symmetries and Weyl-Net Automorphisms |
| 47 | `AQM-47-F3-AFFINE-LINE-SYMMETRY-EXAMPLE` | `report/sections/47_f3_affine_line_symmetry_example.tex` | The \(\mathbb F_3\) Rational-Support Affine-Line Symmetry Example |
| 48 | `AQM-48-F3-FULL-AFFINE-LINE-NET-HILBERT-ACTION` | `report/sections/48_f3_full_affine_line_net_hilbert_action.tex` | The Full \(\mathbb F_3\) Affine-Line Net and Hilbert Action |
| 49 | `AQM-49-REGULAR-FUNCTIONS-AFFINE-LINE-WEYL-LABELS` | `report/sections/49_regular_functions_affine_line_weyl_labels.tex` | Regular Functions, Supports, and Weyl Labels on the Affine Line |
| 50 | `AQM-50-F3-REGULAR-FUNCTIONS-LINE-BY-LINE` | `report/sections/50_f3_regular_functions_line_by_line.tex` | Regular Functions on \(\mathbb F_3[x]\) Line by Line |
| 51 | `AQM-51-REGULAR-FUNCTION-AFFINE-SYMMETRY-ACTION` | `report/sections/51_regular_function_affine_symmetry_action.tex` | Affine Symmetry Action on Regular Functions |
| 52 | `AQM-52-F3-REGULAR-FUNCTION-SYMMETRY-LINE-BY-LINE` | `report/sections/52_f3_regular_function_symmetry_line_by_line.tex` | The \(\mathbb F_3\) Regular-Function Symmetry Action Line by Line |
| 53 | `AQM-53-MINIMAL-FERMION-GEOMETRY-CATALOGUE` | `report/sections/53_minimal_fermion_geometry_catalogue.tex` | Minimal Fermion Geometry Catalogue |
| 54 | `AQM-54-DERIVATIVE-DYNAMICS-F3-EXAMPLES` | `report/sections/54_derivative_dynamics_f3_examples.tex` | Derivative Dynamics from Kähler Differentials over \(\mathbb F_3\) |
| 55 | `AQM-55-DERHAM-CSS-MORE-F3-EXAMPLES` | `report/sections/55_derham_css_more_f3_examples.tex` | More \(\mathbb F_3\) Examples for the de Rham CSS Prototype |
| 56 | `AQM-56-DERHAM-CSS-F2-QUBIT-EXAMPLES` | `report/sections/56_derham_css_f2_qubit_examples.tex` | \(\mathbb F_2\) Qubit Examples for the de Rham CSS Prototype |
| 57 | `AQM-57-DERHAM-CSS-F2-ENTANGLEMENT-CODES` | `report/sections/57_derham_css_f2_entanglement_codes.tex` | Entanglement Inside the \(\mathbb F_2\) de Rham CSS Prototype |
| 58 | `AQM-58-PRODUCT-RINGS-REAL-LINE-COTANGENT` | `report/sections/58_product_rings_real_line_cotangent.tex` | Product Rings and the Formal Real Affine Line |
| 59 | `AQM-59-FINITE-FIELD-CIRCLE-TANGENT-WEYL-LABELS` | `report/sections/59_finite_field_circle_quantum_space.tex` | The Finite-Field Circle: Tangent-Weyl Labels |
| 60 | `AQM-60-TANGENT-WEYL-OPERATOR-PRINCIPLE` | `report/sections/60_tangent_weyl_operator_principle.tex` | Tangent-Weyl Operator Principle and de Rham CSS Prototype |
| 61 | `AQM-61-TANGENT-COTANGENT-WEYL-KINEMATICS-EXAMPLES` | `report/sections/61_tangent_cotangent_weyl_kinematics_examples.tex` | Tangent-Cotangent Weyl Kinematics: Recipe and First Examples |
| 62 | `AQM-62-TANGENT-COTANGENT-WEYL-KINEMATICS-MORE-EXAMPLES` | `report/sections/62_tangent_cotangent_weyl_kinematics_more_examples.tex` | More Tangent-Cotangent Weyl Kinematical Examples |
| 63 | `AQM-63-EVALUATED-DERHAM-CONSTRAINTS-TANGENT-WEYL` | `report/sections/63_evaluated_derham_constraints_tangent_weyl.tex` | Evaluated de Rham Constraints on Tangent-Weyl Kinematics |
| 64 | `AQM-64-QUANTUM-SYSTEM-ASSOCIATION-META-PLAN` | `report/sections/64_quantum_system_association_meta_plan.tex` | Quantum-System Association Meta-Plan |
| 65 | `AQM-65-QSA-VOCABULARY` | `report/sections/65_quantum_system_association_vocabulary.tex` | Quantum-System Association Vocabulary |
| 66 | `AQM-66-QSA-TEST-OBJECT-CATALOGUE` | `report/sections/66_quantum_system_association_test_object_catalogue.tex` | Quantum-System Association Test Object Catalogue |
| 67 | `AQM-67-QSA-FINITE-SET-FIRST-ASSOCIATION` | `report/sections/67_quantum_system_association_finite_set_first.tex` | Structureless Finite-Set First Association |
| 68 | `AQM-68-QSA-FINITE-SET-TENSOR-SITES` | `report/sections/68_quantum_system_association_finite_set_tensor_sites.tex` | Structureless Finite-Set Tensor-Site Association |
| 69 | `AQM-69-QSA-FINITE-SET-DIRECT-SUM-PARTICLE` | `report/sections/69_quantum_system_association_finite_set_direct_sum_particle.tex` | Structureless Finite-Set Direct-Sum Particle Association |
| 70 | `AQM-70-QSA-AND-OR-MANY-PARTICLE-GRAMMAR` | `report/sections/70_quantum_system_association_and_or_many_particle_grammar.tex` | AND/OR Many-Particle Grammar |
| 71 | `AQM-71-QSA-SYMPLECTIC-FIELD-LABELS-SET` | `report/sections/71_quantum_system_association_symplectic_field_labels_set.tex` | Finite Symplectic Field Labels on a Set |
| 72 | `AQM-72-QSA-BOSON-FERMION-LAYER` | `report/sections/72_quantum_system_association_boson_fermion_layer.tex` | Bosonic and Fermionic Association Layer |
| 73 | `AQM-73-QSA-FUSION-CATEGORY-ENDPOINT` | `report/sections/73_quantum_system_association_fusion_category_endpoint.tex` | Fusion-Category Endpoint |
| 74 | `AQM-74-QSA-SINGLE-PARTICLE-REDUCTION` | `report/sections/74_quantum_system_association_single_particle_reduction.tex` | Single-Particle Reduction |
| 75 | `AQM-75-QSA-WHAT-COUNTS-AS-A-POINT` | `report/sections/75_quantum_system_association_what_counts_as_point.tex` | What Counts As A Point |
| 76 | `AQM-76-QSA-COTANGENT-FIRST-ASSOCIATION` | `report/sections/76_quantum_system_association_cotangent_first.tex` | Cotangent-Based First Association |
| 77 | `AQM-77-QSA-INTRINSIC-RELATIVE-COTANGENT` | `report/sections/77_quantum_system_association_intrinsic_relative_cotangent.tex` | Intrinsic Versus Relative Cotangent Data |
| 78 | `AQM-78-QSA-FINITE-PHASE-WEYL-KINEMATICS` | `report/sections/78_quantum_system_association_finite_phase_weyl_kinematics.tex` | Weyl-Heisenberg Kinematics From Finite Phase Spaces |
| 79 | `AQM-79-QSA-GEOMETRIC-FIELD-HOM-X-V` | `report/sections/79_quantum_system_association_geometric_field_hom_x_v.tex` | Geometric Field Association Hom(X,V) |
| 80 | `AQM-80-QSA-FINITE-RING-EXAMPLE-MATRIX` | `report/sections/80_quantum_system_association_finite_ring_example_matrix.tex` | Finite Ring Example Matrix |
| 81 | `AQM-81-QSA-RESIDUE-FIELD-SITE-ASSOCIATION` | `report/sections/81_quantum_system_association_residue_field_site_association.tex` | Residue-Field Site Association for \(\Spec R\) |
| 82 | `AQM-82-QSA-NILPOTENT-SENSITIVE-ASSOCIATION` | `report/sections/82_quantum_system_association_nilpotent_sensitive_association.tex` | Nilpotent-Sensitive Association |
| 83 | `AQM-83-QSA-PRODUCT-RINGS-TENSOR-FACTORS` | `report/sections/83_quantum_system_association_product_rings_tensor_factors.tex` | Product Rings and Tensor Factors |
| 84 | `AQM-84-QSA-INFINITE-RING-BOUNDARIES` | `report/sections/84_quantum_system_association_infinite_ring_boundaries.tex` | Infinite Ring Boundary Cases |
| 85 | `AQM-85-QSA-AGREEMENT-INEQUIVALENCE-TABLE` | `report/sections/85_quantum_system_association_agreement_inequivalence_table.tex` | Agreement and Inequivalence Table |
| 86 | `AQM-86-QSA-DEGENERATE-OVERRESTRICTIVE-CASES` | `report/sections/86_quantum_system_association_degenerate_overrestrictive_cases.tex` | Degenerate and Over-Restrictive Cases |
| 87 | `AQM-87-QSA-OPEN-PROBLEMS-NEXT-TARGETS` | `report/sections/87_quantum_system_association_open_problems_next_targets.tex` | Open Problems and Next Catalogue Targets |

## Maintenance Rules

- Add new body prose under `report/sections/`, not directly in `report.tex`.
- Keep `report.tex` to preamble, global macros/styles, ordered `\include`
  statements, bibliography, and `\end{document}`.
- Cite shards by stable label. Keep labels stable across ordinary edits.
- Every shard must start with `SHARD-ID`, `SHARD-TITLE`, two or three
  `SHARD-SUMMARY` lines, and `SHARD-KEYWORDS`.
- When adding, removing, renaming, or reordering shards, update this map,
  update `report/SHARD_CATALOG.md`, and run `make check-report-shards`.
- The rebuilt root `report.pdf` is the committed main report artifact. Build it
  with `make report` after report-source changes and include it in the same
  commit and push as the sources. LaTeX temporary products remain ignored.
