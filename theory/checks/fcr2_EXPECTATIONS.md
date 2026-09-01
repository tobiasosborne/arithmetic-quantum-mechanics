# FCR-2 falsifier expectations and discovered census

Lane model: gpt-5.6-sol, reasoning xhigh, codex exec.

These values come only from `briefs/fcr2-target.md`, its permitted FCR-1 and
field-regression conventions, and the independent computations described
below.  A passing row is a falsifier result, not a proof.  “N/A” is printed by
the checker rather than silently skipped.

## Exact representations, characters, and sampling

Every ring is materialized as complete integer `ADD` and `MUL` tables.
Equal-characteristic elements are little-endian polynomial coefficients.

| seed | additive group | defining multiplication | reference character | `|Gen|` |
|---|---|---|---|---:|
| `F2` | `C2` | field | `(-1)^a` | 1 |
| `F4` | `C2^2` | `u^2+u+1=0` | `(-1)^[u]` (the trace) | 3 |
| `Z4` | `C4` | integers mod 4 | `zeta4^a` | 2 |
| `F2[e]/e2` | `C2^2` | `e^2=0` | `(-1)^[e]` | 2 |
| `Z8` | `C8` | integers mod 8 | `zeta8^a` | 4 |
| `F2[t]/t3` | `C2^3` | `t^3=0` | `(-1)^[t^2]` | 4 |
| `GR(4,2)` | `C4^2` | `u^2+u+1=0` over `Z4` | `zeta4^[u]` | 12 |
| `F2[x,y]/(x,y)^2` | `C2^3` | `x^2=xy=y^2=0` | no generating character | 0 |

The mixed-characteristic phases all embed in
`Z[zeta_8]=Z[X]/(X^4+1)` as integer four-vectors.  In particular a character
of `Z/8` is already `mu_8`-valued and `epsilon` sums only those character
values: no `zeta_16` can appear.  Characteristic-two Gauss sums are ordinary
integer sums of signs.

The complete `|R|^3` cocycle torsor is used at every order-`<=8` seed.  At
`GR(4,2)`, G1--G3 use 128 triples selected by `Random(0xFC220+16)`, with
`(0,0,0)` forced into the sample.  This is 1/32 of the 4096 cocycles.  G4 is
not sampled: it evaluates all 4096 cocycles for all 12 generating characters.
The final green run takes about 35 seconds on the lane host, below the five-minute
budget.

## G1 — admission and corrected polarization

For

`beta=beta0+s_(alpha,gamma,delta)` and `Q(v)=beta(v,v)`, G1 checks

`beta-beta^T=omega`, and
`Q(v+w)-Q(v)-Q(w)=2 beta(v,w)-omega(v,w)`.

It exhausts all `|V|^2=|R|^4` pairs for every registered cocycle: 8 cocycles
times 16 pairs at `F2`; 64 times 256 at each order-4 seed; 512 times 4096 at
each order-8 seed; and 128 times 65,536 at `GR(4,2)`.

Independent cross-check: direct coefficient expansion gives
`Q(a,b)=alpha*a^2+(1+2 gamma)ab+delta*b^2`; its cross-difference is exactly
`2 beta-omega` without division by two.

Discriminating power: transposition changes `omega` to `-omega`, so the
registered transpose mutation is visible at `Z4`, `Z8`, and `GR(4,2)`, but
not at the characteristic-two seeds where `-omega=omega`.  It targets `Z4`.

## G2 — square law

For every G1 cocycle and all `|H|=|R|^3` elements, generic table
multiplication is compared with

`(t,v)^2=(2t+Q_beta(v),2v)`.

The formal Weyl consequence is the identical exponent statement
`W_beta(v)^2=psi(Q_beta(v))W_beta(2v)`.  The `Z8` red mutation replaces `Q`
by `2Q` and fails at `(t,v)=(0,9)` already for `beta0`.

Independent cross-check: bilinearity gives the general power formula
`(t,v)^k=(kt+binom(k,2)Q(v),kv)`, which is also the route used independently
by G3's powering census.

Discriminating power: every seed has cocycles with nonzero `Q`, so the wrong
coefficient can fail everywhere (and at the fixed order-16 sample).

## G3 — full `H_beta` equivalence census

For characteristic-two rings, `[H,H]=Z(H)=R x 0`.  The checker exhausts all
additive pairs `(h,g)` satisfying
`h(omega(v,w))=omega(gv,gw)`.  It then orbits the complete quadratic power
map by `h(Q(v))=Q'(gv)`.  Taking `h=id` gives centre-pointwise equivalence;
taking every additive automorphism of the centre gives abstract group
equivalence.  Thus no unproved R-linearity assumption enters the census.

For `Z4` and `Z8`, the independently checked presentation with
`z=[x,y]` has only the beta-dependent relators
`x^n=z^(n alpha/2)` and `y^n=z^(n delta/2)`.  The checker exhausts every
possible quotient image of `(x,y)`: determinant one for centre-pointwise
maps and every unit determinant for abstract maps.  The resulting generator
images compute the two parity-Arf orbits; odd centre similitudes do not merge
them.

### Discovered class counts

The two equivalences give the same sizes at every fully censused seed.

| seed | centre-fixed classes (sizes) | abstract classes (sizes) | pseudo-isometries checked |
|---|---|---|---:|
| `F2` | 2 (`6,2`) | 2 (`6,2`) | `6 / 6` |
| `F4` | 2 (`40,24`) | 2 (`40,24`) | `60 / 360` |
| `Z4` | 2 (`48,16`) | 2 (`48,16`) | `192 / 384` generator images |
| `F2[e]/e2` | 2 (`48,16`) | 2 (`48,16`) | `48 / 96` |
| `Z8` | 2 (`384,128`) | 2 (`384,128`) | `1536 / 6144` generator images |
| `F2[t]/t3` | 2 (`384,128`) | 2 (`384,128`) | `384 / 3072` |
| `F2[x,y]/(x,y)^2` | 2 (`384,128`) | 2 (`384,128`) | `384 / 9216` |
| `GR(4,2)` sample | 2 signature types (`89,39`) | 2 (`89,39`) | signatures only; not class counts |

The `GR(4,2)` numbers are sample populations, not estimates of the 4096-member
class sizes and not a complete isomorphism classification.

### Discovered order profiles

Profiles in each row are listed in the same order as the large/small class
when the correspondence is fixed by the reference representative.

| seed | profile A | profile B |
|---|---|---|
| `F2` | `{1:1,2:5,4:2}` | `{1:1,2:1,4:6}` |
| `F4` | `{1:1,2:27,4:36}` | `{1:1,2:3,4:60}` |
| `Z4` | `{1:1,2:7,4:40,8:16}` | `{1:1,2:7,4:8,8:48}` |
| `F2[e]/e2` | `{1:1,2:31,4:32}` | `{1:1,2:15,4:48}` |
| `Z8` | `{1:1,2:7,4:56,8:320,16:128}` | `{1:1,2:7,4:56,8:64,16:384}` |
| `F2[t]/t3` | `{1:1,2:159,4:352}` | `{1:1,2:31,4:480}` |
| non-Frobenius probe | `{1:1,2:191,4:320}` | `{1:1,2:127,4:384}` |
| `GR(4,2)` sample | `{1:1,2:63,4:1728,8:2304}` | `{1:1,2:63,4:192,8:3840}` |

Order profiles already separate the two observed types at every seed.  G3
nevertheless records the finer lift-power map.  Representative fingerprints
include: at `Z4`, quotient-order-4 lifts have fourth-power distribution
`0:32, 2:16` versus `2:48`; at `Z8`, quotient-order-8 lifts have eighth-power
distribution `0:256, 4:128` versus `4:384`; at the dual numbers the numbers
of lifts squaring to zero are `28` versus `12`; at `F2[t]/t3` they are `152`
versus `24`.

Centre and quotient order profiles provide a beta-independent check on the
arena: respectively `{1:1,2:3}` and `{1:1,2:15}` at additive `C2^2` seeds;
`{1:1,2:7}` and `{1:1,2:63}` at additive `C2^3` seeds; `{1:1,2:1,4:2}` and
`{1:1,2:3,4:12}` at `Z4`; and `{1:1,2:1,4:2,8:4}` and
`{1:1,2:3,4:12,8:48}` at `Z8`.

Independent cross-checks: each class-size list sums to `|Adm|=|R|^3`; every
profile sums to `|H|=|R|^3`; every element order divides the displayed group
exponent; the power fingerprints reproduce the same profiles via the general
power formula.  At `Z4`/`Z8`, the 3:1 sizes also follow independently from the
four parity pairs `(alpha mod 2,delta mod 2)`.

Discriminating power: the collapse mutation can fail at every seed because
two types occur throughout.  The wrong-profile fixture is targeted at the
dual numbers and has a different fingerprint from class collapse.

## G4 — exact Gauss invariant

For every beta and every generating character, G4 computes
`epsilon_psi(beta)=|R|^-1 sum_v psi(Q_beta(v))` by two exact routes: direct
summation and a histogram of the values of `Q`.  Coefficientwise division by
`|R|` must be exact, and the result must be one of the eight stored powers of
`zeta_8` (one of `+/-1` in characteristic two).

| seed | value set for every generating `psi` | constant on centre classes? | separates classes? |
|---|---|:---:|:---:|
| `F2` | `{+1,-1}` | yes | yes |
| `F4` | `{+1,-1}` | yes | yes |
| `Z4` | `{+1}` (`zeta8^0`) | yes | **no** |
| `F2[e]/e2` | `{+1}` | yes | **no** |
| `Z8` | `{+1,-1}` (`zeta8^{0,4}`) | yes | yes |
| `F2[t]/t3` | `{+1,-1}` | yes | yes |
| `GR(4,2)` | `{+1}` | yes on the 128-member G3 sample | no on that sample |
| non-Frobenius probe | N/A (`Gen=empty`) | N/A | N/A |

Thus the conjectural epsilon invariant does not separate the two minimal
thickened classes: this is a discovered negative datum, not a failed gate.

Independent cross-check: direct and histogram sums agree for every input;
field signs also agree with G5's zero-count/Arf census.  Discriminating power:
the fake-epsilon mutation is active at every Frobenius seed and is targeted at
`Z4`, where it changes `1` to `zeta8`.

## G5 — field regression

At `F2`, the required split is `6:2`, with profiles
`{1:1,2:5,4:2}` and `{1:1,2:1,4:6}` (the D4/Q8 profiles), zero counts `3,1`,
and epsilon signs `+1,-1`.  At `F4`, the two quadratic-form populations are
`q(q+1)/2=10` and `q(q-1)/2=6`; the four cocycles over each form give cocycle
classes `40:24`, zero counts `7,1`, profiles `{1:1,2:27,4:36}` and
`{1:1,2:3,4:60}`, and epsilon signs `+1,-1`.

Independent cross-check: form count times the `q` invisible gamma parameters
equals the G3 class sizes.  Discriminating power: only `F2` and `F4` reach G5;
the registered field mutation targets the `F4` split.

## G6 — trace-Gram and fixed model

For `beta0` and every generating character at `Z4`, the dual numbers, `Z8`,
and `F2[t]/t3`, the exact monomial matrices
`W(a,b)=Z(-b)X(a)` satisfy the Weyl relation on all ordered pairs.  Their
trace-Gram matrix is exactly `|R| I`: size `16x16` for the two order-4 seeds
and `64x64` for the two order-8 seeds.  Hence the `|R|^2` matrices are a basis
of `M_|R|` and their commutant is scalar.

Independent cross-check: unequal shifts have disjoint diagonal trace support;
equal shifts reduce to exact character orthogonality.  Discriminating power:
G6 is active only at the four named seeds.  The plus-sign model mutation is
visible at `Z4` and `Z8`, but sign is invisible in characteristic two; it is
targeted at `Z4`.

## G7 — no antisymmetric member

Antisymmetry of the coefficient matrix would require
`2 alpha=2 delta=0` and `1+2 gamma=0`.  The last equation has no solution in a
local ring with residue characteristic two.  G7 exhausts all `|R|^3`
coefficient triples at every seed, including all 4096 at `GR(4,2)`, and finds
zero antisymmetric members.  It separately exhausts the multiplication table
and finds no inverse of `2`.

Independent cross-check: reducing `1+2 gamma=0` modulo the maximal ideal gives
`1=0`, impossible in every explicit residue field.  Discriminating power: G7
is active everywhere.  The half-Weyl mutation invents an inverse of doubling
at `Z4`; unlike the FCR-1 odd-seed mutation, it fails before any coboundary
formula can be formed.

## G8 — non-Frobenius probe

The seven nontrivial additive characters of `F2[x,y]/(x,y)^2` are exhausted.
Six have a kernel ideal of size 2 and one has the maximal ideal of size 4;
none has `I_psi=0`, so `Gen=empty`.

Independent cross-check: every linear functional on the two-dimensional
square-zero socle has a nonzero kernel.  Discriminating power: G8 is active
only at this probe, where the Frobenius-blind mutation claims one generating
character.
