# String-anchored trunk proposal: finite cyclotomic F1 kernel

These are lane proposals only.  Every mathematical row remains `SKETCH` until
the hostile critic and adjudication.  Apply no part independently of the
owning labbook update required by L11.  The high definition numbers are the
range reserved by `briefs/f1-sidequest.md` and do not collide with pending
FCR-2 definitions D17 onward.

## 1. `definitions.md`

Anchor: insert the following after the final paragraph of the current D16,
whose exact final sentence is:

> Every formula in D16 is uniform in the residue characteristic and uses no
> half.

```markdown
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

A *quadratic phase* is a map `q:A->mu_N` with `q(0)=1` for which
`B_q(a,x):=q(a+x)q(a)^(-1)q(x)^(-1)` is a bicharacter.  Put
`T_(t,f,q)[u,x]:=[u q(x),f(x)+t]` for `t in A`, `f in Aut(A)`.  The *strict
cyclotomic normalizer* is the normalizer of the D1003 `mu_N`-level Weyl group
inside `Aut_{Free_*^{mu_N}}(S_A)`.  Define

    F_A e_x:=sum_(rho in A^vee)iota(rho(x))e_rho,
    ev_a(rho):=rho(a),
    J_A(a,chi):=(chi^(-1),ev_a) in V_(A^vee),
    r_A(a,chi):=chi(a).

The exact normalizer, Fourier covariance, and failure of strict realization
are claim `F1-MON`.

## D1007 (cyclotomic correspondence target and lifted hyperbolic groupoid)

Let `K_N^cyc` be the rationalized group ring `Q tensor Z[mu_N]` modulo the
kernel of `u|->iota(u)`.  Define `CycCorr_N` to have finite free pointed
`mu_N`-sets as objects and matrices over `K_N^cyc` as morphisms, presented as
Grothendieck classes of finite `mu_N`-weighted correspondences between their
orbit sets; composition is fiber-product/sum and tensor is Cartesian product.
The functor `Real_iota:CycCorr_N->Vect_C` evaluates the weights by `iota`.
Let `P(CycCorr_N)` denote the groupoid of invertible morphisms modulo nonzero
central scalars.

Let `LiftHyp_N` have the D1002 data as objects.  A morphism `A->B` is a pair
`(g,r)` with `g:V_A->V_B` an isomorphism preserving `kappa` and
`r:V_A->mu_N` satisfying
`r(v)r(w)c_B(gv,gw)=c_A(v,w)r(v+w)`; composition is composition of the
resulting center-fixing maps `(u,v)|->(u r(v),g(v))` of phase groups.
The existence and geometric realization of the proposed quantization functor
is conjecture `F1-CORR`; neither a lift nor a Weil splitting is stipulated.
```

## 2. `notation.md`

Anchor: insert after the current row beginning
``| `mu_p`, `mu_4`, `U(1)` |``.  If pending D20 lands first, merge its `mu_N`
entry rather than duplicate it.

```markdown
| `N`, `mu_N`, `iota` | cyclotomic level; abstract cyclic phase group; named faithful complex character | D1001 |
| `A`, `A^vee`, `V_A` | finite abelian configuration group; its `mu_N`-dual; `A x A^vee` | D1002 |
| `c_A`, `kappa_A` | ordered Weyl cocycle `eta(a)^(-1)`; perfect commutator pairing | D1002 |
| `H_N(A)`, `H_N(A)^0`, `S_A` | cyclotomic Heisenberg group; group with zero; pointed Schrodinger module | D1003 |
| `C_iota`, `Free_*^{mu_N}` | cyclotomic complex realization; finite free pointed `mu_N`-sets | D1001 |
| `smash_mu`, `boxdot` | balanced smash product of phase sets; central product of phase groups | D1004 |
| `P_psi`, `chi_b` | central pushout of the raw ring Heisenberg group; `x|->psi(-bx)` | D1005 |
| `q`, `B_q`, `T_(t,f,q)` | quadratic phase; its bicharacter; strict affine-quadratic map | D1006 |
| `F_A`, `ev_a`, `J_A`, `r_A` | Fourier kernel; evaluation character; canonical polarization exchange and its lift cochain | D1006 |
| `K_N^cyc`, `CycCorr_N`, `LiftHyp_N`, `Q_N` | cyclotomic coefficient ring; weighted-correspondence target; lifted hyperbolic groupoid; conjectural functor | D1007 |
```

## 3. `claims/CLAIMS.md`

Anchor: insert after the exact current `FCR-REG` row and before the end of the
`## Rows` table.  All theorem rows deliberately remain `SKETCH`; checker
agreement is not promotion evidence.

```markdown
| `F1-DUAL` | For every `N>=1` and finite abelian `A` with `exp(A)|N`, restriction of `mu_N`-characters to a subgroup is surjective, characters separate points, `|A^vee|=|A|`, and `sum_a iota(chi(a)eta(a)^(-1))=|A|[chi=eta]` for every named faithful `iota` | SKETCH | D1001, D1002 | `theory/sidequests/f1-cyclotomic-kernel.md` §0 | `theory/checks/f1_check.py` (M2,M3) |
| `F1-WEYL` | For D1001--D1003, `c_A((a,chi),(b,eta))=eta(a)^(-1)` is a normalized cocycle, `H_N(A)` is a group with center exactly `mu_N`, `H_N(A)^0` acts faithfully on `S_A`, `W(v)W(w)=c_A(v,w)W(v+w)`, and the commutator `kappa_A` is perfect, uniformly including even `N` | SKETCH | D1001--D1003, F1-DUAL | `theory/sidequests/f1-cyclotomic-kernel.md` §1 | `theory/checks/f1_check.py` (M1,M2) |
| `F1-REAL` | For every named faithful `iota`, `C_iota(S_A)=C^A`, its `|A|^2` Weyl operators are trace-orthogonal and span `End_C(C^A)`, the twisted algebra is `M_|A|(C)`, and `H_N(A)` has a unique irreducible unitary representation with central character `iota`, of dimension `|A|`, with unitary intertwiners unique up to `U(1)` | SKETCH | D1001--D1003, F1-DUAL, F1-WEYL | `theory/sidequests/f1-cyclotomic-kernel.md` §2 | `theory/checks/f1_check.py` (M3) |
| `F1-FUNCT` | At fixed `N`, `A|->(S_A,H_N(A),C_iota(S_A))` is natural on `FinAb_N^iso` and strong symmetric monoidal: configurations use direct product, phase sets balanced smash, phase groups central product, and complex realizations Hilbert tensor product | SKETCH | D1001--D1004, F1-WEYL | `theory/sidequests/f1-cyclotomic-kernel.md` §3 | `theory/checks/f1_check.py` (M6) |
| `F1-RING` | For every finite commutative local `R` and named `psi:R->mu_N` with `iota o psi in Gen(R)` and `exp(R,+)|N`, `b|->(x|->psi(-bx))` identifies `(R,+)` with its `mu_N`-dual, `P_psi~=H_N((R,+))`, the raw map has central kernel `ker psi`, and realization along `iota` recovers exactly D8/D16's `W(a,b)=Z(-b)X(a)` and cocycle `psi_C(ab')`, including `p=2` | SKETCH | D12, D13, D16, D1001--D1005, F1-DUAL | `theory/sidequests/f1-cyclotomic-kernel.md` §4 | `theory/checks/f1_check.py` (M4,M5) |
| `F1-ONE` | At `N=1`, `exp(A)|1` forces `A=0` and the cyclotomic phase system is one-dimensional, whereas an ordinary free rank-`r` F1 module is a pointed set with arbitrary `r` non-basepoints; this construction is not a cardinality-`q` limit | SKETCH | D1001--D1004 | `theory/sidequests/f1-cyclotomic-kernel.md` §5 | `theory/checks/f1_check.py` (M1, trivial case) |
| `F1-MON` | The strict cyclotomic normalizer consists exactly, up to central phase, of `T_(t,f,q)` for `t in A`, `f in Aut(A)`, and a `mu_N`-valued quadratic phase `q`; its phase-space image is `(a,chi)|->(f(a),(chi B_q(a,-)) o f^(-1))`.  For `|A|>1` the Fourier kernel has full column support, so it is not the realization of a strict pointed map, though it is unitary after normalization and implements `J_A(a,chi)=(chi^(-1),ev_a)` projectively | SKETCH | D1001--D1003, D1006, F1-DUAL | `theory/sidequests/f1-cyclotomic-kernel.md` §6 | `theory/checks/f1_check.py` (M7) |
| `F1-CORR` | At every fixed `N>=2`, there exists a projective strong symmetric monoidal functor `Q_N:LiftHyp_N->P(CycCorr_N)` sending affine-quadratic lifts to strict maps and `J_A` to the `mu_N`-weighted Fourier correspondence, whose named-`iota` realization gives projective unitary Egorov intertwiners; moreover `CycCorr_N` is the finite-free correspondence sector of a specified cyclotomic blueprint, band, or comparable F1-geometric category | CONJECTURE | D1001--D1007, F1-FUNCT, F1-MON | — | — |
```

## 4. Owning theory and labbook files

If the capped review admits the rows, copy the repaired shard to the proposed
ground-truth home `theory/sidequests/f1-cyclotomic-kernel.md`.  L11 then
requires the orchestrator to add the owning self-contained labbook section in
the same commit.  This lane is forbidden to make either trunk edit.
