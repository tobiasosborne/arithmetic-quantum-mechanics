# F1 sidequest: qubits, relational groups and tensor-category comparisons

These supporting derivations are **SKETCH**, not promoted results. They
were synthesized from the independent Sol landscape/Hall lanes and direct
coordinator recomputation. They have not received a dedicated hostile
round. Definitions D1008--D1013 are the single sources; source bodies and
locators are registered in `refs/LEDGER.md`. The positive finite phase
kernel has its separate proof and adjudication.

## 1. F1-CROWD — a relational arithmetic Heisenberg object

**ASSUME** a band as in D1008. **PROVE** the prescribed functor is an
affine algebraic crowd, and its restriction to commutative rings is UT3.

`<1>1.` Use the algebraic SL3 crowd constructed in
`refs/f1/2305.13809/paper.pdf`, section 5.4, printed pp. 12--13.
Its underlying functor is given by matrix coordinates, and its colaw
requires all three cyclic products to have entries of the identity in
the sense of null relations.

`<1>2.` Restrict the matrix coordinates by setting the diagonal to 1 and
the three lower triangular coordinates to 0. The determinant relation
then reduces to `1-1` and is automatic. The remaining coordinate band is
`F_1^pm[a,b,t]`, so the underlying functor is D1008's `B^3`.

`<1>3.` Direct matrix expansion leaves just `sum a_i`, `sum b_i` and
the three cyclic central expressions of D1008. Their null relations
present an affine band functor on nine coordinates. Hence both the
underlying object and colaw are representable, as required by the source's
Definition 5.9. This is a specialization of the published construction.

`<1>4.` Any identity-containing subset of a crowd inherits its axioms by
restricting the ternary relation: `(x,1,1)` iff `x=1` remains true, and
the two symmetry implications only permute entries of an existing triple.
These are exactly Definition 5.1's C1--C3. Thus the restriction is a crowd.

`<1>5.` For a ring, nullity means sum zero; the colaw is therefore
`h_1 h_2 h_3=I`. Invertibility makes the cyclic equations equivalent.
The ordinary multiplication is `h(a,b,t)h(c,d,u)=h(a+c,b+d,t+u+ad)`,
exactly D16's reference Heisenberg law.

`<1>6.` At the signed band there are 27 points. The inverse in UT3(Z)
is `h(-a,-b,ab-t)`. It lies in the signed subset except when `ab-t=2`
or `-2`: two choices of `(a,b)` for each sign give four failures, hence
23 points with inverses. The inherited crowd product has an additional
mediator requirement: for output `c=xy`, `c^(-1)` must also be in the
subset. In particular some `x*1` are empty. This is allowed by C1--C3;
it is why this object is not a partially defined ordinary group in the
usual sense of requiring all identities and inverses.

`<1>7.` Exact enumeration by `f1_check.py` M10 gives 319 signed triples,
and 152 triples on the eight Krasner points. The latter has a two-element
inverse set at `h(1,1,1)`. The checks expand actual three-by-three matrices
independently of the coordinate colaw and check C1--C3. These are finite
examples, not the evidence for the general affine statement.

`<1>8.` A nontrivial multiplication relation survives:
`h(1,0,0)*h(0,1,0)={h(1,1,1)}` in the signed example, whereas the square
of `h(1,0,0)` is absent. This names the forward route: representations
of relational groups, with arithmetic realization stated separately.
**QED** (supporting SKETCH)

## 2. F1-FRAME — qubit rays and nonproduct states without addition

**ASSUME** D1009, `N>=1`. **PROVE** the rank-two frame has `N+2` rays,
and its rank-four composite has `N(N+1)(N+2)` nonproduct rays.

`<1>1.` There are `(N+1)^r-1` nonzero rank-r tuples. Multiplication by
a scalar acts freely: inspect any nonzero coordinate, a member of the
group `mu_N`. Thus each orbit has N elements and
`|P_N(r)|=((N+1)^r-1)/N`.

`<1>2.` The Kronecker rule descends to rays because rescaling the two
factors rescales the product by their product. It is injective on rays.
Indeed if `x_i y_j=u x'_i y'_j`, choose indices `i0,j0` with nonzero
product. Their nonzero supports are rectangular and hence agree; dividing
the equality at `(i,j0)` by that at `(i0,j0)` proves all first-factor
coordinate ratios agree. The same argument works for the second factor.
The factors therefore differ by global phases.

`<1>3.` The rank-two count is N+2. Subtracting the `(N+2)^2` product
rays from the rank-four count gives `N(N+1)(N+2)`.

`<1>4.` The array `[[1,0],[0,1]]` has nonrectangular support and is a
nonproduct at every N. At N=1 the counts are 3, 15, 9 and 6 for one
system, full composite, product rays and nonproduct rays. At N=2 they
are 4, 40, 16 and 24. M11 checks the projective quotient and Segre image
directly, including N=3,4.

`<1>5.` The starting state definition is from Thas,
`refs/f1/1808.09694/paper.pdf`, section 3.2. The counting and factorization
proof here is our deduction. No probability, Bell nonlocality or Hilbert
inner product follows from a nonproduct support. **QED** (SKETCH)

## 3. F1-NORMAL — a bare pointed-set qubit after operator realization

**ASSUME** D1010 and a finite pointed set S of positive rank r.
**PROVE** `B(S)=End_C(L(S))`, and smash realizes as tensor product.

`<1>1.` For nonzero points i,j define the normal map taking j to i and
all other points to the basepoint. Its realization is the matrix unit
`E_ij`. These r-squared units span the full endomorphism algebra.

`<1>2.` Composition of normal maps realizes as matrix composition.
The adjoint of a realized partial injection is the realization of its
inverse partial injection. Thus B(S) is a star-algebra and equals M_r(C).

`<1>3.` The nonzero set of `S smash T` is the Cartesian product of the
nonzero sets. Sending its basis point `(s,t)` to `e_s tensor e_t` is a
canonical unitary `L(S smash T)~=L(S) tensor L(T)`.
Smashing matrix-unit maps gives `E_ij tensor E_kl`; these span the full
composite algebra. Coherence follows from associating tuples.

`<1>4.` L is a functor on normal maps; the algebra B is transported by
conjugation along bijections. We make no claim of a unital algebra map
`End L(S)->End L(T)` for every partial injection S->T.

`<1>5.` At r=2 this gives `(C^2,M_2(C))` and smash powers give the usual
complex tensor powers. Native vectors still have no coherent sums. If
only bijections are retained, their two permutation matrices span
`C I+C X`, a commutative algebra, so the partial maps matter.

`<1>6.` This is the concrete **image algebra**, not the unreduced monoid
algebra of all partial injections. For r=2 that monoid has seven elements,
including its zero map. Its contracted monoid algebra has dimension six,
while the image has dimension four; realization imposes additive
relations such as `I=E_00+E_11`. Source for normal maps, smash and base
change: Szczesny, `refs/f1/1204.5395/paper.pdf`, pp. 5--8.
**QED** (SKETCH)

## 4. F1-HALL — oscillator realization and tensor distinctions

**ASSUME** D1010. **PROVE** the Hall product is binomial, the polynomial
realization is compatible with it, and the dense-domain CCR holds.

`<1>1.` A pointed subset with n nonzero elements in V_(m+n) is a choice
of n out of m+n elements. The complementary quotient has rank m. Thus
`u_m u_n=binomial(m+n,n)u_(m+n)` by the Hall convention.

`<1>2.` The map `u_n -> x^n/n!` is a bijection of bases over Q and
preserves the product because factorial cancellation gives the coefficient
in `<1>1`. It identifies the Hall algebra with Q[x].

`<1>3.` On monomials, `a a^dagger x^n=(n+1)x^n` and
`a^dagger a x^n=n x^n`. Their difference is x^n and hence `[a,a^dagger]=I`
on all polynomials by linearity. Factorials in the stipulated inner
product make a and a^dagger mutually adjoint on that invariant domain.

`<1>4.` The normalized basis is `x^n/sqrt(n!)`. Completing its span
gives the usual Hilbert direct sum over n>=0. No claim is made that
the creation operator is bounded or that the CCR holds everywhere.

`<1>5.` The groupoid of pointed sets and bijections is equivalent to
FinBij by deleting/adjoining the basepoint. Baez--Dolan pp. 23--26 and
Morton--Vicary equations (15)--(19), Lemma 2.1 and Theorem 2.7 give the
positive categorical relation `A A^dagger ~= A^dagger A + id` by splitting
add/remove histories. This is a sourced categorical statement; the core
equivalence supplies our F1 interpretation.

`<1>6.` Wedge/disjoint union counts particle-number addition, whereas
smash counts multiplication of the dimension of configurations. With two
labelled colours the polynomial Fock space is C[x_0,x_1], whose one-particle
sector has basis x_0,x_1. Its two-particle sector has basis
`x_0^2,x_0 x_1,x_1^2`, hence dimension three. Independent distinguishable
one-particle sectors instead have tensor dimension four.

`<1>7.` A one-mode two-level cutoff has projected commutator
`diag(1,-1)`. More generally every finite cutoff has a top-state defect
balancing the trace. M8 and M9 verify subset counts and these boundary
identities, not an infinite-dimensional analytic theorem. **QED** (SKETCH)

## 5. F1-CAT — the sector-graded tensor category and external composition

**ASSUME** D1011. **PROVE** central-character grading, internal tensor
rule, and equivalence with matching sectors of the external product.

`<1>1.` Average any positive inner product over the finite group. Every
invariant subspace then has an invariant orthogonal complement. Thus
finite-dimensional representations are semisimple. Central finite-order
operators are simultaneously diagonalizable and their joint eigenspaces
are H-stable; these are the character sectors.

`<1>2.` On vectors in sectors lambda and nu, a central u acts on their
tensor by `lambda(u)nu(u)`. This is the asserted grading law. The unit
is in the trivial sector, so a nontrivial fixed sector is not itself a
unital tensor category. It is a module category over the trivial sector.

`<1>3.` Tensor, duals, direct sums, the symmetric swap and their usual
coherence maps are equivariant. There are finitely many simple modules
since the group algebra is finite-dimensional and semisimple. The unit
is simple and all Hom spaces are finite-dimensional: the full category
is a symmetric fusion category. The forgetful functor is faithful and
preserves tensor. A distinguished simple object requires the central
character iota from D1001; F1-REAL supplies that object.

`<1>4.` A representation of H x K factors through its antidiagonal
central quotient iff `(u,u^(-1))` acts as identity. Inflation along the
quotient and descent of the same operators are inverse tensor functors
on the indicated full subcategory. This proves the matching-product
equivalence without assuming a relative Deligne construction.

`<1>5.` Simple representations of a product are external tensors: one
can decompose under H, and commuting K acts on multiplicity spaces.
The kernel condition on an external simple is
`lambda(u)nu(u)^(-1)=1`, equivalent to lambda=nu. Hence the category has
the displayed direct sum of external matching sectors. Two copies of
the iota Schrödinger module descend, remain irreducible, and have
dimension `|A||B|` by F1-FUNCT and F1-REAL.

`<1>6.` Isomorphisms of A act covariantly by transport along `H(f)^(-1)`.
Matching products are coherent because iterating central quotients
identifies all phase centres independently of parenthesization. Their
unit on the image of this construction is Rep(mu_N), with one simple
in each grade; it is not Vec with its ordinary external product.
Together with omega and the distinguished iota sector this is a precise
categorical candidate for finite arithmetic QM. **QED** (SKETCH)

## 6. F1-FUSION — dihedral/quaternion qubit objects

**ASSUME** D1012. **PROVE** the stated irreducibles, tensor rules and signs.

`<1>1.` The cocycle is bilinear on F2^2, so gives an associative group.
The central involution z=(1,0,0) satisfies x y=z y x for the two coordinate
generators, and `x^2=y^2=z^e`. For e=0, xy has order four and x is a
reflection; for e=1 all six noncentral elements square to z. These
presentations identify D8 and Q8 respectively.

`<1>2.` D1012's matrices satisfy the same generator relations, and
I,X,Z,ZX span M2(C), so sigma_e is irreducible. Its trace is
`chi(t,a,b)=2(-1)^t` on the centre and zero elsewhere.

`<1>3.` Four characters factor through `G_e/<z>=C2^2`. The central
idempotent `(1+z)/2` gives its group algebra, diagonalized by those four
characters; `(1-z)/2` gives M2(C) by the four independent matrices above.
Both summands have dimension four. This exhausts the eight-dimensional
group algebra and proves that these are all irreducibles.

`<1>4.` Twisting sigma by any of the four characters leaves its trace
unchanged and hence gives sigma. Its squared character is four on the
centre and zero off it, exactly the sum of the four quotient characters.
By the explicit algebra decomposition of `<1>3`, this proves
`sigma tensor sigma = 1 + alpha + beta + alpha beta`.

`<1>5.` In D8, six elements square to 1 and two to z; in Q8 the counts
are reversed. D1012's indicator is therefore +1 and -1 respectively.
M12 recomputes the group squares and all four multiplicities exactly.

`<1>6.` Shimizu, `refs/f1/1005.4500/paper.pdf`, Definition 3.1 and
p. 20, identifies these tensor categories as the two Tambara--Yamagami
categories with group F2^2, alternating bicharacter and parameters +1/2
and -1/2. Thus the same fusion ring need not determine the category.
Internal fusion in `<1>4` concerns one diagonal group action; the
independent-system tensor of F1-CAT concerns a different group.
**QED** (supporting SKETCH; categorical identification sourced)

## 7. F1-TORUS — selected roots-of-unity fibres

**ASSUME** D1013 and xi primitive of order N. **PROVE** the selected
central fibre is M_N(C), including the N=2 qubit.

`<1>1.` The relation implies U^N,V^N commute with both generators.
In the selected fibre the N-squared words `U^a V^b`, 0<=a,b<N, span.

`<1>2.` On basis e_j indexed by Z/N, let U e_j=e_(j+1) and
V e_j=xi^j e_j. Then VU=xi UV and both Nth powers are identity.
Their N-squared products are trace-orthogonal by F1-DUAL, hence independent.
The surjective map from the spanning algebra to M_N(C) is an isomorphism.

`<1>3.` At N=2 these are the usual X,Z. Tensoring two selected fibres
gives the four-generator block-diagonal commutator form and M4(C).
At xi=1 the universal torus is commutative; retaining the relations
U^2=V^2=1 then gives C[C2^2], not M2(C).

`<1>4.` Neeb's source `refs/f1/math-0511263/paper.pdf`, introduction
and section 1, situates the calculation as a twisted lattice group algebra.
The additional F1 interpretation is a proposed bridge to monoidal tori;
it is not a claim that Neeb constructs F1 QM. **QED** (SKETCH)
