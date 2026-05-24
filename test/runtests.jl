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
