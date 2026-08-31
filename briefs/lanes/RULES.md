# LANE RULES — read fully before your task

You are ONE lane, possibly running in parallel with others in this repo. Race
safety is absolute and mechanical.

- **Write only inside your declared write scope.** Your brief names it. Create
  nothing outside it.
- If your task needs a change to a file outside your scope: **copy it into your
  lane dir, edit the copy, and write `PATCH.md`** listing exact edits keyed by
  **string anchors, never line numbers** — lines drift under concurrent edits.
  The orchestrator applies patches.
- **Never run** `git commit`, `git add`, `git push`, or anything touching
  `.git/`.
- You may READ everything (including `v0.1/`) and RUN computations, writing
  outputs only into your scope.

Process (`PRD.md` governs — read it):

- Read gate: `CLAUDE.md`, `PRD.md`, then the files your brief names.
- **`v0.1/` is a hint, never evidence (L12).** You may read it to find a
  question worth re-asking or a source worth re-fetching. You may not copy a
  statement, a proof, a convention, or a citation from it into the trunk. Every
  admitted statement is re-derived and re-sourced from scratch.
- Rigorous arguments in Lamport structured style (L6b): numbered steps `<1>1`,
  `<1>2`, sub-proofs `<2>*`, explicit ASSUME/PROVE, terminal QED; every leaf
  cites a D-number (`definitions.md`), a claim id (`claims/CLAIMS.md`), a
  registered source (`refs/LEDGER.md`), or a named computation in your scope.
- Notation and definitions are NEVER redefined — cite `notation.md` and
  `definitions.md` (L4). If you need a new one, propose it in `PATCH.md`.
- **No statement from memory (L3).** Standard textbook mathematics included. If
  the source is not local, say so and stop rather than asserting it.
- Any numeric claim: script it, run it, save the output. Checkers must be
  red-capable — demonstrate the mutation that makes them fail (L1).
- **Honest labels.** Never a status stronger than the evidence. A sharp partial,
  or a clean negative naming a forward attack, is a good outcome. Guessing is
  not.
- Write your main output incrementally, section by section. Long monolithic
  outputs get truncated.

Required final artifact: `SUMMARY.md` in your lane dir:

- `STATUS:` one of {DONE, PARTIAL, NEGATIVE, BLOCKED}
- <= 10 lines: what you established, what remains, which files outside your
  scope `PATCH.md` targets (if any).
