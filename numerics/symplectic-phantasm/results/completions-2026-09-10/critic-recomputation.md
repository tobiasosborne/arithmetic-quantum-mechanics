# Independent recomputation — completion controls

Date: 2026-09-10. Model: `gpt-5.6-sol`, reasoning `xhigh`.

## Symmetric Fock space

For the inverse-index permutation action, `U_pi U_sigma=U_(pi sigma)` and
`U_pi^*=U_(pi^-1)`. Therefore the finite group average is self-adjoint and
idempotent. Its fixed range is the symmetric sector.

Because `T^tensor-r` acts in every slot, it commutes with permutations. For a
contraction its sector norm is at most `||T||^r<=1`, and summing squared norms
over sectors makes `Gamma_s(T)` bounded. The vacuum sector is identity, so
the norm is exactly one. If `||T||>1`, choose one unit h with `||Th||>1`;
then the symmetric unit tensor `h^tensor-r` has image norm `||Th||^r`, which
is unbounded.

For `xi in Sym^n H`, `eta in Sym^m K`, the permutation average of their
ordered embedding contains `(n+m)!/(n!m!)` orthogonal shuffle images, each
repeated `n!m!` times. Thus its squared norm is

    n!m!/(n+m)! ||xi||^2||eta||^2.

Multiplication by the positive square root of the reciprocal is isometric.
At fixed total degree, the images for different n are orthogonal and span all
symmetrized pure tensors. Their finite closed sum is the whole sector. The
algebraic isometry therefore has dense range and extends to a unitary on the
Hilbert completions. Tensor powers commute with the coordinate inclusions,
which proves the naturality square before extension; boundedness extends it.

Independent occupation counting gave sector ranks

| dimension | ranks for r=0,...,4 |
|---:|---|
| 0 | `1,0,0,0,0` |
| 1 | `1,1,1,1,1` |
| 2 | `1,2,3,4,5` |
| 3 | `1,3,6,10,15` |

The fifteen `(n,m)` cases through total four all normalize to squared norm
one; the raw `(1,1)` norm is `1/2`. Actual `2I` sector norms continue as
`1,2,4,8,16,32,...`.

For one mode, `x^r/sqrt(r!)` has unit norm and maps to the unit tensor in the
rth one-dimensional sector. The zero one-particle space still has the scalar
vacuum sector, so `Gamma_s(0)=C`. The number operator is diagonal on the exact
domain `sum r^2|c_r|^2<infinity`.

## Prime tensor limit and GNS

After the unique increasing-order permutation, every inclusion is
`a -> a tensor I`. Hence it is a unital star-homomorphism and
`||a tensor I||=||a||`: the upper tensor bound and a norm-attaining vector
tensored with a unit vector give opposite inequalities. Slot insertion makes
composition literal, including the scalar empty stage.

Moving two representatives to the union of their finite prime sets makes the
algebraic direct-limit operations independent of stage. Isometry makes the
norm independent. The matrix C-star identity and common unit pass to the
completion because product and star are norm-continuous.

At stage P, `rho_P=tensor rho_p` is positive with trace one. The functional
`Tr(rho_P a)` is positive and has norm one. For `P subset Q`, identity
insertion contributes the factor `product_(Q-P)Tr(rho_q)=1`; thus a bounded
positive functional is defined on the algebraic union. Continuous extension
is unique, and approximation of square roots proves positivity on the
completion.

For a positive functional, Cauchy--Schwarz makes the null space orthogonal to
everything. The C-star inequality

    a^*c^*ca <= ||c||^2 a^*a

makes it a left ideal and bounds left multiplication by `||c||`. Completion
therefore gives the GNS star representation. Since `pi(a)[1]=[a]`, the
reference vector is cyclic by construction.

For a matrix density of support rank s on dimension D, the matrix-unit Gram
form has rank `D*s`. The independent fixtures give `24*24=576`,
`24*8=192`, and `3*1=3`. For a pure local vector e, `a=|0><1|` can have
`phi(a^*a)=0`; a support-orthogonal projection kills the cyclic vector but
acts nontrivially on a suitable class. This confirms nonseparating cyclicity.
The selected stage poset independently has 14 inclusions and 30 triangles.

## Represented Bost--Connes control

The shift adjoint is forced by basis inner products:

    mu_n^* delta_k = delta_(k/n) if n divides k, else 0.

This immediately gives the semigroup and isometry laws and the projection
onto multiples of n. The diagonal phase calculation gives
`mu_n^*e(r)mu_n=e(nr)`. The n roots of `ns=r` are `(r+j)/n`; their character
average is zero unless `n|k`, when it is one. This reproduces the corner
identity with its factor `1/n`.

With `q_n=mu_nmu_n^*`, conjugation by mu is multiplicative because
`mu_n^*mu_n=1`, and compression is its inverse on `q_n A q_n`. Compression
by one bounded operator is CP at every matrix amplification and is unital.
It is not multiplicative: at n=2,

    L_2(mu_2 mu_2^*)=1,  L_2(mu_2)L_2(mu_2^*)=q_2,

which differ on `delta_1`.

For the diagonal multiplication operator, testing an adjoint-domain vector
against every basis vector forces adjoint coordinates `(log m)eta_m`.
Square summability is exactly the stated maximal domain, so the operator is
self-adjoint. Its exponential multiplies `delta_m` by `m^(iu)`. The ratio
`(nm)^(iu)/m^(iu)` gives the claimed flow on mu; e(r) is diagonal and fixed.
Continuity on finite generator polynomials plus the two-error norm estimate
extends point-norm continuity to the represented closure.

Finally `e^(-bH)` has positive eigenvalues `m^-b`. For `b>1`, comparison with
the integral of `x^-b` makes their sum finite, so the operator is trace class
and its trace is the prescribed zeta series. Exact controls gave shrinking
tail intervals at b=2,3, while the rational harmonic sum through 256 exceeds
both 3 and the dyadic lower bound 5. These finite numbers only falsify a bad
b=1 bound; the written integral argument carries convergence.
