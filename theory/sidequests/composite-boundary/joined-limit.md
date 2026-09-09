# A uniform quantum boundary of finite degree assemblies

2026-09-09. Root prover. CMP-JOINT-LIMIT is PROVED at its stated scope
after a distinct capped review and one definition clarification.
Definition D1621 is in ../../../definitions.md. Inputs:
CMP-BOUNDARY/TRACE, the positive period polynomials FRL-ORBIT/POS,
and the degree completion CMP-COMPLETE/MELLIN at their reviewed scopes.
This is a distinct artifact with its own review and finite falsifiers;
its proof is not inherited from the reviews of its input claims.

## 1. An actual finite sum of arithmetic experiments

ASSUME D1621 with s>=1, beta>1, integer D>=2 and t>1.
PROVE the declared finite protocol has a positive normalized input,
all failure histories, and the displayed common successful density.

<1>1. ASSUME the finite classical prior.
PROVE normalization and the type of the input state.
  <2>1. Each weight pi_d=d^(-beta)/L_D(beta) is positive and the
  weights sum to one. On the tagged field algebra, use the block
  density pi_d rho_(E_d)(log t). Each block is positive and the sum
  of ordinary traces is one. BY D1621 and POS-STATE.
  <2>2. Each block then uses one copied reference, two fixed zero
  ancillas and the actual arithmetic instrument of D1604. This is
  a finite tagged sum of CPTP processes. BY CMP-SOURCE/BOUNDARY.
  <2>3. The real degree prior is extra classical preparation data.
  No arithmetic matrix coefficient or field operation was replaced.
  QED <1>1 by <2>1--<2>2.

<1>2. ASSUME the successful degree-d preparation and randomization.
PROVE its state and mixture weights.
  <2>1. CMP-BOUNDARY gives physical success w_d(t) and common
  state |0><0|. Uniform relative randomization gives I_d/d by
  averaging its d cyclic translates. BY CMP-TRACE and D1607.
  <2>2. Thus total finite success is

      W_D(beta,t)=sum_d pi_d w_d(t)
         =s(t-1)Z_D(beta,t)/L_D(beta),

  and its normalized common density is exactly rho_(D,t).
  BY <2>1 and the definitions in D1621.
  <2>3. Before relative randomization the CMP full/identity/dephased
  test retains probabilities 1,0,1/d. After randomization the state
  is stationary; its single Q_(d,1) probability is 1/d both with R
  and with I. No nonidentity test is inferred from a stationary input.
  BY CMP-BOUNDARY, <2>1 and Tr((I_d/d)Q_(d,1))=1/d.
  <2>4. QED <1>2.

<1>3. ASSUME the same finite mixture with all preparation outcomes.
PROVE its complete history normalization.
  <2>1. Write a_d(t)=c_d(t^s)/t^(sd), the primitive relative mass.
  Within degree d, primitive failure, averaging failure and success
  have probabilities 1-a_d, (1-1/d)a_d and a_d/d respectively.
  All are nonnegative and sum to one. BY CMP-BOUNDARY.
  <2>2. Multiplying by pi_d and summing over d preserves total one,
  with different degree/history targets kept as distinct tags.
  Randomization is a separate complete instrument, and its discard
  is explicitly specified. BY <1>1 and CMP-SOURCE/TRACE.
  <2>3. QED <1>3. The infinite density below is a limit of these
  finite common-observable outputs, not a claim about summing unlabelled
  physical states from Hilbert spaces of different field cardinalities.

## 2. A uniform coefficient bound over every degree

ASSUME integer d>=2 and t>1. PROVE v_d extends continuously to one
and obeys 0<v_d(t)<=1 uniformly in d.

<1>1. ASSUME x=t^s>=1. PROVE 0<c_d(x)<=x^d-1 when x>1.
  <2>1. FRL-POS gives c_e(x)>=0 for all e, with strict positivity
  at x>1, and FRL-ORBIT's divisor identity gives
  sum_(e|d)c_e(x)=x^d. The e=1 term is x>=1.
  BY those admitted polynomial identities.
  <2>2. Thus c_d(x)<=x^d-x<=x^d-1 for d>1. Strict positivity is
  the same FRL-POS assertion. QED <1>1.

<1>2. ASSUME m=sd is a positive integer. PROVE the bound on v_d.
  <2>1. Direct telescoping gives

      1-t^(-m)=(t-1)sum_(j=1)^m t^(-j)<=m(t-1).

  BY the finite geometric sum and t>1.
  <2>2. Substituting <1>1 into w_d yields
  0<w_d(t)<=(1-t^(-sd))/d<=s(t-1). Division gives 0<v_d(t)<=1.
  BY D1621 and <2>1.
  <2>3. QED <1>2.

<1>3. ASSUME fixed d. PROVE continuity of the extension v_d(1).
  <2>1. The numerator c_d(t^s) is a polynomial in t, vanishes at
  t=1, and has derivative s phi(d) there by CMP-BOUNDARY's period
  coefficient calculation. Divide it by t-1 as a polynomial.
  BY the divisor formula and s a positive integer.
  <2>2. The remaining denominator s d t^(sd) is positive near one,
  so the continuous value is phi(d)/d. QED <1>3.

<1>4. ASSUME 1<=t<=T with fixed T>1. PROVE a uniform lower bound
for every finite normalizer Z_D, D>=2, and for its infinite sum.
  <2>1. Since c_2(t^s)=t^(2s)-t^s,

      v_2(t)=[sum_(j=1)^s t^(-j)]/(2s)>=T^(-s)/2,

  including the continuous value at one. BY a geometric sum.
  <2>2. The d=2 term alone gives
  Z_D(beta,t)>=2^(-beta-1)T^(-s)>0; the same holds for Z_infty
  if it exists. QED <1>4 by <2>1 and positivity.

## 3. Uniform degree completion and trace-norm convergence

ASSUME beta>1 and the bounds of Section 2.
PROVE the finite assemblies approach the same quantum boundary in either
order, and along every path with D tending to infinity and t tending to one.

<1>1. ASSUME 1<=t<=T. PROVE uniform convergence of Z_infty.
  <2>1. Each summand g_d(t)=d^(-beta)v_d(t) is nonnegative and
  at most d^(-beta). For every integer D>=2 its tail is bounded by
  D^(1-beta)/(beta-1), by the integer-cutoff estimate of CMP-MELLIN.
  This bound is independent of t and tends to zero.
  BY Section 2 and CMP-MELLIN.
  <2>2. The finite head is continuous at t=1 by Section 2 <1>3.
  Choose a head with arbitrarily small tail at all t, then take its
  finite continuity limit. This proves continuity of the sum and
  convergence of g(t) to g(1) in the scalar l1 norm.
  BY <2>1, bounding each difference in the tail by 2d^(-beta).
  <2>3. At t=1 its value is sum_(d>=2)phi(d)/d^(beta+1)=Z_deg(beta).
  QED <1>1 by <2>1--<2>2 and D1612.

<1>2. ASSUME the infinite block density rho_(infty,t).
PROVE positivity, trace-one normalization and convergence to rho_beta.
  <2>1. The block probabilities are g_d(t)/Z_infty(beta,t). They
  are positive and sum to one. The corresponding scalar-block density
  has eigenvalue g_d(t)/(d Z_infty) with multiplicity d, so it is
  positive trace class. BY <1>1 and Section 2 <1>4.
  <2>2. The trace norm between two such densities equals the l1
  distance of their block probabilities: diagonalize each scalar block
  and sum the d equal absolute eigenvalue differences.
  BY their explicit diagonal matrices.
  <2>3. Since |Z(t)-Z(1)|<=||g(t)-g(1)||_1,
  the distance of normalized probabilities is at most
  2||g(t)-g(1)||_1/Z(t), which tends to zero by <1>1 and the positive
  lower bound. At t=1 the block formula is precisely rho_beta.
  QED <1>2 by <2>1--<2>3.

<1>3. ASSUME an integer D>=2. PROVE the uniform finite-cutoff estimate.
  <2>1. The finite density is the normalization of the first D blocks
  of the infinite one. Its l1 difference is exactly

      ||rho_(D,t)-rho_(infty,t)||_1
         =2[Z_infty(beta,t)-Z_D(beta,t)]/Z_infty(beta,t).

  The excess on the retained blocks equals the missing tail mass,
  so their two contributions are equal. BY direct finite normalization.
  <2>2. Apply <1>1's tail bound and Section 2 <1>4 to obtain

      ||rho_(D,t)-rho_(infty,t)||_1
        <=2^(beta+2)T^s D^(1-beta)/(beta-1).

  BY <2>1 and the positive normalizer bound.
  <2>3. The right side tends to zero independently of t in [1,T].
  Combining it with <1>2 proves convergence along any path D->infinity,
  t->1, as well as the two iterated limits. QED <1>3.

## 4. Event rates and quantum operational scope

ASSUME the finite protocols in Section 1 and their common outputs.
PROVE the retained event-rate and observable assertions.

<1>1. ASSUME fixed D>=2 and h=log(t). PROVE the first-grade success.
  <2>1. Since (t-1)/h->1, the finite success formula gives

      W_D(beta,t)/h -> s Z_D(beta,1)/L_D(beta)>0.

  BY Section 1 <1>2 and the derivative of exp(h) at zero.
  <2>2. Positive series convergence gives
  L_D(beta)->zeta(beta)-1 and Z_D(beta,1)->Z_deg(beta). Hence the
  first-grade rate tends to s Z_deg(beta)/(zeta(beta)-1).
  The same rate holds on joined paths by Section 3's uniform convergence.
  BY beta>1, D1612 and <2>1.
  <2>3. QED <1>1. The raw event at t=1 remains zero; its retained
  first-grade record is what is being completed.

<1>2. ASSUME a fixed bounded effect a in B_deg and an integer j.
PROVE convergence of its represented probabilities after Frobenius.
  <2>1. For self-adjoint trace-class delta and bounded a,
  |Tr(delta a)|<=||delta||_1||a|| by diagonalizing the positive and
  negative parts of delta and applying the operator norm bound.
  BY the positive spectral decomposition and the absolute trace sum.
  <2>2. Conjugation by U_deg^j preserves the trace norm; equivalently,
  its Heisenberg action preserves the norm of a. Thus the convergence
  of Section 3 persists for these probabilities.
  BY CMP-COMPLETE and <2>1.
  <2>3. The randomized reference is alpha-invariant throughout; its
  invariance is compatible with the nonidentity action detected by the
  separately available unrandomized finite preparations.
  QED <1>2 by the block-scalar density and CMP-BOUNDARY.

<1>3. ASSUME the complete scope of this construction.
PROVE the result concerns assembled arithmetic experiments without an
additional endpoint composition assumption.
  <2>1. Every finite D input is a finite tagged sum of actual field
  experiments, and every output comparison is on its inherited common
  matrix blocks. No operation between separate endpoint objects was
  used in proving convergence. BY Section 1 and CMP-REL/TRACE.
  <2>2. The norm-completed algebra and regulator are specified choices.
  The result proves one uniform realization of their positive state as
  an operational limit. It makes no assertion for arbitrary p-dependent
  physical observables, other regulators, or all mixed arithmetic maps.
  BY the explicit definitions of the common probes and degree prior.
  <2>3. QED CMP-JOINT-LIMIT by Sections 1--4. Tensor and sum operations
  may still be absent from the distinguished endpoint theory, even though
  finite sums before specialization produced this infinite quantum object.

Admission: ../../verdicts/composite-joined-adjudication.md.
