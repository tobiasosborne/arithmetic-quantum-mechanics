# Composition, inclusion and the remaining arithmetic coupling

Status: SKETCH for FRL-COMP and FRL-ACTIVE, pending independent capped
review. Author: root Codex runtime. Definitions D1331--D1334 are in the
single source. Positive orbit-family input: FRL-ORBIT and FRL-POS in
orbit-boundary.md. Arithmetic inputs: FRB-TRANSFER and FRB-NATURAL.

Source comparison: Yoshida, *The Burnside ring and the universal zeta
function of finite dynamical systems*, section 2.2, printed p. 127, gives
the cycle-set product [C(d)][C(e)]=gcd(d,e)[C(lcm(d,e))]. Local snapshot:
refs/frobenius-boundary/yoshida-2014/paper.pdf. The quantum coherence and
reference-state construction here are additional explicit local derivations.

## 1. FRL-COMP: a positive composition category

**ASSUME** D1333 and the positive traces established in FRL-POS.
**PROVE** the word/tag algebras and CPTP maps form a symmetric monoidal
category for every t>=1, with a continuous product reference state. The
constant matrix process families evaluate functorially at t=1, retaining
Frobenius, all listed block instruments and independent quantum tensor.

<1>1. **ASSUME** words R,S and finite output tags.
**PROVE** their algebras and maps have the stated positivity conventions.
  <2>1. Distribute finite tensor over finite direct sum. A simple block
  indexed by (d_1,...,d_n), d_j|r_j and d_j>1, is M_(product_j d_j).
  The reference coefficient on its normalized trace is
  product_j lambda_(r_j,d_j)(t)>0 and the coefficients sum to one.
  **BY** D1333, FRL-POS and finite products of normalized sums.
  <2>2. The ordinary block-trace density is the tensor of D1332's
  sigma_(r_j,t). Hence it is positive, continuous and has trace one,
  including t=1. Tagged families carry ordinary sum trace; no unmentioned
  uniform-tag probability is inserted.
  **BY** <2>1 and Tr(A tensor B)=Tr(A)Tr(B), checked on diagonal entries.
  <2>3. **QED** <1>1. The reference is data, not a requirement that all
  admitted processes preserve this particular state.

<1>2. **ASSUME** the CPTP maps of D1333.
**PROVE** closure under composition and tensor, and symmetric coherence.
  <2>1. Every matrix amplification of a composite is the composite of
  the corresponding positive amplifications. Trace preservation composes.
  **BY** the definition of complete positivity and linear composition.
  <2>2. Phi tensor Psi is (Phi tensor id) followed by (id tensor Psi),
  with matching finite block dimensions. Complete positivity makes these
  maps and their amplifications positive. Applying each trace-preserving
  identity to matrix units gives preservation of the product ordinary trace.
  **BY** D1333 and the defining amplification condition, block by block.
  <2>3. Identity maps and coordinate rebracketings/permutations are CPTP:
  the latter conjugate by permutation unitaries. Their composites act by
  the same coordinate permutation whenever the symmetric coherence diagram
  says they should. Equality is equality of actual linear maps.
  **BY** D1333, permutation multiplication and matrix conjugation.
  <2>4. **QED** closure and coherence. This is a complex CP envelope;
  it is not a fullness assertion about the arithmetic source D1325.

<1>3. **ASSUME** the finite-dimensional matrices in a process are constant
in t, or choose continuous families of CPTP linear maps on the fixed blocks.
**PROVE** evaluation preserves the category and finite protocol probabilities.
  <2>1. Evaluation commutes with finite sums, composition and tensor of
  matrices. Normalization and positivity hold at every point by the stated
  family condition, so evaluation at one has those properties as well.
  **BY** D1333 and componentwise continuous matrix evaluation.
  <2>2. A finite instrument tree gives branch probabilities by finite
  compositions, products and traces of continuous matrices and reference
  densities. These are continuous. Conditional probabilities are continuous
  whenever their specified event has positive limiting probability.
  **BY** <2>1, <1>1 and continuity of sums/products and division by a
  nonzero scalar. Full branches remain linear CP maps before conditioning.
  <2>3. **QED** the categorical positive-family assertion.

## 2. Independent tensor keeps quantum multiplicity

**ASSUME** integers d,e>=1 and D1333's B_(d,e).
**PROVE** B is unitary and

    B^*(S_d tensor S_e)B=I_g tensor S_l,
    M_d tensor M_e is isomorphic to M_g tensor M_l,
    g=gcd(d,e), l=lcm(d,e).

<1>1. **ASSUME** a target pair (i,j). **PROVE** it has a unique preimage.
  <2>1. Choose a to be the residue of j-i in {0,...,g-1}. The required
  k satisfies k=i mod d and k=j-a mod e. These residues agree mod g.
  **BY** D1333 and the choice of a.
  <2>2. Write d=gd', e=ge'. Then d' and e' are coprime. The integer
  Euclidean algorithm provides u,v with ud'+ve'=1. Substitution solves
  d'h=(j-a-i)/g mod e', giving k=i+dh. The solution is unique mod de/g:
  a difference is divisible by both d and e, hence by gd'e'.
  **BY** Euclidean division and the displayed Bezout identity.
  <2>3. There is exactly one k in {0,...,l-1}. Thus B bijects orthonormal
  bases and is unitary. **QED** <1>1 by <2>1--<2>2 and D1333.

<1>2. Replacing k by k+1 adds one to both target coordinates and leaves a
unchanged, including wraparound because l is a multiple of d and e.
Conjugation therefore gives the displayed Frobenius formula. Unitary
conjugation identifies the whole endomorphism algebras; since de=gl, both
normalized ordinary matrix traces agree. **BY** <1>1 and D1331--D1333.

<1>3. **ASSUME** three or more cycle factors.
**PROVE** these reblockings admit coherent associators.
  <2>1. Each binary parenthesization gives, by successive B maps, a
  unitary from its multiplicity/cycle coordinates to the single ordered
  Cartesian Hilbert space. Denote these actual composites T_b.
  **BY** <1>1 and tensoring unitary matrices.
  <2>2. The connector from parenthesization b to c is T_c^*T_b.
  Along any path these products telescope; the result is T_final^*T_initial.
  Consequently the pentagon and all such reassociation diagrams commute.
  The same construction transports the simultaneous Frobenius action.
  **BY** T_b T_b^*=I and ordinary associative matrix multiplication.
  <2>3. **QED**. Internal multiplicity labels need not match literally.

<1>4. **ASSUME** d=e=2. **PROVE** the multiplicity factor cannot be
classicalized while retaining all these quantum processes.
  <2>1. The two simultaneous-shift orbits are {00,11} and {01,10}.
  The normalized vector (|00>+|01>)/sqrt(2) has coherent terms between them.
  Its rank-one test has return probability one on its own state.
  **BY** explicit basis coordinates and the ordinary Born trace.
  <2>2. Dephasing between these two orbits deletes the two cross terms.
  The same rank-one test then has probability 1/2 by expanding its four
  matrix entries. Thus M_2 tensor M_2=M_4 must retain those entries;
  the smaller M_2 direct-sum M_2 loses an observable distinction.
  **BY** the displayed state and entrywise multiplication.
  <2>3. **QED**. The set-level gcd/lcm rule still holds, but its
  orbit multiplicity is a quantum space in this independent tensor category.

## 3. Standard subfield inclusions and their retained instruments

**ASSUME** 2<=r|s, D1333, and at t=p the standard subfield
F_(p^r) subset F_(p^s), with orbit origins coherent as in D1331.
**PROVE** the block encoding and decoder are CPTP, preserve the Frobenius
diagram, compose on success along towers, and have success reference
probability h_(r,s)(t), continuously down to one.

<1>1. The roots of X^(p^r)-X in F_(p^s) are exactly its subfield labels
by orbit-boundary.md Section 1. An orbit belongs to that subfield iff its
length divides r. After removing fixed labels, its support is exactly
R_(p,s)(e_(r,s)). The included physical orbits are the same orbits with
the same origins and multiplicities c_d(p)/d.
**BY** FRL-ORBIT and D1331--D1333.

<1>2. **ASSUME** a block density rho. **PROVE** the CP/instrument assertions.
  <2>1. Zero-block insertion is positive at every amplification, preserves
  ordinary sum trace, and intertwines cycle conjugation blockwise. The
  decoder sends each entire block to precisely one of its two tags; this
  is also positive at every amplification and preserves ordinary sum trace.
  **BY** D1333 and the partition of divisor blocks.
  <2>2. For r|s|v, zero-block insertions compose to j_(r,v); successive
  success restrictions retain precisely the blocks d|r. Products of
  independent decoders retain all four pairs of success/failure tags.
  **BY** transitivity of divisibility and D1333's paired-tag tensor.
  <2>3. Full sequential instruments retain their histories. They are
  not identified with a single binary decoder until a specified classical
  history relabeling is applied; failure keeps its indicated ambient algebra.
  **BY** D1333's output types.
  <2>4. **QED** the stated process assertions.

<1>3. Sum the reference weights of the retained blocks. Divisor inversion
gives (t^r-t)/(t^s-t), tending to (r-1)/(s-1). Dividing the retained density
by that positive probability gives sigma_(r,t) in every block. Tower
probabilities multiply by cancellation, including their limits at one.
**BY** D1332--D1333 and FRL-POS. For 2|4 the boundary probability is 1/3;
two independent such tests have four probabilities 1/9,2/9,2/9,4/9.

<1>4. At p, restricting the observable representation along the physical
inclusion agrees with this block restriction. A physical representative of
a model density rho places rho_d/(c_d(p)/d) on each length-d orbit.
Its ordinary trace is one and its pairing with repeated observables is
the model pairing. Physical inclusion sends it to the corresponding
zero-block inserted representative because those orbit multiplicities agree.
The success and retained-failure operations also agree on these states.
**BY** <1>1, FRL-ORBIT and a sum over equal-period orbit copies.

<1>5. **QED** FRL-COMP by Sections 1--3. The comparisons in <1>4 cover
these specified states and operations. They do not define a unital functor
from every CP map of the envelope to all physical field matrix algebras.
The arithmetic tower here uses standard inclusions; arbitrary named
embeddings need their own compatible orbit-coordinate transport.
The degree-one prime-field register has no moving labels and no conditional
atom here. Thus at p=2 the first inclusion between these active atoms is
F4 subset F16, not F2 subset F4. Retaining the latter requires the ambient
fixed-label sector as additional data.

## 4. FRL-ACTIVE: multiplication and the order retained by tensor

**ASSUME** D1334 and every finite field E of size Q, with d>=1.
**PROVE** the whole-word and conditional identities

    tau(P^nz)=((Q-1)/Q)^d,
    tau(M)=1-((Q-1)/Q)^d,
    tau((M-I)^*(M-I))=2((Q-1)/Q)^d,
    tau^nz(v)=0,  tau^nz((v-P^nz)^*(v-P^nz))=2.

<1>1. There are (Q-1)^d nonzero control tuples and Q target choices.
All other tuples have product zero, so M fixes them. On active controls
the product is nonzero, and target translation has no fixed point.
**BY** the field axioms and D1308,D1334.
<1>2. A permutation matrix's trace counts its fixed basis labels. Dividing
<1>1 by Q^(d+1) gives the first two identities. Expand the squared
difference as 2I-M-M^* to obtain the third.
**BY** D1334, inverse permutations having the same fixed labels, and <1>1.
<1>3. M leaves its controls unchanged, so P^nz commutes with it. Its
restriction v is a unitary in that corner, has zero trace there by <1>1,
and the same expansion gives conditional squared difference two.
**BY** D1334 and <1>1--<1>2.
<1>4. Frobenius preserves nonzero labels, and a field embedding sends
zero to zero and no other point to zero. Thus simultaneous Frobenius
commutes with P^nz and P_(E,d)^nz J_i^tensor(d+1)=
J_i^tensor(d+1) P_(K,d)^nz. Together with FRB-NATURAL this preserves
the restricted multiplication diagram. **BY** D1302,D1304 and injectivity.
<1>5. For two control subsets A,B of one specified word,
P_A^nz P_B^nz=P_(A union B)^nz. Independence of computational labels
gives trace ((Q-1)/Q)^|A union B|. For Q=t^r its leading term at one is
r^|A union B| (t-1)^|A union B|.
**BY** D1334 and multiplying coordinate indicator functions.
<1>6. In contrast, independent moving-orbit words have ambient mass
W_R(t)=product_j(1-t^(1-r_j)), with leading term
product_j(r_j-1) (t-1)^n for a word of length n. Thus independent
normalizations multiply and their vanishing orders add. Conditioning
the entire pair on at least one moving factor has first-order mass, and
is a different operation from conditioning both factors independently.
**BY** D1333 and the Taylor expansion of each scalar weight.
<1>7. **QED** FRL-ACTIVE. For multiplication the order d matches the
interaction arity and the admitted exact hierarchy level d+1. Neither
these identities nor the word order classify arbitrary Clifford levels.

## 5. Concrete remaining mixed relations and the forward target

These supporting scope calculations require no new negative-result campaign.
They identify what the next positive mixed-instrument construction must carry.

<1>1. **ASSUME** F2 subset F4 with alpha^2=alpha+1.
**PROVE** the nonzero cut does not intertwine V on its computational chart.
The trace-zero fibre is {0,1}; hence V|0>=(|0>+|1>)/sqrt(2), so the
nonzero cut gives |1>/sqrt(2), whereas V applied after the F2 nonzero
cut gives zero. **BY** D1303--D1304 and the displayed F4 arithmetic.
**QED**. This concerns the nonzero cut, not a statement about P_r^mov.

<1>2. **ASSUME** three F4 registers, all restricted to moving Frobenius
labels {alpha,alpha^2}. **PROVE** M^(2) does not preserve that tensor corner.
It sends (alpha,alpha,alpha^2) to (alpha,alpha,0), since
alpha alpha=alpha^2. **BY** D1308. **QED**. Its full simultaneous
Frobenius equivariance remains true; equivariance does not preserve each
factor's chosen moving-label cut or the equal-orbit matrix identification.

<1>3. **ASSUME** D1334's P_r^mov and P_r^dual on E=F_(p^r).
**PROVE** their normalized trace overlap is w_r(p)^2.
Every Fourier matrix entry has squared modulus 1/p^r by D1306. If a
coordinate projection has m=p^r-p labels, then
Tr(P_r^mov F_E P_r^mov F_E^*)=m^2/p^r. Divide by p^r to get w_r(p)^2.
The conditional overlap is w_r(p), tending formally to zero.
**BY** entrywise trace expansion and D1306. **QED**. These projections
need not commute; this is an overlap, not an intersection dimension.

The positive next target is to retain the orbit chart, its Fourier chart,
the actual multiplication arrows between measured sectors, and all recorded
success/failure outcomes in a common section algebra. The Fourier overlap
above is a concrete second-order mixed datum. A construction must reproduce
it together with the admitted transfer/Fourier square and arithmetic
multiplication relations. Separate positive corners and constant CP
envelopes do not yet supply that mixed section algebra.
