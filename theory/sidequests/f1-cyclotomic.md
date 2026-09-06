<!-- ROLE: repaired proof shard for briefs/f1-sidequest.md.
     Definitions D1001--D1007 are in definitions.md. This is a
     positive finite kernel inside a multi-route F1 sidequest, not a proposed
     identification of all quantum mechanics over F1.  Adjudicated after one Sol critic round; see
     theory/verdicts/f1-adjudication.md. -->

# A finite cyclotomic F1 kernel: pointed phases, Weyl operators, and realization

Lane model: `gpt-5.6-sol`, reasoning `xhigh`.  Claims through section 6 are `PROVED` after the capped hostile round.
Section 7 is an algebraic `SKETCH`; its geometric extension remains a target.  The mathematics is the standard
finite-abelian Heisenberg/Stone--von Neumann construction, interpreted through
finite free pointed `mu_N`-sets.  No novelty claim is made for that mathematics.

Fix `N >= 1`, an abstract cyclic group `mu_N` of order `N`, and a **named**
faithful character `iota:mu_N -> C^x`.  Fix a finite abelian group `A` whose
exponent divides `N`.  Write `A^vee=Hom(A,mu_N)`,
`V_A=A x A^vee`, and use additive notation on `A` and multiplicative notation
on characters.  D1001--D1007 in `definitions.md` are the definitions cited
below.  In particular,

    X(a)e_x=e_{x+a},       Z(chi)e_x=iota(chi(x))e_x,
    W(a,chi)=Z(chi)X(a),   c((a,chi),(b,eta))=eta(a)^(-1).

The sign is locked: under `chi_b(x)=psi(-bx)`, this says
`W(a,chi_b)=Z(-b)X(a)` and `c=psi(ab')`, exactly D8/D16.

## 0. Two elementary finite-character lemmas

**L-EXT.**  **ASSUME** `B <= A`, `exp(A)|N`, and
`theta:B->mu_N` a character.  **PROVE** `theta` extends to `A`.

`<1>1.` It suffices to extend across `B < B+<a>` and iterate, because `A` is
finite.  Choose `a notin B`, and let `m` be the order of `a+B` in `A/B`.

`<1>2.` Let `d=ord(a)`.  Then `m|d|N`, while `ma` has order dividing `d/m`.
Thus `theta(ma)` belongs to the subgroup `mu_{d/m}` of `mu_N`.

`<1>3.` Since `m|N`, the `m`-th-power map on `mu_N` has image `mu_{N/m}`.
Because `d/m|N/m`, choose `z in mu_N` with `z^m=theta(ma)`.

`<1>4.` Put `theta'(b+ka)=theta(b)z^k`.  If
`b+ka=b'+k'a`, then `m|(k-k')` and the equality `z^m=theta(ma)` makes the two
values equal.  The displayed rule is multiplicative and extends `theta`.

`<1>5.` Iteration terminates and gives a character on `A`. **QED** (`L-EXT`)

**L-DUAL.**  **ASSUME** `A` as above.  **PROVE** (a) characters separate
points, (b) `|A^vee|=|A|`, and (c) character sums are orthogonal.

`<1>1.` If `0 != a in A`, define on `<a>` the character sending `a` to a
primitive `ord(a)`-th root in `mu_N`; extend it by `L-EXT`.  This proves (a).

`<1>2.` A cyclic group `C_d`, `d|N`, has exactly `d` characters into `mu_N`,
one for each possible image of a generator in `mu_d`.

`<1>3.` Induct on `|A|`.  The cyclic case is `<1>2`.  Otherwise choose a
nonzero proper subgroup `B`.  Restriction `A^vee -> B^vee` is onto by `L-EXT`,
and its kernel is `(A/B)^vee`.  Induction gives
`|A^vee|=|(A/B)^vee||B^vee|=|A/B||B|=|A|`.  This proves (b).

`<1>4.` For a nontrivial `chi`, choose `a_0` with `chi(a_0)!=1`.  Translation
of the sum `S=sum_a iota(chi(a))` by `a_0` gives
`S=iota(chi(a_0))S`, hence `S=0`.  The trivial sum is `|A|`.

`<1>5.` Applying `<1>4` to `chi eta^(-1)` gives
`sum_a iota(chi(a)eta(a)^(-1))=|A|[chi=eta]`.  This proves (c).
**QED** (`L-DUAL`)

## 1. The pointed Heisenberg object and exact Weyl relations

**F1-WEYL.**  **ASSUME** D1001--D1003.  **PROVE** `c` is a normalized
2-cocycle; it defines a Heisenberg group `H_N(A)`, an absorbing-zero phase
monoid `H_N(A)^0`, and a faithful action on the free pointed `mu_N`-set
`S_A`; the commutator pairing is perfect and the displayed Weyl law holds.

`<1>1.` For `v=(a,chi)`, `w=(b,eta)`, `r=(d,rho)`,

    c(v,w)c(v+w,r)=eta(a)^(-1)rho(a+b)^(-1)
                    =rho(b)^(-1)(eta rho)(a)^(-1)
                    =c(w,r)c(v,w+r).

Also `c(0,v)=c(v,0)=1`; hence `c` is normalized.

`<1>2.` Therefore
`(u,v)(u',w)=(uu'c(v,w),v+w)` is associative with unit `(1,0)`.
The inverse of `(u,(a,chi))` is
`(u^(-1)chi(a)^(-1),(-a,chi^(-1)))`, by direct substitution.

`<1>3.` Adjoining an absorbing element `0_H` gives a pointed noncommutative
monoid `H_N(A)^0`.  This is a group-with-zero construction; no addition of
states or amplitudes has been introduced.

`<1>4.` D1003 acts on `S_A={0_S} disjoint-union (mu_N x A)` by

    (u,a,chi)[z,x]=[uz chi(x+a),x+a],       0_H s=0_S.

Two successive nonzero actions have phase
`z eta(x+b)chi(x+a+b)`.  Relative to the action labelled
`(a+b,chi eta)`, the ratio is `eta(a)^(-1)`.  Thus this is precisely the group
law of `<1>2`, and `W(v)W(w)=c(v,w)W(v+w)`.

`<1>5.` If `(u,a,chi)` acts identically, comparison of orbit labels gives
`a=0`; at `x=0` the phase gives `u=1`; then all `x` give `chi=1`.  No group
element acts as the zero map, so the monoid action is faithful.

`<1>6.` The commutator of `(1,a,chi)` and `(1,b,eta)` is

    kappa((a,chi),(b,eta))=chi(b)eta(a)^(-1) in mu_N.

This follows by dividing `c(v,w)` by `c(w,v)`.

`<1>7.` If `kappa(v,w)=1` for every `w`, first take `w=(0,eta)` and use
`L-DUAL(a)` to get `a=0`; then take `w=(b,1)` to get `chi=1`.  Thus `kappa` is
perfect, and the center of `H_N(A)` is exactly `mu_N x {0}`.

`<1>8.` Every formula uses evaluation of a character and group operations.
There is no `1/2`, odd-order hypothesis, field structure, or chosen
identification `A ~= A^vee`. **QED** (`F1-WEYL`, `PROVED`)

## 2. Cyclotomic base extension, matrix algebra, and finite SvN

**F1-REAL.**  **ASSUME** D1001--D1003 and the named `iota`.
**PROVE** cyclotomic base extension sends `S_A` to `C^A`, the Weyl operators
span `End_C(C^A)`, the twisted algebra is `M_|A|(C)`, and the finite
Stone--von Neumann statement holds for central character `iota`.

`<1>1.` By D1001,

    C_iota(S_A)=C[S_A]/(e_0, e_[u,x]-iota(u)e_[1,x]).

The classes `e_x:=e_[1,x]`, `x in A`, are a basis, so this is `C^A`; declaring
them orthonormal makes every realized pointed automorphism unitary monomial.

`<1>2.` Realizing `<1>4` of F1-WEYL gives
`W(a,chi)e_x=iota(chi(x+a))e_(x+a)=Z(chi)X(a)e_x`, hence preserves the exact
cocycle and central `mu_N` acts by `iota`.

`<1>3.` The trace is

    Tr W(a,chi)=0                    if a!=0,
                 sum_x iota(chi(x)) if a=0,

because a nonzero translation has no fixed basis vector.  By `L-DUAL(c)`, the
second line is `|A|` for `chi=1` and `0` otherwise.

`<1>4.` Each `W(v)` is unitary.  Since a scalar multiple of
`W(-v+w)` equals `W(v)^*W(w)`, `<1>3` gives
`Tr(W(v)^*W(w))=|A|[v=w]`.  Thus the Weyl operators are linearly independent.

`<1>5.` By `L-DUAL(b)`, there are `|V_A|=|A|^2` such operators, equal to
`dim_C End_C(C^A)`.  Their image is therefore all of `End_C(C^A)`, and the
twisted algebra `C_iota^c[V_A]` is `M_|A|(C)`.

`<1>6.` The standard module is irreducible because any invariant subspace is
a module for the full endomorphism algebra.  Conversely, let `M` be a simple
module for `M_n(C)`, `n=|A|`.  Some diagonal matrix unit `E_jj` has
`E_jj M!=0`; choose `m` there.  The map
`C^n -> M`, `(z_i)|->sum_i z_i E_ij m`, is a nonzero module map, hence is an
isomorphism because both its kernel and image are submodules and `C^n,M` are
simple.  Thus the simple module is unique up to isomorphism and has dimension
`|A|`.

`<1>7.` An irreducible representation of `H_N(A)` on which `(u,0)` acts as
`iota(u)` factors through the twisted algebra by sending its basis `W(v)` to
the image of `(1,v)`.  Conversely every twisted-algebra module gives such an
`H_N(A)`-representation.  `<1>6` is therefore finite Stone--von Neumann.

`<1>8.` For unitary models, any nonzero intertwiner between irreducibles is
invertible by kernels/images; its polar part is a unitary intertwiner.  The
ratio of two unitary intertwiners commutes with `M_n(C)` and is scalar, hence
lies in `U(1)`.  This is the usual noncanonical uniqueness, not a selected
model-independent vector space.

`<1>9.` The registered standard reference is Prasad, arXiv:0912.0574,
`refs/LEDGER.md` T1 (the finite case of the Stone--von Neumann--Mackey
theorem).  Steps `<1>1`--`<1>8` are a self-contained finite proof because the
source body is not presently available under `refs/`. **QED** (`F1-REAL`,
`PROVED`)

## 3. Isomorphism naturality and the fixed-level tensor product

**F1-FUNCT.**  **ASSUME** D1001--D1004 at one fixed `N`.
**PROVE** the assignment is functorial for isomorphisms of finite abelian
groups of exponent dividing `N` and is strong symmetric monoidal.

The targets are (i) finite free pointed `mu_N`-sets and equivariant
bijections, with balanced smash; (ii) finite groups with a specified central
embedding of `mu_N` and isomorphisms fixing it, with central product; and
(iii) finite-dimensional Hilbert spaces and unitary isomorphisms, with
Hilbert tensor. The action is compatible with these three functors.

`<1>1.` For an isomorphism `f:A->B`, put
`f_*chi=chi o f^(-1)` and

    S(f)[u,x]=[u,f(x)],
    H(f)(u,a,chi)=(u,f(a),f_*chi).

Evaluation gives `(f_*eta)(f(a))=eta(a)`, so `H(f)` preserves `c` and is a
group isomorphism.  The formulas preserve identities and composition.

`<1>2.` Direct evaluation gives
`S(f)W_A(a,chi)=W_B(f(a),f_*chi)S(f)`.  After base extension, `S(f)` becomes
the unitary permutation `U_f e_x=e_f(x)`.  This proves exact naturality.

`<1>3.` For pointed `mu_N`-sets define the balanced smash product by

    S smash_mu T=(S smash T)/([us,t]~[s,ut]).

The map
`Phi_[A,B]:S_A smash_mu S_B -> S_(A x B)`,
`[[u,a],[v,b]] |-> [uv,(a,b)]`, is well-defined, equivariant, and bijective;
its inverse sends `[w,(a,b)]` to `[[w,a],[1,b]]`.

`<1>4.` The unit is `S_0=mu_N disjoint-union {0}`.  The maps in `<1>3` obey
the associativity, unit, and symmetry diagrams because every route multiplies
the same phase entries and forms the same ordered tuple.

`<1>5.` The corresponding phase-group tensor is the central product

    H_N(A) boxdot H_N(B)
      =(H_N(A)xH_N(B))/{((u,0),(u^(-1),0)):u in mu_N}.

The map represented by
`((u,a,chi),(v,b,eta)) |-> (uv,(a,b),chi boxplus eta)` is well-defined and an
isomorphism to `H_N(A x B)`, since its cocycle is the product
`chi'_A(a)^(-1)chi'_B(b)^(-1)`.  A Cartesian product without this quotient
would retain two centers and is not the required tensor.

`<1>6.` Under `Phi_[A,B]`, the central-product action is the tensor action.
Base extension sends `Phi_[A,B]` to
`C^A tensor C^B ~= C^(A x B)`, `e_a tensor e_b |-> e_(a,b)`, and sends Weyl
operators to tensor products.  Thus all three levels are strong symmetric
monoidal at fixed `N`. **QED** (`F1-FUNCT`, `PROVED`)

## 4. Exact recovery of the repository's reference system

**F1-RING.**  **ASSUME** a finite commutative local ring datum D12, an additive
character `psi:R->mu_N` with `iota o psi in Gen(R)`, `exp(R,+)|N`, and D16's reference cocycle
`beta_0((a,b),(a',b'))=ab'`.  **PROVE** the cyclotomic phase group is the
central pushout of `H_beta0(R)`, and realization recovers D8/D16 including
characteristic two.

`<1>1.` Put `A=(R,+)` and `chi_b(x)=psi(-bx)`.  If `chi_b=1`, the ideal `bR`
is contained in `ker psi`; generating means that ideal is zero, whence
`b=b.1=0`.  Thus `b|->chi_b` is injective and, by `L-DUAL(b)`, is an
isomorphism `A ~= A^vee`.

`<1>2.` Form the central pushout

    P_psi=(mu_N x H_beta0(R))
          /{(psi(t)^(-1),(t,0,0)):t in R}.

The map
`[u;(t,a,b)] |-> (u psi(t),a,chi_b)` is well-defined and bijective.

`<1>3.` In `H_beta0(R)`, multiplying `(t,a,b)` and `(t',a',b')` adds `ab'`
to the central coordinate.  In `H_N(A)`, the cocycle under `<1>1` is
`chi_b'(a)^(-1)=psi(ab')`.  Hence the bijection in `<1>2` is a group
isomorphism.

`<1>4.` The natural map `H_beta0(R)->P_psi` kills precisely
`{(t,0,0):t in ker psi}`.  A generating character may have nonzero additive
kernel: for example, a nontrivial trace character of `F_(p^m)`, `m>1`, has
kernel of size `p^(m-1)` but contains no nonzero ideal.  Thus the result is a
central pushout, not an identification with the raw group.

`<1>5.` Let the repository's complex character be `psi_C=iota o psi`.
Then

    W(a,chi_b)=Z(chi_b)X(a)=Z(-b)X(a),
    W(a,chi_b)e_y=psi_C(-b(y+a))e_(y+a),

and its product scalar is `psi_C(ab')`.  These are exactly D8 and D16.

`<1>6.` No step divided by two or used odd characteristic.  For a finite
field, every nontrivial additive character is generating; for D12--D16 the
stated generating hypothesis is exactly D13.  Hence `p=2` is included.
**QED** (`F1-RING`, `PROVED`)

## 5. The level-one boundary is not a cardinality limit

**F1-ONE.**  **ASSUME** `N=1` in D1001--D1004.  **PROVE** the phase kernel is
trivial, while ordinary finite-rank F1 modules remain arbitrary pointed sets.

`<1>1.` `exp(A)|1` implies `a=0` for every `a`, so `A=0`, `A^vee=1`,
`V_A=0`, `H_1(A)=1`, and `S_A` has one non-basepoint.  Its realization is
one-dimensional.

`<1>2.` In the ordinary pointed-set model, a free rank-`r` F1 module is the
pointed set with `r` non-basepoints, for every `r>=0`.  This is a rank
parameter, not a finite abelian configuration group subject to `exp(A)|1`.

`<1>3.` Therefore this cyclotomic kernel at `N=1` neither exhausts F1 modules
nor arises by substituting `q=1` into a cardinality formula. **QED**
(`F1-ONE`, `PROVED`)

## 6. Strict monomial dynamics: exact survivor and Fourier obstruction

Call `theta:A->mu_N`, `theta(0)=1`, a quadratic phase when
`B_theta(a,x)=theta(a+x)theta(a)^(-1)theta(x)^(-1)` is a bicharacter.  For
`t in A`, `f in Aut(A)` define the strict pointed automorphism

    T_(t,f,theta)[u,x]=[u theta(x),f(x)+t].

**F1-MON.**  **ASSUME** D1001--D1003.  **PROVE** these and a central phase are
exactly the strict pointed automorphisms normalizing the level-`mu_N` Weyl
group; identify their induced phase maps; prove Fourier/polarization exchange
is outside strict pointed maps when `|A|>1`.

`<1>1.` Every pointed `mu_N`-equivariant automorphism has a unique form
`T[u,x]=[u r(x),sigma(x)]`, with `sigma` a permutation and `r:A->mu_N`.
Factor the central value `r(0)` and put `theta(x)=r(x)r(0)^(-1)`.

`<1>2.` Suppose `T` normalizes the Weyl group.  Conjugates of all diagonal
`Z(chi)` are diagonal, so their Weyl translation labels are zero.  Hence for
each `chi`, `chi o sigma^(-1)` is a scalar times a character.

`<1>3.` Put `t=sigma(0)`.  Conjugation induces an automorphism
`alpha:A^vee->A^vee`; evaluating the scalar of `<1>2` at `sigma(0)` gives
`chi(x)=alpha(chi)(sigma(x)-t)` for all `chi,x`.  Put `f(x)=sigma(x)-t`.
For all `chi`,
`alpha(chi)(f(x+y))=chi(x+y)=alpha(chi)(f(x)+f(y))`.
Surjectivity of `alpha` and character separation (`L-DUAL(a)`) give
`f(x+y)=f(x)+f(y)`.  Bijectivity makes `f in Aut(A)`.

`<1>4.` Conjugating the translations `X(a)` now shows that
`theta(x+a)theta(x)^(-1)` is a scalar times a character of `x`.  Its value at `x=0`
is `theta(a)`, so `B_theta(a,-)` is a character.  The defining expression is symmetric
in `(a,x)`; therefore it is a bicharacter and `theta` is a quadratic phase.

`<1>5.` Conversely, put `theta_a=chi B_theta(a,-)`.  Direct calculation gives

    T_(t,f,theta) W(a,chi) T_(t,f,theta)^(-1)
      =lambda(a,chi) W(f(a),theta_a o f^(-1)),
    lambda(a,chi)=theta(a)/(B_theta(a,a) theta_a(f^(-1)t)) in mu_N.

Thus every displayed `T` normalizes, proving the exact characterization.

`<1>6.` The induced transformations of `V_A` are exactly

    (a,chi) |-> (f(a),(chi B_theta(a,-)) o f^(-1)).

They preserve the modulation Lagrangian `{0}xA^vee`.  Translations and central
phases choose lifts but do not change this phase-space map.  This is the
precise affine-plus-quadratic subgroup surviving in strict monomial maps;
only symmetric bicharacters admitting a `mu_N`-valued quadratic refinement
occur.

`<1>7.` Define the unnormalized Fourier kernel

    F_A:C^A -> C^(A^vee),   F_A e_x=sum_(rho in A^vee)iota(rho(x))e_rho.

Every column has `|A|` nonzero entries.  Base extension of a strict pointed
map has at most one nonzero entry per column, so for `|A|>1`, no scalar
multiple of `F_A` comes from a strict map.

`<1>8.` Orthogonality gives `F_A^*F_A=|A|I`; the normalized Fourier map is
unitary.  With `ev_a(rho)=rho(a)`, direct evaluation gives

    F_A X(a)=Z(ev_a)F_A,
    F_A Z(chi)=X(chi^(-1))F_A,
    F_A W(a,chi)=iota(chi(a))W(chi^(-1),ev_a)F_A.

Thus it performs the canonical polarization exchange
`J_A(a,chi)=(chi^(-1),ev_a)` between `V_A` and `V_(A^vee)`, but requires a
weighted correspondence/additive kernel.  A self-Fourier endomorphism further
requires a named perfect pairing `A~=A^vee`.

`<1>9.` The map `J_A` preserves `kappa`: for `v=(a,chi)`, `w=(b,eta)`,
`kappa(J_Av,J_Aw)=eta(a)^(-1)chi(b)=kappa(v,w)`.  Put
`r_A(a,chi)=chi(a)`.  Since
`c_(A^vee)(J_Av,J_Aw)=chi(b)`, direct substitution gives
`r_A(v)r_A(w)c_(A^vee)(J_Av,J_Aw)=c_A(v,w)r_A(v+w)`.
Thus `(J_A,r_A)` is a morphism of the lifted groupoid used in §7, and the last
formula of `<1>8` is its exact Egorov scalar after realization.

`<1>10.` This obstruction concerns the strict cyclotomic pointed-set category.
It does not deny the ordinary complex Fourier/Weil operator, and it does not
select a canonical linear Weil splitting. **QED** (`F1-MON`, `PROVED`)

## 7. F1-CORR — the precisely typed algebraic extension

**Status: SKETCH.** This supporting argument replaces the original lane's
unformulated geometric existence clause; the blind critic's O1--O3 did
not admit that clause. D1007 now uses framed finite sets and explicitly
monoidal lifted phase isomorphisms. Its target is an additive envelope,
not a claimed category of F1 schemes.

**ASSUME** D1007. **PROVE** there is a projective strong symmetric monoidal
functor `Q_N:LiftHyp_N->PMat(K_N)` taking A to its basis set A and each
lift `(g,r)` to its projective Egorov intertwiner.

`<1>1.` The image of Q[mu_N] under a faithful complex character is
Q(zeta_N), a field: zeta_N is algebraic and its powers span a finite
extension of Q. Thus K_N is a field embedded in C. The Weyl matrices
of the framed S_A have entries in K_N.

`<1>2.` For a lift `(g,r)`, impose the homogeneous linear equations
`T W_A(v)=iota(r(v))W_B(gv)T` for all v, treating iota(r(v)) as its
class in K_N. The two systems are irreducible with the same central
character, so F1-REAL gives a one-dimensional complex solution space
spanned by an invertible matrix.

`<1>3.` Gaussian elimination over K_N has the same pivots after scalar
extension to C. The solution space over K_N therefore has dimension one
and contains a nonzero T. Its determinant is nonzero after embedding
in C, hence nonzero in K_N. This proves existence and uniqueness in PMat.

`<1>4.` Composition and tensor product of solution matrices satisfy
the equations for composed and tensored lifts, respectively. Uniqueness
over K_N implies all projective coherence diagrams commute. Identities
and swaps have their evident permutation solutions. This proves the
strong symmetric monoidal assertion for the tensor declared in D1007.

`<1>5.` The affine-quadratic and Fourier formulas in section 6 solve
the same equations, so Q_N has those values. Since T intertwines two
unitary irreducibles, T* T is a positive scalar. A positive real
normalization gives a unitary after complex realization; no square root
is asserted to belong to the original phase monoid or even to K_N.

`<1>6.` The geometric descent of this additive envelope is still a
research question. The theorem does not supply native superpositions,
a canonical lift for every symplectic map, or a Weil splitting.
**QED** (supporting SKETCH, not part of the promoted core)
