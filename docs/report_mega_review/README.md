# Report Mega Review

Status: active orchestration workspace.

Scope: adversarial review of the sharded report rooted at `report.tex`.
Excluded scope: finite-ring-database implementation work. Reviewers may flag
report claims that depend on finite-ring-database status, but must not review
the database code path as the main object.

Hard command rule for all reviewers:

- Do not run Julia.
- Do not run `julia`, `make test`, `scripts/run_all.jl`, or any producer
  script.
- Use read-only text inspection only, such as `rg`, `sed`, `nl`, `wc`, and
  `git show`.

Central write policy:

- Wave 1 reviewers write only their assigned file under `wave1/`.
- Wave 2 reviewers write only their assigned file under `wave2/`.
- The final reviewer writes only under `final/`.
- No reviewer edits report shards, source manifests, generated data, or another
  reviewer's output file.

Review standard:

- Be skeptical and adversarial.
- Prefer concrete findings with file and line references.
- Look for unsupported claims, convention drift, notation shifts, hidden
  hypotheses, false equivalences, unregistered sources, run/schema/report
  mismatches, counterexamples, and places where a proposal is phrased as a
  result.
- Separate definite defects from questions and possible risks.
- Do not claim an error without enough local evidence to locate it.

Planned waves:

1. Wave 1: 46 narrow reviewers, each assigned two adjacent shards.
2. Wave 2: 4 synthesis reviewers over larger arcs, using wave 1 outputs and
   cross-reading relevant shards.
3. Final wave: one action-document reviewer assembling prioritized findings.

