# Finite-prime tensor limit, product state, and GNS representation

Lane model: `gpt-5.6-sol`, reasoning `xhigh`.

SP-PRIME is `PROVED` through
`theory/verdicts/phantasm-completions-adjudication.md`. Canonical definitions are D1711 and D1713. The finite-stage
identity insertions are proved directly; no source theorem is claimed for
this particular prime-indexed system. SP-WAT18 equation (2.18) supplies only
the finite product-state comparison, and SP-CM08 equations (4.117)--(4.119)
are the registered norm-completion/GNS comparison with stronger separating
hypotheses explicitly excluded here.

For a finite prime set `P`, write its tensor factors in increasing prime
order as prescribed by D1711.

## 1. The finite identity-insertion system

**ASSUME** finite prime sets `P subset Q`. **PROVE**
`iota_(Q P):A_P->A_Q` is an injective isometric unital star-homomorphism and
the embeddings compose.

<1>1. Increasing order gives a canonical permutation unitary

    H_Q ~= H_P tensor H_(Q\P),

under which D1711's formula is `a |-> a tensor 1_(Q\P)` on simple tensors
and then linearly.
**BY** reorder the finite tensor factors from increasing Q order into the
P factors followed by the complementary factors; conjugation by that fixed
unitary implements the same slot insertion.

<1>2. The prescription is well-defined on `A_P`: the tensor-product
multilinear map `(a_p) |-> tensor_q b_q` induces a unique complex-linear map
on the algebraic tensor product, which is already finite-dimensional and
complete.
**BY** the universal property of the finite algebraic tensor product and
D1711's linear extension.

<1>3. On simple tensors, identity insertion preserves products, adjoints,
and the unit; linearity and bilinearity extend these equalities to all
elements.
**BY** componentwise operations in finite matrix tensor products.

<1>4. Under `<1>1`,

    ||iota_(Q P)(a)||=||a tensor 1_(Q\P)||=||a||.

**BY** `<=` is the operator tensor-norm bound; for `>=`, choose unit vectors
`xi` attaining the finite-dimensional norm of `a` and any unit vector `eta`
in the nonzero missing-factor Hilbert space, so
`||(a tensor 1)(xi tensor eta)||=||a||`.

<1>5. Thus `iota_(Q P)` is isometric and hence injective.
**BY** `<1>4`.

<1>6. For `P subset Q subset R`, each R-slot receives `a_r` exactly when
`r in P` and identity otherwise, independently of whether insertion is
performed in one or two stages. Hence

    iota_(R Q)iota_(Q P)=iota_(R P),  iota_(P P)=1_(A_P).

**BY** D1711's explicit increasing-slot formula on simple tensors and
linearity.

<1>7. At the empty stage,

    iota_(Q empty)(c)=c tensor_(q in Q)1_(H_q),

and `<1>3`--`<1>6` remain valid, including Q empty.
**BY** D1711's separately prescribed scalar formula.

<1>8. **QED** the finite unital isometric inductive system.
**BY** `<1>1`--`<1>7`.

## 2. Algebraic limit and C-star completion

**PROVE** the isometric system has a well-defined unital algebraic direct
limit whose norm completion is a unital C-star algebra `A_pr`.

<1>1. Represent an algebraic-limit element by `(P,a)` and declare `(P,a)`
equivalent to `(Q,b)` when their images agree in some finite stage containing
both P and Q.
**BY** the directedness of finite prime sets under union and section 1
composition.

<1>2. Define addition and multiplication by moving two representatives to
`R=P union Q`, performing the operations in `A_R`, and taking the resulting
class; define star stagewise.
**BY** section 1 homomorphism/composition laws make a further-stage choice
give the same class.

<1>3. Put `||[(P,a)]||=||a||_(A_P)`. This is independent of representative.
**BY** section 1 isometry and the equivalence definition.

<1>4. The norm satisfies

    ||xy||<=||x||||y||,  ||x^*||=||x||,
    ||x^*x||=||x||^2

because representatives may be placed in one finite matrix C-star algebra.
**BY** the corresponding matrix-algebra identities and `<1>2`--`<1>3`.

<1>5. All finite-stage units have the same class by unitality of the
embeddings; this class is a two-sided algebraic-limit unit of norm one.
**BY** section 1 `<1>3` and `<1>6`.

<1>6. Complete this normed star algebra. Multiplication and star extend
uniquely because

    ||xy-x'y'||<=||x-x'||||y||+||x'||||y-y'||,
    ||x^*-y^*||=||x-y||,

and the C-star identity passes to limits.
**BY** `<1>4`, Cauchy approximation, and continuity of the norm.

<1>7. The common unit remains a unit in the completion, so the completion is
a unital C-star algebra. It is exactly D1711's `A_pr`.
**BY** `<1>5`--`<1>6` and density of the algebraic limit.

<1>8. **QED** the inductive norm completion.
**BY** `<1>1`--`<1>7`.

## 3. Compatible finite product states and extension

For each finite P put

    rho_P=tensor_(p in P)rho_p,  rho_empty=1,
    phi_P(a)=Tr(rho_P a).

**PROVE** these are compatible states and extend uniquely to a state
`phi_pr` on `A_pr`.

<1>1. Every `rho_P` is positive and

    Tr(rho_P)=product_(p in P)Tr(rho_p)=1.

**BY** tensor products of positive matrices are positive, finite trace
factorization, and D1711's trace-one choices; the empty product is one.

<1>2. Thus `phi_P(1)=1` and, for `a in A_P`,

    phi_P(a^*a)=Tr(rho_P^(1/2)a^*a rho_P^(1/2))>=0.

**BY** cyclicity of finite matrix trace and positivity of
`rho_P^(1/2)a^*a rho_P^(1/2)`.

<1>3. Diagonalize `rho_P=sum_i lambda_i|e_i><e_i|`. Then

    |phi_P(a)|<=sum_i lambda_i |<e_i,a e_i>|<=||a||,

so `||phi_P||=1` because equality holds at the unit.
**BY** positivity, `sum_i lambda_i=1`, and the operator-norm bound on matrix
coefficients.

<1>4. For `P subset Q`, after the increasing-order reordering one has
`rho_Q=rho_P tensor rho_(Q\P)`, and therefore

    phi_Q(iota_(Q P)(a))
      =phi_P(a) product_(q in Q\P)Tr(rho_q)=phi_P(a).

**BY** D1711's identity insertion and finite trace factorization.

<1>5. The compatible values define a positive unital functional `phi_0` on
the algebraic limit, with `|phi_0(x)|<=||x||`.
**BY** `<1>2`--`<1>4` and the stage-independent norm of section 2.

<1>6. For `x in A_pr`, choose algebraic-limit `x_n->x` and define
`phi_pr(x)=lim_n phi_0(x_n)`. This is well-defined, complex-linear, bounded
and unique.
**BY** the bound in `<1>5` makes values Cauchy and makes two approximating
sequences have the same limit; density gives uniqueness.

<1>7. It is unital and positive. For `x=y^*y`, approximate `y` by algebraic
`y_n`; continuity gives

    phi_pr(x)=lim_n phi_0(y_n^*y_n)>=0.

Every positive element has a positive square root in the C-star completion,
so this covers the positive cone.
**BY** section 2 multiplication/star continuity and the C-star square-root
property.

<1>8. Hence `phi_pr` is a state extending the prescribed finite product
formula.
**BY** `<1>6`--`<1>7`.

<1>9. **QED** existence and uniqueness of the prime product state.
**BY** `<1>1`--`<1>8`; SP-WAT18 equation (2.18) is the finite product-state
comparison only.

## 4. GNS quotient, bounded left action, and cyclicity

Use D1713 with `A=A_pr`, `phi=phi_pr`, and

    N_phi={a:phi(a^*a)=0}.

**PROVE** the GNS prescription yields a bounded star representation with a
cyclic reference vector and the represented von Neumann algebra in the
claim.

<1>1. Positivity gives Cauchy--Schwarz:

    |phi(a^*b)|^2<=phi(a^*a)phi(b^*b).

**BY** if `phi(a^*a)>0`, positivity of
`phi((b-lambda a)^*(b-lambda a))` at
`lambda=phi(a^*b)/phi(a^*a)` gives the inequality; if the denominator is
zero, positivity of `phi((a+t b)^*(a+t b))` for every complex `t` forces
the cross term `phi(a^*b)` to vanish (choose its opposite phase and let
`|t|` tend to zero). This gives the zero-right-side case.

<1>2. Therefore `N_phi` is a complex subspace and
`< [a],[b] >=phi(a^*b)` is a well-defined positive definite inner product on
`A_pr/N_phi`.
**BY** `<1>1`: null vectors pair to zero with every vector, so representatives
do not affect the pairing.

<1>3. `N_phi` is a left ideal. Indeed `c^*c<=||c||^2 1`, so

    phi((ca)^*(ca))=phi(a^*c^*ca)<=||c||^2phi(a^*a).

**BY** sandwich the positive operator `||c||^2 1-c^*c` by `a` and apply
the positive functional.

<1>4. Hence left multiplication `pi_phi(c)[a]=[ca]` is well-defined and

    ||pi_phi(c)[a]||<=||c||||[a]||.

It extends boundedly to the Hilbert completion `H_phi`.
**BY** `<1>3` and the displayed estimate, followed by Cauchy extension.

<1>5. On the dense quotient,

    <pi_phi(c)[a],[b]>=<[a],pi_phi(c^*)[b]>,

so the extension is a unital star representation.
**BY** associativity, the definition of the inner product, and section 2's
common unit.

<1>6. The vector `Omega_phi=[1]` is cyclic because
`pi_phi(a)Omega_phi=[a]`, and quotient classes are dense by construction.
**BY** D1713 and `<1>4`.

<1>7. Put `M_phi=pi_phi(A_pr)''`; this is the represented von Neumann
algebra named in D1713 and SP-PRIME.
**BY** D1713's double-commutant prescription.

<1>8. No faithfulness of the state or representation and no separating
property of `Omega_phi` is inferred. If some `d_p>1` and local `rho_p` is pure, the local
projection `q` orthogonal to its support satisfies `pi_phi(q)Omega_phi=0`.
It is represented nontrivially: choose a local matrix unit `a=|f><e|` from
the support vector `e` to a unit vector `f` in `ran q`; then `qa=a` and
`||[a]||^2=phi(a^*a)=1`, so `pi_phi(q)[a]=[a]!=0`. This exhibits the allowed
cyclic-but-nonseparating boundary.
**BY** the product-state formula and D1711's permission for a pure local
density; no conclusion about faithfulness of the full state or representation
is drawn.

<1>9. **QED** the GNS and cyclicity clauses with the null-ideal boundedness
explicit.
**BY** `<1>1`--`<1>8`.

## 5. Exact canonical conclusion

<1>1. The finite prime stages form an isometric unital inductive system and
its norm completion is a unital C-star algebra.
**BY** sections 1--2.

<1>2. The chosen finite product states extend uniquely to a state.
**BY** section 3.

<1>3. D1713's GNS construction yields the represented von Neumann algebra
with a cyclic reference vector.
**BY** section 4.

<1>4. No inter-prime arithmetic coupling, all-prime Weyl assignment,
faithfulness, factor type, separating vector or modular datum is asserted.
**BY** D1711--D1713 Scopes and section 4 `<1>8`.

<1>5. **QED** the exact canonical SP-PRIME statement.
**BY** `<1>1`--`<1>4`, D1711 and D1713 at their stated scopes.
