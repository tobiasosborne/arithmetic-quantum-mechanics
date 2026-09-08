# Typed arithmetic amplitudes and code compatibility

Claims: FRP-CAT and the pure part of FRP-DESCENT.
Status: PROVED within the stated hypotheses after capped review.
Native model convention: inherited Codex runtime, no model override, no nested
CLI; exact model identifier is not exposed to this lane.
Definition source: ../../../definitions.md, D1321--D1327; shared D1301--D1308
are shared definitions and are not redefined here.

Admission and repair record: `../../verdicts/frobenius-hierarchy-adjudication.md`.

## Statement and scope

FRP-CAT is the category/interpretation statement in ../../../claims/CLAIMS.md.
It is uniform in p. It is a presented arithmetic circuit category, not a
classification of symplectic quantizations, stabilizer maps, or Clifford gates.
Only its listed relations are imposed. The proof verifies their nontrivial
arithmetic content under the independently specified Hilbert interpretation.
The argument does not infer injectivity of that interpretation.

## Structured proof

<1>1. ASSUME the finite named arithmetic datum of D1321.
       PROVE the raw objects and amplitude terms form sets.
  <2>1. The alphabet of quantum atoms is finite: it has one atom for each
         field and one for each arrow of the finite category I.
         JUSTIFICATION: D1321.
  <2>2. Finite words in this alphabet are a countable set, including 1.
         JUSTIFICATION: encode a length-n word by an n-tuple in a finite set;
         take the union over the nonnegative integers, as stipulated in D1321.
  <2>3. Each generator set is finite except the multiplication labels d>=1.
         These labels are countable. R_p is countable because its elements
         are rational expressions in two fixed algebraic complex numbers.
         JUSTIFICATION: D1321, D1322 and finite rational expression encoding.
  <2>4. Raw typed circuits and their finite linear combinations are finite
         parse trees over a countable alphabet, and therefore form a set.
         JUSTIFICATION: D1322; encode each finite tree by a finite string.
  <2>5. QED by <2>1--<2>4.

<1>2. ASSUME the raw syntax in <1>1.
       PROVE D1322's equality and category operations exist.
  <2>1. The intersection of all typed congruences containing the specified
         equations is a typed congruence; the indiscrete relation on each
         Hom is one such congruence, so this is a nonempty intersection.
         JUSTIFICATION: closure under each operation is preserved by
         intersection, directly from D1322's definition of congruence.
  <2>2. Quotient each Hom set by this intersection. Operations descend
         because closure under precisely those operations was required.
         JUSTIFICATION: D1322 and <2>1.
  <2>3. Category identities, associativity, bilinearity, dagger involution,
         interchange and symmetric coherence hold in the quotient because
         the corresponding equations occur among the defining axioms.
         JUSTIFICATION: D1322.
  <2>4. Tensor is concatenation on objects and the descended circuit tensor
         on arrows. The empty word is its strict object unit.
         JUSTIFICATION: D1321, D1322 and <2>2.
  <2>5. QED: this constructs a small R_p-linear dagger symmetric monoidal
         category, prior to any Hilbert interpretation.

<1>3. ASSUME the independent generator assignments of D1324.
       PROVE every assignment has the advertised source and target.
  <2>1. W,F,U are operators on ell^2(E); M on ell^2(E)^(d+1);
         J_i,V_i go from ell^2(K) to ell^2(E).
         JUSTIFICATION: D1301--D1304,D1306,D1308.
  <2>2. The code basis is indexed by K because i is injective. Thus t_i
         is a unitary from ell^2(K) onto the actual subspace C_i, and c_i
         is its inclusion into ell^2(E).
         JUSTIFICATION: D1303,D1305,D1324 and basis-vector inner products.
  <2>3. e_E sends 1 to a norm-one basis vector; the Hilbert tensor and
         swaps have the types prescribed by word concatenation.
         JUSTIFICATION: D1324.
  <2>4. QED by <2>1--<2>3; no dimension-only identification replaces a label.

<1>4. ASSUME the trace-normalized reference Weyl operators.
       PROVE D1323(1) is respected by H.
  <2>1. Applied to |x>, W(a,b) has phase psi_E(-b(x+a)) and output |x+a>.
         JUSTIFICATION: D1301, matching the trunk D8 sign convention.
  <2>2. The phase for W(a,b)W(a',b') on |x> divided by that for
         W(a+a',b+b') is psi_E(ab').
         JUSTIFICATION: expand the two expressions in <2>1 and cancel;
         the exponent difference is ab'. This is named computation W-PROD.
  <2>3. Each W is a basis permutation times modulus-one diagonal entries,
         and W(0,0)=I. Thus it is unitary and obeys the required product.
         JUSTIFICATION: D1301 and <2>1--<2>2.
  <2>4. QED. W-PROD does not use division by two.

<1>5. ASSUME D1301's nontrivial trace character.
       PROVE H respects the Fourier equations in D1323(2).
  <2>1. A nontrivial character chi of a finite additive group has sum zero:
         translating its sum by y with chi(y)!=1 multiplies the sum by
         chi(y), whereas permutation of the summands leaves it unchanged.
         JUSTIFICATION: character law in D1301; named computation CHAR-SUM.
  <2>2. The inner product of Fourier columns x,x' is
         |E|^-1 sum_y psi_E((x-x')y), equal to delta_(x,x').
         JUSTIFICATION: D1306, FRB-TRACE and CHAR-SUM.
  <2>3. The coefficient of |z> in F_E^2|x> is
         |E|^-1 sum_y psi_E(-y(x+z))=delta_(z,-x).
         JUSTIFICATION: D1306, FRB-TRACE and CHAR-SUM.
  <2>4. Therefore F_E is unitary and F_E^4=I.
         JUSTIFICATION: <2>2--<2>3, composing the negation permutation twice.
  <2>5. QED, including p=2 where negation itself is the identity.

<1>6. ASSUME finite E has degree r over F_p.
       PROVE all remaining equations in D1323(2)--(3) are respected.
  <2>1. Frobenius permutes E and its r-th power is the identity; its
         Weyl covariance is the algebra lane's FRB-FROB.
         JUSTIFICATION: D1302 and FRB-FROB.
  <2>2. In F_E U_E and U_E F_E, rename the summation label by its
         Frobenius image and use psi_E(z^p)=psi_E(z). The negative
         Fourier coefficient is unchanged.
         JUSTIFICATION: D1302,D1306 and FRB-FROB; named computation F-FROB.
  <2>3. M translates its last register by a product and fixes its inputs;
         its inverse subtracts that product. Repeating p times adds zero.
         JUSTIFICATION: D1308, characteristic p, named computation M-ORDER.
  <2>4. Raising the translated output to its p-th power raises every
         input and their product to its p-th power, giving covariance.
         JUSTIFICATION: D1308 and FRB-NATURAL.
  <2>5. QED by <2>1--<2>4; no hierarchy closure statement was used.

<1>7. ASSUME composable named embeddings i:K->L and j:L->E.
       PROVE D1323(4)--(5) are respected.
  <2>1. J_i is an isometry because its distinct input basis labels have
         distinct output labels. V_i is an isometry because its fibres
         are disjoint and each column has norm one.
         JUSTIFICATION: D1303,D1304 and FRB-TRANSFER.
  <2>2. Composition of inclusions is inclusion of the composite map.
         Trace transitivity, equal fibre sizes and their multiplicativity
         give V_j V_i=V_(ji), including all normalization factors.
         JUSTIFICATION: FRB-TRANSFER; no new choice of trace section is made.
  <2>3. Both transfers commute with the named Frobenius, and the negative
         Fourier relation is F_E J_i=V_i F_K.
         JUSTIFICATION: FRB-TRANSFER, with the characters fixed by D1301.
  <2>4. Identity embeddings have identity trace, single-point fibres, and
         both transfers equal I.
         JUSTIFICATION: D1303,D1304.
  <2>5. QED. The restriction psi_E|K=psi_K^[E:K] is not substituted for
         the trace identity psi_E=psi_K composed with T_i.

<1>8. ASSUME i:K->E, a in K and b in E.
       PROVE the mixed Weyl relation in D1323(6).
  <2>1. W_E(i(a),b)J_i|x> has output |i(x+a)> and phase
         psi_E(-b i(x+a)).
         JUSTIFICATION: D1301,D1304.
  <2>2. That phase is psi_K(-T_i(b)(x+a)).
         JUSTIFICATION: trace adjunction in FRB-TRACE and D1303.
  <2>3. This is exactly J_i W_K(a,T_i(b))|x>.
         JUSTIFICATION: D1301,D1304 and <2>2.
  <2>4. QED on a basis. The logical momentum uses T_i, not b=i(b_0).

<1>9. ASSUME i:K->E and d>=1.
       PROVE the multiplication relation in D1323(6).
  <2>1. On a tuple in K^(d+1), inclusion followed by physical M adds
         the product of the included input elements to the included target.
         JUSTIFICATION: D1304,D1308.
  <2>2. A field embedding preserves this sum and product, so the result
         equals inclusion after M_K on that tuple.
         JUSTIFICATION: D1303 and FRB-NATURAL.
  <2>3. QED on the computational basis. Separate input-register labels
         remain separate; this is multiplication, not addition data.

<1>10. ASSUME the code and preparation assignments of D1324.
        PROVE D1323(7)--(8) are respected.
  <2>1. t_i is unitary and c_i t_i=J_i by the specified code basis.
         JUSTIFICATION: <1>3 and D1324.
  <2>2. W_E(a,0)e_E is the basis ket |a>. These kets have inner products
         delta_(a,a') and their rank-one projectors sum to I.
         JUSTIFICATION: D1301,D1324 and entrywise identity-matrix computation.
  <2>3. QED. These are the only preparation equations added here; no
         relation identifies every other generator with its matrix expansion.

<1>11. ASSUME <1>3--<1>10.
        PROVE the Hilbert interpretation descends to the quotient.
  <2>1. Evaluation of raw circuits preserves composition, linearity,
         scalar conjugation, dagger and tensor by D1324's recursive rule.
  <2>2. It respects every generating arithmetic equation by <1>4--<1>10;
         identities and symmetry axioms hold on elementary tensors because
         both sides perform the same rearrangement and linear operations.
         JUSTIFICATION: D1324 and elementary-tensor evaluation.
  <2>3. Equality of evaluations is therefore one of the congruences in
         <1>2, so the least defining congruence is contained in it.
         JUSTIFICATION: the intersection construction in <1>2.
  <2>4. QED: H is a well-defined R_p-linear dagger functor.

<1>12. ASSUME <1>11.
        PROVE the remaining assertions of FRP-CAT.
  <2>1. The tensor comparison sends a pure tensor in the interpretation of
         two words to the same ordered tensor in their concatenation.
         It is unitary, natural, and coherent, since every composite sends
         each elementary tensor to the identical ordered list of factors.
         JUSTIFICATION: D1321,D1324 and <1>11.
  <2>2. Source scalars are consistent: 1 cannot equal 0, since their
         images on H(1)=C differ. Source words retain their named atoms.
         JUSTIFICATION: D1321,D1322 and <1>11.
  <2>3. Nothing in this construction equates arrow equality with H-equality
         or makes all m-generators of one level closed under composition.
         JUSTIFICATION: the exact equality definition D1322--D1323.
  <2>4. QED: FRP-CAT, without faithfulness or full Clifford scope.

<1>13. ASSUME a code atom C_i and its source arrows.
        PROVE c_i is an isometry and c_i c_i^dagger=j_i j_i^dagger.
  <2>1. c_i=j_i t_i^dagger, since c_i t_i=j_i and t_i t_i^dagger=1.
         JUSTIFICATION: D1323(7).
  <2>2. Thus c_i^dagger c_i=t_i j_i^dagger j_i t_i^dagger=1,
         and c_i c_i^dagger=j_i t_i^dagger t_i j_i^dagger=j_i j_i^dagger.
         JUSTIFICATION: D1323(4),(7).
  <2>3. QED, with no additional projection-object completion.

<1>14. ASSUME a is an endomorphism of Q_K^n and a^[i] is D1327's lift.
        PROVE c_i^tensor n a^[i]=j_i^tensor n a (t_i^dagger)^tensor n.
  <2>1. Substitute the code-lift circuit and use c_i t_i=j_i in each slot.
         JUSTIFICATION: D1323(7),D1327 and tensor interchange.
  <2>2. QED; code identification is a named choice built into its atom.

<1>15. ASSUME a=m_(K,d), n=d+1, or a=u_K, n=1.
        PROVE the physical multiplication or Frobenius intertwines the code lift.
  <2>1. Move the physical gate past j_i^tensor n using D1323(6) for m
         or D1323(5) for u, then apply <1>14.
  <2>2. This gives c_i^tensor n a^[i]=m_(E,d)c_i^tensor n, or
         c_i u_K^[i]=u_E c_i, respectively.
         JUSTIFICATION: <1>13--<1>14 and D1323.
  <2>3. QED: the code carries the stated arithmetic logical operations.

<1>16. ASSUME the mixed Weyl relation and any b with T_i(b)=b_0.
        PROVE W's code lift has the physical representative w_E(i(a_0),b).
  <2>1. Substitute a=w_K(a_0,b_0) into <1>14 and use <1>8.
         JUSTIFICATION: D1323(6),D1327 and trace surjectivity FRB-TRACE.
  <2>2. Changing b by an element of ker(T_i) leaves the action on the
         encoded subspace unchanged, because its right-hand source circuit
         w_K(a_0,b_0) is unchanged.
         JUSTIFICATION: D1323(6), not a choice of included momentum label.
  <2>3. QED: this matches D1305's logical symplectic quotient.

<1>17. ASSUME F_p belongs to the field datum and B is a named F_p-basis of E.
        PROVE D1327's coordinate circuit is a source unitary with the stated
        interpreted Weyl factorization.
  <2>1. Expand a_B^dagger a_B. Tensor basis orthonormality removes all
         off-diagonal pairs x!=y; completeness leaves sum_x b_x b_x^dagger=1.
         Expand a_B a_B^dagger similarly and use the bijection E~F_p^r.
         JUSTIFICATION: D1323(8),D1327 and tensor distributivity.
  <2>2. H(a_B)|x> is the coordinate tuple |x_1,...,x_r> by D1324.
         Positions use B and momenta its trace-dual basis; the phase pairing
         then splits as sum_l b_l(x_l+a_l), so W factors into prime-field Weyls.
         JUSTIFICATION: D1301, FRB-TRACE and D1324.
  <2>3. QED. This is a named, basis-dependent source isomorphism; the Weyl
         assertion here concerns H(a_B), not an additional source equation.

## Evidence boundary

All numerical checks are owned by the checker lane: A1--A4 and A7.
The nontrivial field identities in steps 6--9 depend on the algebra proofs;
finite samples cannot establish their all-field statements.
The registered Lagrangian/stabilizer sources provide background only and
are not invoked to supply this category or its normalization.
