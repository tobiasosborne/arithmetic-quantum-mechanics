<!-- ROLE: pre-registration for the independent SP-SUM exact falsifier.
     Written before this lane's checker existed and without reading any SP-SUM
     prover artifact or notes. -->

# EXPECTATIONS — coherent lists, tagged blocks, and dephasing

Date: 2026-09-10. Lane: `phantasm-sum/checker`.
Model: `gpt-5.6-sol`, reasoning setting `xhigh`.

This is an exact finite falsifier, not a proof or promotion.  The checker uses
integer/Fraction matrices only.  It works at `p=3`, ranks `0,1,2`, and selected
finite lists; a green result cannot prove the arbitrary-prime/rank/list claim.
It adds no biproduct, rig, Gaussian-closure, arithmetic-source or normalized
branch theorem.

Every dense matrix is stored with explicit `(rows,cols)` metadata as well as
entries.  In particular `0xn`, `nx0`, and `0x0` matrices remain distinct typed
maps even though their entry tuples can all be empty.  The D1703/D1704
rank-zero object `H_(F3,0)=C` has dimension one.  D1707's empty list realizes
the zero Hilbert space of dimension zero; these are never identified.

## U1 — actual rectangular matrix-unit words

For rank `n` and `x in F3^n`, tensor the one-register translations with the
actual vacuum to obtain the preparation column `e_x:C->H_n`; its adjoint is
the row `e_x^*`.  For ranks `(m,n)`, the actual composite

    E_(y,x)=e_y e_x^*:H_n->H_m

has shape `3^m x 3^n`, one entry equal to one at `(y,x)`, and all other
entries zero.  The number of these words is `3^(m+n)`, which is also the
coordinate dimension `rows*cols` of the rectangular Hom-space.

For all nine pairs `(m,n) in {0,1,2}^2`, Gaussian elimination on the flattened
actual matrices must give rank `rows*cols`; the expected rank is derived from
the explicit rectangular shape, not a separate literal.  Across all pairs the
checker constructs `(1+3+9)^2=169` matrix-unit words.  Rank-zero/rank-zero is
the actual scalar identity, not the empty-list endomorphism.

## U2 — coherent span versus the uncompleted stabilizer set

Import the installed exact qutrit stabilizer census, with its dependency hash
recorded in `RUNS.md`.  The matrix

    D_2=diag(1,1,0)=E_(0,0)+E_(1,1)

lies in the complex span constructed in U1.  It has rank two and is not
projectively equal to any of the 360 nonzero actual one-qutrit stabilizer
amplitudes (216 Clifford plus 144 rank-one classes) enumerated independently
by that checker.  This finite witness illustrates D1707's deliberate
enlargement; it does not classify pure stabilizer maps in general.

## U3 — D1707 block action, composition, and dagger

A finite list retains ordered positions even when model spaces repeat.  For a
block arrow `T:X->Y`, independently compare:

1. its prescribed dense block placement on the coherent direct sums; and
2. the tuple action `(xi_i)_i -> (sum_i T_(ji)xi_i)_j`, followed by tuple
   flattening.

Use source ranks `(0,1,1)` and target ranks `(1,0)`, with distinct rational
blocks, so the repeated qutrit positions cannot be merged.  Compose with a
second block arrow and verify that dense realization takes block-matrix
composition to ordinary rectangular multiplication.  Verify that adjoint
transpose realizes as the dense matrix adjoint.  An explicit off-diagonal
summand matrix unit must survive the coherent action; replacing the action by
diagonal/tagged action loses it.

## U4 — coherent/tagged dimensions and repeated positions

For a nonempty list of dimensions `(d_i)`, derive the coherent dimension by
enumerating all dense matrix units on `D=sum_i d_i`, and derive the tagged
dimension by enumerating only units whose row and column belong to the same
recorded summand.  Exact cases are:

| ranks | dimensions | coherent | tagged | off-diagonal |
|---|---|---:|---:|---:|
| `(0,1)` | `(1,3)` | 16 | 10 | 6 |
| `(0,0,1)` | `(1,1,3)` | 25 | 11 | 14 |
| `(1,1)` | `(3,3)` | 36 | 18 | 18 |
| `(2)` | `(9)` | 81 | 81 | 0 |

The dimensions are ranks of actual enumerated coordinate families.  Repeated
equal dimensions retain separate position projections and their cross-block
units.

## U5 — empty list and typed empty matrices

For `X=()` and nonempty `Y`, explicitly construct the unique block arrows
`X->Y`, `Y->X`, and `X->X`.  Their coherent matrices have respective shapes
`dim(Y)x0`, `0xdim(Y)`, and `0x0`; dagger swaps the first two shapes and all
typed compositions give the unique zero action.  The empty-list endomorphism
space and algebra have vector-space dimension zero.  The singleton rank-zero
list `(H_(F3,0))` instead realizes `C`, has a `1x1` identity, and has
one-dimensional endomorphism algebra.

No D1706 channel or branch is constructed on the zero Hilbert space.

## U6 — block dephasing on all matrix units

For `X=(C,C^3)`, let `P_0^X,P_1^X` be D1707's ordered summand projections
(never D1305's bare `P_i`).  On every one of the sixteen `4x4` matrix units,
compare the actual map

    Delta_X(A)=P_0^X A P_0^X+P_1^X A P_1^X

with an independent block-membership oracle.  It fixes the ten same-summand
units and kills the six off-diagonal units.  A mutation retaining one actual
cross term `P_0 A P_1` must fail on a named off-diagonal unit.

## U7 — channel data, idempotence, and exact range

From the actual projections verify

    sum_i (P_i^X)^*P_i^X=I_4,

and check unitality and idempotence of `Delta_X`.  Flatten its sixteen actual
matrix-unit images and compute image rank ten, equal to the independently
enumerated tagged coordinate family; check that every tagged basis unit is
fixed.  Omitting one projection fails completeness.  Dividing the actual
dephasing output by the two-block count preserves neither unitality nor
idempotence and is rejected separately.

## U8 — ordinary trace preservation

For every `4x4` matrix unit and several rational dense matrices, compare
`Tr(Delta_X(A))` with the ordinary coherent matrix trace.  Also sum the
ordinary traces of its diagonal blocks independently.  Replacing this by the
dimension-normalized block functional

    Tr(A_00)/1 + Tr(A_11)/3

changes the value on `I_4` from four to two and must fail.  This invokes
D1706/SP-CP only for the nonempty system.

## Advertised mutation map

Each mode changes actual preparation, census, realization, list, projection,
dephasing or trace data.  A red runs only its registered gate.

| flag | actual mutation | intended first gate |
|---|---|---|
| `--red-matrix-unit-loss` | delete the last actual rank-two preparation, hence all words needing it | `U1` |
| `--red-pure-two-unit` | insert `diag(1,1,0)` into the actual qutrit stabilizer census | `U2` |
| `--red-coherent-tagged` | erase off-diagonal blocks in the actual coherent realization | `U3` |
| `--red-merge-repeated` | identify equal-rank list positions before actual coordinate enumeration | `U4` |
| `--red-empty-vacuum` | realize the actual empty list as the one-dimensional rank-zero model | `U5` |
| `--red-dephase-offdiag` | add the actual cross term `P_0 A P_1` to dephasing | `U6` |
| `--red-projection-loss` | omit `P_1^X` from the actual Kraus/projection family | `U7` |
| `--red-dephase-average` | divide the actual two-block dephasing output by two | `U7` |
| `--red-normalized-trace` | replace ordinary trace by normalized summand traces | `U8` |

Expected exits: green `0`; caught red `1`; a red that survives its target gate
`0`, so session-close rejects it; invalid usage, exception or wrong-gate
failure `2`.  The pre-repair checker exposed only these nine no-argument
flags.  All were observed before its first green.  A temporary disabled-comparison control must
make one actual mutation survive with exit `0`, after which source is restored.

## Sole checker repair wave — census and projection propagation

The valid blind verdict found two checker-only MINOR issues.  This repair is
pre-registered before changing the executable.

U2 will first guard the imported actual census at its precise finite scope:
216 Clifford rays, 144 rank-one rays, and 360 pairwise projectively distinct
nonzero endomorphism rays.  The imported dependency hashes remain pinned in
`RUNS.md`.  Add the actual-data mode

| flag | actual mutation | intended first subcheck |
|---|---|---|
| `--red-census-loss` | truncate the imported actual endomorphism tuple before the census/distinctness guard | `U2a imported-census` |

The existing `pure-two-unit` mode must pass U2a, then append
`diag(1,1,0)` to the intact actual family and fail the separate U2b exclusion.
Temporarily disabling only U2a must make `census-loss` survive U2 and exit `0`;
restoring it must return exit `1`.

In U7, the shortened `used=projections[:-1]` family in `projection-loss` mode
will be passed to every actual dephasing call, not only the completeness sum.
Its first failure remains the U7a completeness guard.  As a reachability
control, temporarily disabling only U7a must make the same mutation proceed
to and fail U7b unitality, proving that the actual operation also lost the
projection.  This control is expected to exit `1` at the later named subcheck,
not survive.

Final help exposes exactly ten supported flags.  All ten must exit `1` at
their intended gates before final ordinary and optimized greens.
