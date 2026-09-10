# Phantasm stage 1 — capped review adjudication

Date: 2026-09-10. Scope: SP-WEYL, SP-EGOROV and SP-TENSOR only, under
`briefs/phantasm-stage1-target.md`.

The existing Weyl corollary received one blind hostile pass, recorded in
`phantasm-weyl-r1.md`. Its author's model was not recorded; the critic was
`gpt-5.6-sol`, xhigh, and no cross-family independence is asserted. The new
Egorov/Tensor prover and independent blind critic were both `gpt-5.6-sol`,
xhigh; their single verdict is `phantasm-egorov-tensor-r1.md`. The exact
checker was written independently of the prover. Both verdicts are PASS,
with no FATAL or MAJOR. One repair wave followed each pass; the coordinator
verified the repairs mechanically. There was no fresh hostile re-review.

## Decisions in dependency order

Admitted: SP-WEYL

The arbitrary-rank odd-characteristic realization is a corollary of the
admitted F1-DUAL, F1-WEYL and F1-REAL. The reviewed bridge supplies the
symplectic coordinates, signed character dual, half-form rephasing, raw
central quotient by ker(psi), normalized trace and rank-zero/rank-one
comparisons. The uniqueness assertion explicitly concerns irreducible
unitary representations with the stipulated central character.

Admitted: SP-EGOROV

With SP-WEYL admitted, the exact affine star-isomorphism, semidirect
composition and projective unitary implementation follow from the reviewed
proof. D1703 now owns the arbitrary-rank model class and unitary-intertwiner
quotient it uses. No genuine phase lift is selected.

Admitted: SP-TENSOR

With SP-WEYL and SP-EGOROV admitted, the natural trace-preserving tensor
comparison, exact algebra coherence and projective model coherence follow
from the reviewed proof. The underlying configuration-product result is
the previously admitted F1-FUNCT; only its half-form and affine comparisons
are new. It is not used as an input to SP-WEYL.

The other eleven SP claims retain SKETCH. These decisions do not establish
relation quantization, a characteristic-two lift, an additive completion,
a global arithmetic system or a spectral correspondence with zeta zeros.

## Repair dispositions and mechanical verification

| Finding | Repair and verified scope |
|---|---|
| Weyl OBJ-1: unitary qualifier omitted | The canonical row, exact labbook restatement and raw-group proof now explicitly quantify over unitary representations. The central quotient and all algebraic computations are unchanged. |
| Weyl OBJ-2: constructed R4 checks | R4 now compares the actual zero-label operator with the identity and derives matrix traces from operator entries before comparison with the coefficient functional. Its vacuum mutation changes the actual operator phase; its normalization mutation changes the expected coefficient functional. Both reach R4. On temporary copies, disabling each specific comparison makes its mutation survive, confirming the failure depends on the mathematical comparison. |
| Weyl OBJ-3: proof text is not executable input | Accepted scope limitation. The blind critic recomputed the proof text; the checkers test their implemented finite interfaces and recorded contracts. Source-text sign mutations surviving the checkers are not described as proof validation. |
| Affine/Tensor O1: model-type ownership | D1703 explicitly extends D9's finite-dimensional simple unitary models, unitary intertwiners, composition and U(1) quotient. The standard coordinate construction remains separately named. D9's existing body is unchanged; the shared notation owner, direct dependencies and proof citations are aligned. The real-LaTeX definition body and scope are identical in the canonical register and labbook under the contract comparison. |
| Affine/Tensor O2: synthetic rank-zero red | The synthetic dimension precheck is removed. The advertised red now replaces the actual empty-power Hilbert basis by the F3 basis and fails at E7's model-dimension comparison. All other mathematical gates are unchanged. |

For O1, the reviewed proof diffs only add the model owner and type the model
objects/intertwiners. They do not change the affine product, star, phase,
tensor or coherence equations. The rank-one prescription agrees with D9:
unitarity of each Weyl generator gives
`pi(W(v)^*)=pi(W(-v))=pi(W(v))^*`, and conjugate-linearity extends this to
the algebra. Composition of unitary intertwiners remains an intertwiner;
replacing representatives by phases multiplies a composite by their product,
so the stated quotient has the same composition prescription. These are
definition/interface checks, not a new finite Stone--von Neumann proof.

Two additional coordinator interface defects were repaired before admission.
The contract's false-promotion mutation now clears admission evidence even
when its target is already PROVED; an already-promoted in-memory fixture
exposed the old inert mutation. Inherited provenance is checked before
generic promotion conditions so its mutation still reaches G8. In the new
affine checker, an uncaught red now exits zero, as the session-close interface
requires. Disabling E9's acceptance comparison on a temporary copy exposed
the previous exit-2 false acceptance and verified the corrected exit zero.
Wrong-gate/usage errors remain distinct and are rejected by the explicit
named-gate verifier.

## Evidence and product

The repaired reuse suite passes 141,939 exact finite comparisons and all
eleven intended red gates. The installed affine suite passes 4,654,737
reported comparisons and all nine intended red gates, including all 216
affine F3 arrows, the nonstandard F9 character and 3,779,136 factorwise
rank-two naturality cases. The contract passes green and all 21 intended
red gates. Frozen targeted runs and disabled-comparison controls are in
`numerics/symplectic-phantasm/results/stage1-2026-09-10/`; final source
hashes and the full session-close result accompany the landing record.
The completed landing validation passed all 28 green suites and 279
advertised red runs. All 21 contract mutations were also checked for their
specific intended exit gates after the three promotions; the final layout
build and lockstep gate passed.

The labbook carries the exact statements and scopes, the expanded model
definition and readable proofs. The Weyl proof explicitly separates the
nonzero-plane induction from rank zero. Numerical passes support only
their declared finite scope; the arbitrary-rank conclusions rest on the
reviewed structured proofs and admitted dependencies.

PASS
