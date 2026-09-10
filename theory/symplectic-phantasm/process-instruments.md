# Branch closure, retained instruments, and the ambient trace adjoint

Lane model: `gpt-5.6-sol`, reasoning `xhigh`.

Admitted proof completing SP-CP; capped review and repair dispositions are
in `theory/verdicts/phantasm-processes-adjudication.md`.  Use D1706's current outcome-first and ordinary-trace-
adjoint prescriptions.  The intrinsic Kraus/CP/TNI equivalence is proved in
`process-kraus-blocks.md`; admitted FRP-CP supplies the earlier arithmetic-image
matrix calculation at its stated scope.  The adjoint constructed here is an
ambient reverse-direction CP map and is not automatically a reverse D1706
branch.

## 1. Composition of branches and channels

**ASSUME** D1706 branches `Phi:B_X->B_Y` and `Psi:B_Y->B_Z`, with Kraus
operators `K_(b a,j):H_a->K_b` and `L_(c b,t):K_b->L_c`.
**PROVE** their composite is a branch, and is a channel when both factors
are channels.

<1>1. Expanding the two actual maps gives

    (Psi Phi)(rho)_c
      =sum_(a,b,j,t) (L_(c b,t)K_(b a,j)) rho_a
         (L_(c b,t)K_(b a,j))^*.

**BY** D1706, finite distributivity, and `(LK)^*=K^*L^*`.

<1>2. Thus a composite Kraus index is the triple `(b,j,t)`: the
intermediate block `b` remains part of the hidden path.
**BY** `<1>1` and typing of the two rectangular factors.

<1>3. Put

    A_a=sum_(b,j)K_(b a,j)^*K_(b a,j),
    C_b=sum_(c,t)L_(c b,t)^*L_(c b,t).

Then `A_a<=1_(H_a)` and `C_b<=1_(K_b)`.
**BY** D1706's branch inequalities.

<1>4. The composite effect at input `a` is

    sum_(b,j) K_(b a,j)^* C_b K_(b a,j).

**BY** collect the squared composite Kraus operators from `<1>1`.

<1>5. This is at most `A_a` and therefore at most `1_(H_a)`.
**BY** every difference
`K^*(1_(K_b)-C_b)K` is positive, and use `<1>3`.

<1>6. Hence the composite is a D1706 branch.
**BY** `<1>1`, `<1>5`, and `process-kraus-blocks.md` section 4.

<1>7. If both factors are channels, every `C_b=1_(K_b)` and every
`A_a=1_(H_a)`, so the composite effect in `<1>4` is the identity.
**BY** D1706 and `process-kraus-blocks.md` section 5.

<1>8. Consequently channels compose to channels.  The calculation is a
property of the actual composite map and does not retain the selected Kraus
presentation.
**BY** `<1>6`--`<1>7` and D1706 map equality.

<1>9. **QED** composition closure and normalization.
**BY** `<1>1`--`<1>8`, matching admitted FRP-CP `<1>8` at matrix scope.

## 2. Tensor products, including entangled inputs

**ASSUME** an independent branch `Theta:B_(X')->B_(Y')` with
`X'=(H'_(a'))`, `Y'=(K'_(b'))`, and Kraus operators
`M_(b' a',u)`.  **PROVE** `Phi tensor Theta` is a branch on D1706's
Cartesian block tags, and a channel when both factors are channels.

<1>1. Under distribution of the finite direct sums, the Kraus operator on
block `((b,b'),(a,a'))` and hidden pair `(j,u)` is

    K_(b a,j) tensor M_(b' a',u).

**BY** D1706's listed-factor order and the ordinary tensor product of
linear maps.

<1>2. On an elementary input `rho_a tensor sigma_(a')`, this Kraus family
gives exactly

    Phi(rho)_b tensor Theta(sigma)_(b').

**BY** `(K tensor M)(rho tensor sigma)(K tensor M)^*`
equals `(K rho K^*) tensor (M sigma M^*)`, followed by finite sums.

<1>3. Elementary matrix tensors span every block
`End(H_a tensor H'_(a'))`; hence the formula defines the tensor of the
actual maps on every operator, including entangled positive inputs.
**BY** the matrix-unit basis comparison in admitted FRP-CP
`<1>9.<2>1`--`<1>9.<2>3`.

<1>4. Let `A_a` be Phi's effect and
`D_(a')=sum_(b',u)M_(b' a',u)^*M_(b' a',u)`.  The tensor branch effect is

    A_a tensor D_(a').

**BY** distribute the squared tensor Kraus operators from `<1>1`.

<1>5. If `0<=A_a<=1` and `0<=D_(a')<=1`, then

    1 tensor 1-A_a tensor D_(a')
      =(1-A_a) tensor 1+A_a tensor (1-D_(a')) >=0.

**BY** tensor products of positive finite matrices are positive, seen from
positive square roots or quadratic forms.

<1>6. Thus `A_a tensor D_(a')<=1`, and the tensor map is a branch.
**BY** `<1>4`--`<1>5` and `process-kraus-blocks.md` section 4.

<1>7. If both maps are channels, `A_a=D_(a')=1`; the tensor effect is the
identity on every input block, so the tensor is a channel.
**BY** `<1>4` and `process-kraus-blocks.md` section 5.

<1>8. Cartesian associators, unitors, and swaps act by the same reindexing
on block tags and tensor matrix units on either route, so the tensor closure
obeys the stated coherence.
**BY** D1706 and admitted FRP-CP `<1>9.<2>4`.

<1>9. **QED** tensor closure for branches and channels, without a
product-state restriction.
**BY** `<1>1`--`<1>8`.

## 3. Retaining an instrument outcome

**ASSUME** a D1706 instrument `(Phi_o)_(o in O):B_X->B_Y`; thus every
`Phi_o` is a branch with the same source and target and

    C=sum_o Phi_o

is a channel.  **PROVE** the retained version is a channel into the
outcome-first direct sum and has the stated probabilities.

<1>1. D1706 identifies the retained codomain as

    direct-sum_(o in O)B_Y
      =direct-sum_((o,b) in O times B) End(K_b).

**BY** D1706's outcome-first block prescription.

<1>2. Define the retained map by

    widehat(Phi)(rho)_(o,b)=Phi_o(rho)_b.

Its Kraus list into block `(o,b)` is the selected list of branch `Phi_o`
into block `b`.
**BY** D1706 and the definition of retained version.

<1>3. The retained map is CP by the block Kraus calculation.
**BY** `process-kraus-blocks.md` section 1.

<1>4. The total effect at input `a` is the sum over `o,b,j` of the branch
Kraus squares, which is the effect of the channel `C` and equals
`1_(H_a)`.
**BY** finite distributivity, the instrument channel-sum hypothesis, and
`process-kraus-blocks.md` section 5.

<1>5. Hence `widehat(Phi)` is a channel.
**BY** `<1>3`--`<1>4`.

<1>6. On a density `rho`, its ordinary output trace is

    Tr_(ret)(widehat(Phi)(rho))
      =sum_o Tr_Y(Phi_o(rho))
      =Tr_X(rho)=1.

**BY** D1706's ordinary direct-sum trace and the fact that `C` is a
channel.

<1>7. There is no factor `|O|`: each outcome block occurs exactly once in
the direct sum and ordinary trace adds those blocks.
**BY** `<1>1` and `<1>6`.

<1>8. The Born weight of outcome `o` is `Tr_Y(Phi_o(rho))`.  If it is
positive, D1706's conditional state is `Phi_o(rho)` divided by that weight;
if it is zero, the zero output block remains and is not normalized.
**BY** D1706.

<1>9. Common source and target are essential: without them the sum `C` and
the repeated output family in `<1>1` would not have one type.
**BY** D1706's instrument prescription.

<1>10. **QED** retained-outcome typing, normalization, and probabilities.
**BY** `<1>1`--`<1>9` and SP-WAT18 `paper.txt` 5106--5184.

## 4. Sequential and independent instruments

**ASSUME** instruments `(Phi_o)_(o in O):B_X->B_Y` and
`(Psi_r)_(r in R):B_Y->B_Z`.  **PROVE** D1706's sequential family retains
the ordered outcome pair and sums to a channel.

<1>1. The prescribed family is

    (Psi_r o Phi_o)_((o,r) in O times R),

where the first component is the earlier outcome.
**BY** D1706.

<1>2. Every member is a branch by section 1.
**BY** both factors are branches.

<1>3. Finite bilinearity of composition gives

    sum_(o,r) Psi_r o Phi_o
      =(sum_r Psi_r) o (sum_o Phi_o).

**BY** evaluate both sides on an arbitrary input and distribute the finite
sums.

<1>4. Both channel sums on the right are channels, so their composite is a
channel by section 1.
**BY** the two instrument hypotheses and section 1 `<1>7`.

<1>5. Retaining this sequential instrument gives blocks indexed by
`((o,r),c)`: neither `o` nor `r` becomes a hidden Kraus index.
**BY** D1706's ordered pair and outcome-first retained block prescriptions.

<1>6. Therefore the sequential family is an instrument retaining the
ordered pair of outcomes, and summing those pairs gives a channel.
**BY** `<1>1`--`<1>5`.

<1>7. Now let `(Theta_s)_(s in S):B_(X')->B_(Y')` be independent.  D1706
prescribes tensor outcomes `(o,s)` in listed-factor order and branches
`Phi_o tensor Theta_s`.
**BY** D1706.

<1>8. Each tensor member is a branch by section 2, and

    sum_(o,s) Phi_o tensor Theta_s
      =(sum_o Phi_o) tensor (sum_s Theta_s)

is a channel.
**BY** finite bilinearity, section 2, and the two channel-sum hypotheses.

<1>9. Thus independent instruments tensor to an instrument with every
ordered outcome pair retained.
**BY** `<1>7`--`<1>8`.

<1>10. **QED** sequential and tensor instrument closure.
**BY** `<1>1`--`<1>9`.

## 5. The ordinary-trace adjoint for every linear block map

**ASSUME** an arbitrary complex-linear map `Phi:B_X->B_Y`, without a CP
hypothesis.  **PROVE** the ordinary-trace adjoint prescribed by D1706 exists
and is unique.

<1>1. Choose orthonormal bases in every `H_a,K_b`.  Let
`E^a_(mu nu)` be the matrix units of input block `a` and
`F^b_(alpha beta)` the matrix units of output block `b`, each extended by
zero in every other direct-sum block.
**BY** finite-dimensionality and D1706's block families.

<1>2. These matrix units are orthonormal for the respective ordinary
Hilbert--Schmidt pairings:

    Tr_X((E^a_(mu nu))^* E^(a')_(mu' nu'))
      =[a=a'][mu=mu'][nu=nu']

and likewise for the `F` units.
**BY** direct matrix multiplication and ordinary block trace.

<1>3. Write the unique coefficient expansion

    Phi(E^a_(mu nu))
      =sum_(b,alpha,beta) C_((b,alpha,beta),(a,mu,nu))
         F^b_(alpha beta).

**BY** the output matrix units form a finite complex basis.

<1>4. Define a complex-linear map on output matrix units by

    Phi^(tr*)(F^b_(alpha beta))
      =sum_(a,mu,nu)
        conjugate(C_((b,alpha,beta),(a,mu,nu))) E^a_(mu nu),

and extend linearly.
**BY** a prescription on a finite basis defines one complex-linear map; its
coefficient matrix is the conjugate transpose of Phi's coefficient matrix.

<1>5. For input and output matrix units, the D1706 adjoint identity holds:

    <F^b_(alpha beta),Phi(E^a_(mu nu))>_Y
      =<Phi^(tr*)(F^b_(alpha beta)),E^a_(mu nu)>_X.

**BY** `<1>2`--`<1>4`; both sides equal the coefficient
`C_((b,alpha,beta),(a,mu,nu))` because the pairing is conjugate-linear in
its first argument.

<1>6. Bilinearity in the second variable and conjugate-linearity in the
first extend `<1>5` to every `x in B_X`, `y in B_Y`.
**BY** the two matrix-unit bases.

<1>7. If two maps satisfy the adjoint identity, their difference `D(y)` has
`<D(y),x>_X=0` for every `x`; choosing `x=D(y)` gives `D(y)=0`.
**BY** positive definiteness of the finite Hilbert--Schmidt pairing.

<1>8. Thus the map in `<1>4` is the unique D1706 ordinary-trace adjoint for
every complex-linear `Phi`.
**BY** `<1>4`--`<1>7`, matching SP-WAT18 `paper.txt` 1097--1105.

<1>9. **QED** general existence and uniqueness before CP specialization.
**BY** `<1>8`.

## 6. CP specialization of the ordinary-trace adjoint

**ASSUME** a D1706 CP map `Phi:B_X->B_Y` with Kraus family
`K_(b a,j)`.  **PROVE** the prescribed reverse-direction adjoint is CP,
has the stated Kraus formula, and is unital for a channel.

<1>1. For `x in B_X`, `y in B_Y`, expand the ordinary block pairing:

    sum_b Tr(y_b^*Phi(x)_b)
      =sum_(a,b,j)Tr(y_b^*K_(b a,j)x_aK_(b a,j)^*).

**BY** D1706.

<1>2. Rectangular trace reordering gives

    Tr(y_b^*Kx_aK^*)=Tr((K^*y_bK)^*x_a).

**BY** finite matrix indices, or `scalar.md` section 2 applied after taking
adjoints.

<1>3. By uniqueness in D1706's nondegenerate Hilbert--Schmidt pairing,

    (Phi^(tr*)(y))_a=sum_(b,j)K_(b a,j)^*y_bK_(b a,j).

**BY** `<1>1`--`<1>2`; matrix units show the pairing is nondegenerate.

<1>4. This is a finite block Kraus formula in the reverse direction, with
Kraus operators `K_(b a,j)^*:K_b->H_a`, so `Phi^(tr*)` is CP.
**BY** `process-kraus-blocks.md` section 1.

<1>5. At the output identity `1_Y=(1_(K_b))_b`,

    (Phi^(tr*)(1_Y))_a
      =sum_(b,j)K_(b a,j)^*K_(b a,j)=A_a.

**BY** `<1>3` and the effect notation of `process-kraus-blocks.md`.

<1>6. Therefore a branch has a subunital adjoint, and a channel has a
unital adjoint.
**BY** `A_a<=1` for branches and `A_a=1` for channels, from
`process-kraus-blocks.md` sections 4--5.

<1>7. Conversely, for a CP map with a Kraus presentation, subunitality of
the adjoint is equivalent to the D1706 branch inequalities, and unitality is
equivalent to channel completeness.
**BY** `<1>5` and `process-kraus-blocks.md` sections 4--5.

<1>8. This is the direct-sum version of SP-WAT18 Theorem 2.26
(`paper.txt` 4020--4097).
**BY** the pinned source and `<1>3`--`<1>7`.

<1>9. **PROVE** the adjoint need not be a reverse branch.

  <2>1. On a two-dimensional Hilbert space with basis `e_0,e_1`, ordinary
  discard `D:End(C^2)->C` has Kraus rows `e_0^*,e_1^*` and
  `D(rho)=Tr(rho)`.
  **BY** direct matrix entries, matching admitted FRP-CP `<1>10`.

  <2>2. It is a channel because
  `e_0e_0^*+e_1e_1^*=1_(C^2)` in the source effect.
  **BY** `process-kraus-blocks.md` section 5.

  <2>3. Formula `<1>3` gives `D^(tr*)(lambda)=lambda 1_(C^2)`, which is CP
  and unital.
  **BY** the two reverse Kraus columns.

  <2>4. On the positive scalar `1`, the input ordinary trace is one but the
  output ordinary trace is `Tr(1_(C^2))=2`; hence `D^(tr*)` is not TNI.
  **BY** D1706's ordinary trace.

  <2>5. **QED** `<1>9`.

<1>10. Thus D1706's trace adjoint reverses direction as an ambient CP map;
it does not supply an automatic CP dagger on the branch category.
**BY** `<1>4`, `<1>6`, and `<1>9`.

<1>11. **QED** the exact adjoint clause and its type boundary.
**BY** `<1>1`--`<1>10`.

## 7. Reuse and source-equality boundary

**PROVE** admitted FRP-CP embeds into these ambient formulas at its exact
scope without changing source equality.

<1>1. FRP-CP `<1>6`--`<1>9` already proves Kraus CP, ordinary-trace
nonincrease, composition, and tensor for realized source-certified
arithmetic amplitudes.
**BY** the admitted local proof.

<1>2. FRP-CP `<1>10` gives normalized arithmetic basis preparations and
ordinary discard, and `<1>12` retains external tags by explicit typed
families.
**BY** the admitted local proof and D1327.

<1>3. These are instances of sections 1--6 after replacing each abstract
Kraus operator by the Hilbert realization of its arithmetic amplitude.
**BY** D1326, D1706, and the displayed formulas in this shard.

<1>4. D1325 equality still retains its hidden index sets up to bijection,
source-amplitude equality, and external outcome tags.  Equal D1706 maps do
not become equal D1325 arrows merely because their CP realizations agree.
**BY** D1325 and admitted FRP-CP `<1>11`.

<1>5. Conversely, intrinsic Kraus exhaustion in `process-kraus-blocks.md` gives no
arithmetic source term for an arbitrary ambient branch.
**BY** D1706's Scope and the direction of section 2 in that shard.

<1>6. **QED** the admitted-reuse and source-equality boundary.
**BY** `<1>1`--`<1>5`.

## 8. Exact canonical conclusion

<1>1. Branches and channels compose and tensor with D1706's stated
ordinary-trace normalizations, including entangled tensor inputs.
**BY** sections 1--2 and `process-kraus-blocks.md`.

<1>2. Instruments have common types, retain outcome-first blocks without an
outcome-count factor, compose with earlier/later pairs `(o,r)`, tensor with
listed-factor pairs `(o,s)`, and sum to channels.
**BY** sections 3--4.

<1>3. The trace adjoint reverses direction as a CP map; a channel has a
unital adjoint, which need not be a reverse trace-nonincreasing branch.
**BY** sections 5--6.

<1>4. The ambient result neither changes D1325 equality nor asserts source
exhaustion.
**BY** section 7.

<1>5. **QED** the remaining exact canonical SP-CP clauses.
**BY** `<1>1`--`<1>4`, D1325--D1327, D1706, admitted FRP-CP and the pinned
SP-WAT18 results at their cited scope.
