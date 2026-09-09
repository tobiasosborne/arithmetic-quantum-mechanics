# Positive period references and a uniform mixed arithmetic experiment

Native inherited Codex prover runtime; no model override or nested CLI.
Status: POS-STATE, POS-DIAGRAM, POS-COUNTS, POS-MIXED are PROVED
within their stated hypotheses after capped review. Definitions are ../../../definitions.md,
D1501--D1503,D1507. Existing inputs: FRL-ORBIT/POS, FRB-TRACE/TRANSFER,
MIX-GRAM and the actual D1308 multiplication gate. Every new step is an
internal count, convergent finite-exponential calculation or matrix identity.

Admission: ../../verdicts/positive-arithmetic-adjudication.md.

## 1. Canonical period masses and positive Jordan coefficients

**ASSUME** D1501 with actual E=F_(p^r), r>=1, h>=0.
**PROVE** positivity, normalization, uniqueness and the D1502 expansion.

<1>1. **ASSUME** a divisor d of r and an integer k>=1.
**PROVE** `J_k(d)>0` and `sum_(d|r)J_k(d)=r^k`.
  <2>1. In `sum_(e|d)mu(d/e)e^k`, put a=d/e. Terms with nonsquarefree
  a vanish; choosing a subset of the distinct prime factors of d gives
  `d^k product_(ell|d prime)(1−ell^(−k))` by product expansion.
  Every factor is positive. For d=1 the empty product is one.
  **BY** D1502 and the integer Moebius definition.
  <2>2. Interchanging finite divisor sums gives
  `sum_(d|r)sum_(e|d)mu(d/e)e^k
   =sum_(e|r)e^k sum_(a|r/e)mu(a)=r^k`.
  The inner sum is zero except at r/e=1, by expanding
  `product_(ell|r/e prime)(1−1)`.
  **BY** finite sums and the same product expansion.
  <2>3. **QED** <1>1. Named computation: JORDAN-POSITIVE-SUM.

<1>2. **ASSUME** D1501's b_d.
**PROVE** `b_d(exp h)=sum_(k>=1)h^k J_k(d)/k!` for every d>=1.
  <2>1. For d>1 expand each of the finitely many exponentials
  `exp(e h)`; its constant divisor sum is zero. For d=1,
  `exp(h)−1=sum_(k>=1)h^k/k!` agrees with J_k(1)=1.
  **BY** the exponential series and the Moebius sum in <1>1.
  <2>2. The series converges absolutely for every complex h because
  it is a finite linear combination of entire exponential series.
  Every nonconstant coefficient is strictly positive by <1>1.
  Therefore b_d(exp h)>0 for h>0; in particular b_d(p)>0.
  **BY** <2>1, <1>1 and log p>0.
  <2>3. **QED** <1>2. Named computation: NONZERO-PERIOD-SERIES.

<1>3. **ASSUME** the exact-period census FRL-ORBIT.
**PROVE** D_E and rho_E have the stated coefficients, traces and masses.
  <2>1. P0 and the nonzero period projections form an orthogonal
  partition of the computational basis. Their ranks are 1,b_d(p):
  remove zero from the p fixed labels for d=1, and use FRL-ORBIT
  for d>1. **BY** D1501 and FRL-ORBIT.
  <2>2. Substitution of <1>2 into D1501 gives D_E=sum h^k A_Ek.
  For k>=1 every scalar on a nonzero period block is positive, so
  A_Ek is positive definite on the nonzero-label subspace. Its trace is
  `sum_(d|r)J_k(d)/k!=r^k/k!`.
  A_E0=P0 has trace one.
  **BY** D1502, <2>1 and JORDAN-POSITIVE-SUM.
  <2>3. Consequently `Tr D_E=exp(rh)` and rho_E has trace one.
  For h>0 its zero eigenvalue-block coefficient is exp(−rh)>0, and
  every nonzero-label coefficient is also positive; hence it is faithful.
  At zero it is P0. At h=log p every coefficient of D_E equals one,
  so rho_E=I/p^r. **BY** D1501 and <2>2.
  <2>4. A matrix in the prescribed real span has one scalar on each
  orthogonal block. Its prescribed block trace, divided by that block's
  positive rank, uniquely determines that scalar. This gives exactly rho_E.
  **QED** <1>3 by <2>1--<2>3 and D1501's explicit class-uniformity.

<1>4. **ASSUME** the full algebra End(H_E).
**PROVE** the reference is tracial exactly when h=log p.
  <2>1. On the two basis labels zero and one, the diagonal weights
  are `exp(−rh)` and `exp(−rh)(exp h−1)/(p−1)`.
  The expectation of the commutator of `|0><1|` and `|1><0|`
  is their difference. It vanishes exactly at exp h=p.
  **BY** D1501 and multiplication of matrix units.
  <2>2. A tracial functional must vanish on every commutator. At
  exp h=p the state is the normalized ordinary trace by <1>3.
  **QED** <1>4 by <2>1--<2>2.

## 2. Poisson grades and independent preparation

**ASSUME** D1502 and a nonempty word E_1,...,E_m of total degree R.
**PROVE** the exact Poisson mixture and multinomial tensor formula.

<1>1. **ASSUME** one register E.
**PROVE** sigma_Ek are states and
`rho_E(h)=exp(−rh)sum_(k>=0)(rh)^k sigma_Ek/k!`.
  <2>1. Positivity and traces in section 1 make each normalized
  sigma_Ek positive with trace one. Substitution into the series of
  D_E gives the displayed formula. The Poisson weights sum to one.
  **BY** D1502 and section 1 <1>3.
  <2>2. Convergence holds in trace norm: for complex h the sum of
  coefficient trace norms is `sum |h|^k Tr A_Ek=exp(r|h|)`.
  **QED** <1>1 by <2>1 and the positive coefficient traces.

<1>2. **ASSUME** independent preparation on the word.
**PROVE** `Tr A_(word,k)=R^k/k!` and

    sigma_(word,k)=sum_(k_1+...+k_m=k)
      [k!/(product_j k_j!) product_j (r_j/R)^k_j]
      tensor_j sigma_(E_j,k_j).

  <2>1. Multiply the absolutely convergent series for the factors.
  The coefficient at k is D1502's Cauchy sum. Its trace is the
  coefficient of h^k in `product_j exp(r_j h)=exp(Rh)`.
  **BY** <1>1 and finite tensor-product trace multiplication.
  <2>2. Replace each coefficient by `r_j^k_j sigma_jk_j/k_j!`
  and divide by R^k/k!. The weights are nonnegative and sum to one
  by the multinomial expansion of `(sum_j r_j/R)^k`.
  For m=2 these are the binomial weights.
  **QED** POS-STATE by <2>1--<2>2 and section 1.

## 3. Every named embedding and tower, with transported Fourier contexts

**ASSUME** a D1303 named embedding i:K->E, |K|=p^s, |E|=p^r.
No restriction on divisibility of the relative degree r/s is made.
**PROVE** POS-DIAGRAM's exact reference restrictions and instruments.

<1>1. **ASSUME** a basis label x in K.
**PROVE** i preserves zero and exact absolute Frobenius periods.
  <2>1. `i(x)^(p^d)=i(x^(p^d))`; injectivity makes equality to i(x)
  equivalent to equality x^(p^d)=x. The least positive such d is
  therefore identical. Zero is preserved and reflected by injectivity.
  **BY** field embedding identities and D1302.
  <2>2. The coefficients assigned to period d use b_d(p), independent
  of the ambient extension degree. Therefore
  `J_i^*D_E J_i=D_K`, and coefficientwise `J_i^*A_Ek J_i=A_Kk`.
  In particular `J_i^*L_E J_i=L_K`.
  **BY** D1501--D1503 and <2>1.
  <2>3. Every U_E permutes labels within their period block, so
  U_E commutes with D_E, every A_Ek and L_E.
  **QED** <1>1 by <2>1--<2>2 and D1302.

<1>2. **ASSUME** normalized reference rho_E and the retained J decoder.
**PROVE** success probability exp((s−r)h), output rho_K, and tower coherence.
  <2>1. The successful unnormalized matrix is
  `J_i^*rho_E J_i=exp(−rh)D_K=exp((s−r)h)rho_K`.
  Taking its trace gives the asserted probability; division yields rho_K.
  **BY** <1>1 and section 1's trace normalization.
  <2>2. In a named tower J maps compose strictly by FRB-TRANSFER.
  Repeated restrictions give the same D and L matrices; the exponential
  success probabilities multiply by adding degree differences.
  This uses no division by a degree inside a finite field.
  **BY** <2>1 and FRB-TRANSFER.
  <2>3. For lambda_E instead, success is `(1+s h)/(1+r h)` and
  the conditional output is lambda_K. It is a different finite-h family,
  with the same exact unnormalized restriction and endpoint record.
  **QED** <1>2 by <1>1 and Tr L_E=1+rh.

<1>3. **ASSUME** Fourier-transported reference `F_E rho_E F_E^*`.
**PROVE** its V decoder has the transported smaller reference, with both tags.
  <2>1. `F_E J_i=V_i F_K` gives
  `V_i^*F_E D_E F_E^*V_i=F_K D_K F_K^*`.
  Apply adjoints and <1>1; normalizing gives success exp((s−r)h)
  and conditional density F_K rho_K F_K^*.
  **BY** FRB-TRANSFER and matrix multiplication.
  <2>2. The failure projections obey
  `(I−V_iV_i^*)F_E=F_E(I−J_iJ_i^*)`. Thus the entire retained
  decoder square commutes, with F_K on success and F_E on failure.
  The same calculation holds for L and coefficient by coefficient.
  **BY** FRB-TRANSFER and the displayed projection identity.
  <2>3. Canonical rho_E need not be Fourier invariant: at zero it
  is P0, whose Fourier image is `|+_E><+_E|`, a different matrix.
  **QED** POS-DIAGRAM by <2>1--<2>2 and <1>1--<1>2.

The references are natural under named field embeddings and isomorphisms,
not under every Hilbert-space coordinate identification. A named prime-field
basis gives an actual coordinate unitary, which transports D_E to its actual
generally correlated image. It does not reset that image to a product of
prime-field references. For r>1 a coordinate tuple with all entries nonzero
has order one under the transported single-field reference, versus order r
under the independent prime-field word. All constant coordinate-unitary
source equations are retained; no extra reference-preservation equation is added.

## 4. Frobenius, active multiplication and the moving-orbit comparison

**POS-COMPLEMENT-EXAMPLE. ASSUME** i:F2->F8 and t=exp(h)>=1.
**PROVE** the new expectation of I-E_i is `(2/3)(1-t^(-2))`.
<1>1. MIX-GRAM gives joint-code rank four; it contains the prime-field
basis vectors 0,1. The complement therefore has rank four and annihilates
those two vectors. **BY** MIX-GRAM's regular degree-three case and D1421.
<1>2. Every remaining label has period three: the only divisors of the
absolute degree three are 1,3, and the period-one labels are exactly F2.
D1501 gives their common diagonal weight `(t^3-t)/(6t^3)`.
**BY** FRL-ORBIT and D1501 with b_3(2)=6.
<1>3. Taking the trace against I-E_i sums four times that weight, yielding
`(2/3)(1-t^(-2))`. The earlier formal tracial expression was `1-2/t^2`
by MIX-GRAM with formal kappa=t^2; both equal 1/2 at t=p=2.
The new expression is nonnegative for t>=1. **QED** by <1>1--<1>2,
entrywise trace and scalar arithmetic. This illustrates the changed
reference prescription, not an extension of the same full trace.

**ASSUME** D1501 and an integer k, with gcd(r,0)=r.
**PROVE** the reference Frobenius moment is exp((gcd(r,k)−r)h).

<1>1. **ASSUME** g=gcd(r,k).
**PROVE** the fixed-label weighted trace of U_E^k is exp(gh).
  <2>1. A label of exact period d is fixed by U_E^k exactly when
  d divides k, hence d divides g. For a diagonal density times a
  permutation, the trace sums precisely its fixed-label diagonal entries.
  **BY** D1302 and entrywise trace multiplication.
  <2>2. Those entries sum to `1+sum_(d|g)b_d(exp h)=exp(gh)`.
  The last identity follows coefficientwise from JORDAN-POSITIVE-SUM,
  or by the finite divisor identity for the period-count polynomials.
  Divide by exp(rh) to obtain the normalized moment.
  **QED** <1>1 by <2>1--<2>2.

<1>2. **ASSUME** d>=1 independent E controls and one E target, with
the actual reversible gate `M|x_1,...,x_d,z>=|x_1,...,x_d,z+product x_j>`.
**PROVE** active mass `(1−exp(−rh))^d`, gate trace one minus this mass,
and squared-difference expectation twice this mass.
  <2>1. Each zero control has reference probability exp(−rh).
  Independence gives the active mass. M fixes a computational tuple
  exactly when at least one control is zero, since E is a field.
  The diagonal product reference therefore gives the stated gate trace.
  **BY** D1501, the field no-zero-divisor law and matrix trace.
  <2>2. M and M^* have the same fixed labels. Expand
  `(M−I)^*(M−I)=2I−M−M^*` and take the reference expectation.
  The active-control projection commutes with M because controls remain
  unchanged, so conditioning that corner gives gate trace zero and
  squared-difference expectation two.
  **BY** D1308, <2>1 and matrix multiplication.
  <2>3. The active mass has exact order d, leading coefficient r^d,
  because `1−exp(−rh)=rh+O(h²)`. No invariance of the target reference
  under translations is assumed or needed.
  **QED** <1>2 by <2>1--<2>2 and the scalar exponential expansion.

<1>3. **ASSUME** r>=2 and the marked FRL orbit-algebra representation.
**PROVE** moving-label conditioning recovers its admitted reference.
  <2>1. On a length-d orbit, D_E is scalar b_d(exp h)/b_d(p).
  For d>1 there are b_d(p)/d orbits, each carrying the same matrix
  a_d. Thus their contribution is b_d(exp h)tr_d(a_d).
  **BY** D1501 and FRL-ORBIT's marked representation.
  <2>2. Removing fixed labels keeps d>1, with total weight
  `exp(−rh)(exp(rh)−exp h)`. After conditioning the block weight is
  `b_d(exp h)/(exp(rh)−exp h)`, tending to phi(d)/(r−1).
  The derivative J_1(d)=phi(d) is the product in section 1.
  **QED** POS-COUNTS by <2>1, section 1 and FRL-POS, together with
  <1>1--<1>2. For r=1 there is no moving-label conditional sector.

**Direct coefficient-one consequence.** ASSUME K=F_(p^s) subset E,
r=sn and an integer j. PROVE
`Tr(sigma_(E,1) U_E^(sj))=gcd(n,j)/n`.
<1>1. Section 4 <1>1 gives
`Tr(D_E(h)U_E^(sj))=exp(gcd(r,sj)h)`. Its coefficient of h is
`Tr(B_E U_E^(sj))=gcd(r,sj)` by the reviewed entire expansion.
**BY** D1502 and section 4 <1>1.
<1>2. Divide by r, using `sigma_(E,1)=B_E/r` and
`gcd(sn,sj)=s gcd(n,j)`. **QED** by <1>1 and integer divisibility.
This extracts a universal relative-Galois moment from the admitted formulas;
it adds no new reference or amplitude construction. For j not divisible by
n the value is strictly below one, while the full state can still depend on p.

## 5. A coherent mixed witness for every proper extension

**ASSUME** a named i:K->E of degree n>=2, q=p^s and Q=p^r.
**PROVE** D1507 is well defined and has POS-MIXED's operational distinctions.

<1>1. **ASSUME** an element a0 outside i(K), identifying K with its named image.
**PROVE** there exist a,b with T(ab)=0 and T(a^q b)=1.
  <2>1. Such a0 exists because Q>q. Its q-th power differs from a0:
  the q roots of X^q−X are exactly the q elements of i(K), since
  a degree-q nonzero polynomial has at most q roots.
  **BY** FRB-TRACE's finite-field Frobenius facts and polynomial division.
  <2>2. If a0,a0^q are K-linearly independent, use a=a0.
  Otherwise a0^q=lambda a0 with lambda in K and lambda!=1.
  For a=a0+1, its q-th power is lambda a0+1. If proportional to a,
  comparing coefficients of the independent pair a0,1 would force
  the proportionality scalar both lambda and one, a contradiction.
  **BY** <2>1 and K-linearity of q-th powering.
  <2>3. The relative trace pairing is nondegenerate: for u!=0 choose
  z with T(z)=1 by FRB-TRACE and put v=z/u, giving T(uv)=1.
  Hence the two K-linear functionals b->T(ab),b->T(a^q b) are independent.
  Otherwise their linear relation would contradict <2>2 by nondegeneracy.
  **BY** FRB-TRACE's surjectivity and <2>2.
  <2>4. Two independent linear functionals give a surjection to K².
  Explicitly, the second is nonzero on the first's kernel, since otherwise
  subtracting a suitable multiple of the first would make it zero everywhere.
  Choose b in that kernel and scale its nonzero second value to one.
  In particular b!=0 and a!=0.
  **QED** <1>1 by <2>1--<2>4. Named computation: TRACE-PAIR-CHOICE.

<1>2. **ASSUME** D1507's selected a,b and the rare preparation outcome.
**PROVE** order two, coefficient w_a w_b, and target output one.
  <2>1. Each selected nonzero label x has first density coefficient
  `w_x=phi(period(x))/b_(period(x))(p)>0`; the zero target has
  coefficient one at order zero. Independent preparation therefore has
  order two and leading coefficient w_a w_b. The selected state is
  exactly the basis vector `|a,b,0>` after conditioning.
  **BY** D1501--D1503 and section 1.
  <2>2. After V encoding and relative Frobenius the target is V|0>
  and the controls are a^q,b. Multiplication translates the target by
  a^q b. Trace linearity gives `X_E(z)V|x>=V|x+T(z)>`, so the
  target becomes V|1>. Fourier sends this to J F_K|1>.
  **BY** D1304,D1308, TRACE-PAIR-CHOICE and FRB-TRANSFER.
  <2>3. J decoding succeeds with probability one, with zero failure
  output; successful F_K^* returns exactly |1>. Control registers may
  be discarded without changing this target assertion.
  **QED** <1>2 by <2>1--<2>2 and isometry normalization.

<1>3. **ASSUME** the specified individual protocol modifications.
**PROVE** each changes an observable outcome as claimed.
  <2>1. Without relative Frobenius the translation has trace T(ab)=0;
  without multiplication it is zero. In both cases the successful
  decoded target is |0>, with success one.
  **BY** the target calculation in <1>2 and TRACE-PAIR-CHOICE.
  <2>2. Without F_E the decoder acts on V|1>. MIX-GRAM gives
  `J^*V|1>=kappa^(-1/2)|1/n>` when p∤n, hence success 1/kappa
  and conditional final target F_K^*|1/n>. If p|n its Gram column
  at the nonzero label one vanishes, hence success zero.
  **BY** MIX-GRAM in both characteristic strata.
  <2>3. Dephasing V|0> gives the uniform mixture on its kappa labels.
  After translation each label y has T(y)=1. For every such y,
  `J^*F_E|y>=kappa^(-1/2) F_K|1>` by the trace-adjoint Fourier kernel.
  Thus the decoder succeeds with 1/kappa and still returns |1> on success.
  **BY** D1306, FRB-TRACE and summing the mixture of identical compressed
  rank-one outputs. Named computation: TRACE-FIBRE-COHERENCE.
  <2>4. For F4=F2[alpha]/(alpha²+alpha+1), take a=alpha,b=alpha².
  Then ab=1 has trace zero and a²b=alpha has trace one.
  Each selected control coefficient is phi(2)/(4−2)=1/2, giving 1/4.
  Changing the entry alpha² alpha² from alpha to zero changes the
  final target from one to zero in this protocol.
  **QED** POS-MIXED by <2>1--<2>4 and <1>1--<1>2.

This is an actual coherent trace-fibre/Fourier protocol, with all finite
field data and the choices a,b named. The output distinction is uniform
over every proper extension; its preparation coefficient and register
dimensions retain characteristic dependence. The finite-profile theorem
in the companion shard supplies the same boundary records under L.
