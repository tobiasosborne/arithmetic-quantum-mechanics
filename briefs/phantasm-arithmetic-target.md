# Phantasm arithmetic interfaces — trace, Frobenius, and subsystems

Preparation date: 2026-09-10. Planning model: `gpt-5.6-sol`, reasoning
`xhigh`. This work follows the planned bounded SP-SUM pass. It prepares
SP-TRACE, then SP-FROB, and SP-SUBSYS once SP-CP is admitted. It contains no
proof, review, status change, or new foundational programme.

**Completed 2026-09-10:** SP-TRACE, SP-FROB and SP-SUBSYS are admitted through
`theory/verdicts/phantasm-arithmetic-adjudication.md`. D1710 and the SP-FROB
process-typing dependency were registered before proof work. The planning
language below is preserved as the work order, not the current status.
The next work order is `briefs/phantasm-completions-target.md`.

## Exact objective and boundaries

Build the local arithmetic action needed before any global-state assembly:
restriction of scalars must preserve the odd-characteristic half-form Weyl
datum; relative Frobenius must act covariantly for a named base character;
and a nondegenerate symplectic inclusion must yield a genuine tensor
subsystem with ordinary-trace decoding. Include extension degree divisible by
the characteristic, arbitrary symplectic rank, `n=0`, nonstandard base
characters, and compatible towers.

Do not extrapolate the half-form to characteristic two, redo finite
Stone--von Neumann, identify relative trace with subfield inclusion, replace a
subsystem decoder by D1327's support-code success branch, or infer a global or
spectral construction.

## Exact admitted reuse

| claim/proof | reusable clause | remaining interface |
|---|---|---|
| FRB-TRACE, `theory/sidequests/frobenius-hierarchy/foundation.md` §1 `<1>2`--`<1>6` | Relative trace is K-linear, nonzero/surjective even when `p` divides `[E:K]`; kernel size, tower transitivity, trace pairing and absolute trace-form nondegeneracy | Apply surjectivity/pairing to arbitrary-rank E-symplectic `V`; prove the K-trace form nondegenerate and compare the two named-character half-form products |
| FRB-FROB, foundation.md §2 `<1>1`--`<1>3` | Absolute p-power permutation, exact Weyl covariance, order, trace invariance and basis/trace-dual atomic factorization | Take the `s`th power for `#K=p^s`, tensor `n` times, use relative rather than absolute character invariance, and rephase to D1703's symmetrized frame |
| SP-WEYL plus F1-REAL §2 | Full matrix Weyl realization, trace orthogonality and projective model uniqueness in arbitrary finite rank | Reuse after equality of Weyl products; do not restart SvN |
| SP-TENSOR plus F1-FUNCT §3 | Exact direct-sum/tensor comparison, units, associativity and symmetry | Supply arbitrary-rank subsystem factorization and `n=0`; retain named coordinate/model choices |
| FRP-CP `process-category.md` `<1>6`--`<1>10` | Kraus CP, ordinary-trace normalization, tensor and actual discard for arithmetic images | SP-SUBSYS needs arbitrary Hilbert partial trace through `J`, not a source support-code decoder |
| SP-CP | Ambient finite-block Kraus/channel and ordinary-trace-adjoint theorem | Admitted; reused only for ambient channel and ordinary-trace-adjoint typing |

`theory/checks/phantasm_reuse_check.py` R6 is finite evidence only. It checks
the tower `F3 subset F9 subset F81`, a nonstandard F9 character inside F81,
relative trace/character composition, and `#F9`-power rather than p-power
covariance. It does not prove arbitrary rank, all towers, or subsystem laws.

## Planned process-typing dependency before proof

For this work order, use SP-CP as the common ambient channel criterion.
SP-FROB calls `rho |-> U_(E/K,n) rho U_(E/K,n)^*` an invertible channel, but
its current Definitions omit D1706 and its Dependencies omit SP-CP. Before
using this planned proof route, add
`D1706` and `SP-CP` to the canonical row and DAG fields, with Reuse stating
that SP-CP supplies only the ambient unitary-channel typing. This registers the chosen reuse route, not a new obstruction to unitary
conjugation. This dependency is now registered and SP-CP is admitted;
SP-FROB remains SKETCH until its own proof and SP-TRACE dependency pass review.

The proposed exact D1710 extension is in `briefs/phantasm-arithmetic-interfaces.md`;
the next checker specification is `briefs/phantasm-arithmetic-checks.md`.
Before SP-SUBSYS proof integration, explicitly own the direct-versus-iterated
model comparison, reassociation and phase allowance. The D1710 proposal has now been registered, with irreducible unitary models
and explicitly bound tensor vectors. Its geometric and decoder laws remain
proof obligations. The canonical definition governs the proof.

No new definition number is needed. D1709 already owns the trace form,
general base character, relative power and rank-`n` permutation; D1710 owns
`j,W,J,iota_J,D_J`. Tower restriction maps and proof-local complement bases
are witnesses, not retained data. D1710's specified `J` remains a choice up
to phase; existence and phase-independent consequences belong to SP-SUBSYS.

## Proof A — SP-TRACE

One 260--400-line Lamport shard.

1. Prove alternation of `Tr_(E/K) omega_E`. For `v!=0`, use E-nondegeneracy
   to realize any scalar as `omega_E(v,w)` and FRB-TRACE surjectivity to
   choose one with nonzero relative trace; conclude K-nondegeneracy.
2. Prove `chi_(E/K)=chi_K o Tr_(E/K)` nontrivial from trace surjectivity,
   without restricting or renaming the fixed absolute character `psi_E`.
3. In odd characteristic compare, on every underlying label `v,w`,
   `chi_(E/K)(omega_E(v,w)/2)` with
   `chi_K(omega_Res(v,w)/2)`. Prove product, star, unit and coefficient trace
   agree, so the identity label map is the exact half-form star-isomorphism.
4. For `L subset K subset E`, use trace transitivity to identify one-step
   and iterated restricted forms, characters and Weyl products. Include zero
   rank and degree divisible by `p`; never replace trace by degree times an
   element.

## Proof B — SP-FROB

One 260--400-line Lamport shard after SP-TRACE as an explicit dependency.

1. Prove `x |-> x^(#K)` is K-linear and symplectic for the relative trace
   form because relative trace is invariant under its cyclic conjugate
   permutation. Its `[E:K]`th power is identity; no minimal-period claim is
   needed.
2. Prove `chi_(E/K)(x^(#K))=chi_(E/K)(x)`. This holds for every named
   `chi_K` because relative trace is invariant; it does not assert invariance
   of an arbitrary K-character under the one-step absolute p-power action.
3. Take `(U_E^s)^tensor n`, compare translations, phases and the half-form
   cochain directly, and prove exact covariance on every `W^s_(E,n)(a,b)`.
   At `n=0` use `C`, the empty tensor and the identity channel.
4. Use SP-CP only to type unitary conjugation as an invertible channel;
   prove its inverse and `[E:K]`th power directly. Do not call it partial
   trace or a non-bijective Frobenius interpretation.

## Proof C — SP-SUBSYS

Two 220--360-line Lamport shards: geometry/model comparison, then decoder.

1. For symplectic `j:U->V`, prove
   `V=j(U) direct-sum j(U)^perp`: the intersection is zero, dimensions add,
   and the restricted complement form is nondegenerate. Cover `U=0` and
   zero complement.
2. The sum map `U direct-sum W->V` is symplectic. Use SP-TENSOR and SP-WEYL
   projective model uniqueness to obtain a compatible `J`; record that its
   phase is not selected.
3. Prove `iota_J(a)=J(a tensor 1)J^*` is a unital star-homomorphism. Prove
   `D_J(rho)=Tr_W(J^*rho J)` is a channel with Kraus maps
   `(1 tensor <e_i|)J^*` and ordinary, unnormalized partial trace.
4. Establish the exact Weyl-characteristic restriction
   `Tr(D_J(rho)W_U^s(u))=Tr(rho W_V^s(ju))` (and its starred version if used),
   using trace duality with `iota_J`. Show `J -> lambda J` cancels from both
   maps.
5. For a named compatible decomposition `V=U direct-sum W_1 direct-sum W_2`,
   expand matrix units to prove iterated partial traces compose under the
   stated associator. Incompatible labels or model unitaries give no claim.
6. Explicitly contrast D1327: its support-code success map is TNI, has a
   failure outcome and arises from a field embedding; `D_J` is the TP
   decoder of a specified nondegenerate tensor factor.

## Exact finite falsifier split

Freeze expectations first. Extend or add one arithmetic-interface checker
without treating `phantasm_reuse_check.py` R6 as proof.

- Trace/Frobenius: `F27/F3` (degree 3 equals characteristic),
  `F3 subset F9 subset F81`, nonstandard F9 base character, ranks `n=0,1,2`,
  one-step versus iterated forms/products, and `#K`-power covariance.
- Subsystem: standard `F3` inclusions `V_0->V_1->V_2->V_3`, a non-coordinate
  symplectic injection, correlated rational density matrices, Weyl
  characteristic values, phase-rescaled `J`, and a three-factor decoder
  tower. Compare observable inclusion and state decoder in opposite
  directions.
- Named mutations, each with one registered first gate: `trace-degree`,
  `character-conflation`, `tower-order`, `half-form-trace`,
  `absolute-frobenius`, `half-coordinate`, `rank-zero`,
  `degenerate-subsystem`, `decoder-normalized-trace`, `decoder-phase`,
  `decoder-direction`, and `decoder-tower-order`. Caught mutations exit 1,
  surviving controls exit 0, and usage/unexpected failures exit 2.

## Order and acceptance

After the planned SP-SUM pass: register the SP-FROB dependency repair; freeze
checker expectations and red paths; prove/review SP-TRACE, then SP-FROB;
prove/review SP-SUBSYS once SP-CP is admitted. Use one prover pass, one blind
review and one repair wave per artifact. Labbook and categorical-structure
records move in lockstep.

Acceptance requires the exact canonical statements, all edge cases above,
honest SP-CP dependency, and no claim beyond local arithmetic covariance and
specified subsystem decoding. These results advance the arithmetic action
and local-state interfaces needed by DG-GLOBAL; they do not themselves build
the prime product state, inter-prime maps, modular flow or spectral operator.
