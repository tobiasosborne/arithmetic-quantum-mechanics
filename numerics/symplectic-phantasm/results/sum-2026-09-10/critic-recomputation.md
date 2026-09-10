# Independent recomputation — SP-SUM

Date: 2026-09-10. Model: `gpt-5.6-sol`, reasoning `xhigh`.
This calculation was made from the canonical definitions and statement, not
from a prover-lane derivation.

## Rectangular actual words

For the standard model, let `e_0: C -> H_n` be the tensor of `n`
computational zero preparations. D1704 contains this tensor and its adjoint.
For `x in F_p^n`, the Pauli translation `X(x)` is a second-level unitary and

    e_x = X(x)e_0,                 e_x(1)=delta_x.

Thus the actual composite `E_(y,x)=e_y e_x^*` satisfies

    E_(y,x) delta_z = [x=z] delta_y.

The coefficient of `delta_y` in the result on `delta_x` extracts the
coefficient of `E_(y,x)` from any linear relation. Hence the `p^(m+n)` words
are independent. This equals

    dim Hom_C(H_n,H_m) = p^m p^n,

so they are a basis. If `m=0` or `n=0`, the same calculation is a row or
column basis; if both vanish, it is the single `1 x 1` unit. Complex addition
enters only after D1707 takes the span.

A separate coordinate script enumerated the standard coordinate vectors. For
`p=3` and ranks zero through two, the nine counts are

    1, 3, 9; 3, 9, 27; 9, 27, 81,

and every family consists of exactly that many distinct standard coordinate
vectors. Their total is 169. Controls at `p=2` and `p=5` gave the same formula;
`p=2` is outside the canonical categorical scope.

## Strictness of completion

At fixed ranks, each affine Lagrangian relation is a subset of a finite
cartesian product, so there are finitely many of them. Conditional on admitted
SP-STAB-REL, D1705 therefore has finitely many projective actual-amplitude
classes in that Hom-set. D1704's arbitrary complex scalars expand a nonzero
class only along its one ray.

Choose independent matrix units `E,F` in `End(H_1)`, whose dimension is
`p^2>1`. If

    E+zF = c(E+z'F),

coefficient comparison gives `c=1` and then `z=z'`. There are infinitely many
such rays, so finitely many actual rays cannot exhaust the full span. This is
a category-level strictness statement; it does not say every rectangular
Hom-set is strictly enlarged.

As a finite diagnostic only, I independently imported the frozen qutrit
census and implemented ray equality by cross multiplication in its exact
cyclotomic ring. It contained 360 endomorphism rays and none matched
`diag(1,1,0)`.

## Block realization and empty shapes

Let `iota_i` and `pi_j` be the canonical injection and projection for the
ordered direct sums. For a dense linear map `L:H_X->H_Y`, define

    T_(j i) = pi_j L iota_i.

Then `sum_i iota_i pi_i=1`, so applying the reconstructed block matrix to
`(xi_i)` gives `L(sum_i iota_i xi_i)`. Conversely, applying a block map to an
input supported at `i` and projecting to `j` recovers `T_(j i)`. This gives
surjectivity and injectivity without a dimension count. Expanding one block
of a product proves composition; the orthogonal direct-sum inner product gives
adjoint transpose.

For an empty source and a four-dimensional target, the matrix shape is `4x0`;
in the reverse direction it is `0x4`, and the endomorphism is `0x0`. They all
have empty entry data but different types. The singleton list `(H_0)` instead
has a `1x1` identity and one-dimensional endomorphism algebra.

## Dimensions and repeated tags

For ordered summand dimensions `d_i`, coordinate pairs `(row,column)` number
`D^2`, where `D=sum_i d_i`. Tagged units are exactly those for which row and
column have the same recorded owner, so their number is `sum_i d_i^2`.
Independent enumeration gave

| dimensions | coherent | tagged | cross-block |
|---|---:|---:|---:|
| `(1,3)` | 16 | 10 | 6 |
| `(1,1,3)` | 25 | 11 | 14 |
| `(3,3)` | 36 | 18 | 18 |
| `(9)` | 81 | 81 | 0 |

The two copies in `(1,1,3)` and `(3,3)` have distinct owner indices. Equality
of their underlying dimensions cannot merge their cross-block units.

## Block dephasing and ordinary trace

On an elementary block `iota_r A pi_s`, orthogonality of the summand
projections gives

    P_k (iota_r A pi_s) P_k = [k=r][k=s] iota_r A pi_s.

Summing over `k` fixes the block when `r=s` and kills it otherwise. Therefore
the range is exactly the diagonal-block algebra, and a second application is
unchanged. Also `Delta_X(1)=sum_i P_i=1`.

The same projections are Kraus operators and

    sum_i P_i^*P_i = sum_i P_i = 1.

Admitted SP-CP therefore makes this a CP trace-preserving map on the singleton
D1706 system `(H)`. Nonemptiness of the list and nonzero standard summands
ensure `H` is nonzero. Finally, in a concatenated orthonormal basis,

    Tr(Delta_X(a)) = sum_i Tr(a_ii) = Tr(a).

No normalized block trace occurs. For dimensions `(1,3)`, matrix-unit
enumeration fixes ten units, kills six, and preserves `Tr(I_4)=4`; the
dimension-normalized sum would instead give `1+1=2`.

## Scope result

The recomputation uses a specified computational coordinate basis and an
ordered direct-sum decomposition. Those are canonical data in D1003/D1707,
not hidden choices. It proves no rig, biproduct universal property, Gaussian
closure, arithmetic-source exhaustion, scalar normalization, or zero-space
channel.
