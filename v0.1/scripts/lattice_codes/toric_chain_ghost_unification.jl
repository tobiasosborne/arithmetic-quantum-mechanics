using ArithmeticQuantumMechanics

Base.include(@__MODULE__, joinpath(@__DIR__, "..", "_common.jl"))

const RUN = "2026-05-24-toric-chain-ghost-unification"

function main()
    summary = toric_chain_ghost_unification_summary(4)
    path = data_path(RUN, "toric_chain_ghost_unification.csv")
    header = join((
        "k",
        "nvertices",
        "nedges",
        "nfaces",
        "boundary_square_zero",
        "star_masks_match_boundary_one",
        "plaquette_masks_match_boundary_two",
        "rank_boundary_one",
        "rank_boundary_two",
        "h1_dim",
        "code_dim_from_h1_exact",
        "cellular_supercharge_square_zero",
        "cellular_middle_cohomology_dim",
        "cellular_middle_cohomology_basis_count_exact",
        "cochain_cocycle_count_exact",
        "cochain_coboundary_count_exact",
        "css_commutation_from_boundary",
        "ghost_checks_from_chain_complex",
    ), ",")

    with_csv(path, header;
             sentinel="Algebraic chain-complex certificate: validates partial_1 partial_2=0 and identifies boundary-map supports with ghost-supercharge checks.") do io
        println(io, join((
            summary.k,
            summary.nvertices,
            summary.nedges,
            summary.nfaces,
            summary.boundary_square_zero,
            summary.star_masks_match_boundary_one,
            summary.plaquette_masks_match_boundary_two,
            summary.rank_boundary_one,
            summary.rank_boundary_two,
            summary.h1_dim,
            summary.code_dim_from_h1_exact,
            summary.cellular_supercharge_square_zero,
            summary.cellular_middle_cohomology_dim,
            summary.cellular_middle_cohomology_basis_count_exact,
            summary.cochain_cocycle_count_exact,
            summary.cochain_coboundary_count_exact,
            summary.css_commutation_from_boundary,
            summary.ghost_checks_from_chain_complex,
        ), ","))
    end
    println("wrote ", path)
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
