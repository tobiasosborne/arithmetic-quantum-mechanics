# Operational categorical limit — capped review adjudication

Opened 2026-09-07; admission work continues into 2026-09-08. The user
authorized Sol and occasional Astra agents and set a 03:00 Berlin cutoff.
The current construction concerns the named Hecke/flag subsystem family,
its full positive completion, the mirabolic vector extension and the stated
polarization/composition comparisons. It does not identify a sequence of
prime powers tending to one or claim a universal limit of every Weyl phase.

## Review and repair structure

- Core: Sol/xhigh prover, blind Astra/xhigh critic, one Sol repair wave.
- Composition: Sol/xhigh prover, blind Sol/xhigh critic, one root repair wave.
- Bridge: Sol/xhigh prover, blind Sol/xhigh critic, one Astra/root repair wave.
- Full Karoubi glue: Astra/xhigh prover, blind Sol/xhigh critic, PASS with
  one minor notation correction; root instantiates its explicit wiring
  interface and the already proved pointwise Gram congruence.

The frozen verdicts are retained as `f1-limit-core-r1.md`,
`f1-limit-composition-r1.md`, `f1-limit-bridge-r1.md` and
`f1-limit-karoubi-r1.md`. Different models here are from the same provider;
no cross-provider review is implied. There was no second hostile review of
repairs. Root verified the changes against the numbered objections by
recomputation, proof inspection and exact finite falsifiers.

## Core objections

| Objection | Repair and verified surviving statement |
|---|---|
| CC1, MAJOR: untyped classical outputs | D1218 defines product/unit/relabeling and classical routing maps, and CWIR-1--3 prove their types and coherence. Sequential histories use `(O times P)` after routing; parallel outputs route only classical wires. A one-outcome identity list is identified with the identity only after its singleton unitor. W1/W2/W5 independently verify finite nontrivial routing/history instances. |
| CC2, MAJOR: effects do not fix backaction | The protocol explicitly uses the Lüders instrument `(P2,1-P2)` and retains the quantum output. W4 derives the branch state from the actual Kraus datum. Replacing P2 by u1P2 preserves the POVM but changes joint probability 1/6 to 2/3, and fails the intended gate. |
| CC3, MINOR: section tensor domain | Interval tensors are C(I)-balanced pointwise section tensors. The ordinary C(I) spatial tensor over C is not called injective. |
| CC4, MINOR: nonexistent C gates | Evidence references use actual L/H/W gates and identify analytical clauses proved only in the structured proof. |
| CC5, MINOR: continuous mixing overclaim | Interval labels use pointwise Gram equality and germs use eventual Gram equality. Fibrewise scalar mixing proves congruence without choosing continuous environmental unitaries. The oscillatory rank-drop example remains a boundary of the stronger assertion. |

The verified analytic core is unchanged: fixed normalized regular frames,
closed continuous C*-section algebras, nonzero parabolic corners, germ
evaluation only at one, local functional-calculus normalization, locally
uniform contextual recovery, and continuity of finite specified instrument
trees. Positive limiting postselection probability remains an explicit
hypothesis. The H3 protocol has success 2/3, conditional return 1/4 and
joint endpoint probability 1/6 with the named Lüders backaction.

## Composition objections

| Objection | Repair and verification |
|---|---|
| 1, MAJOR: finite Day tensor not closed | D1222 requires finite-dimensional level algebras. Induction is a quotient of a finite-dimensional tensor space. The C*-version requires star structural maps; unit maps are explicitly the scalar identifications. |
| 2, MAJOR: unnamed rigid comparison | D1236 names `i:U_q->R`, its monoidal/star data and additive Karoubi target closure. It may be a quotient comparison; full faithfulness is never inferred. The non-rigidity argument includes every mixed-degree candidate dual. The q=1 example is the rigid closure of the Schur--Weyl quotient image. |
| 3, MAJOR: bound's dimension range | The expectation bound retains both d>=n and d>card(K)-1 in definition, proof and claim. The finite d=2 sentinel is only its independently checked special example. |
| 4, MAJOR: LC specifications not executable | Actual L/H gate names and sample limits replace all claimed LC execution. Unimplemented LC designs are labeled as such. |
| 5, MAJOR: old SKETCH dependency | Projection, normalized-sum tensor identity, typed corner multiplication and three-block coherence are derived locally. No F1-OP-FLAGCAT sketch is used to establish the new theorem. |
| 6, MINOR: dagger on bare modules | Module/DM equivalences are algebraic strong monoidal equivalences. Dagger belongs to the self-adjoint projection model. |
| 7, MINOR: ILZ convention | The displayed map is q_ILZ=-v, v²=q_H, U_ILZ=delta f, with delta=v+v^-1. The Fibonacci square parameter has order five. |

Root additionally made generic projection evaluation well typed by using
the self-adjoint-idempotent envelope over the named coefficient ring, and
wrote the balanced-induction inverse in actual column indices. The reviewed
polar/cactus proof, Schur--Weyl kernel, cycle trace, and trace/Born estimates
were preserved.

## Bridge objections

| Objection | Repair and verification |
|---|---|
| O1, MAJOR: arithmetic positivity is insufficient | D1249/D1257/D1258 and the new mirabolic-boundary proof define an actual one-sided regular section/germ circuit category. Density/effect positivity is required for every real q>1 sufficiently near one. Coefficient limits, the faithful quotient trace and the specified Kraus generators prove positive descent and a functor. The critic's arithmetic-positive H2 family is explicitly excluded. Arbitrary coefficient-regular UCP superoperators are also excluded: the null-sector preparation is a counterexample. |
| O2, MAJOR: flag-register monoidality | Tensor preservation is asserted for vector Fourier transforms only. Full flag/Fourier comparison uses the decomposable corner and reversed-shuffle correspondence, with no full-flag tensor identification. |
| O3, MAJOR: missing computational gates | B1/B2/B4/B7 are implemented in `f1_limit_mirabolic_check.py`; B3/B5/B6 and the actual dual-reversal mutation are in `f1_limit_bridge_check.py`. The repaired expectations state exact samples. Kernel composition, dimension-seven generation, vector dephasing, all rank-two quotient products, affine and type-C trace-adjoint pairs, dual rank matrices, and thin signed cosets are tested. |
| O4, MINOR: symbols/star/Fourier square | The affine group no longer reuses the Weyl subalgebra symbol. Orbit star, controlled Z projectors for indices 0 through n, and the double-dual Fourier square `(F,x)->(F,-x)` are explicit. |
| O5, MINOR: stale definition references | Type-C and affine correspondence assumptions use D1250--D1256 with their correct meanings. |

The general mirabolic positivity proof comes from the polynomial orbital
Gram formula, not from positive arithmetic samples. Its reference trace is
faithful for q>1 and semidefinite at one. The exact null ideal is the span
of nonempty-antichain orbitals; its GNS quotient is C[S_n]. Regular
operational evaluation retains the actual generator data and does not erase
the separate question of singular boundary states. The arithmetic type-C
and two-vector shuffle correspondences keep their stated arithmetic scope.

## Full completion and common operational interface

The Karoubi reviewer independently verified all six statements, including
same-degree off-diagonal corners, trace multiplicativity, continuous
arbitrary-corner expectations and projection/unitary lifting. Root renamed
the new trace weight to `w_X=theta_X(1)` to avoid the existing fusion
dimension `d_X`. Its branch density ratio is `w_Y/w_X`, which becomes
`P_alpha/P_beta` on parabolic objects.

The explicit D1218/CWIR-1--3 wiring, including the identity list relation,
instantiates hypothesis W in both the full-completion and regular-mirabolic
operational constructions. Root uses the same pointwise/eventual Gram
equality in all three presentations. The proof of congruence is the already
established fibrewise scalar-mixing cancellation in each finite Hom
coordinate space. No continuous mixing unitary or faithful isolated CP
realization is inferred. The resulting new statements have no unresolved
external wiring hypothesis.

## Admission and validation

The initial admitted package comprises ten core, eight composition,
thirteen bridge and six full-completion claims: 37 positive rows. All have
explicit hypotheses, structured proofs and the recorded capped review or
repair disposition. No previous mainline or FCR-2 result changes status.

Finite falsifiers are supporting evidence. They do not establish all-rank
continuity, general categorical coherence or universal CP positivity by
sampling. Actual samples and mutations are in the five new expectations
records. Final checker/mutation totals, source/link verification, labbook
build and commit outcome will be recorded after integration and session close.

## Additional marked-register action

The separately scoped mirabolic right-module-category theorem received an
independent Sol PASS verdict. Its five proposed claims remain unadmitted at
windup: their definitions, proofs and verdict are preserved under
`docs/research-drafts/f1-marked-action/`, and they are not counted among the
37 rows above. The deadline was missed; all research stopped when the clock
was checked at 05:04 UTC, and only final integration/verification/commit
continued. No further proof or admission work is authorized by this session's
completed time window.
