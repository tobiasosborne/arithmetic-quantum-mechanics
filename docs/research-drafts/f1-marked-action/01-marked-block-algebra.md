# One marked block admits a generic right Hecke action

Prover: gpt-6-astra, xhigh. Status: SKETCH, candidate for a separate blind
review. Definitions D1271–D1272 are in this lane. The inputs are Rosso's
based polynomial algebra and the bridge's verified MIR-AFF/VAL/POS/EXPECT/END,
with D1245's antichain coordinates. The new block maps are proved below.

Primary body: `refs/f1/1310.3878/paper.txt`, Rosso, Section 3, pp. 5–7:
convolution (6), Definition 3.2, Remarks 3.3–3.4 and Theorem 3.6. The geometry
supplies the basis formula and injectivity; a presentation citation alone is
not used as their proof. Hecke block traces and expectations are D1102 and
F1-HCK-TOWER. No positive assertion is made for 0<q<1.

## Theorem MMOD-1 (the marked-unmarked block algebra)

**ASSUME** m,n>=0 and the based families R_m,H_n,R_(m+n) of D1271.
**PROVE** rho_(m,n) is a unital injective star-homomorphism over the based
coefficient ring, and for every q>1 it preserves faithful normalized traces
and is an inclusion of finite C*-algebras.

<1>1. **PROVE** the antichain basis formula in D1271 has an admissible label.

<2>1. Put w=u block v. On the first m coordinates, the inequalities defining
`prec_w` are precisely those defining `prec_u`, because w^(-1) restricts
to u^(-1). Thus an antichain A for u is an antichain for w.

<2>2. If a is in the first m positions and i is below a in prec_w, then
`i<a<=m`. Therefore no last-block coordinate lies in its downset, and

    down_(u block v)(A)=down_u(A).

<2>3. Different triples (u,A,v) yield distinct labels (u block v,A), since
restriction of the block permutation recovers u,v and A is retained.
Consequently the based map is injective as a linear map at every parameter.
This does not yet assume multiplicativity. **QED**

<1>2. **PROVE** the arithmetic Hilbert register admits the relevant block
partition without choosing a complementary subspace.

<2>1. Fix a finite field k of order Q, L=k^(m+n), and a full flag F in L.
Its distinguished step U=F_m has dimension m. The lower part of F is a full
flag in U; the upper part is a full flag in L/U, with steps F_(m+j)/U.

<2>2. Conversely these two flags determine F uniquely: its upper steps are
the full inverse images of the quotient-flag steps. Thus the full flags
through U are canonically `Fl(U) times Fl(L/U)`.

<2>3. Partition flag-vector pairs (F,x) additionally by the vector coset
c=x+U in L/U. For fixed U,c, their Hilbert span identifies with

    C[Fl(U) times c] tensor C[Fl(L/U)].

The coset c is an affine U-torsor. Choosing one x_c in c identifies its first
factor with C[Fl(U) times U]. No complement of U in L is used.

<2>4. A different origin in c translates U; MIR-AFF's invariant-kernel
operators commute with such translations. Thus the algebra action on this
factor, though represented with that auxiliary choice in the proof, is
independent of it. Linear identifications of U with k^m and of L/U with k^n
likewise preserve the invariant orbit operators. **QED**

<1>3. **PROVE** independent local updates define an algebra homomorphism.

<2>1. On every summand of <1>2 let R_m(Q) act on the first affine flag-vector
factor via MIR-AFF and H_n(Q) act on the quotient-flag factor via
F1-HCK-FLAG. Their tensor product is a unital star representation.

<2>2. Take the direct sum over all U,c. By <1>2.<2>4 its operator kernels
are intrinsic: a marked update changes the lower flag and translates the
vector within U while fixing the quotient flag; an unmarked update changes
only the quotient flag and leaves both lower flag and vector unchanged.

<2>3. These operators commute with the full affine action on L, since that
action transports U,c and preserves the two invariant local update rules.
They therefore lie in the full R_(m+n)(Q) commutant from MIR-AFF.
The resulting map R_m(Q) tensor H_n(Q)->R_(m+n)(Q) is a unital star-map.
**QED**

<1>4. **PROVE** one marked and one unmarked basis update have exactly the
claimed composite orbital kernel, with coefficient one.

<2>1. Take initial and final pairs (F,x),(F',x'). A nonzero mixed update
requires `F_m=F'_m=U` and `x'-x in U`. If these conditions fail, both the
block construction and the claimed orbital kernel vanish.

<2>2. For a marked update first and an unmarked update second, the
intermediate flag H must have the lower flag of F' and the quotient flag of
F. Its intermediate vector must be x', because the second update leaves the
vector unchanged. By <1>2.<2>2 there is exactly one such H and one vector.

<2>3. This unique intermediate contributes one exactly when the lower
flag/vector relative orbital is (u,A) and the quotient flags have relative
position v. Those are precisely the conditions for the product kernel.

<2>4. In a basis adapted to U, the composite relative permutation is
u block v. Its vector difference lies in U and has the first-block maximal
support antichain A. Hence its orbit label is (u block v,A), in D1245's
standard-pair convention. This proves

    rho_(m,n),Q(T_(u,A) tensor T_v)=T_(u block v,A).

<2>5. In the reverse order the unique intermediate has the lower flag of F,
the quotient flag of F', and vector x. The same conditions result. This also
checks the independent updates commute by an actual kernel computation,
rather than inferring it from matching dimensions. **QED**

<1>5. **PROVE** the zero-rank cases agree with the stated units.

<2>1. If n=0, U=L and the quotient flag is a singleton. The construction is
the full marked affine register and rho_(m,0) is identity.

<2>2. If m=0, U=0, the marked factor is scalar, and the vector is unchanged.
The kernel is the zero-vector Hecke orbital, so rho_(0,n)=i_n as in D1247.
This includes m=n=0, where both maps are the scalar identity. **QED**

<1>6. **PROVE** the arithmetic algebra identity extends uniformly in q.

<2>1. For basis inputs a,b in R_m tensor H_n, expand
`rho(ab)-rho(a)rho(b)` in the composite orbit basis. Every coefficient is a
polynomial in q by Rosso Definition 3.2 and the ordinary Hecke multiplication
rule. If one uses the localized presentation, these are Laurent polynomials
and can first be multiplied by a common power of q.

<2>2. Every coefficient vanishes at all prime powers Q by <1>3–4, hence is
identically zero. This proves multiplicativity over C[q,q^(-1)] and at every
positive real parameter. The identity orbital maps to the identity orbital.

<2>3. Star also follows from the physical arithmetic maps and the same
coefficient argument. Directly, D1246 sends the composite label to
`(u^(-1) block v^(-1),u^(-1)(A))`, exactly the product of the two stars.

<2>4. The injectivity is the independent basis argument <1>1, and therefore
survives every specialization; it is not inferred from generic injectivity.
**QED**

<1>7. **PROVE** the generator convention agrees with Rosso's presentation.

<2>1. For m>=1, the marked boundary generator is T_(e,{1})=T_0, and
rho(T_0 tensor 1)=T_0 in the total rank. Marked T_i, 1<=i<m, map to T_i.
The j-th simple Hecke generator on the right maps to T_(m+j), 1<=j<n.

<2>2. The separator T_m is absent. The two generator sets commute by
Rosso's far-commutation relation (13): their distances are at least two,
including the T_0/T_2 case when m=1. The marked relations (8),(11),(12)
remain entirely within the first block; the right relations are Hecke ones.

<2>3. Thus Theorem 3.6 gives a second homomorphism construction with these
generator images. Since the geometric/based map has the same images on the
generators, it is that map. The basis proof, not this presentation check,
supplies its injectivity. **QED**

<1>8. **PROVE** the coefficient trace and the full Gram form factor.

<2>1. The coefficient trace of the image is one only when u=v=e and A is
empty, and zero otherwise. Therefore

    tau_R,m+n rho_(m,n)=tau_R,m tensor tau_H,n.

<2>2. MIR-VAL and <1>1 give the image orbital valency

    q^(ell(u)+ell(v)+|down_u(A)|-|A|)(q-1)^|A|
      =k_(u,A)(q) q^ell(v).

This is exactly the product of the marked and unmarked Gram diagonal.
Distinct image basis elements remain orthogonal by MIR-POS.

<2>3. For q>1 the marked Gram is strictly positive and the Hecke Gram is
strictly positive by F1-HCK-POS. The algebras on both sides are honest finite
C*-algebras. The injective unital star-map is positive at every matrix level
and preserves the normalized faithful traces as just computed.

<2>4. This proves MMOD-1 for all m,n>=0 and every real q>1, including all
finite-field characteristics. No division by two or arithmetic approximation
to one is used. **QED**

## Theorem MMOD-2 (traced mixed expectation and coherent vector retraction)

**ASSUME** D1272, MMOD-1, q>1 and the existing Hecke block expectations.
**PROVE** F_(m,n) is the unique traced UCP expectation to R_m tensor H_n;
the right-action inclusion and expectation towers cohere, and vector coarse
graining intertwines both structure maps.

<1>9. **PROVE** F_(m,n) is trace-orthogonal projection to the included algebra.

<2>1. By MMOD-1 the image basis is exactly the labels (w,A) for which w
preserves the first m positions and A is contained there. The image is a
unital star-subalgebra, not merely a subspace.

<2>2. MIR-POS makes distinct orbitals orthogonal. Thus deleting the other
coefficients is the L2 orthogonal projection onto that subalgebra.
Decoding its image by the injective rho gives precisely D1272's F.

<2>3. MMOD-1's trace product identity identifies the target trace with the
separated normalized product trace. In particular `F rho=id` and both
maps preserve normalized trace. **QED**

<1>10. **PROVE** this orthogonal projection is completely positive and unique.

<2>1. Write B for the included algebra, tau for the ambient faithful trace
and G=rho F. Orthogonality says `tau(b^*G(a))=tau(b^*a)` for all b in B.
Traciality then implies G is B-bimodular, by testing cad against b and
cyclically moving d; it fixes the unit and preserves star.

<2>2. If a>=0 but G(a) has a negative spectral projection r in B, the
identity with test r gives `tau(rG(a))=tau(ra)>=0`, whereas faithfulness
would make its left side negative. Thus G is positive.

<2>3. Entrywise G is the trace-orthogonal projection from M_l(A) onto M_l(B)
for the matrix trace tensor tau. Repeating <2>1–2 proves positivity at every
matrix level. This yields UCP, and the same holds for F under rho's inverse.

<2>4. Any trace-preserving conditional expectation onto B has the same
bimodule trace-pairing identity, hence equals G by nondegeneracy of the trace
on B. A UCP retraction fixing B is bimodular by the multiplicative-domain
argument: in a Stinespring form G(a)=V^*pi(a)V, equality on b and b^*b gives
`pi(b)V=Vb`. This also proves uniqueness among traced UCP retractions.
The local primary anchors are Umegaki 1954 equation (1) and Stinespring 1955
Theorem 1; existence and matrix positivity were independently derived above.
**QED**

<1>11. **PROVE** the right-action inclusion law is exactly associative.

<2>1. On a triple basis tensor `T_(u,A) tensor T_v tensor T_z`, both maps

    rho_(m+n,k)(rho_(m,n) tensor id),
    rho_(m,n+k)(id tensor iota_(n,k))

send it to `T_(u block v block z,A)`.

<2>2. Equality on the basis proves equality over the common coefficient
ring and in every fibre. The right unit is rho_(m,0)=id from <1>5.
This is a right action of the Hecke multiplicative sequence, not an
associativity claim for two marked factors. **QED**

<1>12. **PROVE** the mixed expectation tower has the same right associativity.

<2>1. From R_(m+n+k) to R_m tensor H_n tensor H_k compare

    (F_(m,n) tensor id) F_(m+n,k),
    (id tensor E^H_(n,k)) F_(m,n+k).

On a composite orbit label, each keeps it exactly when its permutation
preserves all three contiguous blocks and its antichain lies in the first m
positions. Each then decodes it as the same triple tensor of orbit bases.

<2>2. Therefore the two maps are equal. Equivalently both are the unique
traced expectations onto the common triple subalgebra of <1>11. The scalar
unit cases agree by F_(m,0)=id and F_(0,n)=E_n. **QED**

<1>13. **PROVE** vector expectation is compatible with the marked action.

<2>1. For a product basis element, E_(m+n) kills rho's image iff A is
nonempty. If A is empty its value is T_(u block v). Hence

    E_(m+n) rho_(m,n)=iota_(m,n)(E_m tensor id).

<2>2. On a composite orbit T_(w,A), both maps in

    (E_m tensor id) F_(m,n)=E^H_(m,n) E_(m+n)

vanish for A nonempty. For A empty, both keep exactly the block permutations
and decode them as T_u tensor T_v. Thus this second square also commutes.

<2>3. These equations hold as based polynomial linear maps and for every
q>1. E_r is generally not multiplicative there, so this is compatibility of
traced CP comparisons, not an amplitude functor C_R(q)->C_H(q). **QED**

<1>14. **PROVE** the mixed comparison is generally a proper retraction.

<2>1. For m=n=1, R_1 tensor H_1 has basis 1,T_0. R_2 has seven orbit
basis elements: for w=e the chain has three antichains, and for w=s the
two-point antichain poset has four. Thus the dimensions are 2 and 7.

<2>2. The nonzero Hecke generator T_1 in R_2 has a permutation crossing the
separator, so F_(1,1)(T_1)=0. Consequently rho F is not identity, while
F rho=id holds on the included algebra.

<2>3. For m=1,n=2 the image basis is `1,T_0,T_2,T_0T_2`; the two
updates commute and this image has dimension four by MMOD-1. These are
concrete small-rank falsifiers, not proofs of the uniform theorem.
Steps <1>9–<1>14 prove MMOD-2. **QED**
