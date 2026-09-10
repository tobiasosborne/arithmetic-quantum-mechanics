# Mechanical adjudication — SP-FOCK, SP-PRIME, SP-BC-CONTROL

Date: 2026-09-10. Adjudicator model: `gpt-5.6-sol`, reasoning `xhigh`.
This record mechanically disposes of the frozen sole blind PASS verdict and
the sole repair wave. It is not a fresh mathematical review and introduces no
new objection.

## Preserved review

The sole same-family blind verdict is frozen at
`theory/verdicts/phantasm-completions-r1.md`. It gives separate PASS
dispositions to SP-FOCK, SP-PRIME, and SP-BC-CONTROL, with no FATAL or MAJOR
finding and no requested proof repair.

The mathematical proofs remain byte-identical to the reviewed versions:

| proof | SHA-256 |
|---|---|
| `fock.md` | `10b05e43ba54e12ca7d4c6c9bb2551976d5ddb040b075cdda7312fb04318358e` |
| `prime-tensor.md` | `45eda8795015d244722b8543e8d798aaad4dd66859a440f8dcafd5636c495ad7` |
| `bc-control.md` | `629d0900be215a7b61128bb456804a6a5564397931cdeac46b77c94004d85210` |

## Finding 1 — F3 actual tensor-power growth: CLOSED

The repaired F3 applies the actual tensor power of `2I` in sectors zero
through four to a normalized symmetric basis vector. It checks coefficient
`2^r`, squared norm `4^r`, and commutation with the actual symmetrizer.

New `--red-fock-tensor-collapse` replaces those actual powers by same-size
identities and exits 1 first at F3, sector one. Root's disabled-control record
retains the collapsed powers while removing only this new guard; the mutation
then reaches `RED SURVIVED` and exits 0. Restoration returns exit 1. This is
the exact data path and acceptance reachability demanded by the verdict.

## Finding 2 — B1 nonmultiple adjoint divisibility: CLOSED

The repaired B1 compares `mu_star(n,k)` directly with the exact oracle
`k/n` when divisible and undefined otherwise for every sampled n,k.

New `--red-mu-adjoint-divisibility` makes only the actual n=5 helper return
floor division on nonmultiples and exits 1 first at B1. With only the new
direct comparison disabled, root records the mutant surviving B1 with exit 0;
the restored checker catches it. This closes the second false-acceptance path.

## Finding 3 — labbook evidence wording: CLOSED

`labbook-repair.md` records the exact replacement of
`Finite controls in preparation` by
`Exact finite/symbolic controls; review pending` in the main overview
provenance. No statement, definition, proof, scope, or status changed.

## Final checker evidence

The installed checker SHA-256 is
`d4e0f6eb13aefc87d2d964d9d608f7f0c7237e45b0b842e29fcc95f6f43ad4f0`;
the expectations SHA-256 is
`f1f578c39d9ac95455f38e5809892cfedce09ee1f6e79d3fb897ea30d8f07515`.

Root's `checker-final.json` records all fifteen actual help-advertised reds
exiting 1 at their intended F1--F3, P1--P2, and B1--B4 gates. Normal and
optimized green both exit 0. `disabled-final-controls.json` records the two
new mutants exiting 0 when only their respective new guards are disabled.

The completed unchanged baseline contains 33 suites and 352 red modes and
passed in 560.654 seconds. The final completion checker adds one suite and
fifteen reds, giving aggregate evidence of 34 suites and 367 reds. This is an
aggregate of separately completed runs, not a claimed post-promotion combined
runner invocation.

## Exact admitted scopes

SP-FOCK concerns arbitrary complex Hilbert spaces and contractions. It gives
bounded symmetric second quantization, the natural normalized two-variable
exponential unitary, zero/one-mode identifications, and the stated particle-
number action/domain. It asserts no strong-monoidal coherence or free-monoid
comparison.

SP-PRIME concerns the specified finite matrix factors, increasing-prime
identity insertions, and chosen positive trace-one local densities. It gives
the unital C-star inductive completion, compatible product state, and GNS
von Neumann algebra with a cyclic vector. It asserts no inter-prime arithmetic
coupling, state or representation faithfulness, separating vector, or factor
type.

SP-BC-CONTROL concerns the concrete representation on `l2(N_>0)`. It gives
the displayed semigroup/phase relations, corner endomorphisms, UCP transfer
maps, self-adjoint logarithmic energy, invariant point-norm continuous flow,
and trace-class Gibbs density for real `b>1`. It asserts no universal-
presentation faithfulness, KMS classification, modular comparison, global
system, or zeta-zero spectrum.

## Decision

All three mathematical proofs passed the sole blind review unchanged. Both
MINOR checker findings and the labbook NOTE are closed with targeted evidence.
I recommend three separate admissions:

Admitted: SP-FOCK

Admitted: SP-PRIME

Admitted: SP-BC-CONTROL

Root retains the canonical status/provenance edits, final post-promotion
22-contract check, PDF rebuild, lockstep verification, commit, and push. None
is claimed complete by this adjudication.

The coordinator adopted all three admissions and completed the canonical
status/provenance edits. Structured proof sections are unchanged; their
admission headers are the only changes from the reviewed versions. The
post-promotion contract passed green and all twenty-two mutations at their
intended gates. The 191-page labbook builds and passes lockstep. Definitions
on pp.171--172 and 174 and proofs on pp.185--186 and 189--191 were visually
inspected; the final unit-vector growth gloss was checked again after its
clarification. Final source hashes and aggregate 34-suite/367-red coverage
are frozen in the completion result directory. All fifteen bootstrap claims
are proved, while all seven design gates and the full goal remain open.

PASS
