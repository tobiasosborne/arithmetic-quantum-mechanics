# Promotion patch anchors — SP-SUM

These are instructions for root's canonical promotion wave. This lane makes
no trunk or status edit.

1. Install this adjudication as
   `theory/verdicts/phantasm-sum-adjudication.md`, retaining the exact line
   `Admitted: SP-SUM`.

2. In `claims/CLAIMS.md`, anchor the row beginning ``| `SP-SUM` |``:
   change `SKETCH` to `PROVED`, and change the proof annotation from
   `(unreviewed prover pass)` to `(reviewed; SP-SUM adjudication)`. Keep the
   statement, dependencies, proof path, and checker path unchanged.

3. In the claims preamble, anchor `The other seven rows remain SKETCH.`:
   add SP-SUM to the admitted-adjudication sentence and change seven to six.

4. In `claims/PHANTASM-DAG.md`, anchor `## SP-SUM` and update only:
       - Status: PROVED
       - Remaining: None within the admitted statement. The rectangular span,
         strict pure-fragment enlargement, typed block realization,
         coherent/tagged dimensions, and ordinary-trace dephasing passed the
         capped review. Rig and arithmetic-source comparisons remain separate.
       - Review: theory/verdicts/phantasm-sum-adjudication.md
       - Evidence: admitted

   Preserve the corrected Scope/outline and finite falsifier disclaimer.

5. In `labbook/sections/symplectic_phantasm_contracts.tex`, anchor
   `\begin{proposition}[Coherent sums and tagged quantum systems]`: change
   `\statusSketch{}` to `\statusProved{}` and update the SP-SUM provenance to
   the reviewed proof, final exact checker, and adjudication. Do not change the
   proposition, scope, or proof body.

6. In `labbook/sections/symplectic_phantasm.tex`, anchor the synthesis sentence
   `The next bounded work is the coherent-sum and classical-tag comparison`:
   advance it to the arithmetic trace/Frobenius/subsystem interfaces. Anchor
   the nearby multi-claim provenance and record SP-SUM as admitted through its
   adjudication while leaving the remaining claims unpromoted.

7. Run the final 22-contract check once, rebuild the PDF, and run lockstep.
   The completed 31-suite/329-red session-close need not be repeated; combine
   it only as recorded with the separate SP-SUM suite and ten reds.
