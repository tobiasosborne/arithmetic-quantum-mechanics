using ArithmeticQuantumMechanics

Base.include(@__MODULE__, joinpath(@__DIR__, "..", "_common.jl"))

const RUN = "2026-05-24-css-supercharge-symplectic-dictionary"

function write_row(io, name, summary)
    println(io, join((
        name,
        summary.p,
        summary.n,
        summary.x_rows,
        summary.z_rows,
        summary.rank_x,
        summary.rank_z,
        summary.stabilizer_rank,
        summary.css_isotropic,
        summary.encoded_qudits,
        summary.code_dimension_exact,
        summary.logical_symplectic_dimension,
        summary.l_perp_dimension,
        summary.generator_ghost_count,
        summary.basis_free_projective_ghost_count_exact,
        summary.q_square_certificate,
        summary.anticommutator_certificate,
        summary.h0_matches_stabilizer_code,
    ), ","))
end

function main()
    path = data_path(RUN, "css_supercharge_symplectic_dictionary.csv")
    header = join((
        "example",
        "p",
        "n",
        "x_rows",
        "z_rows",
        "rank_x",
        "rank_z",
        "stabilizer_rank",
        "css_isotropic",
        "encoded_qudits",
        "code_dimension_exact",
        "logical_symplectic_dimension",
        "l_perp_dimension",
        "generator_ghost_count",
        "basis_free_projective_ghost_count_exact",
        "q_square_certificate",
        "anticommutator_certificate",
        "h0_matches_stabilizer_code",
    ), ",")

    with_csv(path, header;
             sentinel="Exact CSS/symplectic/Koszul-supercharge dictionary certificate; no Hilbert matrices are built.") do io
        hx, hz = steane_css_matrices()
        write_row(io, "steane_f2", css_supercharge_dictionary_summary(hx, hz, 2))
        hx3, hz3 = qutrit_css_toy_matrices()
        write_row(io, "qutrit_toy_f3", css_supercharge_dictionary_summary(hx3, hz3, 3))
    end
    println("wrote ", path)
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
