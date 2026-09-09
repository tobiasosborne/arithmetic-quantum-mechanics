# Coherent all-length refinement and the remaining mixed conjecture

Author: native inherited Codex agent runtime; no model override or nested CLI.
Status: MIX-TOWER is PROVED within its stated hypotheses; MIX-ALL remains
CONJECTURE. Definition source: ../../../definitions.md, D1422,D1425--D1428.
Dependencies: MIX-GRAM, MIX-CHART, FRB-TRANSFER and FRB-TRACE.
Only tower degrees invertible in the characteristic enter the positive
refinement theorem. The singular Gram classification itself has all degrees.
No field or tower is replaced by a small finite example in the proof.

Admission: ../../verdicts/arithmetic-mixed-adjudication.md.

## 1. Corrected trace transfers compose in every invertible-degree tower

**ASSUME** a named tower `K --i--> L --j--> E` of degrees `m,n>=2`
with `p∤mn`, and D1422's corrected trace maps.
**PROVE** `L_j L_i=L_(ji):H_K->H_E`.

<1>1. **ASSUME** a nonzero prime-field scalar a and any D1303 embedding i.
**PROVE** `D_a^L J_i=J_i D_a^K` and `D_a^L V_i=V_i D_a^K`.
  <2>1. `a i(x)=i(ax)`, since a lies in the common prime field.
  Therefore the inclusion formula holds on every basis vector.
  **BY** D1304 and preservation of addition by a field embedding.
  <2>2. Relative trace linearity gives `T_i(ay)=a T_i(y)`.
  Multiplication by a bijects the fibre over x with the fibre over ax,
  retaining its cardinality and positive normalization.
  **BY** FRB-TRACE,D1304 and bijectivity of nonzero scalar multiplication.
  <2>3. **QED** <1>1 by <2>1--<2>2. Named computation: SCALAR-TRANSFER.

<1>2. **ASSUME** the degrees m,n as above.
**PROVE** the corrected trace tower formula, with no untyped scalar.
  <2>1. The scalar n acts on L in `L_j=V_j D_n^L`, and on K
  in the equality `D_n^L V_i=V_i D_n^K` from <1>1.
  Consequently

      L_j L_i = V_j D_n^L V_i D_m^K
              = V_j V_i D_n^K D_m^K
              = V_(ji) D_(mn)^K = L_(ji).

  **BY** SCALAR-TRANSFER, FRB-TRANSFER and multiplication of scalar
  permutation matrices. The composite degree is mn.
  <2>2. `kappa_(ji)=kappa_j kappa_i`, hence
  `c_(ji)=c_j c_i`; all square roots are positive.
  **BY** FRB-TRACE and cardinality ratios `|E|/|K|`.
  <2>3. **QED** section 1 by <2>1--<2>2. Named computation: CORRECTED-TOWER.

## 2. The direct two-chart frame inside all path frames

**ASSUME** the D1425 tower of length l and arithmetic parameters c_r.
**PROVE** `mathcal T_path` is an isometry and, for composite arrow k,

    mathcal T_k = mathcal T_path (C_(c_l,...,c_1) tensor I_(H_(K_0))).

<1>1. **ASSUME** any `0<c_r<1`, whether arithmetic or not.
**PROVE** the D1425 connector is an isometry.
  <2>1. Each `v_r=c_r e0+h_r e1` has norm one and inner product
  c_r with e0. Thus the tensor v has norm one and inner product c_*
  with `e_empty=|0...0>`.
  **BY** D1425 and finite tensor-product inner products.
  <2>2. The second column `(v-c_*e_empty)/h_*` is orthogonal to
  the first and has squared norm `(1-c_*^2)/h_*^2=1`.
  **QED** <1>1 by <2>1 and D1425. Named computation: CONNECTOR-GRAM.

<1>2. **ASSUME** the arithmetic path frame.
**PROVE** it is isometric and identifies both direct code columns.
  <2>1. Each local frame is isometric by MIX-GRAM. Tensoring with
  an identity preserves the equation `S^*S=I`; composing two such maps
  does also. Iterating proves path isometry.
  **BY** MIX-GRAM, D1425 and adjoint matrix multiplication.
  <2>2. The all-zero path column is
  `J_(i_l)...J_(i_1)=J_k`, by FRB-TRANSFER. Replacing each zero
  column by its vector v_r gives
  `L_(i_l)...L_(i_1)=L_k`, by CORRECTED-TOWER applied successively.
  **BY** D1422,D1425, FRB-TRANSFER and section 1.
  <2>3. Since `c_k=c_*`, taking the normalized difference of these
  two columns gives `W_k`; this is exactly the second connector column.
  Both sides of the displayed frame identity therefore agree on
  `e0 tensor x` and `e1 tensor x` for every logical vector x.
  **QED** <1>2 and section 2 by <2>1--<2>2.

For l=2 the second column is explicitly

    (c_j h_i|01>+h_j c_i|10>+h_j h_i|11>)/sqrt(1-c_j^2 c_i^2),

in the fixed outer-to-inner order. There is no unspecified phase freedom.

## 3. All consecutive-block refinements are coherent

**ASSUME** a partition of an ordered length-l tower into nonempty
consecutive blocks, with D1425 product parameters on the blocks.
**PROVE** first refining into blocks and then within blocks gives the
same connector as direct refinement into the common path basis.

<1>1. **ASSUME** block b has path vector `v_b^path`, product parameter
`c_b` and `h_b=sqrt(1-c_b^2)`.
**PROVE** its connector sends `e0` to its empty word and sends
`c_b e0+h_b e1` to `v_b^path`.
  <2>1. Both identities are immediate column evaluations: the h_b
  factor cancels its connector denominator and the c_b empty-word
  terms cancel. **BY** D1425.
  <2>2. **QED** <1>1 by <2>1. Named computation: TWO-ANCHOR-REFINEMENT.

<1>2. **ASSUME** the ordered block partition.
**PROVE** equality of direct and two-stage connectors.
  <2>1. Both maps send e0 to the full empty word by <1>1.
  Both send `c_*e0+h_*e1` to `v_l tensor...tensor v_1` by applying
  <1>1 to each block. These two input vectors are linearly independent
  because h_*>0. Therefore the maps agree on a basis of C².
  **BY** <1>1 and elementary linearity.
  <2>2. Every finite bracketing or multi-stage consecutive refinement
  can be collapsed one grouping at a time using <2>1. The result is
  always the same direct connector into the named path basis.
  In particular both sides of any associativity comparison, including
  a five-bracketing pentagon, are this same map.
  **BY** <2>1 and induction on the finite number of grouping stages.
  <2>3. **QED** section 3 by <2>1--<2>2. No basis labels are identified
  across unrelated fields; only the explicitly ordered chart basis is used.

## 4. Actual Fourier and Frobenius survive the tower comparisons

**ASSUME** the arithmetic D1425 tower, composite degree N, and
the D1424 matrices `f_(c_r)` on the path factors.
**PROVE**

    F_(K_l) mathcal T_path
      = mathcal T_path ((f_(c_l) tensor ... tensor f_(c_1))
                       tensor ((D_N^(K_0))^(-1) F_(K_0))),
    U_(K_l) mathcal T_path
      = mathcal T_path (I_(2^l) tensor U_(K_0)),
    (tensor_r f_(c_r)) C = C f_(c_*).

<1>1. **ASSUME** a nonzero prime-field scalar a and a regular local frame.
**PROVE** `D_a^L mathcal T_i=mathcal T_i(I_2 tensor D_a^K)`.
  <2>1. SCALAR-TRANSFER proves the formula for J and V. Scalar
  dilations commute with each other; consequently it holds for L and
  its normalized linear combination W as well.
  **BY** D1422 and section 1 <1>1.
  <2>2. The two columns give the frame equation. **QED** <1>1.

<1>2. **ASSUME** the formulas hold for the first l−1 edges.
**PROVE** them for l edges, with the stated logical Fourier factor.
  <2>1. MIX-GRAM gives on the outer frame
  `F_(K_l) mathcal T_(i_l)=mathcal T_(i_l)
  (f_(c_l) tensor ((D_(n_l)^(K_(l-1)))^(-1)F_(K_(l-1))))`.
  Apply the induction hypothesis to the lower path frame, then <1>1
  successively to commute the scalar dilation down to K_0.
  **BY** MIX-GRAM, D1425 and <1>1.
  <2>2. The resulting logical factor is
  `(D_(n_l)^(K_0))^(-1)(D_(n_(l-1)...n_1)^(K_0))^(-1)F_(K_0)`
  `=(D_N^(K_0))^(-1)F_(K_0)`.
  The base case l=1 is MIX-GRAM, so induction proves the Fourier formula.
  **BY** scalar multiplication and <2>1.
  <2>3. Each local Frobenius frame equation is
  `U_(K_r) mathcal T_(i_r)=mathcal T_(i_r)(I_2 tensor U_(K_(r-1)))`.
  Substitution down the path proves its claimed tensor form.
  **BY** MIX-GRAM and D1425.
  <2>4. **QED** <1>2 by <2>1--<2>3.

<1>3. **ASSUME** any D1425 parameters, including nonarithmetic ones.
**PROVE** the chart connector intertwines Fourier.
  <2>1. D1424's involution f_c exchanges e0 and `v=c e0+h e1`.
  Therefore the tensor involution exchanges the full empty word and
  the tensor vector v. Substituting the connector's second column gives
  `F_path C e1=C(h_*e0-c_*e1)`; the first gives
  `F_path C e0=C(c_*e0+h_*e1)`.
  **BY** CHART-MATRICES and D1425.
  <2>2. These are the two columns of `C f_(c_*)`.
  **QED** section 4 by <2>1 and <1>1--<1>2.

This is Fourier coherence for the named invertible-degree tower chart
frames, with their actual logical scaling. It is stronger than retaining
an abstract Fourier matrix on each isolated plane, and remains smaller
than a Fourier-and-multiplication realization on every arithmetic circuit.

## 5. The weighted endpoint for every finite tower length

**ASSUME** D1427's positive real weights and parameter t>1.
**PROVE** the connector extends continuously to its stated endpoint,
retaining all refinement and chart-Fourier identities.

<1>1. **ASSUME** a nonempty subset S of path-factor indices and
`epsilon=t-1>0` tending to zero.
**PROVE** its coefficient in `C_a(t)e1` tends to
`sqrt(a_r/A)` when `S={r}` and zero when `|S|>=2`.
  <2>1. Differentiability of `t^(-a)` at one gives
  `1-t^(-a_r)=a_r epsilon+O(epsilon^2)` and
  `1-t^(-A)=A epsilon+O(epsilon^2)`.
  Equivalently these follow by Taylor expanding `exp(-a log(1+epsilon))`.
  **BY** the displayed elementary scalar expansion.
  <2>2. The S coefficient is
  `product_(r in S) sqrt(1-t^(-a_r))
   product_(r notin S) t^(-a_r/2) / sqrt(1-t^(-A))`.
  It has order `epsilon^((|S|-1)/2)` and the singleton limit stated.
  **BY** D1425,D1427 and <2>1.
  <2>3. The empty-word coefficient of the second column is identically
  zero. There are finitely many subsets, so entrywise convergence is
  matrix-norm convergence. **QED** <1>1 by <2>1--<2>2.

<1>2. **ASSUME** the endpoint connector.
**PROVE** isometry, refinement coherence and Fourier intertwining at one.
  <2>1. Distinct single-excitation vectors are orthogonal, and
  `sum_r a_r/A=1`; they are also orthogonal to the empty word.
  The two endpoint columns are therefore orthonormal.
  **BY** D1427 and finite inner products.
  <2>2. All refinements are products of finitely many connectors.
  Their t>1 equalities from section 3 pass to the limit by continuity.
  Directly, a block of weight A_b contributes
  `sqrt(A_b/A)sqrt(a_r/A_b)=sqrt(a_r/A)` to edge r.
  **BY** <1>1, section 3 and multiplication of positive square roots.
  <2>3. Each f_c tends to Z. Tensor Z fixes the empty word and
  negates every single-excitation vector, so
  `Z^(tensor l) C_a(1)=C_a(1) Z`.
  This is also the continuous limit of section 4 <1>3.
  **BY** D1424,D1427 and the diagonal entries of Z.
  <2>4. **QED** <1>2 by <2>1--<2>3.

<1>3. **ASSUME** the direct normalized tangent d_(c_*).
**PROVE** its encoded limit has exactly the direct two-dimensional support.
  <2>1. `C d_(c_*) C^*` is the normalized difference of the
  rank-one projections onto tensor v and the empty word, divided by h_*.
  Its square is `CC^*`, because `C^*C=I` and `d_(c_*)^2=I`.
  **BY** D1424,D1425 and CONNECTOR-GRAM.
  <2>2. At one it is
  `|W_a><empty|+|empty><W_a|`, with
  `|W_a>=sum_r sqrt(a_r/A)|one_r>`.
  Its square is projection onto `span{|empty>,|W_a>}` and it is zero
  on all orthogonal path directions. Higher-excitation sectors still
  exist in the full independent tensor; they are not images of this
  direct two-dimensional connector.
  **QED** section 5 by <2>1, <1>1--<1>2 and D1427.

## 6. Positive retained decoding and what tower histories mean

**ASSUME** D1426 instruments for the local/direct chart frames and
the continuous connectors of sections 2--5.
**PROVE** retained CP decoding and independent tensor are continuous
through the endpoint; decoder success amplitudes compose coherently.

<1>1. **ASSUME** any connector C(t).
**PROVE** its retained decoder is CPTP and has conditional direct reference.
  <2>1. The amplitudes `C^*` and `I-CC^*` obey
  `CC^*+(I-CC^*)^2=I`, with continuous entries including at one.
  MIX-CHART's matrix argument proves complete positivity and trace
  preservation. **BY** D1426 and sections 2,5.
  <2>2. On the full l-factor maximally mixed state the success weight
  is `2/2^l`; its unnormalized successful density is `I_2/2^l`.
  Dividing by success gives `I_2/2`, hence D1427's direct reference.
  Tensoring a normalized logical identity changes neither ratio.
  **BY** `C^*C=I` and ordinary matrix traces.
  <2>3. **QED** <1>1 by <2>1--<2>2.

<1>2. **ASSUME** two composable isometries `A:X->Y`, `B:Y->Z`.
**PROVE** sequential success equals direct success, while all full
history instruments remain well typed without asserting their equality.
  <2>1. Decoding B then A has success amplitude `A^*B^*=(BA)^*`.
  The other amplitudes are `(I-AA^*)B^*:Z->Y` and
  `I-BB^*:Z->Z`, with distinct failure tags.
  The sum of their squared amplitudes and the success square is I_Z.
  **BY** D1426 and cancellation of adjacent isometries.
  <2>2. The direct decoder instead has a single failure amplitude
  `I-BAA^*B^*`. Its failure output can retain coherence between
  `ran(B) perp` and `B(ran(A) perp)`, whereas sequential measurement
  separates those histories. Thus no equality of these different full
  instruments is imposed. Their success identity is exact.
  **BY** expanding the direct failure projector as
  `(I-BB^*)+B(I-AA^*)B^*` and its quadratic output.
  <2>3. Iteration retains each first-failure history and the all-success
  branch. Independent tensor retains every pair, and any finite tuple,
  of histories. Completeness follows by multiplying the individual
  Kraus completeness sums, as in MIX-CHART.
  **QED** <1>2 by <2>1--<2>2 and finite induction.

<1>3. **QED** MIX-TOWER by sections 1--5 and <1>1--<1>2. The
all-length assertion has no bound on l but requires every n_r invertible
in characteristic p. Identity edges can be omitted; their transfer is
the identity and they require no two-dimensional local angle factor.

## 7. Sharpened all-characteristic mixed-process conjecture

MIX-ALL is a construction problem, not a consequence of the preceding
matrix identifications. The input comprises every D1428 finite diagram,
including towers with `p|n_r`, together with the separately specified
finite-etale Galois-set realization and its orbit-type comparisons.
The latter's embedding-set register is not identified with `l2(E)`.
A proposed positive filtered realization must provide the following data
and prove the following compatibility requirements, not merely name them.

1. **Actual process objects and arrows.** Give the operator algebras,
   positive reference functionals, CP arrows, tensor comparisons and
   exact equality relation. Every named arithmetic fibre realizes the
   original matrices on the prescribed registers, with its named Galois
   action. State all auxiliary marking and continuation choices and their
   comparison maps. An arbitrary constant matrix envelope is insufficient.
2. **A single rule for mixed normalization.** Specify a common filtered
   rule for moments of mixed words in projections, Fourier, multiplication
   and transfer amplitudes. It must recover the prescribed conditional
   chart traces, moving-orbit traces and active-control weights. Give the
   weights and the first retained coefficient explicitly for each claimed
   sector. Positivity must hold on all finite matrix amplifications and
   mixed moment Gram matrices, not just each isolated two-by-two block.
3. **All characteristic strata and all diagram refinements.** Retain the
   rank-one Gram sectors and exceptional common line proved in MIX-GRAM.
   Supply new singular-sector refinement maps compatible with original
   J,V tower identities. In the invertible-degree stratum recover exactly
   MIX-TOWER's connector, logical Fourier scaling and endpoint weights.
   Do not continue a residue-class degree n as an invertible scalar when
   it is zero in the field. Normal-closure/Galois comparisons must act
   compatibly on whichever source fragment supplies them.
4. **Named mixed arithmetic relations.** Preserve Fourier-transfer and
   inclusion/multiplication diagrams of the admitted arithmetic source,
   not an invented commutation with trace transfer. For every prescribed
   measurement placement preserve the tagged instrument's circuit
   probabilities and every independent tensor outcome. An unmeasured
   circuit and a circuit with intermediate sector measurement are distinct
   source processes; retaining measurement tags does not undo dephasing.
5. **Nontrivial observable endpoint.** Exhibit a state/effect witness for
   retained Frobenius and for an active multiplication transition in the
   common model, as well as the already explicit chart tangent witness.
   The mixed rules must determine their interaction rather than declare
   unrelated matrix blocks to be their joint realization.

The next bounded falsifier is a genuine diagram-and-circuit comparison.
Use both binary and ternary towers: `F2->F4->F16` has two singular
quadratic edges and a singular composite; `F3->F9->F81` has regular
quadratic edges and a regular composite. Add `F3->F27` to retain the
odd-characteristic degree-dividing residual parity R. Compare direct and
iterated actual Gram-sector frames where they are defined, and enumerate
the source's retained outcomes for a Fourier/multiplication/transfer word.
On the binary quartic field, choose moving-label controls and target that
the actual multiplication sends to a fixed label, as in FRL-ACTIVE's
existing leakage test. Compare the unmeasured circuit, the circuit with
the stated intermediate measurement, and the incorrectly compressed-only
circuit separately. Failure of the last comparison identifies a process
the candidate must retain; it is not evidence against the valid local
chart or invertible-degree tower theorems.

No full Fourier/multiplication category, no all-characteristic tower
connector, and no continuation of arbitrary mixed moments is constructed
in this shard. Those are exactly the remaining requirements of MIX-ALL.
