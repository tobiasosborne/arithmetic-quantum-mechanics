# Shared helpers for evidence-producing Julia scripts.

const PROJECT_ROOT = normpath(joinpath(@__DIR__, ".."))

"""
    current_run_dir(run)

Return the absolute path `runs/<run>`. Does not create it.
"""
current_run_dir(run::AbstractString) = joinpath(PROJECT_ROOT, "runs", run)

"""
    require_run_bundle(run)

Fail unless `runs/<run>/README.md` already exists. Producers should create run
bundles before writing data.
"""
function require_run_bundle(run::AbstractString)
    dir = current_run_dir(run)
    readme = joinpath(dir, "README.md")
    if !isdir(dir) || !isfile(readme)
        error("missing run bundle README: $(readme)")
    end
    return dir
end

"""
    data_path(run, name)

Return `runs/<run>/data/<name>` and create the data directory after verifying
that the run bundle exists.
"""
function data_path(run::AbstractString, name::AbstractString)
    dir = joinpath(require_run_bundle(run), "data")
    mkpath(dir)
    return joinpath(dir, name)
end

"""
    figure_path(run, name)

Return `runs/<run>/figures/<name>` and create the figures directory after
verifying that the run bundle exists.
"""
function figure_path(run::AbstractString, name::AbstractString)
    dir = joinpath(require_run_bundle(run), "figures")
    mkpath(dir)
    return joinpath(dir, name)
end

"""
    with_csv(f, path, header; sentinel=nothing)

Open `path`, optionally write a `#` sentinel comment, write `header`, call
`f(io)`, and close the file.
"""
function with_csv(f, path::AbstractString, header::AbstractString;
                  sentinel::Union{AbstractString,Nothing}=nothing)
    open(path, "w") do io
        if sentinel !== nothing
            println(io, "# ", sentinel)
        end
        println(io, header)
        f(io)
    end
end

const _SESSION_START = Ref{Float64}(0.0)
const _SESSION_STARTED = Ref{Bool}(false)

"""
    log_progress(prefix, idx, n)

Print a one-line progress message with elapsed wall time.
"""
function log_progress(prefix::AbstractString, idx::Integer, n::Integer)
    if !_SESSION_STARTED[]
        _SESSION_START[] = time()
        _SESSION_STARTED[] = true
    end
    elapsed = time() - _SESSION_START[]
    println(stderr, "[$prefix] $idx/$n (elapsed: $(round(elapsed; digits=2)) s)")
end
