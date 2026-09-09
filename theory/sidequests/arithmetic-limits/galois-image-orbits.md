# Normal-closure symmetry and primitive Frobenius atoms

Claim: GAL-IMAGE. Status: PROVED within the stated hypotheses after capped review.
Author: native inherited Codex runtime; no override, nested CLI or subagent.
Definitions: D1401--D1405 in ../../../definitions.md.
Input: GAL-FUNCTOR, proved in the companion embedding-functor.md shard.

Admission: ../../verdicts/galois-embedding-adjudication.md.

## Source register

S1: Milne, Fields and Galois Theory, version 5.10, September 2022,
`refs/arithmetic-limits/milne-FT/FT.pdf` and `FT.txt`.
Theorem 6.10: embedding and isomorphism of separable closures.
Proposition 8.6 and Corollary 8.10: finite separable factors and composita.
Remark 3.18, printed p. 40: normal core and compositum normal closure.
Propositions 4.19--4.20, printed p. 53, and Corollary 4.21/Proposition
4.23, pp. 53--54: primitive elements, finite-field Frobenius, and subfields.
S2: Stacks, `refs/arithmetic-limits/stacks-04JI/source.html`, Lemma 58.2.2
(03QR): embedding G-sets and transitive finite separable field factors.
S3: Stacks, `refs/arithmetic-limits/stacks-0BMI/source.html`, Lemmas
9.22.1--9.22.3 and Theorem 9.22.4: topology, restriction quotients, finite
Galois inverse limit and the closed-subgroup/field correspondence.
Primitive orbit matrix blocks below use D1331--D1332's definitions only;
their positive parameter continuation is not an input to this proof.

## 1. The normal core is exactly the detected Galois group

ASSUME every field K with named separable closure Omega, and any finite
separable field extension A/K. Choose tau_0 in X_A as in D1404.
PROVE the normal-closure image statement of GAL-IMAGE.

<1>1. ASSUME tau in X_A.
       PROVE tau=g tau_0 for some g in G_K.
  <2>1. Both tau_0(A) and tau(A) are finite separable subfields of Omega.
         The field isomorphism tau tau_0^-1 between them extends to an
         isomorphism of their separable closures, which may both be taken
         to be Omega. With the K-structure retained, this is g in G_K.
         BY S1, 6.10 applied after transporting the base-field structure;
         equivalently, S2's transitivity statement for field factors.
  <2>2. Hence the map G_K/H_(A,tau_0)->X_A, gH->g tau_0, is onto.
         It is well-defined and injective because g tau_0=h tau_0 exactly
         when h^-1g fixes tau_0. It intertwines left multiplication.
         BY D1404 and <2>1. QED the equivariant coset description.

<1>2. ASSUME h in G_K and use the preceding coset description.
       PROVE ker(U_A^emb)=C_A.
  <2>1. A permutation matrix is the identity exactly when it fixes each
         basis label. Here h fixes every coset gH exactly when
         g^-1 h g is in H for every g.
         BY D1401, <1>1 and multiplying the coset identity hgH=gH.
  <2>2. This condition is h in intersection_g gHg^-1=C_A. Replacing
         tau_0 by another embedding conjugates H and leaves the intersection
         unchanged. Thus C_A is independent of tau_0.
         BY D1404 and reindexing the intersection by group multiplication.
  <2>3. The intersection is normal; it is open since it is the kernel
         of a continuous finite permutation action. Its index is finite,
         at most n_A factorial, without any abelianity condition.
         BY GAL-FUNCTOR and <2>1--<2>2. QED the kernel assertion.

<1>3. ASSUME N_A as in D1404.
       PROVE it is the finite Galois normal closure and its group is the image.
  <2>1. There are n_A embeddings. The compositum of their finite separable
         images is finite separable: iterated multiplication maps the tensor
         product of these finite etale fields onto their generated subalgebra.
         A finite-dimensional domain is a field, since multiplication by a
         nonzero element is injective and therefore surjective.
         BY S1, 8.6 and 8.10, and this finite-dimensional computation.
  <2>2. An element of G_K fixes N_A pointwise exactly when it fixes every
         tau(A) pointwise, equivalently when it fixes each embedding tau.
         Therefore Gal(Omega/N_A)=C_A.
         BY D1404, the meaning of compositum, and <1>2.
  <2>3. The Galois correspondence now implies Omega^(C_A)=N_A and
         that N_A/K is Galois, since C_A is normal and closed.
         It contains tau_0(A). Every normal subextension containing
         tau_0(A) contains all its conjugates, hence contains N_A.
         BY S3, Theorem 9.22.4 and <1>1--<1>2. This also agrees with
         the finite normal-core formula of S1, Remark 3.18.
  <2>4. Restriction G_K->Gal(N_A/K) is continuous and surjective with
         kernel C_A by S3, Lemma 9.22.2. The rule
           U_A^emb(g) -> g restricted to N_A
         is consequently a well-defined canonical group isomorphism
         Im(U_A^emb) -> Gal(N_A/K).
         BY <1>2, <2>2--<2>3 and equality of the two kernels.
  <2>5. QED. The image need not equal Aut_K(A), and its order need not
         equal [A:K]. A nonnormal separable extension is fully allowed.

<1>4. ASSUME a tower of finite separable fields f:A->B over K.
       PROVE N_A subset N_B and compatibility of finite image quotients.
  <2>1. Each sigma in X_A extends to tau in X_B by GAL-FUNCTOR's
         surjectivity of R_f. Then sigma(A)=tau(f(A)) subset tau(B).
         Taking composita yields N_A subset N_B and C_B subset C_A.
         BY D1402,D1404 and the fibre-surjection assertion.
  <2>2. The map Im(U_B^emb)->Im(U_A^emb), U_B^emb(g)->U_A^emb(g),
         is well-defined and onto by the inclusion of kernels. Under
         <1>3 it is restriction Gal(N_B/K)->Gal(N_A/K).
         BY <2>1 and the explicit group isomorphisms of <1>3.
  <2>3. Every longer tower composes these restriction maps exactly.
         The Hilbert isometries already intertwine the same g at each stage.
         BY restriction of functions and GAL-FUNCTOR. QED tower compatibility.

## 2. All finite levels and separability scope

<1>5. ASSUME the directed set of finite Galois subfields E/K of Omega.
       PROVE all these levels recover the profinite group and its action.
  <2>1. Every such E is an allowed object, every inclusion E subset F
         is an allowed arrow, and its normal closure is E itself. Hence
         <1>3 identifies Im(U_E^emb) with Gal(E/K).
         BY D1401, GAL-FUNCTOR and <1>3.
  <2>2. The family is directed by composita; its union is Omega. Its
         transition maps are precisely the surjective restrictions from
         <1>4. Thus the canonical homomorphism is a topological isomorphism
           G_K -> inverse-limit_(E/K finite Galois) Im(U_E^emb).
         BY S3, Lemma 9.22.3 and <2>1.
  <2>3. In particular a g acting trivially on all finite levels fixes
         every element of Omega, hence is the identity. The quotient actions
         also determine the Krull topology, not only the abstract group.
         BY <2>2 and the union assertion from S3.
  <2>4. QED recovery from the specified finite actions and restriction
         diagrams. No reconstruction from unmarked abstract matrix algebras,
         no infinite-dimensional register, and no Haar/Fourier datum follows
         from this statement alone.

<1>6. ASSUME a finite field extension L/K which is not separable.
       PROVE it is outside this nonzero embedding-register construction.
  <2>1. If a K-embedding L->Omega existed, every element of its image
         would be separable over K since Omega/K is separable. Minimal
         polynomials are preserved by a K-embedding, forcing every element
         of L to be separable over K, a contradiction.
         BY S1, Definition 6.9 and the definition of a K-embedding.
  <2>2. Therefore Hom_K(L,K^sep) is empty, so extending the present
         formula would yield the zero Hilbert space, excluded by D1401.
         Using an algebraic closure instead can retain embeddings but does
         not detect purely inseparable multiplicity: a purely inseparable
         element has at most one conjugate since X^(p^m)-a has at most one
         root in characteristic p, by (x-y)^(p^m)=x^(p^m)-y^(p^m).
         BY <2>1 and this polynomial identity. The count into an algebraic
         closure is the separable degree by its embedding-count definition.
  <2>3. QED explicit inseparable scope. The theorem applies uniformly
         to separable extensions over imperfect as well as perfect bases.

## 3. The finite-field comparison is a primitive orbit comparison

ASSUME K=F_p, A/K is a finite degree-d field extension, and D1405's choices.
PROVE the orbit comparison and its compatibility with the stated Galois data.

<1>7. ASSUME the arithmetic Frobenius Frob_p on Omega.
       PROVE L_(tau_0)^* U_A^emb(Frob_p) L_(tau_0)=S_d.
  <2>1. Finite fields are perfect and A/K is cyclic Galois, generated
         by x->x^p, of order d. Omega is a union of the finite subfields,
         and Frobenius is invertible on each of them, hence on Omega.
         BY S1, Propositions 4.20 and 4.23, and finite Galois degrees.
  <2>2. Every embedding is Frob_p^j tau_0 for exactly one j modulo d.
         Thus L_(tau_0) bijects orthonormal bases, and postcomposing
         by Frob_p increases j by one including at the wraparound.
         BY <1>1, <2>1 and D1405. QED the cyclic-coordinate formula.

<1>8. ASSUME A=F_p(a), b=tau_0(a), d divides r, and E=F_(p^r) in Omega.
       PROVE T_a is a Frobenius-equivariant unitary onto the orbit subspace.
  <2>1. Primitive a exists by S1, Proposition 4.19. Its d embedding
         images b^(p^j) are distinct: equal images of a would give equal
         homomorphisms on F_p(a). All lie in E by S1, Proposition 4.23.
         BY D1405 and the embedding list of <1>7.
  <2>2. Evaluation at a is therefore a bijection X_A->O_b. Its
         basis linearization is T_a, which is unitary onto ell^2(O_b)
         and satisfies T_a U_A^emb(Frob_p)|tau>=|tau(a)^p>.
         BY <2>1 and D1401,D1405.
  <2>3. T_a L_(tau_0)|j>=|b^(p^j)>, exactly the marked orbit coordinates
         of D1331 with origin b. Conjugation identifies B_A^emb=M_d(C)
         with the full matrix block on this orbit and carries I/d to its
         normalized block density. For d>1 it is a nonfixed-label block
         of D1332; d=1 is the fixed-label atom, excluded from that corner.
         BY D1331--D1332, D1401 and <2>2.
  <2>4. QED primitive-orbit comparison. D1331 may repeat this block on
         every orbit of the same length. The present construction neither
         supplies the number of copies nor prescribes D1332's mixture weights.

<1>9. ASSUME a different embedding tau_1=Frob_p^h tau_0.
       PROVE the coordinate dependence is explicit and Galois compatible.
  <2>1. L_(tau_1)|j>=L_(tau_0)|j+h>, so changing origin is a cyclic
         shift commuting with S_d. The orbit set O_b is unchanged.
         BY D1405 and the formula in <1>7.
  <2>2. Choosing a different primitive element a' gives another evaluation
         comparison T_(a'). The comparison between its orbit space and
         the first is T_(a') T_a^*, intertwining their Frobenius shifts.
         Different primitive orbits need not be literally the same subsets.
         BY <1>8 and composing the two explicit unitaries.
  <2>3. A named change of separable closure transports b and every one
         of its powers. It therefore transports T_a and L_(tau_0) by
         the W_eta comparisons of GAL-FUNCTOR.
         BY D1402,D1405 and multiplicativity of eta. QED canonicity scope.

<1>10. ASSUME standard finite subfields A=F_(p^d) subset B=F_(p^e)
        of Omega with d dividing e, using their inclusion origins.
        PROVE the embedding transfer is the normalized cyclic quotient pullback.
  <2>1. Restriction sends the j-th embedding of B to j modulo d in X_A.
         Hence s_f|j>=(e/d)^(-1/2) sum_(0<=k<e/d)|j+kd>.
         BY D1402 and <1>7; the fibre rank is [B:A]=e/d.
  <2>2. Every other named F_p-embedding f:A->B has f=incl composed
         Frob_p^h|_A for some h modulo d. In the same coordinates its
         restriction sends j to j+h modulo d, so its pullback sums over
         j congruent to the source label minus h. The general functor's
         tower equations already include these shifted maps.
         BY S1, Proposition 4.20, D1402 and GAL-FUNCTOR.
  <2>3. Its input and output dimensions are d and e. The field-label
         register dimensions of D1301 would be p^d and p^e, and D1304's
         J_f sends a field element to its named image. The D1333 divisor
         block map instead inserts unchanged common divisor blocks.
         These are different defined maps on different defined systems.
         BY D1301,D1304,D1333 and the formula in <2>1.
  <2>4. QED transfer comparison. Already F2 subset F4 gives embedding
         dimensions 1->2, while its physical register dimensions are 2->4.

<1>11. ASSUME two finite-field atoms of degrees d,e and their independent tensor.
        PROVE the Galois-set tensor comparison retains quantum orbit multiplicity.
  <2>1. Their basis labels are pairs (i,j) modulo (d,e), and simultaneous
         Frobenius adds (1,1). Each orbit has length l=lcm(d,e), since its
         return time is divisible by both d and e; there are de/l=gcd(d,e)
         orbits. This is the same cycle-set decomposition used by D1333.
         BY <1>7, GAL-FUNCTOR and the elementary return-time divisibility.
  <2>2. The Hilbert tensor still has every pair as basis and full algebra
         M_(de). A partition into g cycles decomposes the Hilbert space,
         but its cross-cycle matrix units remain in that full algebra.
         BY D1401 and GAL-FUNCTOR's Cartesian comparison.
  <2>3. For d=e=2 the two orbits contain 00 and 01 respectively. The
         vector v=(|00>+|01>)/sqrt(2) has return probability one on the
         effect |v><v|. Dephasing between these orbits changes the probability
         to 1/2 by deleting its two off-diagonal matrix entries.
         BY the four-entry expansion of |v><v| and ordinary matrix trace.
  <2>4. QED the quantum interpretation and GAL-IMAGE. No identification
         of Galois-set orbits with classical quantum sectors is imposed.
