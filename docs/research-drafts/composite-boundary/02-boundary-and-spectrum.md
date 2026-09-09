# A positive conditional quantum boundary and finite spectral identities

2026-09-09. Root prover. Proposed CMP-BOUNDARY, CMP-FOURIER, CMP-TRACE.
UNREVIEWED. Definitions D1602--D1607; companion construction supplies
CMP-SOURCE/REL/NATURAL. Existing inputs POS-STATE/DIAGRAM/FINITE,
FRL-ORBIT/POS, FRB-TRACE/FROB, and D1306. No infinite trace is assumed.

## 1. Weighted relative periods and the rare preparation

ASSUME E/K as in D1602, n>1, and the D1501 reference rho_E(h).
PROVE the exact and finite-profile success formulas for D1604.

<1>1. ASSUME d|n. PROVE that the unnormalized D_E reference mass of
labels fixed by sigma^d is t^(sd), t=exp(h).
  <2>1. The fixed field is the subfield of E with p^(sd) elements.
  This follows from the roots of X^(p^(sd))-X as in FRL-ORBIT and
  FRB-TRACE. BY those claims with sd dividing r=sn.
  <2>2. POS-DIAGRAM restricts D_E exactly to the reference on that
  subfield. Its trace is t^(sd). BY POS-DIAGRAM and POS-STATE.
  <2>3. QED <1>1.

<1>2. ASSUME m_d(h) is the D_E mass of labels of exact sigma-period d.
PROVE m_d(h)=c_d(t^s).
  <2>1. The disjoint period partition gives t^(sa)=sum_(d|a)m_d(h)
  for every a|n. Mobius inversion of this finite divisor sum gives
  m_d(h)=sum_(a|d)mu(d/a)t^(sa)=c_d(t^s).
  BY <1>1 and the divisor inversion proved in FRL-ORBIT.
  <2>2. For n>1 this mass vanishes at h=0 and has derivative
  s sum_(a|n)mu(n/a)a=s phi(n)>0. Higher exponential-series
  coefficients are positive by FRL-POS/POS-STATE.
  BY the Jordan coefficient formula in POS-STATE, with scale s.
  <2>3. QED <1>2.

<1>3. ASSUME a sigma-orbit O of length n. PROVE its successful density
contribution and the full preparation probability.
  <2>1. D_E is diagonal and constant on O, since each sigma step is
  a power of absolute Frobenius and preserves absolute period. Denote
  the common diagonal value a_O(h). For input rho_E, the contribution
  of x in O after K_ok is t^(-r)a_O(h)|v_(O,0)><v_(O,0)|/n.
  BY D1501 and the companion Section 3 <1>2.
  <2>2. Summing x in O gives t^(-r)a_O(h)|v_(O,0)><v_(O,0)|.
  Summing O gives trace t^(-r)m_n(h)/n. Thus

      w_(s,n)(h)=c_n(t^s)/(n t^r).

  BY <2>1 and <1>2. This derivation uses the diagonal reference;
  it does not replace K_ok^*K_ok by a scalar on arbitrary inputs.
  <2>3. For h>0, m_n(h)>0, so the conditional state is defined. Its
  evaluation on any common a in M_n is <0|a|0>, independent of its
  physical orbit mixture. The leading event order is one with
  coefficient s phi(n)/n. BY <2>1--<2>2 and <1>2.
  <2>4. QED <1>3, uniformly including p dividing n.

<1>4. ASSUME instead the finite profile lambda_E=L_E/(1+rh).
PROVE its success probability and agreement of boundary records.
  <2>1. Pi_n kills the zero coefficient P0, since n>1. By the
  derivative in <1>2, its B_E mass is s phi(n). The same orbit
  calculation as <1>3 gives success

      h s phi(n)/(n(1+rh)).

  BY D1503 and <1>3.
  <2>2. The common conditional state is still |0><0|. The event
  has the same order and coefficient as the exact preparation.
  Fixed further CP continuations preserve the full leading physical
  matrix by POS-FINITE, using ONE reference and two fixed ancillas.
  BY <2>1, POS-FINITE and the D1604 input convention.
  <2>3. QED <1>4. Resetting the correlated output to independent
  field references would be a different preparation.

## 2. One test detects Frobenius and collective coherence

ASSUME successful D1604 preparation and final effect Q_(n,1).
PROVE the conditional probabilities 1,0,1/n.

<1>1. ASSUME the full relative Frobenius R. PROVE probability one.
  <2>1. Each vector v_(O,0) becomes v_(O,1). The final projector
  fixes every such vector. BY CMP-REL and D1604.
  <2>2. The same holds for their positive normalized mixture.
  QED <1>1 by <2>1 and linearity of the Born probability.

<1>2. ASSUME R is replaced by identity. PROVE probability zero.
  <2>1. Since n>1, v_(O,0) is orthogonal to every v_(O',1).
  The effect annihilates each prepared vector. BY CMP-REL's basis.
  <2>2. QED <1>2 by positivity and linearity.

<1>3. ASSUME computational dephasing immediately before R.
PROVE probability 1/n.
  <2>1. Dephasing |v_(O,0)><v_(O,0)| gives the uniform mixture of
  its n computational tuples. R maps each to one tuple in the graph
  of (O,1). BY D1602--D1604 and CMP-REL.
  <2>2. The squared overlap of any such tuple with v_(O,1) is 1/n;
  its overlap with every other final orbit vector is zero.
  Averaging n equal contributions still gives 1/n.
  BY the normalized orbit sum and the Born rule.
  <2>3. The result is independent of O, hence remains 1/n for the
  physical orbit mixture. QED <1>3.

<1>4. ASSUME the full retained protocol. PROVE completeness and its
unconditioned probabilities, including the vanishing boundary.
  <2>1. Section 1 and the companion completeness proof give primitive
  cut failure 1-m_n(h)/t^r, averaging failure
  (1-1/n)m_n(h)/t^r, and averaging success w_(s,n)(h).
  BY their squared amplitudes on the diagonal reference.
  <2>2. On the last branch, the final success/failure probabilities
  are 1/0, 0/1, or 1/n and 1-1/n for the three circuits respectively.
  All nonnegative branch probabilities sum to one, with different stopped
  histories kept at their stated targets. BY <1>1--<1>3 and <2>1.
  <2>3. At h=0 the primitive success branch is zero. Its first-order
  retained data nevertheless give the common M_n state and the CP
  automorphism Ad(S_n), with full-circuit coefficient s phi(n)/n and
  dephased coefficient s phi(n)/n^2. The identity circuit has zero
  final branch at every h. BY Section 1 and <1>1--<1>3.
  <2>4. The noncommutative algebra and channel arise from actual
  arithmetic generators by CMP-REL. Neither zero ancillas alone nor
  classical outcome tags provide its relative matrix units.
  QED CMP-BOUNDARY by Sections 1--2 and CMP-REL.

The result compares a selected family of quantum probes across p. It
does not identify the entire three-register Hilbert spaces or all their
CP operations. It also does not infer new total tensor/sum operations on
the selected boundary from the prelimit word that produced it.

## 3. The actual first-register Fourier return

ASSUME D1606's primitive code and negative-kernel field Fourier.
PROVE CMP-FOURIER's compression, phase and retained success.

<1>1. ASSUME two graph labels from the primitive sector. PROVE a nonzero
matrix element of F_first between them requires the same triple.
  <2>1. F_first leaves y,z unchanged. Every primitive x has nonzero
y=sigma^k x. In E the equation z=xy therefore determines x=z/y.
  Hence a second graph tuple with the same y,z has the same x.
  Its orbit O and relative index k then also agree.
  BY the field inverse law, n>1 and exact period.
  <2>2. Only the diagonal first-register Fourier coefficient remains:
  |E|^(-1/2)psi_E(-x*x). BY D1306.
  <2>3. QED <1>1.

<1>2. ASSUME an orbit sum v_(O,k). PROVE its compressed Fourier action.
  <2>1. Absolute trace is invariant under x->x^q, so
  psi_E(-sigma(x)^2)=psi_E(-x^2). The phase is constant on O.
  BY FRB-FROB and D1301.
  <2>2. Taking the normalized sum of the n diagonal coefficients
  in <1>1 gives |E|^(-1/2)psi_E(-x^2) times v_(O,k).
  All off-diagonal graph-vector entries vanish by <1>1.
  BY <2>1 and orthonormality of the graph basis.
  <2>3. Thus the compressed amplitude is |E|^(-1/2)D_phase with
  D_phase unitary and scalar on each orbit multiplicity. Its squared
  amplitude is I/|E| on the primitive code. QED <1>2.

<1>3. ASSUME the two retained outcomes in D1606. PROVE their CP and
probability statements and scope on the common algebra.
  <2>1. The amplitudes P_n F_first and (I-P_n)F_first restricted
  to the code have squared-amplitude sum I, by unitarity and projection
  completeness. BY D1606 and <1>2.
  <2>2. Return has probability 1/|E| for every input code state,
  including coherences between orbit multiplicities; failure has
  probability 1-1/|E| and retains the ambient word.
  BY <1>2.<2>3 and <2>1.
  <2>3. D_phase commutes with the common M_n representation, so the
  conditional return leaves its state unchanged. The actual multiplicity
  phase and unconditioned probability still retain arithmetic data.
  QED CMP-FOURIER by <1>1--<1>3. This is one declared Fourier return,
  not invariance of the full endpoint theory under all field Fourier maps.

## 4. Finite Frobenius spectrum and the copied-reference trace

ASSUME the full all-period code of D1602--D1603.
PROVE CMP-TRACE with actual multiplicities and separate channel spectra.

<1>1. ASSUME an integer j, with gcd(n,0)=n. PROVE the trace formula.
  <2>1. On a d-cycle S_d, the trace of its j-th power is d if d|j
  and zero otherwise, by its permutation diagonal. There are c_d(q)/d
  copies. Thus Tr(R^j)=sum_(d|n,d|j)c_d(q)=q^gcd(n,j).
  BY CMP-REL and the fixed-period count in FRL-ORBIT.
  <2>2. QED <1>1. In particular the code dimension is q^n=|E|.

<1>2. ASSUME one cycle S_d. PROVE its determinant and spectrum.
  <2>1. For every d-th root lambda, the vector sum_k lambda^(-k)|k>
  is an eigenvector with eigenvalue lambda. These vectors are linearly
  independent: distinct eigenvalues have independent eigenvectors,
  as follows by applying products of (S_d-lambda I).
  BY direct shift substitution and characteristic zero of C.
  <2>2. Consequently det(I-zS_d)=product_(lambda^d=1)(1-zlambda)
  =1-z^d. Taking the repeated block product gives

      det(I-zR)=product_(d|n)(1-z^d)^(c_d(q)/d).

  BY <2>1 and the polynomial factorization of X^d-1.
  <2>3. Expanding -log(1-zlambda) as its power series for |z|<1
  gives det(I-zR)^(-1)=exp(sum_(j>=1)Tr(R^j)z^j/j).
  All eigenvalue sums are finite. QED <1>2 by <2>1--<2>3.

<1>3. ASSUME the channel on B(ran P). PROVE the spectral distinction.
  <2>1. If R f_a=lambda_a f_a in an orthonormal eigenbasis, its
  channel sends |f_a><f_b| to lambda_a conjugate(lambda_b)|f_a><f_b|.
  Thus its linear-map trace at power j is |Tr(R^j)|^2=q^(2gcd(n,j)).
  BY direct conjugation and <1>1.
  <2>2. On one common M_d block, its eigenvalue ratios are d-th
  roots each with multiplicity d; this differs from the implementer's
  d eigenvalues each occurring once. QED <1>3 by <2>1 and <1>2.

<1>4. ASSUME the randomized preparation of D1607. PROVE its reference
weights and conditional moving-sector boundary.
  <2>1. The unrandomized copied reference has successful orbit
  contribution t^(-r)a_O(h)|v_(O,0)><v_(O,0)|, by Section 1's
  argument at each period d, including d=1.
  BY the same orbit-average calculation with d in place of n.
  <2>2. Uniform randomization over R^j, 0<=j<n, gives I_d/d in
  each relative block, since each residue modulo d occurs n/d times.
  Its expectation on common observables is therefore

      t^(-r) sum_(d|n) [c_d(t^s)/d] tr_d(a_d).

  BY <2>1, Section 1 <1>2 and D1607's explicit discarded random label.
  <2>3. On d>1, first-order unnormalized weights are s phi(d)/d.
  Conditioning their sum yields the faithful tracial boundary with
  weights (phi(d)/d)/sum_(e|n,e>1)phi(e)/e. Every denominator is
  positive by FRL-POS. BY <2>2 and the positive series derivatives.
  <2>4. The raw ordinary reference endpoint retains only d=1, while
  the conditional first grade retains the stated noncommutative blocks.
  QED CMP-TRACE by <1>1--<1>4. The spectral counting trace in <1>1
  and the normalized reference in <1>4 are explicitly different.
