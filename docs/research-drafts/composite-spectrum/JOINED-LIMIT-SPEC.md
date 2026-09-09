# Third bounded claim: a uniform limit of finite assembled preparations

2026-09-09. UNREVIEWED new artifact, separate from the initial two
completion claims. It studies the order of degree completion and the
counting boundary, as required by the goal. It must receive its own
bounded independent verification/review; prior verdicts do not cover it.

Fix base absolute degree s>=1 and a real beta>1. For a finite degree cutoff
D>=2, use the actual finite classical tagged sum of experiments E_d/K,
|K|=p^s and [E_d:K]=d, for 2<=d<=D. Choose the initial classical degree
with probability d^(-beta)/L_D(beta), where L_D=sum_(d=2)^D d^(-beta).
This declared degree prior is extra preparation data. Each chosen degree
uses the CMP copied primitive preparation, followed by uniform relative
randomization and an explicit discard of the randomizer label. Its common
successful state is tr_d and its physical success is

    w_d(t)=c_d(t^s)/(d t^(sd)), t>1.

Every failure retains the actual degree and stopped arithmetic history.
Only successful COMMON observable responses are identified with the finite
matrix blocks; physical field multiplicity states at different p are not
identified.

For d>=2 define

    v_d(t)=w_d(t)/(s(t-1)), t>1,
    v_d(1)=phi(d)/d.

The key proposed uniform bound is 0<v_d(t)<=1 for every t>1 and d>=2.
Its proof should use c_d(x)<=x^d-1 and
1-t^(-sd)=(t-1)sum_(j=1)^(sd)t^(-j)<=sd(t-1).
Continuity at one follows from the known first coefficient, since
log(t)/(t-1)->1.

Set Z_D(beta,t)=sum_(d=2)^D d^(-beta)v_d(t), with the extension at t=1,
and let Z_infty be the infinite series. For the common Hilbert degree
sum define the finite successful conditional density to have d-block

    rho_(D,t),d = [d^(-beta)v_d(t)/(d Z_D(beta,t))] I_d,

zero outside 2..D. The total finite preparation success is
s(t-1)Z_D(beta,t)/L_D(beta). At t=1 it is zero, and its h=log t
coefficient should be s Z_D(beta,1)/L_D(beta).

Candidate assertions:

1. Z_infty converges uniformly for 1<=t<=T by domination with d^(-beta),
   and Z_infty(beta,1)=Z_deg(beta) from the completion proposal.
2. The density rho_(infty,t) is well defined, and rho_(infty,t) tends in
   ordinary trace norm to rho_beta as t decreases to one.
3. For every t in [1,T] and D>=2,

   ||rho_(D,t)-rho_(infty,t)||_1
        <= 2^(beta+2) T^s D^(1-beta)/(beta-1).

   Use v_2(t)=(sum_(j=1)^s t^(-j))/(2s)>=T^(-s)/2 for the normalizer.
   Consequently both iterated limits and every path D->infinity,t->1
   give the same rho_beta. The bound may exceed the trivial norm bound
   two; this does not make it an equality or a sharp estimate.
4. The total success has a nonzero first-order rate, tending with D to
   s Z_deg(beta)/(zeta(beta)-1). Full finite histories remain normalized.
5. Convergence remains true after the specified relative Frobenius and
   for every fixed bounded effect on the common completion. More general
   CP continuations require their own declared output representation;
   no arbitrary p-dependent physical map is included by this assertion.

Preregister exact tests at rational t=1, 6/5, 3/2, 2 and shrinking rational
steps above one, integer beta=2,3,4 and s=1,2. Derive c_d independently by
divisor subtraction; compute finite mixture weights and the exact trace
norm between normalized truncations as sums of scalar absolute values.
Compare the uniform cutoff bound without decimal fitting. Test the
degree prior, actual copied success, all three stopped/final comparisons,
and finite classical trace normalization. A finite tail-fragment test is
evidence only; the infinite bound and interchange require proof.

Mutations should remove the factor 1/d, reset copied preparation, omit
division by t-1, condition at t=1 before retaining a grade, use the wrong
normalizer/prior, lose a failure history, or replace the uniform bound by
an incorrect vanishing estimate. All red modes must hit mathematical gates.

The endpoint is an operational limit of finite assembled experiments with
an explicit degree prior, rather than an assertion that their tensor or
sum operations descend to total operations on Q_1. No unique prior,
all-arithmetic equivalence, or Riemann-zero spectrum is claimed.
