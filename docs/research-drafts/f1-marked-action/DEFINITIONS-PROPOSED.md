# Proposed definitions D1271–D1276: one marked register and a Hecke right action

Prover: gpt-6-astra, xhigh. All definitions are lane proposals. Use the
bridge's D1245–D1248 orbit convention and the repaired D1249/D1257–D1258
regular boundary class. Set R_0(q)=H_0(q)=C, with their usual trace.

## D1271 (marked-unmarked ordered block map)

For m,n>=0, define the based linear map over C[q,q^(-1)] by

    rho_(m,n):R_m(q) tensor H_n(q) -> R_(m+n)(q),
    T_(u,A) tensor T_v |-> T_(u block v,A).

The tensor is over C[q,q^(-1)] before specialization and over C in a fibre.
Here u and v act on the first m and last n consecutive positions, and A is
an antichain in the first m positions in D1245's standard-pair coordinates.
For m=0 this is the zero-vector Hecke inclusion i_n. For n=0 it is identity.
Multiplication, star, injectivity and the trace assertions are theorems.
This definition does not give a map from R_m tensor R_n.

## D1272 (mixed block expectation and vector comparisons)

On the composite orbit basis, define

    F_(m,n)(T_(w,A)) = T_(u,A) tensor T_v

if w=u block v preserves the first m positions and A is contained in them,
and define it to be zero otherwise. This is the proposed traced expectation
onto D1271's image, with its product normalized trace. Write E_r for D1247's
vector expectation R_r->H_r and E^H_(m,n) for D1102's Hecke block expectation.
In particular F_(0,n)=E_n and F_(m,0)=id.

## D1273 (the raw and completed right Hecke-module categories)

The raw marked category C_R(q) has objects m>=0, End(m)=R_m(q), zero Homs
between different objects, multiplication as composition and the orbit star
as dagger. Let C_H(q) be D1221's Hecke skeleton. Their proposed right action
has `m triangleleft n=m+n` and morphism map rho_(m,n).

For q>1 let

    M_q=Kar_dagger(Add(C_R(q))),
    U_q^dagger=Kar_dagger(Add(C_H(q))).

A completed marked object X has finite-support projections
`p_m in M_(r_m)(R_m(q))`; morphisms are the full same-degree rectangular
corners, with matrix adjoint. A Hecke object Y has projections
`e_n in M_(s_n)(H_n(q))`. The degree-k projection of X triangleleft Y is the
block diagonal of the amplified rho_(m,n)(p_m tensor e_n), m+n=k, in the
single matrix algebra of size `sum_(m+n=k)r_m s_n` over R_k(q).
The whole corner includes off-diagonal Homs between these equal-total pairs.
Associators identify the named triple degree/matrix indices, preserving block
order. The unit acting on the right is the degree-zero Hecke object C.

For marked objects use `theta_X=sum_m Tr_(r_m) tensor tau_R,m`,
`d_X=theta_X(p_X)`, and `tau_X=theta_X/d_X` when X is nonzero; use D1263's
analogous Hecke convention on Y. These are finite tracial weights, not traces
asserted to arise from rigidity or fusion.

## D1274 (right-module induction form of the action)

For a finite-dimensional right R_m-module M and right H_n-module N, put

    M triangleleft N=(M tensor_C N)
       tensor_(R_m tensor H_n) R_(m+n),

where the left action on R_(m+n) is rho_(m,n), and the right action is
ordinary multiplication. The right Hecke-module category on the second
argument uses its usual induced tensor
`N star P=(N tensor P) tensor_(H_n tensor H_k) H_(n+k)`.
Extend both operations to finite-support graded sums. This is a statement
about right modules, not an objectwise tensor representation of R_(m+n).
Bare module categories are algebraic; the dagger model is the self-adjoint
matrix-corner presentation of D1273, or the corresponding projection Hilbert
modules with their explicit standard algebra-valued inner products.

## D1275 (reference boundary of the marked right action)

At q=1, use the algebraic based R_r(1), its trace-null ideal N_r of D1248,
and the unital star quotient Pi_r=E_r,1:R_r(1)->H_r(1). The raw reference
quotient category has the same objects and End(m)=R_m(1)/N_m.
It carries the right Hecke action only after the compatibility equations
with rho and F have been proved. This quotient is distinct from retaining
all modules of the algebraic R_r(1).

One-sided regular coefficients mean D1249's continuous orbit coefficients
on [1,1+epsilon], with density/effect positivity for every real q>1 there.
No boundary C*-norm is asserted. The algebraic quotient functor extends to
finite self-adjoint matrix presentations, allowing zero image objects.
No normalized operational state is assigned to a zero image projection.

## D1276 (one-marked collective assembly of regular processes)

Extend the repaired D1257 regular circuit category by the usual Hecke ordered
assembly/split boxes and by

    asm^R_(m,n):[R_m][H_n] -> [R_(m+n)],   Heisenberg map F_(m,n),
    spl^R_(m,n):[R_(m+n)] -> [R_m][H_n],   Heisenberg map rho_(m,n).

The zero-rank word is the scalar unit, so m=0 recovers up_n/down_n of D1257.
Also retain direct mixed lists rho_(m,n)(K_(o,i) tensor L_(p,j)) for a marked
list K and an unmarked Hecke list L; all outcome wires use the explicit
classical-wiring hypothesis W of D1257. Relations comprise their proved
right-module associativity, traced separated retraction, typed list laws,
and the existing sound circuit relations. Pointwise within-outcome Gram
equality is used for regular labels, not an arbitrary isolated-CP quotient.

The endpoint target is the corresponding Hecke category with ordered Hecke
assembly/split; the proposed evaluation replaces every marked atom by its
Hecke atom and uses Pi on its regular coefficients. All operational assertions
remain conditional on W. Two retained marked systems continue to use the
separate arithmetic D1256 shuffle correspondence; no faithful two-marked
algebra tensor inclusion is inferred from the one-marked action.
