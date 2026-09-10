# PATCH — coordinator integration anchors

This lane makes no trunk edit.

1. Copy `ADJUDICATION.md` to
   `theory/verdicts/phantasm-processes-adjudication.md`.
2. In `claims/CLAIMS.md`, anchor on the rows beginning
   ``| `SP-SCALAR` |`` and ``| `SP-CP` |``. Change `SKETCH` to `PROVED`, keep
   the repaired statements and canonical proof/checker paths, and identify the
   process adjudication as the admission record.
3. In `claims/PHANTASM-DAG.md`, anchor on `## SP-SCALAR` and `## SP-CP`.
   Set `Status: PROVED`, `Evidence: admitted`, and `Review` to
   `theory/verdicts/phantasm-processes-adjudication.md`. Replace `Remaining`
   with `None within the admitted statement` plus the retained normalization
   and source-exhaustion boundaries. Preserve proof/check paths.
4. In the two owning labbook propositions, change `\statusSketch{}` to
   `\statusProved{}` and replace pending provenance with the adjudication.
   Preserve the repaired scalar wording and general trace-adjoint paragraph.
5. Update categorical structure and HANDOFF with only these admissions and
   the next bounded SP-SUM task.
6. Run the post-promotion 22-mode contract check, PDF build, lockstep gate and
   full current session-close suite. The adjudication records completed
   targeted 19-mode checker verification, not those final repository gates.
