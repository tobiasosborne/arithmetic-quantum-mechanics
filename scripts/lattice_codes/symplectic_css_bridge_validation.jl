using ArithmeticQuantumMechanics

Base.include(@__MODULE__, joinpath(@__DIR__, "..", "_common.jl"))

const RUN = "2026-05-24-symplectic-css-bridge"

function main()
    path = data_path(RUN, "symplectic_css_bridge_summary.csv")
    header = join((
        "k",
        "p",
        "nvertices",
        "nedges",
        "nfaces",
        "boundary_square_zero",
        "css_isotropic",
        "rank_boundary_one",
        "rank_boundary_two",
        "h1_dim",
        "symplectic_stabilizer_rank",
        "encoded_qudits",
        "encoded_hilbert_dimension_exact",
        "chain_count_matches_symplectic_count",
    ), ",")

    with_csv(path, header;
             sentinel="Exact prime-field certificate for the chain/CSS/symplectic bridge; no Hilbert matrices are built.") do io
        for p in (2, 3, 5)
            summary = symplectic_css_bridge_summary(4, p)
            println(io, join((
                summary.k,
                summary.p,
                summary.nvertices,
                summary.nedges,
                summary.nfaces,
                summary.boundary_square_zero,
                summary.css_isotropic,
                summary.rank_boundary_one,
                summary.rank_boundary_two,
                summary.h1_dim,
                summary.symplectic_stabilizer_rank,
                summary.encoded_qudits,
                summary.encoded_hilbert_dimension_exact,
                summary.chain_count_matches_symplectic_count,
            ), ","))
        end
    end
    println("wrote ", path)
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
