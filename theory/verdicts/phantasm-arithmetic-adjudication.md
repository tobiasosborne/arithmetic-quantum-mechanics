# Mechanical adjudication — SP-TRACE, SP-FROB, SP-SUBSYS

Date: 2026-09-10. Adjudicator model: `gpt-5.6-sol`, reasoning `xhigh`.
This is a mechanical disposition of the preserved sole blind verdict and the
sole repair wave. It is not a fresh mathematical review and raises no new
objection.

## Preserved review record

The sole same-family blind review is frozen at
`theory/verdicts/phantasm-arithmetic-r1.md`. It records separate PASS
dispositions for SP-TRACE, SP-FROB, and SP-SUBSYS, with no FATAL or MAJOR
finding. SP-FROB was explicitly conditional on admitting SP-TRACE first.

The reviewed proof hashes were:

| proof | reviewed SHA-256 |
|---|---|
| `trace.md` | `bc866d7dc3ced40e1fc05d267bf2f98698130c849fc69be8ba13d4df67a5a84a` |
| `frobenius.md` | `104797e27041bfa3004402bd3c9204174f426ca6dfa539313ff824d6af880669` |
| `subsystem-models.md` | `03d9466a51f68434f10d8bef7ab63f33e758a015d3d4294722f62e862aef639d` |
| `subsystem-decoder.md` | `a0335511700a45e832ed9ac09f1534413c1771a66a79dae97b813d9bccc0641f` |

The pre-repair files, critic recomputation, and critic runs are preserved in
`numerics/symplectic-phantasm/results/arithmetic-2026-09-10/`.

## Disposition of finding 1 — CLOSED

The critic found one redundant direct citation to FRP-DESCENT in
`subsystem-decoder.md` section 5 `<1>2`; D1327 itself owns the boundary being
used, and FRP-DESCENT was not a canonical SP-SUBSYS dependency.

Root's `proof-repair.md` records deletion of exactly `/FRP-DESCENT`. No
statement, equation, argument, scope, or dependency was added. The other
three proof files retain their reviewed hashes. The repaired
`subsystem-decoder.md` hash is
`28049a5776a7dbb256df107f0b98607a915f3facd9fa836c16a1434f449a485d`.
This is the exact fix demanded by the preserved verdict and requires no new
mathematical review.

## Disposition of finding 2 — CLOSED

The critic showed that A6 did not reject an empty covariance census. The sole
checker repair now:

- materializes and rejects an empty state census for every field/rank case;
- asserts the exact tuple `(19683,12393,531441,85293)`, whose sum is 648,810;
- adds `--red-covariance-census-loss`, which removes the final actual F81
  rank-two state and executes all remaining comparisons before failing A6
  with observed count 85,280 instead of 85,293.

The final installed checker hash is
`689c53d32f6bd7369bb19697926e55c49500140fa76bb041a80de6de911c563d`;
the final expectations hash is
`547867ea84e9ced9bdcf57273ba6e7a064b4df6120227e58ec984e4c0423ff2c`.

Root's `checker-final.json` records all thirteen actual help-advertised reds
exiting 1 at their intended A1--A12 gates. Normal and optimized greens both
exit 0 and report all 648,810 A6 cases. In the separate
`disabled-final-census-control.json`, only the per-field/rank count guard was
disabled while the shortened actual census and covariance/nonempty checks
remained; the mutant then survived with exit 0 after 648,797 comparisons.
This establishes the repaired guard's acceptance reachability.

## Exact admitted scope

SP-TRACE covers every finite extension of odd-characteristic finite fields,
arbitrary finite symplectic rank including zero, every named nontrivial base
character, extension degrees divisible by the characteristic, exact
half-form label comparison, and compatible induced characters along towers.

SP-FROB covers the standard coordinate register only. Relative `|K|`-power
Frobenius is K-linear symplectic for the SP-TRACE form, preserves the induced
named character, has exact symmetrized Weyl covariance, and induces an
invertible ordinary-trace channel whose `[E:K]`th power is identity. SP-CP is
used only for channel typing. Abstract spaces still require D1709's named
semilinear datum.

SP-SUBSYS covers a symplectic injection over an odd-characteristic finite
field with one common character and chosen irreducible model data. It includes
the nondegenerate complement, a model unitary unique up to phase, the forward
observable inclusion, reverse ordinary partial-trace decoder, phase
independence, zero-rank factors, and decoder composition only under the full
registered iterated-J compatibility.

No claim adds a characteristic-two half-form, normalized decoder, field
support-code identification, global assembly, inter-prime map, modular flow,
or spectral statement.

## Verification accounting

The completed unchanged baseline records 32 suites and 339 red modes. The
final arithmetic checker adds one suite and thirteen red modes, giving the
recorded aggregate 33 suites and 352 reds. This is aggregate evidence from
completed runs, not a claimed post-promotion full-suite invocation.

Root still owns canonical status/provenance edits, the final post-promotion
22-contract check, PDF rebuild, and lockstep verification. None is claimed
complete here.

## Decision

Both preserved findings are closed exactly, and no proof-strength or scope
change entered the repair. Admit in dependency order:

Admitted: SP-TRACE

Admitted: SP-FROB

Admitted: SP-SUBSYS

At canonical integration, G4 required the literal ASSUME marker in the
Frobenius shard. The coordinator relabelled its existing global hypothesis
paragraph without changing its hypotheses or argument. The preserved
reviewed proofs, exact citation repair and admission-header differences
remain auditable in the result directory.

The coordinator completed the canonical admissions in dependency order. The
post-promotion contract passed green and all twenty-two mutations at their
intended gates. The 188-page labbook builds and passes lockstep; the expanded
subsystem definition on pp.172--173 and the arithmetic proofs on pp.185--188
were visually inspected. Existing checker hashes remain unchanged and the
aggregate current coverage is 33 suites and 352 reds as recorded above.
Final artifacts and scoped validation are frozen in the arithmetic result
directory. Finite checks are evidence at their stated scope, not the general
proof. The full goal and all seven design gates remain open.

PASS
