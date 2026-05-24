# Report Source Map

Read this file first when navigating the lab-book source. The compiled report
is rooted at `report.tex`, but that file should remain the preamble and include
order only. Body prose lives in `report/sections/*.tex`.

For rapid lookup, use `report/SHARD_CATALOG.md`. It assigns each shard a stable
label, gives 2-3 summary lines, and lists search keywords. The same metadata
appears in a TeX comment header at the top of every shard.

The target shard size is about 200 lines. The local guard allows larger
topic-preserving shards up to `REPORT_SHARD_MAX_LINES` (default 280 lines).
Run `make check-report-shards` after editing report structure and `make report`
before treating report edits as complete.

## Shard Order

| Order | Label | Source | Title |
|---:|---|---|---|
| 0 | `AQM-00-FRONTMATTER` | `report/sections/00_frontmatter_status.tex` | Frontmatter, Status, and Scope |
| 1 | `AQM-01-PROGRAMME-MAP` | `report/sections/01_programme_map.tex` | Programme Map |
| 2 | `AQM-02-LAB-LOG` | `report/sections/02_lab_log.tex` | Lab Log |
| 3 | `AQM-03-REPRO-MAP` | `report/sections/03_reproducibility_map.tex` | Reproducibility Map |
| 4 | `AQM-04-SOURCES-QUESTIONS` | `report/sections/04_source_queue_open_questions.tex` | Source Queue and Open Questions |
| 5 | `AQM-05-TORIC-SUPERCHARGE` | `report/sections/05_toric_supercharge_checks.tex` | Toric Code Supercharge From Local Checks |
| 6 | `AQM-06-TORIC-CHAIN-GHOST-PROOF` | `report/sections/06_toric_chain_ghost_proof.tex` | Proof of the Toric Chain-to-Ghost Lift |

## Maintenance Rules

- Add new body prose under `report/sections/`, not directly in `report.tex`.
- Keep `report.tex` to preamble, global macros/styles, ordered `\include`
  statements, bibliography, and `\end{document}`.
- Cite shards by stable label. Keep labels stable across ordinary edits.
- Every shard must start with `SHARD-ID`, `SHARD-TITLE`, two or three
  `SHARD-SUMMARY` lines, and `SHARD-KEYWORDS`.
- When adding, removing, renaming, or reordering shards, update this map,
  update `report/SHARD_CATALOG.md`, and run `make check-report-shards`.
- The rebuilt `report.pdf` and LaTeX build products are generated artifacts.
