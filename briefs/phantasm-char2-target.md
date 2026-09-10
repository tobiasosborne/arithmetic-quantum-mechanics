# DG-CHAR2 — bounded definition and comparison work order

Date: 2026-09-10. Planning model: `gpt-5.6-sol`, reasoning `xhigh`.

This is source/reuse/definition planning, not a proof or review. DG-CHAR2
should supply the missing characteristic-two local interface required by
DG-GLOBAL. It must not assert the open general splitting conjecture.

## Value gate

The result is useful only if a characteristic-two arithmetic symmetry can be
entered as explicit data and then sent to an exact Weyl-algebra automorphism,
a projective unitary, and hence a phase-independent conjugation channel. The
global construction must be able to compose and tensor these maps. A list of
obstructions without such a positive carrier does not close DG-CHAR2.

The proposed carrier is the un-split defect-lift groupoid of briefs/phantasm-char2-interfaces.md:
no section is chosen, without asserting that no section exists in a given
case.
Its arrows are `(g,r)`, where `g` is symplectic and `r` is a `mu_4`-valued
cochain correcting the chosen polarizing cocycles. The character kernel is
the translation-like part. There is no separate `(t,g)` coordinate until a
section is chosen; in characteristic two no such section is canonical or
known uniformly to be multiplicative.

## Definition gate before proof

Register two definitions, with numbers assigned only after the concurrently
running completion definitions have reserved theirs:

1. the all-rank characteristic-two Weyl datum `(k,psi,V,omega,beta)`, its
   star-algebra, coefficient trace, standard model and model groupoids;
2. the lifted groupoid, including arrows, equality, defect equation,
   composition, inverse, unit, tensor, projection to the linear symplectic
   groupoid, algebra action, and implementer extension.

Every object retains a named `beta`. Every standard-model formula retains a
named symplectic coordinate map. Every projective realization retains a
chosen irreducible unitary model. A genuine unitary representative retains an
additional `U(1)` phase. A GH08 finite `mu_4` refinement additionally retains
the source's Witt lift and Lagrangian splitting.

Add F1-FUNCT to the DG-CHAR2 reuse ledger: its fixed-level tensor comparison
is needed and is not supplied by the odd-characteristic SP-TENSOR theorem.

## Proposed proof cluster

### A. SP-CHAR2-WEYL

1. For every finite characteristic-two symplectic space, choose a symplectic
   basis and construct one `beta` with `beta-beta^T=omega`. Prove existence,
   while denying a distinguished choice.
2. In chosen coordinates compare the reference `beta_0` model with D1002--
   D1005 at cyclotomic level `N=4`. The configuration group has exponent two;
   its characters land in `mu_2 subset mu_4`.
3. For arbitrary `beta`, use the symmetric cocycle difference and L-TRIV to
   transport the reference frame with a `mu_4` cochain. Apply F1-REAL to get
   the full matrix algebra, trace orthogonality, dimension `q^(2n)`, model
   dimension `q^n`, irreducibility and `U(1)` uniqueness.
4. Check the prescribed star is the operator adjoint, the coefficient trace
   is normalized/faithful, and rank zero is `C`.
5. Recover D8/D16 and F1-RING at rank one, without claiming that D1703's odd
   half-form exists at `p=2`.

### B. SP-CHAR2-LIFT

1. For a symplectic isomorphism `g`, show its cocycle defect is symmetric.
   Apply the constructive exponent-two L-TRIV argument to obtain a
   `mu_4`-valued solution `r`; do this in arbitrary rank.
2. Prove the displayed composition, inverse and tensor formulas directly.
   The associator, unitors and swap have cochain one because they preserve the
   direct-sum cocycle on the nose.
3. Prove the forgetful fibre over each `g` is a torsor for
   `Hom((V,+),mu_2)`. Separately prove that the chosen `psi` and `omega`
   identify this phase-quotient kernel with V. Do not use this to identify it
   with GH08's raw `Hom(V,R)` kernel.
4. Prove `W_beta(v) -> r(v)W_gamma(gv)` is an exact trace-preserving star-
   isomorphism, functorial under composition and tensor.
5. Put `Q_beta(v)=beta(v,v)`. Prove a `mu_2`-valued lift exists exactly when
   `Q_gamma(gv)=Q_beta(v)` for every v. If not, every lift takes an exact
   order-four value. Include the admitted rank-one hyperbolic and anisotropic
   exceptions as regressions, not as the all-rank proof.
6. For chosen irreducible unitary models, use F1-REAL to obtain the unique
   projective unitary implementer. Prove projective composition/tensor and the
   exact functor to conjugation channels. At each fixed object/model, retain
   the full central `U(1)` extension of implementer pairs; do not split it.
7. Under separately named GH08 Witt-lift data, compare the source defect
   equation with the phase-level equation after applying its central
   character. Establish only the map actually proved. Kernel, image and any
   reduction of the `U(1)` implementer extension to GH08's `mu_4` AMp remain
   explicit comparison questions until calculated.

## Exact finite falsifier

Pre-register `phantasm_char2_EXPECTATIONS.md`, then implement
`phantasm_char2_check.py` with integer finite-field and exponent-mod-four
arithmetic only.

- C1: standard `beta_0` products, star, trace and sparse Schrödinger action at
  `F2,F4,F8`, ranks 0,1,2; compare rank one with the installed D8/F1 APIs.
- C2: construct defect cochains from an actual F2-coordinate basis and verify
  their equation. Exhaust rank-one `Sp_2(k)` at `q=2,4,8`; exhaust `Sp_4(F2)`
  if runtime remains bounded and otherwise use a declared generator/control
  set. Use selected rank-two F4/F8 generators, never an implicit split.
- C3: check every fibre ratio is a `mu_2` character and the map
  `t -> (v -> psi(omega(t,v)))` is a bijection for the tested spaces. Keep this
  phase quotient separate from raw Witt-centre data.
- C4: test the `mu_2` iff quadratic-isometry criterion. At rank-one `F2`, use
  both reference hyperbolic beta and an anisotropic beta so the known exception
  is not erased; use the admitted `2,6,14` orthogonal counts at q=2,4,8.
- C5: verify algebra-action identity/composition/inverses on all Weyl labels
  for q=2 rank one and selected q=4/q=8 lifts. Independently compare exact
  cyclotomic implementer conjugation for translations, Fourier and shear.
- C6: check tensor of two rank-one lifts against the rank-two defect and
  action, including associator, unit, swap and rank zero. Use F1-FUNCT only at
  fixed level four.
- C7: verify that changing an implementer by a scalar leaves the channel
  unchanged, while changing `r` by a nontrivial character generally changes
  the algebra automorphism/channel by an inner Weyl conjugation.
- C8: for one fully named q=2 GH08-style Witt datum, compare raw R-valued
  defects, their complex phases and the proposed phase-level arrow without
  claiming kernel/image exhaustion.

Required real mutations: replace beta by the nonexistent half-form; force all
`r` into `mu_2`; erase the defect cochain; drop one factor from composed `r`;
use a scalar phase to identify two character-different lifts; tensor with a
Cartesian two-centre group instead of the fixed-level central product; merge
rank zero with an empty additive object; and identify the raw GH08 kernel with
the phase quotient before applying the central character. Each help mode must
exit 1 at its named first gate; unexpected errors exit 2, and disabled-gate
survivors exit 0.

Finite tests do not prove all-rank lift existence, monoidal coherence or a
source comparison. The written proof must carry those clauses.

## Acceptance and handoff to DG-GLOBAL

Use two bounded proof shards, one independent checker, one blind critic pass,
one repair wave, and mechanical adjudication. DG-CHAR2 closes only after both
new claims are admitted and the GH08 comparison is stated at its actual
strength.

The handoff to DG-GLOBAL is then concrete: every p=2 local linear symplectic
generator must name a lift arrow `(g,r)`. A classical output translation t is
encoded by multiplying r(v) by `psi(omega(t,gv))`. The resulting algebra map
and conjugation channel compose and tensor with the prescribed laws. The gate supplies
no cross-prime arrow, global algebra, scalar-retaining relation lift, rig,
modular identification or spectral statement.
