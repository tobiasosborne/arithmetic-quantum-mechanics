module ArithmeticQuantumMechanics

export project_root, run_bundle_path
export horizontal_edge_index, vertical_edge_index, star_edges, plaquette_edges
export PauliCheck, toric_code_checks, toric_code_stabilizers
export toric_code_check_projectors, symplectic_commutes, gf2_rank
export toric_code_stabilizer_rank
export toric_supercharge_summary

include("ArithmeticQuantumMechanics/ToricCodeSupercharge.jl")

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
