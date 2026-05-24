module ArithmeticQuantumMechanics

export project_root, run_bundle_path
export horizontal_edge_index, vertical_edge_index, star_edges, plaquette_edges
export PauliCheck, toric_code_checks, toric_code_stabilizers
export toric_code_check_projectors, symplectic_commutes, gf2_rank
export toric_boundary_one_rows, toric_boundary_two_columns
export toric_code_stabilizer_rank, toric_boundary_square_zero
export toric_cellular_supercharge_square_zero
export toric_supercharge_summary, toric_chain_ghost_unification_summary
export oriented_toric_boundary_matrices, matmul_modp, rank_modp
export css_symplectic_isotropic, symplectic_css_bridge_summary
export css_supercharge_dictionary_summary, steane_css_matrices
export qutrit_css_toy_matrices

include("ArithmeticQuantumMechanics/ToricCodeSupercharge.jl")
include("ArithmeticQuantumMechanics/SymplecticCssBridge.jl")

"""
    project_root()

Return the absolute path to the repository root for this checkout.
"""
project_root() = normpath(joinpath(@__DIR__, ".."))

"""
    run_bundle_path(run)

Return the absolute path to `runs/<run>` without creating it.
"""
run_bundle_path(run::AbstractString) = joinpath(project_root(), "runs", run)

end
