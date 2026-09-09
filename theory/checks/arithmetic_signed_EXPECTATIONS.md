# Signed-orbit conjecture: preregistered finite evidence

Date: 2026-09-09. The S target was registered in
`briefs/arithmetic-limits-target.md` and
`docs/research-plans/signed-orbit-filtration.md` before this checker.
LIM-SIGNED remains CONJECTURE; these tests do not establish generality.

S1 enumerates actual quotient-field labels in F3,F9,F27,F81,F5,F25,
checks all nonzero labels have inverses, obtains each Frobenius period
by iteration, and traverses its orbit to test membership of its negative.
It compares the resulting internal/external counts with the proposed
Moebius formulas. `--red-sign` changes only that negation action to identity
and must fail S1. The quotient polynomials are declared in the checker;
irreducibility is not assumed without the exact inverse test.

S2 forms sparse integer coefficient polynomials independently of field
enumeration, expands around t=1 by binomial coefficients, and tests the
first or second nonzero coefficients for d=1--48. It also checks positivity
at t=1001/1000,3/2,2. `--red-order` falsely requires the even external
count to have nonzero first derivative and must fail S2 after S1 passes.
All arithmetic is exact and no tolerance is used.
