# Project Instructions for AI Agents

`AGENTS.md` is the authoritative instruction file for this repository. Read it
first at the start of every session and after any context compression.

This repository is a reproducible mathematical research workspace. The main
artifact is the sharded LaTeX lab book rooted at `report.tex`; body prose lives
in `report/sections/*.tex`.

## Build And Test

```bash
make check-report-shards
make report
julia --project=. -e 'using Pkg; Pkg.test()'
julia --project=. scripts/run_all.jl --fast
```

`make ci-before-push` runs the local quality gate. It skips git-only checks
when the directory is not a git repository.

## Beads

If `.beads/` exists, use `bd` for persistent work tracking:

```bash
bd ready
bd show <id>
bd update <id> --claim
bd close <id>
```

Do not run `bd init` or `bd init --force` unless the user explicitly asks.
