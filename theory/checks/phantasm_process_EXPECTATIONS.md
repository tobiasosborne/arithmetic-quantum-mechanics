<!-- ROLE: pre-registration for the independent SP-SCALAR/SP-CP exact
     falsifier. Written before this lane's checker existed and without reading
     any process prover artifact. -->

# EXPECTATIONS — representatives, branches, and retained outcomes

Date: 2026-09-10. Lane: `phantasm-processes/checker`.
Model: `gpt-5.6-sol`, reasoning setting `xhigh`.

This is an exact finite falsifier, not a proof or promotion.  Every scalar is
represented in `Q(i)` as a pair of `Fraction` values; matrices, superoperators,
Choi matrices, traces and probabilities are exact.  No floating value or
tolerance is permitted.  The finite controls use dimensions at most three and
do not prove the arbitrary finite-dimensional statements.

The checker distinguishes D1705 projective amplitude classes, actual linear
representatives, CP maps, D1706 trace-nonincreasing branches and normalized
channels.  It constructs no normalized lift from a projective class and makes
no arithmetic/stabilizer source-exhaustion claim.

## Independent computational routes

The production map applies actual Kraus matrices by dense multiplication:

    Phi(rho)_b = sum_(a,j) K_(ba,j) rho_a K_(ba,j)^*.

Its matrix-unit oracle independently assembles superoperator coefficients

    Phi_(uv,ij) = sum_j K_(u,i) conjugate(K_(v,j))

for each input/output block and decodes those coefficients on a full
matrix-unit basis.  Composition and tensor build new path-labelled Kraus data,
then compare their production action with composition/tensor of the original
maps on every matrix unit.

The CP oracle does not rebuild the Kraus Gram expression.  For each block
component it evaluates the production map on matrix units, assembles the Choi
matrix in output/input order, and verifies Hermiticity and every principal
minor by exact Gaussian-rational determinants.  Nonnegative real principal
minors are the independent PSD criterion.  Completeness uses separately
formed `sum K^*K` matrices and exact PSD tests of their deficits.

The ordinary-trace adjoint is checked independently through the
Hilbert--Schmidt pairing on rectangular matrix-unit bases.  A mutation that
would use `K y K^*` is represented as an actual forward-typed map `X->Y`; the
gate rejects its type against the required reverse map `Y->X`.  No rectangular
matrix multiplication is attempted accidentally.

## P1 — scalar representatives and CP maps

On `C^3`, use

    I_3,  diag(1,0,0),  diag(1,1/2,0)

and scalars `0,1/2,2,i`.  On all nine matrix units check

    Phi_(cT) = |c|^2 Phi_T,

with exact modulus squares `0,1/4,4,1`.  In particular phase `i` fixes the CP
map, while `T` and `2T` give different actual maps for nonzero `T` although
they represent one D1705 projective amplitude class.

## P2 — contraction iff and zero conditioning

Use the three P1 operators together with `2I_3` and zero.  Their `T^*T<=I`
values are respectively true, true, true, false and true.  Compare this exact
PSD deficit criterion with trace nonincrease on rank-one inputs from every
nonzero vector in `{-1,0,1}^3`, plus the standard basis and rational mixed
vectors.  The zero map has output probability zero.  Conditional normalization
returns an explicit undefined-at-zero datum; the zero-conditioning mutation
returns an attempted-conditioning datum and is rejected by P2 without any
division.

## P3 — intrinsic block Kraus controls

Take `X=(C,C^2)` and `Y=(C^2,C)`.  For the scalar input block use Kraus
operators `(3/5)|0>` and `(4/5)` to the two output blocks.  For the two-vector
input use `(1/2)I_2` into the first block and `(1/3)<0|` into the second.
For every component and matrix unit:

- dense Kraus action equals the independent superoperator-coefficient route;
- the Choi matrix assembled from actual map outputs is exactly PSD;
- each per-input completeness deficit is PSD, with equality on the scalar
  input and strict inequality on the two-vector input.

The forward map is typed `X->Y`.  Replacing each Kraus operator by its adjoint
produces a reverse-typed `Y->X` map, so the adjoint-order mutation fails the
declared forward type as a mathematical mismatch.

## P4 — ordinary block trace

Use the channel `M_2 -> M_2 direct-sum C` with Kraus operators `(3/5)I_2`
to the first block and `(4/5)<0|,(4/5)<1|` to the second.  Completeness is

    (9/25)I_2 + (16/25)I_2 = I_2.

The maximally mixed rational density sends ordinary trace `1` to
`9/25+16/25=1`.  Dividing only the first output block trace by two gives
`9/50+16/25=41/50`, so the normalized-block-trace mutation must fail.

## P5 — equality of maps, not Kraus lists

The Kraus lists `{I_2}` and `{(3/5)I_2,(4/5)I_2}` are syntactically distinct
but induce the same map on all four matrix units.  D1706 equality accepts
them.  A list-equality mutation changes the actual equality relation and must
reject this pair.

## P6 — composition, tensor, and hidden/block tags

For composition, use one scalar input, two intermediate scalar blocks and one
scalar output.  Preparation amplitudes `3/5,4/5` feed the intermediate blocks,
each of which is discarded by the identity scalar.  Correct composite path
labels `(b,j,t)` retain both contributions and give the identity scalar
channel.  Omitting `b` collides the two actual path keys and loses one term.

Also compose rational preparation, dephasing and discard maps and compare the
constructed lists against successive actual action on full matrix-unit bases.
For tensor, use distinctly named block tags and compare the actual tensor-list
map with the independent Kronecker action on all matrix units.  Source tags
are `(a,c)`, target tags `(b,d)`.  Reversing one actual target pair while
leaving its matrix factor order fixed must fail the typed tag/map comparison.

## P7 — retained instruments

On `M_2`, the branches with scalar Kraus operators `(3/5)I_2` and `(4/5)I_2`
sum to the identity channel.  The retained target has exactly the two
outcome-first blocks `('red','q')`, `('blue','q')`; its ordinary trace on every
rational density is one.  Dropping the outcome merges the two actual blocks.
Multiplying retained trace by `|O|=2` gives two and is rejected separately.

## P8 — sequential outcome order

Follow `O=('red','blue')`, with amplitudes `3/5,4/5`, by
`R=('left','right')`, with amplitudes `5/13,12/13`.  The four retained keys in
earlier/later order are

    (red,left), (red,right), (blue,left), (blue,right).

Their probabilities are exactly
`9/169,1296/4225,16/169,2304/4225`, summing to one.  Hiding the first outcome
produces only two later-outcome blocks; reversing pairs produces four
different actual keys `(r,o)`.  Both mutations operate on the sequential
instrument construction.

## P9 — tensor outcome order

Tensor the two instruments from P8 independently.  The four listed-factor
outcomes are `(o,s)`, with branch maps equal to the Kronecker products and
total trace one.  Reversing only the actual outcome pair to `(s,o)` while
retaining matrix tensor order must fail the typed outcome comparison.

## P10 — ordinary-trace adjoint and its boundary

For P3's rectangular block map, compare the explicit reverse Kraus list
`K^*` against the ordinary Hilbert--Schmidt pairing on every compatible pair
of source/target matrix units, including a Gaussian-rational phase matrix.
The adjoint is CP and reverse typed; a channel has unital adjoint and a branch
has subunital adjoint.

For discard `Tr:M_2->C`, the actual adjoint maps `lambda` to `lambda I_2`.
It sends the scalar density of trace one to `I_2`, of trace two, so it is
unital but not trace-nonincreasing.  A mutation that classifies it as a D1706
reverse branch must fail this actual trace witness.

## P11 — admitted arithmetic comparison boundary

Run D1327-style basis preparations `C->C^2`, the two-Kraus ordinary discard,
and a two-outcome retained decoder through the ambient formulas.  Preserve
outcome tags and compare actual matrix-unit maps.  Two distinct source-arrow
records carrying `{I}` and `{(3/5)I,(4/5)I}` realize the same CP map but remain
unequal under D1325's finer source equality.  The source-equals-CP mutation
changes that actual source equality relation and must fail.

## Green gates and advertised mutation map

| gate | green scope | actual-data mutation(s) first rejected there |
|---|---|---|
| `P1` | scalar modulus and representative/projective distinction | `scalar-modulus`, `projective-branch` |
| `P2` | contraction iff and explicit zero-conditioning boundary | `contraction-reverse`, `zero-conditioning` |
| `P3` | block matrix-unit/Choi/completeness and rectangular typing | `kraus-adjoint-order` |
| `P4` | ordinary block trace | `block-normalized-trace` |
| `P5` | actual CP-map equality | `kraus-list-equality` |
| `P6` | composition/tensor action and block/path tags | `composite-index-loss`, `tensor-tag-order` |
| `P7` | outcome-first retained instrument and trace | `retained-drop-outcome`, `retained-outcome-factor` |
| `P8` | earlier/later sequential outcomes and channel sum | `sequential-hide-first`, `sequential-pair-order` |
| `P9` | listed-factor tensor outcomes | `tensor-outcome-order` |
| `P10` | trace adjoint, unital/subunital and non-TNI discard adjoint | `adjoint-direction`, `adjoint-is-branch` |
| `P11` | D1327 ambient instances with source equality retained | `source-equals-cp` |

The pre-repair executable was required to expose exactly these seventeen
no-argument flags:

`--red-scalar-modulus`, `--red-projective-branch`,
`--red-contraction-reverse`, `--red-zero-conditioning`,
`--red-kraus-adjoint-order`, `--red-kraus-list-equality`,
`--red-block-normalized-trace`, `--red-composite-index-loss`,
`--red-tensor-tag-order`, `--red-tensor-outcome-order`,
`--red-retained-drop-outcome`, `--red-retained-outcome-factor`,
`--red-sequential-hide-first`, `--red-sequential-pair-order`,
`--red-adjoint-direction`, `--red-adjoint-is-branch`, and
`--red-source-equals-cp`.

Every mutation changes actual matrix, type, path, tag, trace, conditioning or
equality data used by its gate.  No generic `--red NAME` appears in help.  A
caught red exits `1` at its registered gate, a surviving red exits `0`, and
bad usage, unexpected exception or wrong-gate failure exits `2`.  All
seventeen red paths must be observed before the first pre-repair green.  A later
temporary disabled-comparison control must make one actual mutation survive
with exit `0`; source is restored afterward.

The checker may reuse only exact standard-library arithmetic.  A green result
cannot prove intrinsic Kraus exhaustion in arbitrary dimensions, establish a
normalized stabilizer lift, identify D1325 source equality with CP equality,
or supply global arithmetic dynamics.

## Sole checker repair wave — OBJ3 pre-registration

The valid blind verdict found one checker-only coverage gap: P3's existing
`kraus-adjoint-order` mutation correctly exercises the rectangular direction
boundary but stops before the coefficient, Choi and completeness paths.  The
following two actual-data modes are registered before the repair code:

| flag | actual mutation | intended first subcheck |
|---|---|---|
| `--red-kraus-forward-transpose` | preserve the declared `X->Y` type but make the actual `x1->y0` forward component apply its input matrix transposed before `K rho K^*` | `P3a coefficient-action` |
| `--red-kraus-overcomplete` | replace the actual `x1->y0` Kraus operator `(1/2)I_2` by `2I_2` in both production and coefficient/Choi routes | `P3c completeness` |

The first mutation must reach an off-diagonal `x1` matrix unit and disagree
with the independently assembled superoperator coefficients while remaining
forward typed.  The second must pass every P3a coefficient comparison and all
four P3b Choi PSD checks, then fail P3c because its actual per-input effect is
overcomplete.  Neither is an isolated preflight or expected-count mutation.

The original rectangular `kraus-adjoint-order` mode remains the P3 type
boundary.  Final help must expose exactly nineteen supported flags.  Both new
reds must be observed before repaired green; all nineteen modes must later
exit `1` at their registered gates.  For the survival control, temporarily
disable only P3c: with the overcomplete actual Kraus operator retained,
`kraus-overcomplete` must exit `0`; restoring P3c must return exit `1`.
