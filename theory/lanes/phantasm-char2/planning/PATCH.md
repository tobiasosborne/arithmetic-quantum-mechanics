# Proposed canonical anchors for DG-CHAR2

No canonical file is changed by this planning lane.

1. In `definitions.md`, after coordinator allocation of unused numbers, add
   the two definitions stated in CANDIDATE.md. Do not alter D1703's odd-
   characteristic half-form definition.
2. In `notation.md`, add distinct symbols for the characteristic-two Weyl
   datum, defect-lift groupoid, `Q_beta`, `Alpha_(g,r)`, and implementer
   extension. Do not reuse D1701's `S_k^aff` or its `(t,g)` notation for the
   un-split carrier (no chosen section).
3. In `claims/CLAIMS.md`, add fully quantified SKETCH rows
   `SP-CHAR2-WEYL` and `SP-CHAR2-LIFT` from CANDIDATE.md. The second depends on
   the first. Do not mark either PROVED during definition registration.
4. In `claims/PHANTASM-DAG.md`, add both claims with proof/review/check paths
   initially `none/planned`. Add F1-FUNCT to DG-CHAR2's explicit reuse and make
   closure require both admitted claims plus the scoped GH08 comparison.
5. In `refs/LEDGER.md`, expand SP-GH08's locators to lines 616--729 and
   747--828 and record the raw-Witt-centre versus phase-quotient distinction.
6. In the labbook, mirror the definitions and SKETCH statements only after
   the canonical rows exist. Record no splitting, global, modular or spectral
   consequence.
7. Future artifact names: `theory/symplectic-phantasm/char2-weyl.md`,
   `char2-lifts.md`, `theory/checks/phantasm_char2_check.py`, and
   `phantasm_char2_EXPECTATIONS.md`.
