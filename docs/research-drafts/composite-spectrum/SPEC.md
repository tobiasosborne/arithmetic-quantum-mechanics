# Proposed degree completion of the relative quantum boundary

2026-09-09. Second bounded artifact under the active goal. UNREVIEWED.
Inputs are the admitted CMP finite graph construction and its repaired
moving-sector weights. This continues the degree-completion/trace stage;
it does not revisit the finite witness or impose endpoint tensor closure.

## Candidate finite comparison system

For each N>=2 let A_N=direct-sum_(d|N,d>1) M_d(C), with relative
Frobenius u_N=direct-sum S_d. For N|M let j_(N,M) include those blocks
and set the other blocks to zero. These are nonunital corner inclusions.
At fixed actual base K=F_q, the proposed arithmetic comparison is the
CMP-NATURAL encoder F_(q^N)->F_(q^M). Every orbit of length d|N in
the larger field already lies in the smaller field, so its whole
length-d relational code is the encoder image. Verify this point.

The copied-reference moving first coefficient, divided by base degree s,
is the positive trace theta_N(a)=sum_(d|N,d>1) [phi(d)/d] tr_d(a_d).
These UNNORMALIZED traces should restrict exactly along j_(N,M).
Normalized references instead condition with probability theta_N(1)/theta_M(1).

## Candidate C*-completion and dynamics

The norm completion of this directed system is

    A = c0-direct-sum_(d>=2) M_d(C),
    B = its minimal unitization,
    H = Hilbert-direct-sum_(d>=2) C^d,
    U = direct-sum_(d>=2) S_d on H.

The actual finite cycle comparisons define alpha(a)_d=S_d a_d S_d^*.
It should extend to a unital CP automorphism of B, with U as an external
implementing unitary. U is not assumed to belong to B.

Candidate stronger structural property: alpha is OUTER on B. If a unitary
w in B implemented it, its blocks would tend in norm to a scalar lambda I.
Then Ad(w_d) would approach identity uniformly on each block's unit ball.
But Ad(S_d) moves the rank-one relative test Q_(d,0) to the orthogonal
Q_(d,1), whose difference has norm one for every d>=2. This should
contradict an inner implementation. A full proof must justify the scalar
tail condition from unitization; a finite test alone cannot prove outerness.

U should have point spectrum all roots of unity, with infinite multiplicity
for each root, and spectrum their closure, the unit circle. This is the
arithmetic relative-cycle completion's spectrum, not a Riemann-zero spectrum.
The CP action and the implementing operator are to remain separately typed.

## Candidate positive trace regularization

Let a_d=phi(d)/d. On A_+ define theta(a)=sum_(d>=2) a_d tr_d(a_dblock),
using a different symbol for block entries in the final notation. This
is a proposed faithful lower-semicontinuous semifinite trace, compatible
with the finite theta_N. It has infinite mass on the multiplier identity.
It is not legitimate to assign an ordinary theta-trace to U^j just because
some diagonal cancellation makes a formal sum finite.

For a real beta>1, let D_beta have central block d^(-beta) I_d and set

    Z(beta)=sum_(d>=2) phi(d)/d^(beta+1),
    rho_beta|C^d = phi(d)/(Z(beta) d^(beta+2)) I_d.

The ordinary trace of rho_beta should be one; its state on B should be
faithful, positive at every matrix level, and alpha-invariant. D_beta is
a specified degree regularization, not a new arithmetic gate and not
the Frobenius generator. If H_deg=log(d) on the d-th block is used, it
is a central degree-weight operator and its induced dynamics on A is
trivial; it must not be confused with alpha.

Define zeta(x)=sum_(m>=1)m^(-x) for real x>1. The proposed exact identity is

    Z(beta) = zeta(beta)/zeta(beta+1) - 1,  beta>1.

It follows prospectively from the coefficient identity
sum_(d|k)phi(d)=k and absolute/positive series multiplication. The d=1
subtraction is essential because the moving boundary omits the scalar block.
For integer j!=0, the regulated implementer moment is proposed to be

    Tr(rho_beta U^j)
       = [sum_(d|abs(j),d>=2) phi(d)/d^(beta+1)]/Z(beta),

while the j=0 value is one. The same common density does not turn this
implementer trace into a trace of the conjugation channel.

## What to test independently before proof admission

1. Finite divisor-corner inclusions and their compositions; finite trace
   restrictions with the actual coefficient phi(d)/d. Include N=2,3,4,6,12
   and the fixed-base F4->F16 arithmetic graph comparison where useful.
2. The uniform nontrivial action on rank-one tests in several sizes, plus
   its persistence after finite direct-sum extension. Finite checks do
   not certify the infinite outerness proof.
3. Exact positive density normalization for finite cutoffs at integer
   beta=2,3,4. Retain the exact tail bound
   sum_(d>D) phi(d)/d^(beta+1) <= D^(1-beta)/(beta-1).
4. Dirichlet convolution coefficients through a declared finite bound,
   derived from independently counted coprime integers. Test the d=1
   term separately; do not validate a zeta quotient by fitting decimal values.
5. Explicit cycle traces versus the divisor formula for regulated finite
   moments, keeping j=0 separate and including negative j.
6. Track the distinction between tensoring two 2-cycles (two 2-cycles)
   and one 4-cycle. This is an existing cycle-composition comparison,
   not a requirement that the selected endpoint family be tensor closed.

Preregister mutations dropping 1/d, losing d=1 subtraction, resetting a
corner normalization, replacing Frobenius by identity, confusing j=0 with
the finite-divisor formula, and replacing implementer by channel traces.
All must fail at real mathematical gates. General norm completion,
positivity, outerness and infinite-series identities require proofs.

## Intended scope

This constructs one explicit completion of arithmetic-derived quantum
remnants and one explicit positive degree regularization. The finite
arithmetic corner maps and coefficient weights must justify its provenance.
No universal choice of completion, all-operation arithmetic functor,
analytic continuation of a partition function, zero-spectrum realization,
or full MIX-ALL assertion is included.
