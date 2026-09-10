<!-- ROLE: pre-registration for the independent SP-FOCK/SP-PRIME/
     SP-BC-CONTROL exact falsifier. Written before implementation and without
     reading any completion prover artifact or notes. -->

# EXPECTATIONS — Fock, prime tensor, and represented BC controls

Date: 2026-09-10. Lane: `phantasm-completions/checker`.
Model: `gpt-5.6-sol`, reasoning setting `xhigh`.

This is finite and symbolic negative-binding evidence only.  Exact integers,
`Fraction` values, permutation actions and prime-valuation vectors replace
floating square roots and logarithms.  The checker does not prove Hilbert
completion, infinite boundedness, state extension, self-adjointness,
point-norm continuity or trace class.  Those remain written-proof duties.

## F1 — rational symmetrizers and one-mode sectors

For Hilbert dimensions `d=0,1,2` and particle sectors `r=0,...,4`, construct

    P_r=(1/r!) sum_(pi in S_r) U_pi

on the actual tensor basis.  Check exact symmetry, `P_r^2=P_r`, and Gaussian
rank against the independently enumerated weakly increasing occupation basis.
Expected ranks are:

- `d=0`: `(1,0,0,0,0)`;
- `d=1`: `(1,1,1,1,1)`;
- `d=2`: `(1,2,3,4,5)`.

Sector zero is the actual one-dimensional vacuum.  For one mode, the unique
occupation tensor has norm one.  The D1010 vector `x^r/sqrt(r!)` has norm
square one because the polynomial norm square `r!` is divided by `r!`.
Replacing the denominator square by one gives norm square `r!` and first
fails at `r=2`.

## F2 — exponential-law norm squares and naturality

For every `(n,m)` with `n,m>=0`, `n+m<=4`, embed the ordered tensor with all H
slots before K slots into `(H+K)^(tensor(n+m))` for one-dimensional H,K.
The actual symmetrized vector has exact norm square

    n!m!/(n+m)!.

Multiplying by the square of D1708's normalization,
`(n+m)!/(n!m!)`, gives one.  No square root is evaluated.  Omitting the
binomial factor leaves norm square `1/2` at `(1,1)`.

Check homogeneous naturality for rational contractions `S=1/2` and `T=-1`:
applying `(S+T)^(tensor(n+m))` after the actual symmetrized embedding equals
embedding after `S^tensor n` and `T^tensor m`.  Vacuum and zero-factor unit
cases are included.  The 15 `(n,m)` cases are guarded explicitly.

## F3 — contraction functor and expansive witness

For rational diagonal/permutation contractions on dimensions one/two, verify
that tensor powers commute with every permutation symmetrizer through sector
four and that sectorwise identity/composition agree.  The vacuum sector is
identity, so finite contraction controls have norm at least one and no sector
exceeds one for the chosen maps.

For `2I`, the exact witnessed sector norms are `(1,2,4,8,16)`, and the
symbolic formula is `2^r`.  This is a finite witness to growth and a record of
the written-proof obligation; the checker does not infer unboundedness from a
finite truncation.  The expansive mutation replaces one actual member of the
accepted contraction family by `2I`; its exact deficit is `-3I`, so it fails
the contraction test independently of any infinity predicate.

## P1 — increasing-prime identity insertions

Use stages `empty,{2},{3},{2,3},{2,3,5}` with unequal local dimensions

    d_2=2, d_3=3, d_5=4.

On all inclusions and all available triangles, check the actual D1711
increasing-prime insertion formula, scalar empty-stage insertion, common unit,
star, product, injectivity and exact action on matrix units.  Use rational
diagonal test elements and compare the exact characteristic polynomial of
`a^*a` after embedding with the source polynomial raised to the inserted
identity multiplicity.  This supplies a finite norm-isometry witness without
floating eigenvalues.

Putting the factor for prime 2 after prime 3 must disagree on a non-scalar
`{3}->{2,3}` element.  Replacing an inserted identity by the actual projection
`q=diag(1,0)` must fail the unit and triangle laws.

## P2 — product states and finite GNS ranks

Use faithful diagonal densities

    rho_2=diag(1/3,2/3),
    rho_3=diag(1/6,2/6,3/6),
    rho_5=diag(1/10,2/10,3/10,4/10),

and a second family with pure `rho_3=|0><0|`.  Check positivity, trace one,
finite product-state compatibility under every P1 embedding, and positivity
on rational `x^*x` witnesses.

Construct the GNS Gram matrix on all matrix units directly from
`phi(a^*b)`.  For stage `{2,3,5}`, dimension `D=24`: the faithful product has
Gram rank `D^2=576`, while the family pure at prime 3 has density support rank
8 and Gram rank `D*8=192`.  At pure stage `{3}`, Gram rank is 3.  Matrix-unit
left action on `[1]` spans exactly the computed quotient rank, giving the
finite cyclicity control.  For the separating-candidate test use faithful
rho_3, whose actual `a->[a]` Gram action has rank 9.  The mutation replaces
that reference by trace-one pure rho_3, reducing this action rank to 3 and
failing injectivity.  Separately, the nonzero matrix `|0><1|` kills the pure
cyclic vector in GNS norm.  No representation-faithfulness conclusion follows.

## B1 — symbolic semigroup shifts

Represent basis indices as positive integers, never finite shift matrices:

    mu_n(m)=nm,
    mu_n^*(k)=k/n if n divides k, undefined otherwise.

For `m,n in {1,2,3,5,6}` and symbolic sample indices check
`mu_m mu_n=mu_(mn)`, `mu_n^*mu_n=1`, the adjoint divisibility law, and
`q_n=mu_nmu_n^*` as the projection onto multiples of n.  For `n>1`, the basis
index 1 witnesses `q_n!=1`; treating mu_n as unitary must fail there.

## B2 — rational phases and root averages

Represent `r in Q/Z` by a reduced `Fraction mod 1`.  Check
`mu_n^*e(r)mu_n=e(nr)` on symbolic basis indices.  Parameterize roots
`s_j=(r+j)/n`, `j=0,...,n-1`, and evaluate their average through exact
divisibility:

    (1/n) sum_j exp(2pi i k(r+j)/n)

is zero unless `n|k`, when it has phase `exp(2pi i (k/n)r)`.  Omitting `1/n`
gives coefficient n on divisible indices and must fail.  No floating root is
formed.

## B3 — valuation-vector dynamics and corner maps

Represent `log m` by the finite prime-valuation vector of m.  Then
`energy(nm)-energy(m)=energy(n)` exactly.  Check the flow exponent for mu_n,
zero exponent for e(r), addition under products and reversal under adjoints.
Negating the actual mu_n exponent must fail.

Check symbolic basis actions for `nu_n(a)=mu_n a mu_n^*` as a corner
star-homomorphism and `L_n(a)=mu_n^*a mu_n` as unital one-Kraus compression.
The homomorphism mutation substitutes the actual L compression for nu in the
same map-product comparison.  Separately, do not assert multiplicativity of
L_n: for `a=mu_n,b=mu_n^*`,
`L_n(ab)=1` while `L_n(a)L_n(b)=q_n`, separated at index 1 for n>1.

## B4 — exact zeta tail witnesses

For integer `b=2,3` and `N=4,8,16,32`, compute rational partial sums and the
integral-test interval

    S_N + (N+1)^(1-b)/(b-1)
      <= zeta(b) <=
    S_N + N^(1-b)/(b-1).

Check positive shrinking widths and nesting/compatibility with later partial
sums exactly.  This witnesses the analytic proof's tail bounds; it does not
prove trace class by numerical truncation.

For b=1, compute dyadic harmonic partial sums through `2^8` and the exact
finite lower witnesses `H_(2^k)>=1+k/2`.  The red mode supplies a concrete
claimed finite trace bound 3; the k=8 partial sum exceeds it.  This refutes
that actual finite acceptance datum without claiming a general divergence
proof from finitely many terms.

## Mutation map

| flag | actual mutation | intended first gate |
|---|---|---|
| `--red-fock-binomial` | omit the exponential-law binomial norm-square factor | `F2` |
| `--red-fock-vacuum` | delete the actual sector-zero vacuum | `F1` |
| `--red-fock-expansive` | replace an accepted contraction input by actual `2I` with deficit `-3I` | `F3` |
| `--red-one-mode-factorial` | replace the actual one-mode basis denominator square `r!` by 1 | `F1` |
| `--red-prime-position` | insert the prime-2 identity after the prime-3 factor | `P1` |
| `--red-prime-nonunital` | insert `q=diag(1,0)` instead of the prime-2 identity | `P1` |
| `--red-density-trace` | change actual rho_2 to `diag(1/3,1/3)` | `P2` |
| `--red-gns-separating` | replace the faithful separating-test density by pure trace-one rho_3 and lose Gram-action injectivity | `P2` |
| `--red-mu-unitary` | replace the actual range projection q_n by identity | `B1` |
| `--red-root-average` | omit the actual factor 1/n in the exact root average | `B2` |
| `--red-time-sign` | negate the actual mu_n valuation exponent | `B3` |
| `--red-L-multiplicative` | substitute actual L_n for nu_n in the corner-homomorphism comparison | `B3` |
| `--red-b1-trace-class` | accept the concrete b=1 trace bound 3 | `B4` |

Every mode changes actual sector, normalization, map, density, shift, phase,
dynamics, compression or series-bound data.  Help exposes exactly these 13
no-argument flags.  Caught reds exit `1` at their intended gate, a survivor
exits `0`, and usage/unexpected/wrong-gate failures exit `2`.  All reds run
before first green.  Disabled-guard controls target only major acceptance
paths and are restored before final normal and optimized greens.

## Sole checker repair wave — tensor-power and adjoint coverage

The valid blind verdict found two checker-only MINOR gaps.  This repair is
registered before implementation and changes no mathematical scope.

F3 will derive the displayed `2I` sector values from actual
`tensor_power(2I,r)` matrices.  On the normalized symmetric tensor
`e_0^tensor r`, it checks the exact output coefficient `2^r`, squared norm
`4^r`, and commutation with the actual symmetrizer.  Add:

| flag | actual mutation | intended first gate |
|---|---|---|
| `--red-fock-tensor-collapse` | replace the actual tensor powers of `2I` by identity matrices of the same sector dimensions | `F3` actual tensor-power growth |

This mode must not alter the independent base contraction-domain check.  With
only the actual-output growth comparison disabled temporarily, it must survive
F3 with exit `0`.

B1 will compare the actual helper `mu_star(n,k)` directly with the divisibility
oracle for every sampled `n,k`, including nonmultiples.  Add:

| flag | actual mutation | intended first gate |
|---|---|---|
| `--red-mu-adjoint-divisibility` | make actual `mu_star(5,k)` return floor division on nonmultiples | `B1` direct adjoint-divisibility comparison |

The existing left-inverse check on multiples and proper range-projection check
remain separate.  Disabling only the new direct comparison must make this red
survive B1 with exit `0`.  Final help exposes fifteen modes; all existing
thirteen paths and the finite-versus-infinite interpretation remain unchanged.
