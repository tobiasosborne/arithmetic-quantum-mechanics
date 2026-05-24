# INDEX.md - Script, Output, And Report Manifest

This manifest indexes the evidence layer behind the sharded lab book rooted at
`report.tex`. The repository is currently an infrastructure scaffold; no
evidence-producing scripts or run bundles are registered yet.

## Run Bundles

Generated data and figures will live under
`runs/<YYYY-MM-DD>-<slug>/{data,figures}/`. Each run must include a
`README.md` with hypothesis, exact command, headline finding, and next steps.

| Run | Topic | What it covers |
|---|---|---|
| `runs/2026-05-24-toric-supercharge/` | Toric code / local-check ghosts | Algebraic validation of the auxiliary-fermion supercharge construction for a `k=4` toric-code instance. |

## Quick Start

```bash
make check-report-shards
make report
julia --project=. -e 'using Pkg; Pkg.test()'
julia --project=. scripts/run_all.jl --fast
```

## Script To Output Manifest

One row per script that writes files. Add rows in the same change that adds a
producer.

| Script | Tool | Run bundle | CSV outputs | Figures | Report shard |
|---|---|---|---|---|---|
| `scripts/lattice_codes/toric_supercharge_validation.jl` | Julia | `runs/2026-05-24-toric-supercharge/` | `data/toric_supercharge_summary.csv` | _none_ | `AQM-05-TORIC-SUPERCHARGE` |

## CSV Reverse Lookup

Every CSV must be listed here and in `data/SCHEMA.md`.

| CSV path | Producing script | Schema section |
|---|---|---|
| `runs/2026-05-24-toric-supercharge/data/toric_supercharge_summary.csv` | `scripts/lattice_codes/toric_supercharge_validation.jl` | `toric_supercharge_summary.csv` |

## Report Shards

| Label | Source | Title |
|---|---|---|
| `AQM-00-FRONTMATTER` | `report/sections/00_frontmatter_status.tex` | Frontmatter, Status, and Scope |
| `AQM-01-PROGRAMME-MAP` | `report/sections/01_programme_map.tex` | Programme Map |
| `AQM-02-LAB-LOG` | `report/sections/02_lab_log.tex` | Lab Log |
| `AQM-03-REPRO-MAP` | `report/sections/03_reproducibility_map.tex` | Reproducibility Map |
| `AQM-04-SOURCES-QUESTIONS` | `report/sections/04_source_queue_open_questions.tex` | Source Queue and Open Questions |
| `AQM-05-TORIC-SUPERCHARGE` | `report/sections/05_toric_supercharge_checks.tex` | Toric Code Supercharge From Local Checks |

## Source Topics

Source manifests should be created under `references/<topic>/SOURCES.md`.

| Topic | Manifest | Status |
|---|---|---|
| Weil conjectures and zeta functions | _pending_ | No sources acquired. |
| Arithmetic quantum mechanics | _pending_ | No sources acquired. |
| Supersymmetric quantum mechanics | _pending_ | No sources acquired. |
| Toric codes and Levin-Wen models | `references/toric_code/SOURCES.md` | Kitaev arXiv source bundle acquired for the toric-code stabilizer convention. |
