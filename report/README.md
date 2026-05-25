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

## Maintenance Rules

- Add new body prose under `report/sections/`, not directly in `report.tex`.
- Keep `report.tex` to preamble, global macros/styles, ordered `\include`
  statements, bibliography, and `\end{document}`.
- Cite shards by stable label. Keep labels stable across ordinary edits.
- Every shard must start with `SHARD-ID`, `SHARD-TITLE`, two or three
  `SHARD-SUMMARY` lines, and `SHARD-KEYWORDS`.
- When adding, removing, renaming, or reordering shards, update this map,
  update `report/SHARD_CATALOG.md`, and run `make check-report-shards`.
- The rebuilt `report.pdf` and LaTeX build products are generated artifacts.
