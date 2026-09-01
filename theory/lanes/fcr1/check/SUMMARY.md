Lane model: gpt-5.6-sol, reasoning xhigh, codex exec.

# Check-lane summary

Built `fcr_local_check.py`, a standalone exact falsifier for G1--G11 over all
seven registered seeds.  Rings are full element tables; phases are integer
vectors in `Z[zeta_n]` modulo `Phi_n`, `n=3,9,27`; no floats or tolerances.

Built `fcr_local_EXPECTATIONS.md` with first-principles per-gate/per-seed
counts, E3 discrimination notes, complexity justifications, and explicitly
marked discovered G11 data.  Built `fcr_local_RED-MATRIX.md` with distinct
mutation fingerprints, gate reachability, and an E4 internal-decoration audit.

Final observed exits (`python3 -O`, actually run):

- green: `python3 -O fcr_local_check.py` -> **0**
- `--red-nongenerating` -> **1**, killed by G5
- `--red-transpose` -> **1**, killed by G2 at all seven seeds
- `--red-frobenius-blind` -> **1**, killed by G1 (G3 also fires)
- `--red-free-only` -> **1**, killed by G7
- `--red-torsor` -> **1**, killed by G8
- `--red-dim` -> **1**, killed by G5 with a distinct fingerprint
- `--red-halfweyl-drop` -> **1**, killed by G9

Key observed censuses: both order-9 chain rings have 23 submodules and 13
Lagrangians (12 free, one non-free).  The non-Frobenius seed has zero
generating characters; its 26 kernel ideals have sizes `3:24, 9:2`.

Open concern: G6's registered `|I_psi|^2=9` is the commutant/centre inside the
formal twisted algebra.  The non-faithful 9-dimensional matrix image instead
has commutant dimension 3.  The checker tests and reports both arenas; the
prover/orchestrator should state explicitly which one FCR-ALG prose means.

G11 remains census data as required, checked only by identity count, order
divisibility, and profile sum.  G6 and G11 have no registered killing mutation;
the red matrix names concrete mutations that would reach each decoration.
