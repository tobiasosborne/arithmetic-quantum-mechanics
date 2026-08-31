using ArithmeticQuantumMechanics

Base.include(@__MODULE__, joinpath(@__DIR__, "..", "_common.jl"))

const RUN = "2026-05-24-steane-supercharge-molecular"

bitstr(v) = join(string.(Int.(v)))

function write_summary()
    path = data_path(RUN, "steane_molecular_summary.csv")
    header = join((
        "n",
        "check_rank",
        "d_dim",
        "d_size",
        "c_dim",
        "c_size",
        "d_subset_c",
        "logical_word",
        "logical_word_in_c",
        "logical_word_not_in_d",
        "h_h_transpose_zero",
        "stabilizer_rank",
        "l_dim",
        "l_size",
        "l_perp_dim",
        "l_perp_size",
        "logical_symplectic_dim",
        "logical_pauli_classes",
        "logical_pairing_x_z",
        "physical_hilbert_dim",
        "ghost_count",
        "ghost_fock_dim",
        "full_ghost_hilbert_dim",
        "code_dim",
        "encoded_qubits",
        "syndrome_count",
        "nonzero_syndrome_count",
        "syndrome_block_dim",
        "full_q_cohomology_dim",
        "degree_zero_cohomology_dim",
        "q_square_certificate",
        "anticommutator_certificate",
        "codewords_match_two_cosets",
    ), ",")

    summary = steane_molecular_summary()
    with_csv(path, header;
             sentinel="Exact Steane CSS/symplectic/supercharge molecular summary; source convention is Gottesman's seven-qubit CSS table.") do io
        println(io, join((
            summary.n,
            summary.check_rank,
            summary.d_dim,
            summary.d_size,
            summary.c_dim,
            summary.c_size,
            summary.d_subset_c,
            summary.logical_word,
            summary.logical_word_in_c,
            summary.logical_word_not_in_d,
            summary.h_h_transpose_zero,
            summary.stabilizer_rank,
            summary.l_dim,
            summary.l_size,
            summary.l_perp_dim,
            summary.l_perp_size,
            summary.logical_symplectic_dim,
            summary.logical_pauli_classes,
            summary.logical_pairing_x_z,
            summary.physical_hilbert_dim,
            summary.ghost_count,
            summary.ghost_fock_dim,
            summary.full_ghost_hilbert_dim,
            summary.code_dim,
            summary.encoded_qubits,
            summary.syndrome_count,
            summary.nonzero_syndrome_count,
            summary.syndrome_block_dim,
            summary.full_q_cohomology_dim,
            summary.degree_zero_cohomology_dim,
            summary.q_square_certificate,
            summary.anticommutator_certificate,
            summary.codewords_match_two_cosets,
        ), ","))
    end
    return path
end

function write_vectors()
    path = data_path(RUN, "steane_molecular_vectors.csv")
    header = "object,label,x,z"
    data = steane_binary_space_rows()
    h = data.h
    zero = "0000000"
    with_csv(path, header;
             sentinel="Exact binary vectors for the sourced Steane presentation; x,z are Pauli exponent strings.") do io
        for i in axes(h, 1)
            g = bitstr(h[i, :])
            println(io, join(("check_row", "g$(i)", g, ""), ","))
            println(io, join(("l_basis", "X$(i)", g, zero), ","))
            println(io, join(("l_basis", "Z$(i)", zero, g), ","))
        end
        for (i, v) in enumerate(data.d_space)
            println(io, join(("D", "d$(i - 1)", bitstr(v), ""), ","))
        end
        for (i, v) in enumerate(data.u_plus_d)
            println(io, join(("u_plus_D", "coset$(i - 1)", bitstr(v), ""), ","))
        end
        for (i, v) in enumerate(data.c_space)
            println(io, join(("C", "c$(i - 1)", bitstr(v), ""), ","))
        end
        u = bitstr(data.logical_word)
        println(io, join(("l_perp_basis", "Xbar", u, zero), ","))
        println(io, join(("l_perp_basis", "Zbar", zero, u), ","))
        println(io, join(("logical_class", "I", zero, zero), ","))
        println(io, join(("logical_class", "Xbar", u, zero), ","))
        println(io, join(("logical_class", "Zbar", zero, u), ","))
        println(io, join(("logical_class", "Ybar_label", u, u), ","))
    end
    return path
end

function write_cohomology()
    path = data_path(RUN, "steane_cohomology_by_degree.csv")
    header = "degree,ghost_binomial,cohomology_dim"
    with_csv(path, header;
             sentinel="Full Q-cohomology by ghost degree for the six-generator Steane supercharge.") do io
        for row in steane_cohomology_by_degree()
            println(io, join((row.degree, row.ghost_binomial, row.cohomology_dim), ","))
        end
    end
    return path
end

function main()
    for path in (write_summary(), write_vectors(), write_cohomology())
        println("wrote ", path)
    end
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
