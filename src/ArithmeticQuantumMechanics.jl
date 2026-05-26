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
export steane_molecular_summary, steane_binary_space_rows
export steane_cohomology_by_degree
export steane_clifford_morphism_summary, steane_clifford_morphism_rows
export steane_all_clifford_generator_summary, steane_all_clifford_generator_rows
export steane_ghost_gaussian_elementary_rows
export arithmetic_quantum_field_examples, arithmetic_quantum_field_summary_rows
export arithmetic_quantum_field_basis_rows
export p1_rational_point_labels, p1_od_basis_labels, p1_od_evaluation_matrix
export projective_line_sheaf_field_examples
export projective_line_sheaf_field_summary_rows
export projective_line_sheaf_field_basis_rows
export projective_line_stalk_rows
export finite_ring_database_source_preflight
export finite_ring_database_tool_preflight
export finite_ring_database_preflight
export finite_ring_database_schema_version
export finite_ring_database_prd_table_names
export finite_ring_database_schema_sql
export migrate_finite_ring_database_schema!

include("ArithmeticQuantumMechanics/ToricCodeSupercharge.jl")
include("ArithmeticQuantumMechanics/SymplecticCssBridge.jl")
include("ArithmeticQuantumMechanics/SteaneSupercharge.jl")
include("ArithmeticQuantumMechanics/SteaneCliffordGroup.jl")
include("ArithmeticQuantumMechanics/ArithmeticQuantumFields.jl")
include("ArithmeticQuantumMechanics/ProjectiveLineSheafFields.jl")

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

include("ArithmeticQuantumMechanics/FiniteRingDatabasePreflight.jl")
include("ArithmeticQuantumMechanics/FiniteRingDatabaseSchema.jl")

end
