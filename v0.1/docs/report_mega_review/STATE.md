# Mega Review State

Objective: orchestrate a full multi-wave adversarial review of the report,
excluding finite-ring-database implementation work.

Current branch state at campaign start: `main` after fast-forward pull to
`5947477`, with report shards `AQM-00` through `AQM-91`.

Hard reviewer rule: no Julia. Reviewers must not run `julia`, `make test`,
`scripts/run_all.jl`, or producer scripts.

Current plan:

1. Create central workspace and assignment files. Status: done.
2. Spawn Wave 1 reviewers in batches. Status: done. Spawned R01-R46.
   Active subagent limit observed: 6 concurrent agents. Continue by waiting
   for completions, closing completed agents, then spawning the next reviewers.
   Completed so far: R01-R46. File-count check: 46 files present.
3. Wait for all Wave 1 review files. Status: done.
4. Spawn 4 Wave 2 synthesis reviewers. Status: done. Spawned S1-S4; outputs
   present in `wave2/`.
5. Spawn final action-document reviewer. Status: done.
6. Parent agent reviews final action document, reports outcome, and leaves
   working-tree status. Status: done.

Wave 1 output target: `docs/report_mega_review/wave1/`.
Wave 2 output target: `docs/report_mega_review/wave2/`.
Final output target: `docs/report_mega_review/final/REPORT_REVIEW_ACTIONS.md`.
