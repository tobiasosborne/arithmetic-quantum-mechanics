Base.include(@__MODULE__, joinpath(@__DIR__, "..", "_common.jl"))

using ArithmeticQuantumMechanics

const RUN = "2026-05-24-steane-all-clifford-ghost-gaussians"

_cell(x) = replace(string(x), "," => ";")

function write_summary()
    summary = steane_all_clifford_generator_summary()
    header = join((
        "n",
        "steane_stabilizer_generators",
        "standard_clifford_generator_gates",
        "hadamard_generator_gates",
        "phase_generator_gates",
        "cnot_generator_gates",
        "generator_image_rows",
        "all_generator_images_rank_six",
        "rank_six_gate_count",
        "all_generator_images_isotropic",
        "isotropic_gate_count",
        "negative_signed_images_from_steane_generators",
        "transported_presentation_chain_map",
        "theorem_extends_to_all_clifford_words_by_generation",
        "signed_pauli_convention",
        "elementary_gl6_ghost_generators",
        "row_swap_ghost_generators",
        "row_shear_ghost_generators",
        "shear_projector_identities_checked",
        "shear_projector_identities_hold",
        "presentation_change_requires_operator_coefficients",
        "zero_syndrome_shear_reduces_to_scalar_exterior_gl",
        "no_bogoliubov_mixing_needed",
    ), ",")
    path = data_path(RUN, "steane_all_clifford_generator_summary.csv")
    with_csv(path, header;
             sentinel="Exact Steane Clifford-generator and ghost-Gaussian certificate; generator checks plus GL6 elementary ghost moves.") do io
        println(io, join(_cell.([
            summary.n,
            summary.steane_stabilizer_generators,
            summary.standard_clifford_generator_gates,
            summary.hadamard_generator_gates,
            summary.phase_generator_gates,
            summary.cnot_generator_gates,
            summary.generator_image_rows,
            summary.all_generator_images_rank_six,
            summary.rank_six_gate_count,
            summary.all_generator_images_isotropic,
            summary.isotropic_gate_count,
            summary.negative_signed_images_from_steane_generators,
            summary.transported_presentation_chain_map,
            summary.theorem_extends_to_all_clifford_words_by_generation,
            summary.signed_pauli_convention,
            summary.elementary_gl6_ghost_generators,
            summary.row_swap_ghost_generators,
            summary.row_shear_ghost_generators,
            summary.shear_projector_identities_checked,
            summary.shear_projector_identities_hold,
            summary.presentation_change_requires_operator_coefficients,
            summary.zero_syndrome_shear_reduces_to_scalar_exterior_gl,
            summary.no_bogoliubov_mixing_needed,
        ]), ","))
    end
    return path
end

function write_generator_images()
    header = join((
        "gate",
        "gate_kind",
        "source",
        "image_sign",
        "image",
        "signed_image",
        "image_list_rank",
        "image_list_isotropic",
    ), ",")
    path = data_path(RUN, "steane_all_clifford_generator_images.csv")
    with_csv(path, header;
             sentinel="Images of the six Steane stabilizer generators under the standard H/P/CNOT Clifford generating gates.") do io
        for row in steane_all_clifford_generator_rows()
            println(io, join(_cell.([
                row.gate,
                row.gate_kind,
                row.source,
                row.image_sign,
                row.image,
                row.signed_image,
                row.image_list_rank,
                row.image_list_isotropic,
            ]), ","))
        end
    end
    return path
end

function write_ghost_gaussians()
    header = join((
        "operation",
        "a",
        "b",
        "generator_change",
        "projector_identity",
        "ghost_gaussian",
        "checked_syndromes",
        "identity_holds",
        "zero_syndrome_map",
    ), ",")
    path = data_path(RUN, "steane_ghost_gaussian_elementaries.csv")
    with_csv(path, header;
             sentinel="Elementary GL6 presentation moves and their number-preserving fermionic Gaussian ghost lifts.") do io
        for row in steane_ghost_gaussian_elementary_rows()
            println(io, join(_cell.([
                row.operation,
                row.a,
                row.b,
                row.generator_change,
                row.projector_identity,
                row.ghost_gaussian,
                row.checked_syndromes,
                row.identity_holds,
                row.zero_syndrome_map,
            ]), ","))
        end
    end
    return path
end

function main()
    for path in (write_summary(), write_generator_images(), write_ghost_gaussians())
        println("wrote ", path)
    end
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
