using Test
using ArithmeticQuantumMechanics

@testset "scaffold paths" begin
    root = project_root()
    @test isfile(joinpath(root, "report.tex"))
    @test isdir(joinpath(root, "report", "sections"))
    @test run_bundle_path("2099-01-01-example") ==
          joinpath(root, "runs", "2099-01-01-example")
end

@testset "algebraic toric-code ghost boundary supercharge" begin
    for k in 2:4
        summary = toric_supercharge_summary(k)
        @test summary.nqubits == 2k^2
        @test summary.nchecks == 2k^2
        @test summary.max_check_weight == 4
        @test summary.all_projectors_commute
        @test summary.all_checks_square_to_identity
        @test summary.stabilizer_rank == 2k^2 - 2
        @test summary.independent_check_relations == 2
        @test summary.logical_qubits == 2
        @test summary.code_dim_exact == "4"
        @test summary.h0_dim_exact == "4"
        @test summary.q_square_certificate
        @test summary.anticommutator_certificate
        @test summary.degree_zero_homology_matches_code
    end
end

@testset "toric chain complex and ghost checks agree" begin
    for k in 2:4
        summary = toric_chain_ghost_unification_summary(k)
        @test summary.nvertices == k^2
        @test summary.nedges == 2k^2
        @test summary.nfaces == k^2
        @test summary.boundary_square_zero
        @test summary.star_masks_match_boundary_one
        @test summary.plaquette_masks_match_boundary_two
        @test summary.rank_boundary_one == k^2 - 1
        @test summary.rank_boundary_two == k^2 - 1
        @test summary.h1_dim == 2
        @test summary.code_dim_from_h1_exact == "4"
        @test summary.cellular_supercharge_square_zero
        @test summary.cellular_middle_cohomology_dim == 2
        @test summary.cellular_middle_cohomology_basis_count_exact == "4"
        @test summary.cochain_cocycle_count_exact == string(BigInt(1) << (2k^2 - (k^2 - 1)))
        @test summary.cochain_coboundary_count_exact == string(BigInt(1) << (k^2 - 1))
        @test summary.css_commutation_from_boundary
        @test summary.ghost_checks_from_chain_complex
    end
end

@testset "symplectic CSS bridge over prime fields" begin
    for k in 2:4, p in (2, 3, 5)
        boundary_one, boundary_two = oriented_toric_boundary_matrices(k, p)
        @test all(==(0), matmul_modp(boundary_one, boundary_two, p))
        @test css_symplectic_isotropic(boundary_one, boundary_two, p)

        summary = symplectic_css_bridge_summary(k, p)
        @test summary.boundary_square_zero
        @test summary.css_isotropic
        @test summary.rank_boundary_one == k^2 - 1
        @test summary.rank_boundary_two == k^2 - 1
        @test summary.h1_dim == 2
        @test summary.symplectic_stabilizer_rank == 2k^2 - 2
        @test summary.encoded_qudits == 2
        @test summary.encoded_hilbert_dimension_exact == string(BigInt(p)^2)
        @test summary.chain_count_matches_symplectic_count
    end
end

@testset "CSS supercharge symplectic dictionary" begin
    hx, hz = steane_css_matrices()
    steane = css_supercharge_dictionary_summary(hx, hz, 2)
    @test steane.css_isotropic
    @test steane.n == 7
    @test steane.rank_x == 3
    @test steane.rank_z == 3
    @test steane.stabilizer_rank == 6
    @test steane.encoded_qudits == 1
    @test steane.code_dimension_exact == "2"
    @test steane.logical_symplectic_dimension == 2
    @test steane.l_perp_dimension == 8
    @test steane.generator_ghost_count == 6
    @test steane.basis_free_projective_ghost_count_exact == "63"
    @test steane.q_square_certificate
    @test steane.anticommutator_certificate
    @test steane.h0_matches_stabilizer_code

    hx3, hz3 = qutrit_css_toy_matrices()
    qutrit = css_supercharge_dictionary_summary(hx3, hz3, 3)
    @test qutrit.css_isotropic
    @test qutrit.n == 3
    @test qutrit.stabilizer_rank == 2
    @test qutrit.encoded_qudits == 1
    @test qutrit.code_dimension_exact == "3"
    @test qutrit.logical_symplectic_dimension == 2
    @test qutrit.basis_free_projective_ghost_count_exact == "4"
end

@testset "Steane molecular supercharge data" begin
    data = steane_binary_space_rows()
    h = data.h
    @test h == [
        1 1 1 1 0 0 0
        1 1 0 0 1 1 0
        1 0 1 0 1 0 1
    ]
    @test all(==(0), matmul_modp(h, transpose(h), 2))
    @test length(data.d_space) == 8
    @test length(data.c_space) == 16
    @test data.logical_word == [0, 0, 0, 0, 1, 1, 1]

    summary = steane_molecular_summary()
    @test summary.d_subset_c
    @test summary.logical_word_in_c
    @test summary.logical_word_not_in_d
    @test summary.stabilizer_rank == 6
    @test summary.l_dim == 6
    @test summary.l_size == 64
    @test summary.l_perp_dim == 8
    @test summary.l_perp_size == 256
    @test summary.logical_symplectic_dim == 2
    @test summary.logical_pauli_classes == 4
    @test summary.logical_pairing_x_z == 1
    @test summary.physical_hilbert_dim == 128
    @test summary.ghost_fock_dim == 64
    @test summary.full_ghost_hilbert_dim == 8192
    @test summary.code_dim == 2
    @test summary.syndrome_count == 64
    @test summary.nonzero_syndrome_count == 63
    @test summary.syndrome_block_dim == 2
    @test summary.full_q_cohomology_dim == 128
    @test summary.degree_zero_cohomology_dim == 2
    @test summary.q_square_certificate
    @test summary.anticommutator_certificate
    @test summary.codewords_match_two_cosets

    @test [row.cohomology_dim for row in steane_cohomology_by_degree()] ==
          [2, 12, 30, 40, 30, 12, 2]
end

@testset "Steane Clifford Koszul morphisms" begin
    summary = steane_clifford_morphism_summary()
    @test summary.hadamard_maps_l_to_l
    @test summary.hadamard_image_rank == 6
    @test summary.hadamard_exact_same_q_after_ghost_swap
    @test summary.hadamard_logical_x_image == "Zbar"
    @test summary.hadamard_logical_z_image == "Xbar"
    @test summary.phase_maps_l_to_l
    @test summary.phase_image_rank == 6
    @test summary.phase_chain_isomorphism_to_image_presentation
    @test summary.phase_same_q_only_after_homotopy_retract
    @test summary.phase_logical_x_image == "Xbar+Zbar"
    @test summary.phase_logical_z_image == "Zbar"
    @test summary.nonzero_syndrome_blocks == 63
    @test summary.nonzero_syndrome_blocks_contractible
    @test summary.zero_syndrome_cohomology_dim_by_degree == "2;12;30;40;30;12;2"
    @test summary.physical_h0_dim == 2
    @test summary.full_cohomology_dim == 128

    rows = steane_clifford_morphism_rows()
    @test length(rows) == 12
    @test rows[1].morphism == "transversal_H"
    @test rows[1].source == "X1"
    @test rows[1].image == "0000000|1111000"
    @test rows[1].image_basis_coordinates == "Z1"
    @test rows[2].morphism == "transversal_P"
    @test rows[2].source == "X1"
    @test rows[2].image == "1111000|1111000"
    @test rows[2].image_basis_coordinates == "X1+Z1"
end

@testset "Steane all-Clifford ghost Gaussian theorem data" begin
    summary = steane_all_clifford_generator_summary()
    @test summary.standard_clifford_generator_gates == 56
    @test summary.hadamard_generator_gates == 7
    @test summary.phase_generator_gates == 7
    @test summary.cnot_generator_gates == 42
    @test summary.generator_image_rows == 336
    @test summary.all_generator_images_rank_six
    @test summary.rank_six_gate_count == 56
    @test summary.all_generator_images_isotropic
    @test summary.isotropic_gate_count == 56
    @test summary.transported_presentation_chain_map == "U_tensor_identity_on_ghosts"
    @test summary.theorem_extends_to_all_clifford_words_by_generation
    @test summary.elementary_gl6_ghost_generators == 45
    @test summary.row_swap_ghost_generators == 15
    @test summary.row_shear_ghost_generators == 30
    @test summary.shear_projector_identities_checked == 1920
    @test summary.shear_projector_identities_hold
    @test summary.presentation_change_requires_operator_coefficients
    @test summary.zero_syndrome_shear_reduces_to_scalar_exterior_gl
    @test summary.no_bogoliubov_mixing_needed

    images = steane_all_clifford_generator_rows()
    @test length(images) == 336
    @test images[1].gate == "H1"
    @test images[1].source == "X1"
    @test images[1].signed_image == "+0111000|1000000"
    @test all(row -> row.image_list_rank == 6, images)
    @test all(row -> row.image_list_isotropic, images)

    ghosts = steane_ghost_gaussian_elementary_rows()
    @test length(ghosts) == 45
    @test count(row -> row.operation == "row_swap", ghosts) == 15
    @test count(row -> row.operation == "row_shear", ghosts) == 30
    @test all(row -> row.identity_holds, ghosts)
    @test any(row -> row.operation == "row_shear" &&
                     row.projector_identity == "P(S1*S2)=P(S1)+S1*P(S2)",
              ghosts)
end

@testset "Arithmetic quantum field examples" begin
    rows = arithmetic_quantum_field_summary_rows()
    by_name = Dict(row.example => row for row in rows)
    @test length(rows) == 11

    finite = by_name["finite_set_3_full"]
    @test finite.scalar_basis_dim == 3
    @test finite.scalar_pairing_rank == 3
    @test finite.field_phase_dim == 6
    @test finite.radical_dim == 0
    @test finite.reduced_weyl_labels_exact == "729"
    @test finite.hilbert_dim_exact == "27"
    @test finite.observable_basis_dim_exact == "729"
    @test finite.nondegenerate

    linear = by_name["vector_space_F3_linear"]
    @test linear.scalar_basis_dim == 1
    @test linear.scalar_pairing_rank == 1
    @test linear.reduced_weyl_labels_exact == "9"
    @test linear.hilbert_dim_exact == "3"

    affine = by_name["vector_space_F3_affine"]
    @test affine.scalar_basis_dim == 2
    @test affine.scalar_pairing_rank == 1
    @test affine.field_phase_dim == 4
    @test affine.radical_dim == 2
    @test affine.radical_labels_exact == "9"
    @test !affine.nondegenerate

    plane = by_name["affine_plane_F3_linear"]
    @test plane.scalar_pairing_rank == 0
    @test plane.symplectic_rank == 0
    @test plane.radical_dim == 4
    @test plane.reduced_weyl_labels_exact == "1"
    @test !plane.nondegenerate

    parabola = by_name["parabola_F3_degree_le_1"]
    @test parabola.scalar_basis_dim == 3
    @test parabola.scalar_pairing_rank == 3
    @test parabola.field_phase_dim == 6
    @test parabola.reduced_weyl_labels_exact == "729"
    @test parabola.nondegenerate

    basis_rows = arithmetic_quantum_field_basis_rows()
    @test any(row -> row.example == "parabola_F3_degree_le_1" &&
                     row.row_kind == "basis_values" &&
                     row.label == "y" &&
                     row.values == "0 1 1",
              basis_rows)
    @test any(row -> row.example == "vector_space_F3_affine" &&
                     row.row_kind == "scalar_gram_row" &&
                     row.label == "1" &&
                     row.values == "0 0",
              basis_rows)
end

@testset "Projective-line sheaf field examples" begin
    @test p1_rational_point_labels(3) == ["[1:0]", "[0:1]", "[1:1]", "[2:1]"]
    @test p1_od_basis_labels(2) == ["X^2", "XY", "Y^2"]
    @test p1_od_evaluation_matrix(2, 3) == [
        1 0 1 1
        0 0 1 2
        0 1 1 1
    ]

    rows = projective_line_sheaf_field_summary_rows(; p=3, max_degree=4)
    by_degree = Dict(row.d => row for row in rows)
    @test length(rows) == 5

    @test by_degree[0].scalar_section_dim == 1
    @test by_degree[0].scalar_pairing_rank == 1
    @test by_degree[0].nondegenerate

    @test by_degree[1].evaluation_rank == 2
    @test by_degree[1].scalar_pairing_rank == 0
    @test by_degree[1].radical_dim == 4
    @test by_degree[1].reduced_weyl_labels_exact == "1"
    @test !by_degree[1].nondegenerate

    @test by_degree[2].scalar_section_dim == 3
    @test by_degree[2].scalar_pairing_rank == 3
    @test by_degree[2].hilbert_dim_exact == "27"
    @test by_degree[2].nondegenerate

    @test by_degree[4].scalar_section_dim == 5
    @test by_degree[4].evaluation_rank == 4
    @test by_degree[4].evaluation_kernel_dim == 1
    @test by_degree[4].radical_dim == 2
    @test by_degree[4].evaluation_kernel_labels_exact == "9"
    @test !by_degree[4].nondegenerate

    basis_rows = projective_line_sheaf_field_basis_rows(; p=3, max_degree=4)
    @test any(row -> row.example == "P1_F3_O2" &&
                     row.row_kind == "scalar_gram_row" &&
                     row.label == "XY" &&
                     row.values == "0 2 0",
              basis_rows)

    stalk_rows = projective_line_stalk_rows(; p=3, max_degree=4)
    @test length(stalk_rows) == 60
    point_labels = p1_rational_point_labels(3)
    stalk_by_key = Dict((row.d, row.basis_label, row.point_label) => row for row in stalk_rows)
    for d in 0:4
        values = p1_od_evaluation_matrix(d, 3)
        for (basis_index, basis_label) in enumerate(p1_od_basis_labels(d))
            for (point_index, point_label) in enumerate(point_labels)
                row = stalk_by_key[(d, basis_label, point_label)]
                @test row.residue_value == values[basis_index, point_index]
            end
        end
    end
    @test any(row -> row.d == 2 &&
                     row.point_label == "[1:0]" &&
                     row.local_ring == "F3[u]_(u)" &&
                     row.basis_label == "XY" &&
                     row.germ_in_frame == "u*e_X^(2)" &&
                     row.residue_value == 0,
              stalk_rows)
    @test any(row -> row.d == 4 &&
                     row.point_label == "[2:1]" &&
                     row.homogeneous_prime == "(X-2Y)=(X+Y)" &&
                     row.local_ring == "F3[v]_(v-2)" &&
                     row.basis_label == "X^3Y" &&
                     row.germ_in_frame == "v^3*e_Y^(4)" &&
                     row.residue_value == 2,
              stalk_rows)
end
