<!-- ROLE: pre-registration for the independent SP-TRACE/SP-FROB/SP-SUBSYS
     exact falsifier. Written before implementation and without reading any
     arithmetic prover artifact or notes. -->

# EXPECTATIONS — arithmetic trace, relative Frobenius, and subsystems

Date: 2026-09-10. Lane: `phantasm-arithmetic/checker`.
Model: `gpt-5.6-sol`, reasoning setting `xhigh`.

This checker is finite negative-binding evidence only.  It uses exact finite
field tables, cyclotomic/Eisenstein coefficients and `Fraction` matrices; no
floating values or tolerances occur.  It does not prove the arbitrary-rank,
all-extension or compatible-subsystem claims, and supplies no characteristic-
two half-form, field-inclusion functor, support-code identification, global
assembly, modular flow or spectral result.

The implementation may import the existing exact `GF`, cyclotomic, Abelian
and monomial helpers.  `RUNS.md` must record their final hashes.  The existing
`phantasm_reuse_check.py` remains byte-unchanged and receives credit only for
its recorded R6 F81/F9 sample; A1--A12 below are new comparisons.

## Exact field data and independent routes

Use `F27=GF(3,3)` and `F81=GF(3,4)` from the audited polynomial-table
constructor.  Prime-field elements use their embedded constant encodings.

- For F27/F3, `Tr_27/3(x)=x+x^3+x^9`.  Its image has size 3, kernel size 9,
  every fiber size 9, and `Tr(1)=0`; a separately found element has trace 1.
- Inside F81, `F9={x:x^9=x}`.  `Tr_81/9(x)=x+x^9` has image and kernel size
  9.  Choose the first `u in F9` not fixed by cube and define
  `chi_9(y)=zeta_3^Tr_9/3(u y)`, where `Tr_9/3(y)=y+y^3`.
- The direct trace `x+x^3+x^9+x^27` and iterated trace
  `Tr_9/3(Tr_81/9(x))` are coded separately and compared on all 81 elements.

Restricted-form Gram matrices use coefficient bases found from actual unique
spans: `(1,alpha,alpha^2)` for F27/F3 and a verified `(1,beta)` for F81/F9.
All matrix ranks are computed by modular row reduction, not asserted from
their construction.

Half-form products are compared through two separately evaluated exponents:
first apply the relative character after the E-valued half-form; versus first
trace the symplectic value, take the K-half, and apply the named base
character.  Sparse monomial action computes products/star/unit and actual
operator traces without dense rank-two matrices.

Subsystem matrix maps use rational dense matrices of size at most 27 and a
separate Eisenstein `Q(zeta_3)` layer for Weyl characteristic traces.
Decoder action is computed both from actual Kraus rows and by independent
index partial trace.  Direct and tower decoders use separately coded
permutations.

## A1--A7 — trace and Frobenius expectations

### A1 — degree-divisible trace and restricted Gram ranks

Audit F27, check the trace census above, and verify that replacing trace by
degree multiplication gives the zero map.  For symplectic E-ranks 0,1,2,
form the F3 restricted Gram matrices on the actual coefficient basis.  Their
computed sizes/ranks are `(0,0)`, `(6,6)`, `(12,12)`.

### A2 — named character separation

The nonstandard F9 character is additive, nontrivial and differs from the
restricted fixed absolute F81 character on an explicit F9 witness.  Its
relative composite on F81 is nontrivial.  On F27, the fixed absolute trace
character restricts trivially to F3 because `Tr(1)=0`, while the named base
character `t->zeta_3^t` remains nontrivial.

### A3 — tower transitivity

For all F81 elements, direct and iterated trace routes agree and land in F3;
applying the nonstandard named character along both routes agrees.  Replacing
the F81/F9 stage by `x+x^3` is actual wrong trace data and must be rejected.

### A4 — half-form restriction

For F27/F3 and F81/F9 at ranks 0,1,2, compare both half-form exponent routes
on every restricted basis pair plus deterministic mixed labels.  Verify
abstract product, star, unit and coefficient trace, and sparse monomial product
and actual trace on the registered labels/basis states.  Omitting `1/2` only
on the restricted K-form route must fail.

### A5 — relative Frobenius

For F27/F3 use `sigma(x)=x^3`, order 3.  For F81/F9 use `sigma(x)=x^9`,
order 2.  Exhaustively check K-linearity, trace and named-character invariance,
symplecticity on field-label pairs and the declared power.  Substituting
absolute cube on F81 must fail K-linearity or its relative order.

### A6 — sparse Weyl covariance

For
`W(a,b)e_y=chi(-b(y+a)+ab/2)e_(y+a)`, compare conjugation by the basis
permutation with `W(sigma(a),sigma(b))`.  Exhaust every rank-one label and
basis state over F27 and F81.  At rank two, test every basis state for zero,
coordinate, mixed and cross-coordinate labels.  Hilbert dimensions are
`1,27,729` and `1,81,6561`; no dense rank-two matrix is allocated.  Applying
sigma only to the translation coordinate must fail the actual action tuple.

### A7 — rank zero and channel control

Rank zero uses the singleton basis, identity permutation and identity channel
on C.  At ranks one/two, the coordinatewise field permutation is bijective,
its declared period is identity, and its conjugation/inverse action preserves
ordinary trace on selected matrix units.  A qutrit placeholder for the empty
tensor must fail at rank zero.

## A8--A12 — subsystem expectations

### A8 — non-coordinate F3 geometry

With grouped phase labels `(a1,a2;b1,b2)`, use

    j(a,b)=(a,a;b,0),       k(u,v)=(0,u;-v,v).

Check both maps are injective symplectic, mutually orthogonal, and their 81
image sums give every V2 label uniquely.  The configuration-half map
`(a,b)->(a,b;0,0)` is degenerate and must fail.

### A9 — compatible model and ordinary decoder

Use the actual basis permutation `J|x1,x2>=|x1,x1+x2>`.  Exhaust all 81
rank-one Weyl-label pairs and nine basis states in the D1710 compatibility
equation.  From actual Kraus rows `(I tensor <e|)J^*`, check completeness,
action on all 81 V matrix units, ordinary trace preservation and trace duality
with `iota_J` on all qutrit matrix units.  Dividing the actual partial trace by
three must fail against the independent index trace.

### A10 — direction on correlated inputs

Transport through J the factor-coordinate states `|0,1><0,1|`,
`(1/3)sum_x|x,x><x,x|`, and
`(1/3)sum_(x,y)|x,x><y,y|`.  Correct decoding traces the complement and gives
respectively `|0><0|`, `I_3/3`, and `I_3/3` for the Bell density.  Tracing the
retained factor instead gives `|1><1|` on the asymmetric state and fails.

### A11 — Weyl restriction and phase cancellation

For all nine U Weyl labels and the three transported inputs, check

    Tr(D_J(rho)W_U(u))=Tr(rho W_V(j(u))).

Replacing J by `zeta_3 J` leaves both the observable inclusion and decoder
unchanged.  Applying the phase to only one occurrence of J/J* changes actual
Eisenstein matrix data and must fail.

### A12 — explicit compatible decoder tower

Use `M3(x1,x2,x3)=(x1,x1+x2,x1+x2+x3)`.  Verify the actual direct permutation
equals the two-stage route: first M2 on coordinates one/two, then add its
second output to coordinate three.  This is an explicit instance of D1710's
compatibility equation with reassociation and phase `lambda=1`; it does not
infer compatibility for arbitrary chosen model unitaries.

On selected matrix units, an asymmetric product, a classical correlated
state and a GHZ density, compare direct trace over the last two factor
coordinates with the sequential decoders.  Swapping the retained and first
discarded factor in the actual direct decoder must fail.

## Mutation map

| flag | actual mutation | first gate |
|---|---|---|
| `--red-trace-degree` | replace F27 trace by `3*x=0` | `A1` |
| `--red-character-conflation` | use the restricted fixed absolute character instead of named chi9 | `A2` |
| `--red-tower-order` | use `x+x^3` for the F81/F9 trace stage | `A3` |
| `--red-half-form-trace` | omit half on the restricted-form exponent route | `A4` |
| `--red-absolute-frobenius` | use cube instead of ninth power over F81/F9 | `A5` |
| `--red-half-coordinate` | apply sigma only to translation labels in covariance | `A6` |
| `--red-rank-zero` | replace the empty tensor identity by a qutrit permutation | `A7` |
| `--red-degenerate-subsystem` | use the configuration-half injection | `A8` |
| `--red-decoder-normalized-trace` | divide actual decoder output by three | `A9` |
| `--red-decoder-direction` | trace the retained factor | `A10` |
| `--red-decoder-phase` | phase only one J/J* occurrence | `A11` |
| `--red-decoder-tower-order` | retain the first discarded tower factor | `A12` |

Every mode changes actual trace, character, form, permutation, subsystem or
decoder data and runs only its registered gate.  Caught reds exit `1`, a red
surviving its gate exits `0`, and usage/unexpected/wrong-gate failures exit
`2`.  Help exposes exactly these twelve no-argument flags.  All reds must run
before first green.  Disabled-guard survival controls are required for A1,
A6, A9 and A12, after which final source is restored.

## Sole checker repair wave — A6 census guard

The valid blind verdict found one checker-only MINOR: A6 printed but did not
assert its executed census. Before repair implementation, register the exact
per-field/rank counts

    F27 rank 1:  19,683
    F27 rank 2:  12,393
    F81 rank 1: 531,441
    F81 rank 2:  85,293
    total:       648,810.

Every actual state collection must be nonempty. Add the actual-data mode

| flag | actual mutation | intended first gate |
|---|---|---|
| `--red-covariance-census-loss` | remove the final F81 rank-two basis state before running its real label/action loop | `A6` per-field/rank census guard |

The shortened state set must execute 85,280 rather than 85,293 F81 rank-two
comparisons while every remaining covariance equality still passes. The tuple
guard must reject observed `(19683,12393,531441,85280)`. On a temporary copy,
disabling only that guard must let the same actual mutation survive A6 with
exit `0` and report 648,797 executed cases. Final help exposes thirteen modes;
the previous twelve paths remain unchanged.
