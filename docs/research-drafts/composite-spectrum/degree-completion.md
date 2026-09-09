# A completed arithmetic degree boundary and its positive trace

2026-09-09. Root prover. Proposed CMP-COMPLETE and CMP-MELLIN; UNREVIEWED.
Definitions D1611--D1612 are proposed beside this file. Inputs:
CMP-NATURAL, CMP-TRACE and CMP-REL at their admitted finite scopes.
All additional operator and series facts used below are derived explicitly.

## 1. Arithmetic divisor corners and the norm completion

ASSUME D1611. PROVE the finite corner system is the moving common algebra
of the relational arithmetic registers and its norm completion is A_deg.

<1>1. ASSUME N|M and a fixed actual base K=F_q.
PROVE that every period-d orbit for d|N upstairs lies in F_(q^N).
  <2>1. Every label in such an orbit is fixed by sigma^N. Inside
  F_(q^M), the fixed labels are exactly the q^N roots of X^(q^N)-X,
  namely the embedded smaller field. BY FRL-ORBIT's fixed-field proof.
  <2>2. Conversely an embedded label has the same period by
  CMP-NATURAL. The whole period-d orbit multiplicity upstairs is
  therefore exactly the image of the smaller one.
  BY <2>1 and CMP-NATURAL.
  <2>3. J^rel a (J^rel)^* on the larger code acts as a on those
  period blocks and zero elsewhere. On common observables this is
  precisely j_(N,M), without orbit-origin choices.
  QED <1>1 by <2>1--<2>2 and CMP-REL.

<1>2. ASSUME the moving copied-reference first grade.
PROVE the compatibility of the finite unnormalized traces theta_N.
  <2>1. CMP-TRACE gives coefficient s phi(d)/d on the moving d-block
  over K=F_(p^s). Dividing by the fixed positive base degree s gives
  exactly theta_N. BY CMP-TRACE with N>1.
  <2>2. Extending a by zero changes no nonzero term of theta. Hence
  theta_M(j_(N,M)(a))=theta_N(a). Normalized references instead
  restrict with success theta_N(1)/theta_M(1), and conditioning gives
  theta_N/theta_N(1). BY finite sums and positivity of eta_d.
  <2>3. QED <1>2. The trace used here is the derived first-grade
  reference, not the original Hilbert multiplicity trace.

<1>3. ASSUME the directed set of integers >=2 under divisibility.
PROVE its algebraic union consists of all finitely supported matrix blocks.
  <2>1. Any two indices have the common multiple lcm(N,M), and
  j_(M,L)j_(N,M)=j_(N,L) by coordinate inclusion. Each j is an
  isometric injective star homomorphism and a corner inclusion.
  BY D1611 and the maximum norm on finite blocks.
  <2>2. Every finite subset of degrees is contained among the divisors
  of its least common multiple. Missing blocks can be set to zero.
  Thus the union is exactly the algebraic direct sum over all d>=2.
  BY integer divisibility and <2>1.
  <2>3. Its uniform closure consists exactly of sequences with block
  norms tending to zero: finite truncations approximate every such
  sequence, and a uniform limit of finitely supported sequences has
  uniformly small tails. QED <1>3 by <2>2 and the norm definition.

<1>4. ASSUME the concrete A_deg and B_deg.
PROVE they are C*-algebras with the stated unitization.
  <2>1. Multiplication and adjoint act blockwise; vanishing tails are
  preserved by them. The supremum norm is complete, by completeness
  of each finite block and the uniform Cauchy criterion. It satisfies
  ||a^*a||=sup_d ||a_d||^2=||a||^2. BY finite matrix norm identities.
  <2>2. If lambda I+a=0 with a in A_deg, then a_d=-lambda I_d
  cannot have vanishing norm unless lambda=0. Also
  ||lambda I+a||>=|lambda| by taking the block-norm limit at infinity.
  This bound shows that a Cauchy sequence in B_deg has Cauchy scalar
  parts and Cauchy A_deg parts; hence B_deg is closed and complete.
  BY D1611 and <2>1.
  <2>3. Positivity at any finite matrix level is blockwise positivity
  in the concrete Hilbert representation; for B_deg it also forces
  positivity of the scalar matrix at infinity. Positive cones are
  closed under norm limits because their quadratic forms are.
  QED <1>4 by <2>1--<2>2 and the concrete operator representation.

## 2. Frobenius extends and is outer in this unitization

ASSUME D1612. PROVE the positive quantum dynamics and its precise scope.

<1>1. ASSUME the finite cycle matrices S_d.
PROVE U_deg is unitary and alpha is a unital CP automorphism of B_deg.
  <2>1. On H_deg, each S_d preserves its summand norm. The direct
  sum preserves the square-sum norm and has inverse direct-sum S_d^*.
  Thus U_deg is unitary. BY the Hilbert sum definition.
  <2>2. Conjugation preserves every block norm, hence vanishing tails,
  and fixes the scalar unit. It preserves products and adjoints and
  its inverse is conjugation by U_deg^*. At every matrix level the
  action is conjugation by I_m tensor U_deg, hence is positive.
  BY <2>1 and matrix multiplication.
  <2>3. It restricts to the actual finite relative action and
  commutes with the corner inclusions. QED <1>1 by CMP-REL and <2>2.

<1>2. ASSUME for contradiction a unitary w in B_deg with alpha=Ad(w).
PROVE that this is impossible.
  <2>1. Write w=lambda I+a with ||a_d||->0. Since each w_d is
  unitary, its scalar tail has |lambda|=1, by passing to the norm
  limit of w_d^*w_d=I_d. BY D1611 and finite norm continuity.
  <2>2. For the rank-one block projection e_d=|0><0|,

      ||w_d e_d w_d^*-e_d|| <= 2||w_d-lambda I_d|| -> 0.

  Expand the difference as (w_d-lambda I)e_d w_d^*
  +lambda e_d(w_d^*-conjugate(lambda)I) and use the triangle inequality.
  BY <2>1 and ||e_d||=||w_d||=1.
  <2>3. But S_d e_d S_d^*=|1><1|, and its difference from e_d
  has norm one for every d>=2. This contradicts <2>2.
  QED <1>2. The automorphism is outer ON B_deg; it is still spatially
  implemented on H_deg and inner in the larger product multiplier algebra.

<1>3. ASSUME the named Hilbert implementation U_deg.
PROVE its point spectrum and full spectrum.
  <2>1. Every block diagonalizes in the finite Fourier basis from
  CMP-TRACE. Thus those finite eigenvectors form an orthonormal basis
  of H_deg. Its eigenvalues are exactly roots of unity. A root of order
  m occurs in every block whose degree is a positive multiple of m
  (with degree >=2), hence has infinite multiplicity.
  BY CMP-TRACE and the Hilbert direct sum.
  <2>2. Roots of unity are dense on the unit circle: approximate any
  angle by rational multiples of 2pi. Their corresponding unit vectors
  show failure of a bounded inverse for U_deg-lambda I at every point
  of that circle, by the approximate-eigenvector inequality.
  BY <2>1 and rational approximation of a real number by integer rounding.
  <2>3. Off the circle, the inverses of S_d-lambda I have norms at
  most 1/abs(|lambda|-1), using their orthonormal eigenbases. Their
  direct sum is a bounded inverse. QED <1>3.
  This is a discrete Frobenius action and a cycle spectrum; no continuous
  time scaling or Riemann-zero identification is asserted.

<1>4. ASSUME theta on A_deg,+.
PROVE it is a faithful lower-semicontinuous semifinite trace.
  <2>1. All eta_d>0. Thus a positive a has theta(a)=0 only if each
  positive block has zero ordinary trace, hence each block is zero.
  Additivity and homogeneity follow from sums of nonnegative numbers.
  BY the finite matrix spectral theorem and D1611.
  <2>2. For x in A_deg, theta(x^*x)=theta(xx^*) termwise, allowing
  infinity. The functional is the supremum of its continuous finite
  positive block sums, so it is lower semicontinuous on positive inputs.
  BY finite trace cyclicity and the definition of a nonnegative series.
  <2>3. Finite central block cutoffs e_F give 0<=e_F a e_F<=a,
  finite trace, and norm convergence to a as the finite support grows.
  Their traces increase to theta(a). This proves semifiniteness and
  density of the finite-trace positive domain on A_deg.
  BY the vanishing-tail condition and <2>2.
  <2>4. The extended mass of the multiplier identity is infinite:
  eta_d=phi(d)/d>=1/d and the harmonic series diverges. The trace is
  asserted densely defined on A_deg, not on its unitalization B_deg.
  QED CMP-COMPLETE by Sections 1--2.

## 3. Positive degree regularization and a zeta quotient

ASSUME a real beta>1. PROVE CMP-MELLIN's normalization and moments.

<1>1. ASSUME Z_deg(beta) of D1612.
PROVE it is finite, strictly positive, with the stated tail bound.
  <2>1. Since 1<=phi(d)<=d, its terms are positive and at most
  d^(-beta). Their tail after D is bounded by
  integral_D^infinity x^(-beta) dx=D^(1-beta)/(beta-1).
  BY monotonicity of x^(-beta) and elementary integration.
  <2>2. The d=2 term is positive. Thus 0<Z_deg(beta)<infinity.
  QED <1>1 by <2>1.

<1>2. ASSUME rho_beta and omega_beta as defined.
PROVE an alpha-invariant faithful state on B_deg.
  <2>1. Each eigenvalue of rho_beta is positive, and summing its d
  eigenvalues on each block gives total ordinary trace
  (1/Z_deg(beta))sum_(d>=2)phi(d)/d^(beta+1)=1.
  Thus rho_beta is a positive trace-class operator.
  BY <1>1 and the explicitly diagonal Hilbert basis.
  <2>2. For bounded positive a, the nonnegative diagonal sum defining
  Tr(rho_beta a) converges and is at most ||a||. If it is zero, every
  diagonal quadratic form of a is zero because every rho eigenvalue
  is positive. Positivity implies a is zero: for basis vectors u,v,
  |<u,av>|^2<=<u,au><v,av>, obtained from positivity on their two-plane.
  BY the positive two-by-two determinant inequality.
  <2>3. Therefore omega_beta is faithful and omega_beta(I)=1.
  Its matrix amplifications are positive: for a positive matrix [a_ij]
  and scalar vector z, omega_beta(sum bar(z_i)a_ij z_j)>=0.
  BY <2>2 and compression of a positive matrix.
  <2>4. rho_beta is scalar on each cycle block, so it commutes with
  U_deg. Block trace cyclicity and absolutely convergent sums prove
  omega_beta(alpha(a))=omega_beta(a).
  QED <1>2 by <2>1--<2>4.

<1>3. ASSUME zeta(x)=sum_(m>=1)m^(-x), x>1.
PROVE Z_deg(beta)=zeta(beta)/zeta(beta+1)-1.
  <2>1. The identity sum_(d|k)phi(d)=k follows by partitioning
  {1,...,k} according to gcd(a,k): the class with k/gcd(a,k)=d
  contains exactly phi(d) integers. BY the definition of phi as the
  count of residues coprime to d, including phi(1)=1.
  <2>2. Both positive series converge for beta>1, and grouping their
  absolutely convergent product by k=dm gives

      [sum_(d>=1)phi(d)/d^(beta+1)] zeta(beta+1)
        =sum_(k>=1) [sum_(d|k)phi(d)]/k^(beta+1)
        =zeta(beta).

  BY <2>1 and the convergence bound in <1>1.
  <2>3. Divide by the positive number zeta(beta+1), then remove the
  d=1 term, which equals one. QED <1>3.

<1>4. ASSUME an integer j. PROVE the regulated implementer moments.
  <2>1. On a d-cycle, Tr(S_d^j)=d when d divides j and zero
  otherwise, by CMP-TRACE. When j!=0 only finitely many d divide |j|.
  Thus the ordinary trace-class pairing gives

      M_beta(j)=[sum_(d|abs(j),d>=2)phi(d)/d^(beta+1)]/Z_deg(beta).

  For j=0 it gives one by <1>2, not a finite-divisor sum.
  BY D1612 and the convergent diagonal trace.
  <2>2. U_deg need not be in B_deg; this pairing uses the specified
  Hilbert implementation and its trace-class density. Also theta cannot
  be applied as an integrable trace to unregularized U_deg^j, since
  |U_deg^j|=I has infinite theta-mass.
  BY Section 2 <1>4 and unitary absolute value.
  <2>3. D_beta is central degree weighting. If its logarithmic degree
  operator is introduced, conjugation by that central scalar-block flow
  fixes A_deg. It is not the relative Frobenius dynamics alpha.
  QED CMP-MELLIN by Section 3 <1>1--<1>4.

This constructs one specified completion and one positive reference family
from the arithmetic degree coefficients. The zeta quotient is established
only in its convergent real domain beta>1; neither its analytic continuation
nor a realization of its zeros as the spectrum of U_deg has been asserted.
Independent quantum tensor of primitive cycles still has the gcd/lcm
reblocking of FRL-COMP; it is not identified with a single cycle of product
degree. The completion supplies quantum systems and Frobenius dynamics
without imposing that missing endpoint composition rule.
