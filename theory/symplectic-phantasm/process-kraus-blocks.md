# Intrinsic CP and trace conditions on finite block families

Lane model: `gpt-5.6-sol`, reasoning `xhigh`.

Admitted proof of the intrinsic Kraus clause of SP-CP; see
`theory/verdicts/phantasm-processes-adjudication.md`.  Canonical definitions are D1325--D1327 and D1706; admitted FRP-CP
is reused only for its finite matrix calculations.  SP-WAT18 Theorem 2.22
(`paper.txt` 3785--3808) is explicitly stated for a nonzero map.  The proof
applies it only to nonzero block components and supplies empty Kraus lists
for zero components.

Fix finite nonempty families `X=(H_a)_(a in A)` and
`Y=(K_b)_(b in B)` of nonzero finite-dimensional Hilbert spaces.  Let

    B_X=direct-sum_a End(H_a),
    B_Y=direct-sum_b End(K_b)

with D1706's sums of ordinary traces.

## 1. A D1706 Kraus family is completely positive

**ASSUME** finite operators `K_(b a,j):H_a->K_b` and define

    Phi(rho)_b=sum_(a,j) K_(b a,j) rho_a K_(b a,j)^*.

**PROVE** `Phi:B_X->B_Y` is completely positive, without yet assuming the
trace inequality.

<1>1. Let `E` be any finite-dimensional auxiliary Hilbert space.  Under the
canonical distribution over blocks,

    End(E) tensor B_X = direct-sum_a End(E tensor H_a)

and similarly for `Y`.
**BY** map elementary matrix units to blockwise tensor matrix units, as in
admitted FRP-CP step `<1>9.<2>1`.

<1>2. A positive amplified input is therefore a family
`R=(R_a)` with each `R_a>=0` on `E tensor H_a`.
**BY** positivity in a finite direct sum is blockwise: a negative quadratic
form in one block extends by zero, and the converse is the sum of the
nonnegative block quadratic forms.

<1>3. The amplified output block `b` is

    sum_(a,j) (1_E tensor K_(b a,j)) R_a
      (1_E tensor K_(b a,j))^*.

**BY** the displayed Kraus formula on elementary tensors and linearity.

<1>4. Every summand in `<1>3` is positive.
**BY** for a vector `z`, its quadratic form is the quadratic form of `R_a`
at `(1_E tensor K)^*z`.

<1>5. Finite sums are positive, so every output block and hence the direct
sum output are positive.
**BY** `<1>2`--`<1>4`.

<1>6. Since `E` was arbitrary, `Phi` is completely positive.
**BY** the CP definition in SP-WAT18 lines 1148--1152.

<1>7. Empty individual lists and the globally zero map are included: their
contributions are empty sums and zero positive blocks.
**BY** finite-sum conventions and `<1>3`.

<1>8. **QED** the forward Kraus-to-CP implication.
**BY** `<1>1`--`<1>7`, reusing admitted FRP-CP `<1>6` at its actual matrix
scope.

## 2. Every intrinsic block CP map has D1706 Kraus lists

**ASSUME** a complex-linear completely positive map `Phi:B_X->B_Y`.
For each `a,b`, let `iota_a` insert one matrix into block `a`, let `pi_b`
select output block `b`, and put

    Phi_(b a)=pi_b o Phi o iota_a:End(H_a)->End(K_b).

**PROVE** finite D1706 Kraus lists reassemble `Phi`.

<1>1. Every amplification of `iota_a` inserts a positive matrix as one
positive block and zeros elsewhere; every amplification of `pi_b` selects a
positive block.  Thus both maps are CP.
**BY** the blockwise positivity calculation in section 1 `<1>2`.

<1>2. Composition of CP maps is CP, so every `Phi_(b a)` is CP.
**BY** compose their positive amplifications at each auxiliary dimension.

<1>3. If `Phi_(b a)` is nonzero, SP-WAT18 Theorem 2.22 gives a finite
family `K_(b a,j):H_a->K_b` with

    Phi_(b a)(x)=sum_j K_(b a,j)xK_(b a,j)^*.

**BY** the theorem's nonzero hypothesis is satisfied for precisely this
case; finite dimensionality is part of the standing assumptions.

<1>4. If `Phi_(b a)=0`, choose the empty Kraus list; its sum is the zero
map.
**BY** the empty-sum convention, independently of Theorem 2.22.

<1>5. There are finitely many component pairs and every chosen list is
finite, so the combined block family is finite.
**BY** finiteness of `A,B` and `<1>3`--`<1>4`.

<1>6. Every `rho in B_X` decomposes as

    rho=sum_a iota_a(rho_a),

and therefore

    Phi(rho)_b=sum_a Phi_(b a)(rho_a)
      =sum_(a,j)K_(b a,j)rho_aK_(b a,j)^*.

**BY** direct-sum decomposition, linearity, and `<1>3`--`<1>4`.

<1>7. Thus the selected component lists form a D1706 Kraus presentation of
the original actual map.
**BY** `<1>5`--`<1>6`.

<1>8. **QED** CP-to-block-Kraus exhaustion, including all zero components.
**BY** `<1>1`--`<1>7`.

## 3. Ordinary block trace and the per-input effect

**ASSUME** a Kraus presentation of `Phi`.  For every input block define

    A_a=sum_(b,j) K_(b a,j)^*K_(b a,j) in End(H_a).

**PROVE**

    Tr_Y(Phi(rho))=sum_a Tr_(H_a)(A_a rho_a).

<1>1. Expanding D1706's trace gives

    Tr_Y(Phi(rho))
      =sum_(b,a,j)Tr_(K_b)(K_(b a,j)rho_aK_(b a,j)^*).

**BY** D1706 and finiteness of every index set.

<1>2. For each rectangular `K:H_a->K_b`,

    Tr_(K_b)(K rho K^*)=Tr_(H_a)(K^*K rho).

**BY** the explicit rectangular index calculation in `scalar.md` section 2,
equivalently admitted FRP-CP `<1>7.<2>1`.

<1>3. Applying `<1>2` termwise and collecting the finite sum at fixed `a`
gives the claimed formula.
**BY** `<1>1`--`<1>2` and the definition of `A_a`.

<1>4. Every `A_a` is positive.
**BY** it is a finite sum of operators `K^*K` with nonnegative quadratic
forms.

<1>5. **QED** the ordinary block-trace identity.
**BY** `<1>3`--`<1>4`.

## 4. Trace nonincrease if and only if every block effect is bounded by one

**PROVE** `Phi` is trace-nonincreasing on all positive elements exactly when

    A_a<=1_(H_a) for every a.

<1>1. Suppose the displayed inequalities hold and let `rho=(rho_a)>=0`.
For each block,

    Tr(A_a rho_a)<=Tr(rho_a).

**BY** apply `scalar.md` section 3 `<1>1`--`<1>3` with positive
`1-A_a`.

<1>2. Summing `<1>1` and using section 3 gives
`Tr_Y(Phi(rho))<=Tr_X(rho)`.
**BY** D1706's ordinary direct-sum trace.

<1>3. Conversely, assume trace nonincrease.  Fix one input tag `a`, choose
`x in H_a`, and take the positive input with block `|x><x|` at `a` and zero
in every other block.
**BY** blockwise positivity and D1706's direct-sum object.

<1>4. The assumed inequality and section 3 give

    <x,A_a x><=<x,x>.

**BY** the rank-one trace identity.

<1>5. Since `x` was arbitrary, `1_(H_a)-A_a>=0`.
**BY** the quadratic-form characterization of positive semidefinite
operators.

<1>6. Since `a` was arbitrary, every required block inequality holds.
**BY** `<1>3`--`<1>5`.

<1>7. **QED** the TNI iff-condition.
**BY** `<1>1`--`<1>6`.

## 5. Channels and equality in every input block

**PROVE** `Phi` preserves ordinary trace exactly when `A_a=1_(H_a)` for
every `a`.

<1>1. If every equality holds, section 3 gives

    Tr_Y(Phi(rho))=sum_a Tr(rho_a)=Tr_X(rho)

for every `rho`, so `Phi` is trace preserving.
**BY** section 3 and D1706.

<1>2. Conversely, suppose `Phi` is trace preserving.  Inputs supported on
one block and the rank-one calculation in section 4 give
`<x,A_a x>=<x,x>` for every `x`.
**BY** trace preservation and section 3.

<1>3. Thus `A_a=1_(H_a)` for every `a`.
**BY** apply the quadratic-form criterion to the Hermitian operator
`A_a-1` and its negative, or use polarization.

<1>4. The same conclusion is D1706's definition of a channel, so the
intrinsic trace-preserving and displayed completeness meanings agree.
**BY** D1706 and `<1>1`--`<1>3`.

<1>5. SP-WAT18 Theorem 2.26 (`paper.txt` 4020--4097) gives the matching
single-block trace-adjoint formulation; `process-instruments.md` derives its exact
D1706 block formula.
**BY** the pinned source, used only as comparison here.

<1>6. **QED** the channel criterion.
**BY** `<1>1`--`<1>5`.

## 6. Actual map equality, not Kraus-list equality

**PROVE** the intrinsic characterization is compatible with D1706 equality
and does not alter D1325 source equality.

<1>1. D1706 declares two branches equal exactly when their complex-linear
maps `B_X->B_Y` agree.
**BY** D1706.

<1>2. A Kraus list is therefore a presentation witnessing CP/TNI; it is not
retained arrow data in D1706.
**BY** D1706 and sections 1--4.

<1>3. For example, the one-element list `{K}` and the two-element list
`{(3/5)K,(4/5)K}` give the same actual CP map.
**BY** `(9/25+16/25)K rho K^*=K rho K^*` for every `rho`.

<1>4. D1325 instead retains hidden indices up to a label-preserving
bijection and equality of source amplitudes.  The two lists in `<1>3` need
not be equal there.
**BY** D1325 and admitted FRP-CP `<1>11`.

<1>5. Hence intrinsic Kraus exhaustion does not impose Kraus mixing or CP
equality on the arithmetic source, and it does not prove source fullness.
**BY** `<1>1`--`<1>4` and D1706's Scope.

<1>6. **QED** the equality boundary.
**BY** `<1>5`.

## 7. Exact shard conclusion

<1>1. A finite-block map has a D1706 Kraus presentation exactly when it is
completely positive, with zero component maps handled separately from the
nonzero hypothesis of SP-WAT18 Theorem 2.22.
**BY** sections 1--2.

<1>2. Such a map is TNI exactly under the per-input block inequalities and
is a channel exactly under per-input equalities.
**BY** sections 3--5.

<1>3. These are properties of actual maps, independent of a selected Kraus
presentation and without changing D1325 source equality.
**BY** section 6.

<1>4. **QED** the intrinsic Kraus/CP/TNI clause of canonical SP-CP.
**BY** `<1>1`--`<1>3`, D1325--D1327, D1706 and admitted FRP-CP at its
explicitly identified matrix scope.
