# Small-rings catalogue checker expectations

Lane model: gpt-5.6-sol, reasoning xhigh, codex exec.

This is a blind recomputation from D12--D16.  No value was imported from the
orchestrator's scratch program.  `n=|R|`.  Ring elements are little-endian
coefficient tuples; `F4` uses `alpha^2=alpha+1`, and `F2[e]/e2` uses `e^2=0`.
Every ring and character is represented by a complete finite table.

## Exact phase arithmetic

Roots of unity are coefficient vectors in `Z[x]/(Phi_d)`:

| `d` | `Phi_d` | use |
|---:|---|---|
| 2 | `x+1` | `F2`, `F4`, `F2[e]/e2` characters |
| 3 | `x^2+x+1` | `F3` characters |
| 4 | `x^2+1` | `Z4` characters and characteristic-2 Lagrangian characters |
| 8 | `x^4+1` | `Z4` Lagrangian characters |

The checker verifies the polynomial relation and exact order of each root.
Monomial matrices store a permutation and root exponents.  No complex or real
floating-point value is formed.

## C1 -- local-ring, character, and cocycle data

| `R` | `m` | `|kappa|` | `|soc|` | `|R^x|` | all additive chars | `|Gen|` | `|Adm|` | antisymmetric `beta` |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `F2` | `0` | 2 | 2 | 1 | 2 | 1 | 8 | 0 |
| `F3` | `0` | 3 | 3 | 2 | 3 | 2 | 27 | 1 |
| `F4` | `0` | 4 | 4 | 3 | 4 | 3 | 64 | 0 |
| `Z4` | `(2)` | 2 | 2 | 2 | 4 | 2 | 64 | 0 |
| `F2[e]/e2` | `(e)` | 2 | 2 | 2 | 4 | 2 | 64 | 0 |

Derivation: units are found by exhaustive inverse search, `m` is their
complement, and `soc=Ann(m)` is multiplied out.  All additive character tables
are enumerated from the additive coordinates.  For each character,

`I_psi={r : psi(rx)=1 for every x in R}`

is computed directly; `I_psi=0` defines `Gen`.  The unit-scaled orbit of the
named reference character is compared as a set with the exhaustive `Gen`
census, not merely counted.  A bilinear form is a four-entry matrix, and the
condition `beta-beta^T=omega` leaves three free entries, hence `n^3`; every
resulting table is nevertheless constructed, checked, and deduplicated.
Only `F3` has the unique antisymmetric member `omega/2`.

## C2 -- cocycle and `UT_3`

For each ring, the identity

`beta(u,v)+beta(u+v,w)=beta(v,w)+beta(u,v+w)`

is checked on all `n^6` triples in `V^3`.  The coordinate bijection

`(t,a,b) -> [[1,a,t],[0,1,b],[0,0,1]]`

is checked on all `n^6` ordered group pairs; its top-right entry is exactly
`t+t'+ab'`.  At `F3`, all 27 symmetric forms also pass the exact coboundary
transport with `s(v,v)/2`, independently confirming beta-independence there.

## C3 -- group census

The following profiles are discovered by powering every group element.

| `R` | `|H|` | centre order profile | exponent | full order profile |
|---|---:|---|---:|---|
| `F2` | 8 | `1:1, 2:1` (`C2`) | 4 | `1:1, 2:5, 4:2` |
| `F3` | 27 | `1:1, 3:2` (`C3`) | 3 | `1:1, 3:26` |
| `F4` | 64 | `1:1, 2:3` (`C2^2`) | 4 | `1:1, 2:27, 4:36` |
| `Z4` | 64 | `1:1, 2:1, 4:2` (`C4`) | 8 | `1:1, 2:7, 4:40, 8:16` |
| `F2[e]/e2` | 64 | `1:1, 2:3` (`C2^2`) | 4 | `1:1, 2:31, 4:32` |

The centre itself is independently censused by commuting every element with
every other and equals `R x 0`.  At `F2`, the elements
`r=(0;1,1)`, `s=(0;0,1)` generate all eight elements and satisfy
`r^4=s^2=1`, `srs=r^-1`, a dihedral witness.  At `F3`, centre=derived group of
order 3 and exponent 3 give the extraspecial plus presentation.

For `Z4`, direct elementwise comparison gives order 8 exactly when `a,b` are
both units (odd): 4 such phase-space labels times 4 central coordinates gives
16.  For `F2[e]/e2`, additive doubling vanishes and no order 8 occurs.

Additional discovered-by-census beta profiles:

| ring | profile | number of admissible cocycles |
|---|---|---:|
| `F2` | `1:1,2:5,4:2` (D4 type) | 6 |
| `F2` | `1:1,2:1,4:6` (Q8 type) | 2 |
| `F4` | `1:1,2:27,4:36` | 40 |
| `F4` | `1:1,2:3,4:60` | 24 |

The order-64 groups are pairwise non-isomorphic.  `Z4` is separated by its
cyclic centre, exponent 8, and 16 order-8 elements.  The other two both have
centre `C2^2` and exponent 4, but have 27 versus 31 involutions.

## C4 -- commutators and conjugacy classes

Every ordered pair satisfies
`[g,h]=(omega(v,w),0)`.  The set of commutators is all `R x 0`, so the
abelianization has order `n^2`.  Conjugacy classes are constructed as explicit
orbits.

| `R` | annihilator sizes in element order | identity evaluation | classes |
|---|---|---|---:|
| `F2` | `2,1` | `4+1` | 5 |
| `F3` | `3,1,1` | `9+1+1` | 11 |
| `F4` | `4,1,1,1` | `16+1+1+1` | 19 |
| `Z4` | `4,1,2,1` | `16+1+4+1` | 22 |
| `F2[e]/e2` | `4,1,2,1` | `16+1+4+1` | 22 |

Thus the independent orbit count equals
`n^2 + sum_{u!=0}|Ann(u)|^2` at every ring.

## C5 -- exact trace-Gram matrices

For every generating character (not just the reference one), all `n^2` Weyl
operators are constructed as exact monomial matrices.  If shifts differ their
supports are disjoint.  For equal shifts the Gram entry is a complete
character sum, evaluated in `Z[zeta_d]`; it is `n` on the diagonal and zero
off it.  Hence the exact Gram matrix is `n I_(n^2)`, the rank is `n^2`, and the
operators span `M_n(C)`.  An independent exact commutant calculation gives
dimension one.

The same tables give the Pauli image of order 8 at `F2`, `ZX=zeta_3 XZ` at
`F3`, two independent regular `C2` shifts at `F4`, and the `Z4` clock exponent
row `(0,1,2,3)`, i.e. `diag(1,i,-1,-i)`.

## C6 -- representation catalogue

The bottom characters are exhaustively listed as all `n^2` additive
characters of `V`.  For every `u`, the recomputed row is

`|Ann(u)|^2` irreducibles of dimension `n/|Ann(u)|`.

| `R` | bottom | middle | top | irreps/classes | sum of squares |
|---|---|---|---|---:|---:|
| `F2` | `4 x dim 1` | -- | `1 x dim 2` | 5 | 8 |
| `F3` | `9 x dim 1` | -- | `2 x dim 3` | 11 | 27 |
| `F4` | `16 x dim 1` | -- | `3 x dim 4` | 19 | 64 |
| `Z4` | `16 x dim 1` | `4 x dim 2` | `2 x dim 4` | 22 | 64 |
| `F2[e]/e2` | `16 x dim 1` | `4 x dim 2` | `2 x dim 4` | 22 | 64 |

The number of displayed irreducibles equals the independently computed class
count, and the sum of squared dimensions equals `|H|` in every row.

## C7 -- middle stratum and the requested decomposition

For `u=2` in `Z4` and `u=e` in `F2[e]/e2`, exhaustive tests give

`I_(psi_u)=Ann(u)=m`, and `rad(psi_u o omega)=m x m` (size 4).

The 16 labelled Weyl matrices have exactly 8 distinct exact images and also 8
projective images; including central scalars, the full group image has 16
matrices.  This makes the report's “8 scaled images” robust under either
equality or proportionality among the Weyl matrices themselves.

Let `r=2` or `e`.  Since `X(r)` commutes with the represented algebra, the
4-dimensional model splits into its two eigenspaces:

| model block | dimension | multiplicity | scalars on `(r,0),(0,r)` |
|---|---:|---:|---|
| `ker(X(r)-I)` | 2 | 1 | `(+,+)` |
| `ker(X(r)+I)` | 2 | 1 | `(-,+)` |

Each restricted block has four exact projective Weyl matrices with Gram
`2 I_4` and scalar commutant, hence is irreducible.  Twisting by all bottom
characters realizes all four radical scalar pairs `(+,+), (+,-), (-,+),
(-,-)`.  Distinct pairs are inequivalent; C4/C6 leave room for exactly these
four.  Therefore the standard 4-dimensional model contains two of the four
inequivalent 2-dimensional irreducibles, once each.

## C8 -- all submodules, Lagrangians, and labels

Submodules are discovered by closure under adjoining every cyclic submodule;
no line list is supplied to the search.

| `R` | submodule size histogram | Lagrangians total/free/non-free | labels |
|---|---|---|---:|
| `F2` | `1:1,2:3,4:1` | `3/3/0` | 6 |
| `F3` | `1:1,3:4,9:1` | `4/4/0` | 12 |
| `F4` | `1:1,4:5,16:1` | `5/5/0` | 20 |
| `Z4` | `1:1,2:3,4:7,8:3,16:1` | `7/6/1` | 28 |
| `F2[e]/e2` | `1:1,2:3,4:7,8:3,16:1` | `7/6/1` | 28 |

Perpendiculars are recomputed from the generating phase pairing, with
`|L||L^perp|=n^2` checked for every submodule.  The unique non-free witnesses
are `(2)+(2)` and `(e)+(e)`.  Characters of every `A_L` are exhaustively
solved in roots of unity of order equal to the group exponent; every
Lagrangian has exactly `n` of them, giving the displayed label totals.
