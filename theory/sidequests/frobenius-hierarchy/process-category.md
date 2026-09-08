# Positive processes, independent tensor and retained descent

Claims: FRP-CP and the operational part of FRP-DESCENT.
Status: PROVED within the stated hypotheses after capped review.
Native model: inherited Codex runtime, no override or nested CLI; the runtime
does not expose an exact model identifier to this lane.
All D1321--D1327 references point to ../../../definitions.md.
The interpretation H and the source equations are supplied by FRP-CAT.

Admission and repair record: `../../verdicts/frobenius-hierarchy-adjudication.md`.

## Claim scope

The source consists of certified finite lists of arithmetic amplitudes.
The target uses ordinary trace-one density matrices in finite block algebras.
The claim is not that every CP map, state, effect or Kraus equivalence has
an arithmetic source representative. No reset is used to obtain tensor.
Normalized preparations and actual discards are part of the stated source.

## Structured proof

<1>0. ASSUME the fixed countable naming universe of D1325 and FRP-CAT.
       PROVE the process objects and arrows form sets.
  <2>1. Finite subsets of the name universe and finite lists of quantum words
         form sets, so their finite tagged families form a set.
         JUSTIFICATION: D1325 and the word encoding in FRP-CAT.
  <2>2. Each amplitude Hom is a set. Finite arrays of its arrows, with finite
         hidden names and finite certificate derivations, therefore form a set.
         Passing to the stipulated hidden-index bijection quotient preserves
         sethood. Tuple closure keeps all composition/tensor index sets legal.
         JUSTIFICATION: D1322, D1325 and finite parse-tree encoding.
  <2>3. QED: the process category is small with the stated naming convention.

<1>1. ASSUME k:X->Y and l:Y->Z satisfy D1325's certificates.
       PROVE the proposed composition has a source certificate.
  <2>1. For each input a write S_a=sum_(b,j) k_(b,a,j)^dagger k_(b,a,j).
         For each intermediate b write T_b=sum_(c,t) l_(c,b,t)^dagger l_(c,b,t).
         JUSTIFICATION: finite source sums in D1325.
  <2>2. Expand the composite deficit using bilinearity:
           1-sum_(b,j,c,t)(l_(c,b,t)k_(b,a,j))^dagger(l_(c,b,t)k_(b,a,j))
           =(1-S_a)+sum_(b,j) k_(b,a,j)^dagger(1-T_b)k_(b,a,j).
         JUSTIFICATION: D1322's dagger/composition axioms and distributivity.
  <2>3. Substitute certificate sums h^dagger h and g^dagger g for the
         two deficits. The right side becomes a sum of squares with
         amplitudes h_(a,v) and g_(b,w)k_(b,a,j), all with source X_a.
         JUSTIFICATION: D1325 and <2>2.
  <2>4. These amplitudes have legal quantum-word codomains because each g
         starts at the intermediate word Y_b. The list is finite.
         JUSTIFICATION: source typing in D1325.
  <2>5. QED: composition stays in the certified source.

<1>2. ASSUME the finite Kraus-index equality of D1325.
       PROVE composition is well-defined, associative and unital.
  <2>1. A bijection of either input hidden set induces the corresponding
         bijection of each composite triple (b,j,t), preserving amplitudes.
         Equal source amplitudes remain equal after composition.
         JUSTIFICATION: D1325 and D1322's congruence property.
  <2>2. Three successive arrows give the same hidden path data and the
         same amplitude m l k under rebracketing of their finite indices.
         JUSTIFICATION: D1325 and source associativity.
  <2>3. Identity composition adds a singleton hidden factor on each
         diagonal block; removing that singleton is an allowed bijection.
         Its amplitude is the unchanged arrow by source identity laws.
         JUSTIFICATION: D1325.
  <2>4. QED. Intermediate external tags become hidden path indices unless
         an output tag was explicitly chosen to retain their value.

<1>3. ASSUME k:X->Y and l:X'->Y' satisfy source certificates.
       PROVE their independent tensor has a source certificate.
  <2>1. Fix input pair (a,a'). Write S and T for the respective sums k†k
         and l†l. The tensor list has squared-amplitude sum S tensor T.
         JUSTIFICATION: D1322 tensor interchange and D1325 finite sums.
  <2>2. Its deficit has the source decomposition
           1 tensor 1-S tensor T
             =(1-S) tensor 1 + S tensor (1-T).
         JUSTIFICATION: expand and cancel S tensor 1, in D1322.
  <2>3. If h and g certify the factors, the right side is the sum of
         squares of h tensor 1_X'a' and k_(b,a,j) tensor g.
         Their codomains are quantum words and the lists are finite.
         JUSTIFICATION: D1325 and tensor-dagger interchange.
  <2>4. QED, with no assumption that the input density is a product.

<1>4. ASSUME D1325's canonical finite-tag bijections and word swaps.
       PROVE the source is a symmetric monoidal category.
  <2>1. Tensor respects hidden-index bijections by taking their Cartesian
         products, and respects source equality by tensor congruence.
         JUSTIFICATION: D1322,D1325.
  <2>2. The two orders of composing independent tensors produce bijective
         path labels ((j,t),(j',t')) and ((j,j'),(t,t')). Their amplitudes
         agree by source interchange.
         JUSTIFICATION: D1322,D1325; named index computation PATH-INTERCHANGE.
  <2>3. The tensor unit is the singleton tagged empty word; associator,
         unitor and swap paths perform the same coordinate rebracketing
         and permutation on every external tag and quantum factor.
         Thus their coherence diagrams commute under D1325 equality.
         JUSTIFICATION: D1321,D1322,D1325, evaluated on finite tuples.
  <2>4. QED. Smallness follows from finite families over the sets in
         amplitude-category.md <1>1, followed by the specified set quotient.

<1>5. ASSUME both process arrows are normalized in the source.
       PROVE their composite and independent tensor are normalized.
  <2>1. In <1>1 the deficits vanish identically when S_a=1 and T_b=1.
         Hence the composite squared-amplitude sum equals the identity.
         JUSTIFICATION: the displayed identity in <1>1.
  <2>2. In <1>3 the tensor squared-amplitude sum is 1 tensor 1.
         Identity and structural symmetry arrows also have this property.
         JUSTIFICATION: <1>3,D1322,D1325.
  <2>3. QED: the normalized arrows form a symmetric monoidal subcategory.

<1>6. ASSUME a source-certified process k and a positive input block matrix.
       PROVE its realization is completely positive.
  <2>1. For every auxiliary finite Hilbert space C^n, each amplified output
         block is the finite sum
           sum_(a,j)(I_n tensor H(k_(b,a,j))) rho_a
                     (I_n tensor H(k_(b,a,j)))^*.
         JUSTIFICATION: D1326 and linear amplification on matrix entries.
  <2>2. For positive rho_a, each summand is positive: for every vector v,
         its quadratic form is that of rho_a on
         (I_n tensor H(k_(b,a,j)))^*v, hence nonnegative.
         JUSTIFICATION: the defining quadratic-form criterion for positivity.
  <2>3. Finite sums and direct sums preserve this criterion for positivity.
         JUSTIFICATION: add the nonnegative quadratic forms in <2>2.
  <2>4. QED for every n, which is complete positivity in D1326's target.

<1>7. ASSUME the certificate of D1325 and positive rho=(rho_a).
       PROVE the ordinary trace does not increase.
  <2>1. For any rectangular K and matching rho, direct index summation gives
         Tr(K rho K^*)=Tr(K^*K rho).
         JUSTIFICATION: sum K_(ij)rho_(jk)conj(K_(ik)) over i,j,k;
         named finite-matrix computation RECT-TRACE.
  <2>2. Apply H to the certificate and use RECT-TRACE. The trace deficit is
           sum_(a,l) Tr(H(h_(a,l)) rho_a H(h_(a,l))^*) >= 0.
         JUSTIFICATION: FRP-CAT, D1325 and positivity from <1>6.
  <2>3. For a normalized arrow, the same expression has zero deficit
         because its squared-amplitude sum is exactly I in the source.
         JUSTIFICATION: D1325 and RECT-TRACE.
  <2>4. QED: normalized arrows realize trace-preserving CP maps.

<1>8. ASSUME the equality and composition of D1325.
       PROVE the CP realization is a functor.
  <2>1. A hidden-index bijection permutes a finite sum, and source-equal
         amplitudes have the same H-image by FRP-CAT.
         Thus D1326 depends only on the process arrow class.
         JUSTIFICATION: D1325,D1326 and FRP-CAT.
  <2>2. Expanding R(l)(R(k)(rho)) gives exactly the sum indexed by
         (b,j,t) with amplitude H(l_(c,b,t)k_(b,a,j)).
         JUSTIFICATION: finite distributivity in D1326 and functoriality of H.
  <2>3. The diagonal identity amplitude maps each input block to itself.
         JUSTIFICATION: D1325,D1326.
  <2>4. QED. This proof establishes realization compatibility; it does not
         make realization equality the source definition.

<1>9. ASSUME independent tensor as in D1325 and D1326.
       PROVE R is strong monoidal.
  <2>1. The canonical map distributes a tensor of finite direct sums over
         the Cartesian product of their external tag sets, and identifies
         End(H(X_a)) tensor End(H(Y_b)) with End(H(X_a) tensor H(Y_b)).
         JUSTIFICATION: map elementary matrix units to their tensor matrix
         units; these bases give inverse linear maps, by D1326.
  <2>2. On an elementary tensor rho tensor sigma the Kraus expansion gives
         R(k tensor l)(rho tensor sigma)=R(k)(rho) tensor R(l)(sigma).
         JUSTIFICATION: D1325,D1326 and the tensor comparison of FRP-CAT.
  <2>3. Elementary matrix tensors span the block algebra, so the equality
         extends linearly to every input, including entangled densities.
         JUSTIFICATION: the matrix-unit bases in <2>1.
  <2>4. Coherence follows because both sides of every structural diagram
         perform the same block and matrix-unit reindexing.
         JUSTIFICATION: <1>4,<2>1 and D1326.
  <2>5. QED: this tensor is independent-register tensor.

<1>10. ASSUME a field atom and the preparations/discard of D1327.
        PROVE these are normalized source processes with their named semantics.
  <2>1. e_E and b_(E,a) have squared norm 1 by D1323(7)--(8).
         Their single-amplitude preparation processes are normalized.
  <2>2. The squared-amplitude sum of the basis-bra discard is
         sum_a b_(E,a)b_(E,a)^dagger=1, by D1323(8).
  <2>3. Its realization is rho -> sum_a <a|rho|a>=Tr(rho).
         Code discard conjugates by the unitary t_i; word and tagged
         discard tensor these maps and sum the input blocks.
         JUSTIFICATION: D1324,D1326,D1327 and RECT-TRACE.
  <2>4. QED: source-generated tests have actual state and discard arrows.

<1>11. ASSUME two arrows with the same CP realization.
        PROVE CP equality is not generally source equality.
  <2>1. The singleton amplitude processes {1} and {-1} on the empty word
         are normalized because each squared modulus is 1 in R_p.
         JUSTIFICATION: D1321,D1322,D1325.
  <2>2. They have identical CP realization z -> z.
         JUSTIFICATION: D1326 and (-1)z(-1)=z.
  <2>3. They are different source arrows: singleton-index bijections cannot
         change an amplitude, and 1!=-1 in the amplitude source because
         their H-images on C differ.
         JUSTIFICATION: D1325,FRP-CAT and characteristic zero of R_p.
  <2>4. QED: R is explicitly not faithful; phases are retained at source.

<1>12. ASSUME a tag g is to be retained after another operation.
        PROVE the given process typing can retain it without an equality trick.
  <2>1. Replace that operation's target tags b by pairs (g,b) and, for
         each input g, put its Kraus list in the blocks with matching first
         coordinate. All other blocks have empty hidden lists.
         JUSTIFICATION: D1325; this is an explicit typed family.
  <2>2. The completeness equation for each input block is the original
         equation because the added external tag merely reindexes its terms.
         JUSTIFICATION: D1325 finite sums.
  <2>3. The target can later forget g only by a separately supplied tag
         routing arrow with identical quantum types on routed blocks.
         JUSTIFICATION: D1325 deterministic tag-map definition.
  <2>4. QED: finite controlled histories require no unresolved wiring axiom.

<1>13. QED: FRP-CP follows from <1>1--<1>12.

<1>14. ASSUME s:X->Y is a source isometry.
        PROVE D_s is normalized, d_s is certified, and the success formula holds.
  <2>1. p_s=s s^dagger is self-adjoint and p_s^2=p_s. Consequently
         q_s=1-p_s is self-adjoint and q_s^2=q_s.
         JUSTIFICATION: D1327 and s^dagger s=1.
  <2>2. The decoder squared-amplitude sum is
         (s^dagger)^dagger s^dagger+q_s^dagger q_s=p_s+q_s=1.
         The deficit of d_s alone is q_s=q_s^dagger q_s.
         JUSTIFICATION: <2>1,D1325,D1327.
  <2>3. The success Born weight is
         Tr(H(s)^*rho H(s))=Tr(H(p_s)rho), by RECT-TRACE.
         It is one on code-supported densities and zero on complementary
         densities, directly from p_s^2=p_s and p_s q_s=0.
  <2>4. QED. The failure state remains in H(Y), with its tag retained.

<1>15. ASSUME isometries s:X->Y and t:Y->Z.
        PROVE successful decoding composes and the full retained history normalizes.
  <2>1. The success amplitude s^dagger t^dagger equals (t s)^dagger.
         JUSTIFICATION: the source dagger axiom in D1322.
  <2>2. The three history amplitudes with codomains Z,Y,X are respectively
         q_t, q_s t^dagger, and s^dagger t^dagger.
         Their squared-amplitude sum is
         q_t+t q_s t^dagger+t p_s t^dagger=q_t+t t^dagger=1.
         JUSTIFICATION: <1>14 and source distributivity.
  <2>3. For field transfers the composite ts is j_(ji) or v_(ji).
         JUSTIFICATION: D1323(4), already verified by FRB-TRANSFER.
  <2>4. QED: the success branch has tower coherence. The three-tag output
         is not declared equal to the two-tag decoder of ts.

<1>16. ASSUME independent isometries s:X->Y and t:X'->Y'.
        PROVE the tensor decoder retains four normalized outcomes.
  <2>1. The four amplitudes are s^dagger tensor t^dagger,
         s^dagger tensor q_t, q_s tensor t^dagger, and q_s tensor q_t,
         with respective codomains XX',XY',YX',YY'.
         JUSTIFICATION: D1325,D1327, preserving tensor order.
  <2>2. Their effects are p_s tensor p_t, p_s tensor q_t,
         q_s tensor p_t, q_s tensor q_t and sum to I.
         JUSTIFICATION: <1>14 and tensor distributivity.
  <2>3. The success-success amplitude equals (s tensor t)^dagger. Its
         probability is Tr((H(p_s) tensor H(p_t))rho). On a product state
         this factors; no factorization is claimed on arbitrary rho.
         JUSTIFICATION: D1322,RECT-TRACE and matrix-unit trace factorization.
  <2>4. QED: independent tensor preserves partial-success information.

<1>17. ASSUME the Fourier-dual isometries j_i and v_i.
        PROVE the two retained decoder diagrams agree as source processes.
  <2>1. From f_E j_i=v_i f_K and unitarity,
         v_i=f_E j_i f_K^dagger, so v_i^dagger f_E=f_K j_i^dagger.
         JUSTIFICATION: D1323(2),(5).
  <2>2. Also p_v=f_E p_j f_E^dagger and q_v f_E=f_E q_j.
         JUSTIFICATION: D1327 and <2>1.
  <2>3. Thus D_v after f_E has the same success and failure amplitudes as
         D_j followed by f_K on success and f_E on failure, tag by tag.
         JUSTIFICATION: <2>1--<2>2 and D1325 equality.
  <2>4. QED: this is full branch compatibility, not just equal probabilities.

<1>18. ASSUME code-lifted Frobenius or multiplication and encoding c_i.
        PROVE their physical and encoded process diagrams agree.
  <2>1. The amplitude diagrams agree by amplitude-category.md <1>15.
         They are normalized single-amplitude processes because all gates
         are unitary and c_i is an isometry.
         JUSTIFICATION: D1323,D1325 and amplitude-category.md <1>13--<1>15.
  <2>2. Equal source amplitudes imply equal source processes and equal
         realized channels; successful decoding recovers the logical gate.
         JUSTIFICATION: D1325,FRP-CP and c_i^dagger c_i=1.
  <2>3. QED. Code Weyl lifts use the trace quotient in the same way.

<1>19. QED: FRP-DESCENT follows from <1>14--<1>18 and its pure code proof.

## Falsifier ownership and boundary

A7 checks source/target types, completeness, source-generated preparation and
discard, finite histories, tensor outcomes, and success probabilities.
A3 checks the trace normalizations and negative Fourier kernel independently.
These finite computations are binding falsifiers, not proofs of the general
category theorem. Fixed-p positivity above supplies no q-to-one functor.
