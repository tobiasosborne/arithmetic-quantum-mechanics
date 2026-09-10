<!-- ROLE: pre-registration for the SP-EGOROV / affine SP-TENSOR exact
     falsifier. Written before the original lane checker existed. This lane did
     not read any prover-lane artifact. -->

# EXPECTATIONS — affine Egorov and tensor naturality

Date: 2026-09-10. Lane: `phantasm-stage1/egorov-checker`.
Model: `gpt-5.6-sol`, reasoning setting `xhigh`.

This is a pre-registration, not a proof and not promotion evidence. The
checker must use exact finite-field and cyclotomic-integer arithmetic only
(elapsed wall-clock timing is outside the mathematical checks).
It may reuse the already checked `GF` and `CycRing` arithmetic classes from
`theory/checks/wh_kappa_check.py`, but its affine enumeration, action,
operator covariance and tensor comparisons must be new code. In particular,
the two sides of a covariance or naturality check may not be produced by one
shared action helper.

## Canonical inputs and independently derived signs

For rank one write `v=(a,b)`,

    omega((a,b),(c,d)) = a*d-c*b,
    W^s(a,b)e_y = psi(-b*(y+a)+a*b/2)e_(y+a).

For an affine arrow `A=(t,g)`, D1701 gives

    A(v)=g*v+t,
    (s,h) o (t,g) = (s+h*t,h*g).

The canonical SP-EGOROV row gives

    alpha_(t,g)(W^s(v)) = psi(omega(t,g*v)) W^s(g*v).

The following operator signs were derived directly from the displayed
`W^s` formula, rather than from an implementation of `alpha`.

1. `W^s(t)` implements translation:
   `W^s(t) W^s(v) W^s(t)^* = psi(omega(t,v)) W^s(v)`.
2. With the unnormalised Fourier matrix
   `F[x,y]=psi(x*y)`, exact conjugation is
   `F W^s(a,b) F^* = q W^s(b,-a)`. Thus its symplectic matrix is
   `J=((0,1),(-1,0))`. The integer factor `q` avoids adjoining `sqrt(q)`.
3. For `r in k`, the diagonal matrix
   `D_r[x,x]=psi(-r*x^2/2)` satisfies
   `D_r W^s(a,b) D_r^* = W^s(a,b+r*a)`. Thus the lower shear is
   `S_r=((1,0),(r,1))`.

For direct sums, the rank-two form is the component sum. Hence for factor
arrows `A_i=(t_i,g_i)` the direct-sum phase is

    omega(t_1,g_1*v_1) + omega(t_2,g_2*v_2),

which must equal the exponent obtained by applying the two factor actions
after the tensor comparison. This is the remaining affine naturality
comparison in SP-TENSOR; it does not re-establish SP-WEYL or F1-FUNCT.

## Green expectations

### E1 — exact symplectic and affine census over F3

Exhaustively enumerate all `2 x 2` matrices over `F3` and retain determinant
one. Expected: `|Sp(2,F3)|=|SL(2,F3)|=24`. Each retained matrix preserves
`omega` on all `9^2=81` vector pairs. With all translations, the affine set
has `9*24=216` elements. No recalled generator presentation is used for this
census.

### E2 — affine identities, inverses and all-pairs composition

Expected identity: `(0,I)`. Every one of the 216 arrows has a unique inverse,
and the explicit candidate `(-g^(-1)t,g^(-1))` must agree with an exhaustive
two-sided inverse search. For every one of the `216^2=46,656` ordered arrow
pairs, the D1701 semidirect formula must agree pointwise with successive
application on all nine vectors: `419,904` point comparisons. Closure and
both identity laws are checked independently as tuples.

### E3 — the affine Weyl-algebra action

Using terms `zeta^e W(v)` and the half-form multiplier, check:

- identity on all 9 Weyl basis elements;
- star preservation for `216*9=1,944` arrow/label pairs;
- multiplication for `216*9^2=17,496` arrow/ordered-label-pair cases;
- action composition for every ordered affine pair and label,
  `216^2*9=419,904` cases.

All equalities are exponent and label equalities modulo three. The geometric
semidirect result is supplied independently by E2; E3 does not call the
point-action comparison to manufacture both algebra-action sides.

### E4 — independent translation covariance

Build the nine monomial matrices `W^s(t)` directly from the D1703 action and
check their conjugation of every `W^s(v)`: `9^2=81` exact matrix equalities.
The expected phase and unchanged label are constructed from `omega`, not from
the conjugation helper.

### E5 — independent Fourier covariance

Build `F[x,y]=zeta^(x*y)` as a dense matrix in `Z[zeta_3]`. For all nine
labels check `F W^s(v) F^* = 3 W^s(Jv)`. Also check `F^*F=3I` directly.
No floating normalisation or tolerance is permitted.

### E6 — independent shear covariance

For both `r=1,2`, build the diagonal matrices
`D_r[x,x]=zeta^(-r*x^2/2)` and check every Weyl label against
`(a,b) -> (a,b+r*a)`: 18 exact covariance equalities. Also check each
`D_r D_r^*=I`.

### E7 — rank-zero control

The zero symplectic space has one point, one symplectic map, one affine arrow,
one Weyl basis element and the one-dimensional Hilbert model `C`. Its affine
action, tensor unit comparisons on both sides, and identity/inverse laws are
all literal identities. No positive-dimensional placeholder is accepted.

### E8 — non-prime-field character and covariance control

Use the existing exact field builder for
`F9=F3[u]/(u^2+1)`, whose integer encoding is `a+3b` for `a+b*u`. Choose the
nonstandard additive character

    psi_u(a+b*u) = zeta^Tr(u*(a+b*u)) = zeta^b.

Its pre-registered exponent table on encodings `0,...,8` is
`(0,0,0,1,1,1,2,2,2)`, whereas the fixed absolute-trace character has table
`(0,2,1,0,2,1,0,2,1)`. Check additivity on all 81 input pairs,
nontriviality, and inequality from the absolute-trace character. Then check
the D1703 Weyl multiplication on all `81^2=6,561` label pairs, translation
covariance on all `81^2=6,561` `(t,v)` pairs, Fourier covariance for all 81
labels, and the two shears `r in {1,u}` for all 81 labels. Fourier uses the
integer factor 9. These tests exercise field multiplication and a genuinely
non-prime character rather than repeating the F3 table.

### E9 — rank-two tensor comparison and affine naturality

For `F3`, compare the rank-two D1703 operator on the nine-element basis with
the independently formed Kronecker product of two rank-one operators for all
`9^2=81` Weyl labels. Check the swap comparison on all 81 labels and both
rank-zero unit placements. Finally, for every ordered pair of factor affine
arrows (`216^2=46,656`) and every ordered pair of factor Weyl labels (81),
compare the rank-two affine phase/label computation with the two separately
computed rank-one images: `3,779,136` exact naturality cases.

This finite gate tests strict algebra naturality in the named coordinates.
It supplies no choice of a genuine Weil lift; the unitary comparisons are
only expected projectively in the claim.

## Pre-registered mutation map

Every mode below will be advertised by `--help`, must exit nonzero, and must
name exactly the intended first failing gate shown here. Mutations are local
to their target gates so an earlier unrelated check cannot mask reachability.

| mode | mutation | intended first gate |
|---|---|---|
| `--red-sp-enumeration` | retain all invertible matrices instead of determinant-one matrices | E1 |
| `--red-semidir-order` | use translation `s+t` instead of `s+h*t` in affine composition | E2 |
| `--red-alpha-phase` | use `omega(t,v)` instead of `omega(t,g*v)` | E3 |
| `--red-translation-sign` | conjugate by `W^s(-t)` while retaining the canonical expected phase | E4 |
| `--red-fourier-sign` | change the Fourier kernel from `psi(x*y)` to `psi(-x*y)` while retaining `J(a,b)=(b,-a)` | E5 |
| `--red-shear-half` | omit the factor `1/2` in the quadratic shear phase | E6 |
| `--red-zero-qudit` | replace the actual rank-zero Hilbert basis by the three-element F3 basis | E7 |
| `--red-f9-character` | substitute the absolute-trace character for `psi_u` | E8 |
| `--red-tensor-phase` | drop the second affine phase after tensoring | E9 |

Expected exit codes: green `0`; caught red `1`; a surviving red `0`, so
`session-close.sh` rejects it; bad usage or a red failing first at the
wrong gate `2`. The explicit verifier checks the named gate as well as
the exit code.

## Runtime and interpretation

The largest loop is E9's 3,779,136 tuple comparisons; no dense `9 x 9`
matrix multiplication occurs in that loop. Dense exact matrices are limited
to the Fourier/shear controls in dimensions 3 and 9. The intended green run
should remain suitable for inclusion in the repository's full checker suite.
A green run is evidence only at these finite scopes. A disagreement blocks
promotion until the checker, canonical statement and proof are reconciled.

## E7 repair after the single blind review — 2026-09-10

The critic verified the actual rank-zero operator and tensor-unit checks,
including a copied-data mutation, but found that the advertised red stopped
at a synthetic dimension variable before reaching them. The coordinator
repair removes that precheck and makes the red change the actual basis
construction from the empty Cartesian power to the first Cartesian power.
E7 must now reject the resulting three-dimensional model data. The other
gate computations are unchanged. This repair expectation is registered
before the repaired check is executed.

The coordinator also disabled the E9 acceptance comparison on a temporary
copy and observed that the old uncaught-red exit code was 2. The repository
runner would accept that nonzero exit as a caught mutation. A surviving
mutation must instead exit 0; the same disabled-comparison control verifies
this interface repair. No mathematical check is weakened by that return-code
change.
