# REPAIR — sole arithmetic-checker repair wave

Date: 2026-09-10. Repair model: `gpt-5.6-sol`, reasoning `xhigh`.
Input: `theory/lanes/phantasm-arithmetic/critic/VERDICT.md`, checker finding 2
only.

This is a bounded mechanical checker repair. It changes no proof, canonical
record, mathematical scope, status or trunk file and triggers no fresh review.

## A6 census guard — repaired

`covariance_case` now materializes each actual state census and rejects an
empty census before any covariance loop. It returns separate rank-one/rank-two
counts. A6 asserts the exact tuple

    F27: (19683, 12393),   F81: (531441, 85293),

which totals 648810.

New `covariance-census-loss` truncates the actual F81 rank-two state tuple by
one element. It performs all remaining action comparisons and returns 85280
instead of 85293 for that component, so its first failure is the A6 census
guard. No expected literal or reported-only counter is mutated.

On a temporary copy, disabling only the tuple guard allowed the truncated
data to survive with exit `0` after 648797 comparisons. The lane source
retains the guard. Existing twelve red paths and all sparse mathematical
coverage are unchanged.

Root performs the final installed normal/-O and thirteen-mode strict battery.
The checker remains finite negative-binding evidence only.
