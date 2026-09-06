<!-- ROLE: the single source for numbered definitions (L4). Every definition
     lives here exactly once, as a "## Dn (short name)" heading. Theory shards,
     checkers and the labbook cite Dn and never redefine.
     A definition is a STIPULATION and needs no source. The moment it asserts a
     property (nondegeneracy, uniqueness, a dimension), that property is a CLAIM
     and belongs in claims/CLAIMS.md with evidence. -->

# Definitions

## Conventions governing this file

1. One numbered definition per heading, `## Dn (short descriptive name)`.
2. Numbers are never reused and never renumbered. A superseded definition is
   marked superseded in place, with a pointer to its replacement.
3. Every definition must be stated **uniformly in the characteristic** or must
   say explicitly which characteristics it excludes and why. Silently
   odd-characteristic conventions are the campaign's designated foot-gun: the
   symmetrized "half" convention `ω/2` does not exist at `p = 2`.
4. Every choice a definition depends on — a character, a root of unity, a
   polarization, an ordering, a basis — is named in the definition itself, not
   in a remark. The product word of this campaign is *canonical*; an unnamed
   choice makes it a lie.
5. Any commit changing this file updates the owning labbook section in the same
   commit (L11).

## D1 (the symplectic object of a finite field)

For a finite field `κ`, put `V(κ) := κ ⊕ κ` and define `ω : V(κ)×V(κ) → κ` by
`ω((a,b),(a',b')) := a b' − a' b`.
Stipulation only; that `ω` is `κ`-bilinear, satisfies `ω(v,v) = 0` and is
nondegenerate is claim `WH-FORM`. Uniform in the characteristic; `p = 2` is in
scope.

## D2 (admissible polarizing cocycles, and the choice of one)

`Adm(ω) := { β : V(κ)×V(κ) → κ  |  β is κ-bilinear and β − β^T = ω }`.
A *polarizing cocycle* is a choice of element `β ∈ Adm(ω)`, and it is a **datum
of the construction, on the same footing as the character `ψ` of D3** — not a
convention. `β₀((a,b),(a',b')) := a b'` is the *reference* cocycle: a label for
the torsor of D2, not a canonical point of it.
The symmetrized alternative `ω/2` lies in `Adm(ω)` at odd `p` only, and is
unavailable at `p = 2`; that `Adm(ω)` is a torsor of size `q³`, that `ω/2` is
its unique antisymmetric point at odd `p`, and that at `p = 2` it splits into
two isomorphism types are claims `WH-BETA-a`, `-b`, `-c`.

## D3 (the phase datum, and the two choices it hides)

A *phase datum* for `κ` is an additive character `ψ : (κ,+) → C^×` with `ψ ≢ 1`.
Write `X(κ)` for the set of such `ψ`.
The *trace-normalized family*: `Tr_{κ/F_p}(z) := z + z^p + ⋯ + z^{p^{m−1}}` for
`κ = F_{p^m}`, and `ψ_ζ := ζ^{Tr_{κ/F_p}(·)}` for `ζ` a primitive `p`-th root of
unity in `C`.
**Two named choices:** `ψ` itself, and — inside the distinguished family — `ζ`.
Neither is canonical and neither is ever suppressed. `Tr_{κ/F_p}` is canonical.

## D4 (Weyl operators and the observable algebra)

For `ψ` as in D3 and `β ∈ Adm(ω)` as in D2,
`A_{ψ,β}(V) := ⨁_{v ∈ V(κ)} C·W_β(v)` with product fixed on basis elements by
`W_β(v)W_β(v') := ψ(β(v,v')) W_β(v+v')`.
This ordering is fixed once. Depends on `κ`, `ψ` and `β`, and on nothing else.

## D5 (the Heisenberg group of a polarizing cocycle)

`H_β(κ) := κ × V(κ)` with `(t,v)(t',v') := (t + t' + β(v,v'), v + v')`.
It uses no character; it does depend on `β`, and at `p = 2` its isomorphism
class does (claim `WH-BETA-f`). `A_{ψ,β}(V)` is its group algebra with the
centre set to `ψ`.

## D6 (the quadratic form of a polarizing cocycle)

`Q_β : V(κ) → κ`, `Q_β(v) := β(v,v)`; for the reference cocycle,
`Q_{β₀}(a,b) = ab`.
Identically zero under any symmetrized convention, and not zero here; at `p = 2`
it is the object that separates the members of `Adm(ω)`.

## D7 (the Weyl frame and two automorphism groups)

The *Weyl frame* is `F := { C^×·W_β(v) : v ∈ V(κ) } ⊂ A_{ψ,β}(V)`.
`Aut_F(A)` is the group of `C`-algebra automorphisms `α` with `α(F) = F`.
`Aut_F^κ(A) ⊆ Aut_F(A)` is the subgroup whose induced permutation of `V(κ)` is
`κ`-linear. The `κ`-linearity is **imposed data**: the algebra and its frame are
built from `(V,+)` and `ψ∘β` alone and do not carry the `κ`-module structure
(claim `WH-SYMM`).

## D8 (Schrödinger models, and the standard model)

For a `κ`-line `L ⊂ V(κ)` put `A_L := span_C{ W_β(l) : l ∈ L }`. Given a unital
`C`-algebra character `χ : A_L → C`, the *Schrödinger model* of `(L,χ)` is
`M_{L,χ} := A_{ψ,β}(V) ⊗_{A_L} C_χ`.
The *standard model* (for `β = β₀`) is `M₀ := ⨁_{y ∈ κ} C·e_y` with `{e_y}`
declared orthonormal and

    W(a,b) e_y := ψ(−b(y+a)) e_{y+a},   i.e.   W(a,b) = Z(−b)X(a),

where `X(a)e_y := e_{y+a}` and `Z(b)e_y := ψ(by)e_y`. **This is a stipulation.**
The sign is not cosmetic: the naive `Z(b)X(a)` realizes the cocycle `−ab'`, and
the discrepancy is invisible at `p = 2`. That `M₀` satisfies D4 is checked by
gate `C11` of `theory/checks/wh_kappa_check.py` and derived at `WH-SVN`.

## D9 (the model groupoid)

`Mod_{ψ,β}(κ)` is the category whose objects are pairs `(M,π)` with
`π : A_{ψ,β}(V) → End_C(M)` a unital algebra map making `M` a simple module and
every `π(W_β(v))` unitary, and whose morphisms are unitary intertwiners.
`PMod_{ψ,β}(κ)` is the same category with `Hom` replaced by `Hom/U(1)`.

## D10 (Artin–Schreier map, and the type of a polarizing cocycle)

`℘ : κ → κ`, `℘(x) := x² + x`. **[p = 2]** the *type* of `β ∈ Adm(ω)` is
`Arf(Q_β) := Q_β(e)·Q_β(f) ∈ κ/℘(κ)` computed in any symplectic `κ`-basis
`(e,f)` of `V(κ)` (`ω(e,f) = 1`). That this is independent of the basis, that
`κ/℘(κ)` has exactly two elements, and that both types occur are claims
`WH-BETA-e`, `-f`.

## D11 (the level-`μ_p` frame)

`F^{(p)}_{ψ,β} := { ζ^j W_β(v) : j ∈ Z/p, v ∈ V(κ) } ⊂ A_{ψ,β}(V)^×`, the finite
group of Weyl unitaries with phases in `μ_p = ψ(κ)`.
Recorded separately from `F` (D7) because the two behave differently: claim
`WH-BETA-h` says `(A,F)` does not depend on `β` while `F^{(p)}` does, at `p = 2`.

## D12 (finite commutative local ring datum)

A *finite local ring datum* is `(R,𝔪,κ,q)` with `R` a finite commutative
unital local ring with `1≠0`, `𝔪` its unique maximal ideal, `κ:=R/𝔪`, and
`q:=|κ|`; write `R^×` for its unit group.
For an ideal `I⊆R`, put `Ann(I):={r∈R:rI=0}` and
`soc(R):=Ann(𝔪)`.  These are stipulations.  Nilpotence of `𝔪`, nonvanishing of
the socle, and the other finite-local structure properties are established in
`FCR-GEN`, not assumed here.  Uniform in the residue characteristic.

## D13 (characters and generating characters of a finite local ring)

Let `R̂:=Hom((R,+),C^×)` and `X(R):=R̂∖{1}`.  For `ψ∈X(R)` and `u∈R`, put
`ψ_u(x):=ψ(ux)`.  Define
`I_ψ:=Σ{I⊆R : I is an ideal and I⊆ker ψ}`, the largest ideal contained in
`ker ψ`, and `Gen(R):={ψ∈X(R):I_ψ=0}`.  A member of `Gen(R)` is a
*generating character*.  Uniform in the residue characteristic; existence is
not stipulated and is claim `FCR-GEN`.

## D14 (the symplectic object and phase perpendicularity over a local ring)

For D12 put `V(R):=R⊕R` and
`ω((a,b),(a',b')):=ab'−a'b`.  Given `ψ∈X(R)`, write
`B_ψ(v,w):=ψ(ω(v,w))` and, for an `R`-submodule `L⊆V(R)`,
`L^{⊥_ψ}:={v∈V(R):B_ψ(v,l)=1 for every l∈L}`.  A *Lagrangian* is an
`R`-submodule with `L=L^{⊥_ψ}`; put `rad(B_ψ):=V(R)^{⊥_ψ}`.  R-bilinearity,
strong alternation,
R-nondegeneracy of `ω`, and nondegeneracy of `B_ψ` are claims, not
stipulations; `B_ψ`, not R-nondegeneracy alone, is the load-bearing pairing.
Uniform in the residue characteristic.

## D15 (admissible polarizing cocycles over a local ring)

For D14,
`Adm(ω):={β:V(R)×V(R)→R | β is R-bilinear and β−β^T=ω}`.
Put `Sym_R(V(R)):= {s:V(R)×V(R)→R | s is R-bilinear and s=s^T}`.
A *polarizing cocycle* is a named choice `β∈Adm(ω)`.  The reference member is
`β₀((a,b),(a',b')):=ab'`.  This is the non-symmetrized convention: no inverse
of `2` is assumed.  Uniform in the residue characteristic.

## D16 (Weyl algebra, Heisenberg group, and local Schrödinger models)

For D12--D15 define
`A_{ψ,β}(V(R)):=⨁_{v∈V(R)}C·W_β(v)` by
`W_β(v)W_β(v'):=ψ(β(v,v'))W_β(v+v')`, and define
`H_β(R):=R×V(R)` by
`(t,v)(t',v'):=(t+t'+β(v,v'),v+v')`.
For an `R`-submodule `L` put
`A_L:=span_C{W_β(l):l∈L}`; given a unital algebra character
`χ:A_L→C`, put `M_{L,χ}:=A_{ψ,β}(V(R))⊗_{A_L}C_χ`.

The fixed reference model is `ℓ²(R)=⨁_{y∈R}C·e_y`, with `{e_y}` declared
orthonormal,
`X(a)e_y:=e_{y+a}`, `Z(b)e_y:=ψ(by)e_y`, and, exactly,

    W_{β₀}(a,b):=Z(−b)X(a),
    W_{β₀}(a,b)e_y=ψ(−b(y+a))e_{y+a}.

The sign and ordering are stipulations inherited from D8's E1 resolution.
Every formula in D16 is uniform in the residue characteristic and uses no
half.

<!-- F1 sidequest definitions; D17–D999 remain available to mainline work. -->

## D1001 (finite free cyclotomic F1 modules and complex realization)

Fix `N>=1`, an abstract cyclic group `mu_N` of order `N`, and a named faithful
character `iota:mu_N->C^x`.  Let `Free_*^{mu_N}` be the category of finite
pointed sets carrying a `mu_N`-action which fixes the basepoint and is free on
its complement; morphisms are pointed equivariant maps.  Define cyclotomic
complex realization by
`C_iota(S):=C[S]/(e_0, e_{us}-iota(u)e_s)` and by the induced linear maps.
The embedding `iota` is part of the realization datum, not a canonical choice.

## D1002 (finite hyperbolic cyclotomic phase datum)

A finite hyperbolic phase datum at level `N` is a finite abelian group `A` with
`exp(A)|N`, together with
`A^vee:=Hom(A,mu_N)`, `V_A:=A x A^vee`,
`c_A((a,chi),(b,eta)):=eta(a)^(-1)`, and
`kappa_A((a,chi),(b,eta)):=chi(b)eta(a)^(-1)`.
That `|A^vee|=|A|`, that `c_A` is a cocycle, and that `kappa_A` is perfect are
claims `F1-DUAL` and `F1-WEYL`, not clauses of the definition.

## D1003 (cyclotomic phase monoid and pointed Schrodinger module)

For D1002 put `H_N(A):=mu_N x V_A` with
`(u,v)(u',w):=(uu'c_A(v,w),v+w)`, and let `H_N(A)^0` be this set with an
absorbing zero adjoined.  Put
`S_A:={0} disjoint-union (mu_N x A)` and stipulate

    (u,a,chi)[z,x]:=[uz chi(x+a),x+a],    0_H s:=0_S.

On `C_iota(S_A)` put
`X(a)e_x:=e_{x+a}`, `Z(chi)e_x:=iota(chi(x))e_x`, and
`W(a,chi):=Z(chi)X(a)`.  The action law, faithfulness, exact Weyl relation,
and algebraic consequences are claims `F1-WEYL` and `F1-REAL`.

## D1004 (fixed-level isomorphisms and tensor products)

Let `FinAb_N^iso` be the groupoid of finite abelian groups of exponent dividing
`N` and group isomorphisms.  For `f:A->B`, define
`f_*chi:=chi o f^(-1)`, `S(f)[u,x]:=[u,f(x)]`, and
`H(f)(u,a,chi):=(u,f(a),f_*chi)`.
For pointed `mu_N`-sets define
`S smash_mu T:=(S smash T)/([us,t]~[s,ut])`.  For cyclotomic phase groups
define the central product
`H boxdot K:=(H x K)/{((u,1),(u^(-1),1)):u in mu_N}`.
Functoriality and the strong symmetric monoidal comparison with direct products
in `FinAb_N^iso` are claim `F1-FUNCT`.

## D1005 (central pushout comparison with a finite ring)

Let `R` be a finite commutative local ring datum D12 and let a named additive
character `psi:(R,+)->mu_N` satisfy `iota o psi in Gen(R)` and
`exp(R,+)|N`.  Put
`chi_b(x):=psi(-bx)` and define

    P_psi:=(mu_N x H_beta0(R))
           /{(psi(t)^(-1),(t,0,0)):t in R},

the central pushout of D16's raw reference Heisenberg group along `psi`.
Perfect duality, the comparison with `H_N((R,+))`, and recovery of D8/D16 are
claim `F1-RING`.

## D1006 (strict cyclotomic normalizer and Fourier kernel)

A *quadratic phase* is a map `theta:A->mu_N` with `theta(0)=1` for which
`B_theta(a,x):=theta(a+x)theta(a)^(-1)theta(x)^(-1)` is a bicharacter.  Put
`T_(t,f,theta)[u,x]:=[u theta(x),f(x)+t]` for `t in A`, `f in Aut(A)`.  The *strict
cyclotomic normalizer* is the normalizer of the D1003 `mu_N`-level Weyl group
inside `Aut_{Free_*^{mu_N}}(S_A)`.  Define

    F_A e_x:=sum_(rho in A^vee)iota(rho(x))e_rho,
    ev_a(rho):=rho(a),
    J_A(a,chi):=(chi^(-1),ev_a) in V_(A^vee),
    r_A(a,chi):=chi(a).

The exact normalizer, Fourier covariance, and failure of strict realization
are claim `F1-MON`.

## D1007 (framed cyclotomic kernels and lifted phase isomorphisms)

Fix the data of D1001. Put `K_N=Q[mu_N]/ker(iota)` where `iota` is extended
linearly to the rational group ring. Let `Mat(K_N)` have finite sets `I` as
objects and `J x I` matrices over `K_N` as morphisms `I->J`; composition is
matrix multiplication, tensor on objects is Cartesian product and on maps
is Kronecker product. The associated free pointed module is the **framed**
object `S_I={0} disjoint-union(mu_N x I)` with sections `[1,i]`. Write
`PMat(K_N)` for the groupoid of invertible matrices modulo `K_N^x`.
Complex realization applies `iota` to entries. This is an additive
cyclotomic envelope; it is not stipulated to be a category of F1 schemes.

Let `LiftHyp_N` have the configurations of D1002 as objects. An arrow
`A->B` is a pair `(g,r)` where `g:V_A->V_B` is a group isomorphism preserving
`kappa` and `r:V_A->mu_N` satisfies
`r(v)r(w)c_B(gv,gw)=c_A(v,w)r(v+w)`. It denotes the centre-fixing map
`(u,v)->(u r(v),g(v))`; composition composes these maps. Tensor is `A x B`
on objects and `(g x h, (v,w)->r(v)s(w))` on arrows, using the canonical
reordering `V_(A x B)=V_A x V_B`. The unit is `A=0` and symmetry interchanges
factors. No lift of an arbitrary symplectic map is assumed to exist.

## D1008 (upper-unitriangular Heisenberg crowd over bands)

A band `B` means a commutative pointed multiplicative monoid with a null
ideal `N_B` in the semiring of formal sums of nonzero elements, such that
each `a` has a unique `-a` with `a+(-a) in N_B`. Morphisms preserve the
pointed monoid and null sums. Use the regular partial field `F_1^pm={0,1,-1}`
with null sums those vanishing in `Z`, and the Krasner hyperfield `K={0,1}`
with null sums containing either zero or at least two nonzero terms.

Put `H_crowd(B)=B^3`, with identity `(0,0,0)`, represented by
`h(a,b,t)=[[1,a,t],[0,1,b],[0,0,1]]`. Its ternary relation `R_H(B)` consists
of triples `(h_1,h_2,h_3)` for which `sum a_i`, `sum b_i`, and the three
cyclic versions of
`t_1+t_2+t_3+a_1 b_2+a_1 b_3+a_2 b_3` belong to `N_B`.
Its inverse set is `h^(-1)={k:(h,k,1) in R_H}` and its product set is
`h*k={c:there exists d with (h,k,d),(c,d,1) in R_H}`.
Crowd axioms, representability and ring realization are claim `F1-CROWD`.

## D1009 (absolute projective frames and their product-state map)

For D1001 put `F_N={0} disjoint-union mu_N`, with absorbing zero. For
`r>=1` define the Cartesian frame `F_N^r` and its projective nonzero state
set `P_N(r)=(F_N^r\{(0,...,0)})/mu_N`, using simultaneous multiplication
of all coordinates. This is a different object from a free pointed module.
Define `P_N(r) x P_N(s)->P_N(rs)` by the coordinate products
`([x],[y])->[(x_i y_j)_(i,j)]`. Its image consists of *product rays*;
the remaining rays are *nonproduct rays* in this factorization sense.
No Born probability rule or total Hermitian form is stipulated.

## D1010 (normal pointed maps, Hall algebra and algebraic Fock realization)

Let `V_r={*,1,...,r}` for `r>=0`. A normal pointed map sends `*` to `*`
and has at most one preimage for every non-basepoint; equivalently it is
a partial injection of the nonzero sets. Wedge identifies basepoints;
smash collapses all pairs with a basepoint in the Cartesian product.
Let `L(S)=C[S\{*}]`, with its displayed basis orthonormal, and let `B(S)`
be the complex span of the realized normal endomorphisms in `End_C(L(S))`.

The rational Hall vector space has basis `u_r` and product given by
counting pointed subsets `T` with specified `T` and `S/T` isomorphism
classes. Define the algebraic Fock domain `F_alg=C[x]` with
`<x^m,x^n>=delta_mn n!`, creation `a^dagger f=xf`, annihilation `a f=df/dx`.
Its Hilbert completion is denoted `F_bos`. The Hall formula, adjointness
on `F_alg`, and the CCR are claim `F1-HALL`; no bounded CCR is stipulated.

## D1011 (categorical phase system and matching central-character product)

For D1002--D1003 let `C_N(A)=Rep_C(H_N(A))`, the category of finite-dimensional
complex representations and all linear intertwiners. Its internal tensor
is the usual tensor with diagonal group action. Let `C_N(A)_lambda` be
the full subcategory on which central `u in mu_N` acts as `lambda(u)I`.
The unitary version uses invariant Hermitian inner products and the same
linear intertwining spaces. Write `omega_A` for the forgetful tensor functor.

For groups `H,K` with specified central `mu_N`, let
`Rep(H) boxtimes_match Rep(K)` be the full subcategory of `Rep(H x K)`
on which every `(u,u^(-1))` acts trivially. This is an explicit kernel
condition, not an unspecified relative tensor product. The central-product
comparison and grading are claim `F1-CAT`.

## D1012 (the two order-eight qubit groups and their indicators)

For `e in {0,1}` let `G_e` have underlying `F_2^3` and product
`(t,a,b)(u,c,d)=(t+u+ad+e(ac+bd),a+c,b+d)`, all coordinates in `F_2`.
Let `sigma_e(t,a,b)=(-1)^t i^(e(a+b)) Z^b X^a`, where
`X=[[0,1],[1,0]]` and `Z=[[1,0],[0,-1]]`. In the exponent of `i`,
`a,b` are their representatives in `{0,1}`. Define its indicator by
`nu_2(sigma_e)=|G_e|^(-1) sum_g Tr(sigma_e(g^2))`.
The identifications `G_0=D_8` (order eight) and `G_1=Q_8`, irreducibility,
fusion rules and indicators are claim `F1-FUSION`.

## D1013 (one-pair quantum torus and a selected central fibre)

Fix `xi in C^x`. Define `T_xi=C<U^(+-1),V^(+-1)>/(VU-xi UV)`.
If `xi` is a named primitive `N`th root, define the selected central
fibre `T_xi(1,1)=T_xi/(U^N-1,V^N-1)`. No limit identification between
the parameter `xi`, phase level `N`, and a finite-field cardinality is
stipulated. Its clock/shift realization is claim `F1-TORUS`.
