using ArithmeticQuantumMechanics

Base.include(@__MODULE__, joinpath(@__DIR__, "..", "_common.jl"))

const RUN = "2026-05-24-toric-supercharge"

function main()
    summary = toric_supercharge_summary(4)
    path = data_path(RUN, "toric_supercharge_summary.csv")
    header = join((
        "k",
        "nqubits",
        "nchecks",
        "max_check_weight",
        "all_projectors_commute",
        "all_checks_square_to_identity",
        "stabilizer_rank",
        "independent_check_relations",
        "logical_qubits",
        "physical_hilbert_dim_exact",
        "code_dim_exact",
        "boundary_rank_degree_one_exact",
        "h0_dim_exact",
        "q_square_certificate",
        "anticommutator_certificate",
        "degree_zero_homology_matches_code",
    ), ",")

    with_csv(path, header;
             sentinel="Algebraic summary/check record only: no full physical or ghost Hilbert matrices are built.") do io
        println(io, join((
            summary.k,
            summary.nqubits,
            summary.nchecks,
            summary.max_check_weight,
            summary.all_projectors_commute,
            summary.all_checks_square_to_identity,
            summary.stabilizer_rank,
            summary.independent_check_relations,
            summary.logical_qubits,
            summary.physical_hilbert_dim_exact,
            summary.code_dim_exact,
            summary.boundary_rank_degree_one_exact,
            summary.h0_dim_exact,
            summary.q_square_certificate,
            summary.anticommutator_certificate,
            summary.degree_zero_homology_matches_code,
        ), ","))
    end
    println("wrote ", path)
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
