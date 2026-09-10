# SUMMARY — exact arithmetic-interface falsifier lane

Model: `gpt-5.6-sol`, reasoning setting `xhigh`.

The lane supplies a standalone exact `phantasm_arithmetic_check.py` proposal
for SP-TRACE, SP-FROB and SP-SUBSYS.  `EXPECTATIONS.md` was frozen and reported
before implementation.  No arithmetic prover artifact was read and no proof,
trunk, status or git change was made.

A1--A4 audit F27/F3 with extension degree equal to characteristic, producing
trace image three, kernel/fibers nine and restricted symplectic Gram ranks
zero, six and twelve.  They separately check the nonstandard F9 character in
F81, direct/iterated F3/F9/F81 traces and character routes, and rank-zero/one/
two half-form products, star, unit and actual sparse traces.  Existing reuse
checker R6 remains unchanged and is credited only for its narrower sample.

A5--A7 check F27 cube/order-three and F81 ninth-power/order-two relative
Frobenius: K-linearity, trace/character invariance, symplectic semilinearity,
648,810 exact rank-one exhaustive/rank-two sparse Weyl covariance tuples,
rank-zero identity, bijectivity, period, inverse channel and ordinary trace.
No dense dimension-729 or dimension-6561 operator matrix is allocated.

A8--A11 use the non-coordinate F3 maps
`j(a,b)=(a,a;b,0)` and `k(u,v)=(0,u;-v,v)` with
`J|x1,x2>=|x1,x1+x2>`.  They check all Weyl actions, actual Kraus versus index
partial trace, completeness, trace preservation/duality, three transported
correlated inputs, characteristic restriction and exact cyclotomic phase
cancellation.

A12 constructs D1710's compatibility fixture through separate single-step,
complement and composite permutations.  Direct and sequential decoders agree
on all 729 three-register matrix units and three correlated states.  This is
only one explicit compatible datum and is never generalized to arbitrary
model unitaries.

After the sole checker repair, all thirteen actual-data mutations exit `1` at
their intended A1--A12 gates. A6 now requires nonempty state sets and asserts
the exact per-field/rank tuple `(19683,12393,531441,85293)`, total 648810.
The new census-loss mutation runs the truncated F81 rank-two data and is
rejected with observed final count 85280.
Temporarily disabling the corresponding guards made the trace-degree,
half-coordinate, normalized-decoder and tower-order reds each survive with
exit `0`; restored source catches them.  Bad usage exits `2`; ordinary and
optimized greens pass in about 45 and 42 seconds.  A6 is the declared hot path.

On a temporary copy, disabling only the new A6 tuple guard made census-loss
survive with exit `0` after 648797 actual comparisons. Root owns the final
installed thirteen-mode and green battery.

The checker meaningfully reuses pinned GF, Abelian, cyclotomic and monomial
APIs; hashes and presentation boundaries are in `RUNS.md`.  Finite success
does not prove the three claims or imply global/spectral structure.
`PATCH.md` gives anchored integration steps while retaining `SKETCH`.
