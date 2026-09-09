# Fundamentals: the two categories, the Fock functor, and which limit to take

STATUS: steering discussion, recorded 2026-09-09. Not evidence. Nothing here
carries a claim status; every literature name below is a pointer that must be
registered in `refs/LEDGER.md` before it is cited (L3). TJO's framing is
recorded first, Claude's assessment second, so that the two can be told apart.

## 1. TJO's framing (verbatim intent)

The purpose of arithmetic quantum systems here is to find a candidate attack
on the Riemann hypothesis. The idea is old; the concrete route is not, because
this campaign does not shy away from the hard combinatorics.

Two categories are wanted, and the art is a "goldilocks" amount of structure.

**The classical arithmetic category C_p.** Associated to F_p. Objects:
symplectic vector spaces over F_p. Morphisms: symplectomorphisms; probably
the affine group of translations together with Sp(V); whether nonlinear maps
belong is open and delicate. Direct sums are allowed. Tensor-like products on
the classical side are suspect.

**The quantum category Q_p.** Objects induced by Weyl-Heisenberg projective
unitary representations built from C_p (a Lagrangian/polarisation and a
character). Q should be a functor C_p -> Q_p. Cliffords come from
symplectomorphisms. Q_p has direct sums and tensors and is a vanilla tensor
category whose morphisms are Gaussian operations. Tensor product in Q_p
arises from direct sum in C_p. Direct sums in Q_p correspond to total
particle number.

Side puzzle: higher Clifford-hierarchy gates are weird; what do they come
from on the C_p side? Functors? Natural transformations?

**The field with one element.** A one-dimensional V in C_p gives a qudit of
dimension p. At p=1 this is trivial. But the Fock / second-quantisation
functor shows that a trivial elementary input can produce a nontrivial output
(the harmonic-oscillator Fock space) once systems with an indeterminate number
of constituents are allowed. So p=1 can leave something behind; the game is
to leave "just enough" structure that the resulting quantum system has
nontrivial dynamics.

**Extensions and Frobenius.** C_p should really be C_p': symplectic spaces
over F_p and all its extensions, ultimately the algebraic closure. Forgetting
an extension identifies an F_{p^r}-space with an r-dimensional F_p-space; on
the quantum side forgetting is a CP map. Frobenius must be a morphism of C_p'
and of Q_p'. Powering forgets, so it ought to correspond to a partial trace.
C_p' is presumably implicitly studied; Q_p' may not be in the literature.
Q_p' should be a C*-algebra; a reference state and GNS give a von Neumann
algebra. Then set p=1 with Stone-von Neumann and the right normalisation, and
the bet (one beer) is that a quantum system with a vestigial, presumably
noncommutative, Frobenius action remains.

## 2. Assessment: the classical category

**Minimal honest C_p is affine symplectic.** The Weyl system is a projective
representation of the affine symplectic group V x| Sp(V), translations acting
as Weyl operators and Sp(V) as Cliffords. For odd p this lifts to a genuine
representation of the Jacobi group, so no cocycle needs to be carried.

**Nonlinear symplectomorphisms do not quantise as point maps.** In odd prime
dimension the only unitaries preserving Wigner positivity are Cliffords
(Gross). A cubic phase gate is therefore not the image of any bijection of
phase space. The side puzzle has a negative answer for "morphisms of V".

**Goldilocks candidate: Lagrangian correspondences.** Objects: symplectic
spaces over F_q. Morphisms V -> W: Lagrangian subspaces of V (+) W with the
sign-flipped form. This is Weinstein's symplectic category, rigorous rather
than heuristic over finite fields. Graphs of symplectic maps are the
isomorphisms; reductions, inclusions and projections are also morphisms. The
Weil representation extends to a functor on this category and its image is
exactly the Gaussian operations, partial isometries included (Gurevich and
Hadani, finite-field notes on canonical quantisation). This is the category
to build C_p around.

**Higher Cliffords as nonlinear Lagrangians.** A linear Lagrangian is the
graph of the differential of a quadratic form on the Lagrangian L. Degree-k
generating functions give nonlinear Lagrangian subvarieties, and the diagonal
gates of the k-th Clifford level are the quantisations of exactly those. The
hierarchy is thus the degree filtration on the function ring of L, not a
functor or a natural transformation. The extension to the full non-diagonal
levels is a conjecture of the assessment, unsourced.

## 3. Assessment: the quantum category and its two monoidal structures

**Direct sum to tensor forces a rig structure on C_p.** Q(V (+) W) =
Q(V) (x) Q(W) makes Q a symmetric monoidal functor from (+) to (x). The
direct sum on the Hilbert side then has no source in a category of vector
spaces, whose only monoidal structure is (+). To obtain Q(X u Y) = Q(X) (+)
Q(Y) the classical side must have disjoint union, i.e. C_p must be a category
of symplectic finite sets or varieties. The Fock functor is then the free
commutative monoid object in that rig category and "particle number" is the
grading by copies of the generator. This is Joyal-species combinatorics,
which is already F_1 combinatorics.

**Extensions add no quantum objects, only distinguished morphisms.** A
symplectic F_{p^r}-space with the trace form is a symplectic F_p-space of
dimension 2nr and the Weyl algebra is literally the same. Frobenius preserves
the trace form, sits inside Sp_{2r}(F_p), and quantises to an honest Clifford
unitary, a permutation in the computational basis. So Q_p' has the same
objects as Q_p and a richer symmetry structure. The "vestigial Frobenius" is
already a concrete operator before any limit.

**Partial trace is dual to inclusion.** Tracing out Q(W) restricts the
characteristic function to V inside V (+) W; classically this is the inclusion
V -> V (+) W acting contravariantly (Heisenberg picture). Allowing convex
combinations gives the Weyl-covariant Gaussian channels, classified by a
symplectic relation plus a noise character. The stochastic closure of the
Lagrangian category is the channel category wanted.

**The von Neumann type is a reference-state choice.** The infinite tensor
product over a tower is an ITPFI algebra: the tracial state gives the
hyperfinite II_1 factor, non-uniform product states give Powers type III
factors. The state choice is a temperature choice, and Tomita-Takesaki then
supplies a canonical modular flow.

## 4. Assessment: the limit is pointed at the wrong object

**Single-prime p -> 1 yields Soule's zeta, not Riemann's.** The campaign's
Frobenius-boundary work computes counts of monic irreducibles, i.e. the
Hasse-Weil zeta of the affine line over F_q. Its q -> 1 limit in Soule's
sense is 1/(s-1); every F_1-variety in that framework has a zeta that is a
product of factors 1/(s-k) (Soule, Deitmar). No nontrivial zeros appear.
Spec Z's zeta is not of that form. The "something is left over" bet is won,
but what is left over from one prime is a rational function of s.

**The object with zeta(s) as spectral data glues all primes.** The
Bost-Connes system is C*(Q/Z) x| N^x. Its partition function at inverse
temperature beta is zeta(beta), with a phase transition at beta = 1 and
Gal(Q^ab/Q) acting on ground states. Connes and Consani identify it as the
natural F_1 object, with F_{1^n} the n-th roots of unity in the
Kapranov-Smirnov sense. Three features match TJO's picture almost literally:

- The powering isometries mu_n conjugate roots of unity by averaging over
  n-th roots, a conditional expectation. That is "powering forgets" as a CP
  map, and it is where the noncommutativity lives.
- The ground-state Hilbert space is l^2(N) with Hamiltonian log n: a bosonic
  Fock space with one mode per prime at energy log p, the Euler product being
  the free-gas partition function. "Direct sum is particle number" is this,
  with primes as the elementary constituents.
- The arithmetic time evolution is the Tomita-Takesaki modular flow of the
  KMS state. Connes' "characteristic 1" reading is that modular flow is what
  Frobenius becomes in characteristic zero: the noncommutative vestigial
  Frobenius, made precise.

**Reframed plan.** Build Q_p for each p as above, with Frobenius as a
distinguished Clifford and the Galois tower as CP maps. Do not send p to 1.
Take the restricted tensor product over all p, choose the reference state,
and study the modular flow. The p -> 1 shadow is not a limit to take but the
common F_1 skeleton (hyperoctahedral groups W(C_n) = Sp_{2n}(F_1), roots of
unity F_{1^n}) that lets different primes talk to each other.

**Where the novelty would be.** Bost-Connes uses only the abelian part: roots
of unity and the multiplicative monoid. It never uses symplectic structure,
the Weyl algebra, or Sp. A "symplectic Bost-Connes system", each prime
contributing a Weyl-Heisenberg factor with the powering channels acting on
noncommutative data, is definable, and its hard combinatorics is the
primitive-orbit counting the labbook already does. Whether its Frobenius
spectrum relates to Connes' trace formula on the adele class space stays
labelled as an ambition, as HANDOFF already requires.

## 5. Literature to register before anything above is cited

- Weinstein, symplectic category / Lagrangian correspondences.
- Gurevich-Hadani, canonical quantisation of symplectic vector spaces over
  finite fields; Weil representation on correspondences.
- Gross, Hudson's theorem for finite-dimensional quantum systems (Wigner
  positivity and Cliffords).
- Soule, "Les varietes sur le corps a un element"; Deitmar on F_1 zetas.
- Kapranov-Smirnov, cohomology determinants and F_{1^n}.
- Bost-Connes (Selecta 1995); Connes-Consani, "Schemes over F_1 and zeta
  functions" and "Characteristic 1, entropy and the absolute point";
  Connes-Marcolli, Noncommutative Geometry, Quantum Fields and Motives.
- Tits, hyperoctahedral Weyl group as Sp over F_1.
- Julia / Bakas-Bowick / Spector, the free Riemann gas.
