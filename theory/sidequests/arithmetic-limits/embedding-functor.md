# Embedding-fibre quantization and retained descent

Claims: GAL-FUNCTOR and GAL-DESCENT. Status: PROVED within the stated hypotheses after capped review.
Author: native inherited Codex runtime; no override, nested CLI or subagent.
Definitions: D1401--D1403 in ../../../definitions.md.
No algebraic object in this shard is assumed to be a field unless stated.

Admission: ../../verdicts/galois-embedding-adjudication.md.

## Source register

S1: Milne, Fields and Galois Theory, version 5.10, September 2022,
`refs/arithmetic-limits/milne-FT/FT.pdf` and `FT.txt`.
Proposition 8.6 and Corollary 8.7: finite etale algebras are products of
finite separable fields and split over a separable closure. Proposition
8.9: tensor closure. Proposition 8.20 and Theorem 8.21: the embedding-set
anti-equivalence, including the split-algebra coordinate formula.
Theorem 6.10: existence and comparison of separable closures.
S2: Stacks, `refs/arithmetic-limits/stacks-04JI/source.html`, Lemma 58.2.2
(03QR): the etale-scheme/continuous-Galois-set equivalence over a field.
All matrix normalization, coherence and instrument arguments below are
local derivations. Their source inputs are S1--S2, not prior sketches.

## 1. The algebra category and normalized isometries

ASSUME any field K and the named separable closure Omega of D1401.
PROVE GAL-FUNCTOR, first the category and the underlying functor.

<1>1. ASSUME an object A of D1401.
       PROVE X_A is nonempty with |X_A|=n_A and its G_K-action is continuous.
  <2>1. By S1, 8.6--8.7 and 8.20, evaluation gives the algebra isomorphism
           A tensor_K Omega -> product_(sigma in X_A) Omega,
           a tensor z -> (sigma(a)z)_sigma.
         The K-vector dimension of A is preserved by scalar extension.
         BY the indicated S1 results and the basis formula for tensoring
         a finite vector space with a field.
  <2>2. Consequently |X_A|=n_A>0. Each sigma has image a finite separable
         field in Omega, so its stabilizer is open in the Krull topology.
         The action on the finite discrete set X_A is continuous.
         BY D1401, S2 and the evaluation coordinates in <2>1.
  <2>3. Permuting the displayed orthonormal basis gives continuous unitary
         U_A^emb, since a finite permutation representation factors through
         a finite discrete quotient. Its group law is composition on labels.
         BY D1401 and <2>2. QED <1>1.

<1>2. ASSUME an allowed f:A->B with rank r_f.
       PROVE every fibre of R_f has cardinality exactly r_f.
  <2>1. In <1>1's evaluation coordinates the scalar extension of f sends
         (a_sigma)_sigma to (a_(R_f(tau)))_tau.
         BY substitution into evaluation and D1402; equivalently S1, 8.20.
  <2>2. The component idempotent at sigma acts on B tensor_K Omega as
         the coordinate projection onto those tau with R_f(tau)=sigma.
         Thus that component has Omega-dimension |R_f^(-1)(sigma)|.
         BY the explicit coordinate action in <2>1.
  <2>3. Because B is an A-module isomorphic to A^(r_f), scalar extension
         and that idempotent instead give dimension r_f. Comparing with
         <2>2 proves |R_f^(-1)(sigma)|=r_f>0 and n_B=r_f n_A.
         BY D1401 and <2>2. QED the uniform-surjection assertion.

<1>3. ASSUME f:A->B and h:B->C are allowed arrows.
       PROVE identities and composites are allowed; their ranks multiply.
  <2>1. The identity has rank one. Module isomorphisms C~B^(r_h) and
         B~A^(r_f) yield C~A^(r_f r_h). They certify rank without
         entering the construction as choices of coordinates.
         BY D1401 and substituting one finite direct sum into another.
  <2>2. Composition and identities are those of unital K-algebra maps,
         hence satisfy the category equations. Every finite separable
         field tower is included: each term is finite etale by S1, 8.6,
         and a finite-dimensional vector space over a field is free.
         BY D1401, <2>1 and the defining vector-space basis property.
  <2>3. QED category closure and r_(h f)=r_h r_f.

<1>4. ASSUME f:A->B and k:C->D are allowed arrows.
       PROVE their tensor arrow is allowed, with rank r_f r_k.
  <2>1. A tensor_K C and B tensor_K D are finite etale by S1, 8.9,
         and nonzero since their vector-space dimensions are n_A n_C
         and n_B n_D, both positive.
         BY S1 and the tensor basis indexed by pairs of basis vectors.
  <2>2. Tensoring the A-module isomorphism B~A^(r_f) with the C-module
         isomorphism D~C^(r_k) yields
           B tensor_K D ~ (A tensor_K C)^(r_f r_k)
         as modules over A tensor_K C.
         BY distributivity of finite direct sums and the tensor action.
  <2>3. The standard algebra associator, unitors and swap have rank one;
         every structural diagram is equality on pure algebra tensors.
         BY D1401, <2>1--<2>2 and rebracketing/permuting pure tensors.
         QED the symmetric monoidal category assertion.

<1>5. ASSUME f:A->B and sigma,sigma' in X_A.
       PROVE s_f is an isometry and intertwines G_K.
  <2>1. Its two columns have inner product
           <s_f sigma,s_f sigma'>=r_f^(-1) sum_tau
             1_(R_f(tau)=sigma) 1_(R_f(tau)=sigma')
           =delta_(sigma,sigma').
         BY D1402, disjoint fibres, and <1>2's fibre count.
  <2>2. R_f(g tau)=g R_f(tau); hence g bijects the fibre over sigma
         with the fibre over g sigma. Applying U_B^emb(g) to the finite
         sum defining s_f gives s_f U_A^emb(g) on every basis vector.
         BY associativity of function composition and D1401--D1402.
  <2>3. QED s_f^*s_f=I and exact equivariance.

<1>6. ASSUME f:A->B and h:B->C.
       PROVE s_(h f)=s_h s_f and s_(id)=I.
  <2>1. Expand s_h s_f|sigma>. A label upsilon in X_C appears exactly
         once if R_f(R_h(upsilon))=sigma and otherwise never, because
         its intermediate label R_h(upsilon) is uniquely determined.
         Its nonzero coefficient is 1/sqrt(r_f r_h).
         BY D1402 and collecting coefficients in two finite sums.
  <2>2. Restriction satisfies R_(h f)=R_f R_h and <1>3 supplies the
         product rank. The preceding coefficient is therefore exactly
         the defining coefficient of s_(h f). Identity fibres are singletons.
         BY D1402, <1>3 and <2>1. QED exact tower functoriality.

<1>7. ASSUME f,k:A->B have s_f=s_k.
       PROVE f=k, so the functor is faithful on its stated arrows.
  <2>1. The nonzero entries of s_f recover R_f, one specified source
         label per target row. Thus R_f=R_k.
         BY D1402 and positive r_f; no phase cancellation is present.
  <2>2. The embedding-set functor on all finite etale algebra maps is
         faithful by S1, 8.20 or S2. Hence f=k.
         BY <2>1 and the cited source. QED faithfulness, not fullness.

## 2. Tensor coherence and canonicity

<1>8. ASSUME objects A,C.
       PROVE mu_(A,C) is a G_K-equivariant unitary.
  <2>1. A homomorphism A tensor_K C->Omega restricts to a unique pair
         (sigma,tau). Conversely that pair defines a homomorphism by
         a tensor c -> sigma(a)tau(c), since Omega is commutative.
         These constructions are inverse on pure tensors.
         BY the tensor product's defining bilinear universal property.
  <2>2. Thus mu bijects orthonormal bases. Postcomposing the product
         homomorphism by g multiplies g sigma(a) and g tau(c), so mu
         intertwines the diagonal G_K action on the Hilbert tensor.
         BY D1402, <2>1 and g preserving multiplication. QED.

<1>9. ASSUME arrows f:A->B and k:C->D.
       PROVE s_(f tensor k) mu_(A,C)=mu_(B,D)(s_f tensor s_k).
  <2>1. Under <1>8's Cartesian bijection, R_(f tensor k) is R_f times R_k.
         The fibre of a pair is the Cartesian product of its two fibres.
         BY evaluation on a tensor c and D1402.
  <2>2. Each coefficient in the two-factor sum is
         r_f^(-1/2)r_k^(-1/2)=(r_f r_k)^(-1/2).
         This is the tensor arrow's normalization from <1>4.
         BY <2>1, D1402 and positive real square roots. QED naturality.

<1>10. ASSUME any finite ordered list of objects and its parenthesizations.
        PROVE strong symmetric monoidal coherence, including unit and swap.
  <2>1. Every iterated comparison sends the tuple (sigma_1,...,sigma_m)
         to the homomorphism with value product_j sigma_j(a_j) on a pure
         tensor. Algebra and Hilbert associators simply rebracket this tuple.
         BY <1>8 and associativity of multiplication in Omega.
  <2>2. The pentagon paths agree on all basis tuples, hence on all vectors.
         The unique embedding of K supplies the unit comparisons, and
         commutativity in Omega verifies the swap and symmetry hexagon.
         BY <2>1 and the basis formulas of D1402. QED tensor coherence.

<1>11. ASSUME another named separable closure Omega' and a named
        K-isomorphism eta:Omega->Omega'.
        PROVE W_eta is a natural monoidal unitary with conjugated G-action.
  <2>1. Postcomposition by eta is a bijection of all embedding sets, so
         W_(eta,A) is unitary. It carries each restriction fibre to the
         corresponding restriction fibre with the same rank.
         BY D1402 and invertibility of eta.
  <2>2. Hence W_(eta,B)s_f=s'_f W_(eta,A). Multiplicativity of eta
         also gives W_(eta,A tensor C)mu_(A,C)
         =mu'_(A,C)(W_(eta,A) tensor W_(eta,C)), including the unit.
         BY <2>1 and the defining finite sums and pure tensor formulas.
  <2>3. The identity eta g tau=(eta g eta^-1)(eta tau) proves
         W_(eta,A)U_A^emb(g)=U_A'^emb(c_eta(g))W_(eta,A).
         Conjugation c_eta carries pointwise stabilizers of finite subsets
         of Omega to those of their eta-images; it is a homeomorphism
         for the Krull topologies by D1401's finite stabilizer basis.
         If theta:Omega'->Omega'' is another comparison, then
         W_(theta eta,A)=W_(theta,A)W_(eta,A) exactly.
         BY D1402 and composition on embedding labels.
  <2>4. Such eta exist by S1, 6.10. If eta' is another, then
         h=eta' eta^-1 belongs to Aut_K(Omega'), and W_eta'=U'^emb(h)W_eta.
         No chosen eta is asserted to be distinguished.
         BY S1 and <2>3. QED GAL-FUNCTOR, with explicit choice dependence.

## 3. Complete positivity, histories and independent outcomes

ASSUME D1403 and the isometries just established.
PROVE GAL-DESCENT using ordinary matrix trace on every output block.

<1>12. ASSUME any allowed f:A->B.
        PROVE E_f and D_f are CPTP, d_f is trace nonincreasing, and all
        their branches intertwine the G_K conjugation channels.
  <2>1. A map rho->K rho K^* is completely positive: its amplification
         sends Z^*Z to ((I tensor K)Z^*)((I tensor K)Z^*)^*.
         Sums and tagged direct sums of these maps remain positive at
         every amplification by summing their positive quadratic forms.
         BY this displayed factorization and D1403's positivity definition.
  <2>2. P_f is an orthogonal projection since s_f^*s_f=I. Thus Q_f^2=Q_f
         and the decoder's squared Kraus operators sum to
           (s_f^*)^*s_f^*+Q_f^*Q_f=P_f+Q_f=I.
         The encoder's squared amplitude is I, while that of success is P_f<=I.
         BY <1>5 and D1403.
  <2>3. Entrywise summation gives Tr(K rho K^*)=Tr(K^*K rho), even for
         rectangular K. The completeness identities in <2>2 prove the
         two trace-preserving and one trace-nonincreasing assertions.
         BY <2>1--<2>2 and this finite trace computation.
  <2>4. Since U_B s_f=s_f U_A, taking adjoints and replacing g by g^-1
         gives s_f^* U_B=U_A s_f^*. Also U_B commutes with P_f and Q_f.
         Substitute these identities into every Kraus formula.
         BY <1>5. QED CP normalization and branchwise Galois equivariance.

<1>13. ASSUME a density rho on H_A^emb and the reference rho_B^mix.
        PROVE exact encoded recovery and reference success probability 1/r_f.
  <2>1. d_f(E_f(rho))=rho and Q_f s_f=0. Therefore D_f(E_f(rho))=(rho,0).
         BY s_f^*s_f=I and Q_f=I-s_f s_f^*.
  <2>2. d_f(I/n_B)=I_(H_A)/n_B, whose trace is n_A/n_B=1/r_f.
         Upon conditioning on this success the density is rho_A^mix.
         If r_f>1, failure has probability 1-1/r_f and conditional
         density Q_f/(n_B-n_A); if r_f=1 its probability is zero.
         BY <1>2, D1401,D1403 and rank(P_f)=n_A. QED.

<1>14. ASSUME f:A->B and h:B->C.
        PROVE success composition and CPTP stopped histories in this tower.
  <2>1. d_f d_h(rho)=s_f^*s_h^*rho s_h s_f=d_(h f)(rho).
         BY <1>6 and D1403. The same calculation proves E_h E_f=E_(h f).
  <2>2. The stopped history has amplitudes s_f^*s_h^*:C->A,
         Q_f s_h^*:C->B, Q_h:C->C, with tags success-success,
         success-failure and first-failure. Their squared sum is
           s_h(P_f+Q_f)s_h^*+Q_h=P_h+Q_h=I.
         BY <1>12 and multiplication of the explicitly typed amplitudes.
  <2>3. For any longer tower, replacing a success amplitude K by the
         two amplitudes s_f^*K,Q_f K preserves its contribution K^*K
         to completeness. Induction gives every stopped history with its
         correct ambient output; the all-success amplitude is the adjoint
         of the composite isometry by <1>6.
         BY <2>2 and distributivity. Parenthesization of a fixed retained
         history tree changes no amplitude, by associative multiplication.
  <2>4. QED exact success composition and normalized full histories.

<1>15. ASSUME a strict two-step tower and put R=s_h Q_f s_h^*.
        PROVE why histories are retained instead of imposing binary equality.
  <2>1. R=P_h-P_(h f), R Q_h=0, and Q_(h f)=R+Q_h.
         After re-encoding the intermediate failure with s_h, merging
         the two failure tags gives R rho R+Q_h rho Q_h.
         BY D1403 and multiplication of the amplitudes of <1>14.
  <2>2. The binary composite decoder instead has failure
         (R+Q_h)rho(R+Q_h). If R and Q_h are both nonzero, choose unit
         vectors v in Ran(R),w in Ran(Q_h), and rho=|v+w><v+w|/2.
         The two maps differ by (|v><w|+|w><v|)/2.
         BY <2>1 and direct expansion. The surviving positive strategy
         is the fully specified history process, already proved in <1>14.
  <2>3. QED the stated scope distinction; no additional theorem is claimed.

<1>16. ASSUME two allowed arrows f and k, with possibly entangled input.
        PROVE independent decoding is CPTP with every paired outcome.
  <2>1. Its four amplitudes are s_f^* tensor s_k^*, s_f^* tensor Q_k,
         Q_f tensor s_k^*, Q_f tensor Q_k. Their squared sum is
           (P_f+Q_f) tensor (P_k+Q_k)=I tensor I.
         BY D1403 and multiplying elementary tensors of matrices.
  <2>2. By <1>12's amplification argument these formulas are CP on all
         matrices, without a product-input assumption. Completeness proves
         trace preservation. Equivariance holds on each paired output.
         BY <2>1 and <1>12, applied to the diagonal G_K action.
  <2>3. On rho_B^mix tensor rho_D^mix the outcome probabilities are
         (1/r_f,1-1/r_f) tensor (1/r_k,1-1/r_k).
         This follows from Tr(M tensor N)=Tr(M)Tr(N), proved on diagonal
         entries, and <1>13. Entangled inputs need not factor their probabilities.
  <2>4. Every additional independent factor multiplies the completeness
         identity and retains all its tags. Cartesian reassociations and
         closure changes transport the amplitudes, projections and output
         blocks by <1>9--<1>11; their unitaries preserve ordinary trace.
         BY <1>9--<1>11 and substitution into D1403.
  <2>5. QED GAL-DESCENT. Only the all-success amplitude equals that of
         the binary decoder of the tensor isometry; full instruments retain
         their different prescribed outcomes and quantum outputs.
