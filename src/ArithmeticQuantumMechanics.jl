module ArithmeticQuantumMechanics

export project_root, run_bundle_path

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
