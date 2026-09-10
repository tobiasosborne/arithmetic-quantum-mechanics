# Reuse/interface repair — 2026-09-10

The fourteen SP contracts and thirteen definitions were reviewed against
existing admitted proofs. No claim status or definition number was added
or promoted. The first Weyl task is now a short finite-abelian corollary
and explicit convention comparison, with its draft in
`theory/symplectic-phantasm/reuse.md`.

- `phantasm_reuse_check.py`: **141,027 exact comparisons** across R1–R6;
  all **11** advertised mutations failed at their intended gates.
  The first observed execution was the rephasing mutation, failing at R2.
- `phantasm_contract_check.py`: green; all **21** mutations failed at
  their intended gates, including inherited proof status, missing reuse,
  definition cycles and selected notation ownership. A mutation that had
  become sensitive to text wrapping was repaired before the final runs.
- Full repository session-close: **27 green suites, 270 red runs**, all
  passed. The final labbook builds at **174 pages**, its revised
  reuse/lemma page was visually inspected, and the lockstep gate passed.
- Earlier canonical claim statements and definition bodies before the
  Phantasm bootstrap are unchanged. The September 9 frozen evidence is
  untouched; this directory is the new record.

`TARGETED.json` contains actual commands, gate outputs and context hashes,
including the imported existing Abelian implementation and finite-field
library. The final prose edit makes the already tested coordinate-product
identity explicit; it does not change the statements or executable inputs.
`SESSION-CLOSE.json` records counts and hashes. Compressed logs preserve the
unmodified transcripts losslessly, and `LOCKSTEP.txt` records the final gate.

The new numerical tests validate finite interfaces, not arbitrary-rank
proofs or category equivalences. The metadata checker is not a mathematical
type checker. All assembled SP rows remain SKETCH; their inherited parents
retain their existing admitted statuses.
