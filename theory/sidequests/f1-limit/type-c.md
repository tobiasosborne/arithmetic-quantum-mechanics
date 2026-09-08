# Decomposable flags give a positive type-C composition correspondence

Status: PROVED within the stated hypotheses. Admission and repaired scope
are recorded in `../../verdicts/f1-limit-adjudication.md`.

Primary anchors are Iwahori 1964, Theorems 3.2 and 4.1, for the finite
Chevalley flag Hecke algebra, and Curtis 1988, Proposition (1.6), for the
permutation commutant.  The decomposable-flag bijection and every CP map below
are derived here.  Exact locators are in `../../../refs/LEDGER.md`.

## 1. TC-DEC — decomposable flags and their full commutant corner

**ASSUME** symplectic spaces `V,W` over `k=F_Q` of dimensions `2m,2n`,
their symplectic groups `G_V,G_W`, and D1250--D1252.

**PROVE** decomposable complete isotropic flags have a canonical product plus
shuffle parametrization, and their local-symmetry commutant is the product
type-C context algebra with a full matrix shuffle register.

`<1>1.` Let `X(V)` be the set of complete isotropic flags

`0=U_0<U_1<...<U_m`, `dim U_i=i`,

where `U_m` is Lagrangian.  Put `K_V=C[X(V)]` with its flag basis orthonormal,
and similarly for `W` and `V orthogonal-sum W`.

`<1>2.` Let `Sh(m,n)` be the words of length `m+n` with `m` letters `V` and
`n` letters `W`.  For a word `sigma`, let `(a_r,b_r)` count its two letters
among the first `r` positions.

`<1>3.` Given `U in X(V)`, `Z in X(W)` and `sigma in Sh(m,n)`, define

`D_r=U_(a_r) direct-sum Z_(b_r)`, `0<=r<=m+n`.

This is a complete isotropic flag in `V orthogonal-sum W`.

`<2>1.` Each step increases exactly one summand dimension by one.

`<2>2.` Orthogonality of the direct sum makes every `D_r` isotropic.

`<2>3.` The last term `U_m direct-sum Z_n` has half the composite dimension,
so it is Lagrangian.

`<1>4.` Call a composite flag decomposable when it is obtained by `<1>3`.
The map

`d:X(V) times X(W) times Sh(m,n)->Dec(V,W)`

is bijective.

`<2>1.` From a decomposable flag, the dimensions of `D_r intersect V` and
`D_r intersect W` determine the word uniquely.

`<2>2.` The nonrepeated intersections with each summand recover the two
component flags uniquely.

`<2>3.` Construction `<1>3` is inverse to this recovery.

`<1>5.` The subgroup `H=G_V times G_W <= Sp(V orthogonal-sum W)` preserves
`Dec(V,W)` and acts only on the two flag factors under `d`; it fixes the
shuffle label.

`<1>6.` Linear extension of `d` is an H-equivariant unitary

`J_(V,W):K_V tensor K_W tensor l2(Sh(m,n))->K_dec`,

where `K_dec=C[Dec(V,W)]` is a subspace of the composite flag Hilbert space.

`<1>7.` Let `p_(V,W)` be the diagonal projection onto `K_dec`, and put

`D_(V,W)=End_H(K_(V orthogonal-sum W))`.

Then `p_(V,W) in D_(V,W)`.

`<2>1.` The subset is H-stable by `<1>5`, so its orthogonal projection
commutes with H.

`<1>8.` Define the arithmetic type-C context algebra

`A_C(V)=End_(G_V)(K_V)`.

Then `J_(V,W)` gives a star isomorphism

`p D_(V,W) p`
` ~= A_C(V) tensor A_C(W) tensor M_(Sh(m,n))(C)`.

`<2>1.` The corner is `End_H(K_dec)`.

`<2>2.` Under `<1>6`, the H-representation is the exterior tensor product on
`K_V tensor K_W` and the trivial representation on the shuffle factor.

`<2>3.` The commutant of an exterior tensor-product representation of a
product group is the tensor product of the two commutants.  A trivial factor
contributes its full matrix algebra.

`<1>9.` Iwahori--Curtis identifies `A_C(V)` with the arithmetic specialization
of the type-`C_m` Iwahori--Hecke algebra, and similarly in the other ranks.
Thus `<1>8` is an exact composition arena for the two local type-C context
algebras and a collective shuffle register.  **QED** (TC-DEC)

## 2. TC-CP — bidirectional trace-preserving UCP comparison

**ASSUME** D1250--D1253 and normalized operator trace on every displayed
finite-dimensional Hilbert space.

**PROVE** the full composite type-C context algebra and the decomposable
product-shuffle corner are related by mutually trace-adjoint UCP maps.

`<1>10.` Put `G=Sp(V orthogonal-sum W)`.  Since `H<=G`,

`A_C(V orthogonal-sum W)=End_G(K_(V orthogonal-sum W))`
` subset D_(V,W)`.

`<1>11.` Define compression

`Phi_(V,W)(a)=p a p`

from the full composite algebra to the corner `pDp`, whose unit is `p`.
It is unital and completely positive.

`<2>1.` Compression by an orthogonal projection is completely positive at
every matrix level.

`<2>2.` It sends the source unit to the target corner unit `p`.

`<1>12.` Let

`r_(V,W)=rank(p)/dim K_(V orthogonal-sum W)`

be the fraction of composite flags that are decomposable.

`<1>13.` Averaging the conjugates of `p` over `G` gives

`E_G(p)=|G|^(-1)sum_(g in G) U_g p U_g^*=r_(V,W) I`.

`<2>1.` The projection `p` is diagonal in the flag basis.

`<2>2.` The symplectic group acts transitively on complete isotropic flags.
Therefore every averaged diagonal entry is the same.

`<2>3.` Its normalized trace is unchanged by averaging and equals `r`, so
the common diagonal value is `r`.

`<1>14.` Compression is trace preserving for normalized traces:

`tr_p(pap)=tr_G(a)` for every `a in A_C(V orthogonal-sum W)`.

`<2>1.` Since `a` commutes with G,
`Tr(pa)=Tr(E_G(p)a)=r Tr(a)`.

`<2>2.` Divide the left side by `rank(p)=r dim(K)` and the right side by
`dim(K)`.

`<1>15.` For `x in pDp`, extend it by zero on `p^perp K` and define

`Psi_(V,W)(x)=r^(-1)E_G(x)`.

This is a unital completely positive map into `A_C(V orthogonal-sum W)`.

`<2>1.` Group averaging is a UCP conditional expectation from the full matrix
algebra onto `End_G(K)`.

`<2>2.` Positive scaling preserves complete positivity.

`<2>3.` Its value on the corner unit is `r^(-1)E_G(p)=I` by `<1>13`.

`<1>16.` `Psi` is trace preserving:

`tr_G(Psi(x))=r^(-1)Tr(x)/dim(K)=Tr(x)/rank(p)=tr_p(x)`.

`<1>17.` The two maps are adjoint for normalized traces:

`tr_p(Phi(a)x)=tr_G(a Psi(x))`.

`<2>1.` The left side is `Tr(ax)/(r dim K)` because `x=pxp`.

`<2>2.` Since `a` is G-fixed,
`Tr(aE_G(x))=Tr(E_G(ax))=Tr(ax)`.

`<2>3.` Substitution in the right side gives the same scalar.

`<1>18.` Through the isomorphism in TC-DEC, `Phi` is a bistochastic quantum
channel from the full composite type-C context observables to the local
product plus shuffle observables; `Psi` is its trace adjoint preparation.

`<1>19.` These maps do not assert that compression is multiplicative.
It is multiplicative exactly on elements that preserve the decomposable
subspace, and a generic full symplectic transition need not do so.
**QED** (TC-CP)

## 3. TC-COH — the correspondence composes associatively

**ASSUME** three symplectic spaces `U,V,W` of ranks `l,m,n` and D1254 (using D1251--D1253).

**PROVE** the decomposable restriction channels have canonical three-factor
coherence, including the shuffle register.

`<1>20.` Let `Sh(l,m,n)` be words in three letters with the prescribed
multiplicities.  A triple of component flags and such a word defines a
composite flag by taking the direct sum of the three current steps.

`<1>21.` There are canonical bijections

`Sh(l,m) times Sh(l+m,n) ~= Sh(l,m,n)`

and

`Sh(m,n) times Sh(l,m+n) ~= Sh(l,m,n)`.

`<2>1.` In the first bijection, expand every combined `UV` letter of the
outer word using the next letter of the inner `(U,V)` word.

`<2>2.` The second bijection expands combined `VW` letters instead.

`<2>3.` Both procedures recover the same three-letter word and are invertible
by collapsing the indicated pair of letters.

`<1>22.` Under these bijections and the ordinary Hilbert associator, both
iterations of the binary isometries `J` send a basis vector to the identical
three-summand flag.

`<1>23.` Hence both iterated decomposable projections equal the single
diagonal projection `p_(U,V,W)` onto three-summand decomposable flags.

`<1>24.` Compression by these projections therefore obeys the associative
identity

`Phi_(U,V,W)=Phi_((U,V),W) followed by Phi_(U,V)`

and the analogous right-associated identity, after the shuffle bijections.

`<1>25.` All maps preserve normalized traces by TC-CP.  Their trace adjoints
therefore obey the reverse associative identities, so the preparation maps
are coherent as well.

`<1>26.` The scalar normalizations agree explicitly because the proportions
multiply under nested restriction:

`r_(U,V,W)=r_((U,V),W) r_(U,V | inside U direct-sum V)`

and similarly on the other side.  This is also forced by equality of the
rank of the common projection in `<1>23`.

`<1>27.` Thus direct sum supplies an associative operational composition
correspondence, with its shuffle factor retained rather than discarded.
**QED** (TC-COH)

## 4. TC-ONE — the thin endpoint and the nonparabolic obstruction

**ASSUME** the type-C algebraic endpoint `A_C,n(1)=C[B_n]`, where `B_n` is
the signed permutation group, and D1255.

**PROVE** the block group and shuffle factor give the exact thin counterpart,
while ordinary generic parabolic Hecke induction does not supply it.

`<1>28.` Orthogonal direct sum embeds

`B_m times B_n -> B_(m+n)`

as signed permutations preserving the two coordinate blocks.

`<1>29.` This subgroup is proper for `m,n>0` and has full Coxeter rank
`m+n`.  It is not parabolic.

`<2>1.` Its index is
`|B_(m+n)|/(|B_m||B_n|)=binomial(m+n,m)>1`.

`<2>2.` A proper parabolic subgroup of a finite Coxeter group is conjugate to
one generated by a proper subset of simple reflections and hence has smaller
rank.

`<1>30.` Every signed permutation factors uniquely into a block signed
permutation and an unsigned `(m,n)` shuffle, after fixing left-versus-right
coset convention.  Therefore

`l2(B_(m+n)) ~= l2(B_m times B_n) tensor l2(Sh(m,n))`

as a representation of the block subgroup.

`<1>31.` Its block-group commutant is consequently

`C[B_m] tensor C[B_n] tensor M_(Sh(m,n))(C)`

up to the already fixed opposite/right-regular convention.  This is exactly
the `q=1` form of the product-shuffle arena in TC-DEC.

`<1>32.` In particular the group inclusion gives a unital star inclusion
`C[B_m] tensor C[B_n] -> C[B_(m+n)]` at the endpoint.

`<1>33.` For a finite arithmetic field, the decomposable fraction is

`r_(m,n)(Q)=binomial(m+n,m) P_(B_m)(Q)P_(B_n)(Q)/P_(B_(m+n))(Q)`,

where `P_(B_j)(Q)=sum_(w in B_j)Q^ell(w)` is the chamber count.

`<2>1.` TC-DEC counts the numerator as product flags times shuffles.

`<2>2.` Iwahori's Bruhat count gives the denominator.

`<1>34.` Formal evaluation gives `r_(m,n)(1)=1` because
`P_(B_j)(1)=|B_j|=2^j j!`.  The thin Coxeter complex is exhausted by the
block cosets and shuffle register, consistent with `<1>30`.

`<1>35.` Nonparabolicity means there is no standard generic subalgebra map
`H(B_m,q) tensor H(B_n,q)->H(B_(m+n),q)` obtained by selecting Dynkin nodes.
The arithmetic CP correspondence TC-CP and the endpoint group inclusion are
the positive statements proved here.

`<1>36.` A generic type-C bimodule or algebra map with compatible star,
reference trace and three-factor coherence remains additional data.  None is
deduced from an abstract semisimple algebra comparison.  **QED** (TC-ONE)

## 5. MIR-DEC — arithmetic affine-vector composition by the same method

**ASSUME** finite vector spaces `L,M`, their affine flag-vector Hilbert spaces
from D1241, and D1256 with D1254 coherence and the D1252--D1253 CP formulas.

**PROVE** decomposable type-A flags yield an arithmetic mirabolic composition
correspondence, without claiming a generic-q algebra homomorphism.

`<1>37.` Inside `Fl(L direct-sum M)`, decomposable full flags are again
parametrized by `Fl(L) times Fl(M) times Sh(dim L,dim M)`.

`<1>38.` Include every vector coordinate `(x,y) in L direct-sum M`.  Then

`C[Dec flags times (L direct-sum M)]`
` ~= C[Fl(L) times L] tensor C[Fl(M) times M] tensor l2(Sh)`.

`<1>39.` This is equivariant for
`(GL(L) semidirect L) times (GL(M) semidirect M)`.  Hence the corresponding
local-symmetry commutant corner is

`R_X(L) tensor R_X(M) tensor M_(Sh)(C)`.

`<1>40.` The full affine group of `L direct-sum M` is transitive on its
flag-vector Hilbert basis.  Averaging the decomposable projection therefore
gives its rank fraction times the identity, exactly as in `<1>13`.

`<1>41.` Compression from the full composite mirabolic commutant and scaled
full-affine averaging back are mutually trace-adjoint trace-preserving UCP
maps.  The proof is word-for-word `<1>10`--`<1>17` after replacing symplectic
groups and isotropic flags by affine groups and complete flags.

`<1>42.` The shuffle-bijection proof `<1>20`--`<1>26` gives three-factor
coherence at every prime-power arithmetic fibre.

`<1>43.` This constructs an arithmetic operational assembly correspondence
for the vector extension.  It does not prove that these CP maps are evaluations
of one positive generic mirabolic tensor category for all real `q>1`.
**QED** (MIR-DEC)

## 6. Exact scope

`<1>44.` TC-DEC through TC-COH give finite-field, finite-dimensional C*-data:
Hilbert spaces, corner algebras, normalized traces, UCP restriction and
preparation, and explicit associativity.

`<1>45.` TC-ONE gives the exact group-algebra endpoint comparison and proves
why standard parabolic Hecke assembly does not fill the generic gap.

`<1>46.` MIR-DEC gives the analogous positive arithmetic correspondence for
the affine-vector commutants.  Its generic deformation remains open and is
kept out of the proposed proved claims.
