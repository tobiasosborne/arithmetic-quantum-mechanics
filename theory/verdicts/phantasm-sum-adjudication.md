# Mechanical adjudication — SP-SUM

Date: 2026-09-10. Adjudicator model: `gpt-5.6-sol`, reasoning `xhigh`.
This is a mechanical disposition of the preserved blind verdict and the sole
checker repair wave. It is not a fresh mathematical review.

## Record admitted for decision

- Exact claim: SP-SUM in `claims/CLAIMS.md` and `claims/PHANTASM-DAG.md`.
- Mathematical proof: `theory/symplectic-phantasm/sum.md`, reviewed-pass SHA-256
  `11ce000439fa096c2264bc9dca3f38953e198d74c940ade7df94c8761f6c1f06`.
- Sole valid review: `theory/verdicts/phantasm-sum-r1.md`.
- Review setting: same-family `gpt-5.6-sol` prover/critic, literal blind lane,
  critic reasoning `xhigh`.
- Preserved verdict: `PASS`, with no FATAL or MAJOR objection, two MINOR
  checker findings, and one scope-register NOTE.
- Sole checker repair: `checker-repair.md` in the sum result directory.
- Final installed checker SHA-256:
  `7c691be27c36bea16a344e9f3de114c3e48a67c20976871366e6f33f275d1b6c`.

No mathematical proof repair was requested or made. The reviewed pass is
frozen as `reviewed-sum.md` in the result directory; only the canonical
admission header changes at promotion. The critic independently
verified the rectangular matrix-unit span, strict finite-ray enlargement,
block realization including empty and repeated positions, coherent/tagged
dimensions, and ordinary-trace block dephasing, conditional only on the
already admitted dependencies at their registered scopes.

## Disposition of preserved findings

### Finding 1 — U2 imported-census completeness: CLOSED

The repaired U2a checks 216 Clifford rays, 144 rank-one rays, 360 endomorphism
rays, and pairwise projective distinctness before U2b tests exclusion of
`diag(1,1,0)`. The new `--red-census-loss` truncates the actual tuple and exits
1 first at U2a. With only U2a disabled on a temporary copy, that mutation
survived and exited 0. The original `--red-pure-two-unit` reaches and fails U2b.

### Finding 2 — U7 projection-loss propagation: CLOSED

The repaired `used` projection tuple drives completeness and every dephasing
call for unitality, idempotence, and range. `--red-projection-loss` exits 1
first at U7a. With only U7a disabled on a temporary copy, the same shortened
family continues and exits 1 at U7b, proving operation-level propagation.

### Finding 3 — arithmetic-coefficient DAG wording: CLOSED

SP-SUM's DAG Remaining and Construction outline now say that the complex hull
strictly enlarges the pure stabilizer fragment and explicitly make no
arithmetic-source comparison. This matches the exact claim and proof scope.

## Mechanical verification record

Root verified the final installed checker in normal and optimized modes; both
green runs passed U1--U8. All ten actual `--help` red modes exited 1 at their
intended gates. The two disabled-guard controls above establish exit-0
acceptance reachability or the later propagated failure as appropriate.

The already completed canonical session-close covered 31 unchanged suites and
329 reds. The final SP-SUM checker adds one suite and ten red modes, for the
recorded aggregate 32 suites and 339 reds. This is an aggregate of separate
completed runs, not a claimed post-promotion full-suite invocation.

## Scope retained

Admission is limited to odd primes, standard stabilizer model spaces, finite
ordered lists including the empty list for the linear completion, and
nonempty lists for D1706 channels. The coherent span is the full complex
linear Hom-space; the tagged algebra is the chosen block-diagonal subalgebra;
dephasing uses ordinary trace. The result adds no biproduct, fusion, rig,
Gaussian, arithmetic-source, normalized-trace, or zero-space-channel claim.

## Decision

The sole blind mathematical review passed, every preserved finding is closed,
the proof is unchanged, and the checker repair has the required targeted
controls. I recommend promotion of the exact canonical SP-SUM statement.

Admitted: SP-SUM

The coordinator adopted the admission and completed the canonical
status/provenance edits. The post-promotion contract passed green and all
twenty-two mutations at their intended gates. The final 185-page labbook
build and lockstep gate passed; the revised definition on p.171 and the
statement/proof on pp.182--183 were visually inspected. Current checker
coverage remains the verified aggregate described above, with unchanged
existing-suite hashes and the final new checker. Final source hashes are
frozen in the result directory; finite checks are not the general proof.

PASS
