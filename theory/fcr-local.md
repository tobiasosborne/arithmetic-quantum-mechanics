<!-- ROLE: Lamport shard (L6b) for briefs/fcr-local-target.md; survived the
     capped loop, see theory/verdicts/fcr-local-r1.md and -adjudication.md. -->

# `fcr-local` — finite commutative local rings, odd residue characteristic

Lane model: `gpt-5.6-sol`, reasoning `xhigh`, `codex exec`.

Throughout, `D12`--`D16` are the convention groups in `definitions.md`.
Thus `R` is a finite commutative unital local ring with maximal
ideal `𝔪`, residue field `κ=R/𝔪`, and `q=|κ|`.  Definitions are uniform in the
residue characteristic.  A theorem using a half explicitly assumes
`2∈R^×`; this is equivalent here to odd residue characteristic because the
local unit criterion proved in `L-LOCAL <1>5` says that `2` is a unit exactly
when its image in `κ` is nonzero.  The fixed model convention is, without any
change of sign,

`W_{β₀}(a,b)=Z(−b)X(a)` on `ℓ²(R)` (`D16`).

No source is used as a black box except at its displayed locator.  In
particular, the field arguments are ported from `theory/wh-kappa.md` and
`theory/wh-kappa-choice.md` only where the displayed ring calculation below
re-proves them.

## 0. Elementary leaves

**L-ORTH.**  **ASSUME** a finite abelian group `G` and a nontrivial character
`χ:G→C^×`.  **PROVE** `Σ_{g∈G}χ(g)=0`.

`<1>1.` Choose `h` with `χ(h)≠1`; translating the sum gives
`S=Σ_gχ(g+h)=χ(h)S`, and `1−χ(h)≠0`.  **QED** (`L-ORTH`)

**L-LOCAL.**  **ASSUME** `D12`.  **PROVE**: `𝔪` is nilpotent,
`soc(R)≠0`, every nonzero ideal contains a minimal ideal, every minimal ideal
is a one-dimensional `κ`-subspace of `soc(R)`, and every non-unit is a zero
divisor.

`<1>1.` A finite ring is Artinian because every descending chain of its finite
set of ideals terminates.  Its Jacobson radical is nilpotent by
`refs/stacks-algebra/algebra.tex:12739-12756`
(`lemma-artinian-radical-nilpotent`); the radical is `𝔪`, the unique maximal
ideal (`D12`).

`<1>2.` Let `n≥1` be minimal with `𝔪^n=0`.  If `𝔪=0`, then
`soc(R)=Ann(0)=R≠0`.  Otherwise `0≠𝔪^{n−1}⊆Ann(𝔪)=soc(R)` by `<1>1`.

`<1>3.` A nonzero ideal contains an inclusion-minimal nonzero ideal `J` because
the ideal poset is finite (`D12`).  Minimality makes `𝔪J` either `0` or `J`.
The latter would give `J=𝔪^nJ=0` by iteration and `<1>1`; hence
`J⊆soc(R)`.

`<1>4.` The action on `J` factors through `κ=R/𝔪` by `<1>3`, so `J` is a
`κ`-vector space.  A nonzero proper `κ`-subspace would be an `R`-ideal,
contrary to minimality; hence `dim_κJ=1`.

`<1>5.` In a local ring the non-units are exactly `𝔪`: a non-unit generates a
proper ideal, hence lies in the unique maximal ideal, and no element of a
proper ideal is a unit.  If `x∈𝔪` and multiplication by `x` on the finite set
`R` were injective, it would be surjective, giving `xr=1`; therefore it has a
nonzero kernel.  **QED** (`L-LOCAL`)

**L-ANN.**  **ASSUME** `D12`,`D13` and `ψ∈Gen(R)`.  **PROVE**, for every ideal
`I`,
`|I||Ann(I)|=|R|` and `Ann(Ann(I))=I`.

`<1>1.` Put `S=Σ_{r∈R,i∈I}ψ(ri)`.  Summing first over `r` gives `S=|R|`:
for `i=0` the inner sum is `|R|`; for `i≠0`, triviality of `r↦ψ(ri)` would put
the nonzero ideal `iR` in `ker ψ`, contradicting `I_ψ=0` (`D13`), so
`L-ORTH` makes that sum zero.

`<1>2.` Summing first over `i` gives `S=|Ann(I)||I|`: if
`r∉Ann(I)`, then `rI` is a nonzero ideal and the character on `I` cannot be
trivial by `D13`; apply `L-ORTH` again.  Compare with `<1>1`.

`<1>3.` Always `I⊆Ann(Ann(I))`.  Applying `<1>2` twice gives equal
cardinalities, hence equality.  **QED** (`L-ANN`)

## 1. FCR-GEN — generating characters and the local Frobenius criterion

**ASSUME** `D12`,`D13`.  **PROVE** `Gen(R)≠∅` iff `soc(R)` is simple, equivalently
one-dimensional over `κ`; if `ψ∈Gen(R)`, then `ψ_u` is generating exactly for
`u∈R^×`, and `Gen(R)` is a free transitive `R^×`-set.  For `R=κ`, it has
`q−1` elements and is the character torsor in `WH-CHOICE`.

`<1>1.` Wood's definition reduces, in this local commutative case, to
`R/𝔪≅soc(R)` as `R`-modules.

`<2>1.` Wood defines the principal indecomposable top and socle and the QF and
Frobenius conditions at
`refs/wood-ajm-1999/wood_duality_ajm121_1999.txt:107-147`.

`<2>2.` A local ring has only idempotents `0,1`: if `e²=e`, then one of `e` and
`1−e` is a unit (otherwise both lie in `𝔪`), forcing the other to be zero.
Thus Wood's principal decomposition has the single summand `R`, with
multiplicity one, top `R/Rad(R)=R/𝔪=κ`, and module socle `S({}_RR)` in
Wood's notation.

`<2>3.` Wood's module socle `S({}_RR)` is exactly `Ann(𝔪)`.  For one
inclusion, every irreducible submodule `J⊆R` is a simple ideal.  Then `𝔪J`
is either `0` or `J`; the latter would imply `J=𝔪^nJ=0` for a nilpotence
exponent from `L-LOCAL <1>1`, so `J⊆Ann(𝔪)`.  The sum of all such `J`, which
is Wood's `S({}_RR)`, therefore lies in `Ann(𝔪)`.  Conversely, if
`0≠x∈Ann(𝔪)`, the action on `Rx` factors through `κ`; moreover a nonzero
scalar in `κ` lifts to a unit and cannot kill `x`, so `Rx=κx` is
one-dimensional over `κ` and hence simple.  Thus every such `x` belongs to
Wood's module socle, proving `Ann(𝔪)⊆S({}_RR)` as well.  By `D12`, this common
module is `soc(R)`.

`<2>4.` Hence the permutation and multiplicity clauses in Wood are vacuous,
and his Frobenius condition is exactly `κ≅soc(R)`.  If `soc(R)` is simple,
choose `0≠s` in it; `R→soc(R)`, `r↦rs`, is onto and has a maximal kernel,
which must be the unique `𝔪`, so it induces `κ≅soc(R)`.  Conversely such an
isomorphism makes `soc(R)` simple.  This derives the socle criterion rather
than reading it into the source.  By `L-LOCAL <1>4`, simplicity is equivalent
to `dim_κsoc(R)=1`.

`<1>2.` Wood's Theorem 3.10 identifies finite Frobenius rings with those whose
character module is isomorphic to `R`
(`refs/wood-ajm-1999/wood_duality_ajm121_1999.txt:492-504`), and his §4 defines
this isomorphism by `u↦ψ_u`
(`:556-562`).  Lemma 4.1 says precisely that it is an isomorphism iff
`ker ψ` contains no nonzero ideal (`:570-581`), which is `I_ψ=0` (`D13`).
Together with `<1>1`, this proves `Gen(R)≠∅` iff `soc(R)` is simple.

`<1>3.` Fix `ψ∈Gen(R)`.  If `u` is a unit and an ideal `J` lies in
`ker ψ_u`, then the ideal `uJ` lies in `ker ψ`; hence `J=0` by `D13`.
If `u` is a non-unit, then `u∈𝔪` by `L-LOCAL <1>5`, so
`u·soc(R)=0`; the nonzero ideal `soc(R)` from `L-LOCAL <1>2` lies in
`ker ψ_u`.  Thus `ψ_u` is generating iff `u∈R^×`.

`<1>4.` By the character-module isomorphism in `<1>2`, every additive
character is uniquely `ψ_u` for some `u∈R`.  Combining with `<1>3`, every
generating character is uniquely obtained for a unit.  Thus the unit action is
free and transitive.

`<1>5.` If `R=κ`, then `𝔪=0`, `soc(R)=κ`, and all nontrivial characters are
generating because the only ideals are `0,κ`.  The free orbit has
`|κ^×|=q−1`, exactly `WH-CHOICE`.  **QED** (`FCR-GEN`)

**C-PROBE.**  **ASSUME** `R=F_3[x,y]/(x,y)^2` and the parametrization below.
**PROVE** every nontrivial additive character has a nonzero ideal kernel, with
the exact census required by the brief.

`<1>1.` Write
`ψ_{a,b,c}(r+sx+ty)=ζ_3^{ar+bs+ct}`.  Of the `26` nontrivial characters, the
two with `(b,c)=(0,0)` have `I_ψ=(x,y)`; each of the other `24` has
`I_ψ=F_3(cx−by)`.  Indeed every subspace of `(x,y)` is an ideal because its
square is zero, and no ideal containing a unit lies in a nontrivial kernel.
These are all characters because the additive group has basis `(1,x,y)` over
`F_3`, a character is determined by three freely chosen values in `μ_3`, and
only `(a,b,c)=(0,0,0)` is trivial; existence of `ζ_3` is the coefficient-field
root fact named in `theory/wh-kappa.md` §0.  Moreover `soc(R)=(x,y)`:
square-zero gives
one inclusion, while a unit cannot annihilate `x≠0`.  Thus the census has no
generating character, agreeing with `dim_{F_3}soc(R)=2` and recording the
promised proper-quotient collapse at this seed only.  **QED** (`C-PROBE`)

## 2. FCR-RAD — the radical of the phase pairing

**ASSUME** `D12`--`D14` and an arbitrary nontrivial `ψ∈X(R)`.  **PROVE** `ω`
is R-bilinear, strongly alternating, and R-nondegenerate, and
`rad(ψ∘ω)=I_ψ⊕I_ψ`; consequently `ψ∘ω` is nondegenerate iff `ψ∈Gen(R)`.

`<1>1.` The formula in `D14` is R-bilinear by distributivity and commutativity,
and `ω((a,b),(a,b))=ab−ab=0`, so it is alternating in the strong sense in
every residue characteristic.  If `ω((a,b),w)=0` in `R` for every `w`, tests
against `(0,1)` and `(1,0)` give `a=b=0`; thus `ω` is R-nondegenerate.  This
records the convention-group properties but does not confuse them with the
phase nondegeneracy proved below.

`<1>2.` Let `v=(a,b)` be in the phase radical.  Testing against `(0,r)` gives
`ψ(ar)=1` for every `r`, so the ideal `aR` lies in `ker ψ`; hence `a∈I_ψ`
by `D13`.  Testing against `(r,0)` similarly gives `b∈I_ψ` (the sign does not
change a kernel).

`<1>3.` Conversely, if `a,b∈I_ψ`, then
`ab'−a'b∈I_ψ⊆ker ψ` for every `(a',b')`, because `I_ψ` is an ideal (`D13`).
Thus `(a,b)` is radical.

`<1>4.` The radical is zero exactly when `I_ψ=0`, which is the definition of
`Gen(R)` in `D13`.  Computation `C-PROBE` exhibits a nonzero radical for every
nontrivial character at the designated non-Frobenius seed.  **QED** (`FCR-RAD`)

## 3. FCR-COMM — the Weyl commutator, uniformly

**ASSUME** `D12`--`D16`, any residue characteristic, any nontrivial `ψ`, and
`β∈Adm(ω)`.  **PROVE**
`W_β(v)W_β(v')=ψ(ω(v,v'))W_β(v')W_β(v)`.

`<1>1.` R-bilinearity gives the cocycle identity
`β(v,v')+β(v+v',v'')=β(v',v'')+β(v,v'+v'')`; hence the product of `D16` is
associative.  Also `W(0)=1` and
`W(v)^{-1}=ψ(β(v,v))W(−v)`, by the same displayed product.

`<1>2.` The two orders have the same basis term `W(v+v')`; their scalar ratio
is
`ψ(β(v,v')−β(v',v))=ψ(ω(v,v'))` by `D15`.  This is the ring-level re-derivation
of the port `WH-COMM §2 <1>3`; it uses no field property and no half.

`<1>3.` Multiplying `<1>2` by `W(v)^{-1}` also gives
`W(u)W(v)W(u)^{-1}=ψ(ω(u,v))W(v)`.

`<1>4.` The group `H_β(R)` of `D16` is associative by `<1>1`.  Its centre is
`R×0`: centrality of `(t,v)` means `ω(v,w)=0` in `R` for all `w`; testing
`w=(0,1),(1,0)` gives `v=0` by the formula in `D14`.  **QED** (`FCR-COMM`)

## 4. FCR-BETA-ODD — the polarizing cocycle at odd residue characteristic

**ASSUME** `D12`,`D14`--`D16` and `2∈R^×`.  **PROVE** `Adm(ω)` is a torsor
under `Sym_R(V(R))`, of size `|R|^3`; `ω/2` is its unique
antisymmetric member; and for symmetric `s`,
`φ_s(t,v)=(t+s(v,v)/2,v)` is an isomorphism
`H_β(R)→H_{β+s}(R)` fixing the centre pointwise.

`<1>1.` If `β,β'` are admissible, `s=β'−β` satisfies `s=s^T`; conversely
adding a symmetric form preserves `β−β^T=ω`.  The action is free and
transitive; it is nonempty because the R-bilinear form `β₀` satisfies
`β₀(v,w)−β₀(w,v)=ω(v,w)` by the two formulas in `D14`,`D15`.  A symmetric form
on free rank-two `V(R)` is determined freely by
its three matrix entries, so there are `|R|^3`.  This is the verbatim-port
argument of `WH-BETA-a`, re-derived over `R`.

`<1>2.` Since `ω^T=−ω` by the formula in `D14`, `ω/2` is admissible and
antisymmetric.  If `β` is antisymmetric and admissible, then
`ω=β−β^T=2β`, so `β=ω/2`; uniqueness uses exactly `2∈R^×`.

`<1>3.` Put `f(v)=s(v,v)/2`.  Bilinearity and symmetry give
`f(v+w)=f(v)+f(w)+s(v,w)`.  Applying this identity to the two group laws of
`D16` proves
`φ_s((t,v)(t',w))=φ_s(t,v)φ_s(t',w)`; the inverse subtracts `f`, and
`f(0)=0`, so the centre is fixed.  This is the ring re-derivation of the
odd-field port `WH-BETA-b §6 <1>2`.  **QED** (`FCR-BETA-ODD`)

## 5. FCR-ALG — the central simple observable algebra

**ASSUME** `D12`--`D16`, `ψ∈Gen(R)`, `β∈Adm(ω)`, and `2∈R^×` for the displayed
matrix realization.  **PROVE** `A_{ψ,β}(V(R))` is simple, has centre `C·1`,
has complex dimension `|R|^2`, and is isomorphic to `M_{|R|}(C)`; the matrix
isomorphism is not part of the algebra datum.

`<1>1.` For `x=Σ_v a_vW(v)`, define
`E(x)=|V|^{-1}Σ_{u∈V}W(u)xW(u)^{-1}`.  By `FCR-COMM <1>3`,
`E(x)=Σ_v a_v(|V|^{-1}Σ_uψ(ω(u,v)))W(v)`.

`<1>2.` If `v≠0`, then `u↦ψ(ω(u,v))` is nontrivial because the radical is
zero by `FCR-RAD` and `ψ∈Gen(R)`.  Thus `L-ORTH` makes the inner sum zero;
for `v=0` it is `|V|`.  Hence `E(x)=a_0·1`.

`<1>3.` A central element is fixed by every conjugation, so `<1>2` makes it a
scalar.  If a nonzero two-sided ideal contains `x`, choose a nonzero coefficient
`a_{v_0}`; then `W(v_0)^{-1}x` has nonzero `W(0)` coefficient by
`FCR-COMM <1>1`, and averaging it by `<1>2` puts a nonzero scalar in the ideal.
Thus the centre is `C·1` and the algebra is simple.  This ports `WH-ALG §3`,
with `FCR-RAD` replacing the field-only surjectivity step.

`<1>4.` The basis in `D16` has `|V|=|R|^2` elements, proving the dimension.

`<1>5.` For `β=β₀`, the fixed operators on `ℓ²(R)` satisfy the product of
`D16`:
`Z(−b)X(a)Z(−b')X(a')=ψ(ab')Z(−b−b')X(a+a')`.
This follows on `e_y` from
`X(a)Z(−b')=ψ(ab')Z(−b')X(a)`; it is the named sign computation
`C-MODEL`, and fixes the E1 convention rather than choosing another one.

`<1>6.` The resulting unital map
`A_{ψ,β₀}→End_C(ℓ²(R))` is nonzero, hence injective by `<1>3`; both sides have
dimension `|R|^2` by `<1>4` and `dim ℓ²(R)=|R|` (`D16`), so it is onto.

`<1>7.` For general `β`, take `s=β₀−β`.  The isomorphism in
`FCR-BETA-ODD <1>3` induces
`W_β(v)↦ψ(s(v,v)/2)W_{β₀}(v)`, an algebra isomorphism (substitute the identity
for `f(v+w)` from that step).  Compose with `<1>6`.  Writing the endomorphism
algebra as matrices requires an ordering/basis of `ℓ²(R)`; neither is added by
`D16`, so the displayed `M_{|R|}(C)` isomorphism is non-canonical.  **QED**
(`FCR-ALG`)

## 6. FCR-SVN — finite Stone--von Neumann over `R`

**ASSUME** the hypotheses of `FCR-ALG`.  **PROVE** `H_β(R)` has one irreducible
unitary representation with central character `ψ`, up to unitary equivalence;
its dimension is `|R|`; intertwiners are unique up to `U(1)`; every complex
algebra automorphism of `A_{ψ,β}` is inner.

`<1>1.` A representation of `H_β(R)` on which `(t,0)` acts by `ψ(t)` is
equivalent to a unital `A_{ψ,β}`-module: the group law of `D16` becomes exactly
its Weyl product.  Irreducibility is simplicity of the module.

`<1>2.` Put `n=|R|` and identify `A≅End_C(M)`, `M=ℓ²(R)`, by
`FCR-ALG <1>6`--`<1>7`.  The module `M` is simple because the full endomorphism
algebra sends any nonzero vector to any prescribed vector.  The columns give
`A≅M^{⊕n}` as left modules.  Any
simple module `N` is a quotient of `A` (send `a` to `an` for `0≠n∈N`); a
nonzero restriction from one column is an isomorphism of simple modules.
Thus every simple module is `M` and has dimension `n`.

`<1>3.` An `A`-endomorphism of `M` has an eigenvalue over `C`, by the ambient
coefficient-field fact named in `theory/wh-kappa.md` §0; the corresponding
nonzero eigenspace kernel is an `A`-submodule, so simplicity makes the
endomorphism scalar.  Therefore intertwiners between two simple models form a
one-dimensional complex space.

`<1>4.` The model of `FCR-ALG <1>5`, transported by
`FCR-BETA-ODD <1>3`, is unitary because shifts permute the orthonormal basis
and every value of `ψ` has modulus one (a character of a finite group has
finite image).  If `T` intertwines two unitary irreducibles, `T^*T` is scalar
by `<1>3`; rescaling makes `T` unitary, and two unitary choices differ by
`U(1)`.

`<1>5.` For an algebra automorphism `α`, let `M_α` have action
`a·m:=α(a)m`.  It is simple, so `<1>2` supplies an A-isomorphism
`T:M→M_α`.  Its equation `T(am)=α(a)T(m)` gives
`α(a)=TaT^{-1}`.  Uniqueness up to scalar is `<1>3`.  This re-proves the
finite-ring case instead of importing either the field case or a general
Stone--von Neumann theorem.  **QED** (`FCR-SVN`)

## 7. FCR-POL — all self-perpendicular submodules, including non-free ones

**ASSUME** `D12`--`D16`, `ψ∈Gen(R)`, and `2∈R^×`.  A Lagrangian means exactly
an `R`-submodule `L=L^{⊥_ψ}` (`D14`).  **PROVE** every Lagrangian has
`|L|=|R|`; the two coordinate axes are Lagrangian; every ideal gives a
Lagrangian `I⊕Ann(I)`; and if `R` is not a field, `soc(R)⊕𝔪` is non-free.
Every such label yields a Schrödinger model, and all models are isomorphic.

`<1>1.` For any additive subgroup `L≤V`, evaluate
`S=Σ_{v∈V,l∈L}ψ(ω(v,l))` in two orders.  By `FCR-RAD`, the sum over `v` is
`|V|` for `l=0` and zero otherwise (`L-ORTH`), so `S=|V|`.  The sum over `l`
is `|L|` exactly for `v∈L^{⊥_ψ}` and zero otherwise, again by `L-ORTH`.
Thus `|L||L^{⊥_ψ}|=|V|=|R|^2`; if `L=L^{⊥_ψ}`, then `|L|=|R|`.

`<1>2.` For `L=R⊕0`, perpendicularity says `ψ(rb)=1` for every `r`; by
`I_ψ=0` this forces `b=0`, and `a` is unrestricted.  Thus `L=L^{⊥_ψ}`.
The calculation for `0⊕R` is symmetric.

`<1>3.` For an ideal `I`, perpendicularity to `I⊕Ann(I)` says
`bI=0` and `aAnn(I)=0`: if either product ideal were nonzero, it could not lie
in `ker ψ` by `D13`.  Hence
`(I⊕Ann(I))^{⊥_ψ}=Ann(Ann(I))⊕Ann(I)=I⊕Ann(I)` by `L-ANN`.

`<1>4.` Suppose `R` is not a field.  By `FCR-GEN`, `soc(R)` is a nonzero
one-dimensional `κ`-space.  We have `Ann(𝔪)=soc(R)` by `D12`, and
`Ann(soc(R))=𝔪`: inclusion `𝔪⊆Ann(soc(R))` is the definition, while a unit
cannot kill a nonzero socle element.  Thus `L_*=soc(R)⊕𝔪` is the case
`I=soc(R)` of `<1>3`.

`<1>5.` The module `L_*` is not free.  Indeed
`𝔪L_*=0⊕𝔪^2`, so
`L_*/𝔪L_*≅soc(R)⊕𝔪/𝔪^2` over `κ`.  The first summand has dimension one, and
the second is nonzero: `𝔪=𝔪^2` would iterate to `𝔪=𝔪^n=0` by
`L-LOCAL <1>1`, contradicting the non-field hypothesis.  Thus the quotient
needs at least two generators.  A free module of cardinality
`|L_*|=|R|` (`<1>1`) would have rank one and quotient dimension one.

`<1>6.` If `L` is Lagrangian, then `ω(L,L)=0` in `R`: for `l,l'∈L` and every
`r∈R`, also `rl∈L`, so `ψ(rω(l,l'))=1`; the ideal generated by
`ω(l,l')` lies in `ker ψ`, and `D13` forces it to vanish.  Hence `β|_{L×L}` is
symmetric (`D15`).

`<1>7.` The formula
`χ_0(W(l))=ψ(−β(l,l)/2)` defines a character of the commutative algebra `A_L`:
bilinearity, symmetry, and `<1>6` give
`β(l+l',l+l')/2=β(l,l)/2+β(l',l')/2+β(l,l')`, exactly the character identity
for the product in `D16`.  All characters are `χ_0` times an additive
character of `L`; taking a ratio proves one direction, and multiplication by
an additive character proves the converse, so the action is free and
transitive.  No character-count theorem is needed for the model result.

`<1>8.` Choose coset representatives for `V/L`.  The Weyl basis makes `A`
free as a right `A_L`-module on those representatives, so every induced model
`A⊗_{A_L}C_χ` has dimension `|V|/|L|=|R|`.  It contains a simple submodule;
`FCR-SVN <1>2` says that submodule already has dimension `|R|`, so the induced
model is simple and all such models are isomorphic.

`<1>9.` At `R=Z/9`, `soc(R)=𝔪=(3)` and the witness is
`(3)⊕(3)⊂(Z/9)^2`, of order `9` and killed by `3`; at
`F_3[ε]/(ε^2)`, it is `(ε)⊕(ε)`, killed by `ε`.  These direct seed checks are
instances of `<1>4`--`<1>5`, not the ground for the general result.  Therefore
the model catalogue is strictly larger than its free-Lagrangian subcatalogue
for every non-field ring in scope.  **QED** (`FCR-POL`)

## 8. FCR-CHOICE — exactly what is chosen

**ASSUME** `D12`--`D16`, `2∈R^×`, and `Gen(R)≠∅`.  **PROVE** beyond `R` the
presentation uses exactly `ψ∈Gen(R)` and `β∈Adm(ω)`; different `ψ` give
inequivalent representations of the same `H_β(R)`; all resulting algebras are
isomorphic, while the bare-algebra isomorphism torsor has no
automorphism-invariant point.

`<1>1.` Inspection of `D12`--`D16` lists only the two inputs `ψ,β` beyond `R`;
`V,ω,β₀,H,A` and the fixed `ℓ²(R)` formula are then stipulated.  A Lagrangian
and its character label a realization (`FCR-POL`) but do not change the unique
module-equivalence class (`FCR-SVN`).

`<1>2.` The group `H_β(R)` does not use `ψ` (`D16`).  In a representation with
central character `ψ`, `(t,0)` acts as `ψ(t)id`; an intertwiner with a model of
central character `ψ'` would force `ψ(t)=ψ'(t)` for every `t`.  Thus distinct
characters give inequivalent representations of the same group.

`<1>3.` Every algebra is `M_{|R|}(C)` by `FCR-ALG`, so any two are isomorphic.
Once one isomorphism is chosen, all are obtained uniquely by composing with an
automorphism of the target; hence the isomorphism set is an automorphism torsor.
It is nontrivial: for `0≠u∈V`, `Ad W(u)` is nonidentity because zero radical
(`FCR-RAD`) supplies `v` with `ψ(ω(u,v))≠1`, and `FCR-COMM <1>3` computes its
action on `W(v)`.  A point intrinsic to the two bare algebras would have to be
fixed by postcomposition with every target automorphism, but the nontrivial
torsor action is free, so no such point exists.  This is the precise meaning of
“no distinguished isomorphism”; it does not forbid formulas using extra
coordinates or a subsequently imposed naturality condition.

`<1>4.` The `β` input is presentation-level at odd residue characteristic:
`FCR-BETA-ODD` supplies the unique antisymmetric representative and explicit
centre-fixing transports.  This does not erase `β` from the input list in
`D15`; it proves exactly how its effect becomes immaterial.  **QED**
(`FCR-CHOICE`)

## 9. FCR-REG — clause-level odd-field compatibility

**ASSUME** `R=κ` is a finite field of odd characteristic.  **PROVE** exactly
the following definition clauses and trunk claim clauses are recovered on
the nose; the exclusions listed after the tables are not part of the
comparison.

| ring calculation | trunk definition clause recovered on the nose |
|---|---|
| `D12` with `𝔪=0` | The base is the field `κ`, `q=\|κ\|`, `R^×=κ^×`, and `soc(R)=R`; this adds no choice. |
| `D13` and `FCR-GEN <1>5` | The nontrivial-character set is exactly `X(κ)` and its scalar action is the free transitive `κ^×`-action of `D3`. |
| `D14` | `D1`'s object `V(κ)=κ⊕κ` and formula `ω((a,b),(a',b'))=ab'−a'b`. |
| `D15` | `D2`'s set `Adm(ω)`, its translation space of symmetric bilinear forms, and the reference member `β₀=ab'`. |
| `D16` | `D4`'s Weyl product, `D5`'s Heisenberg group law, and `D8`'s fixed model `W_{β₀}=Z(−b)X(a)`, with the same sign. |

| ring theorem | trunk claim clauses recovered on the nose |
|---|---|
| `FCR-GEN` | `WH-CHOICE`'s character clause: all nontrivial characters are generating and `X(κ)` is a `κ^×`-torsor of order `q−1`. |
| `FCR-RAD` | The bilinearity, strong alternation, and nondegeneracy clauses for `ω` in `WH-FORM`; also `I_ψ=0` gives the zero phase radical used in `WH-ALG`. |
| `FCR-COMM` | Both `WH-COMM` identities: the Weyl commutator and its conjugation form, for every `β∈Adm(ω)`. |
| `FCR-ALG` | `WH-ALG`'s simplicity, scalar centre, and dimension `q²`, and the `WH-ALG-MAT` conclusion `A_{ψ,β}≅M_q(C)` with no canonical bare matrix identification. |
| `FCR-SVN` | `WH-SVN`'s unique irreducible unitary representation with central character `ψ`, dimension `q`, `U(1)`-uniqueness of unitary intertwiners, and innerness of algebra automorphisms. |
| `FCR-POL` | `WH-POL`'s catalogue: precisely the `q+1` field lines, `q` algebra characters per line, `q(q+1)` model labels, and all labels isomorphic as modules; the ring theorem's non-free implication has false antecedent. |
| `FCR-BETA-ODD` | `WH-BETA-a`'s `Sym(V)`-torsor of order `q³`, and the clauses of `WH-BETA-b` asserting the unique antisymmetric member `ω/2` and the centre-fixing transports `φ_s`. |
| `FCR-CHOICE` together with the preceding rows | The `WH-CHOICE` clauses naming exactly `ψ` and `β`, distinguishing central characters on the same `H_β(κ)`, and asserting that the resulting algebras are isomorphic. |

`<1>1.` For a field the only ideals are `0,κ`, so a nontrivial character has
`I_ψ=0`; substitution of `𝔪=0` and `R=κ` now gives every definition and
claim clause in the two tables directly from the cited ring theorem.  The
trace-normalized subfamily and its root `ζ` in `D3` remain unchanged field
data; `D13` neither replaces nor compares that additional clause.

`<1>2.` For the `WH-POL` count, `FCR-POL <1>1` makes every nonzero
self-perpendicular field subspace one-dimensional.  Nonzero vectors modulo
`κ^×` give `(q²−1)/(q−1)=q+1` lines.  A line has `q` additive characters by
the `F_p`-basis count, and `FCR-POL <1>7` transfers this count to the
characters of `A_L`.

`<1>3.` The comparison expressly does **not** include `WH-CHOICE`'s
frame-preserving isomorphism torsor of order `q²·\|SL_2(κ)\|`: §8 treats the
different torsor of all bare-algebra isomorphisms, and the ring-side
frame-preserving analysis is future work.  Nor does it include `WH-FORM`'s
2-cocycle clause or either automorphism-group clause.  It also makes no
ring-side symmetry comparison for the `SL_2(κ)`-invariance clause of
`WH-BETA-b`, and does not identify the particular polarization-dependent
matrix construction used by the field proof of `WH-ALG-MAT`.

`<1>4.` Gate `G10` witnesses the `F_3` instance through the exact character
counts, radical and form tables, fixed nine model matrices, rank and
commutant, four lines, odd-half census, and group profile.  The general
odd-field clauses are witnessed by the substitutions and calculations in
`<1>1`--`<1>2`; no excluded clause is inferred from `G10`.  **QED**
(`FCR-REG`)

## 10. Evidence ledger and scope

`<1>1.` **PROVE** every nontrivial external leaf is locally grounded.
`FCR-GEN` uses Wood's definition, Theorem 3.10, and Lemma 4.1 at the exact
locators displayed in §1; nilpotence uses the Stacks lemma displayed in
`L-LOCAL`; all other leaves are derivations in this shard from `D12`--`D16`,
earlier FCR steps, `L-ORTH`, or the named computations `C-PROBE` and `C-MODEL`.
The field shards are ports only where the ring proof is repeated.  **QED**

`<1>2.` No result here addresses the deferred residue-characteristic case,
global decompositions, symmetry actions, or a quantization of the
non-Frobenius probe.  `C-PROBE` records only the radical collapse required by
the brief.  **QED**
