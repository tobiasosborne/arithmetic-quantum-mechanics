<!-- ROLE: Lamport shard (L6b), prover pass for briefs/fcr2-target.md.
     No trunk files are edited here; D17--D20 and claim rows are proposed in
     PATCH.md.  Census values are regression targets only, never proof leaves. -->

# `fcr2-beta` — dyadic polarizing cocycles and their Gauss sums

Lane model: `gpt-5.6-sol`, reasoning `xhigh`, `codex exec`.

Throughout, `D12`--`D16` are in force, `R` is a finite commutative local
ring, `V=R^2`, and `2 in m` unless a statement says otherwise.  The proposed
`D17`--`D21` name the quadratic datum, Gauss sum, three equivalence levels,
additive exponent, and chain length.  Results from `theory/wh-kappa.md`,
`theory/wh-kappa-choice.md`, and `theory/fcr-local.md` are ported only where
the calculation is repeated below.  The promoted checker
`theory/checks/fcr2_beta_check.py` supplies falsification targets, not proof.

## 0. Elementary leaves and normal forms

**L-ORTH.**  **ASSUME** a finite abelian group `G` and a nontrivial character
`chi:G->C^x`.  **PROVE** `sum_G chi=0`.

`<1>1.` Choose `h` with `chi(h)!=1`.  Translation gives
`S=sum_g chi(g+h)=chi(h)S`, hence `S=0`.  This re-derives
`theory/fcr-local.md` `L-ORTH`.  **QED**

**L-LIFT.**  **ASSUME** `m^n=0`, a polynomial `F` over `R`, and a residue
zero `x_0` at which one partial derivative is a unit.  **PROVE** that `x_0`
lifts to an exact zero, with the other coordinates held fixed.

`<1>1.` `m` is nilpotent by `FCR-GEN`, via `theory/fcr-local.md`
`L-LOCAL <1>1`.  If `F(x_r) in m^r` and `u=partial F(x_r)` is a unit, put
`c=-F(x_r)u^{-1} in m^r` in that coordinate.  Polynomial expansion gives
`F(x_r+c)=F(x_r)+uc+c^2G`, hence a value in `m^{r+1}` because
`m^{2r} subset m^{r+1}` for `r>=1`.  Iterate to `m^n=0`; corrections in
`m` preserve the residue point and the unit derivative.  **QED**

**L-NORM.**  **ASSUME** `S/R` is quadratic finite etale and local, with
residue extension `K/k` of degree two.  **PROVE** `N:S^x->R^x` is onto.

`<1>1.` `K^x` is cyclic: if `e` is the exponent of the finite subgroup
`K^x`, every element is a root of `X^e-1`, so `|K^x|<=e`; the reverse
inequality follows from Lagrange and an element of exponent `e`, obtained by
multiplying maximal-order elements in the primary factors.  Thus the norm
`z |-> z^(q+1)` from the cyclic group of order `q^2-1` has image of order
`q-1`, all of `k^x`.  This is an elementary derivation, not a cited field
classification; the cyclic prime-power decomposition used in the one group
step is also recorded in Strömberg `refs/arxiv-1108.0202/`, §On Jordan
decompositions, before `eq:Jordan-decomposition`.

`<1>2.` Lift a residue norm preimage.  Suppose inductively
`N(z)=u mod m^r`.  On `m^rS/m^{r+1}S`, trace is
`id tensor Tr_{K/k}`; it is onto because, for a residue root of
`T^2+T+c`, its trace is `1`.  Choose `x in m^rS` with
`Tr(x)=u/N(z)-1 mod m^{r+1}`.  Then
`N(1+x)=1+Tr(x)+N(x)=u/N(z) mod m^{r+1}`, since
`N(x) in m^{2r}`.  Nilpotence from `FCR-GEN` terminates the induction.
**QED**

**L-QNF.**  **ASSUME** a map
`q(a,b)=A a^2+Uab+D b^2`, with `U in R^x`.  Its polar form is
`b_q(v,w)=q(v+w)-q(v)-q(w)`.  **PROVE**:
(a) `b_q` is unimodular; (b) exact `GL_2(R)`-isometry classes are exactly
the two residue Arf types; (c) modulo a centre-fixing cocycle coboundary,
the same two types have oriented normal forms `ab` and
`a^2+ab+d_*b^2`, where `bar d_*` is any fixed nonzero class in
`k/℘(k)`.

`<1>1.` The polar matrix is `[[2A,U],[U,2D]]`, with determinant
`4AD-U^2 congruent -bar U^2 !=0 mod m`; it is invertible by the local unit
criterion in `theory/fcr-local.md` `L-LOCAL <1>5`.  This proves (a).

`<1>2.` Scale the second variable by `U^{-1}` to reduce exact-isometry
questions to `q=Aa^2+ab+Db^2`.  Its residue polar form is `omega`.
The map `℘(x)=x^2+x` is additive with kernel `{0,1}`, so its image has
`q/2` elements and `k/℘(k)` has two.  If `bar A=0`, the form has an axis
zero.  If `bar A!=0`, a zero with second coordinate one is equivalent, after
multiplication by `bar A`, to
`℘(bar A a)=bar A bar D`.  Thus the residue is isotropic exactly when
`bar A bar D in ℘(k)`.  This repeats, rather than assumes, the field
calculation in `WH-BETA §6 <1>4`.

`<1>3.` In the isotropic case choose a nonzero residue zero.  Its polar row
is nonzero by `<1>1`, so `L-LIFT` gives a primitive `e` with `q(e)=0`.
Choose `f` with `b_q(e,f)=1` and replace it by `f-q(f)e`; then both axis
values vanish and `q(ae+bf)=ab`.  The two vectors form a basis because
their polar pairing is a unit.  This is the exact hyperbolic normal form.

`<1>4.` In the anisotropic case `A,D` are units and
`q(a,Ay)=A(a^2+ay+ADy^2)`.  Put
`S_c=R[T]/(T^2-T+c)`, `c=AD`.  Its derivative `2T-1` is a unit and its
residue polynomial is irreducible by `<1>2`, so `S_c/R` is quadratic finite
etale and local; its norm is `N(a+yT)=a^2+ay+cy^2`.

`<1>5.` Any two `c,c'` with anisotropic residues give isomorphic algebras:
inside `S_c`, lift a residue root of `X^2-X+c'` by `L-LIFT`; evaluation
gives an isomorphism after reduction, hence an isomorphism over `R` because
its `2 x 2` determinant is a unit.  Algebra isomorphisms preserve the norm
(the determinant of multiplication).  By `L-NORM`, multiplication by a
unit of prescribed norm removes the leading unit `A`.  Thus all anisotropic
forms are exactly isometric, proving (b); the two types cannot be isometric
because isotropy survives reduction.

`<1>6.` For the oriented statement, in the hyperbolic case the lifting in
`<1>3` may choose `f_0` with `omega(e,f_0)=1`; its `b_q`-pairing is a unit,
and `f=f_0+c e`, with `c=-q(f_0)/b_q(e,f_0)`, makes `q(f)=0`.  Hence `(e,f)`
is a symplectic basis with zero axis values.  In any symplectic basis the
remaining symmetric cross term `gamma(ab'+a'b)` is the coboundary of
`f_gamma(a,b)=gamma ab`.

`<1>7.` In the anisotropic case the variable scaling in `<1>2`, the norm
description, and `L-NORM` show directly that `q` represents every unit; in
particular there is a primitive `e` with `q(e)=1`.  Choose `f_0` with
`omega(e,f_0)=1`.  Then
`q(f_0+ce)=q(f_0)+c b_q(e,f_0)+c^2`; the derivative in `c` is a unit.
The residue Arf condition puts `bar d_*-bar q(f_0)` in the image of
`x^2+x`, so `L-LIFT` supplies `c` making `q(f_0+ce)=d_*`.  The remaining
cross coefficient is again the coboundary in `<1>6`.  This proves (c).
**QED** (`L-QNF`)

## 1. FCR2-NOANTI — the dyadic torsor has no antisymmetric point

**ASSUME** `D12`,`D14`,`D15` and `2 in m`.  **PROVE** `Adm(omega)` is a
`Sym_R(V)`-torsor of size `|R|^3` and contains no antisymmetric member.

`<1>1.` If `beta,beta'` are admissible, `beta'-beta` is symmetric; adding
any symmetric form preserves admissibility.  The action is free and
transitive, and `beta_0` witnesses nonemptiness (`D15`).  Three free matrix
entries give `|R|^3`.  This ports `FCR-BETA-ODD <1>1` by repeating the
argument; no half was used.  **QED**

`<1>2.` If `beta` were antisymmetric, admissibility would give
`omega=beta-beta^T=2beta`.  At the standard basis this reads
`1=2beta(e,f)`, making `2` a unit, contrary to `2 in m` and
`theory/fcr-local.md` `L-LOCAL <1>5`.  **QED** (`FCR2-NOANTI`)

## 2. FCR2-Q — the corrected quadratic and square identities

**ASSUME** proposed `D17`, and any residue characteristic unless displayed.
**PROVE** the polarization, coboundary, square, Weyl-square, and transport
identities.

`<1>1.` Bilinearity and `beta(w,v)=beta(v,w)-omega(v,w)` (`D15`) give
`Q_beta(v+w)-Q_beta(v)-Q_beta(w)=2beta(v,w)-omega(v,w)`.  For symmetric
`s`, the definition gives `Q_{beta+s}(v)=Q_beta(v)+s(v,v)`.  **QED**

`<1>2.` Multiplying `(t,v)` by itself in `D16` gives
`(t,v)^2=(2t+Q_beta(v),2v)`; multiplying `W_beta(v)` by itself gives
`W_beta(v)^2=psi(Q_beta(v))W_beta(2v)`.  Neither simplification `2v=0`
nor a half has been used.  **QED**

`<1>3.` For `g in SL_2(R)`, put `beta^g(v,w)=beta(gv,gw)`.  Since
`omega(gv,gw)=det(g)omega(v,w)=omega(v,w)` by direct `2 x 2` expansion,
`beta^g` is admissible and `Q_{beta^g}=Q_beta o g`.  The coordinate map
`(t,v)|->(t,gv)` identifies `H_{beta^g}` with `H_beta` and fixes the centre.
**QED** (`FCR2-Q`)

## 3. FCR2-ALG0 — the reference algebra in every residue characteristic

**ASSUME** `D12`--`D16`, `psi in Gen(R)`, and `beta=beta_0`; no parity
hypothesis.  **PROVE** scalar centre, simplicity, dimension `|R|^2`, the
fixed realization `M_|R|(C)`, and Stone--von Neumann.

`<1>1.` `FCR-COMM` gives
`W(u)W(v)W(u)^{-1}=psi(omega(u,v))W(v)`.  For
`E(x)=|V|^{-1}sum_u W(u)xW(u)^{-1}`, `FCR-RAD` and `L-ORTH` therefore give
`E(sum_v a_vW(v))=a_0 1`.  A central element is scalar; averaging a shifted
nonzero coefficient of an ideal puts a nonzero scalar in it.  Thus the
algebra is central simple.  This re-derives the parity-free part of the port
`FCR-ALG <1>1`--`<1>4`.  **QED**

`<1>2.` The Weyl basis in `D16` has `|R|^2` elements.  On `l^2(R)`, direct
use of `X(a)Z(-b')=psi(ab')Z(-b')X(a)` shows
`Z(-b)X(a)Z(-b')X(a')=psi(ab')Z(-b-b')X(a+a')`.  Hence the fixed model is a
nonzero representation; simplicity makes it injective, and equal dimensions
make it `A_{psi,beta_0}=End_C(l^2(R))`, noncanonically `M_|R|(C)` after a
basis ordering.  This repeats `FCR-ALG <1>5`--`<1>6`, where no half occurs.
**QED**

`<1>3.` The column argument in `FCR-SVN <1>2` now applies verbatim: the full
endomorphism algebra has one simple module, of dimension `|R|`; Schur's
eigenvalue argument gives scalar intertwiners, averaging an inner product over
the finite group gives unitarity, and twisting the module proves every algebra
automorphism inner.  Representations of `H_{beta_0}` with centre `psi` are
exactly these modules by `D16`.  **QED** (`FCR2-ALG0`)

## 4. FCR2-CLASS — two group classes at the registered seeds

Write `beta=beta_0+s` with symmetric matrix
`s=[[alpha,gamma],[gamma,delta]]`.  Then
`Q_beta(a,b)=alpha a^2+(1+2gamma)ab+delta b^2` by `FCR2-Q`.

`<1>1.` Reduction modulo `m` is well defined and equals
`bar Q_beta(a,b)=bar alpha a^2+ab+bar delta b^2`, with polar form
`bar omega`.  By the re-derived field calculation `L-QNF <1>2`,
`Arf(bar Q_beta)=bar alpha bar delta in k/℘(k)` is basis-independent and
has exactly two values.  It is unchanged by `gamma` and by changing lifts.
**QED**

`<1>2.` `L-QNF <1>6`--`<1>7` is an explicit centre-fixing construction.
For each `beta`, it produces a symplectic basis `g=[e f]`, a cross coefficient
`gamma_g`, and a normal cocycle `beta_+` or `beta_-`; the map
`Theta_beta(t,(a,b))=(t+gamma_g ab,g(a,b))` is an isomorphism from that normal
group to `H_beta`.  The lift corrections and norm corrections in `L-LIFT`
and `L-NORM` are finite algorithms.  Therefore equal residue Arf gives the
explicit isomorphism `Theta_beta' o Theta_beta^{-1}`, fixing `R x 0`
pointwise.  In particular it also gives an abstract isomorphism.  **QED**

`<1>3.` The two fibres have the asserted sizes.  There are
`q(q+1)/2` hyperbolic pairs `(bar alpha,bar delta)` and `q(q-1)/2`
anisotropic pairs by the count in `WH-BETA §6 <1>5`: for `bar alpha=0`
there are `q` choices, and for each nonzero `bar alpha` exactly `q/2`
choices put the product in `℘(k)`.  Multiplying by `|m|^2` lifts and by
the free `|R|` choices of `gamma` gives
`|R|^3(q+1)/(2q)` and `|R|^3(q-1)/(2q)`.  **QED**

`<1>4.` To prove that the two normal groups are not even abstractly
isomorphic at the eight registered seeds, induction gives the section-free
power formula
`(t,v)^j=(jt+binom(j,2)Q_beta(v),jv)`.  Counting its solutions produces the
following element-order profiles; unequal rows are abstract invariants.

| `R` | hyperbolic profile | anisotropic profile |
|---|---|---|
| `F_2` | `1:1, 2:5, 4:2` | `1:1, 2:1, 4:6` |
| `F_4` | `1:1, 2:27, 4:36` | `1:1, 2:3, 4:60` |
| `Z/4` | `1:1, 2:7, 4:40, 8:16` | `1:1, 2:7, 4:8, 8:48` |
| `F_2[e]/e^2` | `1:1, 2:31, 4:32` | `1:1, 2:15, 4:48` |
| `Z/8` | `1:1, 2:7, 4:56, 8:320, 16:128` | `1:1, 2:7, 4:56, 8:64, 16:384` |
| `F_2[t]/t^3` | `1:1, 2:159, 4:352` | `1:1, 2:31, 4:480` |
| `GR(4,2)` | `1:1, 2:63, 4:1728, 8:2304` | `1:1, 2:63, 4:192, 8:3840` |
| `F_2[x,y]/(x,y)^2` | `1:1, 2:191, 4:320` | `1:1, 2:127, 4:384` |

`<1>5.` Here are the count leaves, independent of the census.  In
characteristic two, the profile is
`1:1, 2:|R||Q^{-1}(0)|-1, 4:|R|^3-|R||Q^{-1}(0)|`.  For a chain ring
`k[t]/t^l`, hyperbolic `ab` has
`q^(l-1)(q+l(q-1))` zeros, while the anisotropic norm has
`q^(2 floor(l/2))`; valuation strata give both formulas.  For the square-zero
non-Frobenius ring, unit/nonunit cases give `24` versus `16` zeros.  For
`Z/2^l`, substituting `j=1,2,4,...` in `<1>4` gives cumulative counts
`(1,8,48,64)` versus `(1,8,16,64)` at `l=2`, and
`(1,8,64,384,512)` versus `(1,8,64,128,512)` at `l=3`.
For `GR(4,2)`, writing each element in its two Teichmueller digits gives
`(1,64,1792,4096)` versus `(1,64,256,4096)`.  Successive differences are
exactly the table.  **QED**

`<1>6.` Thus, at every registered seed, the two Arf fibres are exactly the
two centre-fixed classes and exactly the two abstract classes, with the sizes
in `<1>3`.  The within-class theorem and fibre sizes hold for every finite
local dyadic `R`; abstract separation outside the eight seeds is not claimed.
**QED** (`FCR2-CLASS`)

## 5. FCR2-EPS — the finite-quadratic-module bridge and the true separator

**ASSUME** proposed `D18`, `psi in Gen(R)`, and any `beta`.  **PROVE**
`epsilon_psi(beta) in {+1,-1}`, independence of `psi`, class constancy, and
the separation criterion below.

`<1>1.` Let `e:Q/Z -> mu_infinity`, `x |-> exp(2 pi i x)`.  There is a unique
`q_tilde:V->Q/Z` with `e(q_tilde(v))=psi(Q_beta(v))`.  Integer homogeneity of
`Q_beta` gives `q_tilde(nv)=n^2q_tilde(v)`.  Its polar phase is, critically,
`psi(2beta(v,w)-omega(v,w))` by `FCR2-Q`, not the commutator phase.
The polar matrix is the unit-determinant matrix of `L-QNF <1>1`; if a vector
were in its phase radical, its nonzero image ideal would lie in `ker psi`,
contrary to `D13`.  Hence `(V,q_tilde)` is a finite quadratic module exactly
in the sense of Strömberg, `refs/arxiv-1108.0202/`, paragraph defining an
FQM before §On Jordan decompositions, and Ehlen--Skoruppa
`refs/arxiv-1705.04572/invariants.tex:141-155`.  This constructs the ledger's
warned-about bridge rather than assuming it.  **QED**

`<1>2.` Strömberg's `eq:milgrams_formula` states and then proves for every
FQM that `|V|^{-1/2}sum_v e(q_tilde(v))` is an eighth root of unity
(`refs/arxiv-1108.0202/`, labels `eq:milgrams_formula` and
`lem:gauss_sum_eq_gamma_p`).  Since `sqrt(|V|)=|R|`, this is precisely
`epsilon_psi(beta) in mu_8`.  Ehlen--Skoruppa give the same displayed formula
at `invariants.tex:169-178`.  **QED**

`<1>3.` There is a direct strengthening.  By exact `GL_2` classification
`L-QNF(b)`, the sum depends only on residue type.  The hyperbolic normal form
gives `sum_{a,b}psi(ab)=|R|` by `L-ORTH` and generation (`D13`).  Also `-Q`
has the same residue type and hence is exactly isometric to `Q`; therefore
the sum equals its complex conjugate.  Its normalized absolute value is one
by `<1>2`, so it is `+1` or `-1`, with hyperbolic sign `+1`.  **QED**

`<1>4.` Every generating character is `psi_u`, uniquely for `u in R^x`, by
`FCR-GEN`.  The forms `Q` and `uQ` have unit polar forms and the same
isotropic/anisotropic residue type; `L-QNF(b)` makes them exactly isometric.
Thus `epsilon_{psi_u}(beta)=epsilon_psi(beta)`.  Equal Arf classes are also
exactly isometric, so epsilon is constant on the two classes of
`FCR2-CLASS`.  **QED**

`<1>5.` With `T(R)` and `C_psi(R)` as in proposed `D18`,
`C_psi(R)=sum_{a,b in T(R)}psi(ab)`.  Sum the unnormalized Gauss sums of
`Aa^2+ab+Db^2` over all `(A,D) in R^2`.  `L-ORTH` and `D13` make the `A`-sum
equal `|R|` exactly when `a^2=0`, and similarly for `D`; hence the total is
`|R|^2 C_psi(R)`.  On the other hand, the type counts in
`FCR2-CLASS <1>3`, the hyperbolic value `|R|`, and anisotropic value
`sigma|R|` give the same total.  Solving yields
`sigma=+1 iff C_psi(R)=|R|`, and
`sigma=-1 iff C_psi(R)=|m|`.  Thus epsilon separates exactly in the second
case.  By `<1>4` this criterion is independent of the chosen generating
character.  **QED**

`<1>6.` If `R` is a finite chain ring of length `ell` (`D21`), then
`T(R)=m^ceil(ell/2)`, `T(R)^2=0`, and
`|T(R)|=q^floor(ell/2)` by valuation.  Therefore
`C_psi(R)=q^(2 floor(ell/2))`: epsilon separates iff `ell` is odd.  It separates
for fields and length `3`, but is identically `+1` on both classes at every
even length, including `Z/4`, `F_2[e]/e^2`, and `GR(4,2)`.  In particular,
“length at least three” is false at length four; odd length is the sharp
chain-ring statement.  **QED** (`FCR2-EPS`)

## 6. FCR2-LEVEL — identity-labelled frame transport

Let `N` be the exponent of `(R,+)` (`D20`), and `s=beta'-beta`.
**PROVE** a frame transport always exists with phases in `mu_{2N}`, and give
the exact `mu_N` criterion.

`<1>1.` Multiplicativity of `W_beta(v)|->mu(v)W_beta'(v)` is exactly
`mu(v)mu(w)/mu(v+w)=psi(-s(v,w))` `(dagger)`, by `D16`.  Choose a cyclic
decomposition `V=directsum_i <b_i>`, `ord(b_i)=n_i`; existence of such a
prime-power decomposition is recorded in Strömberg
`refs/arxiv-1108.0202/`, §On Jordan decompositions, before
`eq:Jordan-decomposition`.  **QED**

`<1>2.` For canonical coordinates `0<=k_i<n_i`, put
`F(k)=sum_i binom(k_i,2)s(b_i,b_i)+sum_{i<j}k_i k_j s(b_i,b_j)`.
Choose `rho_i` with
`rho_i^{n_i}=psi(-binom(n_i,2)s(b_i,b_i))`, and define
`mu(sum_i k_i b_i)=prod_i rho_i^{k_i} psi(F(k))`.
Changing `k_i` by `n_i` changes `F` by
`binom(n_i,2)s(b_i,b_i)` because `n_i s(b_i,b_j)=0`; hence the formula is
well defined.  The polynomial identity
`F(k+l)-F(k)-F(l)=s(v,w)` proves `(dagger)`.  **QED**

`<1>3.` The right side defining `rho_i` has square one, since
`n_i s(b_i,b_i)=0`.  A root can therefore be chosen in `mu_{2n_i}`, hence
in `mu_{2N}` (roots exist in `C`, the coefficient-field fact named in
`theory/wh-kappa.md` §0).  A `mu_N` solution exists iff, for every cyclic
basis element, that displayed right side has an `n_i`-th root in `mu_N`:
necessity follows by restricting `(dagger)` to `<b_i>`, and sufficiency is
the formula in `<1>2`.  If the test fails, `mu_{2N}` still works.  **QED**

`<1>4.` At a characteristic-two field `N=2`; the criterion says `mu_2`
works exactly when `psi o Q_beta=psi o Q_beta'`, and `mu_4` always works,
recovering the statement of `WH-BETA-LEVEL` without using its SKETCH
register as evidence.  **QED** (`FCR2-LEVEL`)

## 7. FCR2-REG — clause-level characteristic-two field compatibility

**ASSUME** `R=k` is a finite field of characteristic two.  **PROVE** the
following comparisons at the trunk rows' current registers.

| this shard | trunk clause | comparison |
|---|---|---|
| `FCR2-NOANTI` | `WH-BETA-a,c` | torsor and no-antisymmetric clauses recovered on the nose; both trunk clauses are PROVED |
| `FCR2-Q` | `D6`, `WH-BETA-d` | polarization becomes `Q(v+w)-Q(v)-Q(w)=omega(v,w)` and the square has `2t=2v=0`; recovered on the nose |
| `FCR2-ALG0` | `WH-ALG`, `WH-ALG-MAT`, `WH-SVN` at `beta_0` | every listed algebra/SvN clause recovered; trunk rows are PROVED |
| `FCR2-CLASS` | `D10`, `WH-BETA-TYPE` | Arf, two types, sizes, and group classification agree; the trunk row is SKETCH, so this is consistency, not evidence from it |
| `FCR2-EPS` | `WH-BETA-EPS` | field signs are `+1/-1` and separate; the trunk row is SKETCH, so only consistency is asserted |
| `FCR2-LEVEL` | `WH-BETA-LEVEL` | `N=2` gives the identical `mu_2` iff / `mu_4` always clauses; the trunk row is SKETCH, so only consistency is asserted |

`<1>1.` Each entry follows by the displayed specialization and the cited
step; no SKETCH row is used as a premise.  The comparison does not claim a
Weil action, direct sums, non-Frobenius quantization, or any equivalence finer
than the three levels of `D19`.  **QED** (`FCR2-REG`)

## 8. Evidence and scope ledger

`<1>1.` The only source-dependent theorem used for `FCR2-EPS` is Milgram's
formula after the bridge is constructed in §5 `<1>1`; `FCR2-LEVEL` uses the
cyclic-decomposition statement at the displayed Strömberg locator.  Algebra
steps are explicit ports with their ring calculations repeated.  No census
number is a proof leaf.  **QED**

`<1>2.` General abstract separation of the two normal groups beyond the eight
registered seeds remains open.  `FCR2-CLASS` proves general explicit
centre-fixed isomorphisms within each fibre and exact abstract separation at
the seeds.  No dynamics, direct sums, schemes, or non-Frobenius quantization
is claimed.  **QED**
