<!-- ROLE: pre-registration for the independent SP-STAB-REL exact falsifier.
     Written before this lane's checker existed and without reading any
     stabilizer prover or source-audit lane artifact. -->

# EXPECTATIONS — projective stabilizer/relation comparison

Date: 2026-09-10. Lane: `phantasm-stabilizer/checker`.
Model: `gpt-5.6-sol`, reasoning setting `xhigh`.

This is an exact finite falsifier, not a proof or promotion.  The claim is
restricted to odd prime fields and quotients actual nonzero complex maps by
all of `C^times`, with the zero map in a separate class.  The exhaustive
comparison below is only for zero and one qutrit register over `F3`; selected
`F5` states and generators are a convention control.  No finite census proves
the general presentation, fullness, faithfulness, or essential surjectivity.

The checker may import exact `CycRing` arithmetic from the admitted Weyl
checker and the frozen classical affine-relation API from
`phantasm_relations_check.py`.  In its lane it may locate the latter at the
frozen lane path until the coordinator installs it; in the intended trunk
layout both imports must resolve from adjacent `theory/checks/` files.  No
floating-point number, normalization tolerance, or approximate phase is
permitted.

## Matrix and vectorization conventions

For `p=3` or `5`, use `psi(t)=zeta_p^t`, the D1703 half-form Weyl matrices

    W_m(a,b)e_y = psi(-b dot (y+a) + a dot b/2)e_(y+a),

where labels are stored as ordered symplectic blocks
`(a_1,b_1,...,a_m,b_m)` and Hilbert basis tuples are lexicographic.  The
unnormalized Fourier and lower-shear generators are

    F[x,y]=psi(x*y),
    D_r[x,x]=psi(-r*x^2/2).

Thus `F W(a,b) F^dagger = p W(b,-a)` and
`D_r W(a,b) D_r^dagger=W(a,b+r*a)`.  The Pauli matrices, `F`, and `D_1`
generate actual representatives; projective deduplication must use exact
cross-products of entries and may not divide by a selected matrix entry.

For `T:H_m->H_n`, vectorize in the ordered space
`conjugate(H_m) tensor H_n` by

    vec(T) = sum_x conjugate(e_x) tensor T e_x,

so `conjugate(W_m(v)) tensor W_n(w)` sends `vec(T)` to
`vec(W_n(w) T W_m(v)^dagger)`.  Unvectorization therefore reads coefficient
`(x,y)` as matrix entry `T[y,x]`.  This convention distinguishes operator
vectorization from a CP-map Choi operator; the checker constructs no CP map.

## Independently derived finite censuses

The one-register affine-relation counts, including zero, are inherited as
finite inputs from the independent classical enumeration:

| Hom-set | `F3` relation count | nonzero projective stabilizer amplitudes |
|---|---:|---:|
| `0->0` | 2 | 1 scalar class |
| `0->1` | 13 | `3(3+1)=12` stabilizer-state rays |
| `1->0` | 13 | 12 adjoint effect rays |
| `1->1` | 361 | `216+12^2=360` |

Here `|ASp(2,F3)|=3^2 |SL(2,F3)|=9*24=216`.  Actual qutrit matrices generated
projectively from Pauli `X,Z`, Fourier `F`, and shear `D_1` must give exactly
216 Clifford classes.  Their orbit on the actual computational preparation
`delta_0` must give 12 state rays.  The 144 outer products of ordered state
rays are pairwise distinct projectively and have rank one; none is a Clifford
class.  Hence the actual generated one-register amplitude census is
`216+144=360` nonzero classes, plus zero.  The checker derives these sets from
matrix multiplication and orbits, not from the relation catalog or its
counts.

For `F5`, `|ASp(2,F5)|=5^3(5^2-1)=3000` and the stabilizer-state orbit has
`5(5+1)=30` rays.  The economical F5 gate checks the 30 actual matrix-orbit
states against all 30 nonempty affine Lagrangian states, plus the Weyl,
Fourier, shear, computational-state and cup signs.  It does not enumerate the
full 3000-element Clifford group or all 3900 nonzero endomorphism classes.

## Relation-to-operator construction, pending canonical ownership

This paragraph pre-registers the proposed construction supplied to the lane;
implementation must wait until its canonical definition (expected D1715) is
available and must report any sign, origin, variance or factor-order mismatch.
For nonempty

    R = r+L subset bar(V_m) + V_n,

put `Omega=-omega_m+omega_n`.  The required nonzero operator line consists of
the solutions of

    W_n(w) T W_m(v)^dagger
      = psi(-Omega(r,(v,w))) T             for every (v,w) in L.

On `conjugate(H_m) tensor H_n`, the independently derived unnormalized
character projector is

    P_R = sum_((v,w) in L)
            psi(+Omega(r,(v,w)))
            conjugate(W_m(v)) tensor W_n(w).

Indeed left multiplication by the `(v,w)` action gives eigencharacter
`psi(-Omega(r,(v,w)))`.  A canonical computational-basis scan selects the
first nonzero column of `P_R`, then unvectorizes it.  The checker must verify
the eigen-equations directly using matrix multiplication, rather than using
the averaging helper to manufacture both sides.

If `r' = r+l_0` with `l_0 in L`, then
`Omega(r',l)=Omega(r,l)` because `L` is isotropic, so `P_R`, its first nonzero
column and the unvectorized representative are exactly origin-independent.
The empty relation maps to the zero matrix.  These two facts are checked from
actual alternate origins and matrix data.

## Projective comparison expectations

For equal-shaped matrices `A,B` over `Z[zeta_p]`, the checker treats two
nonzero matrices as projectively equal exactly when all entry cross-products
vanish:

    A_ij B_kl = B_ij A_kl.

It first verifies both matrices are nonzero and chooses an actual nonzero
anchor entry; zero is equal only to zero.  This tests proportionality by an
arbitrary nonzero complex scalar without adjoining quotients or square roots.
In particular `A` and `2A` are equal in D1705, while a phase-only mutation
must distinguish them.  Zero and the `1x1` identity are never equal.

For all 389 `F3` relations, the relation construction must produce exactly
the independently generated projective Hom-sets above, bijectively within
each type.  Graph relations land among the 216 Clifford classes; the other
144 nonzero one-register endomorphisms land among the state/effect outer
products.  This is a finite check of the proposed formula and selected
generator match, not a source-presentation theorem.

## Composition, dagger, tensor and compact cases

Characteristic two is outside this quantum comparison.  The exact F3 total is
140,101 composable ordered relation pairs across objects `{0,V_1}`.  For every
such pair,

    Q(S o R)  ~  Q(S) Q(R),

with exact zero equality when either side is zero and cross-product equality
otherwise.  This exhausts state/effect composites, including orthogonal
same-basis states whose composite is empty and nonzero overlaps with different
unnormalized magnitudes in the same scalar class.  It does not normalize a
branch or retain the number of middle witnesses.

For all 389 relations, `Q(R^dagger) ~ Q(R)^dagger`.  Tensor checks exhaust all
`13^2=169` state pairs and all 169 effect pairs, then use a fixed matrix-derived
sample containing zero, identity, Pauli/Fourier/shear graphs and rank-one
outer-product relations for one-register and mixed tensor cases.  With the
D1702 coordinate reorder and D1703 Hilbert identification,

    Q(R+S) ~ Q(R) tensor Q(S).

The compact cup is the name of the identity relation.  Under the registered
vectorization it maps to the unnormalized Bell vector
`sum_x conjugate(e_x) tensor e_x`; the cap is its dagger and their closed
composite is the actual scalar `p`, hence the unique nonzero class of D1705.
The checker keeps this scalar value visible even though the projective target
forgets it.

## D1715 registration alignment — before S3--S5 implementation

Canonical D1715 now owns the choice-free space `E_p(R)` and requires its Weyl
equation for every origin `r in R` and every direction `l in R-R`.  This is
exactly the convention above; no sign, variance, field, object, or
normalization change is needed.  For every nonempty F3 small relation, S3 will
check the displayed equation over the full Cartesian product `R x (R-R)`, and
will recompute the selected group-average column from every origin in `R`.

The unnormalized projector also supplies an exact finite line-dimension
certificate.  On the `p^(m+n)`-dimensional vectorized space, with
`|L|=p^(m+n)`, S3 expects

    P_R^2 = |L| P_R,       trace(P_R)=|L|.

Since the first identity gives eigenvalues in `{0,|L|}` over `C` and the
second gives rank one, this verifies the line statement for the enumerated
relations without a floating rank computation.  The empty case remains the
separate zero space.  These extra finite checks were registered after D1715
became canonical and before their implementation.

## Green gates

| gate | scope |
|---|---|
| `S1` | Exact Weyl/Fourier/shear matrices; independently generated qutrit projective Clifford group and stabilizer-state orbit; limited F5 state orbit |
| `S2` | Exact `C^times` cross-product quotient, zero separation, qutrit generated Hom-set censuses and explicit unequal-norm equality |
| `S3` | D1715 relation projector/eigen-equations, origin independence, empty map, and bijection with actual qutrit Hom sets; all F3 and selected F5 states |
| `S4` | All 140,101 F3 typed compositions and all 389 daggers, including empty/nonempty state-effect scalars |
| `S5` | State/effect tensors, selected graph/rank-one tensors, vectorized cup/cap and the retained closed scalar `p` |

## Pre-registered actual-data mutations

Every mode changes a matrix, generated family, quotient, averaging action or
diagram datum.  A red runs only its named gate for economy.

| mode | actual mutation | intended gate |
|---|---|---|
| `--red-weyl-sign` | build Weyl matrices with `+b` where D1703 has `-b` | `S1` |
| `--red-fourier-sign` | use Fourier kernel `psi(-xy)` while retaining `(a,b)->(b,-a)` | `S1` |
| `--red-drop-shear` | generate the actual qutrit projective Clifford family without `D_1` | `S1` |
| `--red-phase-only` | restrict D1705 equality to root-of-unity phases, so `A` and `2A` differ | `S2` |
| `--red-zero-collapse` | identify the actual zero matrix with a nonzero matrix class | `S2` |
| `--red-average-sign` | reverse the actual character coefficient in `P_R` | `S3` |
| `--red-origin-dependent` | add the coordinate dot character to the projector coefficient, making alternate origins differ | `S3` |
| `--red-fixed-seed` | use only the first computational seed even when its projected column is zero | `S3` |
| `--red-empty-nonzero` | map the actual empty relation to a nonzero matrix | `S3` |
| `--red-product-order` | compose operator matrices in source order `Q(R)Q(S)` | `S4` |
| `--red-dagger-transpose` | transpose without cyclotomic conjugation | `S4` |
| `--red-tensor-order` | reverse the actual Kronecker factor order | `S5` |
| `--red-cup-singleton` | replace the Bell cup vector by its first basis vector | `S5` |

Expected exits: green `0`; caught red `1`; a red surviving every comparison in
its target gate `0`, so session-close rejects it; invalid usage, an exception,
or a failure attributed to another gate `2`.  All advertised reds must be
observed before the first green.  A later temporary disabled-comparison
control must demonstrate the surviving-red exit `0` on actual mutated data.

## Runtime and interpretation

The hot loop is the 140,101 F3 composition comparison on matrices of size at
most `3x3`.  Relation images, classical composites, Weyl matrices and
projective representatives should be cached.  Rank-two averaging is confined
to the registered tensor sample.  A green run blocks the listed finite
defects but does not prove SP-STAB-REL, does not select normalized amplitudes,
and does not define physical probabilities or CP/Choi semantics.

## One checker repair wave — pre-registration after code verification

The independent checker-only report at
`theory/lanes/phantasm-stabilizer/critic/CODE-VERIFICATION.md` found sound
green computations but weak mutation placement in S3--S5.  The following
repair expectations were recorded before changing the executable.  This wave
does not alter the mathematical scope or the completed proof verdict.

### S3 bulk construction paths

The four existing S3 mutations will no longer stop in special preflights.
They will enter the actual F3 catalog loop:

- `empty-nonzero` mutates each catalogued empty relation image and first fails
  the bulk zero-separation subcheck;
- `fixed-seed` makes the real catalog map use only projector column zero and
  first fails when a nonempty affine relation has a zero first column;
- `average-sign` reverses the projector character for actual nonempty catalog
  relations and first fails a bulk all-origin D1715 equation;
- `origin-dependent` changes the real alternate-origin averages in the catalog
  loop and first fails exact origin independence.

The expected named subchecks are S3a nonzero image, S3b all-origin equations,
S3c projector square, S3d projector trace, S3e origin independence, S3f empty
zero, S3g projective injectivity, S3h actual-family equality, S3i graph split,
S3j nongraph split and S3k F5 state equality.  Three late-path actual-data
mutations are added:

| mode | actual mutation | intended first subcheck |
|---|---|---|
| `--red-projector-entry` | add one to an actual group-average projector entry used by the rank certificate | `S3c projector-square` |
| `--red-family-state-loss` | delete one actual independently generated qutrit state ray before Hom-family comparison | `S3h actual-family` |
| `--red-f5-state-loss` | delete one actual F5 Clifford-orbit state before its final comparison | `S3k F5-state` |

These mutations alter constructed matrix/family data.  They do not change an
expected count literal.

### S4 exhaustive paths

`product-order` will reverse multiplication only inside actual square
`1->1->1` cases in the 140,101-pair loop, avoiding ill-typed rectangular
products and first failing S4a bulk functoriality.  `dagger-transpose` will
propagate through the 389-relation dagger loop and first fail S4c bulk dagger.
The new mode

| mode | actual mutation | intended first subcheck |
|---|---|---|
| `--red-zero-product` | turn the first actual zero product of two nonempty amplitudes into a nonzero matrix entry | `S4b bulk-zero` |

tests the empty-composite branch inside the typed bulk comparison.  Explicit
orthogonal and unequal-norm scalar witnesses remain green checks after the
bulk loops; they are not mutation prechecks.

### S5 tensor and final scalar paths

`tensor-order` will reverse Kronecker factors in the exhaustive 169-pair state
loop and first fail S5a bulk-state-tensor, then would propagate to effect and
mixed cases.  The point-set assertion comparing `cup.pts` with
`identity.pts` will be removed: it discards types and is definitionally the
same `x+x` construction.  The vectorized identity/Bell comparison remains the
substantive cup control.

The new late F5 mode is:

| mode | actual mutation | intended first subcheck |
|---|---|---|
| `--red-f5-cap-weight` | change one actual F5 Bell-cap coefficient from one to two before closing it with the canonical cup | `S5e F5-loop-scalar` |

It must pass every tensor comparison and both F3/F5 vectorization/Bell checks,
then fail the final retained scalar.  `cup-singleton` continues to mutate the
actual Bell cup and fail the F3 vectorization comparison.

All changed and new modes must be observed before repaired green.  The
disabled-comparison control will remove only S5e temporarily: with the F5 cap
still mutated, `f5-cap-weight` must survive S5 and exit `0`; restoration must
return exit `1`.  Help must advertise exactly the supported named flags, a
caught red exits `1`, a survivor `0`, and wrong gate/usage `2`.
