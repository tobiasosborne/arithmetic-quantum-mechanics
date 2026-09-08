# Frobenius, subfield codes, and arithmetic Clifford-hierarchy morphisms

Opened 2026-09-08, at the user's explicit request to plan and orchestrate work.
This is a new authorized campaign, superseding the earlier discussion-only
boundary for these topics. The mainline finite-ring and frozen marked-module
campaigns remain unchanged.

## Aim and deliverable

Construct a small, explicit arithmetic quantum process category containing
Frobenius, field-inclusion and trace transfers, subfield stabilizer codes, and
reversible multiplication gates at higher Clifford levels. Prove the concrete
arithmetic package, give its CP/instrument realization, and integrate the
surviving results and worked examples into the labbook. Record a precise next
stage for a positive q-to-one specialization; do not claim that the entire new
arithmetic category already has such a specialization.

The user explicitly permits adjusting the input category: symplectic spaces,
isotropic flags/Lagrangians and arithmetic descent structure should supply the
geometry. Flags are contexts rather than the sole objects. Higher *levels* of
the Clifford hierarchy are intended, not higher categorical groups.

Effort allocation: about 50% definitions/proofs, 30% exact probes and labbook,
at most 20% review repair and integration. Four native agent slots, including
the orchestrator. Use inherited models; record the actual tool/model convention
on verdicts. No deadline or automatic indefinite research loop is stipulated.

## Scope and stages

1. Arithmetic foundation: trace symplectic form, Frobenius covariance,
   subfield-support stabilizer code, logical Weyl quotient, inclusion and
   normalized trace-fibre transfers, and coherent field towers.
2. Higher gates: for a field E and d>=1,
   M_E^(d)|x_1,...,x_d,z> = |x_1,...,x_d,z+product_i x_i>.
   Establish its exact Clifford level d+1 relative to the prime-field Pauli
   frame, Frobenius covariance, field-embedding intertwining, and encoded
   logical action. Prove all-characteristic scope; no degree/level theorem is
   inferred merely from ordinary polynomial degree without checking it.
3. A typed process category with independent tensor composition, code
   encodings/decodings, Fourier-dual transfers, retained instrument outcomes,
   and a CP realization. Specify equality, identities, scalar conventions,
   choices, and the domain of every arrow. Hierarchy levels label generators;
   fixed higher levels are not declared closed under composition.
4. One blind hostile review, one repair wave, root mechanical adjudication.
   Admit only supported claims, update definitions/notation and self-contained
   labbook sections together, run required session-close checks, commit/push.
5. Preserve the continuing q-to-one programme with concrete candidate data and
   falsifiers: a noncommutative endpoint, a process distinguishing retained
   arithmetic structure, trace positivity, and composition compatibility.

## Fixed conventions and shared proposed interface

Read CLAUDE.md, PRD.md, HANDOFF.md, notation.md, definitions.md, claims/CLAIMS.md,
briefs/lanes/RULES.md, and relevant source locators in refs/LEDGER.md.
Do not import v0.1 as evidence. Root fetches/registers any missing primary sources.

Fix p prime and a named primitive p-th root zeta_p. For E/F_p finite,
H_E=l2(E), psi_E= zeta_p^(Tr_E/Fp), X(a)|x>=|x+a>,
Z(b)|x>=psi_E(bx)|x>, W(a,b)=Z(-b)X(a). Fourier has negative kernel.
For a named field embedding i:K->E, define T:E->K by the relative trace
followed by i^{-1}; hence T(i(a)x)=aT(x).
J_i|a>=|i(a)>; V_T|a>=|ker T|^(-1/2) sum_(T(x)=a)|x>.
The proposed code is C_i=range J_i, with projector P_i=J_i J_i^*.
Its phase stabilizers have labels ker T, its position labels are i(K),
and the logical momentum is a quotient identified using T, not inclusion.
Use ordinary trace-one density matrices for the new finite Hilbert systems;
keep this distinct from Hecke coefficient-trace densities.

Algebra lane reserves D1301--D1319 and claim prefix FRB (specific IDs chosen
in its proposal). Category lane reserves D1321--D1339 and prefix FRP.
Only root edits trunk registries. Coordinate shared definitions by messages.

## Pre-registered finite falsifiers

Checker specifications precede proof admission. Implement exact, independently
computed tests and named data mutations reaching every advertised gate.

- A1: Frobenius preserves the trace symplectic form and the reference Weyl
  convention, including F2, F3, F4, F8, F9, F16 samples.
- A2: independently enumerate subfield-support code and common +1 phase
  stabilizer labels; verify dimension, projector, and logical momentum quotient.
- A3: inclusion/relative-trace identities, tower composition and Frobenius
  equivariance; negative Fourier kernel and correct fibre normalization.
- A4: multiplication-gate bijection, covariance and subfield intertwining,
  including F4->F16; distinguish multiplication from addition as gate data.
- A5: hierarchy membership AND strict lower-level exclusion via independent
  Pauli conjugation/finite-difference sentinels; p=2,3 and separate-register
  degree-three/four cases. A nonzero mixed difference must be observed, not
  fitted from the same formula on both sides.
- A6: exact F2->F4->F16 example: K=F2[a]/(a^2+a+1),
  E=K[b]/(b^2+b+a), sigma(a0,b0)=(a0^2+a*b0^2,b0^2),
  sigma^2(a0,b0)=(a0+b0,b0), sigma has order four.
- A7: CP/instrument normalization, source/target types, success probabilities,
  sequential and independent parallel processes. Category lane supplies any
  additional concrete tests needed for its claims.

Failure examples are constructive boundaries, not separate proof campaigns:
psi_E restricted to K=psi_K^[E:K]; Frobenius fixed vectors differ from
subfield-supported vectors; reset completions of reductions need not preserve
independent tensor; higher hierarchy levels are not groups; complete invariant
flag commutants erase Frobenius. The new structure must retain the data these
examples identify.

## Lane contracts

- Algebra prover writes only theory/lanes/frobenius-hierarchy/algebra/:
  DEFINITIONS-PROPOSED.md, NOTATION-PROPOSED.md, CLAIMS-PROPOSED.md,
  200--500 line Lamport proof shards, a self-contained labbook draft following
  labbook/WRITING-GUIDE.md, PATCH.md and SUMMARY.md. Target 6--9 concise claims.
- Category prover writes only theory/lanes/frobenius-hierarchy/category/:
  analogous proposals, 1--2 proof shards and a labbook draft. Target 2--4
  well-scoped positive claims; an explicit presented arithmetic category is
  acceptable but must not claim representation faithfulness or generic q
  specialization without proof. Also supply ENDPOINT-NEXT.md.
- Checker writes only theory/lanes/frobenius-hierarchy/check/:
  standalone Python checker(s), expectations/mutation matrix, frozen results,
  PATCH.md and SUMMARY.md. Python standard library plus numpy only, prefer
  exact finite arithmetic. Reuse an existing vetted arithmetic helper only
  with explicit provenance and a clear standalone installation strategy.
- Critic is launched later in a fresh context, reads only the brief, final
  artifacts/sources, and registries; follows briefs/critic-protocol.md, writes
  only its verdict lane, and performs independent computations.

## Sources and endpoint discipline

Registered sources include Gurevich--Hadani 0705.4556, Comfort--Kissinger
2105.06244, Comfort 2304.10584, and the finite-field Weyl theory. Root registers
Cui--Gottesman--Krishna 1608.06596, the hierarchy composition source
2212.05398, and trace facts needed from Stacks 0BIE. The higher-gate theorem
should have an internal proof rather than relying on unstated classification.

Keep the existing positive Hecke family as the benchmark. Type-C arithmetic
CP/shuffle comparisons are admitted, but its block Weyl subgroup is
nonparabolic and no generic type-C tensor inclusion is currently proved.
For a nontrivial endpoint Frobenius, retaining the physical normalized trace
p^(1-r) would force its unitary image to be identity in a faithful tracial
endpoint. Name the reference trace and comparison functor in every proposed
specialization. Labels alone do not demonstrate surviving quantum structure.
