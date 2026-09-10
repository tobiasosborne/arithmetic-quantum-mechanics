# SUMMARY — exact process falsifier lane

Model: `gpt-5.6-sol`, reasoning setting `xhigh`.

The lane supplies the standalone exact `phantasm_process_check.py` proposal
for SP-SCALAR and SP-CP.  `EXPECTATIONS.md` was frozen and reported before
implementation.  No process prover artifact was read and no proof, trunk,
status or git change was made.

All matrices and probabilities lie in exact `Q(i)` using `Fraction` pairs.
The production Kraus map uses dense matrix multiplication.  A separate
coefficient-level route evaluates every matrix unit.  Choi matrices are
reconstructed from actual map outputs and tested by Hermiticity and every
exact principal minor, so positivity is not accepted by repeating the Kraus
Gram construction.

P1--P2 check scalar modulus, phase invariance, the distinction between
projective representatives and CP maps, contraction iff on 28 rank-one
inputs, and explicit rejection of zero conditioning.  P3--P6 check typed
rectangular block Kraus data, four independent Choi PSD controls, per-input
completeness, ordinary rather than normalized block trace, nonunique Kraus
lists, composite hidden paths and full tensor matrix-unit action.

P7--P9 check outcome-first retained blocks, no outcome-count trace factor,
earlier/later sequential pairs and listed-factor tensor pairs.  P10 checks 25
rectangular Hilbert--Schmidt adjoint pairings with a nonreal Kraus phase,
adjoint CP/subunitality, channel unitality, and the unital but non-TNI adjoint
of discard.  P11 checks D1327-style basis preparation/discard, retained tags
and the finer D1325 source equality.

After the sole checker repair, all nineteen advertised actual-data mutations
exit `1` at their registered P1--P11 gates.  P3 now has a forward-typed
transpose defect reaching coefficient comparison at `x1:E_(0,1)` and an
actual `2I_2` overcomplete Kraus defect that passes coefficient/Choi checks
before failing completeness.  The zero-conditioning mutation reaches an explicit gate, and
rectangular swapped-adjoint mutations reach typed mathematical mismatches.
Temporarily disabling only the zero-conditioning acceptance comparison made
that red survive with exit `0`; restoration returned exit `1`.  Bad usage
exits `2`; ordinary and optimized greens pass in about one second.

Temporarily disabling only the late P3 completeness comparison made the
overcomplete mutation survive with exit `0`; restoration returned exit `1`.
`REPAIR.md` records the bounded OBJ3 disposition.

The first green attempt exposed and blocked an accumulation error in the
independent coefficient oracle; its exact `x0:E_(0,0)` witness and repair are
recorded in `RUNS.md`.  No production Kraus code changed in that correction.

Finite success cannot prove arbitrary-dimensional CP/Kraus exhaustion,
canonical representative scaling, normalized stabilizer semantics or
arithmetic-source exhaustion.  `PATCH.md` gives anchored integration steps
while retaining both claims at `SKETCH`.
