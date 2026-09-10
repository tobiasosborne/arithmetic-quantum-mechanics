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

<!-- Operational F1 subsystem category: 2026-09-07 increment. -->

## D1101 (positive type-A Hecke systems and their coefficient traces)

Fix a real parameter `q>0`.  Put `H_0(q)=H_1(q)=C`.  For `n>=2`, let
`H_n(q)` be the unital complex algebra generated by `T_1,...,T_{n-1}` with

    (T_i-q)(T_i+1)=0,
    T_i T_{i+1} T_i=T_{i+1} T_i T_{i+1},
    T_i T_j=T_j T_i when |i-j|>1,

and involution `T_i^*=T_i`.  For `w in S_n`, write `T_w` for the product
along a reduced expression; independence of that expression and the basis
property are claim `F1-HCK-POS`.  Define the coefficient functional by
`tau_n(T_w)=delta_(w,e)`.  Positivity, traciality, faithfulness, and the
resulting C*-algebra structure are also claim `F1-HCK-POS`, not clauses of
this definition.

## D1102 (ordered parabolic assembly and coarse graining)

For `m,n>=0`, identify `S_m x S_n` with the permutations of
`{1,...,m+n}` preserving the two contiguous ordered blocks.  On standard
basis symbols put

    iota_(m,n)(T_u tensor T_v)=T_(u x v),
    E_(m,n)(T_w)=[w in S_m x S_n] T_w.

Here the right-hand `T_w` in the expectation is viewed in the parabolic
subalgebra and then identified with `H_m(q) tensor H_n(q)`.  These are
*ordered* structure maps.  Homomorphism, injectivity, trace preservation,
complete positivity, conditional-expectation properties, and coherence are
claim `F1-HCK-TOWER`.  No block-swap or symmetric structure is stipulated.

## D1103 (the unlabelled level-three overlap invariant)

Suppose a finite C*-algebra `C` has a unique noncommutative simple summand
isomorphic to `M_2(C)`, and contains two specified unital subalgebras
`B_1,B_2`, each isomorphic to `C^2`.  Compress the two unordered pairs of
minimal projections of `B_1,B_2` to the `M_2` summand.  When all four
compressions are rank-one projections, define

    a(C;B_1,B_2):=min { Tr_2(PQ) :
                         P from B_1, Q from B_2 }.

`Tr_2` is the ordinary unnormalized matrix trace.  For the diagram
`H_2(q) -> H_3(q) <- H_2(q)` use the left and right standard parabolics.
Existence and the formula `a=q/(q+1)^2` are claim `F1-HCK-LOW`.

## D1104 (complete-flag context algebra)

Let `k=F_Q` be a named finite field of prime-power order `Q`, let `L` be an
`n`-dimensional `k`-vector space, and let `Fl(L)` be its set of complete
flags `0=U_0<U_1<...<U_n=L`, `dim_k U_i=i`. Label relative positions by
reduced gallery words in the order used for the adjacency products. Put

    Cxt(L):=End_(GL(L))(ell^2(Fl(L))).

For `w in S_n`, define the relative-position adjacency operator

    (A_w f)(F):=sum_(F': pos(F,F')=w) f(F').

The normalized flag trace is
`tr_Fl(x):=|Fl(L)|^(-1) Tr_(ell^2(Fl(L)))(x)`.  The identification with
`H_n(Q)` is claim `F1-HCK-FLAG`.

If a finite Weyl--Heisenberg system has a named polarization
`V=L direct-sum L^vee`, call `Cxt(L)` its *complete-flag context algebra*.
This terminology records dependence on the chosen Lagrangian `L`; it does not
identify `Cxt(L)` with the full Weyl observable algebra.

## D1105 (marked level-two Hecke parameter)

In `H_2(q)` put `e_triv=(T_1+1)/(q+1)`, the spectral projection on which
`T_1` has eigenvalue `q`, and define the marked scalar
`r_2:=tau_2(e_triv)`.  Recovery of `q`, and the reciprocal ambiguity when the
two minimal projections are left unlabelled, are claim `F1-HCK-Q`.

## D1106 (operational states and processes of a traced Hecke level)

For D1101, a state is a positive functional `omega:H_n(q)->C` with
`omega(1)=1`, or its coefficient-trace density `h>=0`, `tau_n(h)=1`,
`omega(a)=tau_n(ha)`. An effect satisfies `0<=e<=1`, with probability
`tau_n(he)`. A deterministic Heisenberg channel is unital and completely
positive; an outcome map is subunital CP, and an instrument has a unital
sum. Define the ordered product preparation of two local densities by
`iota_(m,n)(h tensor k)`.

A local Kraus list in `H_n(q)` satisfies `sum_i K_i^*K_i=1`; its
Heisenberg action is `a->sum_i K_i^*aK_i` and its density action is
`h->sum_i K_i h K_i^*`. In an ordered ambient block, retain and embed
its operators using D1102 before applying this rule. Isolated equality
of CP maps is not stipulated to be an assembly congruence.

## D1121 (finite categorical subsystem net)


A finite categorical subsystem
datum is a unitary fusion category `C`, with its positive spherical structure,
together with a tensor-closed replete family `S` of **nonzero** objects
containing the unit. Thus every `d_X>0`; zero morphisms remain allowed.  It assigns

    A_X := End_C(X),
    Tr_X(f) := the positive categorical trace of f,
    tau_X := Tr_X/d_X,
    j_X,Y(f tensor g) := f tensor g in A_(X tensor Y).

Associators are retained as comparison maps rather than suppressed as equalities.
For every assembly inclusion `j_X,Y`, `E_X,Y` denotes the `tau_(X tensor Y)`-
preserving conditional expectation onto its image.  The datum includes all
iterated inclusions and expectations, related by associator conjugacy and the
tower law for nested inclusions.

## D1122 (operational realisation of D1121)

For `X` in D1121's nonzero family, a state is either a
normalised positive functional `omega:A_X -> C`, or its unique density
`rho>=0` satisfying `Tr_X(rho)=1` and `omega(a)=Tr_X(rho a)`.  An effect is
`0<=e<=1`; its Born probability is `omega(e)`.  Restriction from a composite
to an assembly subalgebra sends `rho` to `E_X,Y(rho)`.  Preparation sends a
density `sigma` on `A_X tensor A_Y` to `j_X,Y(sigma)`; equivalently, the
prepared functional is `omega_sigma o E_X,Y`.

## D1123 (context-complete categorical Kraus process)

For nonzero `X,Y` in the family of D1121, a Kraus process
`K:X->Y` is a finite list of category morphisms `K_i:X->Y` such that
`sum_i K_i^* K_i=1_X`.  Lists are identified only under stable scalar-unitary
mixing: pad two lists by zero morphisms to a common length and apply one
ordinary unitary matrix to the Kraus index.  Its isolated Heisenberg shadow and
Schrodinger action are

    Phi_K(a) = sum_i K_i^* a K_i,       a in A_Y,
    T_K(rho) = sum_i K_i rho K_i^*,     rho in A_X.

Its right-context action is retained as data:

    Phi_K^Z(a) = sum_i (K_i^* tensor 1_Z) a (K_i tensor 1_Z),
                 a in A_(Y tensor Z).

Composition is the list `(L_j K_i)_(j,i)` and tensor product is
`(K_i tensor L_j)_(i,j)`, with the category associators.  This is a sufficient
process class; it is not stipulated to contain every CP map between `A_X` and
`A_Y`.

## D1124 (charge-carrying dilation process)

A dilation between nonzero objects `X->Y` is a named
nonzero environment `E` and an isometry `v:X->Y tensor E`.  It induces

    Phi_v(a)=v^*(a tensor 1_E)v.

Sequential composition is always defined and retains the ordered environment.
Parallel composition is defined when the environment can be moved past the
other output by named unitary interchange data: in particular in a braided
unitary fusion category, or when the environment has a specified half-braiding.
No parallel product for arbitrary charge-carrying environments is stipulated
in a merely monoidal category.

## D1125 (finite-injection symmetric-group quantum net)

For a finite set
`S`, put

    G(S)=Sym(S),              A(S)=C[G(S)],
    (sum a_g g)^*=sum conjugate(a_g) g^(-1),
    tau_S(sum a_g g)=a_1.

For an injection `f:S->T`, extend permutations of `S` by the identity off
`f(S)` to obtain `i_f:A(S)->A(T)`.  Let `E_f` delete coefficients outside
`i_f(G(S))` and identify the remaining subgroup algebra with `A(S)`.  Disjoint
union gives `mu_S,T:A(S) tensor A(T)->A(S disjoint-union T)` by block
permutations.  A local process is a stably unitary-equivalent finite list
`K_i in A(S)` with `sum K_i^*K_i=1`; its action in an ambient injection
`f:S->T` uses the retained list `i_f(K_i)`.  This construction is a proposed
operational `q=1` fibre, not a uniqueness claim about quantum mechanics over
`F_1`.

## D1126 (Kraus Gram and contextual equivalence)

For D1125, fix `|S|=n>=1`, put `H=Sym(S)`, and take normalized local lists.
Write `K_i=sum_(h in H) a_i(h)h`.  Its Kraus Gram is

    J_K(h,k)=sum_i a_i(h) conjugate(a_i(k)),       h,k in H.

Two lists are *contextually equivalent* when, after every finite injection
`f:S->T`, their Heisenberg channels agree on all of `C[Sym(T)]`:

    Phi_(K,f)(x)=sum_i i_f(K_i)^* x i_f(K_i).


Stable scalar-unitary equivalence means padding both lists by zeros to a common
length and applying one complex unitary matrix to the Kraus index, as in D1125.
An admissible Gram is a positive semidefinite matrix `J in M_H(C)` satisfying

    sum_(h in H) J(hx,h)=delta_(x,1)       for every x in H.

## D1127 (partial-injection operational realisation)

Let `FinPInj` have finite sets and partial injections.  Write
`f:S partial->T` as a bijection `f:D->E` between `D subset S` and `E subset T`.
For the D1125 net define

    R(f)=i_(E subset T) o A(f:D isomorphic E) o E_(D subset S)
         : A(S) -> A(T).

Inclusions use extension by the identity; `E` is subgroup coefficient
expectation.  The target category has finite tracial C*-algebras and unital,
trace-preserving CP maps, with trace adjoint as dagger.

For the group net D1125--D1127, densities use the normalized coefficient
trace: `h>=0`, `tau_S(h)=1`, `omega_h(a)=tau_S(ha)`. This differs from
D1122's use of an unnormalized categorical trace.

## D1141 (partial-flag Hecke category)

For D1101, a composition `alpha=(alpha_1,...,alpha_r)` of `n` has positive
integer parts summing to `n`; include the empty composition of zero. Let
`W_alpha<=S_n` preserve the consecutive blocks of those sizes, and put
`P_alpha(q)=sum_(w in W_alpha)q^ell(w)` and
`e_alpha(q)=P_alpha(q)^(-1) sum_(w in W_alpha)T_w`.

The category `Gamma_q` has these compositions as objects, morphisms
`Gamma_q(alpha,beta)=e_beta H_n(q)e_alpha` for equal totals and the zero
vector space for different totals, identity `e_alpha`, adjoint `*`, and
composition by multiplication. Tensor is concatenation on objects and
`iota_(m,n)` on morphisms. Let `x=(1)` be the distinguished generator.
Use finite formal direct sums and split self-adjoint idempotents when the
additive idempotent completion is invoked. Only nonzero objects/projections
are used as systems with normalized states. Rigidity is not stipulated.

The generic version uses the based Hecke algebra over
`Z[t,t^(-1),{P_alpha(t)^(-1)}_alpha]`; evaluation at a positive real `q`
sets `t=q`. The localized coefficients are part of the construction.

For a finite field `F_Q` and `L=F_Q^n`, let `Fl_alpha(L)` be flags whose
successive quotient dimensions are the parts of `alpha`. If `r_alpha`
forgets steps from complete flags, define
`J_alpha e_E=P_alpha(Q)^(-1/2) sum_(F:r_alpha(F)=E)e_F`.
The normalized corner trace is `tau_alpha=P_alpha(q) tau_n` on
`e_alpha H_n(q)e_alpha`. A normalized Kraus family
`v_j in e_beta H_n(q)e_alpha` means `sum_j v_j^*v_j=e_alpha` and acts
in Heisenberg form by `a -> sum_j v_j^* a v_j`. No unscaled density
transport between differently normalized corners is stipulated.

## D1142 (Weyl constraint flags and controlled context coupling)

Fix a finite field `k=F_Q` of characteristic `p`, an `n`-dimensional
configuration space `L` (the named Lagrangian), and a nontrivial additive
character `psi:k->U(1)`. The Weyl Hilbert space is `C[L]` with basis `e_x`.
For additive characters `chi:L->U(1)`, put
`X(u)e_x=e_(x+u)` and `Z(chi)e_x=chi(x)e_x`; the k-linear dual is identified
with these characters via the named `psi`. For a k-subspace `U<=L`, let
`U^ann={chi:chi|_U=1}` and set
`P_U^X=|U|^(-1)sum_(u in U)X(u)` and
`P_U^Z=|U^ann|^(-1)sum_(chi in U^ann)Z(chi)`.

On `K_ctx(L)=C[Fl(L)]`, take the flag basis `e_F` orthonormal. For a full
flag `F=(U_i(F))`, define on `K_ctx(L) tensor C[L]`
`C_i=sum_F |e_F><e_F| tensor P_(U_i(F))^Z`.
The operator `R(g)e_x=e_(gx)` for `g in GL(L)` is the configuration
permutation unitary; the same group permutes flags. This construction
retains the field, the chosen Lagrangian and its origin, and the phase
datum; it does not identify `K_ctx(L)` with `C[L]`.

## D1143 (a Bell state on two collective three-constituent sectors)

In `C[S_3]` let `s=(12)`, `t=(23)`, and
`z=(2*1-(123)-(132))/3`. Put `Z_*=zs`,
`X_num=z(s+2t)` and `Y_anti=z(st-ts)`. With the block inclusion
`mu:C[S_3] tensor C[S_3]->C[S_6]`, define
`P_Bell=(1/4)mu(z tensor z+Z_* tensor Z_*`
`+(X_num tensor X_num+Y_anti tensor Y_anti)/3)` and `h_Bell=9P_Bell`.
The coefficient trace is D1125's `tau_6`. On the standard block the
normalized observables are `Z_*` and `X_*=X_num/sqrt(3)`.
Projection, density normalization, marginals and Bell correlations are
claim `F1-OP-BELL`, not stipulations.

## D1144 (apartment comparison of arithmetic and q=1 context algebras)

For D1104 choose an ordered basis of `L=F_Q^n`. Its coordinate complete
flags are indexed by permutations. Let `J_ap:C[S_n]->C[Fl(L)]` send each
orthonormal permutation basis vector to its coordinate-flag basis vector,
with the regular-action convention fixed by the gallery order in D1104.
Put `Omega_Q(x)=J_ap^* x J_ap` for `x in Cxt(L)`. Its range is to be
identified with the regular image of `C[S_n]`. Independence of the chosen
basis, complete positivity, trace compatibility and limits of multiplicative
or refinement compatibility are claim `F1-OP-APART`.


<!-- Operational categorical limit, admitted after capped review, 2026-09-08. -->

## D1201 (normalized regular Hecke frame)

For D1101 and `q>0`, put

    b_w(q)=q^(-ell(w)/2)T_w(q),       w in S_n.

Use `b_w(q)` as the orthonormal basis of `L^2(H_n(q),tau_(n,q))`, identify
that Hilbert space with the fixed `K_n=ell^2(S_n)`, and write `B_w(q)` for
left multiplication by `b_w(q)` on `K_n`.  This is a choice of continuous
regular frame, not a claim that the generators are independent of `q`.

## D1202 (continuous positive Hecke section algebra)

For a compact interval `I subset (0,infinity)`, define

    H_n^cts(I)
      ={q |-> sum_(w in S_n) f_w(q)B_w(q): f_w in C(I)}
      subset C(I,End(K_n)).

It has pointwise operations and the supremum operator norm.  Define the
`C(I)`-valued coefficient trace by
`tau_n^cts(x)(q)=tau_(n,q)(x(q))`.  Closedness, the C*-property, faithful
fibre positivity, and surjectivity of evaluation are claim `F1-LIM-CTS`.

## D1203 (continuous parabolic corner category)

For D1141 and D1202, `Gamma_I^cts` has compositions as objects and

    Hom(alpha,beta)=e_beta H_n^cts(I)e_alpha

when `|alpha|=|beta|=n`, with zero Hom spaces between different totals.
Identity, composition, and adjoint are `e_alpha`, pointwise multiplication,
and pointwise star.  Ordered tensor is composition concatenation on objects.
On section algebras its domain is the `C(I)`-balanced tensor product

    H_m^cts(I) tensor_(C(I)) H_n^cts(I),

equivalently the section algebra of the pointwise fibre tensor products, and
its map is D1102's contiguous-block map.  Its normalized trace is

    tau_alpha,q=P_alpha(q)tau_(n,q)

on the endomorphism corner.  Write `A_alpha(I)` for that continuous
endomorphism algebra and `A_alpha(q)` for its fibre.

## D1204 (the positive Hecke corner germ at one)

Let `I_epsilon=[1-epsilon,1+epsilon]`, `0<epsilon<1`.  Define
`Gamma_1^germ` as the filtered germ category of the `Gamma_Iepsilon^cts`:
two section morphisms are equal when their restrictions agree on a smaller
endpoint interval.  Operations descend by restriction.  A positive germ is
one having a positive representative on one interval.  Only evaluation at
one is canonical on this germ category.  It is an ordered monoidal
star-category locally represented by C*-categories; no canonical C*-norm on
the germ Hom spaces is stipulated.

## D1205 (corner atoms and separated register words)

For each nonempty composition `alpha`, let `[alpha]` be the quantum atom with
observable algebra `A_alpha(q)` and reference trace `tau_alpha,q`.  A register
word is a finite ordered word `[alpha_1]...[alpha_r]`, with observable algebra
the spatial tensor product of the atom algebras and reference trace their
product.  The empty word has algebra `C`.

For a nonempty finite set `O`, the classical wire `underline(O)` has algebra
`C^O` and uniform reference trace
`tau_O(f)=|O|^(-1)sum_o f(o)`.  Empty deterministic outcome wires are
excluded.  Operational object words may contain quantum atoms and classical
wires in any displayed order; their algebra and reference trace are the
ordered spatial tensor products.  The separated word `[alpha][beta]` and
collective atom `[alpha concat beta]` are distinct types.

## D1206 (finite Heisenberg UCP category)

`HCPU_fd` has finite-dimensional unital C*-algebras as objects.  An arrow
`A->B` is a UCP map `B->A`.  Composition is composition in this Heisenberg
order; ordered tensor is the spatial tensor product.  For chosen faithful
reference traces, the Schrödinger density dual `Phi_*` is specified by

    tau_B(Phi_*(rho)a)=tau_A(rho Phi(a)).

Trace preservation of `Phi_*` follows from unitality of `Phi`.

## D1207 (preparations, discards, measurements, and corner instruments)

For any D1205 register word `X`, a preparation label is a density
`h>=0`, `tau_X(h)=1`, realizing `omega_h(a)=tau_X(ha):A_X->C`.  Discard is
the unit map `C->A_X`.  A POVM label is a finite nonempty family
`(e_o)_(o in O)`, `e_o>=0`, `sum_o e_o=1_X`, realizing

    C^O -> A_X,       f |->sum_o f(o)e_o.

An effect is one member of the two-outcome POVM `(e,1-e)`.

For equal-total compositions `alpha,beta`, a corner-Kraus instrument is a
finite family

    K_(o,i) in e_beta H_n(q)e_alpha,
    sum_(o,i)K_(o,i)^*K_(o,i)=e_alpha.

Its Heisenberg realization is

    Phi_K((a_o)_o)=sum_(o,i)K_(o,i)^*a_oK_(o,i).

It is a typed arrow

    K:[alpha] -> [beta] underline(O),

so its quantum output is retained.  At a fixed fibre, two lists are equal
when their normalized-basis coefficient Grams agree within each outcome;
equivalently, after zero padding, they differ by a scalar-unitary Kraus mixing
within each fixed outcome.  This is a sufficient process class; arbitrary CP
maps without such retained data are not included by this clause.

## D1208 (assembly and split processes)

For D1203 define

    asm_(alpha,beta):[alpha][beta]->[alpha concat beta]

to have Heisenberg realization the restricted trace-preserving conditional
expectation

    E_(alpha,beta):A_(alpha concat beta)->A_alpha tensor A_beta.

Define

    spl_(alpha,beta):[alpha concat beta]->[alpha][beta]

to have realization the corner inclusion `j_(alpha,beta)`.  The defining
relations include associative three-block assembly/split and

    spl_(alpha,beta) o asm_(alpha,beta)=id_([alpha][beta]).

The reverse composite is the collective coarse graining `jE` and is not set
equal to the identity.

## D1209 (retained collective context and ordered parallel process)

For a D1207 corner-Kraus family
`K:[alpha]->[beta]underline(O)` and a right context `gamma`,
retain the actual corner list

    K triangleleft gamma:
      [alpha concat gamma]->[beta concat gamma]underline(O),

    K triangleleft gamma
      =(iota_(n,k)(K_(o,i) tensor e_gamma))_(o,i).

For lists `K,L` on two ordered contiguous blocks with outcome sets `O,P`,
retain the typed direct collective instrument

    K boxtimes_c L:
      [alpha concat alpha']->[beta concat beta']underline(O times P),

    K boxtimes_c L
      =(iota(K_(o,i) tensor L_(p,j)))_((o,p),(i,j)).

These direct collective processes are distinct in type from the tensor of
the corresponding separated-register processes.  Their sequential and
parallel identities use D1218's explicit classical routing and history
bijections.  Context nesting and the routed identities are proved in
`theory/sidequests/f1-limit/operational-category.md` and `theory/sidequests/f1-limit/classical-wiring.md`.  No quantum block
exchange is included for `q!=1`.

## D1210 (typed operational circuit category)

`Op_q` is the strict ordered monoidal category presented by D1205 objects and
the generator boxes D1207--D1209 and D1218.  A raw morphism is a finite typed
planar circuit.  Equality is the congruence generated by planar graph isomorphism,
the strict category/monoidal axioms, literal equality of state and POVM
labels, fibre coefficient-Gram equality of Kraus labels, D1218's typed
classical wiring and routed instrument identities, retained-context
identities, and D1208's proved assembly relations.

`Op_I^cts` uses continuous positive normalized section labels over `I`.
Two continuous Kraus labels are equal when their coefficient Grams agree
pointwise on `I`; no continuous choice of environmental unitary is required.
`Op_1^germ` uses germs of such finite labelled circuits, and Kraus labels are
equal when their Grams agree on a common smaller interval.  Other presentation
relations likewise hold on a common smaller interval.  Equality is not
defined as equality of one isolated CP shadow.

## D1211 (operational realization and evaluation)

`Real_q:Op_q->HCPU_fd` sends every object to its D1205 algebra and every
generator to its D1207--D1209 UCP map.  It is allowed to be nonfaithful.
For `q in I`, `Ev_q:Op_I^cts->Op_q` evaluates every label.  Endpoint
evaluation `Ev_1:Op_1^germ->Op_1` is defined on germs.  No evaluation at a
fixed `q!=1` is defined on an arbitrary endpoint germ without first choosing
a representative whose interval contains `q`.

## D1212 (finite operational protocol and postselection)

A finite protocol is a finite rooted instrument tree whose root carries a
normalized state section, whose vertices carry typed finite-outcome circuits
and may depend on the finite preceding outcome history, and whose leaves
carry effects.  A branch weight is obtained by composing the outcome CP maps
and applying the final Born pairing.  An event weight is a finite sum of
branch weights.  A conditioned probability `N(q)/D(q)` is asserted near one
only when `D(1)>0`.

## D1213 (raw local corner lift)

For `a_0 in e_beta(q_0)H_n(q_0)e_alpha(q_0)`, a raw lift is obtained by
expanding `a_0` in D1201's normalized basis with constant coefficients and
compressing pointwise by `e_beta(q),e_alpha(q)`.  Tensor-register raw lifts
are finite sums in the `C(I)`-balanced tensor product of such sections.  This
lift is local data and is not declared canonical.

## D1214 (normalized local operational lifts)

For raw Kraus lifts `Khat_r(q)`, put

    S(q)=sum_r Khat_r(q)^*Khat_r(q),
    Ktilde_r(q)=Khat_r(q)S(q)^(-1/2)

on a neighborhood where `S` is invertible in the source corner.  For a state
density, lift its square root `c`, set `H=c^*c`, and divide by its positive
trace.  For a POVM, lift each square root, put `A_o=c_o^*c_o`,
`S=sum_o A_o`, and set `e_o=S^(-1/2)A_oS^(-1/2)`.  These are germ
normalizations and do not assert a global choice.

## D1215 (local contextual recovery class)

For the complete object `x^n`, express a retained list in the normalized
basis and store its coefficient Gram.  Let `d in S_(2n-1)` be the involution
that fixes one local point and swaps the other `n-1` local points with the
complement.  Embed each local regular-basis element explicitly by

    Btilde_h(q)=iota_(n,n-1)(B_h(q) tensor 1)
      in H_(2n-1)(q).

The recovery map sends a Gram `J` to

    sum_(h,k)J(k,h)Btilde_h(q)^*B_d(q)Btilde_k(q).

The selected minor indexed at `q=1` by the distinct permutations
`h^(-1)dk` defines the endpoint neighborhood on which contextual recovery is
claimed.  No all-`q>0` sharp context bound is part of this definition.

## D1216 (arithmetic evaluation and apartment comparison)

An arithmetic fibre is evaluation of D1202--D1211 and D1218 at the positive real
parameter `q=Q=p^r`, followed where desired by D1104/D1141's flag
realization.  Endpoint specialization is evaluation at `q=1`.  D1144's
`Omega_Q:H_n(Q)->C[S_n]` is a separate UCP compression inside one fixed
arithmetic fibre; it is not an evaluation map.

## D1217 (the three-constituent refinement protocol)

In `H_3(q)`, put `alpha=(1,2)`, `e_alpha=e_2=(T_2+1)/(q+1)`, and prepare the
normalized corner density `rho_alpha=e_2`.  Refine with the isometry
`v=e_2:alpha->(1,1,1)`.  In the standard `M_2` block let
`P_2=z_std e_2`.  Apply the two-outcome **Lüders instrument**

    K_s=P_2,                 K_f=1-P_2,
    [x^3]->[x^3]underline({s,f}),

and postselect its successful branch, retaining the quantum output.  On that
branch apply the retained right-context extension of `u_1=2e_1-1` from the
first two constituents, then measure `P_2` again.  The exact weights are
claims, not clauses of this definition.

## D1218 (classical wiring and routed instrument operations)

Let `*` be a fixed singleton.  For every bijection `r:O->P`, the classical
relabeling

    rel_r:underline(O)->underline(P)

has Heisenberg realization `r^*:C^P->C^O`, `r^*(f)=f after r`.  Classical
product and unit are the star-isomorphisms

    mul_(O,P):underline(O)underline(P)->underline(O times P),
    unit_cl:underline(*)->1,

induced by `delta_(o,p) |->delta_o tensor delta_p` and `C~=C^{*}`.  Their
inverses are included.  Relabelings compose as their set bijections; the
Cartesian associator and singleton unitors are the corresponding relabelings.

For every classical wire and every operational object word `X`, include the
classical routing isomorphism

    route_(O,X):underline(O)X -> X underline(O),

whose Heisenberg realization is the spatial flip
`A_X tensor C^O -> C^O tensor A_X`.  Its inverse, unit, nesting, and
naturality relations are the canonical spatial-flip relations.  This moves a
classical wire; it is not an exchange between two quantum blocks.

If `K:[alpha]->[beta]underline(O)` and
`L:[beta]->[gamma]underline(P)` are instruments, their routed sequential
instrument is

    Seq(L,K)
      =(id_[gamma] tensor mul_(O,P))
       o(id_[gamma] tensor route_(P,underline(O)))
       o(L tensor id_underline(O)) o K
      :[alpha]->[gamma]underline(O times P),

and has list `(L_(p,j)K_(o,i))_((o,p),(j,i))`.  If additionally
`K':[alpha']->[beta']underline(P)`, routed parallel composition is

    Par(K,K')
      =(id_[beta][beta'] tensor mul_(O,P))
       o(id_[beta] tensor route_(O,[beta']) tensor id_underline(P))
       o(K tensor K')
      :[alpha][alpha']->[beta][beta']underline(O times P),

with list `(K_(o,i) tensor K'_(p,j))_((o,p),(i,j))`.  The same formulas type
direct collective lists after replacing separated output atoms by their
stated collective atoms.

Sequential associativity is stated after the relabeling
`((o,p),r)<->(o,(p,r))`.  Parallel/sequential interchange is stated after
the history bijection

    ((o,p),(o',p')) <-> ((o,o'),(p,p')).

One-outcome instruments use the singleton classical unitor. The single
Kraus list `(e_alpha)`, followed by that unitor, is identified with the
identity process on `[alpha]`. All these
relations are equations of typed arrows, and their UCP realizations are the
canonical set relabelings and spatial flips followed by the displayed branch
maps.

## D1221 (multiplicative-sequence skeleton and variance convention)

A multiplicative sequence over `C` is a family of unital algebras
`A_*=(A_n)_(n>=0)`, with `A_0=C`, and unital maps

    mu_(m,n):A_m tensor A_n -> A_(m+n)

whose two composites from `A_l tensor A_m tensor A_n` to `A_(l+m+n)`
agree, and whose unit maps satisfy `mu_(0,n)(lambda tensor a)=lambda a`
and `mu_(n,0)(a tensor lambda)=lambda a`. Its skeleton `C[A_*]` has
objects `[n]`, zero Hom spaces between
unequal degrees, `End([n])=A_n`, composition equal to algebra
multiplication (`a after b=ab`), and tensor induced by `mu`.

A presheaf means a complex-linear functor `C[A_*]^op -> Vect_C`.  At
degree `n` it is a **right** `A_n`-module with action
`m dot a=F(a)(m)`.  The representable `h_[n]=Hom(-,[n])` is the right
regular module: precomposition sends `x` to `x a`.  This fixes all
opposite/covariance conventions.

## D1222 (finite Schur--Weyl or Day completion)

For a D1221 sequence with every `A_n` finite-dimensional over `C`,
the finite Schur--Weyl category `SW_fin(A_*)` is the algebraic direct sum

    direct-sum_(n>=0) mod_fd-A_n,

so each object has finite degree support and finite-dimensional right-module
components.  For a right `A_m`-module `M` and right `A_n`-module `N`, put

    M star N := (M tensor_C N)
                  tensor_(A_m tensor A_n) A_(m+n),

where `A_(m+n)` is a left `A_m tensor A_n`-module through `mu_(m,n)`
and a right module by multiplication.  The unit is `C=A_0`.  The
associator is the canonical balanced-tensor-product isomorphism, not an
identification of underlying vector spaces.  This is the finite part of
Day convolution on presheaves.

## D1223 (finite projective composition category)

Let `Proj(A_*)` be the additive Karoubi completion of `C[A_*]`.  Concretely,
its degree-`n` objects are pairs `(r,e)` with `r>=0` and an idempotent
`e in M_r(A_n)`; the represented right module is `e A_n^r`.  A morphism

    (r,e) -> (s,f)

is an element of `f M_(s,r)(A_n)e`, composition is matrix multiplication,
and unequal degrees have zero Hom space.  Tensor uses the matrix-amplified
map `mu_(m,n)` and the idempotent `mu(e tensor f)`.  If the `A_n` are
finite-dimensional C*-algebras and every structural map `mu` is a
star-homomorphism, the C*-version uses self-adjoint projections and matrix
star as its dagger. Equivalence to bare algebraic right modules forgets
this dagger; no inner product is inferred from bare module data.

## D1224 (universal positive Hecke composition category)

Let `R` be D1141's localized generic coefficient ring and put

    U_R := Kar_*(Add(C[H_*(R)])),

where `Kar_*` splits self-adjoint idempotents for the involution fixing the
coefficient parameter and sending `T_w` to `T_(w^-1)`.

Its evaluation functor at `q>0` is defined on every object and arrow presented
over `R`.  Put

    U_q := Proj_*(H_*(q))

for the self-adjoint-projection C*-version of the positive multiplicative
sequence in D1101--D1102. Base change gives
a functor `U_R->U_q`; it is not stipulated to contain every projection built
separately by functional calculus in the fibre.  Let `x=[1]`; then
`End_Uq(x^tensor n)=H_n(q)`.  The coefficient trace on a projection
corner is normalized only after division by its corner weight, as in
D1141. `U_q` is an amplitude category. Normalized states and effects are
taken on its nonzero finite C*-endomorphism algebras. Its full operational
envelope is the explicit finite-trace construction D1261--D1266; the fusion-only hypothesis of D1121 is not
imposed on `U_q`. No amplitude maps from the degree-zero unit are inferred.

## D1225 (partial-flag embedding and completion)

Let `Gamma_q` be D1141.  The typed object `alpha` of total `n` is sent to
the projective right module

    Y_q(alpha)=e_alpha H_n(q),

and `z in e_beta H_n(q)e_alpha` is sent to left multiplication
`L_z:e_alpha H_n(q)->e_beta H_n(q)`. In the self-adjoint projection model
this is a fully faithful monoidal star-functor; its bare-module realization
forgets the dagger. Its extension gives an equivalence

    Kar(Add(Gamma_q)) ~= U_q,

because the complete-flag object `(1,...,1)` has `e=1` in every degree.

## D1226 (Davydov--Molev parameter and generator translation)

Put `v=sqrt(q)>0`.  Davydov--Molev's Hecke generator `t_i`, satisfying

    (t_i-v)(t_i+v^(-1))=0,

corresponds to D1101's generator by

    T_i=v t_i,                 q=v^2.

Thus their multiplicative sequence and ours are isomorphic after this
base and generator change.  Their algebraic Hecke braiding is the image of
the positive braid word in the `t_i`.  The comparison does not declare that
braiding unitary for the coefficient-trace C*-structure.

## D1227 (finite abelian comparison)

For `q>0`, define `DM_fin(v)` to be the finite-support,
finite-dimensional right-module subcategory of Davydov--Molev's
Schur--Weyl category `C(H_*(v))`.  The parameter change D1226 and the
realization `(r,e) |-> eH_n(q)^r` define a strong monoidal equivalence

    U_q ~= DM_fin(sqrt(q)).

This is an algebraic strong monoidal equivalence: the bare right-module
target has no specified dagger. Its tensor is the induced module of D1222,
not the objectwise tensor of representations of unrelated `H_m` and `H_n`.

## D1228 (spectral physical adjacent exchange)

In `H_n(q)` define

    u_i=(2T_i+1-q)/(q+1)=2(T_i+1)/(q+1)-1.

It is the self-adjoint unitary which is `+1` on the `q`-eigenspace of
`T_i` and `-1` on its `-1`-eigenspace.  For adjacent indices its exact
braid defect is

    u_i u_(i+1) u_i-u_(i+1) u_i u_(i+1)
      =-((q-1)^2/(q+1)^2)(u_i-u_(i+1)).

## D1229 (longest-element polar reversal)

Let `w_0^(n)` be the longest permutation and `D_n=T_(w_0^(n))`.  In the
finite C*-algebra `H_n(q)` set

    J_n=D_n |D_n|^(-1),        |D_n|=(D_n^2)^(1/2),

with `J_0=J_1=1`.  For an interval `I` of consecutive tensor positions,
`J_I` denotes the shifted copy of `J_|I|`.  These positive square roots
are the unique C*-functional-calculus roots at the evaluated `q>0` fibre.

## D1230 (unitary Hecke coboundary commutor)

For `m,n>=0`, define on tensor powers

    sigma_(m,n)=J_(m+n) mu_(m,n)(J_m tensor J_n).

For projection-completed objects, restrict this operator to the source and
target corners; for direct sums, also apply the canonical matrix-index
flip.  The family `sigma` is the unitary coboundary commutor of claim F1-LIM-COB.  Its
coherence consists of naturality, `sigma_(n,m)sigma_(m,n)=1`, the unit
axioms, and the cactus square of Henriques--Kamnitzer Definition 3 /
Kamnitzer--Tingley Definition 4.4.

## D1231 (analytic scope of physical exchange)

The D1230 commutor is extra canonical structure on every positive real
C*-fibre and varies continuously on `q>0`.  It is the polar unitary of the
corresponding block braid.  It need not have coefficients in the localized
generic ring of D1141, and it is not a braiding when `q!=1`.  At `q=1` it
is the ordinary unitary block permutation and hence the symmetric
commutor.

## D1232 (classical Schur--Weyl quotient)

For `d>=1`, put `V_d=C^d` and let `P_sigma` permute tensor positions in
`V_d^tensor n` with the convention

    P_sigma(v_1 tensor ... tensor v_n)
      =v_(sigma^(-1)(1)) tensor ... tensor v_(sigma^(-1)(n)).

The map

    rho_(d,n):C[S_n] -> End_(U(d))(V_d^tensor n),
    sigma |-> P_sigma,

is the classical Schur--Weyl homomorphism.  Its kernel is the sum of
Wedderburn blocks indexed by partitions of `n` having more than `d` rows,
equivalently, when `n>=d+1`, the ideal generated by the embedded
`(d+1)`-strand antisymmetrizer.  It is faithful exactly when `d>=n`.

## D1233 (assembly of Schur--Weyl quotients)

Under `V_d^tensor(m+n) ~= V_d^tensor m tensor V_d^tensor n`, define

    nu_(m,n)(rho_(d,m)(a) tensor rho_(d,n)(b))
      =rho_(d,m+n)(mu_(m,n)(a tensor b)).

The kernel statement in D1232 makes this well-defined.  These maps are
associative unital algebra maps.  On right modules the strong monoidal
Schur--Weyl functor is

    M |-> M tensor_(C[S_n]) V_d^tensor n,

where the left symmetric-group action on the tensor power is `rho_(d,n)`.

## D1234 (tensor trace and physical conditional expectation)

Let

    tr_(d,n)(a)=d^(-n)Tr(rho_(d,n)(a)).

Then `tr_(d,n)(sigma)=d^(cyc(sigma)-n)`.  For `d>=n`, this is faithful on
`C[S_n]`.  For a subgroup `K=S_m times S_(n-m)`, its trace-preserving
conditional expectation `E_(d,K)` is characterized by

    tr_(d,n)(k^* E_(d,K)(x))=tr_(d,n)(k^*x), k in K.

In the group basis its coefficients solve the Gram system

    G_d(k,h)=d^(cyc(k^(-1)h)-n),
    G_d c=(d^(cyc(k^(-1)sigma)-n))_(k in K).

## D1235 (fixed-degree stable trace comparison)

Let `tau_n` be the coefficient trace and `E_(infty,K)` the coefficient
deletion expectation.  For fixed `n` and `x=sum a_sigma sigma`,

    |tr_(d,n)(x)-tau_n(x)|
      <= d^(-1) sum_(sigma!=1)|a_sigma|.

For `N=|K|`, `d>=n` and `d>N-1`, if `sigma notin K`, every group-basis coefficient
of `E_(d,K)(sigma)` has modulus at most `1/(d-(N-1))`; if `sigma in K`,
the expectation is exactly `sigma`.  Thus `E_(d,K)->E_(infty,K)`
coefficientwise at fixed `n`.  This is a large-`d` comparison, not a claim
that a fixed finite `d` trace or expectation equals the coefficient one.

## D1236 (rigid extension datum)

A rigid comparison datum consists of an additive idempotent-complete
monoidal category `R`, a named strong monoidal functor `i:U_q->R`, and
a named left and right dual `y^vee` of `y=i(x)`, with four maps

    coev_R:1->y tensor y^vee, ev_R:y^vee tensor y->1,
    coev_L:1->y^vee tensor y, ev_L:y tensor y^vee->1

satisfying the four zigzags with the stated associators. The target is
generated from `y,y^vee` by tensor, finite sums and retracts. The functor is
a comparison and may have a kernel; a fully faithful extension is claimed
only when full faithfulness is separately required and proved. In the
positive dagger version, `R` is a C*-category, `i` preserves star, and the
duality, dagger and positive spherical structure are explicitly compatible.
Duals of sums and retracts are formed in this additive Karoubi closure.

## D1237 (fusion quotient datum)

A fusion quotient datum consists of a monoidal ideal `I` in a chosen rigid
extension, a compatible dagger on the quotient, a positive pivotal trace,
and the instruction to quotient and then take additive Karoubi completion.
It qualifies as a fusion category only if the result is semisimple with
simple unit, finite-dimensional Homs, duals, and finitely many simple
isomorphism classes.  A trace radical or negligible ideal must be named;
it is not inferred from an algebra quotient alone.

## D1238 (Temperley--Lieb branch datum)

Put `f_i=(q-T_i)/(q+1)` and
`delta=sqrt(q)+1/sqrt(q)`.  A Temperley--Lieb branch adds the tensor ideal
relations

    f_i f_(i+1) f_i=delta^(-2)f_i,
    f_(i+1) f_i f_(i+1)=delta^(-2)f_(i+1),

equivalently kills the three-strand excluded Hecke summand, and supplies
the diagrammatic cups, caps, dagger, and Jones--Markov trace.  The faithful
coefficient/flag trace of D1101 is not declared to descend through this
nonzero ideal.

## D1239 (Fibonacci root branch datum)

The unitary Fibonacci branch is the even part of the level-three
`SU(2)`/Jones fusion quotient: it additionally chooses the order-five
root parameter giving `delta=2cos(pi/5)`, quotients the Jones trace radical,
and retains the even labels `{0,2}`, with `2 tensor 2=0 direct-sum 2`.
It is not the `q=1` specialization of the positive real Hecke/flag family,
where `delta=2` and the spin tower is untruncated.

Precisely, name `q_H=exp(2 pi i/5)`, `v=exp(pi i/5)` with `v^2=q_H`,
and the ILZ17 parameter `q_ILZ=-v`. Then
`delta=-(q_ILZ+q_ILZ^(-1))=v+v^(-1)`; the ILZ17 loop generator is
`U_i=delta f_i`, where `f_i` denotes our idempotent. The order of
`q_ILZ^2=q_H` is five. This fixes the source sign and generator scaling.

## D1241 (arithmetic affine-vector context algebra)

For `k=F_Q`, a finite-dimensional `k`-vector space `L`, `G=GL(L)` and
`X=Fl(L)`, let `Aff(L)=G semidirect L` act on `Y_L=X times L` by

`(g,a)(F,x)=(gF,a+gx)`.

The arithmetic affine-vector context algebra is

`R_X(L)=End_(Aff(L))(C[Y_L])`

with Hilbert adjoint and normalized operator trace
`tau_Q=Tr/(|X||L|)`.  Its invariant-kernel convention is
`K_f((F,x),(F',x'))=f(F,F',x'-x)`.

## D1242 (controlled translation-constraint algebra)

For a complete flag `F=(U_i(F))`, with `U_0=0` and `U_n=L`, define for
`0<=i<=n`

`C_i^X=sum_F |F><F| tensor P^X_(U_i(F))`,
`C_i^Z=sum_F |F><F| tensor P^Z_(U_i(F))`.

Here D1142 fixes both Weyl projector conventions, with the named phase when
identifying linear duals and additive characters. Thus `C_0^Z=I tensor
|0><0|` and `C_n^Z=I`. The same definitions apply on the dual space.

Let `Ctx_X(L)` be the star algebra generated on
`C[Fl(L)] tensor C[L]` by the relative-position flag operators
`A_w tensor I` and all `C_i^X`, including the endpoint constraints.  The
distinguished mirabolic projection is
`e=C_1^X` for `n>=1`; its unnormalized adjacency generator is `T_0=Qe-I`.

## D1243 (Fourier dual flag reversal)

For a named nontrivial additive character `psi:k->U(1)`, put

`F_(L,psi)e_x=|L|^(-1/2)sum_(lambda in L^vee)psi(-lambda(x))e_lambda`.

For `F=(U_i)` define `D_L(F)_j=U_(n-j)^perp`.  The Fourier dual flag unitary is
`W_(L,psi)=D_L tensor F_(L,psi)`. Under the canonical evaluation
identification `L=(L^vee)^vee`, its square across the dual pair is

`W_(L^vee,psi) W_(L,psi)e_(F,x)=e_(F,-x)`.

This formula includes characteristic two, where vector negation is the
identity. It fixes the negative Fourier-kernel and phase convention.

## D1244 (phase-polarized mirabolic comparison groupoid)

`PMir_(k,psi)` has finite-dimensional `k`-vector spaces as objects and linear
isomorphisms as arrows.  An object carries the pair

`R_X(L)`, `R_Z(L^vee)=W_(L,psi)R_X(L)W_(L,psi)^*`,

their Hecke inclusions, controlled constraint families, and the named unitary
`W_(L,psi)`.  A same-register realization additionally names a linear
self-duality `sigma:L->L^vee`.  Morphisms act on flags, vectors and duals by
the induced permutation unitaries.

## D1245 (mirabolic orbit poset and orbit basis)

For `w in S_n`, define `i prec_w j` by
`i<j` and `w^(-1)(i)<w^(-1)(j)`.  For an antichain `A`, let

`down_w(A)={i:i=a or i prec_w a for some a in A}`.

The orbit label `(w,A)` denotes the affine orbital whose relative flag
position is `w` and whose vector has maximal-support antichain `A`.  Write its
adjacency basis element as `T_(w,A)`; `A=empty` is the zero-vector Hecke basis.

## D1246 (based mirabolic trace family)

On Rosso's polynomial orbit-basis algebra, the conjugate-linear orbit star
is induced by `(F,F',v) |-> (F',F,-v)`: conjugate scalar coefficients
and send each orbit indicator to the indicator of the swapped orbit. In
D1245's standard-pair coordinates `(F_0,wF_0)` this is

`T_(w,A)^*=T_(w^(-1),w^(-1)(A))`.

The permutation `w^(-1)` identifies the two orbit posets; vector negation
preserves their support antichains. Define the coefficient trace by

`tau_q(T_(w,A))=[w=e and A=empty]`.

The marked parameter domain for this star-trace family is
real `q>1`; `q=1` is retained as a positive semidefinite boundary.  Positivity
is a claim, not part of this definition.

## D1247 (Hecke inclusion and vector expectation)

Let `i_q:H_n(q)->R_n(q)` be `T_w |-> T_(w,empty)`.  Define coefficient
deletion

`E_q(T_(w,A))=[A=empty]T_w`.

Its conditional-expectation and endpoint-quotient properties are claims.

## D1248 (algebraic and trace-supported mirabolic endpoints)

The algebraic endpoint is the full based specialization `R_n(1)`.  Its
reference trace is the specialization `tau_1` of D1246.  The trace-supported
endpoint is the GNS quotient

`R_n(1)/N_(tau_1)`,
`N_(tau_1)={x:tau_1(x^*x)=0}`.

These two endpoints are not identified by definition.

## D1249 (regular one-sided coefficients and admissible densities)

For `J_epsilon=[1,1+epsilon]`, `epsilon>0`, a regular mirabolic section is
`h(q)=sum_(w,A) h_(w,A)(q) T_(w,A)(q)` with every coefficient continuous
on J_epsilon. The section algebra has pointwise polynomial multiplication,
D1246's star and continuous coefficient trace. No C*-norm on this boundary
section algebra is stipulated. Hecke sections use D1202, restricted to J;
finite separated register words use continuous coefficients in the product
bases, including the coordinate basis of any classical factor.

A regular density label additionally satisfies `h(q)>=0` and `tau_q(h(q))=1`
for **every real** `1<q<=1+epsilon`, using the positive fibres of MIR-POS.
A regular effect satisfies `0<=e(q)<=1` throughout that punctured interval.
A regular POVM has finitely many such positive sections summing to the unit.
Positivity only at prime powers is insufficient for any of these labels.
Coefficient continuity forces the trace normalization at one; positivity of
the GNS-quotient density is proved in MIR-REG, not inferred from arithmetic
samples. Density families with coefficient poles, such as
`q/(q-1)(1-e)`, are not regular labels and require separate boundary data.

## D1250 (arithmetic type-C context algebra)

For a `2n`-dimensional symplectic `k`-space `V`, let `X_C(V)` be its complete
isotropic flags and put

`A_C(V)=End_(Sp(V))(C[X_C(V)])`

with Hilbert adjoint and normalized operator trace.  At a prime power this is
the finite type-`C_n` flag Hecke commutant.

## D1251 (decomposable isotropic flag and shuffle isometry)

For symplectic spaces of ranks `m,n`, a flag in `V orthogonal-sum W` is
decomposable when every step is `U_a direct-sum Z_b` for steps in component
isotropic flags.  `Sh(m,n)` is the set of two-letter lattice-path shuffles.
The shuffle isometry is the basis bijection

`J_(V,W):K_V tensor K_W tensor l2(Sh(m,n))->K_dec`.

Let `p_(V,W)=J_(V,W)J_(V,W)^*`.

## D1252 (type-C local-symmetry composition arena)

Put `H_(V,W)=Sp(V) times Sp(W)` and

`D_(V,W)=End_(H_(V,W))(K_(V orthogonal-sum W))`.

The product-shuffle arena is the corner
`p_(V,W)D_(V,W)p_(V,W)`, typed with corner unit `p_(V,W)` and normalized
operator trace on its range.

## D1253 (type-C restriction and preparation channels)

Let `G=Sp(V orthogonal-sum W)`, let `E_G` be conjugation averaging on the full
matrix algebra, and put `r_(V,W)=rank(p)/dim(K)`.  Define

`Phi_(V,W)(a)=pap`,
`Psi_(V,W)(x)=r_(V,W)^(-1)E_G(x)`

for `a in A_C(V orthogonal-sum W)` and `x` in the product-shuffle corner,
extended by zero on the orthogonal complement.

## D1254 (ternary shuffle coherence)

`Sh(l,m,n)` is the set of three-letter words with the named multiplicities.
The two canonical binary-expansion bijections from nested shuffle sets to
`Sh(l,m,n)` are the coherence maps.  All iterated decomposable-flag isometries,
restriction channels and trace-adjoint preparations are compared using these
fixed bijections and the ordinary Hilbert associator.

## D1255 (thin type-C block comparison)

At `q=1`, use the signed permutation groups `B_n`, the block inclusion
`B_m times B_n<=B_(m+n)`, and the unique factorization into a block signed
permutation and a fixed-convention unsigned `(m,n)` shuffle.  The induced
group-algebra star inclusion is the thin block assembly.  No generic Hecke
lift is included in this definition.

## D1256 (arithmetic affine decomposable composition arena)

For vector spaces `L,M`, let `p^aff_(L,M)` project onto basis pairs consisting
of a decomposable flag in `Fl(L direct-sum M)` and an arbitrary vector in
`L direct-sum M`.  The local symmetry is

`(GL(L) semidirect L) times (GL(M) semidirect M)`.

The affine product-shuffle arena, restriction and preparation maps are defined
by the same corner-compression and scaled full-group averaging formulas as
D1252--D1253.

## D1257 (regular separated operational mirabolic category)

For each real q>1, use quantum register atoms `[H_n]` and `[R_n]`, n>=1,
with their faithful normalized coefficient traces, together with nonempty
finite classical wires of D1205. The empty word has algebra C. Ordered
register tensor is the actual spatial tensor product; `[R_m][R_n]` is not
identified with `[R_(m+n)]`. The regular interval version uses D1249's
continuous product-basis sections on J_epsilon.

Generators are all regular normalized preparations, discards and finite
POVMs on register words; all retained same-register instruments with finite
regular coefficient lists `K_(o,i)` satisfying
`sum_(o,i)K_(o,i)(q)^*K_(o,i)(q)=1` for every real q>1 in J; and the arrows

`up_n:[H_n]->[R_n]`, Heisenberg map `E_q:R_n(q)->H_n(q)`,
`down_n:[R_n]->[H_n]`, Heisenberg map `i_q:H_n(q)->R_n(q)`.

The instrument output type is `X->X underline(O)`. Its list is retained when
tensored onto any separated context or included factorwise through i_q.
The list realizes `(a_o)_o |-> sum_(o,i) K_(o,i)^* a_o K_(o,i)`.
The full output density for the uniform classical trace has o-block
`|O| sum_i K_(o,i)hK_(o,i)^*`.

**Classical wiring hypothesis W.** Supply the repaired core's explicit
classical product/unit/relabeling and classical-wire routing maps, with their
correct types and parameter-independent UCP realizations. Any finite
classical control is a typed blockwise family of admitted labels. Its stated
relations must be satisfied by these maps, and a singleton-outcome identity
Kraus box must be the identity process. Here W is instantiated by D1218/CWIR-1--3; no quantum block exchange is
inferred from classical routing.

Under W, `RegOp_J` is the free finite typed ordered monoidal circuit category
on these boxes, modulo category/monoidal and W relations, literal state/POVM
label equality, and pointwise equality of coefficient Kraus Grams separately
inside each fixed outcome. Include correctly typed list-composition/tensor
identities and `down_n o up_n=id_[H_n]`; the reverse composite realizes iE
and is not set to the identity. Gram equality here is pointwise on J's
punctured interval; it does not demand a continuous choice of mixing matrices.
Relations are closed under insertion into any larger typed circuit.
No additional isolated-CP equality quotient is used.

Germs `RegOp_(1+)` identify labelled circuits when these presentation
relations hold on some common smaller one-sided interval. They have no
asserted C*-norm. No cross-rank mirabolic assembly is present: D1256 remains
a separately named arithmetic shuffle correspondence.

## D1258 (regular operational boundary functor)

Let `Pi_n:R_n(1)->H_n(1)` be D1248's GNS quotient with the fixed empty-orbit
basis identification, so `Pi_n=E_1`. For a register word X let Q_X be the
tensor of Pi on its mirabolic factors and identity on its Hecke and classical
factors. Replace every mirabolic atom by its Hecke atom to obtain bar(X).
The endpoint category `Op_H,1^sep` has these Hecke/classical words, the same
W wiring, all normalized preparations/POVMs/retained same-register Kraus
instruments, and their finite typed circuits, with the same endpoint label
relations. It has a UCP Heisenberg realization.

The functor `Ev_(1+):RegOp_(1+)->Op_H,1^sep` evaluates continuous
coefficients at one and applies Q_X to every density, effect and Kraus entry.
It sends up_n and down_n to identity. Its well-definedness, positivity,
normalization, compatibility with all generator relations and finite Born
limits are F1-MIR-REG. On a chosen interval, ordinary evaluations at q>1
also exist. An arbitrary boundary germ has no evaluation at a fixed q>1
without a representative containing that q.

Arbitrary UCP families with merely regular superoperator coefficients are
not admitted by D1257: the rank-one singular-sector state has constant values
on the orbit basis yet fails to annihilate the endpoint null ideal. The
regular density/Kraus generator restrictions are part of the functor's domain.

## D1259 (vector/polarization bridge package)

The package in rank n retains D1241–D1248, the Fourier data D1243–D1244,
and the regular operational boundary construction D1249/D1257–D1258 under W.
When composition is requested, it additionally names an arithmetic D1253 or
D1256 correspondence with D1254 shuffle coherence. Only the vector Fourier
factor is tensor-preserving under direct sums; the full flag/Fourier bridge
uses the decomposable shuffle isometry and its reversed-word identification.
An isomorphism of packages preserves the based Hecke inclusion, conjugate-linear
star, reference trace, both controlled families for `0<=i<=n`, the named
phase and the exact square

`W_(L^vee,psi) W_(L,psi)e_(F,x)=e_(F,-x)`

under canonical double duality, and every named UCP map. It also respects the
regular label class and the quotient boundary functor. Abstract algebra
isomorphism alone is not an isomorphism of bridge packages.

## D1261 (continuous finite graded self-adjoint completion)

For a nonempty compact interval `I subset (0,infinity)`, put
`A_n(I)=H_n^cts(I)` as in D1202. Write

    U_I^cts = Kar_dagger(Add(C[A_*(I)])).

Concretely an object `X` is a finite-support family
`(r_n,p_(X,n))_(n>=0)`, with nonnegative integers `r_n` and self-adjoint
projections `p_(X,n) in M_(r_n)(A_n(I))`; omitted components are zero.
For `Y=(s_n,p_(Y,n))`, put

    Hom(X,Y)=direct-sum_n p_(Y,n) M_(s_n,r_n)(A_n(I)) p_(X,n).

Composition is matrix multiplication degree by degree, dagger is matrix
adjoint with the Hecke star, and identity is `(p_(X,n))_n`.
The norm is the maximum of the component supremum C*-norms. A direct sum
uses a single block-diagonal projection in `M_(r_n+s_n)(A_n(I))` in each
degree. Its endomorphism corner includes the off-diagonal rectangular
corners between the summands of that same degree. It is not the direct sum
of their endomorphism algebras. Different degrees have zero Homs.
At a fibre `q`, denote this self-adjoint completion by `U_q^dagger`.
It is the positive dagger model of D1224's `U_q`.

## D1262 (balanced ordered tensor in the completion)

The section-algebra block map has domain

    A_m(I) tensor_(C(I)) A_n(I) -> A_(m+n)(I),

where the balanced C*-tensor product is the section algebra of the
pointwise spatial fibre tensor products. It is not the ordinary tensor
product over `C` with two independently varying parameters.

For D1261 objects `X,Y`, the degree-k matrix multiplicity of `X tensor Y`
is `t_k=sum_(m+n=k) r_m s_n`. Its projection is the block diagonal of
`iota_(m,n)^(r_m,s_n)(p_(X,m) tensor p_(Y,n))`, indexed by the pairs
`(m,n)` and lexicographic matrix indices. Morphism tensor is the analogous
block-diagonal amplified inclusion. The whole degree-k endomorphism
algebra is the full corner in `M_(t_k)(A_k)`, including off-diagonal blocks
between different pairs `(m,n)` with the same sum.
The unit is the degree-zero object `(1,1)`. Associators are the named
permutation matrices that identify the two finite indexings by triples
`(l,m,n;i,j,k)`. They do not exchange ordered Hecke blocks.

## D1263 (finite graded trace and normalized systems)

For an endomorphism `a` of `X`, put pointwise

    theta_X(a)=sum_n (Tr_(r_n) tensor tau_n)(a_n),
    w_X=theta_X(1_X),
    tau_X=theta_X/w_X.

`Tr_r` is ordinary, unnormalized matrix trace; `tau_n` is D1101's
normalized coefficient trace. The operational systems are the nonzero
objects on connected intervals, or nonzero fibre objects. Positivity of
`w_X` in every fibre of such an interval is a theorem, not an extra
assumption. The trace is not asserted to arise from categorical duality.
A normalized density is `rho>=0`, `tau_X(rho)=1`. Product register words
have spatial tensor observable algebras and product normalized traces.

## D1264 (traced assembly in the completion)

For nonzero X,Y, put `B_X=End(X)` and let

    j_(X,Y):B_X tensor B_Y -> B_(X tensor Y)

be morphism tensor. On intervals its tensor domain is C(I)-balanced.
Let `E_(X,Y):B_(X tensor Y)->B_X tensor B_Y` be characterized by

    (tau_X tensor tau_Y)(b^* E_(X,Y)(a))
       =tau_(X tensor Y)(j_(X,Y)(b)^* a).

Existence, uniqueness, continuity and complete positivity are claims.
The expectation onto the included algebra is `j E`; `E j=id`.
Ordered assembly is the process `[X][Y]->[X tensor Y]` realized in
Heisenberg orientation by E. Split has the reverse type and realization j.
The separated word and the collective atom remain distinct process types.

## D1265 (local completion germs and evaluation)

Use intervals `I_epsilon=[1-epsilon,1+epsilon]`, `0<epsilon<1`.
Objects of `U_1^germ` are germs of D1261 finite projection presentations,
with fixed matrix multiplicities under restriction; morphisms are the
corresponding germs of matrix-corner sections. Equality means literal
agreement on a common smaller interval, before passing to categorical
isomorphism. Operations and associators descend by restriction.
Evaluation at one is canonical; evaluation away from one requires a
representative interval. No C*-norm is assigned to these germ Hom spaces.
A local lift is a representative on some interval, not a canonical or
global section of evaluation. Isomorphic projection presentations are
compared by explicit morphisms, not silently made equal.

## D1266 (controlled operational completion without fusion hypotheses)

Use nonzero D1261/D1263 objects as quantum atoms, separated ordered words
of them, and finite nonempty classical wires with the uniform trace of
D1205. Include every normalized preparation, discard and finite POVM on a
register algebra. Include instruments specified by finite families

    K_(o,i) in Hom_U(X,Y),
    sum_(o,i) K_(o,i)^* K_(o,i)=1_X,

with Heisenberg map `(a_o)_o |-> sum_(o,i) K_(o,i)^* a_o K_(o,i)`
from `B_Y tensor C^O` to `B_X`. Retain the lists for collective extension
`K tensor 1_Z` and for ordered parallel composition. Include D1264 assembly
and split and finite typed circuits. Arbitrary CP maps need not admit this
retained presentation.

**Classical presentation hypothesis W.** To assert a presented operational
category, use an explicitly typed classical wiring presentation: it provides
classical product/unit/relabeling maps and any classical-wire routing needed
by multi-outcome composition, and its stated relations are satisfied by their
parameter-independent UCP realizations. Any included finite classical control
is a typed blockwise family of the already admitted generator/circuit labels;
it carries no additional arbitrary CP-map data. All instrument equations are written
with these maps, respecting their actual source/target words. A one-outcome
identity Kraus box is the identity process. The remaining relations are
category/monoidal axioms, literal label equality, scalar-unitary list
relations, correctly typed list/context/parallel identities, and the traced
assembly/split relations proved here. These are closed as a congruence.

Under W call the categories `Op^U_q`, `Op^U_I`, and `Op^U_1,germ`.
For interval labels use pointwise coefficient-Gram equality within each
outcome, as in repaired D1210; for germs use eventual such equality on a
common smaller interval. In the fixed ambient matrix-Hecke coordinates
this is equivalent to stable scalar-unitary mixing in each individual fibre.
No continuous family of the mixing unitaries is required or inferred.
CWIR-3 proves the resulting fibrewise congruence for products and contexts.
No faithfulness of the entire circuit realization is stipulated. The
explicit wiring D1218/CWIR-1--3 instantiates W; the general construction
may also be read conditionally for another sound wiring presentation.

## D1301 (trace-framed arithmetic register)

Fix a prime `p` and a named primitive complex `p`-th root `zeta_p`.
For a finite field `E/F_p` of cardinality `p^r`, the trace-framed arithmetic
register retains the field `E`, its Hilbert space `H_E=l2(E)` with orthonormal
basis `|x>` indexed by `x in E`, and the D3 trace character
`psi_E(x)=zeta_p^(Tr_(E/F_p)(x))`.
Its prime-field phase space is `S_E=E direct-sum E` with form
`Omega_E((a,b),(a',b'))=Tr_(E/F_p)(ab'-a'b)`.
The reference operators are the D8 operators
`X_E(a)|x>=|x+a>`, `Z_E(b)|x>=psi_E(bx)|x>`,
`W_E(a,b)=Z_E(-b)X_E(a)`.
An ordered list of registers has the tensor-product Hilbert space and
direct-sum prime-field phase space. The empty list has Hilbert space `C`.
The field structures and ordered factors are retained data.

## D1302 (arithmetic Frobenius operator)

For a D1301 register, put `sigma_E(x)=x^p` and
`U_E|x>=|sigma_E(x)>`. For a list, Frobenius means the tensor product of
these operators. All uses retain D1301's named `p` and `zeta_p`.

## D1303 (named embedding and transported relative trace)

For D1301 registers over the same named `p,zeta_p`, a named field embedding
`i:K->E`, `|K|=p^s`, and `r=ds`, define
`T_i(x)=i^(-1)(sum_(j=0)^(d-1) x^(p^(sj)))` and `kappa_i=|ker T_i|`.
Here `i^(-1)` is restricted to `i(K)`.
For `j:L->K` the composite trace is denoted `T_(i j):E->L`.

## D1304 (inclusion and normalized trace-fibre transfers)

For a D1303 embedding, define linear maps `J_i,V_i:H_K->H_E` by
`J_i|a>=|i(a)>` and
`V_i|a>=kappa_i^(-1/2) sum_(T_i(x)=a)|x>`, using the positive real square
root. Their reverse arrows are their Hilbert adjoints `J_i^*,V_i^*`.

## D1305 (subfield support code and logical phase quotient)

For a D1303 embedding, put `C_i=span_C{|i(a)>:a in K}`,
`P_i=J_i J_i^*`, `N_i={0} direct-sum ker T_i`, and
`G_i={Z_E(b):b in ker T_i}`.
The proposed logical phase space is `N_i^perp/N_i`, where perpendicularity
uses `Omega_E` of D1301. The logical coordinate map is
`[(i(a),b)] |-> (a,T_i(b))` whenever `N_i^perp=i(K) direct-sum E`.
Its well-definedness and symplectic property are claims, not stipulations.

## D1306 (negative-kernel arithmetic Fourier transform)

For a D1301 register define
`F_E|x>=|E|^(-1/2) sum_(y in E) psi_E(-xy)|y>`, with positive real square
root. A subscript on a tensor factor means that this operator acts there
and the identity acts on every other factor.

## D1307 (prime-field Pauli group and Clifford hierarchy)

For an ordered D1301 list `A=(E_1,...,E_n)`, let
`P_A={lambda tensor_j W_(E_j)(a_j,b_j):lambda in U(1)}`.
Set `C_1(A)=P_A` and, recursively for `k>=1`,
`C_(k+1)(A)={U unitary: U P U^* in C_k(A) for every P in P_A}`.
The exact level of `U` is the least positive `k` with `U in C_k(A)`, if
such a `k` exists. All scalar phases are included, in particular at `p=2`.
These sets are not stipulated to be groups beyond the second level.

## D1308 (reversible multiplication gates)

For a D1301 register and integer `d>=1`, define the linear operator
`M_E^(d)|x_1,...,x_d,z>=|x_1,...,x_d,z+product_(j=1)^d x_j>`
on `H_E^(tensor(d+1))`. Each argument occupies a distinct register.

## D1309 (phase polynomials and additive differences)

For a D1301 list with configuration space `A=product_j E_j` and a function
`f:A->F_p`, put `D_f|t>=zeta_p^(f(t))|t>` and
`delta_h f(t)=f(t)-f(t-h)` for `h in A`.
A polynomial of total degree at most `m` means a polynomial expression in
the coordinates of named `F_p`-bases, representing `f`, with that degree
bound. The condition concerns existence of such an expression; no unique
polynomial representative is stipulated.

## D1310 (the degree-four binary tower)

Put `K=F_2[a]/(a^2+a+1)` and `E=K[b]/(b^2+b+a)`.
The named embeddings are the constant embeddings `F_2->K->E`.
Write an element of `E` as `(u,v)=u+vb`, with `u,v in K`, and use
`zeta_2=-1`. Irreducibility and the resulting field orders are claims.

## D1321 (named arithmetic register datum)

Fix D1301's prime p and named root zeta_p. Choose a finite nonempty set F of
explicit finite fields of characteristic p and a finite category I whose
objects are these fields and whose arrows are named injective field maps,
including identities and composites. Equality of field arrows means equality
of their functions on the named finite sets. Polynomial presentations,
element names and embeddings are retained choices. Put R_p=Q(zeta_p,sqrt(p)),
with its given complex embedding, positive sqrt(p), and complex conjugation.
At p=2 this coefficient field is real: the source is the specified arithmetic
gate fragment, not the full Clifford category, which also has gates needing i.

Quantum atoms are Q_E for E in F and C_i for each arrow i:K->E in I. A
quantum word X is a finite ordered sequence of these atoms, including the
empty word 1. Its tensor product is concatenation. Attach the prime-field
symplectic space E direct-sum E, with D1301's trace form, to Q_E, and the
D1305 quotient N_i^perp/N_i to C_i. Attach the orthogonal direct sum to a
word. An isotropic context is a flag of F_p-isotropic subspaces of this
attached space. Contexts are retained geometric data, not a quotient by a
symmetry group and not the sole objects. There is no generator for every
context in this definition. The atom C_i retains its ambient field,
embedding and isotropic reduction label even when its Hilbert space is
isomorphic to that of Q_K. No identification of Q_E tensor Q_L with one
extension-field atom is imposed.

## D1322 (arithmetic amplitude syntax)

The pure source A_I has the words of D1321 as objects. Its terms are finite
R_p-linear combinations of well-typed circuits generated by identities,
symmetry swaps, tensor, composition, dagger, and the following arrows:

| generator | source -> target | labels |
|---|---|---|
| w_E(a,b) | Q_E -> Q_E | a,b in E |
| f_E, u_E | Q_E -> Q_E | negative Fourier; prime Frobenius |
| m_(E,d) | Q_E^(d+1) -> Q_E^(d+1) | integer d>=1 |
| j_i, v_i | Q_K -> Q_E | i:K->E in I |
| e_E | 1 -> Q_E | zero preparation |
| t_i | Q_K -> C_i | named logical identification |
| c_i | C_i -> Q_E | code encoding |

Dagger reverses the source and target and conjugates coefficients. Coefficient
scalars are elements of R_p acting centrally on each Hom. General endomorphisms
of the empty word may also contain closed circuit diagrams; they are not
asserted to equal coefficient scalars. Equality is the least
typed congruence generated by the R_p-linear dagger strict symmetric monoidal
axioms and precisely D1323's relations. In particular, equality is not
equality of Hilbert matrices, equality up to nonzero scalar, or equality of
CP maps. A scalar is not discarded. Infinite sums are absent.

## D1323 (arithmetic presentation relations)

Use the notation of D1322, with r=[E:F_p], tensor powers in the given order,
and composable i:K->L, j:L->E. Impose the following equations and their
daggers, and no other arithmetic equations by default:

1. `w_E(0,0)=1` and
   `w_E(a,b)w_E(a',b')=psi_E(ab')w_E(a+a',b+b')`.
   Each w_E(a,b) is unitary.
2. f_E, u_E and m_(E,d) are unitary; `f_E^4=1`, `u_E^r=1`,
   `m_(E,d)^p=1`, and `f_E u_E=u_E f_E`.
3. `u_E w_E(a,b)=w_E(a^p,b^p)u_E` and
   `u_E^(tensor(d+1)) m_(E,d)=m_(E,d) u_E^(tensor(d+1))`.
4. `j_i^dagger j_i=v_i^dagger v_i=1`; `j_id=v_id=1`;
   `j_j j_i=j_(ji)` and `v_j v_i=v_(ji)`.
5. `u_E j_i=j_i u_K`, `u_E v_i=v_i u_K`, and
   `f_E j_i=v_i f_K`.
6. For i:K->E, a in K and b in E,
   `w_E(i(a),b)j_i=j_i w_K(a,T_i(b))`, and
   `m_(E,d)j_i^(tensor(d+1))=j_i^(tensor(d+1))m_(K,d)`.
7. `e_E^dagger e_E=1`; `t_i^dagger t_i=1`, `t_i t_i^dagger=1`,
   and `c_i t_i=j_i`.
8. Put `b_(E,a)=w_E(a,0)e_E`. Impose
   `b_(E,a)^dagger b_(E,a')=delta_(a,a')` and
   `sum_(a in E) b_(E,a)b_(E,a)^dagger=1_QE`.

In the fourth relation, v_(ji) uses the transported composite trace, whose
transitivity is the algebra lane's transfer claim. All equalities are
typed before they can be used. The d+1 hierarchy label on m_(E,d) refers to
D1307's prime-field Pauli hierarchy; it is a generator label, not a
composition-closed class of arrows.

## D1324 (arithmetic Hilbert interpretation)

Assign H(Q_E)=ell^2(E), H(C_i)=C_i=range(J_i) inside ell^2(E), and tensor
products in the word order, with H(1)=C. The code has the orthonormal basis
`|i(a)>`, indexed by a in K. Send the generators w,f,u,m,j,v to the
D1301--D1308 operators W,F,U,M,J,V respectively. Send e_E to |0>, t_i to
the unitary `|a> -> |i(a)>` with codomain the code space, and c_i to its
inclusion into ell^2(E). Send swaps to ordinary Hilbert tensor swaps,
dagger to adjoint and R_p scalars through the named embedding. Denote this
candidate interpretation by H; well-definedness is FRP-CAT.

## D1325 (source-certified arithmetic processes)

Fix a countable naming universe containing the field-element labels of D1321
and closed under finite ordered tuples. Every external tag set and hidden
index set below is a finite subset of this universe; products use ordered
tuples in the same universe. This naming convention is presentation data.

A process object is a finite nonempty tagged family X=(X_a)_(a in A) of
quantum words. Tags are elements of named finite sets; distinct tags are
retained even when their quantum words agree. An arrow k:X->Y is a family
of finite hidden index sets J_(b,a) and amplitude classes
`k_(b,a,j):X_a->Y_b` in A_I, subject to the following source certificate for
each a: there exist finitely many amplitude arrows h_(a,l):X_a->Z_(a,l),
to arbitrary quantum words, with

    1_Xa - sum_(b,j) k_(b,a,j)^dagger k_(b,a,j)
      = sum_l h_(a,l)^dagger h_(a,l).

The equation is equality in D1322, with a finite derivation in its
congruence; the chosen certificate is evidence, not additional arrow data.
An arrow is normalized if `sum_(b,j) k^dagger k=1` in the source.
Hidden sets may be empty. Arrow equality is bijection of each hidden
index set carrying amplitudes to equal source arrows. No general Kraus
mixing, zero deletion, external-tag relabeling or CP-equality quotient is
imposed. In particular labels of external outcomes are never hidden by
this equality. A coefficient-scalar process is a singleton coefficient
amplitude on the empty word satisfying the same certificate, not a projective
class. General endomorphisms of the singleton empty-word process object may
have other closed-diagram amplitudes and more than one hidden index.

The identity has the single amplitude 1 on each diagonal external block
and an empty list elsewhere. For k:X->Y and l:Y->Z, composition has hidden
index triples (b,j,t) on block (c,a), and amplitude
`l_(c,b,t) k_(b,a,j)`. The tensor object has tag set A times B and word
X_a tensor Y_b. Tensor arrows have the Cartesian product hidden indices
and amplitudes k tensor l, with the indicated factor order. Associators,
unitors and swaps use the canonical finite-tag bijections and quantum
word swaps. A deterministic tag map g:A->B, with the same quantum word on
each routed block, has identity amplitude on block (g(a),a); this includes
discarding a classical tag. It cannot change the quantum type.

## D1326 (ordinary-trace completely positive realization)

The target has objects finite direct sums
`B_X=direct-sum_a End_C(H(X_a))` and arrows completely positive maps that
do not increase the sum of the ordinary matrix traces. The trace is
`Tr_X(rho)=sum_a Tr(rho_a)`; a density has Tr_X(rho)=1. The target tensor
is the ordinary finite-dimensional tensor product, distributed over the
tag blocks. The candidate process functor R sends D1325's arrow to

    R(k)(rho)_b=sum_(a,j) H(k_(b,a,j)) rho_a H(k_(b,a,j))^*.

Born weight of output tag b is its ordinary matrix trace. Conditioning
divides by that weight only when it is positive, and is not itself a
linear arrow. Retaining a history means making it part of the external
tag. Ordinary process composition sums over its intermediate input tag;
if that outcome must remain available, use an output tag carrying it.
This convention is distinct from D1205's uniform classical trace and
from the coefficient traces on the Hecke families.

## D1327 (retained arithmetic decoding and register circuits)

For an isometry s:X->Y in A_I, write p_s=s s^dagger and q_s=1-p_s.
The retained decoder D_s has source the singleton family (Y) and target
`(success:X, failure:Y)`, with one amplitude s^dagger on success and one
amplitude q_s on failure. The success arrow d_s:(Y)->(X) has amplitude
s^dagger and residual certificate q_s. The encoding arrow has amplitude s.
These constructions apply to j_i, v_i, c_i, their composites and their
independent tensor products. They do not stipulate a reset completion.

For an endomorphism a of Q_K^n, its code lift is
`a^[i]=t_i^tensor n a (t_i^dagger)^tensor n` on C_i^n. In particular take
a=u_K, w_K(a_0,b_0), or m_(K,d). These are explicit abbreviations for
source circuits. The Fourier comparison of retained decoders keeps both
tags: on the success block apply f_K, and on the failure block apply f_E.
Together these blocks form a tag-controlled normalized process.

The zero-state preparation on Q_E has the one amplitude e_E; basis
preparation at a has amplitude b_(E,a)=w_E(a,0)e_E. Quantum discard Q_E->1
has singleton external output and hidden amplitudes b_(E,a)^dagger over
a in E. Code discard is this discard after t_i^dagger; word discard is
their independent tensor. Discard of a tagged family sums all its input
blocks into the singleton empty-word output. A normalized source-generated
state followed by a retained decoder gives an actual preparation/test
protocol. Arbitrary complex states and arbitrary CP maps are not stipulated
as source generators. The R_p-span of the realized basis matrix units
already gives all R_p-valued matrices; the arithmetic structure consists of
the marked source data and relations, not a claim that this linear envelope
alone reconstructs the field.

If F_p is a named field in F and B=(beta_1,...,beta_r) is a named F_p-basis
of E, write x=sum_l x_l beta_l and define the coordinate circuit

    a_B=sum_(x in E) (tensor_l b_(Fp,x_l)) b_(E,x)^dagger
         : Q_E -> Q_Fp^tensor r.

This circuit retains B as its construction label. No basis-independent
identification of these two source objects is imposed. Its unitarity and
its interpreted trace-dual Weyl factorization are part of FRP-CAT.

## D1331 (marked Frobenius orbit algebra)

Fix r>=1 and a real variable t>=1, distinct from a field characteristic.
Let mu be the integer Moebius function (zero on numbers divisible by a
prime square, otherwise (-1) to the number of prime factors), and let
phi(d) count the integers 1<=a<=d coprime to d. Set

    c_d(t)=sum_(e|d) mu(d/e)t^e,
    O_r=direct-sum_(d|r) M_d(C),
    S_d|j>=|j+1 mod d>,  u_r=direct-sum_(d|r) S_d.

At an arithmetic comparison t=p, choose E=F_(p^r). In every orbit O of
sigma_E choose an origin b_O and label its vectors by sigma_E^j(b_O),
0<=j<|O|. Define R_(p,r):O_r->End(H_E) by acting with the same matrix a_d
on every marked orbit of length d. The comparison carries these origin
choices. For a tower of standard subfields in one finite field, use the
same origin on an orbit wherever that orbit occurs. No compatible origins
for every named embedding or field automorphism are stipulated.

## D1332 (conditional orbit boundary and reference state)

For D1331 and r>=2 put e_r=direct-sum_(d|r,d>1) I_d, with zero d=1 block,
and O_r^+=e_r O_r e_r. Its identity is e_r and its Frobenius is
u_r^+=e_r u_r e_r. With tr_d=Tr/d the normalized ordinary matrix trace,
define the ambient reference functional and its active weight by

    theta_(r,t)(a)=sum_(d|r) c_d(t)t^(-r) tr_d(a_d),
    w_r(t)=1-t^(1-r).

For t>1 define omega_(r,t)(a)=theta_(r,t)(a)/w_r(t) on O_r^+.
At t=1 stipulate

    omega_(r,1)(a)=sum_(d|r,d>1) phi(d)/(r-1) tr_d(a_d).

The ordinary block-trace density of this functional is
sigma_(r,t)=direct-sum_d lambda_(r,d)(t) I_d/d, where
lambda_(r,d)(t)=c_d(t)/(t^r-t) for t>1 and phi(d)/(r-1) for t=1.
At t=p its physical conditioning projection is
P_r^mov=sum_(x in E, x^p!=x) |x><x|. This removes fixed basis labels;
it is not the orthogonal complement of all Frobenius-invariant vectors.

## D1333 (orbit processes, independent composition and retained inclusion)

Objects are finite ordered words R=(r_1,...,r_n), r_j>=2, and finite
nonempty tagged families of these words. The empty word has algebra C.
For a word set O_R^+=tensor_j O_(r_j)^+ and take the product reference
functional omega_(R,t)=tensor_j omega_(r_j,t). A tagged family has the
direct sum algebra. A process is a complex-linear CPTP map between these
algebras in the Schroedinger orientation, using the sum of ordinary matrix
traces on all simple blocks. Equality is equality of linear maps;
composition is composition, tensor is the matrix tensor with paired tags.
The distinguished Frobenius channel is conjugation by tensor_j u_(r_j)^+.

For 2<=r|s define e_(r,s) in O_s^+ to be identity on blocks d|r, d>1,
and zero on the other blocks. Let j_(r,s):O_r^+->O_s^+ insert zero blocks.
It is the specified encoding on ordinary-trace densities. Its retained
decoder has output tags success and failure, with algebras O_r^+, O_s^+,
and maps rho to

    ((rho_d)_(d|r,d>1), (1-e_(r,s))rho(1-e_(r,s))).

The reference probability of its success is denoted h_(r,s)(t):
(t^r-t)/(t^s-t) for t>1 and (r-1)/(s-1) at t=1.
The unnormalized ambient word weight is W_R(t)=product_j w_(r_j)(t).
The word length records its order of vanishing; it is not a Clifford level.
This CP envelope is not stipulated to be an image of every arithmetic
process in D1325. The arithmetic comparison is only the marked observable
representations of D1331 and the specified gates and block instruments.

For d,e>=1 set g=gcd(d,e), l=lcm(d,e), and define the reblocking unitary

    B_(d,e): C^g tensor C^l -> C^d tensor C^e,
    |a,k> -> |k mod d, a+k mod e>, 0<=a<g, 0<=k<l.

Its multiplicity factor C^g is quantum. Iterated reblockings are compared
through the same ordered Cartesian basis, not by identifying internal labels.

## D1334 (multiplication active cuts and overlapping controls)

For D1301 and D1308 put Q=|E|, d>=1, and

    P_(E,d)^nz=(I-|0><0|)^tensor d tensor I,
    tau_(E,d)=Tr/Q^(d+1),
    v_(E,d)=P_(E,d)^nz M_E^(d) P_(E,d)^nz.

The normalized corner trace is tau_(E,d)^nz(a)=
tau_(E,d)(a)/tau_(E,d)(P_(E,d)^nz). On a specified word of n registers
and a subset A of its indices, P_A^nz tests nonzero labels precisely on A.
For comparison with Fourier use P_r^dual=F_E P_r^mov F_E^* on one field
register. These are separate cuts: nonzero controls, nonfixed Frobenius
labels, and Fourier-transported nonfixed labels are not identified.

## D1401 (finite etale embedding datum)

Fix a field `K` and a named separable closure `Omega=K^sep`.
Put `G_K=Aut_K(Omega)` with its Krull topology. Let `Et_K^+` have as
objects nonzero finite etale commutative unital K-algebras and as arrows
unital K-algebra homomorphisms `f:A->B` for which B is finite locally free
over A of one constant positive rank `r_f`. Equivalently, `B` is isomorphic
to `A^(r_f)` as an A-module; no such module isomorphism is chosen.
The tensor is `tensor_K` and its unit is K. Set

    X_A=Hom_(K-alg)(A,Omega),  n_A=dim_K A,
    H_A^emb=ell^2(X_A),  B_A^emb=End_C(H_A^emb),
    U_A^emb(g)|tau>=|g composed tau>,  rho_A^mix=I/n_A.

The basis of `ell^2(X_A)` is orthonormal for counting measure. The
observable algebra is the full matrix algebra, including coherent matrix
entries between distinct G_K-orbits. The reference trace is ordinary
matrix trace, and the named reference density is `rho_A^mix`.

## D1402 (embedding-fibre transfers and comparison maps)

For D1401 and `f:A->B`, define

    R_f:X_B->X_A,  R_f(tau)=tau composed f,
    s_f|sigma>=r_f^(-1/2) sum_(R_f(tau)=sigma)|tau>.

The square root is the positive real square root. For objects A,C, let
`mu_(A,C):H_A^emb tensor H_C^emb -> H_(A tensor_K C)^emb` send
`|sigma> tensor |tau>` to the basis vector of the homomorphism
`a tensor c -> sigma(a)tau(c)`. The unit comparison sends `1 in C` to
the unique K-embedding of K into Omega. For a named K-isomorphism of
separable closures `eta:Omega->Omega'`, define
`W_(eta,A)|tau>=|eta composed tau>` and
`c_eta(g)=eta g eta^(-1)`.

## D1403 (retained embedding decoding)

For D1401--D1402, put `P_f=s_f s_f^*`, `Q_f=I-P_f`, and use the
retained-isometry decoder schema of D1327 in the full complex matrix
algebras. Its encoding, success map and retained decoder are

    E_f(rho)=s_f rho s_f^*,
    d_f(rho)=s_f^* rho s_f,
    D_f(rho)=(d_f(rho),Q_f rho Q_f)
      : B_B^emb -> B_A^emb direct-sum B_B^emb.

The output tags are success:A and failure:B; trace on a tagged algebra
is the sum of ordinary matrix traces. A completely positive map is a
linear map whose identity-matrix amplifications preserve positive matrices;
it is trace preserving if it preserves this specified trace. Independent
decoders pair every output tag. A stopped tower decoder applies the next
decoder only on the preceding success output and retains every failure
at the object where it first occurs. Full instruments are compared with
these histories, without identifying them with the binary decoder of a
composite isometry.

## D1404 (embedding stabilizer and normal closure)

For D1401 with A a field and a named `tau_0 in X_A`, put

    H_(A,tau_0)={g in G_K:g composed tau_0=tau_0},
    C_A=intersection_(g in G_K) g H_(A,tau_0) g^(-1),
    N_A=K( union_(tau in X_A) tau(A) ) subset Omega.

Thus N_A is the compositum of all embedded conjugates. The definition of
N_A does not use tau_0. The notation C_A anticipates the proved independence
of its defining expression from the choice of tau_0.

## D1405 (primitive finite-field orbit comparison)

For D1401 with `K=F_p`, let `Frob_p:Omega->Omega` be `x->x^p`.
Let A be a degree-d field extension of F_p, choose `a in A` with
`A=F_p(a)`, and choose `tau_0 in X_A`. Put `b=tau_0(a)` and
`O_b={b,b^p,...,b^(p^(d-1))}`. For a positive multiple r of d, let
`E=F_(p^r)` be the unique such subfield of Omega and define

    T_a:H_A^emb -> ell^2(O_b) subset ell^2(E),
    T_a|tau>=|tau(a)>.

The orbit coordinate unitary `L_(tau_0):C^d->H_A^emb` sends
`|j>` to `|Frob_p^j composed tau_0>` for `0<=j<d`. In these coordinates
write `S_d|j>=|j+1 mod d>`. The word primitive here means degree exactly d
over F_p, and does not require a generator of A's multiplicative group.

## D1421 (joint arithmetic code and Gram datum)

For a D1303 named finite-field embedding `i:K->E` of degree `n>=2`, put
`q=|K|=p^s`, `Q=|E|=q^n`, and retain `kappa_i=Q/q` from FRB-TRACE.
Write `Gamma_i=J_i^*V_i`, `P_i=J_i J_i^*` as in D1305, and
`Ptilde_i=V_i V_i^*`. Let `S_i=ran J_i+ran V_i`, let `E_i` be its
orthogonal projection, and use the physical trace `tau_E(a)=Tr(a)/Q`.
The projection algebra is the unital star algebra generated by
`P_i,Ptilde_i` inside `End(H_E)`; zero-dimensional summands are omitted.
Put `|+_K>=q^(-1/2)sum_(x in K)|x>` and
`R_K|x>=|-x>`. Statements about the joint representation of Frobenius
refer to the restriction of `U_E` to `S_i`.

## D1422 (invertible-degree corrected trace frame)

For a D1421 embedding with `p` not dividing `n`, let
`D_n^K|x>=|nx>`, `L_i=V_i D_n^K`, `c_i=kappa_i^(-1/2)`,
`h_i=sqrt(1-c_i^2)`, and `W_i=(L_i-c_i J_i)/h_i`.
Define `mathcal T_i:C^2 tensor H_K -> H_E` by
`mathcal T_i(|0> tensor x)=J_i x` and
`mathcal T_i(|1> tensor x)=W_i x`.
Write `B_i=(D_n^K)^(-1)F_K`. More generally, for a nonzero prime-field
scalar `a`, `D_a^K|x>=|ax>` and `D_a^E|y>=|ay>`.
All square roots are positive. This definition is restricted to `p∤n`.

## D1423 (singular-degree arithmetic sectors)

For a D1421 embedding with `p|n`, put
`alpha_i=J_i|+_K>`, `beta_i=V_i|0>`, `d_i=sqrt(q/kappa_i)`, and
`A_K=|+_K>^perp` inside `H_K`.
If `n>2`, put `e_i=sqrt(1-d_i^2)` and define
`mathcal T_i^ang:C^2->H_E` by its columns
`alpha_i,(beta_i-d_i alpha_i)/e_i`.
For every `p|n`, define `mathcal T_i^res:C^2 tensor A_K->H_E` by
`|0> tensor x |-> J_i x` and `|1> tensor x |-> V_i F_K x`.
If `n=2,p=2`, retain the common line `C alpha_i=C beta_i` and use only
the residual frame; no division by `e_i=0` is permitted.

## D1424 (conditioned matrix chart and normalized tangent)

For `0<=c<=1`, put `h=sqrt(1-c^2)` and use the fixed algebra `M_2(C)`
with faithful reference state `tr_2=Tr/2`. Define

    p_c = [[1,0],[0,0]],
    q_c = [[c^2,ch],[ch,h^2]],
    f_c = [[c,h],[h,-c]],
    d_c = [[-h,c],[c,h]].

For `c<1`, `d_c=(q_c-p_c)/h`; at `c=1` the displayed continuous matrix
defines the retained tangent. Its endpoint is `d_1=X`, while `f_1=Z`.
Conditioning on a represented chart means dividing its physical restricted
trace by that chart's support weight before varying `c`.
If a logical factor `H` is retained, the reference is
`tr_2 tensor tr_H` on `M_2 tensor End(H)` and the chart matrices act
on the first factor. The parameter variation is a matrix continuation,
not a claim that noninteger field cardinalities are fields.

## D1425 (iterated arithmetic frame and refinement connector)

Let `K_0 --i_1--> K_1 --...--i_l--> K_l`, `l>=1`, be a named tower
whose degrees `n_r>=2` satisfy `p∤n_r`. Set `N=product_r n_r`.
Use outer-to-inner chart order `l,...,1`. Its path frame is

    mathcal T_path = mathcal T_(i_l)
      (I_2 tensor mathcal T_(i_(l-1))) ...
      (I_(2^(l-1)) tensor mathcal T_(i_1))
      : (C^2)^(tensor l) tensor H_(K_0) -> H_(K_l).

For any numbers `0<c_r<1`, put `v_r=c_r|0>+h_r|1>`,
`h_r=sqrt(1-c_r^2)`, `c_*=product_r c_r`, and
`h_*=sqrt(1-c_*^2)`. The refinement connector
`C_(c_l,...,c_1):C^2->(C^2)^(tensor l)` has columns

    |0> |-> |0...0>,
    |1> |-> (v_l tensor ... tensor v_1-c_*|0...0>)/h_*.

At an arithmetic fibre use `c_r=kappa_(i_r)^(-1/2)`.
Consecutive-block refinements use the same definition, with each block's
parameter the product of its constituent parameters and its path factors
in the same outer-to-inner order.

## D1426 (continuous CP charts and retained frame decoding)

For finite-dimensional Hilbert spaces `X,Y`, a continuous retained chart
instrument on a closed real parameter interval is a finite family of
continuous matrices `K_b(t):X->Y_b` with
`sum_b K_b(t)^*K_b(t)=I_X`. Its map is
`rho |-> direct-sum_b K_b(t)rho K_b(t)^*`.
States and normalization use ordinary matrix traces on the blocks.
For a continuous isometry `S(t):X->Y`, its retained decoder has
success amplitude `S(t)^*:Y->X` and failure amplitude
`I_Y-S(t)S(t)^*:Y->Y`, with distinct classical tags. The failed ambient
state is retained. Independent decoders retain all pairs of tags and
have Kraus matrices given by tensor products.
Sequential decoders retain every history. A reference state such as
D1424's `tr_2` specifies input probabilities; it does not replace the
ordinary trace used to test channel normalization.

## D1427 (weighted tower endpoint)

For `l>=1` and fixed positive real weights `a_1,...,a_l`, let
`A=sum_r a_r`, `c_r(t)=t^(-a_r/2)` for `t>1`, and use the D1425
connector. At `t=1` define

    C_a(1)|0>=|0...0>,
    C_a(1)|1>=sum_r sqrt(a_r/A)|one_r>,

where `|one_r>` has one entry `1` in the factor belonging to edge `i_r`
and all other entries `0`. Consecutive blocks have weights given by sums.
The endpoint reference on the direct chart is `tr_2`; on the entire path
space it is `tr_(2^l)`, and conditioning the latter on `ran C_a(1)`
recovers the direct reference. These are distinct unconditioned states.

## D1428 (finite mixed extension test diagram)

A mixed extension test diagram is a finite diagram of D1303 named
finite-field embeddings in one characteristic, closed under its named
composites, together with finite words of its arithmetic registers.
The named amplitude operations are D1302 Frobenius, D1306 Fourier,
D1304 inclusion and trace transfer and their adjoints, nonzero prime-field
dilations, D1308 multiplication gates of any explicitly named positive finite arity,
tensor identities, and their finite composites and adjoints.
The retained processes are their isometric encodings, D1327 decoders,
finite compositions with every outcome history retained, and independent
tensor with every outcome tuple retained.
The marked sector tests comprise the D1421 joint sectors, the D1423
singular sectors when present, and any explicitly selected D1331 orbit
and D1334 active-control projections and their actual Fourier transports.
An equality in this test diagram is an equality of the named finite-field
amplitude maps or of the corresponding tagged CP maps, not an equality
obtained by separately compressing intermediate gates.

## D1441 (signed Frobenius orbit count candidates)

For an odd prime p and r>=1, let the two generators of
`Gamma_r^sgn=C_r times C_2` act on `F_(p^r)^times` by `x->x^p` and
`x->-x`, respectively. A point of exact Frobenius period d is called
internal if its negative belongs to its Frobenius orbit, and external
otherwise. No assertion about its count is part of this definition.
Use D1331's real variable t and integer functions mu,phi,c_d. For even
`d=2^k m`, `k>=1` and m odd, define candidate point-count polynomials

    A_d^sgn(t)=sum_(e|m) mu(m/e)(t^(2^(k-1)e)-1),
    B_d^sgn(t)=sum_(e|m) mu(m/e)(t^(2^(k-1)e)-1)^2.

For odd d set `A_d^sgn=0`, `B_1^sgn=t-1`, and `B_d^sgn=c_d(t)`
when d>1. Put `J_2(m)=m^2 product_(ell|m prime)(1-ell^(-2))`, with
empty product one. These definitions apply only to odd characteristic;
the negation action is identity at p=2.


## D1501 (period-uniform arithmetic reference)

Fix the actual prime p, the named primitive root zeta_p, and a finite
diagram of D1301--D1304 arithmetic fields and embeddings. The real
parameter is h>=0, with t=exp(h); p remains part of the arithmetic data.
For E=F_(p^r), put P_(E,0)=|0><0| and let P_(E,d)^times project onto
nonzero labels with exact absolute Frobenius period d, d|r. Define
b_1(t)=t−1 and b_d(t)=sum_(e|d)mu(d/e)t^e for d>1, where mu is the
integer Moebius function of D1331. Set

    D_E(h)=P_(E,0)+sum_(d|r) b_d(exp h)/b_d(p) P_(E,d)^times,
    rho_E(h)=exp(−r h)D_E(h).

A period-uniform density means a matrix in the real span of these
orthogonal projections, with no off-diagonal blocks. Its prescribed masses
are exp(−rh) at zero and exp(−rh)b_d(exp h) on each nonzero period block.
For an ordered word E_1,...,E_m use tensor products D_word,rho_word and
R=sum_j r_j. The empty word has D=rho=1 and R=0. The reference is additional
state data, not a replacement for the constant maximally mixed preparation.

## D1502 (positive reference coefficients and coefficient states)

For D1501 put A_(E,0)=P_(E,0). For integers k>=1 define

    J_k(d)=sum_(e|d)mu(d/e)e^k
          =d^k product_(ell|d prime)(1−ell^(−k)),
    A_(E,k)=sum_(d|r) J_k(d)/(k! b_d(p)) P_(E,d)^times.

The empty product makes J_k(1)=1. Put B_E=A_(E,1),
sigma_(E,0)=P_(E,0) and sigma_(E,k)=k! A_(E,k)/r^k for k>=1.
Word coefficients are the Cauchy tensor coefficients
A_(word,k)=sum_(k_1+...+k_m=k) tensor_j A_(E_j,k_j).
For nonempty words put sigma_(word,k)=k! A_(word,k)/R^k for k>=1
and sigma_(word,0)=tensor_j P_(E_j,0).

## D1503 (finite positive boundary profile)

For D1502 define L_E(h)=P_(E,0)+h B_E and
L_word(h)=tensor_j L_(E_j)(h). A positive operator polynomial on a
finite-dimensional block matrix algebra B is a finite sum
A(h)=sum_(k=0)^m h^k A_k with every A_k positive in B.
Its coefficients, including zero coefficients, are retained data.
Let P_(E,+)=I−P_(E,0). For a subset S of word positions set

    P_S=tensor_j [P_(E_j,+) if j in S, otherwise P_(E_j,0)],
    B_S=tensor_j [B_(E_j) if j in S, otherwise P_(E_j,0)].

Thus L_word=sum_S h^|S| B_S. Its normalized finite-profile preparation
is lambda_word(h)=L_word(h)/Tr(L_word(h)); for one field its denominator
is 1+r h. D_word and L_word are different families.

## D1504 (positive-series process category)

Objects are the D1326 finite tagged block matrix algebras with their sum
of ordinary matrix traces. A positive scalar normalizer is a series
Z(h)=sum_(k>=0)z_k h^k with z_k>=0, z_0>0 and Z(h)<infinity for every
real h>=0. A process representative X->Y is a pair (Phi,Z), where
Phi(h)=sum_(k>=0)h^k Phi_k, every Phi_k:B_X->B_Y is completely positive,
and for every positive a and every k,

    Tr_Y(Phi_k(a)) <= z_k Tr_X(a).

It is normalized when equality holds for every k,a. Tagged instruments
are the same definition with their output tags retained. Two representatives
are equal precisely when Z' Phi=Z Phi' coefficientwise as linear maps,
with identical external tags. Composition uses (Psi Phi,W Z), tensor uses
(Phi tensor Psi,Z W), and identities use (id,1). Products use Cauchy
coefficients. Evaluation is Phi(h)/Z(h), a usual ordinary-trace CP map.
This is a semantic CP category; it does not assert faithfulness of the
source's distinct Kraus presentations or identify amplitude equations
beyond their actual CP interpretation.

## D1505 (arithmetic profile action and finite reference protocols)

On the objects of D1504 retain every actual constant D1326 arithmetic
process map. Its action on a D1503 polynomial is coefficientwise:
Phi_*A=sum_k h^k Phi(A_k). A profile experiment object is a pair (X,A)
with A such a polynomial; an arrow (X,A)->(Y,C) is a constant arithmetic
CP map Phi satisfying C=Phi_*A. Equality is equality of those typed CP
maps; identity, composition and tensor use their usual actual operations.
Zero profiles are allowed but have no conditional state. One may equally
use all finite-dimensional constant CP maps as an explicitly larger envelope.
Independent profiles tensor by the Cauchy product.
A finite reference protocol is a finite circuit using actual constant
arithmetic CP maps and either exact rho_E preparations or finite-profile
lambda_E preparations, with finitely many reference registers and every
specified measurement placement and retained history named. It can be
evaluated in D1504. At the amplitude level all actual arithmetic gates,
adjoints and coherent compositions retain their original matrices; a CP
map is applied only where the protocol prescribes an instrument/channel.

## D1506 (leading operational boundary record)

For a nonzero positive series or polynomial A(h)=sum_k h^k A_k,
let v(A)=min{k:A_k!=0}, M(A)=A_(v(A)), w(A)=Tr M(A), and
eta(A)=M(A)/w(A). The boundary record is (v,M), equivalently (v,w,eta).
For a branch of an experiment normalized by a scalar with constant term
one, w is its leading event-probability coefficient, v its vanishing order,
and eta its limiting conditional density. For a normalizer with constant
term z_0, the event coefficient is w/z_0.
Conditioning on a positive-probability branch divides by its actual trace.
Leading normalization alone is not an arrow or a stipulated functor;
the full profile is retained before any later continuation or conditioning.

## D1507 (relative-Frobenius multiplication protocol)

For a named proper embedding i:K->E, q=|K|=p^s, |E|=p^r, choose named
a,b in E with T_i(ab)=0 and T_i(a^q b)=1. Their existence is a claim.
Prepare the independent reference word E,E,K and retain the outcome
postselecting its computational labels to a,b,0. Encode the target by V_i,
apply U_E^s to the first control, apply the actual M_E^(2) to both controls
and target, then apply F_E to the target. Apply the retained J_i decoder
to the target, and on success apply F_K^* and measure the target label.
All failure tags remain available. The optional coherence test dephases
the target in its E computational basis immediately after V_i.
The reference preparation may be either rho_word or lambda_word; comparison
of their boundary records uses D1506, not equality at finite h.

## D1601 (completed concrete arithmetic source)

For a finite named field diagram I in characteristic p, let A_I^mat be
the image of the D1324 arithmetic amplitude interpretation, with equality
of typed actual matrices and scalars in R_p=Q(zeta_p,sqrt(p)). Its finite
additive completion has finite lists of objects and rectangular matrices
of its arrows. Its self-adjoint projection completion has objects (X,e)
with e=e^*=e^2 an actual endomorphism in that completion, and arrows
f:(X,e)->(Y,g) given by actual matrices f=gfe. Hilbert realization is ran e.
Independent tensor is the actual tensor of words, projections and arrows.

Use finite retained Kraus lists of these arrows whose actual squared
amplitudes sum to at most the source identity; normalized lists have sum
equal to that identity. Classical tags use block output algebras and sum
of ordinary traces. States include the D1501 and D1503 additional reference
preparations and the prescribed fixed zero preparations. Coherent sums
retain source Hom blocks; they are not classical tags. No surjectivity
onto all complex CP maps is stipulated. Collective assembly is specified
by actual isometries, arithmetic circuits and projections in this source.

## D1602 (relative multiplication-graph register)

Fix a named extension E/K with |K|=q=p^s, |E|=q^n=p^r, r=sn and n>=1.
Let sigma(x)=x^q and let U|x>=|sigma(x)> on the D1301 field register.
For each sigma-orbit O of length d|n and k in Z/d, put

    v_(O,k)=d^(-1/2) sum_(x in O)|x,sigma^k(x),x sigma^k(x)>.

Let G_(d,k) be the diagonal projector on precisely the computational
tuples appearing in this sum as O varies over length-d orbits. Put
G=sum_(d|n)sum_(k=0)^(d-1)G_(d,k), Delta=U tensor U tensor U, and
T=(1/n)sum_(j=0)^(n-1)Delta^j. Define P=TG and
P_d=T sum_k G_(d,k), Q_(d,k)=T G_(d,k). That these are self-adjoint
projections and have the advertised ranges is a claim. The Hilbert
register H_(E/K)^rel is ran P, with its inherited inner product.
For every n>=1 define the copied multiplication graph map
C:H_E->H_E^tensor3 by C|x>=|x,x,x^2>. Its arithmetic isometry
realization is established in CMP-REL.
No origin in an orbit is chosen. The square roots in the displayed
normalized vectors are positive real normalizations for analysis, not
additional coefficients required of their ambient projector matrices.

## D1603 (relative Frobenius and common observables)

For D1602 use the actual multiplication M=M_E^(2) of D1308 and set

    R=M (I tensor U tensor I) M^*,
    E_(d;a,b)=Q_(d,a) R^(a-b) Q_(d,b).

Let B_(E/K)^rel be the complex star algebra generated on ran P by R|ran P
and all Q_(d,k). Let B_n=direct-sum_(d|n)M_d(C), with matrix units e_(d;a,b),
and let u_n^rel=direct-sum_(d|n)S_d, S_d|k>=|k+1 mod d>.
The proposed comparison sends e_(d;a,b) to E_(d;a,b).
For n>1 the primitive relative component means the d=n component;
its abstract algebra is M_n(C). These common observables do not include
arbitrary operations on or between different orbit multiplicities.

## D1604 (copied reference preparation and retained histories)

For D1602 with n>1, let Pi_n project in H_E onto labels of sigma-period n.
Use C of D1602, realized by two zero ancillas,
controlled addition into the second slot, and M_E^(2) into the third.
For one input rho_E(h) of D1501, or lambda_E(h) of D1503, use the
three preparation Kraus amplitudes

    K_cut=I-Pi_n : H_E -> H_E,
    K_fail=(I-T)C Pi_n : H_E -> H_E^tensor3,
    K_ok=T C Pi_n : H_E -> H_E^tensor3.

Their output tags are primitive-cut failure, averaging failure, and success.
On success apply R, then measure the projection Q_(n,1), retaining its
complement. The other histories stop at their stated objects. In the
dephased comparison, the computational dephasing channel on all three
slots is inserted immediately before R. In the identity comparison R is
replaced by I. All comparisons use the same final projection, including T.
The two zero ancillas are fixed states, not additional POS references.

## D1605 (primitive relative quantum boundary)

For D1604 retain the D1506 order, leading probability coefficient and
conditional state on the common M_n observable algebra. The candidate
boundary realization has algebra M_n(C), state |0><0|, projections |k><k|,
the matrix units generated in D1603, and the channel Ad(S_n) on that block,
where S_n is the single n-cycle and u_n^rel is the all-period implementer.
Use the full graded physical preparation before any later continuation;
this definition does not identify physical multiplicity states across p.

The quantum boundary's arithmetic processes are those induced by the
displayed common matrices and specified instruments. A larger category of
all CP maps is an explicitly optional envelope. No tensor or sum operation
between boundary objects, and no conventional C_1, is stipulated.

## D1606 (fixed-base relational transfers and Fourier return)

For a named K-embedding i:E->F between finite extensions of the same
named K, let J_i be the D1304 label inclusion. Its candidate relational
isometry is J_i^rel=(J_i tensor J_i tensor J_i)|ran P_(E/K).
Its retained decoder has successful amplitude (J_i^rel)^* and failure
amplitude I-J_i^rel(J_i^rel)^*, with distinct target tags. Towers retain
every stopped history. Comparisons use all period components, with a
length-d component remaining length d in the larger ambient extension.

For D1602 with n>1 let F_first=F_E tensor I tensor I and retain, on the
primitive code, the return amplitude P_n F_first|ran P_n and the ambient
failure amplitude (I-P_n)F_first|ran P_n. Both outcomes are retained.
No invariance under Fourier on other slots is stipulated.

## D1607 (finite relational spectral data)

For D1602--D1603 use ordinary Hilbert trace on H_(E/K)^rel and the
characteristic polynomial det(I-zR|H_(E/K)^rel), including actual orbit
multiplicities. Also keep the separate normalized trace tr_d on a common
M_d block and the linear-map trace on its channel Ad(S_d).
For n>=1 let c_d(q) be D1331's exact-period polynomial evaluated at q.
The copied-reference spectral mixture is formed by applying C and T with
the success outcome retained, then uniformly randomizing over R^j,
0<=j<n, and explicitly discarding that classical randomization label.
For all n>=1 its copied map is C of D1602. The uniform channel can be
implemented using n copies of the amplitude R^j/n for every j, so no
additional square root is needed in the source scalar field. It is a
different preparation from the unrandomized witness of D1604. Moving-sector
conditioning of this mixture is defined only for n>1.

## D1611 (divisor corners and their concrete completion)

For N>=2 put A_N=direct-sum_(d|N,d>1) M_d(C), with operator norm the
maximum of its block norms. For N|M define j_(N,M) by extending block
coordinates by zero. Put eta_d=phi(d)/d and
theta_N(a)=sum_(d|N,d>1)eta_d tr_d(a_d), with tr_d=Tr/d.

Let H_deg=Hilbert-direct-sum_(d>=2) C^d, and define A_deg to be the
block-diagonal operator algebra of sequences a=(a_d) with ||a_d||->0,
in the supremum operator norm. Let B_deg=A_deg+C I_H be its concrete
minimal unitization. For positive a in A_deg define the extended-valued
functional theta(a)=sum_(d>=2)eta_d tr_d(a_d). The symbol H_deg denotes
the Hilbert space, not a Hamiltonian.

These are proposed concrete objects; norm completion, trace properties,
and comparison with the arithmetic corner embeddings are claims. No
endpoint tensor or coherent direct-sum operation on the distinguished
primitive systems is stipulated by this choice of completion.

## D1612 (completed Frobenius and positive degree regularization)

On D1611's Hilbert space define U_deg=direct-sum_(d>=2) S_d, with S_d
the actual relative-cycle matrix from D1603. Put
alpha(a)_d=S_d a_d S_d^*, fixing the scalar unit in B_deg.
For a real beta>1 define

    Z_deg(beta)=sum_(d>=2)phi(d)/d^(beta+1),
    D_beta=direct-sum_(d>=2)d^(-beta)I_d,
    rho_beta=direct-sum_(d>=2)[phi(d)/(Z_deg(beta)d^(beta+2))]I_d,
    omega_beta(a)=Tr_(H_deg)(rho_beta a).

Define zeta(x)=sum_(m>=1)m^(-x) for real x>1. For an integer j define
the implementing-operator moment
M_beta(j)=Tr_(H_deg)(rho_beta U_deg^j). This expression uses the named
Hilbert implementation: U_deg need not belong to B_deg itself.

The regulator D_beta is additional central degree-weight data for this
completion, not an arithmetic amplitude, a Frobenius generator, or a
claim that degree energy has been uniquely selected by the quantum theory.
No analytic continuation or infinite unregularized trace is stipulated.

## D1621 (degree-mixture preparation and normalized success profiles)

Fix an integer base degree s>=1, a real beta>1, and for each integer
d>=2 a named extension E_d/K with |K|=p^s and [E_d:K]=d. For an
integer cutoff D>=2 let L_D(beta)=sum_(d=2)^D d^(-beta). Prepare the
classical degree tag with probabilities d^(-beta)/L_D(beta), then prepare
the EXACT D1501 reference rho_(E_d)(log t) in that degree and apply the
three D1604 copied-reference preparation amplitudes. On its
success apply D1607's uniform relative randomization and explicitly
discard the randomization label. Keep every failed degree and its
primitive/averaging history. This degree prior is declared additional
classical preparation data, not an assertion that all such real weights
are coefficients of the original arithmetic amplitude source.

For t>1 set

    w_d(t)=c_d(t^s)/(d t^(sd)),
    v_d(t)=w_d(t)/(s(t-1)),
    Z_D(beta,t)=sum_(d=2)^D d^(-beta)v_d(t).

Set v_d(1)=phi(d)/d and use that value in Z_D(beta,1). On the named
Hilbert degree sum of D1611, define rho_(D,t) to have d-block
[d^(-beta)v_d(t)/(d Z_D(beta,t))]I_d for 2<=d<=D and zero elsewhere.
At t=1 this designates the retained first-grade conditional record,
not normalization of an actually successful zero-probability event.

Define L_infty(beta)=sum_(d>=2)d^(-beta),
Z_infty(beta,t)=sum_(d>=2)d^(-beta)v_d(t), and the corresponding
rho_(infty,t) by the same block formula when the sums converge. The
rho_beta of D1612 is the proposed t=1 value. The stated outputs are
restrictions to common quantum observables, not identifications of
physical arithmetic multiplicity states. Uniform randomization makes
this reference stationary under relative Frobenius; the unrandomized
D1604 experiment remains the separate coherence-sensitive witness.

# Symplectic Phantasm bootstrap — 2026-09-09

These are source-informed stipulations. Their properties are unpromoted
lemma contracts; adopting a definition does not admit its desired theorems.
The primary-source and postponed-definition inventory is
`docs/research-plans/symplectic-phantasm-sources.md`.

## D1701 (finite symplectic objects and affine symmetries)

Fix a finite field $k$ of characteristic $p$. A symplectic object is a
finite-dimensional $k$-vector space $V$ with a $k$-bilinear alternating form
$\omega_V$ whose radical is zero. Its rank is $n$ when $\dim_k V=2n$.
The zero space is allowed. Write $\overline V=(V,-\omega_V)$ and equip
$V\oplus W$ with $\omega_V\oplus\omega_W$. A subspace $L\subseteq V$ is
Lagrangian when $L=L^\perp$, where
$L^\perp=\{v:\omega_V(v,L)=0\}$.
The linear symmetry groupoid $\mathsf S_k$ has these objects and
form-preserving linear isomorphisms. The affine symmetry groupoid
$\mathsf S_k^{\mathrm{aff}}$ has arrows $(t,g):V\to W$, where
$g:V\to W$ is such an isomorphism and $t\in W$, acting by $v\mapsto gv+t$.
Composition is $(s,h)\circ(t,g)=(s+ht,hg)$ and the identity is $(0,1_V)$.

**Scope.** All characteristics are included in this classical datum. Rank one means dimension two; no quantum realization is part of the definition.

**Sources.** SP-GH07, SP-W09.

**Obligations.** SP-LREL, SP-WEYL, SP-EGOROV.

**Reuses.** D1,D14.

**Delta.** Arbitrary-rank finite symplectic objects and affine symmetry arrows; the rank-one field and local-ring forms retain their existing meanings.

## D1702 (affine Lagrangian relations)

Fix a finite field $k$ and finite-dimensional symplectic $k$-spaces $V,W$.
An arrow $R:V\to W$ is either the empty relation or an affine translate
of a Lagrangian linear subspace of $\overline V\oplus W$.
For $R:V\to W$ and $S:W\to Z$ prescribe
\[
 S\circ R=\{(v,z):\text{there exists }w\in W\text{ with }(v,w)\in R,
 (w,z)\in S\}.
\]
The identity is $\Delta_V=\{(v,v):v\in V\}$; the dagger is relational
converse. The product is the direct sum on objects and the Cartesian
product on relations, with coordinates reordered from
$(\overline V\oplus W)\oplus(\overline {V'}\oplus W')$ to
$\overline{V\oplus V'}\oplus(W\oplus W')$. The unit object is the zero
symplectic space. Write $\mathsf L_k^{\mathrm{aff}}$ for this candidate.

**Scope.** Closure and category/coherence laws are proof obligations. Empty relations are retained; nonlinear subvarieties are outside this definition.

**Sources.** SP-W09, SP-LW14, SP-CK21.

**Obligations.** SP-LREL, SP-STAB-REL.

**Reuses.** D1701.

**Delta.** The affine relation candidate with an explicit empty relation, sign and composition; it is not an existing flag-context category.

## D1703 (odd-characteristic Weyl datum in arbitrary rank)

Fix a finite field $k$ of odd characteristic, a nontrivial additive
character $\psi:k\to U(1)$, and a finite-dimensional symplectic
$k$-space $(V,\omega_V)$. Put $\beta_V=\omega_V/2$.
Extend the existing Weyl notation to $A_{\psi,\beta_V}(V)$, with basis
$\{W_{\beta_V}(v):v\in V\}$ and prescribed operations
\[
 W_{\beta_V}(v)W_{\beta_V}(z)
 =\psi(\omega_V(v,z)/2)W_{\beta_V}(v+z),\qquad
 W_{\beta_V}(v)^*=W_{\beta_V}(-v),\qquad 1=W_{\beta_V}(0).
\]
Prescribe $\tau_V(\sum_v c_vW_{\beta_V}(v))=c_0$. On $k\times V$
prescribe $(t,v)(t',z)=(t+t'+\omega_V(v,z)/2,v+z)$, with central
character $\psi$.
For $V=k^n\oplus k^n$ and
$\omega_V((a,b),(a',b'))=a\cdot b'-a'\cdot b$, let
$H_{k,n}=\ell^2(k^n)$ with counting inner product and its standard
coordinate identification with $\ell^2(k)^{\otimes n}$.
Use the distinct symmetrized-model notation
\[
 W^{\mathrm s}_{k,n}(a,b)
 =\psi(a\cdot b/2)\bigotimes_{j=1}^n W_{\beta_0}(a_j,b_j),
 \qquad
 (W^{\mathrm s}_{k,n}(a,b)f)(x)
 =\psi(-b\cdot x+a\cdot b/2)f(x-a).
\]
Here $W_{\beta_0}(a_j,b_j)\delta_y
=\psi(-b_j(y+a_j))\delta_{y+a_j}$ is the existing reference model.
An abstract-space model additionally names a symplectic coordinate
identification. At $n=0$ use $H_{k,0}=\mathbb C$ and the empty tensor.

**Scope.** The half-form convention excludes characteristic two. The finite-abelian realization is already admitted; SP-WEYL records its coordinate, phase and central-quotient transport.

**Sources.** SP-GH07, SP-PRASAD09, SP-GROSS06.

**Obligations.** SP-WEYL, SP-EGOROV, SP-TENSOR, SP-TRACE,DG-CHAR2.

**Reuses.** D3,D4,D5,D8,D1001,D1002,D1003,D1301,D1701.

**Delta.** Extend the existing Weyl algebra notation to arbitrary rank and fix a symmetrized model by rephasing D8, without reversing position labels.

## D1704 (actual stabilizer amplitudes)

Fix an odd prime $p$ and the reference root
$\zeta_p=\exp(2\pi i/p)$ in the trace-framed field registers. For the
ordered word $A=(\mathbb F_p,\ldots,\mathbb F_p)$ of length $n\geq0$,
use the existing full-scalar Pauli group $P_A$ and second hierarchy level
$C_2(A)$ on $H_{\mathbb F_p,n}=\ell^2(\mathbb F_p^n)$.
Define $\mathsf{Stab}^{\mathrm{amp}}_p$ to have these Hilbert spaces as
objects and actual linear maps generated under composition, tensor product
and adjoint by the unitaries in $C_2(A)$, the computational preparation
$\mathbb C\to H_{\mathbb F_p,1}$ sending $1$ to $\delta_0$, and every
scalar map $c:\mathbb C\to\mathbb C$ with $c\in\mathbb C$.
Use the coordinate identification
$H_{\mathbb F_p,m+n}=H_{\mathbb F_p,m}\otimes H_{\mathbb F_p,n}$.
Equality is equality of the resulting linear maps, including zero.

**Scope.** Scalars and amplitudes are retained. Such a map defines a physical successful branch only with the required norm or instrument normalization. No closure under addition is imposed here.

**Sources.** SP-GROSS06, SP-CK21.

**Obligations.** SP-STAB-REL, SP-SCALAR, SP-SUM,DG-REL-LIFT.

**Reuses.** D1301,D1307,D1703.

**Delta.** Only the generated category of actual complex stabilizer amplitudes is new. The Pauli group and Clifford level are those already defined in D1307.

## D1705 (stabilizer amplitudes modulo invertible scalars)

Fix an odd prime $p$ and the actual stabilizer amplitude category with
objects $\ell^2(\mathbb F_p^n)$. In each Hom-set identify two nonzero
maps $T,S$ precisely when $S=cT$ for some $c\in\mathbb C^\times$.
Keep the zero map in a separate class. Write
$\mathsf{Stab}^{\mathrm{proj}}_p$ for the quotient with the induced
composition, tensor product and adjoint. This scalar quotient is different
from quotienting unitary intertwiners only by $U(1)$.

**Scope.** The quotient records no success probability or norm. A coherent sum of independently rescaled representatives is not prescribed by this definition.

**Sources.** SP-CK21.

**Obligations.** SP-STAB-REL, SP-SCALAR.

**Reuses.** D1704.

**Delta.** A quotient by all nonzero complex scalars, keeping zero distinct; it is not the U(1)-only model quotient of D9.

## D1706 (finite quantum branches and instruments)

Extend the existing ordinary-trace CP target to a finite nonempty family
$X=(H_a)_{a\in A}$ of arbitrary nonzero finite-dimensional complex Hilbert
spaces. Use its existing notation
$B_X=\bigoplus_a\operatorname{End}(H_a)$ and
$\operatorname{Tr}_X=\sum_a\operatorname{Tr}_{H_a}$.
For another such family $Y=(K_b)_{b\in B}$, a branch
$\Phi:B_X\to B_Y$ is a linear map admitting finite Kraus lists
$K_{b a,j}:H_a\to K_b$ such that
\[
 \Phi(\rho)_b=\sum_{a,j}K_{b a,j}\rho_aK_{b a,j}^*,\qquad
 \sum_{b,j}K_{b a,j}^*K_{b a,j}\leq1_{H_a}\quad\text{for every }a.
\]
Branch equality is equality of the linear maps. A channel has equality
in every displayed inequality. An instrument has a finite nonempty outcome
set $O$ and branches $\Phi_o:B_X\to B_Y$ with a common source and target,
whose sum is a channel. Its retained version has codomain
$\bigoplus_{o\in O}B_Y$ and sends $\rho$ to $(\Phi_o(\rho))_o$.
Use the existing state and outcome convention: $\rho\geq0$,
$\operatorname{Tr}_X\rho=1$, outcome probability
$\operatorname{Tr}_Y\Phi_o(\rho)$, and conditional normalization only at
positive probability. Composition is composition of maps; tensor uses
Cartesian products of tags and ordinary Hilbert tensor factors.

**Scope.** This is an ambient finite quantum process definition. It does not assert that every branch comes from the arithmetic or stabilizer generators. Traces are ordinary, not dimension-normalized.

**Sources.** SP-WAT18.

**Obligations.** SP-CP, SP-SCALAR, SP-SUM, SP-SUBSYS.

**Reuses.** D1325,D1326,D1327.

**Delta.** Ambient Hilbert blocks and a matrix Kraus presentation extend D1326. Ordinary trace, outcome retention and conditional normalization are reused; D1325 source equality is not replaced.

## D1707 (coherent additive completion and classical tags)

Fix an odd prime $p$ and its actual stabilizer amplitude category.
First take the complex linear span of each Hom-set inside the ambient
linear maps. Its matrix completion has objects finite lists
$(H_{\mathbb F_p,n_1},\ldots,H_{\mathbb F_p,n_s})$, including the empty
list, and arrows matrices whose entries lie in these linear spans.
Composition is matrix multiplication and dagger is adjoint transpose.
Realize a list as $H=\bigoplus_{i=1}^sH_{\mathbb F_p,n_i}$.
Its coherent observable algebra is $\operatorname{End}(H)$.
For a nonempty list the tagged observable algebra is instead
$\bigoplus_i\operatorname{End}(H_{\mathbb F_p,n_i})$, embedded as the
block-diagonal operators on $H$. Both constructions and their chosen
block decomposition are recorded; they are not identified with one another.

**Scope.** This completion deliberately adds linear combinations. Whether it preserves a proposed Gaussian fragment, or comes from classical disjoint unions, is a separate question.

**Sources.** SP-CK21, SP-WAT18.

**Obligations.** SP-SUM,DG-RIG.

**Reuses.** D1704,D1706.

**Delta.** The complex linear and matrix completion of this particular stabilizer category; it is not the arithmetic R_p syntax or the graded Hecke completion.

## D1708 (bosonic Fock space and bounded second quantization)

For a complex Hilbert space $H$, let $P_r=(r!)^{-1}\sum_{\pi\in S_r}U_\pi$,
where $U_\pi(h_1\otimes\cdots\otimes h_r)=h_{\pi^{-1}(1)}\otimes\cdots\otimes h_{\pi^{-1}(r)}$, and set
$\operatorname{Sym}^rH=\operatorname{ran}P_r$, with
$\operatorname{Sym}^0H=\mathbb C$. Define
\[
 \Gamma_s(H)=\widehat{\bigoplus}_{r\geq0}\operatorname{Sym}^rH,
 \qquad\Omega=1\in\operatorname{Sym}^0H.
\]
The hat means Hilbert direct sum. The algebraic finite-particle space is
$\bigoplus_{r\geq0}^{\mathrm{alg}}\operatorname{Sym}^rH$.
For a contraction $T:H\to K$, prescribe
$\Gamma_s(T)=\bigoplus_{r\geq0}T^{\otimes r}|_{\operatorname{Sym}^rH}$.
Particle number is the operator $N_H\xi=(r\xi_r)_r$ on the domain
$\{\xi:\sum_r r^2\|\xi_r\|^2<\infty\}$.

**Scope.** Boundedness and functor laws are obligations. No bounded second quantization of an arbitrary expansive map is asserted, and no unspecified categorical free-monoid property is imposed.

**Sources.** SP-DER06.

**Obligations.** SP-FOCK,DG-RIG.

**Reuses.** D1010.

**Delta.** General Hilbert-space symmetric Fock functor and its contraction domain. D1010 already names the one-mode polynomial domain and its completion.

## D1709 (scalar restriction and a named Frobenius datum)

Let $E/K$ be a finite extension of finite fields, with $|K|=p^s$, and let
$(V,\omega_E)$ be a finite-dimensional symplectic $E$-space.
On $\operatorname{Res}_{E/K}V$ prescribe
$\omega_{\mathrm{Res}}(v,w)=\operatorname{Tr}_{E/K}(\omega_E(v,w))$.
For a named nontrivial additive character $\chi_K$, write
$\chi_{E/K}=\chi_K\circ\operatorname{Tr}_{E/K}$.
The notation $\psi_E$ remains reserved for the fixed absolute-trace family;
no equality with $\chi_{E/K}$ is stipulated for an arbitrary $\chi_K$.
Write $\sigma_{E/K}(x)=x^{|K|}=\sigma_E^s(x)$.
An abstract Frobenius datum additionally names a bijective
$\sigma_{E/K}$-semilinear map $\varphi_V:V\to V$ satisfying
$\omega_E(\varphi_Vv,\varphi_Vw)=\sigma_{E/K}(\omega_E(v,w))$.
On $E^n\oplus E^n$ use coordinatewise $\sigma_{E/K}$.
Its Hilbert permutation is
$U_{E/K,n}=(U_E^s)^{\otimes n}$ on $\ell^2(E^n)$, with the empty tensor
identity at $n=0$. The absolute permutations $\sigma_E,U_E$ keep their
existing meanings.

**Scope.** The classical data allow characteristic two; the half-form quantum comparison is restricted to odd characteristic. Abstract symplectic spaces do not acquire descent data by omission. This does not define a field-inclusion functor.

**Sources.** SP-STFIELD, SP-GH07.

**Obligations.** SP-TRACE, SP-FROB.

**Reuses.** D3,D1301,D1302,D1303,D1701.

**Delta.** Arbitrary-rank scalar restriction and general base character, explicitly distinguished from the fixed absolute-trace character and from field inclusion.

## D1710 (a specified quantum subsystem decoder)

Fix an odd-characteristic finite field $k$, a nontrivial additive
character, and a symplectic linear injection $j:U\to V$ between
finite-dimensional symplectic $k$-spaces. Put $W=j(U)^\perp$.
A quantum subsystem datum additionally specifies finite-dimensional
Weyl model Hilbert spaces $H_U,H_W,H_V$, with $W^{\mathrm s}_U$,
$W^{\mathrm s}_W$, $W^{\mathrm s}_V$ denoting the symmetrized operators
transported through their named coordinates, and a unitary
$J:H_U\otimes H_W\to H_V$ satisfying
\[
 J(W^{\mathrm s}_U(u)\otimes W^{\mathrm s}_W(w))J^*=W^{\mathrm s}_V(ju+w).
\]
Define the observable inclusion $\iota_J(a)=J(a\otimes1)J^*$ and the
state decoder $\mathcal D_J(\rho)=\operatorname{Tr}_{H_W}(J^*\rho J)$,
where the partial trace is specified by
$\operatorname{Tr}(\mathcal D_J(\rho)a)=\operatorname{Tr}(\rho\iota_J(a))$
for every $a\in\operatorname{End}(H_U)$.

**Scope.** The existence of the decomposition and compatible model unitary is an obligation. The datum is not scalar restriction, a generic field trace, or a non-bijective interpretation of finite-field Frobenius.

**Sources.** SP-STFIELD, SP-WAT18.

**Obligations.** SP-SUBSYS.

**Reuses.** D1701,D1703,D1706.

**Delta.** A nondegenerate symplectic subsystem and its trace-dual decoder. It is not the support-code decoder of D1327.

## D1711 (finite-prime tensor assembly with a chosen reference)

For every prime $p$, choose an integer $d_p\geq1$, a Hilbert space
$H_p=\mathbb C^{d_p}$ and a positive operator $\rho_p$ of trace one.
For a finite set of primes $P$, put
$A_P=\bigotimes_{p\in P}\operatorname{End}(H_p)$, using increasing prime
order, and $A_\varnothing=\mathbb C$. For $P\subseteq Q$ prescribe
$\iota_{QP}(a)=a\otimes1$ with the required coordinate reordering.
Define the candidate norm completion
$A_{\mathrm{pr}}=\overline{\varinjlim_P A_P}^{\|\cdot\|}$ using the
finite matrix norms. On finite tensors prescribe
$\varphi_{\mathrm{pr}}(\bigotimes_{p\in P}a_p)
=\prod_{p\in P}\operatorname{Tr}(\rho_pa_p)$.

**Scope.** The inductive and state-extension properties belong to a lemma. The matrices are specified data, not yet an all-prime Weyl assignment. Neither inter-prime arithmetic maps nor a factor type is supplied.

**Sources.** SP-CM08, SP-WAT18.

**Obligations.** SP-PRIME,DG-GLOBAL.

**Reuses.** D1706.

**Delta.** A specified unital inductive tensor system and reference; it is not the nonunital degree-block completion of D1611.

## D1712 (a represented Bost--Connes control system)

On $H_{\mathrm{BC}}=\ell^2(\mathbb N_{>0})$ with basis $(\delta_m)_{m\geq1}$,
fix the usual embedding $\mathbb Q/\mathbb Z\to U(1)$ given by
$r\mapsto\exp(2\pi i r)$, and prescribe
\[
 e(r)\delta_m=\exp(2\pi i mr)\delta_m,\qquad
 \mu_n\delta_m=\delta_{nm}\quad(n\geq1).
\]
Let $A_{\mathrm{BC}}^{\mathrm{rep}}=C^*(e(r),\mu_n:r\in\mathbb Q/\mathbb Z,
n\geq1)\subseteq B(H_{\mathrm{BC}})$.
Define $H_{\log}\delta_m=(\log m)\delta_m$ on
$\{\xi:\sum_m(\log m)^2|\xi_m|^2<\infty\}$ and prescribe
$\sigma_u(a)=e^{iuH_{\log}}ae^{-iuH_{\log}}$.
Define $\nu_n(a)=\mu_na\mu_n^*$ and $L_n(a)=\mu_n^*a\mu_n$.
For real $b>1$ prescribe
$Z_{\mathrm{BC}}(b)=\sum_{m\geq1}m^{-b}$ and
$\rho_{\mathrm{BC},b}=Z_{\mathrm{BC}}(b)^{-1}e^{-bH_{\log}}$.

**Scope.** This is a concrete represented control, not an assertion of faithfulness of a universal presentation or an identification with the sought symplectic system. Convergence, invariance and CP properties remain lemma obligations.

**Sources.** SP-BC95, SP-CM04, SP-CM08.

**Obligations.** SP-BC-CONTROL,DG-GLOBAL.

**Reuses.** none.

**Delta.** The concrete represented Bost--Connes benchmark. The degree regulator of D1612 has a different algebra and partition function.

## D1713 (state, GNS and modular comparison data)

A $C^*$-dynamical datum is a unital $C^*$-algebra $A$ with a point-norm
continuous homomorphism $\sigma:\mathbb R\to\operatorname{Aut}(A)$.
A state is a positive linear functional $\varphi$ with $\varphi(1)=1$.
Its GNS Hilbert space $H_\varphi$ is the prescribed completion of
$A/N_\varphi$ with
$N_\varphi=\{a:\varphi(a^*a)=0\}$ and
$\langle[a],[b]\rangle=\varphi(a^*b)$, left action
$\pi_\varphi(a)[b]=[ab]$, and cyclic vector $\Omega_\varphi=[1]$.
Write $M_\varphi=\pi_\varphi(A)''$.
For real $b>0$, a $\mathrm{KMS}_b$ state means that for every $a,c\in A$
there is a bounded continuous function on $0\leq\operatorname{Im}z\leq b$,
holomorphic in the interior, whose boundary values are
$F_{a,c}(u)=\varphi(a\sigma_u(c))$ and
$F_{a,c}(u+ib)=\varphi(\sigma_u(c)a)$.
A modular comparison datum additionally requires $\Omega_\varphi$ to be
cyclic and separating for $M_\varphi$. With
$S_\varphi(a\Omega_\varphi)=a^*\Omega_\varphi$ and polar decomposition
$\overline S_\varphi=J_\varphi\Delta_\varphi^{1/2}$, its modular-flow
prescription is $a\mapsto\Delta_\varphi^{iu}a\Delta_\varphi^{-iu}$.

**Scope.** Analytic existence and comparison theorems must be cited or proved before use. No equality between modular flow, the specified physical flow, or Frobenius is a stipulation.

**Sources.** SP-CM08, SP-CCM07.

**Obligations.** SP-PRIME,DG-MODULAR.

**Reuses.** D1122,D1326.

**Delta.** Extend the state conventions to a general C*-algebra and specify GNS and modular hypotheses; no new finite Born normalization is introduced.
