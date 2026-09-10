# REPAIR — sole SP-SUM checker repair wave

Date: 2026-09-10. Repair model: `gpt-5.6-sol`, reasoning `xhigh`.
Input: `theory/lanes/phantasm-sum/critic/VERDICT.md`, findings 1--2 only.

This is a bounded mechanical checker repair.  It changes no mathematical
proof, canonical record, scope, status or trunk file and triggers no new
review.

## Finding 1 — imported census guard repaired

U2 now checks the actual imported tuple before the exclusion witness:

- 216 Clifford rays;
- 144 rank-one rays;
- 360 endomorphism rays;
- every pair of the 360 endomorphism representatives is projectively
  distinct under exact cyclotomic cross-products.

The direct and transitive import hashes remain recorded in `RUNS.md`.  New
`census-loss` truncates the actual endomorphism tuple and first fails U2a.
Existing `pure-two-unit` passes the intact census guard, then appends the
rank-two diagonal to the actual family and first fails U2b.  Thus completeness
and exclusion are separate live assertions.

With only U2a disabled, `census-loss` survived U2 and exited `0`.  Restoration
returned it to exit `1` at U2a.

## Finding 2 — shortened projection family propagated

U7's `used` tuple now drives the completeness sum and every actual dephasing
call used for unitality, idempotence and range.  `projection-loss` still first
fails U7a completeness.  With only U7a temporarily disabled, the mutation
continued with one projection and failed U7b unitality.  This verifies that
the operation itself, rather than only its completeness summary, changes.

## Final verification

The changed/new reds were observed before final greens.  All ten advertised
modes exit `1` at their intended U1--U8 gates.  Normal and optimized greens
pass; help exposes exactly ten flags.  Explicit empty matrix shapes and all
finite scopes are unchanged.  `RUNS.md` records the exact paths.

The checker remains finite negative-binding evidence only.
