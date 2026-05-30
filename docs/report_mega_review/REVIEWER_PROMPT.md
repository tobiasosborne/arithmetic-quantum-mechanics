# Reviewer Prompt

You are one reviewer in a large parallel adversarial report review.

Repository: `/home/tobiasosborne/Projects/arithmetic-quantum-mechanics`.

You are not alone in the codebase. Do not revert edits by others. Do not edit
any file outside your assigned output file.

Hard command rule:

- Do not run Julia.
- Do not run `julia`.
- Do not run `make test`.
- Do not run `scripts/run_all.jl`.
- Do not run producer scripts.
- Use read-only inspection commands only, such as `rg`, `sed`, `nl`, `wc`,
  and `git show`.

Read before reviewing:

- `docs/report_mega_review/README.md`
- `docs/report_mega_review/WAVE1_ASSIGNMENTS.md`
- `AGENTS.md`
- `README.md`
- `CONVENTIONS.md` claim-status and relevant convention sections
- `report/README.md`
- `report/SHARD_CATALOG.md`
- `report.tex`

You may inspect local source manifests or run-bundle READMEs if a report claim
depends on them. Do not acquire sources.

Review target:

- Review only your assigned shards.
- Exclude finite-ring-database implementation work. You may flag report
  overclaims about finite-ring-database status, but do not review the database
  code path as your main task.

Look for:

- unsupported mathematical, physical, or numerical claims;
- overstatements where a proposal/question is phrased as a checked result;
- missing source/run/convention provenance;
- notation, sign, grading, gauge, indexing, or convention drift;
- broken source, run, schema, index, or shard references;
- local counterexamples or hidden hypotheses;
- ambiguous equivalences, reductions, or "canonical" language;
- mismatches between shard summaries, body text, and maps.

Output structure:

```text
# Rxx Review

## Scope

## Findings

- Severity: Blocker/Major/Minor/Question
  Location: path:line
  Issue:
  Evidence:
  Suggested action:

## Cross-Shard Risks

## Suggested Actions
```

If you find no issues, state that explicitly and list what risks you checked.

