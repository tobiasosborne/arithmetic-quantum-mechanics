# REPAIR — sole process-checker repair wave

Date: 2026-09-10. Repair model: `gpt-5.6-sol`, reasoning `xhigh`.
Input: `theory/lanes/phantasm-processes/critic/VERDICT.md`, OBJ3 only.

This is the one bounded mechanical checker repair.  It changes no proof,
canonical statement, scope, status or trunk file, and commissions no further
proof review.

## OBJ3 — repaired

P3 retains the original `kraus-adjoint-order` rectangular type-boundary mode.
Two actual-data modes now reach the previously uncovered comparisons:

1. `kraus-forward-transpose` keeps source `X` and target `Y`, but the real
   dense production action transposes the `x1` input matrix only for the
   `x1->y0` component.  The independently assembled coefficient action stays
   canonical.  The mutation first fails P3a on off-diagonal matrix unit
   `x1:E_(0,1)`.
2. `kraus-overcomplete` replaces the actual `x1->y0` operator `(1/2)I_2` by
   `2I_2` in the fixture used by production, coefficient and Choi routes.
   It therefore passes all P3a equality and P3b positivity checks, then first
   fails P3c's actual per-input completeness/strictness condition.

Neither mode changes an expected literal or stops in an isolated preflight.
P3's messages name the coefficient, Choi and completeness subchecks.

## Verification

Both new reds exited `1` at their exact intended paths before repaired green.
The repaired green passed P1--P11.  Temporarily disabling only P3c made the
overcomplete actual data survive P3 with exit `0`; restoring the comparison
returned the mutation to exit `1` at P3c.

All nineteen final help-advertised reds exit `1` at their registered gates.
The original seventeen paths are preserved.  Normal and optimized greens
pass, help exposes exactly nineteen supported flags, and malformed/multiple
usage exits `2`.  Full outputs are in `RUNS.md`.

The finite checker remains negative-binding only and supplies no proof or
promotion.
