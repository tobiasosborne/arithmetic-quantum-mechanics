using ArithmeticQuantumMechanics

Base.include(@__MODULE__, joinpath(@__DIR__, "..", "_common.jl"))

const RUN = "2026-05-24-steane-clifford-koszul-morphisms"

function write_summary()
    path = data_path(RUN, "steane_clifford_koszul_summary.csv")
    header = join((
        "n",
        "stabilizer_generators",
        "hadamard_maps_l_to_l",
        "hadamard_image_rank",
        "hadamard_generator_permutation",
        "hadamard_exact_same_q_after_ghost_swap",
        "hadamard_logical_x_image",
        "hadamard_logical_z_image",
        "hadamard_code_action",
        "phase_maps_l_to_l",
        "phase_image_rank",
        "phase_generator_basis_change",
        "phase_chain_isomorphism_to_image_presentation",
        "phase_same_q_only_after_homotopy_retract",
        "phase_logical_x_image",
        "phase_logical_z_image",
        "nonzero_syndrome_blocks",
        "nonzero_syndrome_blocks_contractible",
        "zero_syndrome_cohomology_dim_by_degree",
        "physical_h0_dim",
        "full_cohomology_dim",
    ), ",")
    summary = steane_clifford_morphism_summary()
    with_csv(path, header;
             sentinel="Steane Clifford/Koszul morphism summary/check record for transversal H and P.") do io
        println(io, join((
            summary.n,
            summary.stabilizer_generators,
            summary.hadamard_maps_l_to_l,
            summary.hadamard_image_rank,
            summary.hadamard_generator_permutation,
            summary.hadamard_exact_same_q_after_ghost_swap,
            summary.hadamard_logical_x_image,
            summary.hadamard_logical_z_image,
            summary.hadamard_code_action,
            summary.phase_maps_l_to_l,
            summary.phase_image_rank,
            summary.phase_generator_basis_change,
            summary.phase_chain_isomorphism_to_image_presentation,
            summary.phase_same_q_only_after_homotopy_retract,
            summary.phase_logical_x_image,
            summary.phase_logical_z_image,
            summary.nonzero_syndrome_blocks,
            summary.nonzero_syndrome_blocks_contractible,
            summary.zero_syndrome_cohomology_dim_by_degree,
            summary.physical_h0_dim,
            summary.full_cohomology_dim,
        ), ","))
    end
    return path
end

function write_maps()
    path = data_path(RUN, "steane_clifford_generator_maps.csv")
    header = "morphism,source,image,image_basis_coordinates"
    with_csv(path, header;
             sentinel="Images of the six Steane stabilizer labels under transversal Clifford H and P.") do io
        for row in steane_clifford_morphism_rows()
            println(io, join((row.morphism, row.source, row.image, row.image_basis_coordinates), ","))
        end
    end
    return path
end

function main()
    for path in (write_summary(), write_maps())
        println("wrote ", path)
    end
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
