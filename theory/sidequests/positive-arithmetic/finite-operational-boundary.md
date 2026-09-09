# Positive process series and finite sufficient operational profiles

Native inherited Codex prover runtime; no model override or nested CLI.
Status: POS-PROCESS and POS-FINITE are PROVED within their stated hypotheses.
Definitions: ../../../definitions.md, D1501--D1506. Dependencies:
POS-STATE, FRP-CAT and FRP-CP. The positive coefficient constructions,
annihilation lemma and finite adequacy theorem below are internal matrix
derivations. No limit of changing Hilbert dimensions is asserted.

Admission: ../../verdicts/positive-arithmetic-adjudication.md.

## 1. A precise category with positive CP coefficients

**ASSUME** D1504's positive-series process representatives.
**PROVE** evaluation, composition, tensor and equality are well defined,
forming a symmetric monoidal category of ordinary-trace CP processes.

<1>1. **ASSUME** a representative (Phi,Z):X->Y.
**PROVE** its series converges in finite-dimensional operator norm on
every compact h interval, with CP trace-nonincreasing evaluation Phi(h)/Z(h).
  <2>1. In one input block of dimension d, form the positive block matrix
  `C_k=sum_(i,j) E_ij tensor Phi_k(E_ij)` by applying `id tensor Phi_k`
  to the positive matrix `|sum_i i,i><sum_i i,i|`.
  Its trace is `sum_i Tr Phi_k(E_ii)<=d z_k`; hence its norm and each
  of its matrix entries are bounded by d z_k.
  Sum this bound over the finitely many input/output tag blocks.
  **BY** complete positivity, D1504's trace inequality and the
  nonnegative eigenvalues of a finite positive matrix.
  <2>2. Since `sum_k z_k H^k=Z(H)<infinity` for each H>=0,
  <2>1 bounds every matrix entry's series uniformly on |h|<=H.
  Finite-dimensional norm convergence follows. At real h>=0 each
  finite partial sum is CP; its amplified positive quadratic forms
  have positive limits. Thus Phi(h) is CP at every finite amplification.
  **BY** <2>1 and convergent nonnegative scalar majorants.
  <2>3. Sum the coefficient trace inequalities to get
  `Tr Phi(h)(a)<=Z(h)Tr a` for a>=0. Since Z(h)>=z_0>0,
  division is defined and gives a CP trace-nonincreasing map, continuously
  at zero as well. For normalized representatives equality holds.
  **QED** <1>1 by <2>1--<2>3.

<1>2. **ASSUME** representatives (Phi,Z):X->Y and (Psi,W):Y->V.
**PROVE** their Cauchy composite and tensor representatives satisfy D1504.
  <2>1. The k-th composite coefficient is
  `sum_(i+j=k) Psi_i Phi_j`, a finite sum of CP maps. On a>=0 its
  trace is at most `sum_(i+j=k) w_i z_j Tr a`, the k-th coefficient
  of WZ times Tr a. If both representatives are normalized, equality holds.
  **BY** D1504 and substitution of its inequalities into positive outputs.
  <2>2. Each tensor coefficient is a finite sum of tensor products
  of CP maps. Its trace bound also follows coefficientwise: if
  `Phi_i^*(I)<=z_i I` and `Psi_j^*(I)<=w_j I`, then
  `Phi_i^*(I) tensor Psi_j^*(I)<=z_i w_j I`.
  To verify the inequality, write the difference as
  `(z_i I−Phi_i^*I) tensor w_j I
   +Phi_i^*I tensor (w_j I−Psi_j^*I)`, a sum of positives.
  **BY** trace duality and tensor-product positive quadratic forms.
  <2>3. Scalar products WZ remain positive-coefficient normalizers,
  finite on every h>=0 and with positive constant term. Associativity
  is the equality of each finite triple Cauchy sum; evaluation commutes
  with composition and tensor by absolute convergence from <1>1.
  **QED** <1>2 by <2>1--<2>3.

<1>3. **ASSUME** the cross-multiplied equality of D1504.
**PROVE** it is an equivalence relation respected by every category operation.
  <2>1. Reflexivity and symmetry are immediate. For transitivity,
  `Z'Phi=Z Phi'` and `Z''Phi'=Z'Phi''` imply
  `Z'(Z''Phi−Z Phi'')=0`. A scalar series with nonzero constant term
  can be cancelled coefficientwise: the first possible nonzero coefficient
  of its product would be that coefficient times z'_0, a contradiction.
  Hence `Z''Phi=Z Phi''`.
  **BY** D1504 and finite coefficient multiplication.
  <2>2. Multiplying the cross identities by other scalar normalizers
  and composing/tensoring their linear-map coefficients proves congruence.
  Scalar normalizers commute with all maps; tags remain unchanged.
  Normalization also descends: take traces of the cross identity and
  cancel the nonzero scalar normalizer to recover its coefficient equalities.
  **BY** <2>1 and distributivity of composition/tensor over finite sums.
  <2>3. Identity (id,1), canonical block/word swaps, associators and
  unitors are constant actual CP maps. Their usual matrix equations
  remain true coefficientwise. Thus they satisfy the symmetric monoidal
  identities after the quotient as well.
  **QED** section 1 by <2>1--<2>3 and <1>1--<1>2.

## 2. Exact and finite preparations inside that category

**ASSUME** POS-STATE and the admitted actual arithmetic amplitudes/processes.
**PROVE** all their coherent source relations survive, while rho_E and
lambda_E are additional normalized preparation arrows.

<1>1. **ASSUME** an actual constant trace-nonincreasing arithmetic CP map Phi.
**PROVE** (Phi,1) is an arrow preserving its actual composition equations.
  <2>1. Set Phi_0=Phi, Phi_k=0 for k>0, z_0=1 and z_k=0 for k>0.
  D1504's inequalities are precisely its ordinary trace bound at k=0.
  Composition/tensor are the original constant CP maps.
  **BY** D1326 and section 1.
  <2>2. At amplitude level retain the original Hilbert interpretation
  of every generator, sum, composite and adjoint. A coherent composite
  is evaluated as its actual amplitude matrix before passing to its
  prescribed CP instrument. Equal source amplitudes remain equal matrices;
  equal actual tagged CP processes remain equal constant arrows.
  **BY** FRP-CAT, FRP-CP and the constant inclusion in <2>1.
  <2>3. The CP semantic equality need not distinguish source Kraus
  presentations that already realize the same channel. No new amplitude
  faithfulness theorem is claimed. All original fixed preparations,
  including the maximally mixed one, remain their original constant maps.
  **QED** <1>1 by <2>1--<2>2.

<1>2. **ASSUME** a field E of absolute degree r.
**PROVE** `(z->zD_E(h),exp(rh))` and `(z->zL_E(h),1+rh)`
are normalized preparation arrows from the scalar algebra.
  <2>1. A preparation map z->zA is CP exactly when A>=0; its
  amplifications send a positive scalar matrix to its tensor with A.
  POS-STATE gives positive A_Ek with traces r^k/k!, matching the
  coefficients of exp(rh). D1504's normalization therefore holds.
  **BY** D1502, POS-STATE and the displayed tensor quadratic form.
  <2>2. For L, coefficients P0,B_E have traces 1,r, matching 1+rh.
  All higher coefficients vanish. Its normalizer is positive for h>=0.
  **BY** D1503 and POS-STATE.
  <2>3. Independent preparations tensor with multiplied normalizers.
  The exact reference equals the ordinary maximally mixed preparation at
  h=log p, but is not identified with that constant map as a family.
  The finite reference agrees with it only where an independent calculation
  establishes agreement; no arithmetic comparison point is stipulated for L.
  **QED** <1>2 by <2>1--<2>2 and POS-STATE.

<1>3. **ASSUME** a finite circuit with reference preparations, constant
arithmetic maps and named instruments.
**PROVE** its entire tagged process has a positive-series representative.
  <2>1. Every generator has such a representative by <1>1--<1>2.
  Repeated composition and independent tensor preserve the coefficient
  conditions by section 1. Keep intermediate measurement outcomes in
  external output tags when the protocol calls for their retention.
  **BY** D1505 and finite circuit induction.
  <2>2. Zero success at h=0 is allowed: the arrow still evaluates to
  a valid zero subnormalized output there. Rare-event conditioning is a
  separate operation on its output series, handled by D1506 below.
  **QED** <1>3 by <2>1 and D1504's trace inequality.

## 3. Exact arithmetic action on finite positive profiles

**ASSUME** D1503 and D1505.
**PROVE** coefficientwise action and profile experiments are monoidal and
retain complete arithmetic compositions before conditioning.

<1>1. **ASSUME** constant CP maps Phi,Psi and positive polynomials A,C.
**PROVE** positivity, functoriality and tensor compatibility of their actions.
  <2>1. Each Phi(A_k) is positive. The equations
  `(Psi Phi)_*A=Psi_*(Phi_*A)` and `id_*A=A` hold coefficientwise.
  Coefficients of A tensor C are `sum_(i+j=k)A_i tensor C_j`, positive;
  applying Phi tensor Psi gives `(Phi_*A) tensor (Psi_*C)`.
  **BY** complete positivity and finite distributive matrix operations.
  <2>2. Consequently a composable pair of profile arrows has exactly
  its stated target profile under the composite map. Tensor arrows have
  the tensor target. The actual swaps and associators give their usual
  coefficientwise equalities, so the profile category is symmetric monoidal.
  **BY** D1505 and <2>1.
  <2>3. Canonical L_word are monoidal reference objects because their
  definition is a tensor product. They are not stipulated to be natural
  under arbitrary CP maps: the output is Phi_*L, not a reset to a target
  canonical reference. Their preparation arrows belong to the series
  category of section 2; in this action category they are marked objects.
  **QED** POS-PROCESS by <2>1--<2>3 and sections 1--2.

## 4. A positivity lemma eliminates all irrelevant higher coefficients

**ASSUME** a finite-dimensional CP map Phi:B_X->B_Y, an orthogonal
projection P in one finite input algebra, and a positive matrix B whose
support is P and whose restriction to ran P is positive definite.
**PROVE** `Phi(B)=0` implies Phi annihilates every matrix supported in P.

<1>1. **ASSUME** a positive matrix C=PCP.
**PROVE** Phi(C)=0 if Phi(B)=0.
  <2>1. The least eigenvalue of B on ran P is a positive number b.
  Thus `0<=C<=||C||P<=(||C||/b)B`.
  A positive linear map preserves this ordering by applying it to the
  positive differences. Hence `0<=Phi(C)<=0` and Phi(C)=0.
  **BY** finite positive-matrix diagonalization and positivity of Phi.
  <2>2. Every supported matrix is a complex linear combination of
  supported positive matrices: split its real and imaginary Hermitian
  parts into their positive and negative spectral parts inside ran P.
  Linearity therefore extends the conclusion to the whole corner.
  **QED** the annihilation lemma by <2>1--<2>2.

**ASSUME** a D1501 word of m field registers and its D1503 masks.
**PROVE** Phi(D_word) and Phi(L_word) have the same first nonzero matrix
coefficient, with order <=m whenever Phi is nonzero.

<1>2. **ASSUME** a subset S of word positions.
**PROVE** `P_S D_word P_S=h^|S| B_S+sum_(k>|S|)h^k C_(S,k)`
with positive supported C_(S,k), and B_S faithful on ran P_S.
  <2>1. At a zero position only A_E0=P0 contributes. At a nonzero
  position the series begins with h B_E, and every subsequent coefficient
  is positive and supported on the nonzero subspace, by POS-STATE.
  Multiplying these independent factors gives the displayed series.
  **BY** D1502--D1503 and positive Cauchy tensor coefficients.
  <2>2. B_E is positive definite on the nonzero subspace, so the
  tensor B_S is positive definite on its mask. The mask projections are
  orthogonal and sum to I; every coefficient of D_word is their direct
  sum, with no cross-mask blocks.
  **BY** POS-STATE and D1503.
  <2>3. **QED** <1>2 by <2>1--<2>2.

<1>3. **ASSUME** Phi!=0 and v the least |S| with Phi(B_S)!=0.
**PROVE** v exists, v<=m and the two leading coefficients equal
`sum_(|S|=v)Phi(B_S)`.
  <2>1. The matrix `sum_S B_S=tensor_j(P0+B_Ej)` is faithful on
  the full input space. If Phi killed every B_S, it would kill this
  faithful matrix and hence the entire algebra by <1>1, contradicting
  Phi!=0. Thus a surviving mask exists and its size is at most m.
  **BY** <1>1,<1>2 and finite tensor spectra.
  <2>2. Every mask of size smaller than v has Phi(B_S)=0, so <1>1
  kills all its supported higher coefficients C_(S,k), not just its first.
  Larger masks begin at larger orders. At order v the surviving terms
  are precisely `sum_(|S|=v)Phi(B_S)` in both D_word and L_word.
  **BY** <1>1--<1>2 and D1503's polynomial formula.
  <2>3. That sum is nonzero because positive matrices cannot cancel:
  at least one has strictly positive trace. All lower coefficients vanish.
  **QED** the finite-profile lemma by <2>1--<2>3.

## 5. Conditional limits, future postselection and finite protocols

**ASSUME** the exact and finite-profile preparations on m independent
field references, and a fixed CP branch Phi from their full register word.
**PROVE** their leading probability coefficient and conditional state agree,
and the entire finite profile remains sufficient for all later branches.

<1>1. **ASSUME** a nonzero output positive series A with leading matrix M
at order v and scalar normalizer Z with Z(0)>0.
**PROVE** probability asymptotic `h^v Tr(M)/Z(0)` and conditional limit
`M/Tr(M)`.
  <2>1. Convergence gives `A(h)=h^v(M+O(h))` in matrix norm and
  `Tr A(h)=h^v(Tr M+O(h))`. Positivity and M!=0 give Tr M>0.
  Divide by Z(h)=Z(0)+O(h), or by Tr A(h), respectively.
  **BY** D1506, section 1 convergence and scalar division.
  <2>2. Both canonical word normalizers have constant term one:
  exact exp(Rh), finite product_j(1+r_j h). The lemma in section 4
  therefore gives identical v, event coefficient and conditional density.
  **QED** <1>1 by <2>1 and section 4.

<1>2. **ASSUME** a further fixed CP continuation Psi, possibly acting
jointly after tensoring an independent reference word.
**PROVE** the adequacy statement survives that continuation.
  <2>1. Without an added reference apply section 4 to the composite
  CP map Psi Phi. The polynomial action keeps Phi(L_word), so its
  later output is exactly Psi Phi(L_word), the correct finite surrogate.
  With an independent word, concatenate the input references first and
  use the composite map `Psi (Phi tensor id)`; this is CP even when
  Psi is entangling. The new bound is the total number of references.
  **BY** POS-PROCESS and section 4, with no restriction to product outputs.
  <2>2. For a nonzero prefix branch of order v and a subsequent
  nonzero combined branch of order w, positivity implies w>=v.
  Their conditional probability has order w−v and coefficient equal
  to the ratio of their leading traces. Both prefix and final traces
  agree under D and L, so this conditional asymptotic agrees as well.
  **BY** <1>1 and the fact a constant linear map cannot lower series order.
  <2>3. Leading normalized states alone do not satisfy this property.
  For one input L=P0+hB_E, its leading state is P0. A later nonzero-label
  projection kills P0 but gives hB_E from the retained profile, with order
  one and conditional output B_E/r. Thus deleting later grades would
  delete an actual positive-probability branch.
  **QED** <1>2 by <2>1--<2>3 and D1503.

<1>3. **ASSUME** a finite D1505 reference protocol with all branch histories.
**PROVE** its boundary records are computed by finite profiles of bounded degree.
  <2>1. Allocate all reference preparations as independent input
  registers before the circuit. Their later appearances can be implemented
  by identity wires until their prescribed use. For a finite adaptive
  circuit, allocate every potentially used reference, and discard unused
  ones on the relevant history. This produces one fixed CP map for each
  branch from a finite independent reference word.
  **BY** finite tensor circuits, constant discard and the specified
  measurement placement; no measurement is inserted into coherent paths.
  <2>2. Normalized exact inputs are D_word/exp(Rh); finite inputs are
  L_word/product_j(1+r_jh). Apply <1>1--<1>2 to each branch map.
  The profile degree never exceeds the number of allocated reference
  registers. If the branch map is zero it is absent for both preparations;
  otherwise its order is at most that number by section 4.
  **BY** <2>1 and sections 4--5 <1>1--<1>2.
  <2>3. Every arithmetic operation remains its full matrix during this
  calculation. Conditioning is performed only on the named outcomes, after
  their unnormalized CP maps act. This retains coherent returns from sectors
  that an intermediate compression would incorrectly delete.
  **QED** POS-FINITE by <2>1--<2>3 and section 4.

## 6. Finite grade meaning and comparison of retained structures

**ASSUME** the canonical finite word profile with degrees r_1,...,r_m.
**PROVE** its grade states have the following independent subset weights.

<1>1. **ASSUME** a grade k between zero and m.
**PROVE** `Tr coefficient_k(L_word)=sum_(|S|=k)product_(j in S)r_j`
and its normalized state is the mixture of B_S with these subset weights.
  <2>1. Tr B_Ej=r_j and Tr P0=1. Tensor traces therefore give
  Tr B_S=product_(j in S)r_j. Normalize each B_S by that trace;
  it becomes sigma_(E_j,1) at selected positions and P0 elsewhere.
  **BY** D1502--D1503 and ordinary tensor trace.
  <2>2. The normalized finite preparation is exactly an independent
  Bernoulli activation mixture with probabilities `r_j h/(1+r_j h)`.
  At a fixed grade its subset weights are proportional to product r_j.
  The maximal grade m is operationally necessary: selecting all nonzero
  labels yields that grade and a positive coefficient product r_j.
  **QED** <1>1 by <2>1 and product expansion of L_word.

The series category retains exact finite-h families; the finite profile
retains sufficient data for every specified leading branch question. It
does not retain all subleading Taylor coefficients or the exact arithmetic
comparison value at h=log p. These are separate, explicit retention rules.

Copied and independent references are different experiments. For the
nonzero diagonal test x=y!=0 on two independent E references, the exact
probability is `sum_(x!=0)rho_E(x)^2`, with order two and leading
coefficient `sum_(x!=0)w_x^2`. The actual copy isometry
`delta|x>=|x,x>` instead transports one reference, giving that event
order one and coefficient r. The naive continuation `(t^r−1)/t^(2r)`
of the independent arithmetic point count has order one, so it is not
the new mixed-reference rule. Positivity respects the order-two bound
because the independent diagonal event lies inside the both-nonzero event.
The positive strategy is to transport the actual copied/correlated profile
and preserve its circuit, rather than reset it to independent references.

The earlier MIX chart family changes its angle matrices. Here all actual
arithmetic matrices, including their Gram angles, are constant; states and
their finite operational profiles change. A named Fourier transform sends
D and L to their actual conjugates, not to the canonical reference again.
Likewise a prime-field coordinate unitary transports correlated field data.
No automatic identification with the MIX tangent or its weighted connector
is imposed. Any future comparison must specify the state/channel maps and
prove the named operational diagrams. The present nontrivial content is
the canonical positive normalization, the bounded sufficient reference
profile, and the all-extension mixed witness in the companion shard.
