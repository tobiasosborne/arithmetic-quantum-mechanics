# Exact contextual faithfulness of the symmetric-group Kraus Gram

Status: KCF-1 at q=1 is PROVED after the capped operational review.
The final q>0 Hecke extension remains SKETCH; exact examples do not
promote that unreviewed extension.

Scope: fix a finite set `S` of size `n`, put `H=Sym(S)`, and use the D1125
inclusions `C[H] -> C[Sym(T)]` for finite injections `S->T`.  A normalised
Kraus list is `K=(K_i)` with `K_i in C[H]` and `sum_i K_i^*K_i=1`.

## Candidate D1126 (Kraus Gram and contextual equivalence)

Write `K_i=sum_(h in H) a_i(h)h`.  Its Kraus Gram is

    J_K(h,k)=sum_i a_i(h) conjugate(a_i(k)),       h,k in H.

Two lists are *contextually equivalent* when, after every finite injection
`f:S->T`, their Heisenberg channels agree on all of `C[Sym(T)]`:

    Phi_(K,f)(x)=sum_i i_f(K_i)^* x i_f(K_i).

Equivalently, all ambient state/effect Born experiments agree: finite
C*-algebra states separate self-adjoint outputs, and <1>9 below gives the
separation directly for the recovery effect.

Stable scalar-unitary equivalence means padding both lists by zeros to a common
length and applying one complex unitary matrix to the Kraus index, as in D1125.
An admissible Gram is a positive semidefinite matrix `J in M_H(C)` satisfying

    sum_(h in H) J(hx,h)=delta_(x,1)       for every x in H.

## Theorem KCF-1 (exact operational quotient and sharp context bound)

**Statement.**  For `n>=1` and normalised local Kraus lists `K,L`, the
following are equivalent:

1. `J_K=J_L`;
2. `K,L` are stably scalar-unitarily equivalent;
3. `K,L` are contextually equivalent over all finite ambient sets.

It is enough in (3) to test one ambient set of cardinality `2n-1` and all its
observables.  More strongly, one explicitly constructed involution `g` in that
ambient algebra recovers every entry of `J_K` from `Phi_K(g)`.

For `n>=2`, the cardinality `2n-1` is sharp as a universal bound: there are two
normalised lists with distinct Grams whose channels agree in every context of
cardinality at most `2n-2`, but differ in cardinality `2n-1`.  Thus `n-1`
ancillary points are sufficient and, in the worst case, necessary.  At the
bound the sharpness pair has an explicit positive density and effect whose Born
probabilities differ.

**Proof.**

<1>1. ASSUME `|S|=n` and identify `S` with a subset of an ambient set `T`.

<1>2. For any permutation `g in Sym(T)`,

    H intersect gHg^(-1)=Sym(S intersect gS),

where each symmetric group is embedded by fixing the complement pointwise.

<2>1. A member of `H` has support in `S`; a member of `gHg^(-1)` has support
in `gS`.

<2>2. Their intersection therefore consists exactly of permutations supported
in `S intersect gS`, proving the formula.

<1>3. Take `|T|=2n-1`, choose `s_0 in S`, and let the complement `T\S` have
`n-1` points.

<2>1. Define `g` to fix `s_0` and swap the other `n-1` points of `S` with the
`n-1` points of `T\S` in named pairs.

<2>2. Then `g=g^*=g^(-1)`, `S intersect gS={s_0}`, and <1>2 gives
`H intersect gHg^(-1)={1}`.

<1>4. The map

    H x H -> Sym(T),        (h,k) |-> h^(-1) g k

is injective.

<2>1. If `h^(-1)gk=h'^(-1)gk'`, then
`h'h^(-1)=gk'k^(-1)g^(-1)` belongs to `H intersect gHg^(-1)`.

<2>2. By <1>3 it is the identity, forcing `h=h'` and `k=k'`.

<1>5. Expand the Heisenberg channel on this `g`:

    Phi_K(g)
      =sum_(i,h,k) conjugate(a_i(h)) a_i(k) h^(-1) g k
      =sum_(h,k) J_K(k,h) h^(-1) g k.

<2>1. By <1>4, all displayed group-basis elements are distinct.

<2>2. The coefficient of `h^(-1)gk` is therefore exactly `J_K(k,h)`.

<2>3. Hence equality of the two channels on this single observable forces
`J_K=J_L`.

<1>6. Conversely, `J_K=J_L` makes the coefficient expansion of
`Phi_K(x)` and `Phi_L(x)` equal for every group-basis element `x` in every
ambient symmetric group.

<2>1. Linearity then gives equality on the entire ambient group algebra.

<2>2. This proves equivalence of (1) and (3), and the `2n-1` sufficiency.

<1>7. Gram equality is equivalent to stable scalar-unitary equivalence.

<2>1. For each `h`, form the coefficient column
`v_h=(a_i(h))_i`; for `L`, form `w_h=(b_j(h))_j`.

<2>2. Equality of Grams says that `v_h |-> w_h` preserves every inner
product, so it defines an isometry from `span{v_h}` to `span{w_h}`.

<2>3. Pad the two coefficient spaces by zero coordinates to a common finite
dimension.  Their orthogonal complements then have equal dimension, so extend
the isometry to a unitary `U` of the padded space.

<2>4. Then `w_h=Uv_h` for every `h`, which coefficientwise is precisely
stable scalar-unitary mixing of the Kraus lists.

<2>5. The reverse implication follows immediately by summing over the unitary
Kraus index.  This proves equivalence of (1) and (2).

<1>8. Admissible Grams are exactly the Grams of normalised lists.

<2>1. Every `J_K` is positive semidefinite because it is a finite Gram matrix.

<2>2. The coefficient of `x` in `sum_i K_i^*K_i` is

    sum_(i,h) conjugate(a_i(h))a_i(hx)
      =sum_h J_K(hx,h).

<2>3. Kraus normalisation is therefore exactly the displayed affine equations
in D1126.

<2>4. Conversely, factor any finite positive semidefinite `J` as a Gram
matrix and use the resulting vectors as coefficient columns `a_i(h)`.
The affine equations then give `sum_i K_i^*K_i=1`.

<2>5. Thus D1126 gives a list-independent finite parametrisation of the
context-complete process quotient.

<1>9. The recovered difference is an operational Born difference.

<2>1. Since `g` is a self-adjoint involution,
`e_g=(1+g)/2` is an effect in the ambient C*-algebra.

<2>2. The channels are unital, so

    Phi_K(e_g)-Phi_L(e_g)
      =(Phi_K(g)-Phi_L(g))/2.

<2>3. If the Grams differ, <1>5 makes this a nonzero self-adjoint element.
Some state of the finite-dimensional C*-algebra separates it, for example a
vector state in a matrix block containing a nonzero spectral projection.

<2>4. That state assigns different Born probabilities to the same effect
after the two processes.  No Hilbert fibre functor on an input tensor category
is needed; this is ordinary finite C*-algebraic separation.

<1>10. It remains to prove sharpness.  ASSUME `n>=2`, `n<=N<=2n-2`, embed
`S` into any `N`-point ambient set, and take arbitrary `g in Sym(N)`.

<2>1. Inclusion-exclusion gives

    |S intersect gS| >= |S|+|gS|-N = 2n-N >= 2.

<2>2. Therefore `H intersect gHg^(-1)` contains a transposition `t`; its
conjugate `t'=g^(-1)tg` is also a transposition in `H`.

<1>11. In `C[H]`, put

    p_+=(1/|H|)sum_(h in H) h,
    p_-=(1/|H|)sum_(h in H) sign(h)h,
    r=1-p_+-p_-.

<2>1. These are the mutually orthogonal central projections for the trivial,
sign, and remaining representation blocks; `r=0` when `n=2` is allowed.

<2>2. The odd transpositions satisfy
`p_-t=-p_-` and `t'p_+=p_+`.

<2>3. Since `tg=gt'`,

    p_-gp_+ = -p_-tgp_+ = -p_-gt'p_+ = -p_-gp_+,

so `p_-gp_+=0`.  Taking adjoints, or replacing `g` by `g^(-1)`, also gives
`p_+gp_-=0`.

<1>12. Define the two local Kraus lists

    K=(p_++p_-, r),          L=(p_+-p_-, r).

<2>1. Orthogonality of the three projections gives
`sum_i K_i^*K_i=sum_i L_i^*L_i=1`.

<2>2. On any ambient element `x`, their Heisenberg-channel difference is

    Phi_K(x)-Phi_L(x)=2(p_+xp_-+p_-xp_+).

<2>3. By <1>11 this vanishes on every group-basis element `g` in every
ambient cardinality `N<=2n-2`, hence it vanishes on the full algebra.

<1>13. The two Grams are nevertheless distinct.

<2>1. The coefficients of `p_+` and `p_-` at the identity are both `1/|H|`.

<2>2. At Gram entry `(1,1)`, the common `r` contribution cancels, while the
first Kraus terms differ by `4/|H|^2`.

<2>3. In the `2n-1` context of <1>3, <1>5 therefore distinguishes them.
Equivalently, `p_-gp_+` is a nonzero sum of distinct double-coset basis terms.

<1>14. The distinction at the bound has a constructive Born witness.

<2>1. Put `e_g=(1+g)/2` and
`Delta=Phi_K(e_g)-Phi_L(e_g)`, for the sharpness lists of <1>12.

<2>2. Those Kraus operators are self-adjoint, so normalisation also gives
`sum_i K_iK_i^*=sum_i L_iL_i^*=1`.  Traciality makes both Heisenberg channels
`tau_T`-preserving; hence `tau_T(Delta)=0`.

<2>3. Each channel sends `e_g` to an effect.  Therefore
`-1<=Delta<=1`, and `rho=1+Delta` is positive with `tau_T(rho)=1`.

<2>4. The difference between the two Born probabilities for initial density
`rho` and effect `e_g` is

    tau_T(rho Phi_K(e_g))-tau_T(rho Phi_L(e_g))
      =tau_T((1+Delta)Delta)=tau_T(Delta^2)>0.

<2>5. Strict positivity uses faithfulness of the coefficient trace and
`Delta!=0` from <1>13.  Every coefficient of `rho` and `e_g` is rational.

<1>15. Thus no smaller ambient cardinality is a universal faithfulness bound,
whereas `2n-1` always suffices.  Together with <1>5--<1>9, all parts of the
statement follow.  QED.

## Consequence for the proposed `q=1` endpoint

The process morphism can be stored exactly as an admissible positive Gram `J`,
rather than as a chosen Kraus list or as its isolated CP action.  Composition
and disjoint-union tensor descend because Gram equality is the stable
scalar-unitary congruence already used in D1125.  KCF-1 supplies a finite
operational test for that quotient: `n-1` ancillary points expose all process
coherences of an `n`-point support.

## Separated Hecke extension (SKETCH only)

For the positive Hecke C*-tower, the same recovery argument should apply with
`H_q(S_n)` inside `H_q(S_(2n-1))`.  The candidate witness is the involutive
minimal double-coset representative

    d=(0,n,n+1,...,2n-2,1,...,n-1),      length(d)=(n-1)^2.

The required exact lemmas are: the intersection parabolic is trivial;
`length(hdk)=length(h)+length(d)+length(k)`; and the `T_(h^(-1)dk)` are
distinct.  They would make `Phi_K(T_d)` recover the Gram for every `q>0`.
Since `T_d` is self-adjoint, scaling it by
`max(q,1)^length(d)` would give a bounded effect.

For the lower bound, the proposed minimal-double-coset lemma supplies a local
simple reflection `s` when the ambient rank is below `2n-1`.  The trivial and
sign projections obey `T_s p_+=q p_+` and `p_-T_s=-p_-`, giving
`(q+1)p_-T_dp_+=0`.  This would make the same `p_+ plus-or-minus p_-` lists
indistinguishable below the bound.  These Coxeter-length and positivity steps
belong to the separate Hecke proof and are not claimed by KCF-1.

---

# Partial-injection functor for the symmetric-group quantum net

Status: PMAP-1 is PROVED after the capped operational review.  This is finite `q=1` only.  Szczesny, Definition 6 (p. 8) supplies
normal pointed-module maps; D1010 records that at the one-point monoid their
nonzero parts are partial injections.

## Candidate D1127 (partial-injection operational realisation)

Let `FinPInj` have finite sets and partial injections.  Write
`f:S partial->T` as a bijection `f:D->E` between `D subset S` and `E subset T`.
For the D1125 net define

    R(f)=i_(E subset T) o A(f:D isomorphic E) o E_(D subset S)
         : A(S) -> A(T).

Inclusions use extension by the identity; `E` is subgroup coefficient
expectation.  The target category has finite tracial C*-algebras and unital,
trace-preserving CP maps, with trace adjoint as dagger.

## Proposition PMAP-1

**Statement.**  `R` is a dagger functor and, with the D1125 block inclusions
`mu_(S,T):A(S) tensor A(T)->A(S disjoint-union T)`, a lax symmetric monoidal
functor.  The laxators are generally proper.  The empty partial injection is
sent to the trace-and-prepare channel, not the zero linear map.

**Proof.**

<1>1. Each factor of `R(f)` is UCP and preserves the coefficient trace.
<2>1. Relabelling is a trace-preserving star-isomorphism, subgroup extension
is a trace-preserving star-monomorphism, and its trace adjoint is the subgroup
conditional expectation from CPOP-5.
<2>2. Thus `R(f)` is a bistochastic CP map.

<1>2. On a permutation basis element `sigma in Sym(S)`, `R(f)` is zero unless
`supp(sigma) subset D`; when it survives, it is the permutation
`f sigma f^(-1)` on `E`, extended by the identity on `T\E`.

<1>3. Let `g:T partial->U` have domain `F`.
<2>1. The element from <1>2 survives the expectation in `R(g)` exactly when
`f(supp(sigma)) subset F`.
<2>2. Together with `supp(sigma) subset D`, this is equivalent to

    supp(sigma) subset D intersect f^(-1)(F)=dom(gf).

<2>3. In that case the output is `(gf)sigma(gf)^(-1)`, extended by identity;
otherwise both `R(g)R(f)` and `R(gf)` vanish.
<2>4. Hence `R(g)R(f)=R(gf)` on a basis and therefore on all of `A(S)`.
The full-domain identity clearly maps to the identity channel, so `R` is a
functor.

<1>4. With inner product `<a,b>_S=tau_S(a^*b)`, subgroup inclusion and
expectation are adjoint, while relabelling by `f` has adjoint relabelling by
`f^(-1)`.
<2>1. Reversing the three factors in D1127 gives exactly `R(f^dagger)`, where
`f^dagger:E->D` is the inverse partial injection.
<2>2. Therefore `R(f^dagger)=R(f)^dagger`.

<1>5. For partial injections `f:S partial->T` and `f':S' partial->T'`, test
the lax naturality square on `sigma tensor sigma'`.
<2>1. The block permutation survives `R(f disjoint-union f')` exactly when
`supp(sigma) subset dom(f)` and `supp(sigma') subset dom(f')`.
<2>2. These are exactly the two survival conditions on
`mu_(T,T')(R(f)(sigma) tensor R(f')(sigma'))`, and the surviving relabelled
block permutations agree.
<2>3. Thus

    R(f disjoint-union f') mu_(S,S')
      =mu_(T,T') (R(f) tensor R(f')).

<1>6. Block permutation inclusions obey the disjoint-union associator, unit,
and swap identities on the nose after the canonical set bijections.
<2>1. They are therefore lax symmetric monoidal coherence maps for `R`.
<2>2. They need not be invertible: two singleton systems give
`C tensor C -> C[S_2]=C^2`, a proper inclusion.  Hence the result is lax, not
strong monoidal.

<1>7. If `f` has empty domain, its first expectation is
`E_empty(a)=tau_S(a) in C`, and the final inclusion sends a scalar to the
scalar identity of `A(T)`.
<2>1. Therefore `R(f)(a)=tau_S(a)1_T`.  This is the normalised
trace-and-prepare channel and is not the zero CP map.
<2>2. Consequently `R` is an ordinary, nonadditive functor and is not required
to preserve the zero morphisms of the pointed-map category as zero linear
maps.

<1>8. Wedge of finite pointed sets becomes disjoint union of their nonzero
parts, and `mu` realises it as collective assembly by a proper tensor-algebra
embedding.  It is not the classical C*-algebra direct sum, which would encode
exclusive alternatives rather than jointly assembled subsystems.  QED.
