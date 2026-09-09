# Exact finite joined-limit falsifiers

`composite_joined_check.py` uses only the standard library and exact
integer/Fraction arithmetic. The preregistration is preserved in its
verifier lane; frozen outputs and coverage are in
`numerics/composite-joined/results/`.

Green passes 9,272 comparisons across J1--J5. J1 checks the divided period
polynomial, endpoint grade and uniform scalar bounds; J2 checks actual
copied arithmetic preparations and randomizer histories; J3 checks degree
priors and normalized physical mixtures; J4 checks exact trace-norm tails
and fixed common effects; J5 checks first-grade success and finite continuity.

The actual field samples reach F256 and include s=2. Scalar samples use
d=2..64, s=1,2, beta=2,3,4, rational t in [1,2] and shrinking rational
steps above one. The cutoff pairs range from (2,4) to (32,64).
The invariant randomized reference and the unrandomized Frobenius witness
are different placements and are tested separately.

Eleven distinct --red-* mutations and plain --red must all exit one with
JSON status FAIL at J1--J5. Plain --red aliases drop-divisor. Parser errors
and unrelated interpreter exceptions are not accepted as red evidence.
The verifier fixed and recorded an empty-vector rational-zero bug during
development before freezing the final executable.

No finite sample certifies the infinite degree bound, trace-norm limit,
all real beta>1 or arbitrary joined paths. Those claims rely on the written
and independently reviewed proof. At t=1 the raw success is zero; the
checker retains a separate first-grade state and never normalizes that
zero event directly.
