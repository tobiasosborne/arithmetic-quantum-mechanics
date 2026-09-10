# PATCH — coordinator integration anchors

This lane recommends admissions but makes no trunk/status edit.

1. Copy `ADJUDICATION.md` to
   `theory/verdicts/phantasm-relations-adjudication.md`.
2. In `claims/CLAIMS.md`, anchor on the rows beginning
   ``| `SP-LREL` |``, ``| `SP-COMPACT` |`` and
   ``| `SP-STAB-REL` |``. Change each status from `SKETCH` to `PROVED`, keep
   the final canonical proof paths, and identify this adjudication as the
   admission record.
3. In `claims/PHANTASM-DAG.md`, anchor on `## SP-LREL`, `## SP-COMPACT` and
   `## SP-STAB-REL`. For each section set `Status: PROVED`, replace `Remaining`
   by `None within the admitted statement` followed by its retained boundary,
   set `Review` to
   `theory/verdicts/phantasm-relations-adjudication.md`, and set
   `Evidence: admitted`. Keep the existing final proof/checker paths.
4. In the matching labbook propositions, change `\statusSketch{}` to
   `\statusProved{}` and replace `repair/adjudication pending` in provenance
   with the final adjudication reference. Preserve the exact scopes.
5. Update the categorical-structure record and HANDOFF only to reflect these
   three admissions and the next bounded task. Do not infer scalar
   normalization, CP semantics or source exhaustion.
6. Run the Phantasm contract check, labbook lockstep/build, all checker greens
   and advertised reds, then the full session-close gate. This adjudication
   records only the already completed targeted 14/18 mutation verification;
   it does not pre-certify the repository-wide run.
