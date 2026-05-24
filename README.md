# arithmetic-quantum-mechanics

Lab-book workspace for investigating bridges between Weil conjectures and zeta
functions, arithmetic quantum mechanics, supersymmetric quantum mechanics, and
Kitaev/Levin-Wen/toric-code style topological lattice models.

Status: active research notebook. The repository contains the report scaffold,
provenance rules, run-bundle discipline, tool runner, checked toric/CSS/Steane
stabilizer-supercharge results, a first arithmetic-quantum-field proposal, and
projective sheaf-field examples.

## Layout

- `report.tex` - sharded LaTeX lab-book master.
- `report/sections/*.tex` - body shards.
- `report/README.md` - report source map.
- `report/SHARD_CATALOG.md` - stable shard labels and search keywords.
- `AGENTS.md` - scientific-practice rules for agents.
- `CONVENTIONS.md` - notational, modelling, and data-layout conventions.
- `INDEX.md` - script to output to report manifest.
- `scripts/` - reproducibility scripts and the canonical driver.
- `runs/<YYYY-MM-DD>-<slug>/` - generated data and figures grouped by run.
- `data/SCHEMA.md` - CSV column contracts.
- `references/` - local source manifests and append-only source files.
- `docs/NUMERICAL_NOTES.md` and `HANDOFF.md` - session-facing state.

## Commands

```bash
# Check sharded report structure.
make check-report-shards

# Build report.pdf from report.tex.
make report

# Run the Julia package smoke tests.
julia --project=. -e 'using Pkg; Pkg.test()'

# Run registered evidence producers.
julia --project=. scripts/run_all.jl --fast

# Show locally available optional tools.
make tool-versions
```

Julia and LaTeX are useful immediately. Sage and GAP are expected optional
tools for later exact arithmetic and group/category computations; scripts that
depend on them should fail closed or skip explicitly when the executable is not
available.

## Scientific Practice

No mathematical or physical claim should be added from memory. Acquire or cite
a local source, record the convention in `CONVENTIONS.md`, and connect any
computed result to a script, run bundle, schema row, and report shard.
