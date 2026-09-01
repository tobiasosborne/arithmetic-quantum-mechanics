# FCR-1 falsifier expectations

Lane model: gpt-5.6-sol, reasoning xhigh, codex exec.

These expectations come only from `briefs/fcr-local-target.md`, its permitted
trunk conventions, and first-principles calculations recorded below.
Throughout, `n:=|R|`; `q` retains its trunk meaning `|κ|`, so `n=q` only
when `R` is a field.  “N/A” means the brief does not register that gate at that seed;
the checker prints the scope exclusion rather than silently omitting a line.

## Exact representations and reference characters

Every ring is materialized as full `ADD` and `MUL` tables.  Elements of an
equal-characteristic ring are little-endian coefficient tuples.

| seed | additive coordinates | phase ring | reference exponent |
|---|---:|---:|---|
| `F3` | `C3` | `Z[zeta_3]` | `a` |
| `F9=F3[t]/(t^2+1)` | `C3^2` | `Z[zeta_3]` | `Tr(a+bt)=2a` |
| `Z9` | `C9` | `Z[zeta_9]` | `a` |
| `F3[e]/e2` | `C3^2` | `Z[zeta_3]` | coefficient of `e` |
| `Z27` | `C27` | `Z[zeta_27]` | `a` |
| `F3[t]/t3` | `C3^3` | `Z[zeta_3]` | coefficient of `t^2` |
| `F3[x,y]/(x,y)^2` | `C3^3` | `Z[zeta_3]` | coefficient of `y` (not generating) |

For phase order `d=3,9,27`, the coefficient-vector modulus is
`Phi_d=X^(2d/3)+X^(d/3)+1`.  The checker verifies
`Phi_d(X)(X^(d/3)-1)=X^d-1` and that the first `d` powers of `zeta_d` are
distinct.  No complex approximation is used.

## G1 — characters, kernel ideals, and generating characters

| seed | `|X(R)|` | distribution `|I_psi| : number of psi` | `|Gen(R)|=|R^x|` |
|---|---:|---|---:|
| `F3` | 2 | `1:2` | 2 |
| `F9` | 8 | `1:8` | 8 |
| `Z9` | 8 | `1:6, 3:2` | 6 |
| `F3[e]/e2` | 8 | `1:6, 3:2` | 6 |
| `Z27` | 26 | `1:18, 3:6, 9:2` | 18 |
| `F3[t]/t3` | 26 | `1:18, 3:6, 9:2` | 18 |
| `F3[x,y]/(x,y)^2` | 26 | `3:24, 9:2` | 0 |

An additive group and its character group have the same order, so deleting
the trivial character gives `n-1`.  The coordinate parameterization explicitly
lists all `n` characters and checks that their tables are distinct and
additive.  For `Z/(3^k)`, `|I_{psi_c}|=gcd(c,3^k)`.  For either principal
equal-characteristic chain, a character is generating exactly when its top
coefficient is nonzero; the remaining two layers give the displayed `3` and
`9` kernel ideals.  At the non-Frobenius seed, `m=(x,y)` is two-dimensional
and `m^2=0`; the restriction of any scalar character to `m` has a nonzero
kernel.  A nonzero restriction has a kernel line (24 characters, `|I|=3`),
while the two characters vanishing on all of `m` have `I=m` (`|I|=9`).

Discriminating power: the census is active at all seeds.  The
`--red-frobenius-blind` claim is distinguishable only at the last seed and
fires here with a size-3 ideal witness.

## G2 — the forms

| `n` / seeds | vectors checked for `omega(v,v)=0` | ordered pairs for `beta-beta^T=omega` |
|---|---:|---:|
| 3 / `F3` | 9 | 81 |
| 9 / `F9`, `Z9`, `F3[e]/e2` | 81 each | 6,561 each |
| 27 / the three order-27 seeds | 729 each | 531,441 each |

The formulas give `omega(v,v)=ab-ab=0`.  The two basis rows and columns give
`omega((a,b),w)=a omega(e1,w)+b omega(e2,w)` and its second-variable analogue;
the explicitly checked ring distributive laws then imply R-bilinearity.
Testing every nonzero row against all `w` gives R-nondegeneracy.  Finally,
`ab'-a'b=omega(v,v')` gives the pair count above.

Discriminating power: because every seed has odd residue characteristic,
`beta_0^T-(beta_0^T)^T=-omega != omega`; `--red-transpose` is visible at every
seed (the red run is targeted at `F3`).

## G3 — the character-valued radical

For every nontrivial character, all `n^4` pairs `(v,w)` are evaluated.  The
expected radical-size distribution is obtained by squaring every ideal size in
G1:

| seed | characters exhausted | distribution `|rad| : number of psi` | phase lookups |
|---|---:|---|---:|
| `F3` | 2 | `1:2` | 162 |
| `F9` | 8 | `1:8` | 52,488 |
| `Z9` | 8 | `1:6, 9:2` | 52,488 |
| `F3[e]/e2` | 8 | `1:6, 9:2` | 52,488 |
| `Z27` | 26 | `1:18, 9:6, 81:2` | 13,817,466 |
| `F3[t]/t3` | 26 | `1:18, 9:6, 81:2` | 13,817,466 |
| `F3[x,y]/(x,y)^2` | 26 | `9:24, 81:2` | 13,817,466 |

Indeed `psi(omega((a,b),(r,0)))=1` for all `r` iff `b in I_psi`, and the
analogous test against `(0,r)` says `a in I_psi`.  Conversely those two
conditions make every `ar'-rb'` invisible, so the radical is `I_psi^2`.

The 13,817,466-lookups rows modestly exceed the `10^7` caution because the
brief explicitly requires every character and both radical directions by
exhaustion.  They are vectorized table lookups, not Python-level dense matrix
multiplication.  `--red-frobenius-blind` also reaches G3 at the last seed: the
smallest possible radical has size 9, not 1.

## G4 — exact Weyl and commutation relations

| seed | chosen character | ordered matrix pairs per identity |
|---|---|---:|
| `F3` | generating | 81 |
| `F9`, `Z9`, `F3[e]/e2` | generating | 6,561 each |
| `Z27`, `F3[t]/t3` | generating | 531,441 each |
| non-Frobenius seed | N/A: `Gen(R)` empty | 0 |

With `W(a,b)=Z(-b)X(a)`, application to a basis vector shows that the phase
left after factoring `W(a+a',b+b')` is `psi(ab')`, exactly the registered
`beta_0`.  Swapping the factors and using G2 leaves `psi(omega(v,v'))`.
Matrices are stored as exact permutation/exponent pairs and compared through
coefficient vectors in `Z[zeta_n]`.

At order 27, each of the 531,441 matrix pairs compares 27 phase entries for
each of two identities (about 28.7 million small exact comparisons).  This is
the direct exhaustive matrix check required by G4 and avoids a much costlier
dense `27^3` matrix product per pair.  `--red-transpose` reaches G4 at every
Frobenius seed; it is blind only at the non-Frobenius seed where G4 is out of
scope.

## G5 — FCR-ALG pipeline

| seed | Weyl operators / exact rank | matrix commutant dimension |
|---|---:|---:|
| `F3` | 9 / 9 | 1 |
| `F9`, `Z9`, `F3[e]/e2` | 81 / 81 each | 1 each |
| `Z27`, `F3[t]/t3` | 729 / 729 each | 1 each |
| non-Frobenius seed | N/A | N/A |

Different shifts have disjoint matrix support.  Within a shift, the `n`
phase rows are the `n` characters induced by a generating pairing; their exact
Gram matrix is `n I`, since a nontrivial character sums to zero.  This gives
rank `n^2` without division in a cyclotomic field.  The matrix commutant is
solved exactly by phase-potential equations, giving one live component.

Discriminating power: `--red-dim` sees rank 9 rather than the claimed 10 at
`F3`.  `--red-nongenerating` at `Z9` sees rank 27 rather than 81 and matrix
commutant dimension 3 rather than 1.  These mutations therefore have different
observable effects despite both firing G5.

## G6 — designated non-generating `Z9` probe

This gate is N/A at the other six seeds.  For `psi_3(x)=zeta_9^(3x)`,
`I_psi=(3)={0,3,6}` has size 3.  A formal Weyl basis element commutes with all
Weyl elements exactly when its label lies in `I_psi^2`; hence the commutant
inside the formal twisted algebra (its center) has dimension `3^2=9`, strictly
larger than the scalars.

The checker separately records that the commutant of the non-faithful
9-dimensional matrix image has dimension 3.  This arena distinction is forced
by direct computation and prevents the brief's `|I|^2` expectation from being
silently conflated with the matrix-image quantity used by G5.

Discriminating power: `--red-g6-arena-confusion` replaces the formal
commutant claim `|I_psi|^2=9` by the matrix-image dimension `3`.  The exhaustive
central-label census still gives `9`, so G6 rejects the arena conflation while
the unmutated non-generating probe remains valid positive input.

## G7 — all submodules and Lagrangians

| seed | submodule size histogram | Lagrangians | free / non-free |
|---|---|---:|---:|
| `Z9` | `1:1, 3:4, 9:13, 27:4, 81:1` | 13 | 12 / 1 |
| `F3[e]/e2` | same | 13 | 12 / 1 |
| other five seeds | N/A | N/A | N/A |

Both rings are principal local chain rings of length two with residue field
`F3`.  The four size-3 submodules are the four lines in the two-dimensional
socle, and perpendicularity gives four size-27 partners.  A free size-9 line
has a primitive generator: `(81-9)/6=12` such lines after dividing 72 primitive
vectors by 6 units.  The only non-free size-9 submodule is `m R^2`, giving 13.
Alternation makes every free line isotropic, and `m^2=0` makes `m R^2`
isotropic; since all have size 9 and `|L||L^perp|=81`, each is Lagrangian.

The checker discovers all 23 submodules by closure, rather than feeding this
classification into the enumeration, then asserts the predicted histogram
and the dual-size identity on every result.  `--red-free-only` is
discriminating at both registered seeds and is targeted at `Z9`.

## G8 — unit torsor and nonunits

| seed | distinct generating `psi_u`, `u` a unit | non-generating `u in m` |
|---|---:|---:|
| `F3` | 2 | 1 |
| `F9` | 8 | 1 |
| `Z9` | 6 | 3 |
| `F3[e]/e2` | 6 | 3 |
| `Z27` | 18 | 9 |
| `F3[t]/t3` | 18 | 9 |
| non-Frobenius seed | N/A (`Gen=empty`) | N/A |

The reference pairing `u -> psi(u·)` is injective at each Frobenius seed.
Multiplication by a unit preserves `I=0`; multiplication by a nonunit puts a
nonzero socle ideal into the kernel.  Distinct character tables are distinct
central characters.  `--red-torsor` targets `u=3 in (3) subset Z9` and sees
`I=(3)`, so G8 has discriminating power there (and analogously at every
non-field Frobenius seed).

## G9 — odd halving and the beta torsor

| seed | `2^(-1)` in table encoding | `|Adm(omega)|=n^3` | `s` checked for `phi_s` |
|---|---:|---:|---:|
| `F3` | 2 | 27 | all 27 |
| `F9` | 2 | 729 | all 729 |
| `Z9` | 5 | 729 | all 729 |
| `F3[e]/e2` | 2 | 729 | all 729 |
| `Z27` | 14 | 19,683 | 128 seeded |
| `F3[t]/t3` | 2 | 19,683 | 128 seeded |
| `F3[x,y]/(x,y)^2` | 2 | 19,683 | 128 seeded |

A symmetric bilinear form on `R^2` is determined uniquely by three
coefficients `(alpha,gamma,delta)`, giving `n^3` members `beta_0+s` of
`Adm(omega)`.  Antisymmetry forces `2 alpha=2 delta=0` and
`1+2 gamma=0`.  Since 2 is a unit, there is one solution, namely
`beta_0+s=omega/2`.  At `F3`, `Z9`, and `F3[e]/e2` every full table is censused,
as registered.  The coefficient census covers uniqueness at every other seed.

For every selected `s`, the checker exhausts all `n^4` pairs in
`s(v+w,v+w)/2-s(v,v)/2-s(w,w)/2=s(v,w)`.  At order at most 9 every `s` is
used.  At order 27, 128 distinct triples from a fixed PRNG seed exceed the
brief's minimum of 100; the resulting 68,024,448 table comparisons per seed
are the registered G9 reduction from a prohibitive `19,683*531,441` census.
`--red-halfweyl-drop` changes the left coboundary to `2s(v,w)` and is
discriminating at every seed.

## G10 — exact `F3` field regression

This gate is N/A at the other six seeds.  At `F3` it expects: two nontrivial
characters, two generating characters, two units; `|V|=9`; 81 ordered form and
matrix pairs; four projective lines; Weyl rank 9; matrix commutant dimension 1;
the same nine fixed permutation/exponent matrices as
`wh_kappa_check.py`'s corrected `Z(-b)X(a)` model; and profile
`{1:1, 3:26}` for `H_beta0`.

These are the `n=3` values `n-1`, `n+1`, `n^2`, and `n^3`, plus a literal
matrix fixture.  `--red-transpose` also reaches this gate after G2 and G4,
because its active beta is no longer the fixed regression beta.

## G11 — element-order profiles (discovered data)

| seed | exhaustively discovered profile `order:count` | sum |
|---|---|---:|
| `F3` | `1:1, 3:26` | 27 |
| `F9` | `1:1, 3:728` | 729 |
| `Z9` | `1:1, 3:26, 9:702` | 729 |
| `F3[e]/e2` | `1:1, 3:728` | 729 |
| `Z27` | `1:1, 3:26, 9:702, 27:18954` | 19,683 |
| `F3[t]/t3` | `1:1, 3:19682` | 19,683 |
| `F3[x,y]/(x,y)^2` | `1:1, 3:19682` | 19,683 |

These counts were not pre-predicted; they are data discovered by brute-force
powering in the explicit group table.  As independent internal identities,
each profile has exactly one identity, every reported order divides `|R|^3`,
and the counts sum to `|R|^3` as displayed.  Equal-characteristic seeds have
exponent 3 directly from characteristic 3 and the class-two power formula;
this independently corroborates those census rows.  The registered
`--red-profile-drop-identity` mutation omits `(0,0)` from
the powering census.  It leaves `n^3-1` records and no order-one element, so
G11 rejects the profile.
