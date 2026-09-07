# Sidequest: arithmetic quantum mechanics over F_un

Opened **6 September 2026**. Literature-grounded exploration, separate from
the finite-local-ring and Atlas campaigns. Entry point for the accompanying
[labbook](../../labbook/main.pdf), section **“Sidequest: quantum mechanics
over the field with one element”**. Work order: [scope](../../briefs/f1-sidequest.md).

The north star is a precise formulation of quantum mechanics over `F_1`.
The immediate task is comparative: explore the developed analogies before
choosing which meaning of “over” should govern that formulation.

**Operational continuation, 7 September 2026:**
[Quantum mechanics in subsystem composition](f1-operational.md) constructs
a positive Hecke family and its endpoint A(S) = C[Sym(S)]. Its overlapping
subsystems intrinsically remember the arithmetic parameter; collective
qubits, genuine CP semantics, and a sharp context bound make the
subsystem-first proposal concrete. This is one developed branch of the
comparative map below, with the remaining Weyl/polarization gap stated explicitly.

**North-star clarification, 7 September 2026.** The user's primary object
is now explicitly the **family of subsystems and the ways they compose**.
Any proposed endpoint must admit a quantum operational realization:
C*-algebras, normalized positive functionals/density operators, CP dynamics,
Born probabilities, and compatible assembly of systems and processes.
The strategy is to extract an intrinsic compositional category from
arithmetic QM that still remembers p, then formulate a genuine p→1
specialization of that structure. Fibonacci illustrates the desired kind
of composition; it is not asserted to be the F1 answer.

In particular, a strong monoidal fibre functor to ordinary Hilbert spaces
is not imposed universally. The natural comparison from the tensor product
of local observable algebras into a composite algebra may be a proper
embedding: fusion observables can be collective. The source category and
its realization must specify channel extensions and state preparations on
these extra degrees of freedom. The classical and combinatorial models
surveyed below are potential inputs, not automatically acceptable quantum
endpoints. The earlier representation-category construction is one example
with a fibre functor, not a restriction on this broader research target.

A particularly relevant new literature entry is
[Comfort–Kissinger's graphical calculus](https://arxiv.org/abs/2105.06244),
Theorem 4.16: for odd primes, affine Lagrangian relations describe pure
stabilizer processes modulo invertible scalars. This is an arithmetic
process category whose objects, morphisms and composition remember p.
Its projective quotient alone omits normalization information needed for
the endpoint Born rule. [Comfort's mixed-state extension](https://arxiv.org/abs/2304.10584),
section 4, adds discarding/coisotropic relations for the indicated stabilizer
fragment. For the fusion comparison, see
[Bonderson–Shtengel–Slingerland](https://arxiv.org/abs/0707.4206), section 2,
on density operators, quantum traces and measurement, and
[Ahmadi–Kissinger](https://arxiv.org/abs/2211.03855) on categorical fusion
spaces and Fibonacci/Ising quantum computation.

## The answer suggested by the literature

There is substantial mathematics here. It supports several different
constructions, with different quantum content:

| Route | What survives or is constructed | Quantum interpretation |
|---|---|---|
| Tits and thin geometry | Incidence, coordinate polarizations, finite reflection groups | A combinatorial shadow of phase-space symmetry |
| Monoid schemes and cyclotomic extensions | Basis vectors, permutations, roots of unity | Phase-permutation kinematics after choosing a configuration object |
| Chang–Lewis–Minic–Takeuchi | A projective `q=1` specialization of finite-field amplitude models | A classical model with no superposition |
| Thas's absolute quantum theory | Frames, support orthogonality, partial Hermitian forms, monomial unitaries | A richer finite quantum-information analogy |
| Blueprints / Tits–Weyl models | An actual model of the reference group `UT_3` over `F_1` | Arithmetic Heisenberg geometry before choosing a representation |
| Bands and crowds | A relational Heisenberg law, with ordinary ring-valued groups | Partial or multivalued multiplication before arithmetic realization |
| Hall algebras and groupoidification | Creation/annihilation correspondences, oscillator CCR | Bosonic Fock quantum mechanics after additive realization |
| Exterior/fermionic analogy | Occupancy subsets, signs and parity-sensitive operations | A distinct graded categorical composition problem |
| Toric, cyclotomic and Habiro geometry | Lattices, torsion points, functions at roots of unity | A bridge to quantum tori and finite Weyl representations |
| Lambda geometry | Compatible Frobenius lifts as arithmetic descent data | A framework for testing descent of a quantum assignment |
| Bost–Connes endomotives | A published `F_1` model whose realization is a quantum statistical system | Noncommutative observables and genuine time evolution |
| Tropical, matroidal and motivic connections | Support/incidence, arithmetic sites, Feynman-integral geometry | Further geometric information; different from a Hilbert-space theory |

These are not competing answers to one already fixed definition. A useful
formulation should state which structures it retains and give comparison
maps where they exist. Our proposed finite Heisenberg construction is one
such comparison, not a replacement for the other routes.

## First distinguish the two roles of a field

In this project a finite field `κ` is an **arithmetic base**, while amplitudes
are complex. With a named additive character `ψ` and polarizing cocycle `β`,
the construction is

$$
H_\beta(\kappa)=\kappa\times\kappa^2,\qquad
(t,v)(t',v')=(t+t'+\beta(v,v'),v+v'),
$$
$$
W_\beta(v)W_\beta(v')=\psi(\beta(v,v'))W_\beta(v+v'),
\qquad \mathcal H=\ell^2(\kappa;\mathbb C).
$$

For the reference cocycle `β₀((a,b),(a',b'))=ab'`, the convention is exactly
`W(a,b)=Z(-b)X(a)`. This is the sign fixed in the project's
[definitions](../../definitions.md).

In contrast, the direct “quantum F_un” literature starts from *state
coefficients* in `F_q`. Chang et al. use projective finite-field states and
a probability rule that detects zero versus nonzero brackets. Their
`q=1` construction retains only the coordinate states. It does not take a
limit of this project's complex `q`-dimensional Schrödinger models.
See [Quantum F_un](https://arxiv.org/abs/1312.4191), §§2.1, 2.4, 3.2.

This distinction explains why “the limit becomes classical” and “the
Heisenberg algebra survives over finite-set combinatorics” can both be
correct. They refer to different constructions and different realizations.

## The qubit and tensor product in each picture

This is the principal comparison test for the sidequest. A “qubit analogue”
might mean two distinguishable states, a two-dimensional complex realization,
a simple object of categorical dimension two, or a two-label sector. Those
are different properties; each entry below states which one it supplies.

| Route | Candidate qubit | Composition of two copies |
|---|---|---|
| Free pointed `F_1` module / Chang coordinate states | Two nonzero basis points and a basepoint; two pure state rays | Smash product: four nonzero basis points. All native pure states are product states |
| Cyclotomic free module | Two free `μ_N` orbits; two projective native states, with phases retained before projectivization | Balanced smash product over `μ_N`; rank `2×2=4`. Complex realization is `C²⊗C²` |
| Thas frame | Rank-two projective frame with `N+2` rays; at `N=1` these are `10,01,11` | Kronecker products enter the rank-four frame. At `N=1` it has 15 nonzero states, of which 9 are products and 6 are nonproducts |
| Thin symplectic geometry | A position/momentum pair of coordinate polarizations; no Hilbert qubit is specified by that pair | Orthogonal direct sum of phase geometries and a product of their coordinate-choice sets; Hilbert tensoring needs realization |
| Blueprint Heisenberg model | Its chosen `F_2` fibre and reference cocycle give the order-eight dihedral group and its two-dimensional central-character module | Arithmetic phase-space direct sum, central product of represented Heisenberg groups, then Hilbert tensor |
| Signed/Krasner Heisenberg crowd | A finite relation object with 27/8 points; these cardinalities are not numbers of qubit states | Products of band schemes/crowd objects exist; identifying the physical composite requires a central extension and realization prescription |
| Hall/groupoid oscillator | No distinguished qubit in one oscillator. Two colours give a two-dimensional one-particle sector after realization | Disjoint union of colours gives tensor products of full Fock spaces. Two identical bosons in two modes give dimension 3, whereas two distinguishable qubits give dimension 4 |
| Fermionic/exterior analogy | Empty/occupied mode has underlying dimension two, but parity restricts its operations; a fixed-parity two-mode sector can encode a qubit | Graded Hilbert tensor with a fermionic exchange sign; this is an adjacent categorical model, not an established F1 quantization functor |
| Finite quantum torus | `VU=-UV`, `U²=V²=1` gives `M₂(C)` | Tensor product of the two algebras, equivalently a block-diagonal four-generator pairing, gives `M₄(C)` |
| Lambda descent | A qubit would be a specified arithmetic fibre plus phase datum; lambda structure alone selects no qubit | Descent-compatible correspondences and their realization must be supplied |
| Bost–Connes | Two chosen energy eigenvectors can encode a qubit; no distinguished two-state sector is preserved by the full observable algebra | Tensor products of quantum statistical systems after complex realization; no canonical qubit factorization of the arithmetic system |
| Tropical/matroidal/motivic routes | Support or incidence patterns may encode two labels; a positive two-dimensional quantum system is additional structure | Semiring tensor products, geometric products or categorical products depend on the chosen framework; they do not determine a Born rule |

For the two direct nonadditive state models, the contrast can be computed
exactly. In Thas's rank-`r` frame, the number of projective nonzero points is

$$
\frac{(N+1)^r-1}{N}.
$$

The reason is that `μ_N` acts freely on any nonzero tuple: fixing a tuple
fixes one of its nonzero coordinates and hence the scalar. At rank two
this is `N+2`. The Kronecker product of two projective rank-two frames is
injective on product rays, so there are `(N+2)²` product rays in the
rank-four frame, and

$$
\frac{(N+1)^4-1}{N}-(N+2)^2=N(N+1)(N+2)
$$

nonproduct rays. For example, `10;01`, viewed as a two-by-two coefficient
array, has diagonal support and cannot factor as a column times a row.
This is a **tensor-factorization notion of entanglement**, available even
without addition of states. It does not establish Hilbert-space interference,
a Born rule or Bell correlations. It also does not contradict Chang's
four-state composite: Chang's coordinate-only state object is smaller.
These counts are our derivation from Thas's definitions, not quoted results.

Strict pointed maps add another distinction: a morphism from the rank-one
unit can select only a simple vector. The nonsimple points of a Cartesian
frame are therefore extra state data, not automatically all morphisms from
the unit in the strict pointed-module category. A categorical formulation
has to decide whether to enlarge its morphisms, its state notion, or both.

There is a particularly direct **bare-pointed-set realization**. Keep the
normal partial maps of a rank-two pointed set. Sending one basis point to
another and the rest to zero gives each matrix unit `E_ij`; their complex
span is `M_2(C)`. Smash realizes canonically as Hilbert tensor, with
`E_ij smash E_kl` realizing as `E_ij⊗E_kl`. Thus this route supplies a qubit
after additive realization without first choosing a Heisenberg phase group.
The span is an image algebra: it is not the unreduced monoid algebra of
partial injections. At rank two the contracted monoid algebra has dimension
six, while the image has dimension four. This is our deduction from
[Szczesny's normal-map and base-change definitions](https://arxiv.org/abs/1204.5395),
pp. 5–8.

### A tensor-category qubit already visible in this project

The full category `Rep_C(H_N(A))` carries more structure than a chosen
Schrödinger representation. It is a symmetric fusion category with a
faithful tensor functor to finite-dimensional complex vector spaces
(or unitary representations with their usual Hilbert-space tensor).
It is graded by the characters of its central `μ_N`:

$$
\mathcal C_N(A)=\bigoplus_{\lambda\in\widehat{\mu_N}}
\mathcal C_N(A)_\lambda,\qquad
\mathcal C_N(A)_\lambda\otimes\mathcal C_N(A)_\nu
 \subseteq\mathcal C_N(A)_{\lambda\nu}.
$$

Consequently the fixed nontrivial central-character sector used by
Stone–von Neumann is generally **not a tensor subcategory**. This is a
positive reason to retain a tensor category: it remembers how sectors combine.

For `A=C₂`, `N=2`, the phase group is the order-eight dihedral group `D₈`.
It has four one-dimensional representations and one two-dimensional
irreducible `σ`. The latter is the qubit object, and

$$
\sigma\otimes\sigma\simeq
\mathbf1\oplus\alpha\oplus\beta\oplus\alpha\beta,
\qquad \alpha^2=\beta^2=\mathbf1.
$$

The quaternion group `Q₈`, which the main project encounters through its
other characteristic-two cocycle type, has the same fusion rules. Their
canonical Frobenius–Schur indicators of `σ` are respectively `+1` and `-1`.
Thus identical two-dimensional Hilbert spaces and identical fusion
multiplicities need not erase the underlying categorical distinction.
The character computation is recorded with the sidequest's exact checks.
[Shimizu's primary calculation](https://arxiv.org/abs/1005.4500), p. 20,
identifies these as the Tambara–Yamagami categories
`TY(F₂²,χ_alt,+1/2)` and `TY(F₂²,χ_alt,-1/2)`.

A necessary qualification is that `End_Rep(H)(σ)=C`, and for the nontrivial
central character `Hom_Rep(H)(1,σ)=0`. The equivariant category alone
therefore supplies neither all qubit observables nor all state vectors.
The fibre functor recovers the state space `ω(σ)=C²`, with observable
algebra `End_C(ω(σ))=M₂(C)`. A categorical formulation must retain that
realization, or replace it by a precisely specified state/observable
construction. Categorical dimension two by itself is insufficient.

Two tensor operations must be kept distinct here. The formula just above
uses the **same group's diagonal action** on a four-dimensional Hilbert
space. For two *independent* qubits, the symmetry is instead the central
product

$$
H_2(C_2)\mathbin{\boxdot}H_2(C_2)\simeq H_2(C_2\times C_2),
$$

of order 32, whose nontrivial-central-character irreducible has dimension
four. At the category level this is obtained by retaining matching central
characters in the external product of representation categories:

$$
\operatorname{Rep}(H_A\boxdot H_B)\simeq
\bigoplus_\lambda
\operatorname{Rep}(H_A)_\lambda\boxtimes
\operatorname{Rep}(H_B)_\lambda.
$$

The matching condition makes the antidiagonal central subgroup act trivially.
This is not an assertion that arbitrary sectors descend, nor an unspecified
relative tensor product. The right side is the full subcategory satisfying
that explicit condition, with its inherited tensor product.

The Hall analogue has a different categorical structure: two-linearization
retains the tower of `Rep(S_n)` and induction/restriction between degrees.
For example, `Rep(S₂)` has two simple objects, but two simple labels are
not by themselves a coherent qubit. With a two-colour one-particle
space `C²`, bosonic degree two is `Sym²(C²)`, a qutrit-sized sector.
Keeping the tensor category prevents these dimension and particle-statistics
distinctions from being lost.

Your proposed direction is therefore well motivated, with an important
qualification: a tensor category can be the primary quantum object and
ordinary Hilbert tensor products can be its realization. One need not
discard ordinary tensor products in every route. Free pointed modules,
frames, representation categories and categorical Fock spaces give
different precise composition laws worth comparing.

## 1. Thin geometry: what the familiar q→1 formulas really retain

Tits's analogy concerns finite geometries and their symmetry groups.
For fixed rank, Gaussian counting polynomials specialize to subset counts:

$$
\#\mathbb P^{r-1}(\mathbb F_q)=1+q+\cdots+q^{r-1}\longmapsto r,
\qquad {r\brack k}_q\longmapsto {r\choose k}.
$$

Thus the thin projective geometry has `r` coordinate points, with subsets
playing the role of subspaces. The corresponding linear symmetry is
`S_r`. In symplectic rank `r`, the reflection group is
`W(C_r)=(C_2)^r⋊S_r`: permutations of `r` symplectic pairs and exchanges
within pairs. This is a **Weyl group**, not the group of Weyl displacement
operators. These geometry/group comparisons are developed in
[Deitmar, Schemes over F1](https://arxiv.org/abs/math/0404185), §5, and
[Lorscheid's Tits–Weyl models](https://arxiv.org/abs/1201.1324), §3.

For quantum mechanics, the thin symplectic apartment supplies a useful
candidate polarization geometry. Selecting one direction from each pair
gives `2^r` coordinate Lagrangians, matching the polynomial specialization
`∏_{i=1}^r(q^i+1)→2^r`. This is incidence data, not an eigenbasis with
amplitudes. In rank one, the two directions suggest position and momentum;
the reflection exchanges them. Realizing that exchange by Fourier
transform requires phases and sums.

Three quantities must not be conflated: the rank `r` of an `F_1` module,
the field cardinality `q`, and a quantum deformation parameter. For example,
`|UT_3(F_q)|=q^3→1` is a specialization of a counting polynomial. It neither
proves the absence of an `F_1` model of `UT_3` nor defines a limit of groups.
Finite fields do not form a family with numerical cardinalities approaching 1.

## 2. Monoid schemes and cyclotomic phases

The minimal pointed monoid is `F_1={0,1}`, with absorbing zero and no
addition. A free rank-`r` pointed module has `r` nonzero basis points;
it is not a Cartesian cube with `2^r` elements. Its invertible linear maps
are permutations. For the cyclotomic pointed monoid
`F_{1^N}={0}∪μ_N`, a free rank-`r` module consists of `r` free `μ_N`
orbits and a basepoint. Its automorphisms are `μ_N^r⋊S_r`.
The free-root-of-unity-set viewpoint is explicitly used in
[Connes–Consani–Marcolli, Fun with F1](https://arxiv.org/abs/0806.2401), §3.

This is already enough to store clock and shift operators, since both
are monomial matrices. It is not enough to add state vectors or to perform
a Fourier transform as a map of free pointed modules.

The notation for an extension needs a convention. For a raw pointed
monoid its integral realization is the **group ring**
`Z[μ_N]≅Z[t]/(t^N-1)`. It is generally not the cyclotomic integer ring
`Z[ζ_N]`. The latter is a quotient that imposes cyclotomic additive
relations, or arises from an appropriate cyclotomic blueprint. A complex
phase realization further chooses a faithful character `ι:μ_N→U(1)`.
These distinctions are explained in
[Lorscheid, A blueprinted view on F1-geometry](https://arxiv.org/abs/1301.0083),
§1.1.4. Likewise, `μ_{q-1}` records multiplicative field data; the usual
finite-field Weyl phases are `μ_p`, arising from the **additive** group.

## 3. Existing absolute quantum theories

Chang et al.'s coordinate-state model and Thas's frame model should be
presented separately. Thas allows all tuples in `({0}∪μ_N)^r`, while retaining
the rule that addition is unavailable. His Hermitian expression is **partial**:
the displayed sum is meaningful only when it has at most one nonzero term.
Orthogonality becomes disjointness of supports. Reversible dynamics is
monomial; the unitary subgroup depends on the specified involution. For
the involution `z↦z^{-1}`, all phase-permutation matrices preserve the
partial form.

This gives a developed operator and quantum-information analogy, but not
an ordinary positive-definite Hilbert space. In particular, Thas's no-cloning
discussion distinguishes all frame states from simple projective rays:
the latter can be copied with a suitable permutation and a fixed blank
basis state. The deletion statements using singular “almost unitary” maps
are also different from deterministic unitary deletion in complex QM.
See [Thas, Absolute Quantum Theory](https://arxiv.org/abs/1808.09694),
§§3–4, 6–7, published in *Symmetry* 11 (2019), 174.

**Implication for this project.** There are at least three different state
objects to compare: a free pointed module, Thas's Cartesian frame, and its
complex linear realization. Their permitted states and their tensor
products carry different information. For instance, the complex vector
`(|00⟩+|11⟩)/√2` is a legitimate entangled state after complex realization;
it is not an element of a free pointed module. That does not invalidate
either construction; it identifies the structure added by realization.

## 4. An actual F1 model of the arithmetic Heisenberg group

There is a direct positive literature result here. Lorscheid proves that
standard-parabolic unipotent radicals of `GL_n` have Tits–Weyl models.
Take the upper-triangular Borel in `GL_3`. Its unipotent radical is

$$
h(a,b,t)=\begin{pmatrix}1&a&t\\0&1&b\\0&0&1\end{pmatrix},\qquad
h(a,b,t)h(a',b',t')=h(a+a',b+b',t+t'+ab').
$$

This is precisely the project's reference-cocycle Heisenberg group.
The underlying blue scheme of this model is affine three-space. Its
Weyl extension consists of one point, while its ring realization recovers
the full unipotent group. The two functors retain different information.
See [Tits–Weyl models](https://arxiv.org/abs/1201.1324), Proposition 5.5
and the preceding discussion of unipotent radicals.

Consequently, the first arithmetic-base target is already concrete:
start from that geometric Heisenberg model, realize it over a finite ring,
then take a named complex central-character quotient. The outstanding
questions concern the **representation and its descent**, not the bare
existence of this reference group model. The full polarizing-cocycle
torsor, particularly its characteristic-two types, is an additional problem.

Tits–Weyl models also retain a lift of reflection-group information over
the signed extension. That makes the comparison with Fourier and Weil
operators interesting, but a Tits extension is not automatically a
metaplectic extension. A splitting, a phase normalization, and a
character-compatible comparison must each be proved.

## 5. Bands and crowds: keep a relational Heisenberg law

The 2023 work of Lorscheid and Thas replaces a binary group operation by
a ternary **crowd relation**, modelled on `xyz=1`. It constructs algebraic
crowds over bands and recovers ordinary groups over rings. Over the Krasner
hyperfield, its type-A flags describe combinatorial flag varieties; the
symmetric group is a subcrowd of a generally larger relational object.
See [Towards the horizons of Tits's vision](https://arxiv.org/abs/2305.13809),
Theorems 1.1–1.2 and §§5.1–5.4.

**Our explicit specialization of that construction:** restrict the `SL_3`
crowd to `h(a,b,t)`. Its points over a band `B` are `B^3`. For triples
`(a_i,b_i,t_i)`, impose nullity of

$$
\sum_i a_i,\qquad \sum_i b_i,\qquad
t_1+t_2+t_3+a_1b_2+a_1b_3+a_2b_3,
$$

and the cyclic variants of the last expression. A null relation is band
structure; it is not an instruction to invent a binary addition.
Over any commutative ring these conditions give exactly `h₁h₂h₃=I`.

Over the regular partial field `F_1^±={0,±1}` there are 27 points.
There are 319 permitted triples, and only 23 points have an inverse within
this finite set. The product of two `a=1` elementary translations is
absent, but `h(1,0,0)h(0,1,0)=h(1,1,1)` exists and remembers the central
cross-term. A crowd product requires both an output and an inverse mediator;
merely having the integer matrix product in the set is insufficient.

Over the Krasner hyperfield there are eight points and 152 permitted
triples. Inverses can be multivalued. These counts are exact examples,
not a claim of an eight-element Heisenberg **group**.

This is a second precise candidate for Heisenberg geometry over `F_1`.
It has correct arithmetic realizations and retains nontrivial multiplication
relations before realization. A positive representation theory of these
relations is a separate north-star problem. The signed band is different
from the raw phase monoid, even though their underlying sets can agree.

## 6. A finite cyclotomic Heisenberg system

Here is a concrete bridge between the phase-permutation literature and
this project's finite Weyl systems. Fix a finite abelian group `A`, a phase
group `μ_N` with `exp(A)|N`, and a faithful `ι:μ_N→U(1)`. Put
`A^∨=Hom(A,μ_N)` and define

$$
H_N(A)=\mu_N\times A\times A^\vee,
$$
$$
(z,a,\chi)(w,b,\eta)
 =\bigl(zw\eta(a)^{-1},a+b,\chi\eta\bigr).
$$

Its Schrödinger action already exists on the pointed free `μ_N`-set
`E_N(A)={0}∪(μ_N×A)`:

$$
(z,a,\chi):(u,x)\longmapsto (zu\chi(x+a),x+a).
$$

Complex realization produces `C[A]` with its orthonormal basis, and

$$
W(a,\chi)e_x=\iota(\chi(x+a))e_{x+a},\qquad
W(a,\chi)W(b,\eta)=\iota(\eta(a)^{-1})W(a+b,\chi\eta).
$$

The commutator pairing is perfect; the realized twisted algebra is
`End_C(C[A])`; the fixed-central-character irreducible representation has
dimension `|A|`. These are finite-abelian Heisenberg facts, here exhibited
with an explicit cyclotomic pointed-module structure. They are not a claim
of a newly discovered Stone–von Neumann theorem over bare `F_1`.
The supporting [structured argument](../../theory/sidequests/f1-cyclotomic.md)
states the exact category, tensor comparison, and choices.

For a finite ring with generating character `ψ`, use `A=(R,+)` and
`χ_b(x)=ψ(-bx)`. Then this formula becomes **exactly** `Z(-b)X(a)`.
The raw ring Heisenberg group maps into the phase construction by
`(t,a,b)↦(ψ(t),a,χ_b)`. Its kernel is `ker ψ` in the centre; even a
generating character need not be faithful as a homomorphism of additive
groups. For `F_4`, the order-64 raw group maps onto an order-32 phase group.
The general comparison is a central pushout, not an identification of raw groups.

The construction is natural on group isomorphisms and respects products
at a common phase level. This is a definite functoriality statement; it
does not silently claim covariance under all homomorphisms of `A`.
At `N=1`, the exponent condition forces `A` to be trivial. This restriction
on a **perfect finite Weyl pairing** does not force every rank-`r` pointed
`F_1` module or every other `F_1` quantum construction to be trivial.

Fourier transform is the immediate extension problem: each Fourier column
has `|A|` nonzero coefficients, so for `|A|>1` it cannot be the realization
of a monomial map in this category. Enlarging the phase group alone does
not fix the support issue. Phase-labelled correspondences and their sums
are a natural next target, motivated by the following literature.

## 7. Hall and groupoid analogies: a different positive answer

Szczesny constructs Hall algebras of finite pointed monoid modules using
normal morphisms. At the one-point monoid, objects are finite pointed sets
and exact sequences count subsets. If `u_n` denotes the class with `n`
nonzero elements, the Hall product is

$$
u_m u_n={m+n\choose m}u_{m+n},\qquad u_n\longleftrightarrow x^n/n!.
$$

The Hall algebra itself is therefore a polynomial algebra after scalar
extension; it is **not by itself** the Weyl algebra. On `C[x]`, adjoining
the annihilation operator `D=d/dx` to creation by `x` gives

$$
[D,x]=1.
$$

See [On the Hall algebra of semigroup representations over F1](https://arxiv.org/abs/1204.5395),
§§2, 4–5. The displayed one-point example is rederived locally.

There is also a developed categorified version. Morton and Vicary model
Khovanov's Heisenberg category by spans of the groupoid of finite sets and
bijections. “Add then remove” decomposes into “remove then add” plus the
case where the removed element was just added. Linearization recovers
the oscillator. See [The Categorified Heisenberg Algebra I](https://arxiv.org/abs/1207.2054),
§§2.1–2.4, and [Khovanov's graphical calculus](https://arxiv.org/abs/1009.3295).
The interpretation of finite sets as `F_1` vector spaces connects these
papers to this sidequest; the span construction itself does not require
a choice among blueprint or lambda geometries.

With `⟨x^m,x^n⟩=δ_mn n!`, multiplication by `x` and `D` are adjoints
on the algebraic Fock domain. In the orthonormal basis `x^n/√n!`, their
coefficients are the usual square roots. Hilbert completion gives bosonic
Fock space; the unbounded CCR is asserted on the polynomial domain.
A finite cutoff cannot satisfy `[D,x]=I`, as its commutator has trace zero.

This analogy also clarifies second quantization: `S_r=GL_r(F_1)` becomes
the particle-permutation group, and the sequence of symmetric groups
controls creation/annihilation. Groupoid cardinality remembers the
automorphism weights `1/r!`; discarding those weights changes normalization.
See [Baez–Dolan, From finite sets to Feynman diagrams](https://arxiv.org/abs/math/0004133).
This oscillator is distinct from quantizing the finite plane `F_p^2`.

## 8. Tori, roots of unity and analytic interpolation

Before passing to tori, the **fermionic analogy** deserves its own place.
A one-mode fermionic algebra has two occupancy states and
`c²=(c†)²=0`, `cc†+c†c=1`; there is a published categorical construction
of that algebra and its Fock states in
[Lin–Wang–Wu–Yang (2013)](https://arxiv.org/abs/1307.4522), §§2–4.
Interpreting occupancy subsets as combinatorial exterior-power data is
our proposed F1 bridge, rather than a claim made by that paper.

[Hadzihasanovic–de Felice–Ng (2018)](https://doi.org/10.4230/LIPIcs.FSCD.2018.17),
§2, supply a precise monoidal category of local fermionic modes and maps
of definite parity. The basic object is `C^{1|1}`; tensor adds parity,
and the physical fermionic swap gives a minus sign to `|11⟩`. Thus the
two occupancy labels are not an unrestricted operational qubit. For
example, parity-preserving one-mode observables are diagonal, while
the two-mode odd sector spanned by `|10⟩,|01⟩` can encode a qubit.
Signed/cyclotomic F1 data are a plausible carrier for exchange signs;
the source proves the complex categorical theory, not its F1 descent.
This supplies another reason to keep the category and the realization
separate, and to distinguish bosonic, fermionic and distinguishable-system
composition.

The toric route has different inputs and limits.

A monoidal torus retains its character lattice `Λ`. A chosen integral
skew pairing on a lattice is a plausible arithmetic precursor of a
logarithmic symplectic form; it is additional data, not a consequence of
being a torus. A quantum torus is a twisted lattice group algebra.
For one pair, write `VU=ξ UV`. If `ξ` is a primitive `N`th root and the
central values `U^N=V^N=1` are fixed, clock and shift give the finite
matrix algebra `M_N(C)`. Without fixing central values, the rational
quantum torus is an infinite algebra over its centre. The lattice and
central-extension theory is developed in
[Neeb, On the classification of rational quantum tori](https://arxiv.org/abs/math/0511263).

Here `ξ→1` makes the torus algebra commutative. It is a deformation
specialization, distinct from a field-cardinality specialization and from
forgetting addition. At first order `VU=e^h UV` gives the log-canonical
Poisson bracket `{V,U}=UV`. This is a formal calculation over an additive
coefficient ring, not a Poisson bracket already defined on a bare monoid.

Manin's cyclotomic analytic geometry uses Habiro completions with
evaluations and Taylor expansions at roots of unity. This provides a
developed language for asking whether the *different cyclotomic
realizations* of a quantum construction belong to one arithmetic family.
See [Cyclotomy and analytic geometry over F1](https://arxiv.org/abs/0809.1564),
§§2–3. It does not itself construct an interpolation of the project's
Hilbert spaces or their Weil intertwiners. Such an interpolation must
specify its normalizations and its varying central-character fibres.

## 9. Frobenius descent and arithmetic quantum statistical mechanics

Borger proposes lambda structures as descent data below `Spec Z`.
For a scheme flat over `Z`, this can be expressed by commuting Frobenius
lifts, one for each prime. On a commutative monoid algebra, the standard
lift sends a monomial `m` to `m^p`. Tori and cyclotomic group schemes fit
this framework. See [Lambda-rings and the field with one element](https://arxiv.org/abs/0906.3146),
introduction and §2.2.

For QM, the question becomes: does the observable assignment possess
compatible arithmetic descent data? Applying `a↦a^p` coordinatewise to
the standard integral Heisenberg group does **not** preserve its group law:
addition and the cross-term obstruct it. This rejects that specific lift,
not every lambda structure or every form of quantization. More generally,
Frobenius-like endomorphisms need not act by invertible time evolutions.
Correspondences are a better candidate target than a group of unitaries
for all arithmetic maps. The project's existing character-compatibility
obstruction under field embeddings remains relevant.

The Bost–Connes system is a particularly strong positive precedent.
Connes, Consani and Marcolli construct an `F_1` model of its endomotive
whose scalar extension recovers the rational system. It uses the
cyclotomic tower and maps `σ_n(e(r))=e(nr)`, together with transfer
correspondences. The noncommutative realization has time evolution

$$
\sigma_t(\mu_n)=n^{it}\mu_n,\qquad \sigma_t(e(r))=e(r).
$$

See [Fun with F1](https://arxiv.org/abs/0806.2401), Proposition 6.1,
Theorem 6.2 and §4.1. In the standard complex representation on
`ℓ²(N_{>0})`, `H e_n=(log n)e_n`, so the partition function is
`Tr(e^{-βH})=ζ(β)` for `β>1`. The original analysis is in
[Bost–Connes (1995)](https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/CONNES/1994-1998/M_95_38/M_95_38_web.pdf),
§§2, 7. This is genuine quantum statistical dynamics, not a finite
Stone–von Neumann system in disguise.

The correspondence and categorical direction has developed further:
[Lieber–Manin–Marcolli](https://arxiv.org/abs/1901.00020), published in 2022,
lift Bost–Connes structures to Grothendieck rings, assembler categories,
spectra and Nori motives. This makes categorical output a literature-based
possibility for the project's north star, although no fusion-category
endpoint for our proposed finite `F_1` Heisenberg geometry is established here.

## 10. Tropical, matroidal, homotopical and motivic boundaries

Blueprints and bands connect `F_1` ideas with tropical and matroidal
geometry. Their value here is preserving support and incidence information
when ordinary addition is weakened. The Krasner hyperfield, Boolean
semiring, signed partial field and pointed monoid are different objects:
sharing the symbols `0,1` does not make their addition or null relations
interchangeable. In particular, the richer combinatorial flag varieties
in the band approach need not reduce to a single coordinate apartment.

Connes and Consani's [Arithmetic Site](https://arxiv.org/abs/1405.4527)
uses a tropical semiring on the topos associated with multiplicative
positive integers. It realizes arithmetic Frobenius correspondences and
relates its points to an adelic quotient. This is a geometric companion
to noncommutative arithmetic, not yet a prescription for local Weyl
algebras, positive states or a Born rule. Those are concrete questions for
a future comparison.

Relative and homotopical geometries enlarge the possible bases and
targets; Manin discusses this perspective in §1.10 of the cited cyclotomy
paper. Spectral and categorical structures are therefore plausible places
for information lost by sets. We have not found in the inspected sources
a corresponding general Stone–von Neumann statement over a sphere-like
or tropical base. This is a gap, not a proof of impossibility.

Finally, [Bejleri–Marcolli, Quantum field theory over F1](https://arxiv.org/abs/1209.4837)
studies torifications and the geometry of varieties associated with
Feynman integrals. Its introduction explicitly separates this question
from constructing physical Lagrangians and Feynman rules over `F_1`.
It belongs in the comparison because it is a developed QFT/F1 analogy,
but its title must not be cited as a solution of the present problem.

## Precise north stars and comparison problems

**Finite arithmetic formulation.** Fix the cyclotomic configuration
groupoid and the pointed-module realization of §6. This is a completely
specified finite kinematical theory: its input, phases, central extension,
observable algebra, tensor products and ring comparison are explicit.
Its projective Schrödinger realization is the first positive result to
verify. It should remain one component of the sidequest.

**Geometric formulation.** Fix the upper-unitriangular algebraic crowd of
§5 and compare it with the existing Tits–Weyl model. Require every finite
commutative-ring fibre to recover `H_{β₀}(R)`. A representation theory
must additionally specify how central characters are supplied and how
relations are realized. Ordinary group representations may be taken only
after the crowd becomes a group, or after a separately defined realization.
Extending this construction to general `β`, including characteristic-two
types, is an explicit open target.

**Categorical formulation.** Use pointed finite sets and add/remove
correspondences as the domain; recover the algebraic Fock representation
of §7 by additive realization. The developed categorical Heisenberg
theory is the starting point. The nontrivial comparison question is how
finite cyclotomic phase kernels can enrich those correspondences while
preserving adjoints, tensor composition and normalization.

**Arithmetic dynamics formulation.** Use cyclotomic endomotives and their
transfer maps, with Bost–Connes as the required worked example. Investigate
which finite Weyl algebras occur as compatible fibres, quotients or
corners, stating which one is meant. No identification of a Bost–Connes
system with the finite cyclotomic construction is asserted.

The unifying goal is a comparison diagram of these constructions. The
finite projective intertwiner functor now has an explicitly framed
cyclotomic matrix target and a stated monoidal domain; its supporting
argument is recorded as SKETCH. An earlier proposed geometric extension
named no definite category and was rejected during review. Geometric
descent and arithmetic dynamics remain research targets, rather than
being presented as a well-formed universal conjecture.

## Next experiments, without prematurely eliminating routes

| Experiment | What would count as a result |
|---|---|
| Rank-one Tits reflection / Fourier | Explicit comparison of a chosen Tits lift with the projective Fourier operator; all phases and squares checked |
| Nonreference Heisenberg geometry | Band/blueprint models for the two characteristic-two cocycle types, or a precise obstruction naming a replacement |
| Phase-labelled correspondences | An intrinsic composition rule for intertwiners with exact Gauss factors, natural in the phase embedding |
| Hall versus finite Weyl | A stated functor or correspondence relating particle creation to finite configuration quantization; an exact explanation if they are independent |
| Cyclotomic torus fibres | A central-fibre comparison with clock/shift, followed by a test of compatible changes of phase level |
| Bost–Connes finite sectors | Compute finite cyclotomic pieces and transfer maps; distinguish full matrix algebras from commutative cyclotomic observables |
| Arithmetic descent | Test explicitly named Frobenius lifts/correspondences against Weyl cocycles and the character-compatibility conditions |
| State-space comparison | Work out two-site states in the free module, Thas frame, complex realization and categorical Fock constructions |

## Evidence and limitations

Primary PDFs were retrieved, inspected and hashed; the durable record is
[refs/LEDGER.md](../../refs/LEDGER.md), under the F1 sidequest. The search
covered the direct absolute-QM papers, foundational geometric approaches,
newer band/crowd work, categorical Heisenberg papers and arithmetic
quantum-statistical constructions. Searches were followed into source
bodies; publication dates were distinguished from repository upload dates.

This is a substantive map of the relevant developed analogies, not an
exhaustive bibliography of all `F_1` geometry. The source search did not
establish a consensus universal definition of `F_1` QM or a single
published theory covering all these outputs. Missing comparison theorems
are explicitly left open. The finite checks, their deliberate failing
mutations, and the local proof status are recorded separately from what
the literature proves.
