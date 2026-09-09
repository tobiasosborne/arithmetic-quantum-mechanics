# A collective arithmetic register with relative Frobenius

2026-09-09. Root prover. CMP-SOURCE, CMP-REL, CMP-NATURAL are PROVED
within their stated scopes after capped review and mechanical repair.
Definitions: ../../../definitions.md, D1601--D1606. Existing
inputs: FRP-CAT/CP/DESCENT, FRB-FROB/TRANSFER/NATURAL and FRL-ORBIT.
Every calculation below is finite matrix arithmetic. No origin choice or
characteristic-one field is assumed.

## 1. The completed prelimit source

ASSUME D1601 and the admitted actual arithmetic interpretation.
PROVE the source has independent tensor, finite coherent sums and
self-adjoint retracts, with positive retained quantum processes.

<1>1. ASSUME actual image arrows f,g. PROVE their sums, composites,
adjoints and independent tensors are actual image arrows of the same type.
  <2>1. Each is the interpretation of the corresponding operation on
  arithmetic amplitudes. Equality of actual matrices is preserved by
  these operations. BY FRP-CAT and D1601.
  <2>2. Finite lists and rectangular matrix multiplication supply the
  additive completion, with adjoint transposing the list indices and
  taking the adjoint of each entry. The equations follow entrywise.
  BY D1601 and finite matrix multiplication.
  <2>3. Restricting f=gfe to ran e and ran g respects composition,
  adjoint and identity e. Tensor gives (f tensor f')=(g tensor g')
  (f tensor f')(e tensor e'), and e tensor e' is a projection.
  BY <2>1--<2>2 and the defining equations for projections.
  <2>4. Matrix index rebracketing gives unitary associators. Both paths
  of a pentagon act by the same permutation on indices and the same
  underlying arithmetic tensor. QED <1>1 by <2>1--<2>3 and FRP-CAT.

<1>2. ASSUME a retained Kraus list with sum K_j^*K_j<=I.
PROVE its interpretation is completely positive and trace nonincreasing.
  <2>1. At every matrix level the image of a positive a is the sum of
  (I tensor K_j)a(I tensor K_j)^*, hence positive. BY positive quadratic
  forms and D1601.
  <2>2. Ordinary trace cyclicity gives output trace
  Tr(a sum_j K_j^*K_j)<=Tr(a) for positive a. Equality holds for a
  normalized list. BY the stated inequality and finite trace multiplication.
  <2>3. Composite and tensor lists have the corresponding trace bounds:
  sum_(i,j) K_i^*L_j^*L_jK_i<=sum_i K_i^*K_i<=I, and
  (sum_i K_i^*K_i) tensor (sum_j L_j^*L_j)<=I tensor I.
  BY positivity, multiplication and tensor spectra of positive matrices.
  <2>4. Tags retain the sum of ordinary block traces. Coherent sums
  instead retain rectangular Hom entries. These are different types.
  QED CMP-SOURCE by <1>1--<1>2. This supplies a concrete source and its
  representation, not a faithfulness claim for the older syntactic source.

<1>3. ASSUME a computational label tuple. PROVE its rank-one projector
and the diagonal graph projectors used below are accessible amplitudes.
  <2>1. The zero ket is an arithmetic generator. X(a)|0>=|a> is
  obtained from the D8 Weyl shift with zero momentum. Tensoring and
  taking adjoints gives each tuple ket, bra and matrix unit.
  BY D8, D1323--D1324 and <1>1.
  <2>2. Every graph predicate used here is an explicitly finite set of
  tuples obtained from the named field tables and Frobenius. Sum its
  mutually orthogonal diagonal matrix units. BY <2>1 and D1602.
  <2>3. The resulting projector satisfies the source's actual matrix
  equality, without requiring a new predicate oracle. QED <1>3.

## 2. The origin-free graph basis and relative matrix algebra

ASSUME E/K as in D1602. PROVE CMP-REL's graph register and its generators.

<1>1. ASSUME a sigma-orbit O of length d. PROVE the d vectors v_(O,k)
are orthonormal and the full graph projector is G.
  <2>1. For fixed O,k, there are d distinct tuple labels because their
  first coordinates are distinct. Different O have disjoint first
  coordinates. If k!=l modulo d, sigma^k(x)!=sigma^l(x), by the
  definition of exact orbit length. BY D1602.
  <2>2. Thus each displayed vector has norm one and different pairs
  (O,k) have zero inner product. Every tuple in G belongs to exactly
  one such orbit graph. BY <2>1 and the diagonal definitions.
  <2>3. QED <1>1.

<1>2. ASSUME Delta=U^tensor3. PROVE T is an orthogonal projector,
commutes with every G_(d,k), and P,Q_(d,k) have the claimed ranges.
  <2>1. Delta^n=I. In T^2 each residue modulo n occurs n times, so
  T^2=T; inversion permutes the summands, so T^*=T. Its range is the
  Delta-fixed space: Delta T=T and T fixes every fixed vector.
  BY FRB-FROB and the finite cyclic sum.
  <2>2. Frobenius is a field automorphism, hence sends
  (x,sigma^k x,x sigma^k x) to the same expression with x replaced
  by sigma x. It preserves O,k and transitively permutes its d tuples.
  BY FRB-FROB/NATURAL and D1602.
  <2>3. Therefore the diagonal graph tests commute with Delta and T.
  On each graph T is the rank-one projector |v_(O,k)><v_(O,k)|:
  averaging n steps repeats its d tuples n/d times.
  BY <2>1--<2>2 and <1>1.
  <2>4. Products T G_(d,k), T G and their period sums are orthogonal
  projectors with the advertised ranges. Every coefficient in their
  computational matrices is rational. QED <1>2 by <2>1--<2>3.

<1>3. ASSUME the actual multiplication M. PROVE R is unitary, preserves
all P_d and sends v_(O,k) to v_(O,k+1).
  <2>1. M^* subtracts xy from the third coordinate. Applying the
  middle-slot Frobenius and then M gives
  R(x,y,z)=(x,sigma y,z-xy+x sigma y).
  BY D1308 and D1603.
  <2>2. For a graph tuple z=xy, this becomes
  (x,sigma^(k+1)x,x sigma^(k+1)x). Thus R advances k without changing
  the orbit O or the coefficient of its normalized orbit sum.
  BY <2>1 and D1602.
  <2>3. R is a product of unitaries and R^n=I. M commutes with Delta
  by the field automorphism identity sigma(xy)=sigma(x)sigma(y);
  middle-slot U commutes with Delta, hence R commutes with Delta and T.
  The graph union and its period cuts are invariant under R.
  BY FRB-NATURAL, <2>1--<2>2 and conjugation.
  <2>4. QED <1>3. This is actual Frobenius on one register transported
  through arithmetic multiplication, while simultaneous Frobenius acts
  as identity on the descended register by <1>2.

<1>4. ASSUME D1603's E_(d;a,b). PROVE the common matrix algebra.
  <2>1. On v_(O,k), Q_(d,b) is zero unless |O|=d,k=b. In that case
  R^(a-b) takes it to v_(O,a), fixed by Q_(d,a).
  BY <1>2--<1>3.
  <2>2. Therefore E_(d;a,b)E_(e;c,f) is zero unless d=e,b=c,
  and otherwise equals E_(d;a,f). Adjoints reverse a,b and
  sum_(d,a)E_(d;a,a)=P. BY <2>1 on the orthonormal basis.
  <2>3. Every d|n has c_d(q)>0 labels, hence c_d(q)/d orbits,
  by FRL-ORBIT and its positivity proof applied to q. Each M_d is
  represented faithfully. All generators act identically on repeated
  length-d orbit blocks; their complex algebra is exactly B_n.
  BY <2>1--<2>2, D1603 and FRL-ORBIT.
  <2>4. For d>1, [R,Q_(d,0)]v_(O,0)=v_(O,1)!=0.
  Also Ad(R)E_(d;a,b)=E_(d;a+1,b+1), with indices modulo d.
  This is a trace-preserving CP automorphism on the common block,
  by unitary conjugation; it has order d there.
  QED CMP-REL by <2>1--<2>4 and <1>1--<1>3.

## 3. Collective descent and the correlated preparation

ASSUME D1602 and its copied map C for n>=1. For the retained primitive
instrument assume additionally n>1 as in D1604. PROVE that instrument
is actual and separate orbit descent does not supply the whole relative index.

<1>1. ASSUME a single orbit O. PROVE the separately fixed subspace is
one-dimensional and locate its two-copy image.
  <2>1. A vector fixed by the transitive cyclic permutation has equal
  coefficients on O, hence is a multiple of
  f_O=d^(-1/2)sum_(x in O)|x>. BY coefficient comparison.
  <2>2. Append a zero third register to f_O tensor f_O and apply M.
  Its image is d^(-1)sum_(x,y in O)|x,y,xy>
  =d^(-1/2)sum_k v_(O,k).
  BY the unique y=sigma^k(x) for x,y in O and D1602.
  <2>3. This is only the uniform relative vector, fixed by R. Joint
  invariant descent retains all d orthogonal v_(O,k) instead.
  QED <1>1. This is an orbitwise statement; the full single-field
  system, including its multiplicities, is not claimed to be scalar.

<1>2. ASSUME the two fixed zero ancillas. PROVE C is an arithmetic
isometry and T C|x>=v_(O,0)/sqrt(d) for x in a d-orbit.
  <2>1. Controlled addition copies the computational label into the
  zero second slot; M adds x*x to the zero third slot. The unchanged
  first coordinate makes the resulting label map injective.
  BY D1308 at arities one and two; this copies a basis, not arbitrary
  unknown quantum states as independent states.
  <2>2. T averages the orbit of (x,x,x^2), repeating it n/d times.
  The result is (1/d)sum_(y in O)|y,y,y^2>=v_(O,0)/sqrt(d).
  BY Section 2 <1>2.
  <2>3. The graph relation is preserved throughout. QED <1>2.

<1>3. ASSUME the three Kraus amplitudes in D1604. PROVE completeness.
  <2>1. K_cut^*K_cut=I-Pi_n. Since T is an orthogonal projector,
  K_fail^*K_fail+K_ok^*K_ok=Pi_n C^* C Pi_n=Pi_n.
  BY <1>2, Section 2 <1>2 and D1604.
  <2>2. Their sum is I, so the tagged process is CPTP. Subsequent R
  and the projective measurement Q_(n,1), I-Q_(n,1) are also complete
  on the success output. Every stopped failure retains its stated tag.
  BY Section 1 <1>2 and D1604.
  <2>3. QED <1>3. K_ok^*K_ok is not Pi_n/n on coherent inputs;
  on each primitive orbit it is the projector |f_O><f_O|. The factor
  1/n success used later concerns the specified diagonal reference.

## 4. Fixed-base embeddings and retained comparison maps

ASSUME a named K-embedding i:E->F and the all-period registers D1606.
PROVE CMP-NATURAL.

<1>1. ASSUME x in E. PROVE preservation of orbit lengths and graph vectors.
  <2>1. i(sigma x)=sigma i(x), and injectivity reflects equality of
  iterates. Thus O maps bijectively to an orbit i(O) of the same length.
  Also i(xy)=i(x)i(y). BY the field embedding identities and FRB-FROB.
  <2>2. J_i^tensor3 v_(O,k)=v_(i(O),k), with unchanged normalization.
  BY <2>1 and the finite orbit sum.
  <2>3. Hence P_F J_i^tensor3=J_i^tensor3 P_E. To check on vectors
  outside P_E, note that both graph predicates agree on embedded tuples
  and each simultaneous orbit average has the same value after repetitions.
  BY <2>1, D1602 and the fact [E:K] divides [F:K].
  <2>4. QED <1>1. The maps require no origin choices, including when
  i is a nontrivial field automorphism.

<1>2. ASSUME a tower of such embeddings. PROVE isometric coherence and
the covariance of relative Frobenius and component tests.
  <2>1. J^rel is an isometry by <1>1 and the isometry of J^tensor3.
  Matrix multiplication gives J_j^rel J_i^rel=J_(ji)^rel.
  BY FRB-TRANSFER and restriction to invariant ranges.
  <2>2. The graph-vector formula intertwines R and every length-d,k
  test. A length-d component remains length d upstairs, whether or
  not it is the largest period in the upper field.
  BY <1>1 and Section 2.
  <2>3. A different base field changes the relative Frobenius and is
  outside this fixed-base comparison. QED <1>2.

<1>3. ASSUME each J^rel. PROVE retained decoders and their tower law.
  <2>1. The successful amplitude is (J^rel)^*; the failure amplitude
  is I-J^rel(J^rel)^*. Their squared-amplitude sum is I on the larger
  code. BY the isometry equation in <1>2 and projection multiplication.
  <2>2. Successful amplitudes compose by adjointing <1>2. Sequential
  decoders retain each first failure at its actual code, so the whole
  tower is CPTP without identifying it with a binary composite decoder.
  Independent prelimit decoding retains every product outcome.
  BY <2>1 and Section 1's CP composition/tensor calculus.
  <2>3. QED CMP-NATURAL by <1>1--<1>3. No transfer to an incorrectly
  selected upper primitive component is asserted.

Admission and the single repair wave: ../../verdicts/composite-boundary-adjudication.md.
