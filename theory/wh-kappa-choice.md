<!-- ROLE: Lamport shard (L6b), companion to wh-kappa.md, same brief and same
     repair wave. Splits off at L2's 500-line cap. ASSUMES D1-D11 and Theorems
     WH-FORM, WH-COMM, WH-ALG, WH-POL, WH-SVN of wh-kappa.md; adds nothing to
     the definitions. LANE wh-repair; WRITE SCOPE this directory. -->

# `wh-kappa-choice` — the choices the system depends on, and the symmetries it has

Companion to `wh-kappa.md`; `D1`–`D11`, `L-ORTH`, `L-VAL`, `L-DUAL`, `L-TRIV`
and Theorems 1–5 are cited from there by number. `p` prime, `κ = F_q`,
`q = p^m`, `p = 2` in scope everywhere. Named computations live beside this file
(`theory/checks/wh_kappa/beta_census.py`, `theory/checks/wh_kappa/frame_mu.py`, `theory/checks/wh_kappa/fp_symmetry.py`, `theory/checks/wh_kappa/funct_sections.py`,
`theory/checks/wh_kappa/split24.py`; logs in `runs/`), and the pre-registered falsifier is
`theory/checks/wh_kappa_check.py` with this lane's gates `C10`, `C11`.

## 6. Theorem WH-BETA — the polarizing cocycle is a second datum

*The theorem OBJ-1 forced, and the increment's main positive result. Everything
above holds for every `β ∈ Adm(ω)`; from here the choice is visible.*

**ASSUME** `D1`–`D6`,`D10`,`D11`. **PROVE**
(a) `Adm(ω)` is a torsor under the symmetric `κ`-bilinear forms `Sym(V)`;
`|Adm(ω)| = q³`;
(b) **[ODD p]** `Adm(ω)` contains exactly one antisymmetric member, `ω/2`, it is
`SL_2(κ)`-invariant, and for every `s ∈ Sym(V)` the map
`φ_s(t,v) := (t + s(v,v)/2, v)` is a group isomorphism `H_β(κ) → H_{β+s}(κ)`
fixing the centre pointwise: at odd `p` the choice is immaterial and has a
canonical representative;
(c) **[p = 2]** `Adm(ω)` contains no antisymmetric member, so that criterion
distinguishes nothing;
(d) **[p = 2]** `Q_β` is a `κ`-quadratic form with polar form `ω`;
`(t,v)² = (Q_β(v),0)` in `H_β(κ)`, so the element-order profile of `H_β(κ)` is
`{1:1, 2: q·n₀−1, 4: q³−q·n₀}` with `n₀ := |Q_β^{-1}(0)|`;
(e) **[p = 2]** `Q_β` has a nonzero zero iff `Arf(Q_β) = 0`, and `n₀ = 2q−1` in
that case, `n₀ = 1` otherwise; `κ/℘(κ)` has exactly two elements, so `Arf` is a
`Z/2`-valued, basis-free, `SL_2(κ)`-invariant type;
(f) **[p = 2]** two members of `Adm(ω)` are carried to each other by an
`SL_2(κ)`-isometry iff they have the same `Arf`; both types occur; the
hyperbolic class has `q(q+1)/2` quadratic forms and stabiliser
`|O(Q)∩SL_2(κ)| = 2(q−1)`, the anisotropic class `q(q−1)/2` and `2(q+1)`;
`H_β(κ) ≅ H_{β'}(κ)` iff `Arf(Q_β) = Arf(Q_{β'})`;
(g) **[p = 2]** the type is visible **inside the quantum system**:
`W_β(v)² = ψ(Q_β(v))·1` and `q^{-1}Σ_{v∈V} W_β(v)² = ε·1` with `ε = +1` for the
hyperbolic type and `ε = −1` for the anisotropic one;
(h) **the level statement.** For all `β,β' ∈ Adm(ω)` there is a frame
isomorphism `A_{ψ,β} → A_{ψ,β'}`, `W_β(v) ↦ μ(v)W_{β'}(v)`, at **every**
characteristic; `μ` can be taken `μ_p`-valued iff `ψ∘Q_β = ψ∘Q_{β'}`, and at
`p = 2` it can always be taken `μ_4`-valued. So `(A, F)` does not depend on `β`;
`F^{(p)}` — equivalently `H_β(κ)` — does, and only at `p = 2`.

`<1>1.` (a) If `β,β' ∈ Adm(ω)` then `s := β'−β` has `s − s^T = 0`, i.e. is
symmetric; conversely `β+s ∈ Adm(ω)` for symmetric `s`, freely and transitively.
A symmetric `κ`-bilinear form on `V = κ²` is free on `s(e,e), s(e,f), s(f,f)`, so
`|Sym(V)| = q³ = |Adm(ω)|`. **QED**
  `<2>1.` *Checked, exhaustively:* `theory/checks/wh_kappa/beta_census.py` gate `B1` re-verifies
  `β'−β'^T = ω` and `κ`-bilinearity for each of the `q³` members and finds them
  pairwise distinct, `q ∈ {2,3,4,5,8,9}`; `wh_kappa_check.py` gate `C10`
  re-verifies admissibility independently.

`<1>2.` (b) **[ODD p]** `<2>1.` `ω/2` is `κ`-bilinear with `ω/2 − (ω/2)^T =
ω/2 + ω/2 = ω`, and antisymmetric; two antisymmetric members differ by an `s`
both symmetric and antisymmetric, so `2s = 0`, so `s = 0`. `<2>2.` `ω/2` is
`SL_2(κ)`-invariant because `ω` is (Thm 1 `<1>5`) — a canonical point of the
torsor, at odd `p` only. `<2>3.` For `s ∈ Sym(V)` put `f(v) := s(v,v)/2`; then
`f(v+v') = f(v)+f(v')+s(v,v')` by bilinearity and symmetry, which is exactly the
condition for `φ_s(t,v) := (t+f(v), v)` to satisfy
`φ_s((t,v)(t',v')) = φ_s(t,v)φ_s(t',v')` for the two products `β` and `β+s`;
`φ_s` is bijective and fixes `κ×0`. **QED**
  `<2>4.` *Checked, exhaustively:* `theory/checks/wh_kappa/beta_census.py` gate `B4` verifies `φ_s` is
  an isomorphism on all `|V|²` pairs for **every** one of the `q³` members at
  `q = 3,5,9`; gate `B3` finds a single element-order profile
  `{1:1, p:q³−1}` there; red mode `--red-iso` (perturbing `φ_s` at one value)
  exits non-zero.

`<1>3.` (c) **[p = 2]** `−1 = 1`, so antisymmetric means symmetric, and a
symmetric `β` has `β − β^T = 0 ≠ ω` (`ω(e,f) = 1`, Thm 1 `<1>3`). So no member
of `Adm(ω)` is antisymmetric: the torsor has no point singled out by symmetry.
**QED** *(gate `B2`, both branches)*

`<1>4.` (d)(e) **[p = 2]** `<2>1.` `Q_β(v+v') = Q_β(v)+Q_β(v')+β(v,v')+β(v',v)
= Q_β(v)+Q_β(v')+ω(v,v')` (at `p = 2`, `+ = −`), and `Q_β(cv) = c²Q_β(v)`.
`<2>2.` In `H_β(κ)`, `(t,v)² = (2t+β(v,v), 2v) = (Q_β(v), 0)`; so a
non-identity `(t,v)` has order `2` iff `v = 0` or `Q_β(v) = 0`, and order `4`
otherwise (its square is then the non-identity central `(Q_β(v),0)`, of order
`2`). Counting: `q·n₀ − 1` elements of order `2` and `q³ − q·n₀` of order `4`.
`<2>3.` In a symplectic basis `(e,f)`, `ω(e,f) = 1`, `<2>1` gives
`Q_β(ae+bf) = αa² + ab + δb²` with `α := Q_β(e)`, `δ := Q_β(f)`. `<2>4.` `℘` is
additive at `p = 2` and `ker ℘ = {x : x² = x} = F_2` (a degree-2 polynomial has
at most 2 roots and `0,1` are roots), so `|℘(κ)| = q/2` and `κ/℘(κ)` has exactly
two elements. `<2>5.` *`Q_β` has a nonzero zero iff `αδ ∈ ℘(κ)`.* If `b = 0` the
zero condition is `αa² = 0`, solvable with `a ≠ 0` iff `α = 0`, and then
`αδ = 0 ∈ ℘(κ)`. If `b ≠ 0` scale to `b = 1`: `αa² + a + δ = 0`; multiplying by
`α` gives `(αa)² + (αa) = αδ`, i.e. `℘(αa) = αδ`, solvable for `a` iff
`αδ ∈ ℘(κ)` (for `α ≠ 0`; for `α = 0` take `a = δ`). `<2>6.` Hence
`{Arf = 0}` is the basis-free condition "`Q_β` is isotropic", and since
`κ/℘(κ)` has only two elements (`<2>4`) the class `αδ mod ℘(κ)` is itself
basis-free, so `SL_2(κ)`-invariant. `<2>7.` If `Arf = 0` the zero set is a union
of `κ`-lines (`Q_β(cv) = c²Q_β(v)`) and `<2>5` produces exactly two of them
(two roots of `℘(x) = αδ` when `α ≠ 0`; the lines `b = 0` and `a = δ` when
`α = 0`), so `n₀ = 2(q−1)+1 = 2q−1`; if `Arf ≠ 0` then `n₀ = 1`. **QED**
  `<2>8.` *Checked:* gate `B5` verifies `Arf` is constant on `SL_2(κ)`-orbits
  for all `q³` members `×` all `|SL_2|` group elements, and takes exactly two
  values, `q = 2,4,8`; gate `B6` reports `n₀ = 2q−1` and `1` in the two classes;
  gate `B3` finds exactly two order-profiles, of sizes `(6,2), (40,24),
  (288,224)` at `q = 2,4,8`; red mode `--red-arf-blind` exits non-zero.

`<1>5.` (f) **[p = 2]** `<2>1.` *Normal forms.* If `Arf(Q) = 0` pick `e` with
`Q(e) = 0`, `e ≠ 0` (`<1>4.<2>5`) and `f` with `ω(e,f) = 1` (nondegeneracy);
replacing `f` by `f + Q(f)e` gives `Q(f) = 0` and `Q(ae+bf) = ab`. If
`Arf(Q) ≠ 0` then `Q(v) ≠ 0` for `v ≠ 0`; pick any `e` and rescale by
`λ = Q(e)^{-1/2}` (Frobenius is bijective) to get `Q(e) = 1`, then `f` with
`ω(e,f) = 1`; replacing `f` by `f + ae` changes `Q(f)` by `℘(a)`, so `Q(f)` can
be moved to any chosen representative of its class `mod ℘(κ)`. `<2>2.` Both
normalisations send a symplectic basis to a symplectic basis, so they are
realised by elements of `SL_2(κ)` (Thm 1 `<1>5`): two forms with the same `Arf`
are `SL_2(κ)`-isometric, and two with different `Arf` are not (`<1>4.<2>6`).
`<2>3.` *Counting.* Over a fixed basis the forms with polar form `ω` are exactly
the `q²` maps `αa²+ab+δb²` (`<1>4.<2>3`) — the map `β ↦ Q_β` is `q`-to-1 on
`Adm(ω)`, its fibres being the translates by the alternating members `cω` of
`Sym(V)` — of which
`#{αδ ∈ ℘(κ)} = q + (q−1)(q/2) = q(q+1)/2` are hyperbolic and `q(q−1)/2`
anisotropic — **both classes are nonempty for every `q`**. By orbit–stabiliser
with `|SL_2(κ)| = q(q²−1)`, `|O(Q)∩SL_2(κ)| = 2(q−1)` and `2(q+1)` respectively.
`<2>4.` *Groups.* Same `Arf` gives `Q' = Q∘g`, `g ∈ SL_2(κ)`; then
`r(v,v') := β(gv,gv') − β'(v,v')` is symmetric with `r(v,v) = 0`, so
`f(v) := Σ_{i<j}c_ic_j r(b_i,b_j)` (coordinates on an `F_2`-basis `b_i` of `V`)
satisfies `f(v+v')−f(v)−f(v') = r(v,v')`, and `(t,v) ↦ (t+f(v), gv)` is an
isomorphism `H_{β'}(κ) → H_β(κ)`. Different `Arf` gives different `n₀` hence
different order profiles (`<1>4.<2>2`), so no isomorphism of any kind exists.
**QED**
  `<2>5.` *Checked:* gate `B6` computes `|O(Q)∩SL_2(κ)| = 2, 6, 14` (hyperbolic)
  and `6, 10, 18` (anisotropic) at `q = 2,4,8` by direct enumeration, matching
  `2(q∓1)`, and finds `O(Q)` computed in `GL_2` already inside `SL_2`; gate `B7`
  constructs the isomorphism of `<2>4` and verifies it on all pairs for every
  member of the hyperbolic class. The orchestrator's independent census
  (`briefs/lanes/wh-repair.md`) reports the same `6`/`2` split at `q = 2` with
  `D_4` and `Q_8`, and one class at `p = 3,5`.

`<1>6.` (g) **[p = 2]** `<2>1.` `W_β(v)² = ψ(β(v,v))W_β(2v) = ψ(Q_β(v))·1`
(`D4`, `2v = 0`). `<2>2.` For the hyperbolic normal form `Q(a,b) = ab`
(`<1>5.<2>1`), `Σ_{a,b}ψ(ab) = Σ_a(Σ_bψ(ab)) = q` by `L-ORTH` and `L-VAL`, so
`ε = +1`. `<2>3.` `Σ_vψ(Q(v))` is constant on isometry classes (`g` bijective).
Summing over all `q²` forms with polar form `ω` and exchanging the order:
`Σ_{α,δ}Σ_{a,b}ψ(αa²+ab+δb²) = Σ_{a,b}ψ(ab)(Σ_αψ(αa²))(Σ_δψ(δb²)) = q²`, since
by `L-ORTH` the inner sums vanish unless `a = 0` and `b = 0`. With `<2>2` and the
class sizes of `<1>5.<2>3`: `(q(q+1)/2)q + (q(q−1)/2)S = q²` forces `S = −q`.
So `ε = −1` on the anisotropic class. `<2>4.` Hence
`q^{-1}Σ_v W_β(v)² = ε·1` with `ε = ±1` reading off the type — an identity
**inside `A_{ψ,β}`**, so the type is an invariant of the level-`μ_p` frame
`F^{(p)}` and not merely of the auxiliary datum `β`. **QED**
  `<2>5.` *Checked:* gate `B6` computes the Gauss sum for all `q³` members at
  `q = 2,4,8` and finds `|Σ| = q` always, with the sign matching the type; gate
  `B8` verifies in addition that `Tr` kills `℘(κ)` and is onto `F_2`, and that
  the sign equals `Tr(Arf_κ(Q_β))` — the `κ`-level and `F_2`-level invariants
  agree, for all `q³` members.

`<1>7.` (h) **The level statement.** `<2>1.` Put `s := β' − β` ∈ `Sym(V)`.
`W_β(v) ↦ μ(v)W_{β'}(v)` is an algebra map iff
`μ(v)μ(v')/μ(v+v') = ψ(−s(v,v'))` `(†)`, and it preserves `F` by construction.
`ψ∘(−s)` is a symmetric 2-cocycle on the exponent-`p` group `V`, so `L-TRIV`
supplies `μ`: **the frame isomorphism exists at every characteristic.**
`<2>2.` *Necessity.* Setting `v' = v` in `(†)` at `p = 2` (`2v = 0`, `μ(0) = 1`)
gives `μ(v)² = ψ(s(v,v))`. So `μ` is `μ_2`-valued only if `ψ∘Q_β = ψ∘Q_{β'}`,
and if `ψ(s(v,v)) = −1` for some `v` then that `μ(v)` has exact order `4`.
`<2>3.` *Sufficiency in `μ_2` and in `μ_4`.* With `σ := ψ`-exponent of `s` and
`F_2`-coordinates `c_i` on a basis `b_i`: if `σ(v,v) ≡ 0` then
`l(v) := Σ_{i<j}c_ic_jσ_{ij}` solves `(†)` in `μ_2`; in general
`m(v) := 2Σ_{i<j}c_ic_jσ_{ij} + Σ_i c_iσ_{ii} ∈ Z/4` solves `(†)` with
`μ = i^m`. `<2>4.` **[ODD p]** `μ(v) := ψ(s(v,v)/2)` solves `(†)` inside `μ_p`,
so at odd `p` nothing leaves the level-`μ_p` frame — the second proof, after
`<1>2`, that the choice is immaterial there. **QED** *(Theorem WH-BETA)*
  `<2>5.` *Checked:* `theory/checks/wh_kappa/frame_mu.py` gate `M1` searches **all** `2^{q²}` candidate
  `μ_2` phase functions at `q = 2` and finds solutions for exactly the members
  with `ψ∘Q_β = ψ∘Q_{β'}`; `M2` and `M3` verify the explicit `l` and `m` on all
  `|V|²` pairs for every one of the `q³` members at `q = 2,4,8` (`μ_4` always
  works; `μ_2` for exactly `q` of the `q³`); `M4` does the odd-`p` case at
  `q = 3,5,9`. Red modes `--red-drop-linear`, `--red-mu2-always` exit non-zero.

`<1>8.` **What this says, stated once.** The assignment
`Spec κ ↦ (A_{ψ,β}(V), F)` depends on `(κ,ψ)` alone. The assignment
`Spec κ ↦ (A_{ψ,β}(V), F^{(p)})` — the Weyl operators as a finite group of
unitaries, which is the object the `p = 2` stabiliser formalism uses — depends
on `(κ,ψ,β)`, and at `p = 2` its isomorphism class is the two-valued type
`Arf(Q_β)`, equivalently the sign `ε` of `<1>6`. At odd `p` the `β`-dependence
is vacuous and `ω/2` is a canonical representative. **This is a sharp
non-canonicity statement, and per `PRD.md` it is a positive structural result
about the definition, not a negative one.**

## 7. Theorems WH-CHOICE and WH-CANON — the choices, and what is canonical

**ASSUME** `D1`–`D11`, Thms WH-ALG, WH-POL, WH-SVN, WH-BETA. **PROVE**
(a) `X(κ) := κ̂∖{1}` has `q−1` elements and is a `κ^×`-torsor; (b) **the data
beyond `κ` are exactly two**: a nontrivial `ψ ∈ X(κ)` and a polarizing cocycle
`β ∈ Adm(ω)`; given `(ψ,β)` the algebra involves no further choice, while a
Hilbert space needs `(L,χ)` in addition; (c) `Mod_{ψ,β}(κ)` is a connected
groupoid with automorphism group `U(1)` at every object; (d) the **projective**
Hilbert space is canonical in `(κ,ψ)` — and, by WH-BETA `<1>7`, also independent
of `β`; (e) distinct `ψ` give representations of the same group `H_β(κ)` with
distinct central characters, hence inequivalent; (f) `A_{ψ,β} ≅ A_{ψ',β'}`
always, but the frame-preserving isomorphisms form a torsor under a group of
order `q²|SL_2(κ)| ≥ 24`, so none is distinguished.

`<1>1.` (a) `|κ̂| = q` by `L-DUAL` (`U = κ`), so `|X(κ)| = q−1`. `κ^×` acts by
`(u·ψ)(x) := ψ(ux)`, preserving nontriviality, and freely (`u·ψ = ψ` forces
`ψ((u−1)·) ≡ 1`, so `u = 1` by `L-VAL`); a free action of a group of order `q−1`
on a set of that size is transitive. **QED**
  `<2>1.` `X(κ) ≠ ∅` concretely: `Tr_{κ/F_p}(z) = z+z^p+⋯+z^{p^{m−1}}`
  (`refs/arxiv-2202.00248/EAQECCs_over_rings_v15.tex:794`) is a nonzero
  polynomial of degree `p^{m−1} < q`, so `Tr(z) ≠ 0` for some `z`; `Tr` lands in
  `F_p` as `Tr(z)^p = Tr(z)`; so `ψ_ζ` is nontrivial.
  `<2>2.` `ζ` is a further choice among `p−1` primitive roots, and
  `ψ_{ζ^k} = ψ_ζ(k·)`: the `ζ`-choice is the `F_p^×`-suborbit inside the
  `κ^×`-torsor. **Degenerate case (erratum E5):** at `κ = F_2`, `κ^×` is trivial,
  `X(κ)` is a single point, and the "two distinct primitive `ζ`" formulation is
  vacuous — `β`, not `ψ`, is where the `q = 2` choice lives.
  `<2>3.` Corroboration only: `refs/arxiv-1710.09884/StabCodesFrob5.tex:242`
  states for a finite commutative Frobenius ring that any two generating
  characters differ by a unit, and `:245` names finite fields; this shard proves
  (a) from `L-DUAL` instead of leaning on it.

`<1>2.` (b) `A_{ψ,β}(V)` uses `D1`,`D2`,`D4`, `ψ` **and `β`**; a model needs
`(L,χ)` (Thm 4 `<1>3`). Round 1's "exactly one datum" is refuted by WH-BETA
`<1>1`,`<1>4`: *two* data, the second immaterial at odd `p` and two-valued at
`p = 2`. **QED**

`<1>3.` (c) Objects of `Mod_{ψ,β}(κ)`: pairs `(M,π)` with `M` simple and every
`π(W(v))` unitary; morphisms: unitary intertwiners. Nonempty and connected by
Thm 5 `<1>1`,`<1>3`,`<1>5`; `Aut(M,π) = U(1)` by Thm 5 `<1>3.<2>4` with
unitarity. **QED**

`<1>4.` (d) Let `PMod_{ψ,β}` have the same objects and `Hom/U(1)`. By `<1>3`
**every Hom-set is a singleton**. Hence every square of transition maps commutes
— both composites are *the* unique morphism, so naturality is performed, not
asserted — and `PMod` is equivalent to the terminal category, so
`lim P(M)` exists with every projection an isomorphism. Define `P(H_ψ(κ))` to be
that limit. `<2>1.` It does not depend on `β` either: WH-BETA `<1>7` gives a
frame isomorphism `A_{ψ,β} → A_{ψ,β'}`, and transport of structure along it is
an equivalence `Mod_{ψ,β} → Mod_{ψ,β'}`; both categories having singleton
projective Hom-sets, the induced map on limits is the unique isomorphism.
**The projective Hilbert space is canonical in `(κ,ψ)`; the Hilbert space is
not, and the level-`μ_p` frame inside it is not.** **QED**

`<1>5.` (e) A representation of `H_β(κ)` restricts on the centre to `ψ·id`, so
`ψ ≠ ψ'` gives non-isomorphic representations of the *same* group: no
identification of the underlying spaces is `H_β(κ)`-linear. **QED**

`<1>6.` (f) `W_ψ(a,b) ↦ W_{ψ_u}(u^{-1}a,b)` is an isomorphism
`A_{ψ,β₀} → A_{ψ_u,β₀}`, since `β₀(u^{-1}a,b') = u^{-1}β₀(v,v')`.
  `<2>1.` The frame-preserving isomorphisms `A_{ψ,β} → A_{ψ',β'}` form a free
  transitive `Aut_F^κ(A_{ψ,β})`-set, of order `q²|SL_2(κ)| ≥ 4·6` by Thm 8
  `<1>2`,`<1>3`. More than one exists and the data `(V,ω,β,F,ψ,ψ')` name none.
  `<2>2.` Coherent systems `{φ_u}`, `φ_{u'}φ_u = φ_{uu'}`, do exist —
  `h_u := diag(u^{−j},u^{j−1})`, `j ∈ Z/(q−1)`, and distinct `j` give distinct
  systems — so the family is trivialisable but **not canonically**: a "value at
  `κ`" is a section, not a theorem. **QED** *(WH-CHOICE, WH-CANON)*

## 8. Theorem WH-WEIL(a–g) — symmetry, and where the characteristic bites

Fix `β ∈ Adm(ω)`. Write `g = [[r,s],[t,u]] ∈ SL_2(κ)`,
`s_g(v,v') := β(gv,gv') − β(v,v')`, `Q_g(v) := s_g(v,v)`; note
`Q_g(v) = Q_β(gv) − Q_β(v)`.

`<1>1.` `s_g` is symmetric bi-additive and `s_{gh}(v,v') = s_h(v,v') +
s_g(hv,hv')`. `<2>1.` Symmetry: `s_g(v,v') − s_g(v',v) = ω(gv,gv') − ω(v,v') = 0`
by Thm 1 `<1>5`. `<2>2.` Telescope `β(ghv,ghv') − β(v,v')` through `β(hv,hv')`.
`<2>3.` For `β = β₀`: `s_g(v,v') = rt·aa' + st·(ab'+a'b) + su·bb'` (expand
`β₀(gv,gv') = rt aa' + ru ab' + st a'b + su bb'`, subtract `ab'`, use
`ru − 1 = st`). **QED**

`<1>2.` `Aut_F^κ(A)` (`D7`) is `{α_{g,λ} : α(W(v)) = λ(v)W(gv)}` with
`g ∈ SL_2(κ)` and `(∗) λ(v)λ(v')ψ(s_g(v,v')) = λ(v+v')`; `α ↦ g` is a
homomorphism with kernel `V̂` of order `q²`, and every kernel element is
`Ad_{W(u)}`. `<2>1.` Frame preservation gives `α(W(v)) = λ(v)W(gv)` with `g`
additive; multiplicativity is `(∗)`; `κ`-linearity of `g` is *imposed* in `D7`
(and by Thm 1 `<1>6` it is automatic once `ω∘g = ω`, but not once only
`ψ∘ω∘g = ψ∘ω` — §9). `<2>2.` `g ∈ SL_2(κ)`: applying `α` to Thm 2 (c) gives
`ψ((det g −1)ω(v,v')) = 1` for all `v,v'`; `ω` is onto `κ`, so `det g = 1` by
`L-VAL`. `<2>3.` For `g = 1`, `(∗)` says `λ ∈ V̂`, of order `q²` (`L-DUAL`,
`U = V`, `d = 2m`); `u ↦ ψ(ω(u,·))` is injective `V → V̂` (argument of Thm 3
`<1>1.<2>2`) hence bijective, so each such `α` is `Ad_{W(u)}` (Thm 2 (d)).
**QED**

`<1>3.` **[uniform in `p`]** `Aut_F^κ(A) → SL_2(κ)` is **onto**:
`c(v,v') := ψ(s_g(v,v'))` is a symmetric 2-cocycle on `V`, of exponent `p`, so
`L-TRIV` supplies `λ` solving `(∗)`. Hence
`1 → V̂ → Aut_F^κ(A) → SL_2(κ) → 1` is exact at every characteristic. **QED**
  `<2>1.` *Checked:* `theory/checks/wh_kappa/split24.py` gate `X2` enumerates every fibre by complete
  search and finds `|Aut_F^κ| = 24, 216, 960, 3000 = q²|SL_2(κ)|` at
  `q = 2,3,4,5`, every fibre of size exactly `q²`; red mode `--red-fibre` exits
  non-zero.

`<1>4.` **[ODD p]** `α_g(W(v)) := ψ(Q_g(v)/2)W(gv)` is a **splitting**: `(∗)`
holds since `Q_g(v+v') = Q_g(v)+Q_g(v')+2s_g(v,v')`, and `α_gα_h = α_{gh}` by
`<1>1`. So at odd `p`, `SL_2(κ)` acts on `A_{ψ,β}` by algebra automorphisms with
`μ_p` phases. **QED** *(gate `X4`, `q = 3,5`: a subgroup of order `|SL_2(κ)|`
meeting `V̂` trivially)*

`<1>5.` **[p = 2]** `α_{g,λ}` has phases in `ψ(κ) = μ_2` **iff**
`g ∈ O(Q_β) := {g : Q_β∘g = Q_β}`. `<2>1.` Setting `v' = v` in `(∗)` with
`2v = 0` gives `λ(v)² = ψ(Q_g(v))`; so `λ` is `μ_2`-valued iff
`Q_g(V) ⊆ ker ψ`, i.e. iff `ψ∘Q_β∘g = ψ∘Q_β`. `<2>2.` *For every `β`, that is
already the exact isometry condition.* `Q_g(v) = Q_β(gv) − Q_β(v)` is
**additive** (the `ω`-terms cancel, `ω∘g = ω`) with `Q_g(cv) = c²Q_g(v)`, so
`Q_g(a,b) = αa² + δb²` in a basis; if `ψ∘Q_g ≡ 1` then `ψ(αa²) = 1` for all `a`,
and `a ↦ a²` is bijective, so `α = 0` by `L-VAL`, likewise `δ = 0`. Hence
`ψ∘Q_g ≡ 1` iff `Q_g ≡ 0` iff `g ∈ O(Q_β)`. Conversely, if `Q_g ≡ 0` then
`ψ∘s_g` is a symmetric cocycle with trivial diagonal and Thm 6 `<1>7.<2>3`
supplies a `μ_2`-valued `λ` (for `β₀`, explicitly `λ = ψ∘f` with `f(v) = st·ab`,
using `Q_g(v) = rt·a² + su·b²` from `<1>1.<2>3`). `<2>3.` By
WH-BETA `<1>5`, `|O(Q_β)∩SL_2(κ)| = 2(q−1)` for the hyperbolic type — the type
of `β₀`, where solving `rt = su = 0, det = 1` gives exactly `diag(r,r^{-1})` and
`antidiag(s,s^{-1})` — and `2(q+1)` for the anisotropic type. **QED**
  `<2>4.` **Proper, with one exception, and the exception is `β`-visible.**
  `2(q−1) < q(q²−1)` always; `2(q+1) < q(q²−1)` **except at `q = 2`**, where
  `2(q+1) = 6 = |SL_2(F_2)|`. So the `μ_2`-phase subgroup is proper for every
  hyperbolic `β`, and for anisotropic `β` proper iff `q ≥ 4`. The round-1 claim
  "`O(Q)∩SL_2` is proper at `p = 2`" was true for `β₀` and false as a
  characteristic-2 invariant — OBJ-1(b)'s counterexample, now inside the
  statement. *Checked:* `runs/split24-anisotropic-q2.txt`, where the
  hyperbolic-type gates fire against the anisotropic cocycle at `q = 2`,
  reporting a `μ_2` part of order `24 = |Aut_F^κ|`.

`<1>6.` **[p = 2] `μ_4`, exactly when the type forces it.** For any `α_{g,λ}`,
`λ(v)² = ψ(Q_g(v))` (`<1>5.<2>1`). If `g ∉ O(ψ∘Q_β)` then `ψ(Q_g(v)) = −1` for
some `v`, and that `λ(v)` has exact order 4: **every** frame automorphism over
such a `g` carries a phase of order 4. Since `O(Q_β)∩SL_2(κ)` is proper except
in the single case (`q = 2`, anisotropic type) of `<1>5.<2>4`, `μ_4` is forced
for every `β` at every `q ≥ 4`, and for `β` of hyperbolic type at `q = 2`; it is
**not** forced for the anisotropic `β` at `q = 2`. **QED**

`<1>7.` **Projective unitary representations (OBJ-4).** Fix a model `(M,π)`.
`<2>1.` *Phases are unimodular.* Taking absolute values in `(∗)` makes
`v ↦ |λ(v)|` a homomorphism from a finite group to `R_{>0}`, hence trivial:
`|λ| = 1`. `<2>2.` Every `α ∈ Aut_F^κ(A)` is `Ad_T` with `T` unique up to a
scalar (Thm 5 `<1>4`); by `<2>1` `α` permutes the *unitary* Weyl operators, so
`T` may be chosen unitary and is then unique up to `U(1)` (Thm 5 `<1>5`). This
gives an injective homomorphism `Aut_F^κ(A) → PU(M)`: **a projective unitary
representation of `Aut_F^κ(A)`, at every characteristic.**
  `<2>3.` *What is not true.* `Aut_C(A) ≅ PGL_q(C)` does **not** map to `PU(M)`
  by `Ad`: at `q = 2`, `T = diag(2,1)` conjugates `π(W(1,0)) = [[0,1],[1,0]]` to
  `[[0,2],[1/2,0]]`, whose singular values `2, 1/2` differ, so it is not a
  scalar times a unitary. The round-1 shard wrote `Aut(A_ψ)` where it needed
  `Aut_F`; corrected here (OBJ-4), and the frame hypothesis is what `<2>1` uses.
  `<2>4.` **[ODD p]** composing with `<1>4` gives a projective unitary
  representation of `SL_2(κ)`.
  `<2>5.` **[p = 2]** For `β₀`: `SL_2(κ)` acts projectively **iff** the extension
  of `<1>3` splits; see `<1>8`. Per ledger note **N1**, a uniform-in-`p` claim
  that "`SL_2(κ)` acts projectively" would claim more than the sources support,
  and by `<1>5` the `μ_p`-phase version is false at `p = 2`. **QED**

`<1>8.` **[p = 2] The extension splits at `q = 2` and `q = 4` (OPEN-1).**
`<2>1.` *Credit.* Answered by the round-1 verdict
(`theory/verdicts/wh-kappa-r1.md`, "Open questions the critic closed"); the
result is the critic's, the verification is this lane's and shares no code with
it. `<2>2.` At `q = 2` (`|Aut_F^κ| = 24`) exhaustive search over all generating
pairs finds **4 distinct complements of `V̂` of order 6**, every one using a
phase of exact order 4 (`theory/checks/wh_kappa/split24.py` `X4`). `<2>3.` At `q = 4`, lifting a
`(2,3,5)` generating pair of `SL_2(F_4)` over all `16×16` phase choices, **64
lifts** satisfy `x² = y³ = (xy)^5 = 1` and generate a subgroup of order 60
meeting `V̂` trivially; all 64 use order-4 phases (`X5`). `<2>4.` *No complement
avoids `μ_4`* for `β₀`: the `μ_2` part has order `q²·2(q−1)` and `|SL_2(κ)|`
does not divide it at `q = 2,4` (`6 ∤ 8`, `60 ∤ 96`) — `X6`. `<2>5.` So the
projective unitary representation of `SL_2(κ)` **exists** at `q = 2,4` for `β₀`
and needs `μ_4`; the general `p = 2` case stays open. Red modes `--red-fibre`,
`--red-mu2split` exit non-zero. **QED**

`<1>9.` **Relation to the registered char-2 source, stated exactly.**
`refs/arxiv-0808.1664/WeilCharTwo12-8-08.tex:100-110`: Weil's own
characteristic-2 construction reaches only `1 → V^* → Ps(V) → O(Q) → 1`, with
`Q(v) = β(v,v)` "for some non-symmetric bilinear form `β`" satisfying
`β(v,u) − β(u,v) = ω(v,u)` — the same `Q` as `D6`, the same admissibility as
`D2`, and the same "for some" that WH-BETA turns into a theorem; `<1>5` derives
independently, for `V(κ) = κ⊕κ`, that the `μ_p`-phase group is exactly
`O(Q_β)`. `:795-800` linearises only over `AMp(V)`, a central extension of
`ASp(V)` by `μ_4` — the register `<1>6`,`<1>8` land in — while `:771-793` gets
the **projective** representation from Stone–von Neumann at every
characteristic, matching `<1>7.<2>2`. Agreement is evidence, not proof either
way; the two `μ_4`'s live over different groups (OPEN-4). **QED** *(WH-WEIL)*

## 9. Theorem WH-SYMM — the `κ`-structure is not recoverable from the system

*The second canonicity finding of the increment (OBJ-3). `D7` imposes
`κ`-linearity; the algebra cannot see it.*

**ASSUME** `D1`–`D7`. **PROVE** (a) `A_{ψ,β}(V)` and its frame `F` are built from
the abelian group `(V,+)` and the `C^×`-valued cocycle `ψ∘β` alone, so nothing in
the object refers to the `κ`-module structure of `V`; (b) the frame
automorphisms with merely `F_p`-linear `g` surject onto
`Sp(V, ψ∘ω) ≅ Sp_{2m}(F_p)`, with the same kernel `V̂`, so
`|Aut_F(A)| = q²·|Sp_{2m}(F_p)|`; (c) `SL_2(κ) ⊆ Sp_{2m}(F_p)` with index
`> 1` as soon as `m > 1`, so `D7`'s clause discards symmetry the system has;
(d) **[p = 2]** the orthogonal phenomenon of Thm 8 `<1>5` survives the
enlargement, with the same index.

`<1>1.` (a) `D4` defines `A` by structure constants `ψ(β(v,v'))` indexed by
`(V,+)`, `D7` defines `F` as the lines `C^×W(v)`; neither mentions `κ`-scaling.
**QED**

`<1>2.` (b) Repeat Thm 8 `<1>2` **without** the `κ`-linearity clause: the same
computation gives `α(W(v)) = λ(v)W(gv)` with `g` additive, `(∗)` unchanged, and
— since Thm 2 (c) is an identity in `ψ∘ω` — the constraint on `g` is
`ψ(ω(gv,gv')) = ψ(ω(v,v'))`, i.e. `g ∈ Sp(V,ψ∘ω)`, **not** `ω∘g = ω`. `L-TRIV`
applies verbatim, so every such `g` lifts and the kernel is again `V̂`. `ψ∘ω` is
a nondegenerate alternating `F_p`-valued form on the `2m`-dimensional
`F_p`-space `V` (nondegenerate: `ψ(ω(v,·)) ≡ 1` forces `ω(v,·) ≡ 0` by `L-VAL`
and `ω(v,·)` being onto, hence `v = 0`), so its isometry group is
`Sp_{2m}(F_p)`. **QED**

`<1>3.` (c) `SL_2(κ) ⊆ Sp(V,ψ∘ω)` since `ω∘g = ω` implies `ψ∘ω∘g = ψ∘ω`, and by
Thm 1 `<1>6` the containment is exactly the difference between preserving the
`κ`-valued form and preserving its `ψ`-shadow. **QED**
  `<2>1.` *Checked, by complete enumeration* (`theory/checks/wh_kappa/fp_symmetry.py` `S1`,`S2`):
  `|SL_2(κ)| = 6, 24, 60, 120, 504, 720` against `|Sp_{2m}(F_p)| = 6, 24, 720,
  120, 1451520, 51840` at `q = 2,3,4,5,8,9` (indices `1,1,12,1,2880,72`),
  matching `p^{m²}∏_{i=1..m}(p^{2i}−1)` in every case; red mode
  `--red-sp-formula` exits non-zero. At `m = 1` — the prime field, the
  campaign's guiding path — the two coincide; for `m > 1` `D7` discards the
  index.

`<1>4.` (d) **[p = 2]** The `μ_2`-phase condition of Thm 8 `<1>5.<2>1` is
`ψ∘Q_β∘g = ψ∘Q_β`, which is meaningful for `F_p`-linear `g` as well;
`ψ∘Q_β` is an `F_p`-valued quadratic form on `V` with polar form `ψ∘ω`, so the
subgroup is `O(ψ∘Q_β) ∩ Sp_{2m}(F_p)`. *Checked* (`S3`): at `q = 2, 4, 8` its
orders are `2, 72, 40320` and its index in `Sp_{2m}(F_p)` is `3, 10, 36` — the
**same index** as `|O(Q_β)∩SL_2(κ)| = 2, 6, 14` has in `SL_2(κ)`. The
characteristic-2 orthogonal phenomenon is therefore not an artefact of the
imposed `κ`-linearity. **QED** *(Theorem WH-SYMM)*

`<1>5.` **Reading.** Two independent non-canonicities are now separated: the
system does not remember `β` (Thm 6), and it does not remember the `κ`-structure
of `V` (this theorem). Both are statements *about the definition*, and any
general `Spec R ↦ quantum system` assignment restricting to this one carries
them.

## 10. Theorem WH-FUNCT(a–d) — functoriality in `κ`, and the sections that exist

`<1>1.` **(a, negative; scoped per OBJ-7)** For `κ = F_{p^m} ⊆ κ' = F_{p^{mn}}`
the **trace-normalised family with a common `ζ`** is not restriction-compatible:
`ψ'_ζ|_κ = ψ_{ζ^n}`, trivial exactly when `p | n`. `<2>1.` For `x ∈ κ`,
`x^{p^m} = x`, so the summands of `Tr_{κ'/F_p}(x) = Σ_{k<mn} x^{p^k}` repeat with
period `m`: `Tr_{κ'/F_p}|_κ = n·Tr_{κ/F_p}`. `<2>2.` Hence `ψ'_ζ(x) = ψ_ζ(x)^n`,
and `ζ^n = 1` iff `p | n`. Smallest instance `F_2 ⊂ F_4`. `<2>3.` The row says
*the trace-normalised family*, not "the obvious functor": the round-1 wording
quantified over candidates the proof never touched. The statement that
quantifies over **all** families is `<1>3`. **QED**
  `<2>4.` *Checked* (`theory/checks/wh_kappa/funct_sections.py` gate `F1`): `n·Tr` verified for
  `F_2⊂F_4, F_2⊂F_8, F_4⊂F_16, F_3⊂F_9, F_3⊂F_27, F_2⊂F_16, F_9⊂F_81`, with the
  restriction trivial exactly at `p | n`; red mode `--red-restrict` exits
  non-zero.

`<1>2.` **(b, the functor)** Let `FF^±` have objects `(κ,ψ)`, `ψ ∈ X(κ)`, and
morphisms `(κ,ψ) → (κ',ψ')` the field embeddings `ι` with `ψ'∘ι = ψ`. Then
`(κ,ψ) ↦ A_{ψ,β₀}(V(κ))` is a functor to unital `C`-algebras and injective
homomorphisms. `<2>1.` `V(ι)(a,b) := (ιa,ιb)` is additive with
`β₀(V(ι)v,V(ι)v') = ι(β₀(v,v'))`. `<2>2.` `W(v) ↦ W'(V(ι)v)` sends basis to
distinct basis elements and is multiplicative because `ψ'(ι β₀(v,v')) =
ψ(β₀(v,v'))`; it is unital and nonzero, hence injective (Thm 3 `<1>3`), and it
respects composition and identities on basis elements because `V(−)` does.
**QED** *(gate `F5`: all structure constants compared for every
character-compatible `F_2→F_4`, `F_2→F_8`, `F_4→F_16`, and
`F_2→F_4→F_16 = F_2→F_16`)*

`<1>3.` **(c, no section over the full category — OBJ-2)** There is **no**
choice of `ψ_κ ∈ X(κ)`, one for each finite field, compatible with *all* field
embeddings. `<2>1.` Frobenius `x ↦ x^p` is an embedding `κ → κ`, so a section
must satisfy `ψ_κ∘Frob = ψ_κ`. `<2>2.` Writing `ψ_c := ψ_ζ(c·)`,
`ψ_c(x^p) = ζ^{Tr(cx^p)} = ζ^{Tr(c^{1/p}x)} = ψ_{c^{1/p}}(x)` (using
`Tr(y^p) = Tr(y)` and bijectivity of Frobenius), so `ψ_c` is Frobenius-invariant
iff `c^{1/p} = c` iff `c ∈ F_p`. `<2>3.` Take `κ = F_{p^p}`. For `c ∈ F_p^×` and
`x ∈ F_p`, `Tr_{κ/F_p}(cx) = p·cx = 0`, so every Frobenius-invariant character of
`F_{p^p}` restricts **trivially** to `F_p` — contradicting `ψ_{F_p} ∈ X(F_p)`
along the inclusion `F_p ⊂ F_{p^p}`. First instance `F_2 ⊂ F_4`. **QED**
  `<2>4.` *Credit and check.* The obstruction is the round-1 verdict's (OBJ-2);
  recomputed by `theory/checks/wh_kappa/funct_sections.py` gates `F2`,`F3`: the Frobenius-invariant
  characters of `F_4, F_8, F_16, F_9, F_27` number exactly `p` each, and for
  `F_4`, `F_27` no nontrivial one survives restriction to the prime field; red
  mode `--red-section-exists` exits non-zero. The round-1 "sections exist by
  induction along `F_{p^{n!}}`" is **refuted**, and its route was insufficient
  anyway (a character of `F_{p^{n!}}` may restrict trivially to an intermediate
  field).

`<1>4.` **(d, the sections that do exist)** Over the inclusion poset of the
subfields of a fixed algebraic closure `\bar F_p`, the compatible systems
`(ψ_κ)` are **exactly** the restrictions of the additive characters `Ψ` of
`(\bar F_p,+)` with `Ψ|_{F_p} ≠ 1`. `<2>1.` Given such a `Ψ`, `ψ_κ := Ψ|_κ` is
compatible by construction and nontrivial for every `κ`, since `F_p ⊆ κ` and
`Ψ|_{F_p} ≠ 1`. `<2>2.` Conversely a compatible system defines `Ψ(x) := ψ_κ(x)`
for any `κ ∋ x` — well defined by compatibility, additive because any two
elements lie in a common finite subfield — and `Ψ|_{F_p} = ψ_{F_p} ≠ 1`.
`<2>3.` The condition "nontrivial on every subfield" is therefore equivalent to
"nontrivial on the prime field". **QED**
  `<2>4.` *Checked* (gate `F4`): in `F_16`, `8` of the `15` nontrivial characters
  restrict nontrivially to **every** subfield and they are exactly the `8` with
  `Tr(c) ≠ 0`; likewise `54` of `80` in `F_81` and `32` of `63` in `F_64`.

`<1>5.` **Not claimed:** functoriality in `κ` for the *system* (only the algebra,
`<1>2`); and no compatible choice of `β` along embeddings — `β₀` is used in
`<1>2` because it is *stipulated*, not canonical (Thm 6 `<1>3`); whether the
type can be chosen compatibly at `p = 2` is **OPEN-5**. **QED** *(WH-FUNCT)*


## 11. Ledger

Shared with `wh-kappa.md` ("Ledger of the shard pair"); nothing here is `[ADMITTED]`.
