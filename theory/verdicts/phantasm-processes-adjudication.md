# Mechanical adjudication — scalar representatives and finite processes

Date: 2026-09-10. Adjudicator: `gpt-5.6-sol`, reasoning `xhigh`.

This record mechanically disposes the preserved blind verdict and the sole
prover/checker repair waves. It is not a fresh hostile review, and it adds no
new mathematical objection or proof.

## Record used

- `theory/verdicts/phantasm-processes-r1.md` — sole blind verdict.
- `prover-repair.md` in the result directory below — OBJ-1 and OBJ-2.
- `checker-repair.md` in that directory — OBJ-3.
- Final targeted records in
  `numerics/symplectic-phantasm/results/processes-2026-09-10/`.
- Repaired canonical claim, proof, definition, labbook and checker anchors.

The critic returned `FAIL(OBJ-1)`: one MAJOR on SP-SCALAR, plus two MINOR
objections concerning SP-CP's adjoint proof leaf and checker P3 reachability.
Its verified-correct fence accepted the CP, contraction, scalar-modulus,
intrinsic Kraus, trace, composition, tensor, instrument, retained-outcome,
adjoint-boundary and source-equality calculations. Those calculations were not
re-reviewed or changed.

## OBJ-1 — scalar-quotient consequence

The original statement said a successful branch required choosing an actual
representative. The critic exhibited the representative-independent rule

    N_[T](rho)=T rho T^*/||T||^2

on every nonzero projective class, so that necessity sentence was too strong.

The sole repair weakens the canonical SP-SCALAR row, DAG, proof and labbook in
lockstep. They now say:

- D1705 itself stipulates no actual branch or probability;
- a branch may be specified by choosing an admissible representative **or**
  by adding an admissible class-invariant normalization rule;
- phase changes do not change the resulting branch;
- compatibility of an added rule with composition is a separate obligation.

The repaired `scalar.md` proves the norm-rule cancellation under `S=cT`, the
contraction inequality `T^*T/||T||^2<=I`, and the separate zero-class branch.
It claims neither a canonical preferred rule nor a normalization functor.

OBJ-1 is closed at the critic's surviving weaker statement.

## OBJ-2 — trace-adjoint existence

D1706 prescribes the ordinary-trace adjoint for every complex-linear block
map. The original proof constructed only the CP/Kraus specialization.

Repaired `process-instruments.md` section 5 now starts with an arbitrary
complex-linear map. Ordinary-trace-orthonormal block matrix units construct
the conjugate-transpose coefficient map and prove existence, the pairing
identity and uniqueness. Section 6 then specializes to CP maps and retains the
verified reverse-Kraus, subunital/unital and non-TNI discard calculations.

The integrated labbook contains the same general construction. Root's
mechanical notation repair writes
`Tr_X((E^a)^*E^(a'))`, keeping the fixed block label distinct from the
orthonormality indices; this changes no mathematics.

OBJ-2 is closed.

## OBJ-3 — P3 mutation reachability

The original `kraus-adjoint-order` mode stopped at the rectangular direction
boundary and did not reach P3's coefficient or completeness paths.

The sole checker repair adds two actual-data modes:

- `kraus-forward-transpose` keeps the forward type and first fails P3a on the
  off-diagonal input unit `x1:E_(0,1)`;
- `kraus-overcomplete` replaces `(1/2)I_2` by `2I_2`, passes P3a coefficient
  equality and P3b Choi positivity, then first fails P3c completeness.

With only P3c disabled on a temporary copy, `kraus-overcomplete` survived with
exit `0`; restoration returned it to exit `1` at P3c. OBJ-3 is closed.

## Final targeted verification

The installed checker hash is
`21ab75d607ade15d3e61ad391f8631ab4a84de39e2b1c252c14695bdacb5a56d`.
Root verified:

- ordinary and optimized green runs, P1--P11;
- exactly nineteen help-advertised actual-data mutations, each exiting `1`
  at its intended gate;
- the disabled-P3c survival control above;
- the earlier disabled P2 acceptance control, also exiting `0` while its sole
  guard was disabled.

The final green retains the exact finite scalar, block, composition, tensor,
outcome and adjoint controls. It is negative-binding finite evidence, not the
general proof.

The canonical existing-suite session-close completed successfully with
30 green suites and 310 advertised red runs. Its thirty checker hashes remain
unchanged. The final process checker adds one green suite and nineteen red
modes, giving complete current coverage of **31 green suites and 329 red
modes**. Coverage is assembled from the unchanged existing suites and the
new checker; it is not presented as one post-promotion runner invocation.

After both promotions, the contract checker passed green and all twenty-two
mutations at their intended gates. The final 183-page PDF built and the
lockstep gate passed. The new definition was inspected on p.170 and the final
scalar/instrument statements and proofs on pp.180--181. A page break keeps
the scalar proposition heading with its statement. Final source hashes and
coverage records accompany the landing; no finite pass supplies the general
mathematical proof.

## SP-SCALAR decision

The sole MAJOR is repaired by weakening the exact statement; its main theorem
and the repaired consequence have no remaining FATAL or MAJOR. FRP-CP is an
admitted dependency. Scope remains nonzero finite-dimensional Hilbert spaces,
arbitrary linear `T` including zero, and actual ordinary-trace branches.

Admitted: SP-SCALAR

## SP-CP decision

The blind verdict found no FATAL or MAJOR on SP-CP. Its sole proof MINOR and
checker MINOR are repaired and mechanically reached. FRP-CP is admitted.
Scope remains finite nonempty families of nonzero Hilbert blocks with ordinary
trace, actual CP-map equality and explicitly retained outcome order.

Admitted: SP-CP

## Boundaries retained

These admissions do not select a preferred lift from projective stabilizer
arrows, prove composition compatibility for any normalization rule, identify
D1325 source equality with CP equality, or assert arithmetic/stabilizer Kraus
exhaustion. The trace adjoint is an ambient reverse CP map and need not be a
reverse branch. No global, modular, Gaussian-channel or spectral result is
introduced.

The coordinator adopted these admissions after mechanical verification and
completed the final integration and gates described above.

PASS
