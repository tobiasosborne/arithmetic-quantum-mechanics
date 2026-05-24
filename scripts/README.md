# scripts/README.md - Contributor Guide

This directory holds exploration entry points that support the lab book rooted
at `report.tex`. Scripts are evidence producers, not scratch dumps.

Initial topic directories:

```text
scripts/
  arithmetic/      zeta functions, finite fields, trace formulas
  susy/            supersymmetric-QM and index diagnostics
  lattice_codes/   toric-code, quantum-double, Levin-Wen diagnostics
  bridges/         explicit dictionaries or comparison diagnostics
  run_all.jl       canonical local driver
```

Every producer must be listed in `scripts/run_all.jl`, `INDEX.md`, and
`data/SCHEMA.md` if it writes CSV output.

## Adding A Producer

1. Register or cite the local source and convention the script implements.
2. Create the run bundle first:

```text
runs/YYYY-MM-DD-<slug>/
  README.md
  data/
  figures/
```

3. Write the script under the appropriate topic directory.
4. Make the script write only into its run bundle.
5. Add the script to `scripts/run_all.jl`.
6. Add rows to `INDEX.md` and `data/SCHEMA.md`.
7. Add or update the report shard that consumes the result.

## Julia Producer Pattern

```julia
Base.include(@__MODULE__, joinpath(@__DIR__, "..", "_common.jl"))

const RUN = "YYYY-MM-DD-question-slug"

function main()
    path = data_path(RUN, "example_summary.csv")
    with_csv(path, "quantity,value") do io
        println(io, "placeholder,0")
    end
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
```

`data_path` and `figure_path` require `runs/<RUN>/README.md` to exist before
writing. This enforces the run-bundle discipline.

## Optional Tools

Sage and GAP are expected to be useful later. A producer that depends on an
optional executable must check availability before writing data. Missing tools
should be reported as an explicit skip or a hard failure, never as partial
output.

## Checklist

- [ ] Source registered under `references/`.
- [ ] Convention recorded in `CONVENTIONS.md`.
- [ ] Run bundle created before script output.
- [ ] Script listed in `scripts/run_all.jl`.
- [ ] Output documented in `INDEX.md`.
- [ ] CSV columns documented in `data/SCHEMA.md`.
- [ ] Report shard updated or a handoff note records the deferred report work.
