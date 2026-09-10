# SUMMARY — exact SP-SUM falsifier lane

Model: `gpt-5.6-sol`, reasoning setting `xhigh`.

The lane supplies a standalone exact `phantasm_sum_check.py` proposal.
`EXPECTATIONS.md` was frozen and reported before implementation.  No SP-SUM
prover artifact was read and no proof, trunk, status or git change was made.

U1 constructs all 169 actual preparation/adjoint matrix-unit words over F3
for source and target ranks zero, one and two.  Explicit rectangular shapes
and exact Gaussian rank show that every `3^m x 3^n` Hom-space is spanned,
including rank-zero `C`.  U2 uses the installed exact qutrit amplitude census
to check that `diag(1,1,0)=E00+E11` belongs to the coherent span but not the
360 nonzero pure stabilizer classes.

U3 realizes block arrows by D1707's tuple action and checks dense action,
composition and adjoint transpose with repeated qutrit positions and a
coherent cross-block map.  U4 derives the coherent/tagged dimensions
`16/10`, `25/11`, `36/18`, and `81/81` by ranks of enumerated coordinate
families.  Repeated equal blocks remain different positions.

U5 represents `4x0`, `0x4`, and `0x0` matrices with explicit shapes, checks
their unique block-arrow realizations, dagger and composition, and separates
the empty-list zero Hilbert space from the singleton rank-zero model `C`.
No channel is assigned to the empty list.

U6--U8 check D1707's `P_i^X` dephasing on all sixteen `4x4` matrix units:
ten fixed diagonal-block units, six killed off-diagonal units, complete
projection Kraus data, unitality, idempotence, rank-ten tagged range and
ordinary trace.  The identity distinguishes normalized block trace two from
ordinary trace four.

After the sole checker repair, all ten advertised actual-data mutations exit
`1` at their intended U1--U8 gates.  U2 now guards the imported
216-Clifford/144-rank-one/360-distinct-endomorphism census before separately
excluding `diag(1,1,0)`; truncating the actual census reaches U2a.  U7 passes
its shortened projection family through completeness and every actual
dephasing call.  With only U7a disabled, projection loss proceeds to U7b
unitality.  Temporarily disabling only U2a made the truncated-census mutation
survive with exit `0`; restoration returned exit `1`.  Bad
usage exits `2`; ordinary and optimized greens pass in about four seconds.

`REPAIR.md` records the bounded two-finding checker disposition.

The checker imports only the installed exact qutrit census for its optional U2
witness; dependency hashes are in `RUNS.md`.  Finite success does not prove
SP-SUM, preserve a Gaussian fragment, create a classical rig/biproduct, or
assert arithmetic-source exhaustion.  `PATCH.md` gives anchored integration
steps while retaining `SKETCH`.
