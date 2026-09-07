# A concrete operational F1 theory of subsystem contexts

**Sidequest result, 7 September 2026.** This develops the user's proposal to
study the category of arithmetic subsystems and assembly, retain the prime
intrinsically, and then seek a genuinely quantum `p=1` endpoint. It follows
the broader [literature map](f1-qm.md), with
[work order](../../briefs/f1-operational-target.md) and a new labbook section.

We obtained a positive candidate with an explicit specialization, not just
matching counts:

$$
\text{finite-field flags}
\longrightarrow \{H_n(q),\text{ subsystem inclusions},\tau_n\}
\xrightarrow{q=1}
\{\mathbb C[S_n],\text{ subsystem inclusions},\tau_n\}.
$$

Here `q=p^r` is the field size in arithmetic realizations; the intervening
Hecke parameter is defined for every real `q>0`. The endpoint is a family of
finite C*-quantum systems, with density operators, CP dynamics, Born
probabilities and collective degrees of freedom. It also admits an explicit
functor from the normal-map category of finite `F_1` modules.

The scope matters: this is the **flag-context sector extracted from a
polarized Weyl system**. It is not yet a specialization of the full Weyl
algebra, its phase datum, and every change of polarization. No uniqueness
claim for quantum mechanics over `F_1` is made.

## 1. The arithmetic can live in overlapping subsystem embeddings

At every `q>0`, the first three Hecke algebras have the same abstract types:

$$
H_1(q)=\mathbb C,\qquad H_2(q)\cong\mathbb C^2,\qquad
H_3(q)\cong\mathbb C\oplus\mathbb C\oplus M_2(\mathbb C).
$$

Yet the pair of overlapping inclusions

$$
H_2(q)\xrightarrow{\{1,2\}}H_3(q)
\xleftarrow{\{2,3\}}H_2(q)
$$

remembers the parameter. Compress the two pairs of minimal projections to
the unique `M_2` block and take the smallest ordinary matrix-trace overlap.
The result, independent of a basis and of labelling either pair, is

$$
a(q)=\min\operatorname{Tr}_2(PQ)=\frac{q}{(q+1)^2}.
$$

It determines `{q,q^{-1}}`, and therefore determines `q` uniquely on the
arithmetic range `q≥1`. Explicitly,

$$
q=\frac{1-2a+\sqrt{1-4a}}{2a}\quad(q\geq1).
$$

Thus it is not the list of algebras that feels the field. Their relative
embeddings do. This invariant can be formulated in the abstract monoidal
C*-category through the left and right copies of `End(x⊗x)` inside
`End(x⊗x⊗x)`, with the elementary object `x` retained.

See the [subsystem-overlap figure](../../labbook/figures/f1-operational-overlap.pdf).

| parameter | intrinsic overlap | return probability after the locally invisible unitary |
|---|---:|---:|
| `q=1` | `1/4` | `1/4` |
| `q=2` | `2/9` | `25/81` |
| `q=3` | `3/16` | `25/64` |
| `q=5` | `5/36` | `169/324` |

The third column is `(1-2a(q))²`, derived in §4 below. These are exact
rational values. The result is proved in
[the Hecke shard](../../theory/sidequests/f1-operational/hecke.md), §5.

## 2. Why the Hecke parameter really is arithmetic

For a finite field `k=F_Q`, choose an `n`-dimensional configuration
Lagrangian `L` of the Weyl system. A complete flag is a chain of
subspaces of dimensions `0,1,...,n`. The Hilbert space of context labels is
`K_ctx(L)=C[Fl(L)]`. Its invariant transition algebra is

$$
\operatorname{Cxt}(L)=
\operatorname{End}_{GL(L)}\bigl(\mathbb C[\operatorname{Fl}(L)]\bigr)
\cong H_n(Q).
$$

The generators change one subspace of a flag while holding the others
fixed. Each panel has `Q+1` flags, giving the relation

$$
T_i^2=(Q-1)T_i+Q\,1.
$$

Together with the braid and distant-commutation relations these are the
type-A Hecke relations. This is the classical finite-field construction
in [Iwahori (1964)](https://repository.dl.itc.u-tokyo.ac.jp/records/39909),
especially Lemma 3.1 and Theorems 3.2 and 4.1.

Replace `Q` in these relations by a positive real parameter `q`, retain
`T_i*=T_i`, and use the permutation basis `T_w`. The coefficient trace

$$
\tau_n(T_w)=\delta_{w,1},\qquad
\tau_n(T_u^*T_v)=\delta_{u,v}q^{\ell(u)}
$$

is faithful and positive. Left multiplication on its Hilbert space gives
a finite C*-algebra for every `q>0`. At prime powers the trace agrees with
normalized operator trace on the actual flag Hilbert space.

At `q=1`, the quadratic relation becomes `T_i²=1`, so the algebra is
exactly `C[S_n]`. This is evaluation of a based algebra presentation and
its structure maps. It neither invents a characteristic-one field nor
takes a sequence of prime numbers tending to one.

## 3. The endpoint is a quantum net on F1 modules

Write a finite pointed `F_1` module as `{*}∪S`. Normal morphisms are partial
injections of `S`, in the convention used by
[Szczesny](https://arxiv.org/abs/1204.5395), Definition 6. Define

$$
\mathcal A(S)=\mathbb C[\operatorname{Sym}(S)],\qquad
\tau_S\left(\sum_g a_g g\right)=a_1.
$$

An injection extends permutations by the identity and induces a unital
*-embedding of algebras. Its reverse map deletes coefficients outside the
subgroup. That reverse map is a trace-preserving conditional expectation
and is completely positive. The general expectation principle is classical;
the finite-dimensional amplification proof is written out locally, with
[Umegaki (1954)](https://doi.org/10.2748/tmj/1178245177) as a primary source.

For a partial injection `f:S⇀T`, first restrict to its domain by that
expectation, then relabel, then include into the target. This gives a
dagger functor into finite traced C*-algebras and bistochastic CP maps.
The empty partial map is the reference reset `a↦τ_S(a)1`, not the zero
CP map. This ordinary functor is not an additive base-extension functor.

The wedge operation of pointed modules becomes disjoint union of the
nonzero constituent sets. Its quantum assembly is the proper inclusion

$$
\mu_{S,T}:\mathcal A(S)\otimes\mathcal A(T)
\hookrightarrow\mathcal A(S\sqcup T).
$$

The maps are coherently associative and symmetric; the functor is **lax**
monoidal. They need not be isomorphisms. In particular, two scalar
one-constituent algebras assemble into `C[S_2]=C²`, and three constituents
have a collective `M_2` block.

All normalized states are positive functionals; using the coefficient
trace they have densities `h≥0`, `τ(h)=1`. Effects satisfy `0≤e≤1` and
the Born probability is `τ(he)`. Product preparations have density
`μ(h⊗k)`, and subgroup expectations give the corresponding marginals.
These statements are finite C*-quantum mechanics, not a substitute
probability rule.

Classical alternatives can separately be modelled by direct sums of
C*-algebras, with the state assigning probabilities to the central
summands. This is different from wedge-as-assembly, and from the coherent
direct sums in an additive amplitude category.

## 4. An explicit collective qubit experiment

In the unique `M_2` block of `H_3(q)`, the two subsystem projections can
be represented as

$$
P_1=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
P_2=\begin{pmatrix}a&\sqrt{a(1-a)}\\
\sqrt{a(1-a)}&1-a\end{pmatrix},\qquad a=\frac q{(q+1)^2}.
$$

Let `e_1=(T_1+1)/(q+1)` in the full algebra and `u_1=2e_1-1`.
This is a unitary. Its conjugation is the identity on the isolated
commutative left `H_2(q)`, but not on `H_3(q)`.

Prepare the standard-block pure state with density `P_2` and measure
`P_2`. The return probability is initially one and after `u_1` becomes
`(1-2a)²`. The full coefficient-trace density is

$$
h=\frac{1+q+q^2}{q}P_2,
$$

because the coefficient of ordinary trace on the standard block is
`q/(1+q+q²)`. At `q=1`, this is `h=3P_2`, and the probability changes
from one to `1/4`.

There is a direct preparation protocol. Assemble three reference states,
giving density `1`; measure the projection `P_2`. At `q=1` this succeeds
with probability `1/3` and prepares `3P_2` conditionally. Apply the local
transposition `(12)` and repeat the measurement. Every step is an ordinary
CP operation with the stated Born probabilities.

Two disjoint three-constituent standard sectors also support a Bell state.
The local `M_2⊗M_2` algebra embeds in `C[S_6]`; the conditional expectation
extends the Bell functional while preserving all local correlations.
The exact group-algebra example has density `9P_Bell`, maximally mixed
local qubit marginals, and the usual correlations giving CHSH `2√2`.
This supporting calculation is recorded in
[the comparison shard](../../theory/sidequests/f1-operational/flag-category.md), §6.

## 5. Which process data must survive composition?

The preceding unitary proves that equality of isolated CP maps is too
coarse for composing these systems. The same issue occurs for Fibonacci:
a braid can be locally invisible on the two-anyon charge algebra and
visible in a larger fusion space. The source formulas and the exact
comparison are in [the CP shard](../../theory/sidequests/f1-operational/cp.md).

A sufficient process description retains a normalized Kraus list
`K_i∈A(S)`, `ΣK_i* K_i=1`, and extends its operators into each ambient
algebra before taking their CP action. Lists compose by operator products
and act on disjoint regions through the block inclusion. Scalar unitary
mixing of Kraus indices gives the same process in every context.

At `q=1`, this can be made exact and minimal. Write
`K_i=Σ_h a_i(h)h`, for `h∈Sym(S)`, and define

$$
J_K(h,k)=\sum_i a_i(h)\overline{a_i(k)}.
$$

The admissible Grams are precisely

$$
J\geq0,\qquad \sum_hJ(hx,h)=\delta_{x,1}\quad(x\in\operatorname{Sym}(S)).
$$

In particular `Tr J=1`. They are positive process matrices with additional
normalization constraints. Equality of these matrices is equivalent to
stable scalar-unitary Kraus equivalence and to equality of every ambient
CP action.

**Sharp finite-context theorem.** For a local system of `n≥1`
constituents, one ambient system with `2n-1` constituents suffices to
recover every entry of `J`. For `n≥2`, this bound is optimal in the worst
case. Thus `n-1` ancillary constituents can be necessary.

The reason is concrete. Place a second copy of the local support so that
the two supports share exactly one point, and let an involution exchange
their other points. The two symmetric groups intersect trivially, making
all words `h^{-1}gk` distinct. The channel's value on `g` exposes every
Gram coefficient. With fewer points, trivial and sign sectors provide
two normalized processes that remain indistinguishable. The proof gives
an explicit positive density and effect separating them at the bound.
See [the context theorem](../../theory/sidequests/f1-operational/contexts.md).

For two constituents, all normalized inner Kraus processes have identity
isolated action because `A(S)=C²` is commutative. Nevertheless their Grams
form the disk
`J=[[r, ib],[-ib,1-r]]`, `b²≤r(1-r)`. A three-constituent context can
distinguish them. This is a particularly small illustration of why the
family of subsystems matters more than the isolated system.

The analogous sharp bound in the positive Hecke family has exact checks
at `q=2`, `n=2,3`, and a written double-coset proof strategy. It remains
SKETCH here; the promoted theorem is the `q=1` statement.

## 6. The actual partial-flag category

The construction need not stop at a tower of algebras. For a composition
`α` of `n`, let `W_α` be its Young subgroup and set

$$
P_\alpha(q)=\sum_{w\in W_\alpha}q^{\ell(w)},\qquad
e_\alpha=\frac{\sum_{w\in W_\alpha}T_w}{P_\alpha(q)}.
$$

Define a category by

$$
\operatorname{Hom}_{\Gamma_q}(\alpha,\beta)
=e_\beta H_n(q)e_\alpha
$$

for equal total rank, with zero Hom spaces between different ranks.
Composition is multiplication, adjoint is `*`, and tensor concatenates
compositions via the block Hecke inclusion. Its nonzero endomorphism
corners are positive C*-quantum systems. Finite sums and idempotent
splitting give its additive completion.

At prime powers these are exactly the intertwiner spaces between partial
flag permutation modules. Refinement is represented by typed averaging
projections; the physical corner trace is `P_α(q)τ_n`, not unscaled `τ_n`.
At `q=1`, the tensor powers of `(1)` have endomorphisms `C[S_n]`, the
linearized finite-bijection category. Other objects add partial-flag
retracts.

All formulas exist over the explicit localized ring
`Z[t,t^{-1},{P_α(t)^{-1}}]`. This supplies a based specialization mechanism,
with no unnamed category to be invented later. The category and its Weyl
coupling remain supporting SKETCH pending a dedicated review; the Hecke
algebra and endpoint operational theorems are independently reviewed.

There are no nonzero amplitude maps from rank zero to positive rank in
this graded category. Its operational envelope supplies normalized states
on the endomorphism algebras and additional preparations. Rigidity and a
strong monoidal Hilbert fibre are not being assumed.

## 7. How this attaches to the original Weyl system

For a subspace `U≤L`, averaging characters trivial on `U` gives

$$
P_U^Z=\frac1{|U^{\rm ann}|}\sum_{\chi\in U^{\rm ann}}Z(\chi)
=\sum_{x\in U}|x\rangle\langle x|.
$$

A flag is therefore a nested chain of commuting Weyl constraint
projections. `GL(L)` acts by the polarization-preserving Clifford
permutations and carries these chains equivariantly. The new flag Hilbert
space records these context labels coherently. On
`C[Fl(L)]⊗C[L]`, the controlled projections

$$
C_i=\sum_F|F\rangle\langle F|\otimes P_{U_i(F)}^Z
$$

couple the context register to actual Weyl constraints. This is a quantum
coupling, not just a numerical analogy. The construction names the field,
the Lagrangian, its origin and the phase data.

What remains missing is a specialization of the **whole** Weyl system and
these couplings, including affine displacements, changes of polarization
and the full symplectic action. The flag and Weyl Hilbert spaces have
dimensions `[n]_Q!` and `Q^n`; they are not identified.

There is also a direct **operational comparison** at every finite field.
Embed the coordinate-flag apartment in the full flag Hilbert space and
compress the invariant operators. This gives a basis-independent UCP map
`Omega_Q:H_n(Q)->C[S_n]`, `T_w↦w`, preserving the coefficient trace and
commuting with the ordered block inclusions and coefficient expectations.
It is a linear bijection, but not an algebra homomorphism for `Q>1`.
This supporting calculation is in the comparison shard, §7.

That CP comparison is distinct from evaluation of parameter-dependent
formulas: it sends `e_α(Q)` to `(|W_α|/P_α(Q))e_α(1)`. It therefore is
not automatically natural for the separately defined partial-flag corner
compressions. For a coarse flag, an internal generator compresses to
scalar `Q`, while the corresponding operation after the apartment map
compresses to scalar one. Compatible refinement-process comparison is
an explicit remaining problem, rather than a claimed solved square.

## 8. Other branches remain distinct

Full symplectic flags lead to type-C Hecke algebras and, at one, signed
permutation groups. Their rank-two group is `D_8` and has a qubit block.
But the block subgroup `B_m×B_n` is not parabolic in `B_{m+n}`. The type-A
assembly argument therefore does not automatically solve this branch.

The Temperley–Lieb quotient uses adjacent coefficient
`q/(1+q)²=δ^{-2}`, `δ=√q+1/√q`. At one this gives the `SU(2)` spin
tensor-power **centralizer tower**, after supplying the rank-two quotient
and a Jones/Markov state. It does not preserve the faithful flag state:
already at level two, flag weights are `(1/2,1/2)` while the spin
singlet/triplet weights are `(1/4,3/4)`. A full rigid-category interpretation
also needs its duality conventions. See
[Goodman–Wenzl](https://msp.org/pjm/1993/161-2/pjm-v161-n2-p05-p.pdf) and
[Bernstein–Frenkel–Khovanov](https://arxiv.org/abs/math/0002087).

Fibonacci instead uses a different root-of-unity Jones quotient and its
positive trace/star structure. It is an excellent operational comparison,
but is not forced by evaluation at one along the real positive flag family.
See [Kauffman–Lomonaco](https://arxiv.org/abs/0804.4304) and
[Iohara–Lehrer–Zhang](https://arxiv.org/abs/1707.01196).

## Status and next mathematical target

The reviewed results establish a positive, nontrivial operational endpoint,
intrinsic arithmetic memory in the subsystem diagram, and an exact
context-sensitive process quotient. They do not select a unique universal
`F_1` theory. The next central problem is extending the explicitly specified
flag/Weyl coupling and its coherent process structure through the same
specialization, while comparing other polarizations and the type-C route.

Proofs and scope are recorded in
[the adjudication](../../theory/verdicts/f1-operational-adjudication.md).
The [exact checker](../../theory/checks/f1_operational_check.py) has
fourteen aggregate mathematical gates and twenty-five data mutations.
Its sampled checks support the examples; the general statements rest on
the structured proofs and primary sources.
