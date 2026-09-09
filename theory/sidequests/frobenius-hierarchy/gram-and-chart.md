# Uniform arithmetic Gram sectors and a conditioned Fourier tangent

Author: native inherited Codex agent runtime; no model override or nested CLI.
Status: PROVED within the stated hypotheses after capped review. Claims:
MIX-GRAM and MIX-CHART. Definition source: ../../../definitions.md,
D1421--D1424,D1426; admitted inputs: D1301--D1306,
FRB-TRACE, FRB-TRANSFER and FRB-FROB. Every new leaf is an explicit
finite-field, inner-product or displayed matrix computation.
No statement depends on a deprecated snapshot or a finite sample.

Admission: ../../verdicts/arithmetic-mixed-adjudication.md.

## 1. The Gram map for every characteristic and degree

**ASSUME** D1421, with `i:K->E`, `q=p^s`, `Q=q^n`, `n>=2`.
**PROVE** `sqrt(kappa_i)(Gamma_i)_(x,a)=delta_(a,nx)` and the
singular-square classification in MIX-GRAM.

<1>1. **ASSUME** `x,a in K`.
**PROVE** the asserted Gram entry and its two spectral forms.
  <2>1. `T_i(i(x))=nx`: every summand of D1303's relative trace is
  `i(x)`, because `x^q=x`. **BY** D1303 and FRB-TRACE.
  <2>2. The coefficient of `|i(x)>` in `V_i|a>` is
  `kappa_i^(-1/2)` precisely when `T_i(i(x))=a`, otherwise zero.
  Taking the inner product with `J_i|x>` proves the formula.
  **BY** D1304 and <2>1. Named computation: GRAM-ENTRY.
  <2>3. If `p∤n`, multiplication by n is bijective in K, so
  `Gamma_i=c_i(D_n^K)^(-1)` and
  `Gamma_i^*Gamma_i=kappa_i^(-1)I_q`.
  **BY** D1422, <2>2 and basis permutation multiplication.
  <2>4. If `p|n`, then `Gamma_i=d_i|+_K><0|` and
  `Gamma_i^*Gamma_i=d_i^2|0><0|`, where `d_i^2=q/kappa_i=q^(2-n)`.
  **BY** D1421,D1423 and <2>2, summing q equal column entries.
  <2>5. **QED** <1>1 by <2>3--<2>4: these are all q eigenvalues.

<1>2. **ASSUME** the two D1304 isometries.
**PROVE** their range intersection has dimension one exactly for
`n=2,p=2`, and otherwise zero.
  <2>1. For any `z in H_K`, orthogonal decomposition gives
  `||(I-P_i)V_i z||^2=||z||^2-||Gamma_i z||^2`.
  Thus `V_i z` belongs to `ran J_i` exactly when
  `z` belongs to the eigenvalue-one space of `Gamma_i^*Gamma_i`.
  **BY** FRB-TRANSFER's isometries and matrix inner-product expansion.
  <2>2. In the invertible branch `kappa_i=q^(n-1)>1`; in the singular
  branch `q^(2-n)=1` iff `n=2`. The latter has `p|2`, hence `p=2`.
  Its eigenvalue-one space is the line `C|0>`.
  **BY** <1>1 and integer inequalities `q>=2,n>=2`.
  <2>3. The corresponding common unit vector is
  `alpha_i=J_i|+_K>=V_i|0>=beta_i`.
  Equality follows from their unit norms and inner product one.
  **BY** <1>1.<2>4 and the squared norm of their difference.
  <2>4. **QED** <1>2 and section 1 by <2>1--<2>3.

## 2. Fourier and Frobenius on the exact arithmetic frames

**ASSUME** D1306's negative Fourier kernel, with the same named
root of unity on all fields as in D1301.
**PROVE** the Fourier formulas below, with their stated domains.

<1>1. **ASSUME** the finite-field trace pairing of FRB-TRACE.
**PROVE** `F_K^2=R_K`, `F_E V_i=J_i F_K`,
`F_K|+_K>=|0>` and `F_K|0>=|+_K>`.
  <2>1. The `(z,x)` entry of `F_K^2` is
  `q^(-1)sum_y psi_K(-y(x+z))=delta_(z,-x)`.
  For `x+z!=0`, choose a character-nontrivial translate of y; the
  sum equals itself times a scalar different from one and is zero.
  **BY** D1306 and FRB-TRACE's nondegenerate trace pairing.
  <2>2. `R_E J_i=J_i R_K` by additivity of i, and
  `R_E V_i=V_i R_K` by linearity of the relative trace.
  **BY** D1304,D1421 and the basis substitution `x->-x`.
  <2>3. `F_E^2J_i=F_E V_i F_K=J_i F_K^2` by FRB-TRANSFER and
  <2>1--<2>2. Right cancellation of the unitary `F_K` gives
  `F_E V_i=J_i F_K`. **BY** FRB-TRANSFER's unitarity.
  <2>4. The zero column of the Fourier matrix is uniform; the Fourier
  transform of the uniform vector is the zero basis vector by the same
  character sum as <2>1. **BY** D1306 and <2>1.
  <2>5. **QED** <1>1 by <2>1--<2>4. Named computation: FOURIER-SWAP.

<1>2. **ASSUME** `p∤n` and D1422.
**PROVE** `mathcal T_i` is an isometry onto `S_i`, and
`F_E mathcal T_i=mathcal T_i(f_(c_i) tensor B_i)`.
  <2>1. `J_i^*L_i=c_i I`. Hence `J_i^*W_i=0` and
  `W_i^*W_i=(1-c_i^2)I/h_i^2=I`.
  Also `L_i=c_i J_i+h_i W_i`; the two ranges span `S_i`.
  **BY** section 1 <1>1.<2>3 and FRB-TRANSFER's isometries.
  <2>2. A basis substitution in D1306 gives
  `F_K D_n^K=(D_n^K)^(-1)F_K=B_i`.
  In particular `B_i` is unitary and `B_i^2=R_K`.
  **BY** the Fourier kernel `psi_K(-nxy)` and <1>1.<2>1.
  <2>3. `F_E J_i=L_i B_i` and `F_E L_i=J_i B_i`.
  The first uses `V_i=L_i(D_n^K)^(-1)`; the second uses <1>1.
  Thus `F_E W_i=(h_i J_i-c_i W_i)B_i`.
  **BY** FRB-TRANSFER, <2>2 and D1422's subtraction formula.
  <2>4. These two columns are precisely the claimed tensor matrix.
  Its domain is `C^2 tensor H_K`; its range is `S_i subset H_E`.
  **QED** <1>2 by <2>1--<2>3. Named computation: REGULAR-FRAME.

<1>3. **ASSUME** `p|n`, initially with `n>2`.
**PROVE** the orthogonal decomposition into D1423's angle and residual
frames and their Fourier matrices.
  <2>1. `0<d_i<1` and `<alpha_i,beta_i>=d_i`. Gram subtraction
  makes `mathcal T_i^ang` isometric; the two Fourier images are
  `F_E alpha_i=beta_i` and `F_E beta_i=alpha_i`.
  Thus `F_E mathcal T_i^ang=mathcal T_i^ang f_(d_i)`.
  **BY** section 1, <1>1 and D1423. Named computation: SINGULAR-PLANE.
  <2>2. `F_K A_K=|0>^perp`, by unitarity and `F_K|+>=|0>`.
  The Gram formula makes `J_i A_K` orthogonal to all of `ran V_i`,
  and `V_i(|0>^perp)` orthogonal to all of `ran J_i`.
  These residual spaces are also orthogonal to the angle plane.
  **BY** section 1 <1>1.<2>4 and D1423.
  <2>3. Therefore `mathcal T_i^res` is isometric with range equal
  to their orthogonal direct sum. In its two columns Fourier is

      F_res = [[0,R_K|_(A_K)],[I_(A_K),0]].

  Indeed `F_E J_i x=V_i F_K x`, while
  `F_E V_i F_K x=J_i F_K^2 x=J_i R_K x`.
  The restriction of R_K preserves A_K because R_K fixes `|+>`.
  **BY** <1>1 and FRB-TRANSFER. Named computation: SINGULAR-RESIDUAL.
  <2>4. The dimensions `2+2(q-1)=2q` equal `dim S_i` from section 1;
  hence these spaces exhaust the joint support.
  **QED** <1>3 by <2>1--<2>3 and dimension of a direct sum.

<1>4. **ASSUME** `p=2,n=2`.
**PROVE** `S_i=C alpha_i direct-sum ran mathcal T_i^res`, with
Fourier `1 direct-sum (X tensor I_(A_K))`.
  <2>1. Section 1 supplies the common line. The orthogonality and
  residual calculation <1>3.<2>2--<2>3 do not divide by `e_i`, so
  remain valid; their total dimension is `1+2(q-1)=2q-1`.
  **BY** section 1 and the cited explicit inner products.
  <2>2. Fourier fixes the common vector by FOURIER-SWAP, and
  `R_K=I` because `-x=x` in characteristic two. Substitution in
  SINGULAR-RESIDUAL proves the asserted matrix.
  **QED** <1>4 by <2>1--<2>2.

## 3. Projection algebra and physical block weights

**ASSUME** D1421 and the orthogonal frames of section 2.
**PROVE** the following complete three-stratum table. Each displayed
matrix summand acts identically on its indicated multiplicity space.
The trace on a matrix block is its normalized trace times the listed weight.

| Stratum | Joint projection algebra | Joint block weights | Complement weight |
|---|---|---|---|
| `p∤n` | `M2 tensor I_q` | `2q/Q=2/kappa_i` | `1-2q/Q` |
| `p|n,n>2` | `M2 direct-sum C direct-sum C`, multiplicities `1,q-1,q-1` | `2/Q,(q-1)/Q,(q-1)/Q` | `1-2q/Q` |
| `p=2,n=2` | `C direct-sum C direct-sum C`, multiplicities `1,q-1,q-1` | `1/Q,(q-1)/Q,(q-1)/Q` | `1-(2q-1)/Q` |

The full unital algebra adds a scalar summand on the complement. Fourier
preserves the joint support and complement; its complement restriction
is the actual `F_E` restriction, with no additional matrix formula asserted.

<1>1. **ASSUME** the regular frame of section 2 <1>2.
**PROVE** the first table row, including absence of further summands.
  <2>1. Conjugating `P_i,Ptilde_i` by the frame gives
  `p_(c_i) tensor I_q,q_(c_i) tensor I_q`.
  Their off-diagonal matrix entry is `c_i h_i>0`.
  Multiplication by the diagonal projections extracts the two matrix
  units `E_01,E_10`; their products supply both diagonal units.
  **BY** D1424 and REGULAR-FRAME. Named computation: TWO-PROJECTIONS.
  <2>2. The support identity belongs to the algebra: `P_i+Ptilde_i`
  is positive and invertible on `S_i`, zero on its complement, so its
  finite nonzero eigenvalues admit a polynomial f with `f(0)=0`
  and `f(lambda)=1` on each distinct positive eigenvalue.
  Explicit interpolation gives such f; thus `f(P_i+Ptilde_i)=E_i`.
  **BY** the two-by-two matrix in <2>1 and finite polynomial interpolation.
  <2>3. On the complement both projections vanish, and the unital
  algebra therefore acts by one common scalar. Its physical trace is
  dimension divided by Q. On `M2 tensor I_q` it is `(2q/Q)tr_2`.
  **QED** <1>1 by <2>1--<2>2 and ordinary matrix traces.

<1>2. **ASSUME** `p|n,n>2`.
**PROVE** the second table row.
  <2>1. On the angle plane the projections are `p_(d_i),q_(d_i)`.
  On the two residual spaces they are respectively `(I,0)` and `(0,I)`.
  These formulas follow from the orthogonality in section 2 <1>3.
  **BY** D1423 and SINGULAR-PLANE/SINGULAR-RESIDUAL.
  <2>2. `P_i Ptilde_i P_i/d_i^2` is projection onto `C alpha_i`.
  Likewise `Ptilde_i P_i Ptilde_i/d_i^2` projects onto `C beta_i`.
  Their nonzero angle generates the full plane M2 by TWO-PROJECTIONS.
  Subtracting the plane components from the original projections isolates
  each residual scalar summand. The complement is isolated by subtraction
  from the full identity. **BY** <2>1 and finite matrix products.
  <2>3. All summands have exactly the dimensions in the table; on a
  d-dimensional scalar summand the physical trace of its identity is d/Q.
  **QED** <1>2 by <2>1--<2>2 and ordinary traces.

<1>3. **ASSUME** `p=2,n=2`.
**PROVE** the third row and the residual Fourier matrix factor.
  <2>1. Both projections equal one on the common line. On residual
  spaces they have values `(1,0)` and `(0,1)`. Thus they commute, and
  their products `P_i Ptilde_i`, `P_i-P_i Ptilde_i`,
  `Ptilde_i-P_i Ptilde_i` isolate the three joint scalar blocks.
  **BY** section 2 <1>4 and projection multiplication.
  <2>2. On the residual corner their matrices are `E_00 tensor I_A`
  and `E_11 tensor I_A`, while Fourier is `X tensor I_A`.
  Products `E_00 X E_11` and its adjoint give off-diagonal units.
  Hence these compressed operations generate `M2 tensor I_A`.
  **BY** section 2 <1>4 and explicit two-by-two multiplication.
  <2>3. The joint weights and complement weight follow by dimensions.
  Conditioning on the residual support gives `tr_2 tensor tr_(A_K)`
  on its full corner. **QED** <1>3 and section 3 by <2>1--<2>2.

## 4. Frobenius, Galois action and the support period

**ASSUME** D1421, any characteristic stratum.
**PROVE** the Frobenius representation and period assertions of MIX-GRAM.

<1>1. **ASSUME** `p∤n`.
**PROVE** `U_E mathcal T_i=mathcal T_i(I_2 tensor U_K)`.
  <2>1. `D_n^K U_K=U_K D_n^K` since the prime-field scalar n
  satisfies `n^p=n`. Both J and V intertwine U by FRB-TRANSFER.
  Thus L and W do also, by their D1422 formulas.
  **BY** D1302,D1422 and FRB-TRANSFER.
  <2>2. Apply the two column identities to the definition of the frame.
  **QED** <1>1 by <2>1.

<1>2. **ASSUME** `p|n`.
**PROVE** both angle vectors are fixed, and the residual Frobenius
matrix is `I_2 tensor U_K|_(A_K)`.
  <2>1. Frobenius fixes `|0>` and permutes the terms of `|+>`;
  therefore it fixes alpha and beta by FRB-TRANSFER.
  **BY** D1302 and D1423.
  <2>2. `U_K F_K=F_K U_K`: replacing Fourier summation labels by
  p-th powers preserves the absolute trace and the product xy.
  Thus U preserves A_K and both residual columns intertwine its
  restriction. **BY** D1306, FRB-FROB and FRB-TRANSFER.
  <2>3. If n>2, the representation is `1+1+2(U_K minus 1)`;
  in the exceptional case it is `1+2(U_K minus 1)`.
  Here subtraction specifies the actual orthogonal complement of the
  fixed uniform vector, not a negative Hilbert summand.
  **QED** <1>2 by <2>1--<2>2 and section 2's orthogonal frames.

<1>3. **ASSUME** `q=p^s`.
**PROVE** `U_E^s=I` on `S_i` in all strata.
  <2>1. FRB-FROB gives `U_K^s=I`; every summand in <1>1--<1>2
  is a restriction or a copy of that representation.
  The common line, when present, is fixed.
  **BY** <1>1--<1>2 and FRB-FROB.
  <2>2. In particular the relative finite-field Galois action generated
  by `U_E^s` is trivial on this joint support; the nontrivial absolute
  Frobenius action remains on its logical factors.
  This does not identify the joint support with all of `H_E`.
  **QED** <1>3 and MIX-GRAM by <2>1 and sections 1--3.

## 5. Conditioning first and the positive tangent

Early physical-trace stress, recorded once: in the invertible branch the
formal complementary weight is `1-2/kappa`. At `kappa=3/2` it is `-1/3`.
Thus that unconditioned central weight cannot be a positive state near one.
The forward construction conditions on the joint chart first, using section
3's positive weight at each arithmetic fibre, and only then varies its angle.
This observation is not a separately promoted obstruction claim.

**ASSUME** D1424 and either the regular joint chart or singular `n>2`
angle chart of section 2, with their physical conditional reference states.
**PROVE** the endpoint retains a faithful M2 chart and actual Fourier
conjugation, with a noncommuting normalized tangent.

<1>1. **ASSUME** `0<c<1` and `h=sqrt(1-c^2)`.
**PROVE** `d_c^2=f_c^2=I`, `f_c p_c f_c=q_c`, and
`f_c d_c+d_c f_c=0`.
  <2>1. Multiply the two-by-two matrices of D1424. The diagonal
  squares are `c^2+h^2=1`, the off-diagonal squares cancel, and
  `f_c|0>=c|0>+h|1>`, whose rank-one projection is q_c.
  **BY** D1424. Named computation: CHART-MATRICES.
  <2>2. Direct subtraction gives
  `q_c-p_c=h[[-h,c],[c,h]]=h d_c`. Products with f_c in
  either order have opposite entries, proving anticommutation.
  **BY** D1424 and entrywise subtraction/multiplication.
  <2>3. **QED** <1>1 by <2>1--<2>2.

<1>2. **ASSUME** the matrix family on the closed interval `0<=c<=1`.
**PROVE** continuity, faithful reference and endpoint distinction.
  <2>1. Every matrix entry is continuous; at one `p_1=q_1=E_00`,
  `f_1=Z` and `d_1=X`. `E_00 X E_11=E_01` and its adjoint
  generate M2 with the diagonal projections. Thus the retained tangent,
  together with p_1, retains the full M2 algebra at the endpoint.
  **BY** D1424 and explicit matrix units.
  <2>2. `tr_2(A^*A)=sum_(j,k)|A_jk|^2/2`, positive for `A!=0`.
  It is the conditioned physical trace by section 3. On a logical
  factor use the product normalized matrix trace; the same entry sum
  proves faithfulness. **BY** D1424 and section 3.
  <2>3. Prepare density matrix `rho=E_00` and measure effect E_00.
  The initial probability is one; after d_1=X it is zero.
  Actual Fourier acts by Ad_Z on the endpoint chart, and Ad_Z(X)=-X.
  These assertions follow from the same retained matrices, with no new
  Fourier operator substituted after continuation.
  **QED** <1>2 by <2>1--<2>2 and ordinary Born traces.

## 6. Retained CP operations and the exact scope of the chart result

**ASSUME** D1426 and a finite collection of D1424 chart factors.
**PROVE** their continuous instruments and independent tensor remain
completely positive and trace preserving at every parameter, including one.

<1>1. **ASSUME** a D1426 family `K_b(t)`.
**PROVE** complete positivity, trace preservation and continuity.
  <2>1. For every ancillary space Z, each matrix
  `(I_Z tensor K_b) rho (I_Z tensor K_b)^*` is positive when rho is:
  its quadratic form on x is rho's quadratic form on
  `(I_Z tensor K_b)^*x`. Sums and tagged direct sums stay positive.
  **BY** finite matrix quadratic forms and D1426.
  <2>2. Cyclicity of finite matrix trace gives output trace
  `Tr(rho sum_b K_b^*K_b)=Tr(rho)`. Entries are finite sums of
  products of continuous entries, so every output matrix is continuous.
  **BY** D1426 and matrix multiplication.
  <2>3. **QED** <1>1 by <2>1--<2>2.

<1>2. **ASSUME** continuous isometries and independent instruments.
**PROVE** retained decoding and tensor completeness.
  <2>1. For S, `SS^*+(I-SS^*)^2=I` by `S^*S=I`.
  For independent families the sum of squared Kraus amplitudes is
  `(sum_b K_b^*K_b) tensor (sum_d L_d^*L_d)=I tensor I`.
  All pairs of tags remain distinct. **BY** D1426 and multiplication.
  <2>2. D1424's rank-one columns e0 and `v=c e0+h e1` are
  continuous isometries. Since `f_c e0=v`, the decoder identity is
  `D_v Ad_(f_c)=(id_C direct-sum Ad_(f_c)) D_(e0)`.
  Success follows from `v^* f_c=e0^*`; failure follows from
  `(I-vv^*)f_c=f_c(I-e0e0^*)`.
  **BY** CHART-MATRICES and D1426, branch by branch.
  <2>3. In the physical regular frame the corresponding identity is
  `D_(L_i) Ad_(F_E)=(Ad_(B_i) direct-sum Ad_(F_E)) D_(J_i)`.
  It follows from `F_E J_i=L_i B_i` and the same failure calculation.
  Both logical factors and ambient failure states are retained.
  **QED** <1>2 by <2>1--<2>2 and REGULAR-FRAME.

<1>3. **QED** MIX-CHART by sections 3,5 and <1>1--<1>2, with scope:
regular degrees use the whole joint chart; singular n>2 uses its named
plane; quadratic characteristic two uses the residual M2 factor of
section 3 <1>3 at `f=X`, without an arithmetic coalescing-plane claim.
Frobenius acts on the logical factors as in section 4, not as an added
chart flip. Arbitrary multiplication transitions and singular tower
refinements are not established by these local positive chart constructions.
