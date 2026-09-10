# Candidate definitions and claims for DG-CHAR2

The labels below are provisional. The coordinator should assign the next
unused definition numbers after concurrent completion-interface registration.

## D-CHAR2-WEYL — all-rank polarizing datum

Fix a finite field `k` of characteristic two, a nontrivial additive character
`psi:k->mu_2 subset C^times`, a finite-dimensional symplectic k-space
`(V,omega)`, and a named k-bilinear map `beta:VxV->k` satisfying
`beta-beta^T=omega`. Put `Q_beta(v)=beta(v,v)`.

Define the complex vector space with basis `W_beta(v)`, product

    W_beta(v)W_beta(w)=psi(beta(v,w))W_beta(v+w),

unit `W_beta(0)`, involution

    W_beta(v)^*=psi(Q_beta(v))W_beta(v),

and coefficient trace `tau_beta(sum_v c_v W_beta(v))=c_0`.

Define `Mod_(psi,beta)(V)` to have irreducible unital star-representations in
which every Weyl basis element is unitary and unitary intertwiners as arrows;
`PMod` quotients its arrows by `U(1)`.

For standard `V=k^n+k^n`, prescribe

    beta_0((a,b),(a',b'))=a dot b',
    H_(k,n)=l2(k^n),
    W_beta0(a,b)delta_y=psi(-b dot (y+a))delta_(y+a),

with `H_(k,0)=C`. No half-form notation is used.

## D-CHAR2-LIFT — defect-lift symmetry groupoid

Fix common `(k,psi)` as above and `mu_4={1,i,-1,-i}`. Objects are
`(V,omega_V,beta_V)` from D-CHAR2-WEYL. An arrow V to W is a pair `(g,r)` in
which `g:V->W` is a k-linear symplectic isomorphism and
`r:V->mu_4`, `r(0)=1`, satisfies

    r(v)r(w) psi(beta_W(gv,gw)-beta_V(v,w))=r(v+w).

Equality is componentwise. For `(g,r):V->W` and `(h,s):W->Z`, prescribe

    (h,s)o(g,r)=(hg, v -> r(v)s(gv)),
    1_V=(1_V,1),
    (g,r)^-1=(g^-1, w -> r(g^-1 w)^-1).

Tensor uses direct sums of objects and

    (g,r) tensor (h,s)=(g direct-sum h,(v,w)->r(v)s(w)).

The unit is `(0,0,0)`; associator, unitors and swap are the D1701 linear maps
with cochain one. The forgetful functor sends `(g,r)` to g in `S_k`.

The translation action on a lift over g is prescribed by

    t.(g,r)=(g, v -> psi(omega_W(t,gv))r(v)),    t in W.

At an endomorphism object and g equal to the identity, this embeds the
translation group through `t -> (v -> psi(omega_V(t,v)))`.

Prescribe the framed-algebra action

    Alpha_(g,r)(W_betaV(v))=r(v)W_betaW(gv).

For chosen model objects `(H_V,pi_V)`, an implementer is a unitary U with

    U pi_V(a) U^*=pi_W(Alpha_(g,r)(a)).

Its projective class is the intended Hilbert arrow. For a fixed object/model,
the group of pairs `((g,r),U)` is retained as the pullback central extension

    1 -> U(1) -> Imp_(psi,beta)(V) -> Aut_D-CHAR2-LIFT(V) -> 1.

This definition does not prescribe a section of either the forgetful
extension or the implementer extension.

## Proposed claim SP-CHAR2-WEYL

For every D-CHAR2-WEYL datum of symplectic rank n, polarizing beta choices
exist but none is distinguished. The displayed operations make
`A_(psi,beta)(V)` a unital finite-dimensional star-algebra with faithful
normalized coefficient trace, star-isomorphic to `End_C(C^(q^n))`. Its
irreducible unitary model has dimension `q^n`, is unique up to unitary
equivalence, and unitary intertwiners are unique up to `U(1)`. The standard
model is the level-four F1 realization, agrees with D8/D16 at rank one, and
gives C at rank zero. Changing beta admits frame isomorphisms but selects no
preferred one.

Scope: characteristic two only; beta and any coordinates are named. No odd
half-form, canonical beta, or general symmetry splitting is asserted.

## Proposed claim SP-CHAR2-LIFT

For fixed `(k,psi)`, D-CHAR2-LIFT is a symmetric monoidal groupoid and every
k-linear symplectic isomorphism has at least one lift. Each forgetful fibre is
a torsor for `Hom((V,+),mu_2)`, which the chosen phase pairing identifies with
the target translation space by the displayed action. This is a phase-level
statement and not an identification with GH08's raw Witt-centre kernel.

The maps `Alpha_(g,r)` form an exact symmetric monoidal functor to finite
matrix star-algebras and trace-preserving star-isomorphisms. For chosen models,
they have unique projective unitary implementers; those compose/tensor
projectively, and their conjugation channels compose/tensor exactly. The
implementer-pair group is the displayed central `U(1)` extension.

A lift can be chosen `mu_2`-valued exactly when
`Q_betaW(gv)=Q_betaV(v)` for every v. Otherwise every lift assumes a value of
exact order four. No multiplicative section over `Sp(V)` and no reduction of
the central `U(1)` extension to `mu_4` is asserted.

Dependencies to register: D1001--D1005, D1007, D1701, the two new definitions,
F1-REAL, F1-RING, F1-FUNCT, WH-WEIL-a, WH-WEIL-c and WH-WEIL-d. SP-WEYL and
SP-EGOROV are interface precedents at odd scope, not characteristic-two proof
lemmas.

## Comparison deliberately not yet formulated as a claim

The GH08 raw-to-phase map needs the exact `2R`/k identification, central
character quotient, kernel and image written first. docs/research-plans/phantasm-char2-source-comparison.md gives that
bounded work. Until it is typed, do not add an `SP-CHAR2-GH` claim or include
an isomorphism with GH08 ASp/AMp in either proposed claim above.
