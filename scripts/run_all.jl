# Canonical local driver for evidence producers.
#
# Usage:
#   julia --project=. scripts/run_all.jl
#   julia --project=. scripts/run_all.jl --fast

using Printf

const SCRIPTS_DIR = @__DIR__

# Entries are NamedTuples:
#   topic  - display group
#   label  - display name
#   path   - path relative to scripts/
#   tool   - :julia, :sage, :gap, or :shell
#   fast   - include in --fast mode?
#   entry  - optional Julia function to call after include, default :main
const ALL_ENTRIES = [
    (
        topic = "lattice codes",
        label = "toric_supercharge_validation",
        path = "lattice_codes/toric_supercharge_validation.jl",
        tool = :julia,
        fast = true,
    ),
]

struct RunResult
    topic::String
    label::String
    status::Symbol
    elapsed::Float64
    notes::String
end

entry_get(entry, key::Symbol, default) = haskey(entry, key) ? getfield(entry, key) : default

function executable_available(exe::String)::Bool
    try
        run(pipeline(`which $exe`, stdout=devnull, stderr=devnull))
        return true
    catch
        return false
    end
end

function run_julia_script(path::String, entry::Symbol)::Tuple{Symbol,Float64,String}
    abs_path = joinpath(SCRIPTS_DIR, path)
    isfile(abs_path) || return (:failed, 0.0, "file not found: $abs_path")

    mod = Module()
    elapsed = 0.0
    try
        elapsed = @elapsed begin
            Base.include(mod, abs_path)
            isdefined(mod, entry) || error("entry function $(entry) not defined in $path")
            func = Base.invokelatest(getproperty, mod, entry)
            Base.invokelatest(func)
        end
        return (:ok, elapsed, "")
    catch e
        msg = sprint(showerror, e)
        length(msg) > 200 && (msg = msg[1:200] * "...")
        return (:failed, elapsed, msg)
    end
end

function run_external(path::String, tool::Symbol)::Tuple{Symbol,Float64,String}
    abs_path = joinpath(SCRIPTS_DIR, path)
    isfile(abs_path) || return (:failed, 0.0, "file not found: $abs_path")

    cmd = if tool == :sage
        executable_available("sage") || return (:skipped, 0.0, "sage not found on PATH")
        `sage $abs_path`
    elseif tool == :gap
        executable_available("gap") || return (:skipped, 0.0, "gap not found on PATH")
        `gap -q $abs_path`
    elseif tool == :shell
        `bash $abs_path`
    else
        return (:failed, 0.0, "unsupported tool: $(tool)")
    end

    elapsed = 0.0
    try
        elapsed = @elapsed run(cmd)
        return (:ok, elapsed, "")
    catch e
        msg = sprint(showerror, e)
        length(msg) > 200 && (msg = msg[1:200] * "...")
        return (:failed, elapsed, msg)
    end
end

function run_entry(entry)::RunResult
    tool = entry_get(entry, :tool, :julia)
    path = String(entry.path)
    label = String(entry.label)
    topic = String(entry.topic)
    entryfn = entry_get(entry, :entry, :main)

    if tool == :julia
        status, elapsed, notes = run_julia_script(path, entryfn)
    else
        status, elapsed, notes = run_external(path, tool)
    end

    return RunResult(topic, label, status, elapsed, notes)
end

function print_summary(results::Vector{RunResult})
    if isempty(results)
        println("run_all.jl: no registered entries")
        return
    end

    w_topic = max(length("Topic"), maximum(length(r.topic) for r in results))
    w_label = max(length("Script"), maximum(length(r.label) for r in results))
    w_notes = 50

    sep = "+" * "-"^(w_topic + 2) * "+" * "-"^(w_label + 2) *
          "+---------+-----------+" * "-"^(w_notes + 2) * "+"

    println()
    println(sep)
    println("| " * rpad("Topic", w_topic) * " | " *
            rpad("Script", w_label) * " | Status  | Seconds   | " *
            rpad("Notes", w_notes) * " |")
    println(sep)

    for r in results
        sec = r.status == :skipped ? "        -" : @sprintf("%8.3f", r.elapsed)
        notes = length(r.notes) > w_notes ? r.notes[1:w_notes - 1] * "..." : r.notes
        println("| " * rpad(r.topic, w_topic) * " | " *
                rpad(r.label, w_label) * " | " *
                rpad(string(r.status), 7) * " | " *
                sec * " | " *
                rpad(notes, w_notes) * " |")
    end
    println(sep)

    n_ok = count(r -> r.status == :ok, results)
    n_failed = count(r -> r.status == :failed, results)
    n_skipped = count(r -> r.status == :skipped, results)
    @printf("Total: %d ok  %d failed  %d skipped\n", n_ok, n_failed, n_skipped)
end

function main(args::Vector{String}=ARGS)
    fast_mode = "--fast" in args
    entries = fast_mode ? filter(e -> entry_get(e, :fast, false), ALL_ENTRIES) : ALL_ENTRIES

    println(fast_mode ? "run_all.jl: --fast mode" : "run_all.jl: full mode")
    println("Project root: ", abspath(joinpath(SCRIPTS_DIR, "..")))

    results = RunResult[]
    for entry in entries
        print("  [$(entry.topic)] $(entry.label) ... ")
        flush(stdout)
        result = run_entry(entry)
        if result.status == :ok
            @printf("ok (%.2f s)\n", result.elapsed)
        elseif result.status == :skipped
            println("skipped ($(result.notes))")
        else
            println("FAILED")
            println("    ", result.notes)
        end
        push!(results, result)
    end

    print_summary(results)
    any(r -> r.status == :failed, results) && exit(1)
end

if abspath(PROGRAM_FILE) == @__FILE__
    main(ARGS)
end
