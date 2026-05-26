# data/SCHEMA.md - CSV Column Reference

Generated CSVs live under `runs/<YYYY-MM-DD>-<slug>/data/`; this file records
their schemas.

Twenty-two CSV outputs exist.

## Common Rules

- A row whose first column begins with `#` is a sentinel comment line and must
  be skipped by parsers.
- Exact values should be represented as strings in `_exact` columns.
- Floating approximations should be represented in `_float` columns.
- Residual columns must document norm, denominator, precision, and tolerance.

## CSV Schemas

| CSV path | Producing script | Status |
|---|---|---|
| `runs/2026-05-24-toric-supercharge/data/toric_supercharge_summary.csv` | `scripts/lattice_codes/toric_supercharge_validation.jl` | Active |
| `runs/2026-05-24-toric-chain-ghost-unification/data/toric_chain_ghost_unification.csv` | `scripts/lattice_codes/toric_chain_ghost_unification.jl` | Active |
| `runs/2026-05-24-symplectic-css-bridge/data/symplectic_css_bridge_summary.csv` | `scripts/lattice_codes/symplectic_css_bridge_validation.jl` | Active |
| `runs/2026-05-24-css-supercharge-symplectic-dictionary/data/css_supercharge_symplectic_dictionary.csv` | `scripts/lattice_codes/css_supercharge_symplectic_dictionary.jl` | Active |
| `runs/2026-05-24-steane-supercharge-molecular/data/steane_molecular_summary.csv` | `scripts/lattice_codes/steane_supercharge_molecular.jl` | Active |
| `runs/2026-05-24-steane-supercharge-molecular/data/steane_molecular_vectors.csv` | `scripts/lattice_codes/steane_supercharge_molecular.jl` | Active |
| `runs/2026-05-24-steane-supercharge-molecular/data/steane_cohomology_by_degree.csv` | `scripts/lattice_codes/steane_supercharge_molecular.jl` | Active |
| `runs/2026-05-24-steane-clifford-koszul-morphisms/data/steane_clifford_koszul_summary.csv` | `scripts/lattice_codes/steane_clifford_koszul_morphisms.jl` | Active |
| `runs/2026-05-24-steane-clifford-koszul-morphisms/data/steane_clifford_generator_maps.csv` | `scripts/lattice_codes/steane_clifford_koszul_morphisms.jl` | Active |
| `runs/2026-05-24-steane-all-clifford-ghost-gaussians/data/steane_all_clifford_generator_summary.csv` | `scripts/lattice_codes/steane_all_clifford_ghost_gaussians.jl` | Active |
| `runs/2026-05-24-steane-all-clifford-ghost-gaussians/data/steane_all_clifford_generator_images.csv` | `scripts/lattice_codes/steane_all_clifford_ghost_gaussians.jl` | Active |
| `runs/2026-05-24-steane-all-clifford-ghost-gaussians/data/steane_ghost_gaussian_elementaries.csv` | `scripts/lattice_codes/steane_all_clifford_ghost_gaussians.jl` | Active |
| `runs/2026-05-24-arithmetic-quantum-fields/data/arithmetic_quantum_field_examples.csv` | `scripts/bridges/arithmetic_quantum_fields.jl` | Active |
| `runs/2026-05-24-arithmetic-quantum-fields/data/arithmetic_quantum_field_bases.csv` | `scripts/bridges/arithmetic_quantum_fields.jl` | Active |
| `runs/2026-05-24-projective-line-sheaf-fields/data/projective_line_sheaf_field_summary.csv` | `scripts/bridges/projective_line_sheaf_fields.jl` | Active |
| `runs/2026-05-24-projective-line-sheaf-fields/data/projective_line_sheaf_field_basis_rows.csv` | `scripts/bridges/projective_line_sheaf_fields.jl` | Active |
| `runs/2026-05-24-projective-line-sheaf-fields/data/projective_line_stalk_rows.csv` | `scripts/bridges/projective_line_sheaf_fields.jl` | Active |
| `runs/2026-05-26-finite-ring-database/data/ring_summary.csv` | `scripts/arithmetic/finite_ring_db_exports.jl` | Active |
| `runs/2026-05-26-finite-ring-database/data/ring_presentations.csv` | `scripts/arithmetic/finite_ring_db_exports.jl` | Active |
| `runs/2026-05-26-finite-ring-database/data/ring_isomorphism_certificates.csv` | `scripts/arithmetic/finite_ring_db_exports.jl` | Active |
| `runs/2026-05-26-finite-ring-database/data/ring_quantization_summary.csv` | `scripts/arithmetic/finite_ring_db_exports.jl` | Active |
| `runs/2026-05-26-finite-ring-database/data/ring_quantization_obstruction.csv` | `scripts/arithmetic/finite_ring_db_exports.jl` | Active |

## toric_supercharge_summary.csv

Produced by: `scripts/lattice_codes/toric_supercharge_validation.jl`
Run bundle: `runs/2026-05-24-toric-supercharge/`
Report shard: `AQM-05-TORIC-SUPERCHARGE`
Sentinel: row 1 begins with `#` and states that this is an algebraic
certificate; no full physical or ghost Hilbert matrices are built.

| column | type | description |
|---|---|---|
| k | int | Linear size of the periodic square toric-code lattice. |
| nqubits | int | Number of physical edge qubits, equal to `2k^2`. |
| nchecks | int | Number of local star plus plaquette checks, equal to `2k^2`. |
| max_check_weight | int | Maximum number of qubits touched by a local check. |
| all_projectors_commute | bool | Whether every pair of stabilizer checks has zero binary symplectic commutator. |
| all_checks_square_to_identity | bool | Whether every stabilizer check squares to the identity in the Pauli representation used here. |
| stabilizer_rank | int | Rank over `F_2` of the binary stabilizer-check matrix. |
| independent_check_relations | int | Number of check relations, `nchecks - stabilizer_rank`. |
| logical_qubits | int | Number of encoded qubits, `nqubits - stabilizer_rank`. |
| physical_hilbert_dim_exact | string | Exact physical Hilbert-space dimension `2^nqubits`. |
| code_dim_exact | string | Exact toric-code protected-subspace dimension. |
| boundary_rank_degree_one_exact | string | Exact rank of the degree-one-to-degree-zero boundary map in the ghost formulation. |
| h0_dim_exact | string | Exact degree-zero homology/cohomology dimension selected by the local-check ghost supercharge. |
| q_square_certificate | bool | Algebraic certificate that `Q^2=0`, using commuting projectors and fermion anticommutation. |
| anticommutator_certificate | bool | Algebraic certificate that `{Q,Q^*}=sum_i P_i`, using commuting projectors and fermion anticommutation. |
| degree_zero_homology_matches_code | bool | Whether the computed degree-zero quotient dimension matches the toric-code code dimension. |

## toric_chain_ghost_unification.csv

Produced by: `scripts/lattice_codes/toric_chain_ghost_unification.jl`
Run bundle: `runs/2026-05-24-toric-chain-ghost-unification/`
Report shard: `AQM-05-TORIC-SUPERCHARGE`
Sentinel: row 1 begins with `#` and states that this is an algebraic
chain-complex certificate.

| column | type | description |
|---|---|---|
| k | int | Linear size of the periodic square toric-code lattice. |
| nvertices | int | Number of vertices, dimension of `C_0`. |
| nedges | int | Number of edges/qubits, dimension of `C_1`. |
| nfaces | int | Number of plaquettes, dimension of `C_2`. |
| boundary_square_zero | bool | Whether `partial_1 partial_2=0`, checked as even overlap between every vertex row and face boundary column. |
| star_masks_match_boundary_one | bool | Whether the star-check supports match the rows of `partial_1`. |
| plaquette_masks_match_boundary_two | bool | Whether the plaquette-check supports match the columns of `partial_2`. |
| rank_boundary_one | int | Rank over `F_2` of `partial_1`. |
| rank_boundary_two | int | Rank over `F_2` of `partial_2`. |
| h1_dim | int | First homology dimension, `nedges - rank_boundary_one - rank_boundary_two`. |
| code_dim_from_h1_exact | string | Exact dimension `2^h1_dim` predicted for the toric-code code space. |
| cellular_supercharge_square_zero | bool | Whether the finite-cell cochain supercharge squares to zero. |
| cellular_middle_cohomology_dim | int | Middle cohomology dimension of the cellular cochain supercharge. |
| cellular_middle_cohomology_basis_count_exact | string | Exact number of middle cohomology classes, equal to `2^cellular_middle_cohomology_dim`. |
| cochain_cocycle_count_exact | string | Exact size of `ker(partial_2^T)` in the computational `Z` basis. |
| cochain_coboundary_count_exact | string | Exact size of `im(partial_1^T)`, the star-generated coboundary orbit size. |
| css_commutation_from_boundary | bool | Whether CSS commutation follows from `partial_1 partial_2=0`. |
| ghost_checks_from_chain_complex | bool | Whether the supports used in the ghost supercharge are exactly the supports determined by the boundary complex. |

## symplectic_css_bridge_summary.csv

Produced by: `scripts/lattice_codes/symplectic_css_bridge_validation.jl`
Run bundle: `runs/2026-05-24-symplectic-css-bridge/`
Report shard: `AQM-08-SYMPLECTIC-CSS-BRIDGE`
Sentinel: row 1 begins with `#` and states that this is an exact prime-field
certificate; no Hilbert matrices are built.

| column | type | description |
|---|---|---|
| k | int | Linear size of the periodic square toric-code lattice. |
| p | int | Prime field characteristic and qudit dimension for this exact check. |
| nvertices | int | Number of vertices, dimension of `C_0`. |
| nedges | int | Number of oriented edges/qudits, dimension of `C_1`. |
| nfaces | int | Number of faces, dimension of `C_2`. |
| boundary_square_zero | bool | Whether the oriented matrices satisfy `partial_1 partial_2=0` over `F_p`. |
| css_isotropic | bool | Whether the CSS rowspace is isotropic in `F_p^n x F_p^n`. |
| rank_boundary_one | int | Rank over `F_p` of `partial_1`. |
| rank_boundary_two | int | Rank over `F_p` of `partial_2`. |
| h1_dim | int | Middle homology dimension, `nedges - rank_boundary_one - rank_boundary_two`. |
| symplectic_stabilizer_rank | int | Dimension of the isotropic stabilizer subspace. |
| encoded_qudits | int | Number of encoded qudits, `nedges - symplectic_stabilizer_rank`. |
| encoded_hilbert_dimension_exact | string | Exact code-space Hilbert dimension `p^encoded_qudits`. |
| chain_count_matches_symplectic_count | bool | Whether the homological and symplectic counts agree. |

## css_supercharge_symplectic_dictionary.csv

Produced by: `scripts/lattice_codes/css_supercharge_symplectic_dictionary.jl`
Run bundle: `runs/2026-05-24-css-supercharge-symplectic-dictionary/`
Report shard: `AQM-09-SYMPLECTIC-SUPERCHARGE-DICTIONARY`
Sentinel: row 1 begins with `#` and states that this is an exact dictionary
certificate; no Hilbert matrices are built.

| column | type | description |
|---|---|---|
| example | string | Name of the CSS example checked. |
| p | int | Prime field characteristic and qudit dimension. |
| n | int | Number of physical qudits. |
| x_rows | int | Number of supplied `X`-check rows. |
| z_rows | int | Number of supplied `Z`-check rows. |
| rank_x | int | Rank over `F_p` of the `X`-check rowspace. |
| rank_z | int | Rank over `F_p` of the `Z`-check rowspace. |
| stabilizer_rank | int | Dimension of the CSS isotropic stabilizer subspace `L`. |
| css_isotropic | bool | Whether the supplied CSS matrices satisfy `H_X H_Z^T=0`. |
| encoded_qudits | int | Number of encoded qudits, `n - stabilizer_rank`. |
| code_dimension_exact | string | Exact degree-zero supercharge cohomology dimension. |
| logical_symplectic_dimension | int | Dimension of `L^perp/L`. |
| l_perp_dimension | int | Dimension of the symplectic centralizer `L^perp`. |
| generator_ghost_count | int | Number of ghosts in a generator-basis supercharge. |
| basis_free_projective_ghost_count_exact | string | Number of ghosts in the projective-line basis-free variant. |
| q_square_certificate | bool | Algebraic certificate that the CSS ghost supercharge squares to zero. |
| anticommutator_certificate | bool | Algebraic certificate that `{Q,Q^*}` is the sum of violated-check projectors. |
| h0_matches_stabilizer_code | bool | Whether degree-zero supercharge cohomology matches the stabilizer code count. |

## steane_molecular_summary.csv

Produced by: `scripts/lattice_codes/steane_supercharge_molecular.jl`
Run bundle: `runs/2026-05-24-steane-supercharge-molecular/`
Report shards: `AQM-10-STEANE-SYMPLECTIC-MOLECULAR`,
`AQM-11-STEANE-SUPERCHARGE-COHOMOLOGY`
Sentinel: row 1 begins with `#` and states that this is an exact Steane
CSS/symplectic/supercharge molecular summary.

| column | type | description |
|---|---|---|
| n | int | Number of physical qubits. |
| check_rank | int | Rank of the three sourced binary check rows. |
| d_dim | int | Dimension of the rowspace `D`. |
| d_size | int | Number of vectors in `D`. |
| c_dim | int | Dimension of `C = D^perp`. |
| c_size | int | Number of vectors in `C`. |
| d_subset_c | bool | Whether `D <= C`. |
| logical_word | string | Binary representative `u` for `C/D`. |
| logical_word_in_c | bool | Whether `u in C`. |
| logical_word_not_in_d | bool | Whether `u notin D`. |
| h_h_transpose_zero | bool | Whether `H H^T=0` over `F_2`. |
| stabilizer_rank | int | Rank of the six CSS stabilizer labels. |
| l_dim | int | Dimension of the isotropic stabilizer subspace `L`. |
| l_size | int | Number of labels in `L`. |
| l_perp_dim | int | Dimension of `L^perp`. |
| l_perp_size | int | Number of labels in `L^perp`. |
| logical_symplectic_dim | int | Dimension of `L^perp/L`. |
| logical_pauli_classes | int | Number of logical Pauli label classes. |
| logical_pairing_x_z | int | Binary symplectic pairing of the chosen `Xbar,Zbar` representatives. |
| physical_hilbert_dim | int | Dimension of the seven-qubit Hilbert space. |
| ghost_count | int | Number of fermionic ghosts in the generator supercharge. |
| ghost_fock_dim | int | Dimension of the ghost exterior algebra. |
| full_ghost_hilbert_dim | int | Dimension of physical Hilbert space tensor ghost Fock space. |
| code_dim | int | Dimension of the no-ghost Steane code. |
| encoded_qubits | int | Number of encoded qubits. |
| syndrome_count | int | Number of stabilizer syndrome sectors. |
| nonzero_syndrome_count | int | Number of nonzero syndrome sectors. |
| syndrome_block_dim | int | Dimension of each syndrome sector. |
| full_q_cohomology_dim | int | Total dimension of full ghost-degree `Q` cohomology. |
| degree_zero_cohomology_dim | int | Dimension of `H^0(Q)`, the physical no-ghost code. |
| q_square_certificate | bool | Algebraic certificate that `Q^2=0`. |
| anticommutator_certificate | bool | Algebraic certificate that `{Q,Q^*}=sum_i P_i`. |
| codewords_match_two_cosets | bool | Whether `C` is exactly the union of the two sourced codeword cosets. |

## steane_molecular_vectors.csv

Produced by: `scripts/lattice_codes/steane_supercharge_molecular.jl`
Run bundle: `runs/2026-05-24-steane-supercharge-molecular/`
Report shards: `AQM-10-STEANE-SYMPLECTIC-MOLECULAR`,
`AQM-11-STEANE-SUPERCHARGE-COHOMOLOGY`
Sentinel: row 1 begins with `#` and states that the rows are exact binary
vectors for the sourced Steane presentation.

| column | type | description |
|---|---|---|
| object | string | Kind of row: `check_row`, `l_basis`, `D`, `u_plus_D`, `C`, `l_perp_basis`, or `logical_class`. |
| label | string | Human-readable label for the row. |
| x | string | Binary `X` exponent string, or a binary vector when `z` is blank. |
| z | string | Binary `Z` exponent string for Pauli labels; blank for ordinary binary vectors. |

## steane_cohomology_by_degree.csv

Produced by: `scripts/lattice_codes/steane_supercharge_molecular.jl`
Run bundle: `runs/2026-05-24-steane-supercharge-molecular/`
Report shard: `AQM-11-STEANE-SUPERCHARGE-COHOMOLOGY`
Sentinel: row 1 begins with `#` and states that this is full `Q`-cohomology by
ghost degree.

| column | type | description |
|---|---|---|
| degree | int | Ghost degree `q`. |
| ghost_binomial | int | Exterior-algebra dimension `binomial(6,q)`. |
| cohomology_dim | int | Dimension `2 * binomial(6,q)` of `H^q(Q)`. |

## steane_clifford_koszul_summary.csv

Produced by: `scripts/lattice_codes/steane_clifford_koszul_morphisms.jl`
Run bundle: `runs/2026-05-24-steane-clifford-koszul-morphisms/`
Report shard: `AQM-12-STEANE-CLIFFORD-KOSZUL-MORPHISMS`
Sentinel: row 1 begins with `#` and states that this is an exact
Clifford/Koszul morphism certificate for transversal `H` and `P`.

| column | type | description |
|---|---|---|
| n | int | Number of physical qubits. |
| stabilizer_generators | int | Number of chosen Steane stabilizer generators. |
| hadamard_maps_l_to_l | bool | Whether transversal Hadamard preserves the stabilizer label subspace. |
| hadamard_image_rank | int | Rank of the Hadamard image generator list. |
| hadamard_generator_permutation | string | Generator permutation induced by transversal Hadamard. |
| hadamard_exact_same_q_after_ghost_swap | bool | Whether Hadamard is an automorphism of the same `Q` after ghost swapping. |
| hadamard_logical_x_image | string | Image of the chosen logical `Xbar` label. |
| hadamard_logical_z_image | string | Image of the chosen logical `Zbar` label. |
| hadamard_code_action | string | Exact action on `|0bar>,|1bar>`. |
| phase_maps_l_to_l | bool | Whether transversal phase preserves the stabilizer label subspace. |
| phase_image_rank | int | Rank of the phase image generator list. |
| phase_generator_basis_change | string | Generator basis change induced by transversal phase. |
| phase_chain_isomorphism_to_image_presentation | bool | Whether phase gives a chain isomorphism to its image presentation. |
| phase_same_q_only_after_homotopy_retract | bool | Whether comparison to the original written `Q` uses the common syndrome-sector retract. |
| phase_logical_x_image | string | Image of the chosen logical `Xbar` label. |
| phase_logical_z_image | string | Image of the chosen logical `Zbar` label. |
| nonzero_syndrome_blocks | int | Number of nonzero syndrome sectors. |
| nonzero_syndrome_blocks_contractible | bool | Whether all nonzero syndrome sectors are contractible Koszul blocks. |
| zero_syndrome_cohomology_dim_by_degree | string | Semicolon-separated dimensions of zero-syndrome cohomology by ghost degree. |
| physical_h0_dim | int | Dimension of physical no-ghost cohomology. |
| full_cohomology_dim | int | Dimension of full ghost-degree cohomology. |

## steane_clifford_generator_maps.csv

Produced by: `scripts/lattice_codes/steane_clifford_koszul_morphisms.jl`
Run bundle: `runs/2026-05-24-steane-clifford-koszul-morphisms/`
Report shard: `AQM-12-STEANE-CLIFFORD-KOSZUL-MORPHISMS`
Sentinel: row 1 begins with `#` and states that the rows are Clifford images
of the six Steane stabilizer labels.

| column | type | description |
|---|---|---|
| morphism | string | Clifford morphism name: `transversal_H` or `transversal_P`. |
| source | string | Source stabilizer generator label. |
| image | string | Image Pauli label as `x|z` binary strings. |
| image_basis_coordinates | string | Coordinates of the image in the original Steane generator basis. |

## steane_all_clifford_generator_summary.csv

Produced by: `scripts/lattice_codes/steane_all_clifford_ghost_gaussians.jl`
Run bundle: `runs/2026-05-24-steane-all-clifford-ghost-gaussians/`
Report shard: `AQM-13-CLIFFORD-GROUP-GHOST-GAUSSIAN-THEOREM`
Sentinel: row 1 begins with `#` and states that this is an exact
Clifford-generator and ghost-Gaussian certificate.

| column | type | description |
|---|---|---|
| n | int | Number of physical Steane qubits. |
| steane_stabilizer_generators | int | Number of sourced Steane stabilizer generators. |
| standard_clifford_generator_gates | int | Count of checked standard Clifford generating gates. |
| hadamard_generator_gates | int | Number of single-qubit Hadamard generators checked. |
| phase_generator_gates | int | Number of single-qubit phase generators checked. |
| cnot_generator_gates | int | Number of ordered CNOT generators checked. |
| generator_image_rows | int | Number of signed stabilizer-generator image rows written. |
| all_generator_images_rank_six | bool | Whether every image list has binary rank six. |
| rank_six_gate_count | int | Number of Clifford generator gates whose six images have rank six. |
| all_generator_images_isotropic | bool | Whether every image list is binary symplectic-isotropic. |
| isotropic_gate_count | int | Number of Clifford generator gates with isotropic image lists. |
| negative_signed_images_from_steane_generators | int | Number of negative signed images among the checked one-gate Steane generator images. |
| transported_presentation_chain_map | string | Label for the exact Clifford covariance chain map. |
| theorem_extends_to_all_clifford_words_by_generation | bool | Whether the generator check is used with the H/P/CNOT generation theorem. |
| signed_pauli_convention | string | Compact label for the signed Hermitian Pauli convention. |
| elementary_gl6_ghost_generators | int | Row swaps plus row shears generating presentation changes. |
| row_swap_ghost_generators | int | Number of row-swap ghost maps. |
| row_shear_ghost_generators | int | Number of directed row-shear ghost maps. |
| shear_projector_identities_checked | int | Number of syndrome-sector shear projector identities checked. |
| shear_projector_identities_hold | bool | Whether all shear identities hold. |
| presentation_change_requires_operator_coefficients | bool | Whether full-chain shears require stabilizer-operator coefficients. |
| zero_syndrome_shear_reduces_to_scalar_exterior_gl | bool | Whether shears become ordinary exterior GL maps on the code sector. |
| no_bogoliubov_mixing_needed | bool | Whether the ghost transforms preserve ghost degree. |

## steane_all_clifford_generator_images.csv

Produced by: `scripts/lattice_codes/steane_all_clifford_ghost_gaussians.jl`
Run bundle: `runs/2026-05-24-steane-all-clifford-ghost-gaussians/`
Report shard: `AQM-13-CLIFFORD-GROUP-GHOST-GAUSSIAN-THEOREM`
Sentinel: row 1 begins with `#` and states that the rows are images of the
six Steane generators under the standard H/P/CNOT Clifford generating gates.

| column | type | description |
|---|---|---|
| gate | string | Clifford generator name, e.g. `H1`, `P1`, or `CNOT1_2`. |
| gate_kind | string | Gate family: `H`, `P`, or `CNOT`. |
| source | string | Source Steane stabilizer generator label. |
| image_sign | int | Sign of the Hermitian signed Pauli image. |
| image | string | Unsigned binary Pauli label as `x|z`. |
| signed_image | string | Signed binary Pauli label. |
| image_list_rank | int | Rank of all six images for this gate. |
| image_list_isotropic | bool | Whether all six images for this gate commute symplectically. |

## steane_ghost_gaussian_elementaries.csv

Produced by: `scripts/lattice_codes/steane_all_clifford_ghost_gaussians.jl`
Run bundle: `runs/2026-05-24-steane-all-clifford-ghost-gaussians/`
Report shard: `AQM-13-CLIFFORD-GROUP-GHOST-GAUSSIAN-THEOREM`
Sentinel: row 1 begins with `#` and states that the rows are elementary GL6
presentation moves and their ghost-Gaussian lifts.

| column | type | description |
|---|---|---|
| operation | string | `row_swap` or `row_shear`. |
| a | int | First generator index. |
| b | int | Second generator index. |
| generator_change | string | Stabilizer presentation move. |
| projector_identity | string | Projector identity used by the move. |
| ghost_gaussian | string | Creation-operator action of the ghost Gaussian. |
| checked_syndromes | int | Number of syndrome sectors checked for this row. |
| identity_holds | bool | Whether the projector identity holds. |
| zero_syndrome_map | string | Simplified exterior ghost map on the code sector. |

## arithmetic_quantum_field_examples.csv

Produced by: `scripts/bridges/arithmetic_quantum_fields.jl`
Run bundle: `runs/2026-05-24-arithmetic-quantum-fields/`
Report shard: `AQM-14-ARITHMETIC-QUANTUM-FIELDS`
Sentinel: row 1 begins with `#` and states that the rows are exact `F_3`
finite-function-space symplectic certificates; no Hilbert matrices are built.

| column | type | description |
|---|---|---|
| example | string | Stable example slug. |
| p | int | Prime field characteristic, here `3`. |
| physical_space | string | Description of the finite physical point set. |
| field_space | string | Description of the chosen scalar function space extended to `F_3^2`. |
| point_count | int | Number of physical points. |
| scalar_basis_dim | int | Dimension of the scalar function space `U`. |
| scalar_pairing_rank | int | Rank of `B(f,g)=sum_x f(x)g(x)` over `F_3`. |
| field_phase_dim | int | Dimension of `E=U q + U p`. |
| symplectic_rank | int | Rank of the pointwise symplectic form on `E`. |
| radical_dim | int | Dimension of the radical of the pointwise symplectic form. |
| reduced_phase_dim | int | Dimension of `E/rad(E)`. |
| total_field_labels_exact | string | Exact count `3^field_phase_dim`. |
| radical_labels_exact | string | Exact count `3^radical_dim`. |
| reduced_weyl_labels_exact | string | Exact count `3^reduced_phase_dim`. |
| hilbert_dim_exact | string | Hilbert dimension of the reduced Weyl representation. |
| observable_basis_dim_exact | string | Dimension of the Weyl operator basis after reduction. |
| nondegenerate | bool | Whether the chosen field space has zero radical. |

## arithmetic_quantum_field_bases.csv

Produced by: `scripts/bridges/arithmetic_quantum_fields.jl`
Run bundle: `runs/2026-05-24-arithmetic-quantum-fields/`
Report shard: `AQM-14-ARITHMETIC-QUANTUM-FIELDS`
Sentinel: row 1 begins with `#` and states that rows are basis values and
scalar Gram rows for the exact `F_3` examples.

| column | type | description |
|---|---|---|
| example | string | Stable example slug matching the summary CSV. |
| row_kind | string | `basis_values` or `scalar_gram_row`. |
| label | string | Basis label for this row. |
| values | string | Space-separated `F_3` row values. |

## projective_line_sheaf_field_summary.csv

Produced by: `scripts/bridges/projective_line_sheaf_fields.jl`
Run bundle: `runs/2026-05-24-projective-line-sheaf-fields/`
Report shards: `AQM-15-PROJECTIVE-SHEAF-FIELD-DEFINITIONS`,
`AQM-16-PROJECTIVE-LINE-SHEAF-FIELD-CALCULATION`
Sentinel: row 1 begins with `#` and states that the rows are exact
`F_3` certificates for \(H^0(\mathbf P^1,\mathcal O(d))\otimes F_3^2\),
`d=0..4`; no Weyl matrices are built.

| column | type | description |
|---|---|---|
| example | string | Stable example slug, `P1_F3_Od`. |
| d | int | Twist degree in `O(d)`. |
| p | int | Prime field characteristic, here `3`. |
| scheme | string | Scheme label, here `P1_F3`. |
| sheaf | string | Sheaf label, here `O(d)`. |
| rational_points | string | Space-separated rational point representatives in the fixed evaluation order. |
| point_count | int | Number of rational points used in the finite pairing. |
| scalar_section_dim | int | Dimension of `H^0(P1,O(d))` over `F_3`. |
| evaluation_rank | int | Rank over `F_3` of the scalar section evaluation matrix at rational points. |
| evaluation_kernel_dim | int | Scalar section dimension minus evaluation rank. |
| scalar_pairing_rank | int | Rank over `F_3` of `B(s,t)=sum_P s(P)t(P)`. |
| field_phase_dim | int | Dimension of `H^0(P1,O(d)) tensor F_3^2`. |
| symplectic_rank | int | Rank of the induced pointwise symplectic form. |
| radical_dim | int | Dimension of the radical of the induced pointwise symplectic form. |
| reduced_phase_dim | int | Dimension of the reduced symplectic Weyl label space. |
| total_section_labels_exact | string | Exact count `3^field_phase_dim`. |
| evaluation_kernel_labels_exact | string | Exact count of `V`-valued labels vanishing at all chosen rational points. |
| radical_labels_exact | string | Exact count `3^radical_dim`. |
| reduced_weyl_labels_exact | string | Exact count `3^reduced_phase_dim`. |
| hilbert_dim_exact | string | Hilbert dimension of the reduced Weyl representation. |
| observable_basis_dim_exact | string | Dimension of the reduced Weyl operator basis. |
| nondegenerate | bool | Whether the induced pointwise symplectic form has zero radical. |

## projective_line_sheaf_field_basis_rows.csv

Produced by: `scripts/bridges/projective_line_sheaf_fields.jl`
Run bundle: `runs/2026-05-24-projective-line-sheaf-fields/`
Report shard: `AQM-16-PROJECTIVE-LINE-SHEAF-FIELD-CALCULATION`
Sentinel: row 1 begins with `#` and states that rows are basis values and
scalar Gram rows for the exact `P1(F3), O(d), d=0..4` examples.

| column | type | description |
|---|---|---|
| example | string | Stable example slug matching the summary CSV. |
| d | int | Twist degree in `O(d)`. |
| row_kind | string | `basis_values` or `scalar_gram_row`. |
| label | string | Basis label for this row. |
| values | string | Space-separated `F_3` row values. |

## projective_line_stalk_rows.csv

Produced by: `scripts/bridges/projective_line_sheaf_fields.jl`
Run bundle: `runs/2026-05-24-projective-line-sheaf-fields/`
Report shard: `AQM-17-PROJECTIVE-LINE-STALKS`
Sentinel: row 1 begins with `#` and states that rows are exact symbolic stalk
germs for `P1(F3), O(d), d=0..4` at the four rational points used by the
finite pairing.

| column | type | description |
|---|---|---|
| d | int | Twist degree in `O(d)`. |
| point_label | string | Rational point representative. |
| homogeneous_prime | string | Homogeneous prime ideal of `F_3[X,Y]` for this point. |
| chart | string | Standard affine chart used to compute the stalk. |
| local_coordinate | string | Affine coordinate on the chosen chart. |
| local_maximal_ideal | string | Maximal ideal of the chart coordinate ring at the point. |
| local_ring | string | Local ring of `P1_F3` at the point in chart notation. |
| residue_field | string | Residue field, here `F3` for all rational points. |
| local_frame | string | Chosen local frame of `O(d)` on the chart. |
| basis_label | string | Homogeneous monomial section label. |
| x_exponent | int | Exponent of `X` in the monomial section. |
| y_exponent | int | Exponent of `Y` in the monomial section. |
| germ_in_frame | string | Germ of the monomial written in the chosen local frame. |
| residue_value | int | Image of the germ in the residue field after setting the local coordinate to its point value. |

## ring_summary.csv

Produced by: `scripts/arithmetic/finite_ring_db_exports.jl`
Run bundle: `runs/2026-05-26-finite-ring-database/`
Report shard: _pending_
Sentinel note: row 1 begins with `#` and states that this is an in-memory MVP
review export from local `finite_ring_mvp_*` helpers. It does not populate or
read `finite_rings.sqlite`.

| column | type | description |
|---|---|---|
| ring_id | string | Stable canonical ring ID for the deduplicated representative. |
| representative_name | string | Local MVP representative name retained after deduplication. |
| presentation_count | int | Number of local MVP presentations attached to this representative, including certified merges. |
| source_names | string | Canonical JSON array of local presentation/example names attached to the representative. |
| order_exact | string | Exact finite cardinality of the ring as a decimal string. |
| characteristic_exact | string | Exact characteristic as a decimal string; the zero-ring convention stores `1`. |
| additive_invariants_json | string | Canonical JSON array of additive invariant factors. |
| local_status | string | Open status token for the local-ring predicate; `unknown` in this MVP export. |
| reduced_status | string | Open status token for the reduced-ring predicate; `unknown` in this MVP export. |
| field_status | string | Open status token for the field predicate; `unknown` in this MVP export. |
| product_status | string | Open status token for the product-decomposition predicate; `unknown` in this MVP export. |
| frobenius_status | string | Open status token for the Frobenius-ring predicate; `unknown` in this MVP export. |
| generating_character_status | string | Open status token for certified generating-character data; `unknown` in this MVP export. |
| residue_field_sizes_json | string | Canonical JSON array of residue-field sizes, empty array for the zero ring, or JSON string `"unknown"` when not certified. |
| audit_status | string | Audit state for this row; `not_audited` in this MVP export. |

## ring_presentations.csv

Produced by: `scripts/arithmetic/finite_ring_db_exports.jl`
Run bundle: `runs/2026-05-26-finite-ring-database/`
Report shard: _pending_
Sentinel note: row 1 begins with `#` and states that this is an in-memory MVP
review export from local `finite_ring_mvp_*` helpers. It does not populate or
read `finite_rings.sqlite`.

| column | type | description |
|---|---|---|
| presentation_id | string | Stable presentation ID derived from the canonical JSON presentation payload. |
| name | string | Local MVP presentation name. |
| canonical_ring_id | string | Stable ring ID of the canonical deduplicated representative. |
| canonical_name | string | Representative presentation name after deduplication. |
| link_status | string | Presentation-to-representative status, currently `canonical` or `certified_isomorphic_merge`. |
| presentation_type | string | Local construction class, currently `manual_mvp_structure_constants`. |
| order_exact | string | Exact finite cardinality of the presentation as a decimal string. |
| characteristic_exact | string | Exact characteristic as a decimal string; the zero-ring convention stores `1`. |
| additive_invariants_json | string | Canonical JSON array of additive invariant factors. |
| source_locator | string | Local source and convention locator for the presentation payload. |

## ring_isomorphism_certificates.csv

Produced by: `scripts/arithmetic/finite_ring_db_exports.jl`
Run bundle: `runs/2026-05-26-finite-ring-database/`
Report shard: _pending_
Sentinel note: row 1 begins with `#` and states that this is an in-memory MVP
review export from local `finite_ring_mvp_*` helpers. It does not populate or
read `finite_rings.sqlite`.

| column | type | description |
|---|---|---|
| certificate_id | string | Stable ID for the verifier-approved isomorphism certificate row. |
| source_presentation_id | string | Presentation ID for the presentation being merged. |
| target_presentation_id | string | Presentation ID for the canonical target presentation. |
| source_name | string | Local MVP name of the source presentation. |
| target_name | string | Local MVP name of the target presentation. |
| verdict | string | Certificate verdict; `isomorphic` for rows emitted by this MVP exporter. |
| certificate_type | string | Certificate payload type, currently `additive_generator_image_matrix`. |
| additive_generator_image_matrix_json | string | Canonical JSON matrix whose rows give source additive-generator images in target coordinates. |
| checked_by | string | Verifier helper that checked the certificate. |
| checker_result | string | Verifier result token, currently `ok` for emitted rows. |
| identity_preserved | bool | Whether the certificate sends the source identity to the target identity. |
| addition_preserved | bool | Whether the additive generator map is well-defined/addition-preserving. |
| multiplication_preserved | bool | Whether the certificate preserves multiplication. |
| bijective_additive_map | bool | Whether the additive map is bijective. |

## ring_quantization_summary.csv

Produced by: `scripts/arithmetic/finite_ring_db_exports.jl`
Run bundle: `runs/2026-05-26-finite-ring-database/`
Report shard: _pending_
Sentinel note: row 1 begins with `#` and states that this is an in-memory MVP
review export from local `finite_ring_mvp_*` helpers. It does not populate or
read `finite_rings.sqlite`.

| column | type | description |
|---|---|---|
| quantization_id | string | Stable quantization row ID built from the canonical ring ID, layer, and MVP name segment. |
| canonical_ring_id | string | Stable ring ID of the canonical deduplicated representative. |
| presentation_name | string | Local MVP presentation name for the quantization record. |
| layer | string | Quantization layer, currently `residue` or `thickened_frobenius`. |
| status | string | Row status, currently `available`, `blocked`, or `not_applicable_until_layer_semantics`. |
| hilbert_dim_exact | string | Exact Hilbert dimension when available; blank for blocked or not-applicable rows. |
| label_group_order_exact | string | Exact Weyl-label group order when available; blank for blocked or not-applicable rows. |
| observable_basis_dim_exact | string | Exact observable-basis dimension when available; blank for blocked or not-applicable rows. |
| construction | string | Construction label for available rows; blank for obstruction-only rows. |
| source_locator | string | Local source, convention, or report locator for available rows; blank when the row only records an obstruction. |
| obstruction | string | Obstruction code for non-available rows; blank when `status` is `available`. |

## ring_quantization_obstruction.csv

Produced by: `scripts/arithmetic/finite_ring_db_exports.jl`
Run bundle: `runs/2026-05-26-finite-ring-database/`
Report shard: _pending_
Sentinel note: row 1 begins with `#` and states that this is an in-memory MVP
review export from local `finite_ring_mvp_*` helpers. It does not populate or
read `finite_rings.sqlite`.

| column | type | description |
|---|---|---|
| canonical_ring_id | string | Stable ring ID of the canonical deduplicated representative. |
| presentation_name | string | Local MVP presentation name for the obstructed quantization record. |
| layer | string | Quantization layer, currently `residue` or `thickened_frobenius`. |
| status | string | Non-available row status, currently `blocked` or `not_applicable_until_layer_semantics`. |
| obstruction | string | Obstruction code explaining why this layer is not available in the MVP export. |
