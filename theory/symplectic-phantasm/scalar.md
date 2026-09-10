# Scalar representatives and successful one-Kraus branches

Lane model: `gpt-5.6-sol`, reasoning `xhigh`.

Admitted proof of the corrected canonical SP-SCALAR statement.
Capped review and sole-repair dispositions are recorded in
`theory/verdicts/phantasm-processes-adjudication.md`.  Canonical definitions
are D1326 and D1704--D1706; the admitted dependency is FRP-CP.  SP-WAT18
Theorem 2.22 (`paper.txt` 3785--3808) supplies the finite-dimensional Kraus
characterization, while the proof below also gives the one-Kraus amplified
positivity directly.  Nothing assigns a preferred representative to a D1705
projective class.

Fix nonzero finite-dimensional complex Hilbert spaces `H,K`, a linear map
`T:H->K` (possibly the zero map), and `c in C`.  Put

    Phi_T(rho)=T rho T^*.

This is proof-local shorthand for the map in the canonical claim.

## 1. Complete positivity, including the zero operator

**PROVE** `Phi_T:End(H)->End(K)` is completely positive for every `T`.

<1>1. Let `E` be any finite-dimensional auxiliary Hilbert space and let
`R>=0` in `End(E tensor H)`.
**BY** the definition of complete positivity in SP-WAT18 lines 1148--1152.

<1>2. The amplification is

    (1_End(E) tensor Phi_T)(R)
      =(1_E tensor T) R (1_E tensor T)^*.

**BY** equality on elementary matrix tensors and linearity.

<1>3. For every `y in E tensor K`, its quadratic form is

    <y,(1_E tensor T)R(1_E tensor T)^*y>
      =<(1_E tensor T)^*y,R(1_E tensor T)^*y> >=0.

**BY** positivity of `R`.

<1>4. Hence every finite amplification is positive.
**BY** `<1>2`--`<1>3`.

<1>5. This includes `T=0`, when every amplification is the zero positive
map.  It does not rely on SP-WAT18 Theorem 2.22's explicit nonzero-map
hypothesis.
**BY** direct substitution in `<1>2`.

<1>6. **QED** complete positivity.
**BY** `<1>1`--`<1>5`; this is the one-Kraus specialization of admitted
FRP-CP step `<1>6` at arbitrary finite Hilbert scope.

## 2. Exact ordinary-trace formula

**ASSUME** `rho in End(H)`.  **PROVE**

    Tr_K(Phi_T(rho))=Tr_H(T^*T rho).

<1>1. Choose orthonormal bases and expand the left side:

    sum_i (T rho T^*)_(ii)
      =sum_(i,j,h) T_(ij) rho_(jh) conjugate(T_(ih)).

**BY** finite matrix multiplication and the definition of ordinary trace.

<1>2. Reordering the finite sum gives

    sum_(j,h) (sum_i conjugate(T_(ih))T_(ij)) rho_(jh)
      =Tr_H(T^*T rho).

**BY** the matrix entries of `T^*T`.

<1>3. Thus the formula holds for rectangular `T`; it is not a cyclic-trace
assertion between differently sized square matrices.
**BY** `<1>1`--`<1>2`.

<1>4. **QED** the trace formula.
**BY** `<1>3`, matching admitted FRP-CP step `<1>7.<2>1`.

## 3. Trace nonincrease if and only if contraction

**PROVE** `Phi_T` is trace-nonincreasing on positive operators exactly when
`T^*T<=1_H`.

<1>1. Suppose `T^*T<=1_H` and let `rho>=0`.  Put
`D=1_H-T^*T>=0`.
**BY** the operator-order assumption.

<1>2. One has `Tr(D rho)>=0`.
**BY** write `rho=S^*S`; then
`Tr(D rho)=Tr(S D S^*)`, and `SDS^*>=0` has nonnegative diagonal entries
and trace.

<1>3. The trace formula gives

    Tr(Phi_T(rho))=Tr(rho)-Tr(D rho)<=Tr(rho).

**BY** section 2 and `<1>2`.

<1>4. Conversely, suppose the displayed trace inequality holds for every
positive `rho`.  For arbitrary `x in H`, take `rho=|x><x|`.
**BY** a rank-one outer product is positive, including at `x=0`.

<1>5. The assumed inequality and section 2 give

    <x,T^*T x> <= <x,x>,

so `<x,(1_H-T^*T)x>>=0` for every `x`.
**BY** the trace of `A|x><x|` is `<x,Ax>`.

<1>6. Therefore `1_H-T^*T>=0`, i.e. `T^*T<=1_H`.
**BY** the quadratic-form characterization of positive semidefinite
operators.

<1>7. At `T=0`, `T^*T=0<=1_H` and the resulting zero branch is TNI.
**BY** direct substitution; the nonzero Hilbert hypotheses do not exclude a
rank-zero operator.

<1>8. **QED** the contraction iff-condition.
**BY** `<1>1`--`<1>7` and D1706's singleton-block branch convention.

## 4. Scalar law and its exact exceptions

**PROVE** `Phi_(cT)=|c|^2 Phi_T` and determine when the actual maps agree.

<1>1. For every `rho`,

    Phi_(cT)(rho)=(cT)rho(cT)^*
      =c conjugate(c) T rho T^*=|c|^2 Phi_T(rho).

**BY** conjugate-linearity of the Hilbert adjoint.

<1>2. Hence phases do not change the CP map: if `|c|=1`, then
`Phi_(cT)=Phi_T` for every `T`.
**BY** `<1>1`.

<1>3. If `T!=0` and `|c|!=1`, then the two maps differ.
**BY** choose `x` with `Tx!=0`; on `|x><x|`, `Phi_T` is the nonzero outer
product `|Tx><Tx|`, and `<1>1` multiplies it by a scalar different from one.

<1>4. If `T=0`, every scalar multiple still gives the same zero CP map,
including when `|c|!=1`.
**BY** section 1 `<1>5`.

<1>5. For an admissible `T`, the success weight on a density `rho` scales
as

    Tr(Phi_(cT)(rho))=|c|^2 Tr(Phi_T(rho)).

**BY** `<1>1` and linearity of ordinary trace.

<1>6. If `c=0`, this weight is zero for every input and D1706 forbids
conditional normalization at that outcome.
**BY** `<1>1` and D1706's positive-probability condition.

<1>7. **QED** the scalar and phase clauses, with the `T=0` exception
explicit.
**BY** `<1>1`--`<1>6`.

## 5. Consequence for the all-invertible-scalar quotient

**ASSUME** a nonzero D1705 class `[T]`.  **PROVE** D1705 itself stipulates no
actual branch or probability, while either an admissible representative or
an added class-invariant normalization rule can specify a branch.

<1>1. D1705 identifies `T` with `cT` for every `c in C^times`, including
both unit-modulus and non-unit-modulus scalars.
**BY** D1705.

<1>2. Unit-modulus rescalings give the same CP map, but for `T!=0` every
rescaling with `|c|!=1` gives a different CP map and rescales every nonzero
success weight by `|c|^2`.
**BY** section 4 `<1>2`--`<1>5`.

<1>3. Thus the formula `rho |-> T rho T^*` does not descend from actual
representatives to a well-defined map on D1705 classes.
**BY** `<1>1`--`<1>2`.

<1>4. A chosen nonzero representative can be made contractive by replacing
it with `cT` for a sufficiently small nonzero `|c|`, but D1705 prescribes no
such scalar or normalization rule.
**BY** finite-dimensional boundedness gives `T^*T<=||T||^2 1`; choose
`0<|c|<=1/||T||` when `T!=0`.

<1>5. **PROVE** operator-norm normalization gives one possible
class-invariant branch rule on nonzero classes:

    N_[T](rho)=T rho T^*/||T||^2.

  <2>1. If `S=cT` with `c!=0`, then
  `||S||^2=|c|^2||T||^2` and
  `S rho S^*=|c|^2T rho T^*`.
  **BY** homogeneity of operator norm and section 4 `<1>1`.

  <2>2. Therefore `N_[S]=N_[T]`; the rule is independent of the chosen
  representative.
  **BY** cancellation in `<2>1`.

  <2>3. The normalized operator satisfies
  `(T/||T||)^*(T/||T||)<=1`, so `N_[T]` is a TNI CP branch.
  **BY** `T^*T<=||T||^2 1`, sections 1 and 3.

  <2>4. **QED** `<1>5`.

<1>6. Thus a branch can be specified either by choosing an actual
representative satisfying `T^*T<=1` or by adding an admissible
class-invariant rule such as `<1>5`.
**BY** sections 1 and 3, `<1>4`--`<1>5`.

<1>7. The separate zero class has representative `T=0` and gives the zero
branch; it is retained and never conditionally normalized.
**BY** D1705, sections 3--4, and D1706.

<1>8. D1705 itself stipulates neither method, an actual branch, nor a
probability.  In particular, the raw unnormalized formula in `<1>3` is not a
map on projective classes.
**BY** D1705's Scope and `<1>3`--`<1>7`.

<1>9. Compatibility of an added normalization rule with composition is a
separate obligation; no functorial lift or no-go theorem is proved here.
**BY** the canonical SP-SCALAR scope and the absence of a composition
calculation in `<1>1`--`<1>8`.

<1>10. **QED** the weakened scalar-quotient consequence.
**BY** `<1>1`--`<1>9`.

## 6. Exact canonical conclusion

<1>1. `Phi_T` is CP for every linear `T`, including `T=0`.
**BY** section 1.

<1>2. It is a D1706 TNI branch exactly when `T^*T<=1_H`.
**BY** sections 2--3.

<1>3. Scalar rescaling obeys `Phi_(cT)=|c|^2Phi_T`, with phases fixed and
the zero-operator exception recorded.
**BY** section 4.

<1>4. The scalar-quotient prescription stipulates no actual successful
branch or probability.  Either an admissible representative or an admissible
class-invariant normalization rule can specify a branch; phase changes alone
do not change it, and composition compatibility of an added rule is separate.
**BY** section 5.

<1>5. **QED** the exact canonical SP-SCALAR statement.
**BY** `<1>1`--`<1>4`, D1326 and D1704--D1706, and admitted FRP-CP at the
matrix-calculation scope explicitly cited above.
