<!-- ROLE: Lamport shard (L6b) for briefs/wh-kappa-target.md incl. Errata E1-E5,
     REPAIRED against theory/verdicts/wh-kappa-r1.md (OBJ-1..OBJ-9). LANE
     wh-repair; WRITE SCOPE this directory. D-numbers are PROPOSED in ./PATCH.md,
     claim ids in ./CLAIMS-ROWS.md, objection-by-objection disposition in
     ./REPAIR-NOTES.md. Every leaf cites a D-number, an earlier step, a refs/
     source read in THIS lane with file:line, or a named computation in this
     directory. [ADMITTED] marks a step with no local ground. -->

# `wh-kappa` — the Weyl–Heisenberg system of `Spec κ`, every choice named

`p` prime, `m ≥ 1`, `κ = F_q`, `q = p^m`. **`p = 2` is in scope everywhere.**
A step using `1/2` is marked `[ODD p]` and the statement it supports carries that
hypothesis in its own text, never in a remark. Sources are cited as
`refs/arxiv-<id>/<file>:<line>`; every such line was opened in this lane.

**What round 1 changed.** The critic (`theory/verdicts/wh-kappa-r1.md`, OBJ-1,
FATAL) showed that the round-1 shard treated the polarizing cocycle `β` as a
convention when it is a **datum**. That is not a blemish to be minimised: it is
the sharpest thing this increment produced, and §6 now states it as a theorem
with an intrinsic invariant. `β` is named as a choice in `D2` and carried in
every statement downstream of it. OBJ-2, OBJ-3 and OBJ-4..9 are dispatched at
§10, §9, and in place; `REPAIR-NOTES.md` is the objection-by-objection record.

## 0. Data, and what is not assumed

`D1` `V(κ) = κ⊕κ`, `ω((a,b),(a',b')) = ab' − a'b`.
`D2` **`Adm(ω)`**, the *admissible polarizing cocycles*: the `κ`-bilinear
`β : V×V → κ` with `β − β^T = ω`. A polarizing cocycle `β ∈ Adm(ω)` is a
**choice**, on the same footing as `ψ`. `β₀((a,b),(a',b')) := ab'` is the
*reference* cocycle (`Adm(ω)` is a torsor, §6 `<1>1`, so a reference is a label,
not a canonical point).
`D3` `ψ : (κ,+) → C^×` **nontrivial**; distinguished family `ψ_ζ = ζ^{Tr(·)}`,
`ζ` a primitive `p`-th root of `1` (a choice).
`D4` `W_β(v)W_β(v') = ψ(β(v,v'))W_β(v+v')`, `A_{ψ,β}(V) = ⨁_v C·W_β(v)`.
`D5` `H_β(κ) := κ × V`, `(t,v)(t',v') = (t+t'+β(v,v'), v+v')` — the Heisenberg
group **of `β`**; it uses no character, and it is *not* choice-free.
`D6` `Q_β(v) := β(v,v)`.
`D7` the Weyl frame `F = {C^×W_β(v)}`; `Aut_F(A)` its stabiliser in `Aut_C(A)`;
`Aut_F^κ(A) ⊆ Aut_F(A)` those whose induced permutation of `V` is `κ`-linear.
The `κ`-linearity is **imposed data**, not a property of the algebra (§9).
`D8` the model `M_{L,χ}`; the standard model `W(a,b) = Z(−b)X(a)` (a
stipulation, §5 `<1>1`, tested by gate C11).
`D9` the groupoid `Mod_{ψ,β}(κ)`.
`D10` `℘(x) := x² + x`; **`[p = 2]`** `Arf(Q_β) := Q_β(e)Q_β(f) ∈ κ/℘(κ)` for a
symplectic basis (well defined: §6 `<1>4`).
`D11` the **level-`μ_p` frame** `F^{(p)}_{ψ,β} := {ζ^j W_β(v) : j ∈ Z/p} ⊂ A^×`
— the finite group of Weyl unitaries. (That `F` is `β`-independent while
`F^{(p)}` is not is Thm 6 `<1>7`, a claim, not part of the stipulation.)

Not assumed below: Maschke, Artin–Wedderburn, Skolem–Noether, Jacobson density,
Burnside, Pontryagin duality, the classification of quadratic forms, the Arf
invariant as a black box, or any property of the Weil representation. All of it
is derived from `D1`–`D11` and elementary linear algebra; sources corroborate,
and twice (§8 `<1>7`–`<1>8`) fix what is deliberately **not** claimed.

**Ambient facts about `C` used, named once (OBJ-8).** `C` is an algebraically
closed field of characteristic `0`: `n`-th roots exist (`L-TRIV` `<1>3`) and
every endomorphism of a finite-dimensional `C`-space has an eigenvalue (§5
`<1>3.<2>4`). These are properties of the coefficient field fixed by `D4`, not
theorems quoted from a source; no other property of `C` is used.

### Elementary lemmas, used throughout

**L-ORTH.** *`G` finite abelian, `χ : G → C^×` nontrivial; then `Σ_{u∈G}χ(u) = 0`.*
`<1>1.` Pick `u₀` with `χ(u₀) ≠ 1`. `<1>2.` `S := Σ_uχ(u) = Σ_uχ(u+u₀) = χ(u₀)S`,
as `u ↦ u+u₀` permutes `G`; and `1−χ(u₀) ≠ 0`. **QED**

**L-VAL.** *`ψ(κ) ⊆ μ_p`; `ker ψ` is an `F_p`-subspace of index `p`; and for
`u ∈ κ`, `ψ(u·) ≡ 1` iff `u = 0`.* `<1>1.` `ψ(t)^p = ψ(pt) = 1` as `char κ = p`.
`<1>2.` `ker ψ` is an additive subgroup of a `char p` field, hence an
`F_p`-subspace; `κ/ker ψ` embeds nontrivially in `μ_p` (`D3`), so the index is
`p`. `<1>3.` If `u ≠ 0` then `uκ = κ ⊄ ker ψ`. **QED**

**L-DUAL.** *(restated for what is used, OBJ-8)* *Let `U` be a finite
`F_p`-vector space of dimension `d`. Then `Û := Hom(U,C^×)` has order `p^d`, and
every element of `Û` takes values in `μ_p`.* `<1>1.` `χ(u)^p = χ(pu) = 1`, so
`χ(U) ⊆ μ_p ≅ Z/p`, an `F_p`-space; hence `Û = Hom_{F_p}(U,μ_p)`. `<1>2.` `U` is
free on a basis `u_1,…,u_d`, so a homomorphism is a free choice of `d` values:
`|Û| = p^d`. **QED** *(applied to `U = κ` (`d = m`, giving `|κ̂| = q`) and to
`U = V` (`d = 2m`, giving `|V̂| = q²`); the trivial character is included, and
no step below needs it excluded.)*

**L-TRIV.** *`U` a finite abelian group of exponent `p`, `c : U×U → C^×` a
symmetric 2-cocycle. Then `∃ μ : U → C^×` with `c(u,u') = μ(u+u')/(μ(u)μ(u'))`.*
`<1>1.` `E := C^× × U`, `(z,u)(z',u') := (zz'c(u,u'), u+u')`, is a group
(associativity = the cocycle identity) and is **abelian** (`c` symmetric).
`<1>2.` `(1,u)^p = (γ(u), pu) = (γ(u), 0)`, `γ(u) := c(u,u)c(2u,u)⋯c((p−1)u,u)`
(induction in the abelian group `E`). `<1>3.` Fix an `F_p`-basis `u_1,…,u_n` of
`U`; choose `z_i` with `z_i^p = γ(u_i)^{-1}` (`C` algebraically closed, named
above); put `f_i := (z_i,u_i)`, so `f_i^p = 1`. `<1>4.` `H := ⟨f_1,…,f_n⟩` is
abelian of exponent dividing `p`, i.e. an `F_p`-space; `U` is free on `{u_i}`,
so there is a unique `F_p`-linear `σ : U → H` with `σ(u_i) = f_i`, and
`pr_U ∘ σ = id`. `<1>5.` Writing `σ(u) = (μ(u),u)`, "σ is a homomorphism" reads
`μ(u)μ(u')c(u,u') = μ(u+u')`. **QED**

## 1. Theorem WH-FORM — the form, at every characteristic

**ASSUME** `D1`,`D2`, `κ` any finite field, `p = 2` included. **PROVE** (a) `ω`
is `κ`-bilinear; (b) `ω(v,v) = 0` (**alternating**, not merely antisymmetric);
(c) `ω` nondegenerate; (d) every `β ∈ Adm(ω)` is a 2-cocycle and `β − β^T = ω`;
(e) the group of **`κ`-linear** automorphisms of `V` preserving `ω` is
`SL_2(κ)`; (f) the group of **`F_p`-linear** automorphisms of `V` preserving the
`κ`-valued `ω` is *also* `SL_2(κ)` — nothing larger.

`<1>1.` (a) Each argument occurs once and `κ` is commutative:
`ω(cv,v') = (ca)b' − a'(cb) = c·ω(v,v')`, likewise on the right; additivity is
distributivity. **QED**

`<1>2.` (b) `ω((a,b),(a,b)) = ab − ab = 0`. `<2>1.` An identity in the
commutative ring `κ` with no division and no cancellation of distinct terms: it
holds verbatim at `p = 2`. `<2>2.` *Not a footnote.* Antisymmetry gives only
`2ω(v,v) = 0`, empty at `p = 2`; (b) is strictly stronger there and must be
computed, as here. **QED**

`<1>3.` (c) `ω(v,·) ≡ 0` gives `ω(v,(0,1)) = a = 0`, `ω(v,(1,0)) = −b = 0`.
**QED**

`<1>4.` (d) `β − β^T = ω` is `D2`. `β` is bi-additive, and every bi-additive map
is a 2-cocycle: both `β(v,v')+β(v+v',v'')` and `β(v',v'')+β(v,v'+v'')` expand to
`β(v,v')+β(v,v'')+β(v',v'')`. **QED**

`<1>5.` (e) `<2>1.` `ω(v,v') = det[v|v']`, columns `v,v'` (`D1`, expansion).
`<2>2.` `[gv|gv'] = g[v|v']`, so `ω(gv,gv') = det(g)ω(v,v')` by multiplicativity
of `det` for `2×2` matrices over a commutative ring (expand both sides).
`<2>3.` So `ω∘g = ω` iff `(det g − 1)ω ≡ 0`; `ω((1,0),(0,1)) = 1`, so iff
`det g = 1`. **QED**

`<1>6.` (f) **[OPEN-2, closed.]** Let `g : V → V` be additive with
`ω(gv,gu) = ω(v,u)` for all `v,u`. `<2>1.` `g` is injective: `gv = 0` forces
`ω(v,u) = ω(gv,gu) = 0` for all `u`, so `v = 0` by `<1>3`; hence bijective, `V`
being finite. `<2>2.` `ω(gv₁,gv₂) = ω(v₁,v₂) = 1` for the standard basis, so
`gv₁,gv₂` are `κ`-independent (a dependence would force `ω(gv₁,gv₂) = 0` by
`<1>1`,`<1>2`), hence a `κ`-basis. `<2>3.` For `c ∈ κ`, `u ∈ V` put
`w := g(cu) − c·g(u)`. Then `ω(gv_i,w) = ω(gv_i,g(cu)) − c·ω(gv_i,gu)
= ω(v_i,cu) − c·ω(v_i,u) = 0` by `κ`-bilinearity (a) and the hypothesis; `w = 0`
by `<2>2` and nondegeneracy. So `g` is `κ`-linear, and `det g = 1` by `<1>5`.
**QED**
  `<2>4.` *Credit and check.* This answer was supplied by the round-1 verdict
  (`theory/verdicts/wh-kappa-r1.md`, OBJ-3 `(b)1`), including its warning that
  the tempting route via "`ω`-self-adjoint endomorphisms are the `κ`-scalars" is
  **false at `p = 2`**. Both are recomputed here, independently:
  `theory/checks/wh_kappa/fp_symmetry.py` gate `S1` enumerates the `F_p`-linear isometries of the
  `κ`-valued `ω` by complete backtracking and finds exactly `|SL_2(κ)| =
  6,24,60,120,504,720` at `q = 2,3,4,5,8,9`, every one of them `κ`-linear and
  set-equal to an independent `SL_2` enumeration; gate `S4` finds `8` and `64`
  `ω`-self-adjoint `F_p`-endomorphisms at `q = 2,4` against `2` and `4`
  `κ`-scalars, so the self-adjointness route is indeed unavailable. Red modes
  `--red-kappa-linear`, `--red-sp-formula` both exit non-zero
  (`runs/fp_symmetry-*.txt`).

`<1>7.` **The `F_p`-question that does bite is `ψ∘ω`, not `ω`** — see §9.
**QED** *(Theorem WH-FORM)*

**N-CHAR2 (why `Adm(ω)` has no symmetrised point, with a source).**
`refs/arxiv-2204.08162/main.tex:478` states that the canonical *normalisation*
of the Weyl-system cocycle exists when the group is **2-regular** — `a ↦ 2a` an
automorphism — and is then the unique bicharacter `ξ` with `ξ² = ⟨·,·⟩`. For
`V(κ)` at `p = 2`, `a ↦ 2a` is the zero map: the hypothesis fails and `ω/2` has
no referent. `D2` matches `σ_can((x,γ),(x',γ')) = γ(x')` of
`refs/arxiv-2204.08162/main.tex:463` under `κ̂ ≅ κ`. That the polarizing cocycle
is a choice and not a convention is also the registered literature's own
wording: `refs/arxiv-0808.1664/WeilCharTwo12-8-08.tex:107-110` writes
`Q(v) = β(v,v)` "**for some** non-symmetric bilinear form `β`" with
`β(v,u) − β(u,v) = ω(v,u)` — *for some*, not *the* (ledger note **N2**).

## 2. Theorem WH-COMM — Weyl relations, uniformly in `p`, for every `β`

**ASSUME** `D1`–`D4`, `β ∈ Adm(ω)` arbitrary. **PROVE** (a) `A_{ψ,β}(V)` is a
unital `C`-algebra of dimension `q²`, unit `W(0)`; (b)
`W(v)^{-1} = ψ(β(v,v))W(−v)`; (c) `W(v)W(v') = ψ(ω(v,v'))W(v')W(v)`; (d)
`W(u)W(v)W(u)^{-1} = ψ(ω(u,v))W(v)`. **No step uses which `β ∈ Adm(ω)` was
chosen; only `β − β^T = ω` and bi-additivity enter.**

`<1>1.` (a) Associativity on basis elements is exactly the 2-cocycle identity for
`ψ∘β`, which holds by Thm 1 `<1>4` and multiplicativity of `ψ`. `β(0,v) =
β(v,0) = 0`, so `W(0)` is a two-sided unit. `dim = |V| = q²`. **QED**

`<1>2.` (b) `W(v)W(−v) = ψ(β(v,−v))W(0) = ψ(−β(v,v))·1` (bi-additivity); same on
the other side. **QED**

`<1>3.` (c) `W(v)W(v') = ψ(β(v,v'))W(v+v')` and `W(v')W(v) = ψ(β(v',v))W(v+v')`;
`W(v+v')` is invertible by `<1>2`, so the ratio is
`ψ(β(v,v') − β(v',v)) = ψ(ω(v,v'))` (`D2`). **QED**

`<1>4.` (d) Multiply (c) on the right by `W(v)^{-1}`.
`<1>5.` No step used `p ≠ 2`, `ω(v,v) = 0`, or a choice inside `Adm(ω)`;
alternation first bites in Thm 4, and the choice of `β` first bites in Thm 6.
**QED** *(Theorem WH-COMM)*

`<1>6.` **`D5` and its centre.** `H_β(κ)` is a group: associativity is the
cocycle identity, unit `(0,0)`, inverse `(−t+β(v,v), −v)`. Its centre is `κ×0`:
`(t,v)` is central iff `β(v,v')−β(v',v) = 0` for all `v'`, iff `ω(v,·) ≡ 0`, iff
`v = 0` (Thm 1 `<1>3`). `A_{ψ,β}(V) = C[H_β(κ)]/((t,0)−ψ(t))`, so `ψ ↦ A_{ψ,β}`
is a family over `X(κ)` **at fixed `β`**; the group depends on `β` and, at
`p = 2`, on more than its isomorphism class (§6). **QED**

## 3. Theorem WH-ALG — central simple of dimension `q²`, no polarization

**ASSUME** `D1`–`D4`, `β ∈ Adm(ω)` arbitrary. **PROVE** `A_{ψ,β}(V)` is simple,
`Z(A) = C·1`, `dim_C A = q²`. **No line, no Lagrangian, no module, and no choice
inside `Adm(ω)` is used below.**

`<1>1.` The *Weyl average* `E(x) := q^{-2}Σ_{u∈V} W(u)xW(u)^{-1}` satisfies
`E(Σ_v a_vW(v)) = a_0·1`. `<2>1.` By Thm 2 (d),
`E(x) = Σ_v a_v(q^{-2}Σ_u ψ(ω(u,v)))W(v)`. `<2>2.` For `v ≠ 0`, `ω(·,v)` is a
nonzero `κ`-linear map `V → κ` (Thm 1 `<1>1`,`<1>3`), hence **onto** — which is
what is needed, `ker ψ` having index `p`, not `q` — so `u ↦ ψ(ω(u,v))` is a
nontrivial character by `L-VAL`. `<2>3.` By `L-ORTH` the inner sum is `q²` for
`v = 0`, else `0`; `W(0) = 1`. **QED**

`<1>2.` `Z(A) = C·1`: a central `z` has `W(u)zW(u)^{-1} = z`, so
`z = E(z) = a_0·1`; scalars are central. **QED**

`<1>3.` `A` is simple. `<2>1.` Let `0 ≠ x = Σ_v a_vW(v)` lie in a two-sided ideal
`I`; pick `a_{v₀} ≠ 0`. `<2>2.` `y := W(v₀)^{-1}x ∈ I`, and each
`W(v₀)^{-1}W(v)` is a nonzero scalar times `W(v−v₀)` (Thm 2 `<1>1`,`<1>2`), so
the `W(0)`-coefficient of `y` is a nonzero multiple of `a_{v₀}`. `<2>3.`
`E(y) ∈ I`, being a `C`-combination of `x ↦ W(u)xW(u)^{-1}` and `I` two-sided.
`<2>4.` `E(y) = c·1`, `c ≠ 0`, so `I = A`. **QED**

`<1>4.` `dim_C A = q²` (Thm 2 `<1>1`). **QED** *(Theorem WH-ALG)*

`<1>5.` **What was not borrowed.** The general theory phrases `<1>2`–`<1>3` as
"`ψ∘β` is a nondegenerate cocycle, so `V` is of central type"
(`refs/arxiv-1412.2490/groupsp4andsemi.tex:102-125`, `:359-361`), routing
semisimplicity through Karpilovsky and the abelian case through `[BSZ]`, neither
fetched — per ledger note **N3** both would be `[ADMITTED]`. Unused here:
`<1>1`–`<1>4` is complete and elementary. The operational form is
`refs/arxiv-2501.00650/TotslipVersion5_Aug_25.tex:1645-1651` (the `q²` Weyl
operators are a `C`-basis of `End(M)`, proved in-source), corroborating Thm 5
`<1>2`, where `A ≅ M_q(C)` is proved at the cost of a polarization.

## 4. Theorem WH-POL — Lagrangian lines, and the models they carry

**ASSUME** `D1`–`D4`,`D6`,`D8`. **PROVE** (a) every `κ`-line is `ω`-isotropic,
hence maximal isotropic, at every characteristic — so *Lagrangian line* and
*line* are the same condition here; (b) there are `q+1 = |P¹(κ)|` of them;
(c) `A_L := span{W(l) : l ∈ L}` is commutative of dimension `q` and carries
exactly `q` characters, an `L̂`-torsor; (d) `dim M_{L,χ} = q`; (e) **[p = 2]** if
`Q_β|_L ≠ 0` every character of `A_L` takes a value of exact order 4.

`<1>1.` (a) `L = κv₀` and `ω(cv₀,c'v₀) = cc'ω(v₀,v₀) = 0` by `κ`-bilinearity
(Thm 1 `<1>1`) and the *computed* alternating property (Thm 1 `<1>2`) — at
`p = 2` antisymmetry would not suffice. As `dim_κ V = 2` and `ω` is
nondegenerate, a line is maximal isotropic. Per erratum E2 the isotropy
condition selects nothing among lines; the content is that lines **are** the
Lagrangians. **QED**

`<1>2.` (b) Nonzero vectors modulo `κ^×`: `(q²−1)/(q−1) = q+1 = |P¹(κ)|`. **QED**

`<1>3.` (c) `W(cv₀)W(c'v₀) = ψ(cc'Q_β(v₀))W((c+c')v₀)` by `D4`,`D6` and
`β(cv₀,c'v₀) = cc'β(v₀,v₀)`; the phase is symmetric in `(c,c')`, so `A_L` is
commutative of dimension `|L| = q`. `<2>1.` *Characters exist.*
`c(c,c') := ψ(cc'Q_β(v₀))` is a symmetric bi-additive (hence 2-)cocycle on
`(L,+)`, of exponent `p`; `L-TRIV` gives `μ`, and `χ(W(cv₀)) := μ(c)^{-1}` is an
algebra character. `<2>2.` *`L̂`-torsor.* For characters `χ,χ'` the ratio
`l ↦ χ'(W(l))/χ(W(l))` is a homomorphism `L → C^×`, and conversely; the action is
free, and `|L̂| = q` by `L-DUAL` (`U = L`, `d = m`). **QED**

`<1>4.` (d) `A` is free as a right `A_L`-module on coset representatives
`v_1,…,v_q` of `L` in `V` (`{W(v_i)W(l)}` is, up to nonzero scalars, the basis
`{W(v_i+l)}`), so `M_{L,χ} := A ⊗_{A_L} C_χ` has dimension `q²/q = q`. **QED**

`<1>5.` (e) **[p = 2]** Let `Q₀ := Q_β(v₀) ≠ 0`, `ν(c) := χ(W(cv₀))`. Then
`ν(0) = 1` and, putting `c' = c` in `<1>3`, `ν(c)² = ψ(c²Q₀)ν(2c) = ψ(c²Q₀)`.
`<2>1.` `c ↦ c²` is Frobenius, injective hence bijective on the finite field
`κ`, so `{c²Q₀ : c ∈ κ} = Q₀κ = κ`. `<2>2.` `ψ` is nontrivial, so
`ψ(c²Q₀) = −1` for some `c`, whence `ν(c)² = −1`: order exactly 4.
`<2>3.` **[ODD p]** nothing of the sort: `μ(c) = ψ(c²Q₀/2)` trivialises inside
`ψ(κ)`, since `ψ((c²+c'²)Q₀/2)ψ(cc'Q₀) = ψ((c+c')²Q₀/2)`. **QED**

`<1>6.` **Precision note, binding on the claim row (OBJ-9).** "Exactly `q+1`
Schrödinger models" counts *polarizations*. A model is a **pair** `(L,χ)`; by
`<1>3` there are `q(q+1)` such pairs, and by Thm 5 `<1>4` **all of them are
isomorphic as `A`-modules** — the count is of labels, not of objects. Only the
lines with `Q_β|_L = 0` carry a distinguished character (`χ ≡ 1` is a character
iff `Q_β(v₀)κ ⊆ ker ψ` iff `Q_β(v₀) = 0`, by `L-VAL`), and **how many such lines
there are is a `β`-dependent number**: `2` for `β₀`, and in general `2` or `0`
according to the type of `Q_β` (§6 `<1>5`). Enumerated at `q = 2,3,4,5,8,9`:
`q+1` lines, `q` characters each, `q(q+1) = 6,12,20,30,72,90` pairs, exactly two
lines with `Q_{β₀}|_L = 0` (`theory/checks/wh_kappa/beta_census.py` `B6` reports `#{Q=0} = 2q−1`, i.e.
two lines, for the type of `β₀`). **QED** *(Theorem WH-POL)*

## 5. Theorem WH-SVN — one irreducible representation, of dimension `q`

**ASSUME** `D1`–`D4`,`D8`, Thms WH-ALG, WH-POL. **PROVE** (a) the model induced
from `L₀ = 0⊕κ` with `χ₀ ≡ 1` has basis `{e_y}_{y∈κ}` and
`W_{β₀}(a,b)e_y = ψ(−b(y+a))e_{y+a}`, i.e. **`W(a,b) = Z(−b)X(a)`** — erratum
E1's option (i), *derived*; (b) `A ≅ End_C(M) ≅ M_q(C)`, by an isomorphism
depending on `(L,χ)`; (c) every simple `A`-module is `≅ M`, and an `A`-map
`M → M` is a scalar; (d) consequences, including that every algebra automorphism
is inner; (e) each `W(v)` is unitary for `{e_y}` orthonormal, and the intertwiner
of (c) can be scaled unitary, uniquely up to `U(1)`; (f) `H_β(κ)` has exactly one
irreducible unitary representation with central character `ψ` up to unitary
equivalence, of dimension `q`. *(Ordered so that no leaf points forward, OBJ-8.)*

`<1>1.` (a) **The step the brief was missing.** `Q_{β₀}(0,b) = 0·b = 0`, so
`χ₀ ≡ 1` is a character of `A_{L₀}` (Thm 4 `<1>6`). Take coset representatives
`(y,0)` and put `e_y := W(y,0)⊗1`.
  `<2>1.` `W(a,b)e_y = ψ(β₀((a,b),(y,0)))W(a+y,b)⊗1 = W(a+y,b)⊗1`, since
  `β₀((a,b),(y,0)) = a·0 = 0`.
  `<2>2.` To apply `χ₀` the `L₀`-factor must be moved to the **right**:
  `W(a+y,0)W(0,b) = ψ((a+y)b)W(a+y,b)`, hence
  `W(a+y,b) = ψ(−b(y+a))·W(a+y,0)W(0,b)`.
  `<2>3.` Therefore `W(a,b)e_y = ψ(−b(y+a))e_{y+a}`, which is `Z(−b)X(a)`.
  `<2>4.` The sign in `<2>2` is the whole content of erratum E1: the naive
  `Z(b)X(a)` realises the cocycle `−ab'`, not `β₀`'s `ab'`. This is now a
  **pre-registered gate, not a lane computation** (OBJ-6): `wh_kappa_check.py`
  gate `C11` (added by this lane) builds `D8`'s model and the naive one and
  reports `0` violations of `D4` for `Z(−b)X(a)` at all six `q`, against
  `36, 400, 3888` for `Z(b)X(a)` at `q = 3,5,9` and `0` at `q = 2,4,8`; red mode
  `--red-naive-order` exits non-zero, firing only at `q = 3,5,9`
  (`runs/check--red-naive-order.txt`).
  `<2>5.` **Methodological note (E1+E3), on the record.** That the red mode
  passes at `q ∈ {2,4,8}` is the point: at `p = 2`, `−1 = 1`, so the ordering
  defect is invisible in even characteristic; symmetrically `β^T − β = −ω = ω`
  at `p = 2`, so a transposed cocycle is invisible to `D2`'s identity there.
  **Each characteristic conceals a different sign defect; a convention is
  validated only when validated in both.** `dim M = q` by Thm 4 `<1>4`. **QED**

`<1>2.` (b) `π : A → End_C(M)` is unital and nonzero, so `ker π` is a proper
two-sided ideal, hence `0` (Thm 3 `<1>3`): `π` is injective; and
`dim End_C(M) = q² = dim A`, so `π` is onto. Choosing the basis `{e_y}` gives
`≅ M_q(C)` — **an isomorphism that depends on `(L,χ)` and a basis, and is named
as such**. **QED**

`<1>3.` (c) `<2>1.` `M` is simple: `π(A) = End_C(M)`, so every nonzero vector
generates. `<2>2.` `A ≅ M^{⊕q}` as a left `A`-module (the columns of
`End_C(M)`). `<2>3.` A simple module `N` is generated by any `0 ≠ n`, hence a
quotient of `A ≅ M^{⊕q}`; restricting to a summand gives a nonzero `M → N`,
surjective (its image is a nonzero submodule) and injective (its kernel is a
proper submodule of the simple `M`). `<2>4.` *Schur.* An `A`-endomorphism `φ` of
`M` has an eigenvalue `λ ∈ C` (ambient fact, §0), and `ker(φ−λ)` is a nonzero
submodule, so `End_A(M) = C·id`. **QED**

`<1>4.` (d) Every `α ∈ Aut_C(A)` is inner: `M_α` (action `a·m := π(α(a))m`) is
simple of dimension `q`, so `M_α ≅ M` by `<1>3.<2>3`, i.e. `α = Ad_T`, with `T`
unique up to a scalar by `<1>3.<2>4`. **No Skolem–Noether.** **QED**

`<1>5.` (e) `<2>1.` *Unitarisability, for every `β`.* By `D11` and `L-VAL` the
Weyl operators generate the **finite** group `F^{(p)} = μ_p·{W_β(v)} ⊂ A^×`, of
order `p·q²`; averaging any inner product on `M` over that group makes every
`π(W_β(v))` unitary. `<2>2.` For `β₀` and the standard model no averaging is
needed: `W(v)` sends the orthonormal `{e_y}` to `{ψ(−b(y+a))e_{y+a}}`, again
orthonormal, as `|ψ| = 1` (`L-VAL`). `<2>3.` If `T` intertwines unitary
representations,
`T*T` commutes with every `π₁(W(v))`, so `T*T = c·id`, `c > 0`, by `<1>3.<2>4`;
`c^{-1/2}T` is unitary and two unitary intertwiners differ by a unimodular
scalar. **QED**

`<1>6.` (f) Representations of `H_β(κ)` with central character `ψ` are exactly
`A_{ψ,β}(V)`-modules (Thm 2 `<1>6`); irreducible ⟺ simple; apply `<1>3`,`<1>5`;
the dimension is `q` by `<1>1`. **QED** *(Theorem WH-SVN)*

`<1>7.` **Corroboration.** Uniform in the characteristic in three registered
sources: Prasad `refs/arxiv-0912.0574/SvN.tex:181-191` (intertwining isometry
unique up to scaling; the finite case is the compact-open branch proved from
`:193`); Bekka `refs/arxiv-2502.00387/CCR-GeneralRings-v5.tex:1143-1151` with
`:997-999`, checking that a finite field satisfies (Isom) for **every**
nontrivial character, no parity exception; Gurevich–Hadani
`refs/arxiv-0808.1664/WeilCharTwo12-8-08.tex:759-763` for `V` over `F_{2^d}`.
Proved here, so nothing is `[ADMITTED]`.


## Companion shard

`L2` caps a shard at 500 lines and this cluster is full. The choice-and-symmetry
cluster — **WH-BETA** (the polarizing cocycle as a datum, and the `p = 2`
dichotomy), **WH-CHOICE/WH-CANON**, **WH-WEIL**, **WH-SYMM** and **WH-FUNCT**,
together with the shared ledger of admitted steps and open questions — is the
companion shard `wh-kappa-choice.md`, which assumes `D1`–`D11` and Theorems 1–5
above and nothing else.

## Ledger of the shard pair

**`[ADMITTED]` steps: none.** No step depends on a theorem quoted from a source.
The two ambient properties of `C` (roots exist; endomorphisms have eigenvalues)
are named in §0 as properties of the coefficient field fixed by
`D4`, not as quoted theorems (OBJ-8). Sources are cited (i) to corroborate
results proved here (Thms 3, 5, WH-FORM, and Thm 7 of the companion), (ii) to fix what is deliberately
**not** claimed at `p = 2` (Thm 8 `<1>7.<2>5`, `<1>9`), (iii) for the
2-regularity failure and the "for some `β`" wording that WH-BETA turns into a
theorem (N-CHAR2). Ledger note **N3** bites nothing: the Karpilovsky/`[BSZ]`
facts are unused.

**Evidence in this lane** (all exact-integer, no tolerance; logs in `runs/`,
green exit 0 and every red mode exit 1, tabulated in `PATCH.md`):
`theory/checks/wh_kappa/beta_census.py` (B1–B10), `theory/checks/wh_kappa/frame_mu.py` (M1–M4), `theory/checks/wh_kappa/fp_symmetry.py` (S1–S4),
`theory/checks/wh_kappa/funct_sections.py` (F1–F5), `theory/checks/wh_kappa/split24.py` (X1–X6), plus the two gates this lane
adds to the pre-registered falsifier, `C10` (β-dichotomy) and `C11` (`D8`'s
model), and the repair of `C7`'s dead `ψ`-isotropy branch (OBJ-5).

**Open questions, each with a forward attack.**
- **OPEN-1** (`p = 2`): does `1 → V̂ → Aut_F^κ(A) → SL_2(κ) → 1` split for every
  `q = 2^m`? **Settled affirmatively at `q = 2, 4` for `β₀`** (Thm 8 `<1>8`).
  Attacks: `H²(SL_2(κ), V̂)`; the anisotropic type at `q = 2`, where the `μ_2`
  part is everything, as a source of a uniform construction.
- **OPEN-2** — **closed**: the `F_p`-linear isometries of the `κ`-valued `ω` are
  exactly `SL_2(κ)` (Thm 1 `<1>6`). The question that bites is the `ψ∘ω` one,
  answered by Thm 9 `<1>2`: `Sp_{2m}(F_p)`.
- **OPEN-3** — **closed**: no section over all finite fields with all embeddings;
  the sections over the inclusion poset are exactly the characters of
  `(\bar F_p,+)` nontrivial on `F_p` (Thm 10 `<1>3`,`<1>4`).
- **OPEN-4**: is the `μ_4` forced in Thm 8 `<1>6` the *same* `μ_4` as
  `refs/arxiv-0808.1664/…:795-800`? Not established: the two live over different
  groups.
- **OPEN-5** (new, from Thm 6): is there a distinguished `β`, or a compatible
  choice of type `Arf(Q_β)` along field embeddings at `p = 2`? The hyperbolic
  type is the one with `Q|_L = 0` lines, hence the only one admitting `D8`'s
  standard model at all (Thm 4 `<1>6`, Thm 5 `<1>1`) — that is the first
  genuinely canonical-looking argument for `β₀`, and it should be either proved
  into a characterisation or discarded.
- **OPEN-6** (new, from Thm 6 `<1>1` and gate `B10`): dropping `κ`-bilinearity
  for bare bi-additivity — all the brief requires — the invariant
  `n₀ = |Q_β^{-1}(0)|` takes `q` values rather than two (`{1,3}`, `{1,3,5,7}`,
  `{1,3,…,15}` at `q = 2,4,8`), so `H_β(κ)` then has **more than two**
  isomorphism classes, while `Σ_vψ(Q_β(v)) = ±q` throughout, so `ψ∘Q_β` keeps
  exactly two classes. Thm 6 is stated for the `κ`-bilinear cocycles; which
  category the campaign should fix is a live question, and the gap between the
  two invariants is where its answer lies.
