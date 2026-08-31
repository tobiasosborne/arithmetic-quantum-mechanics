<!-- ROLE: proposed edits to files OUTSIDE this lane's write scope. Keyed by
     STRING ANCHORS, never line numbers (PRD lane discipline). The orchestrator
     applies these. Nothing here has been written to the trunk by this lane. -->

# PATCH — proposed additions to `definitions.md` and `notation.md`

Two targets: `definitions.md` (nine new `Dn`) and `notation.md` (one table
block). Both files are currently empty of content, so each patch is a single
anchored replacement.

**Anchor collision warning.** Both anchors are the "nothing yet" placeholders.
If a concurrent lane's patch has already consumed them, apply these entries by
**appending** instead: for `definitions.md`, after the last `## D…` heading; for
`notation.md`, as extra rows at the end of the symbol table, dropping any row
whose symbol is already present.

**Stipulation discipline.** `definitions.md` says a definition is a stipulation
and that any asserted *property* is a claim. The entries below therefore
stipulate only. Nondegeneracy, `ω(v,v) = 0`, simplicity, the dimension count,
the Weyl law for the standard model, and the character count are **claims** and
live in `./CLAIMS-ROWS.md`, not here.

---

## Patch 1 — `definitions.md`

**ANCHOR (replace this exact line):**

```
*No definitions yet.*
```

**REPLACEMENT:**

```
## D1 (the symplectic object of a finite field)

For a finite field `κ`, put `V(κ) := κ ⊕ κ` and define
`ω : V(κ) × V(κ) → κ` by `ω((a,b),(a',b')) := a b' − a' b`.
Stipulation only; that `ω` is `κ`-bilinear, satisfies `ω(v,v) = 0`, and is
nondegenerate is claim `WH-FORM`. Uniform in the characteristic; `p = 2` is in
scope.

## D2 (the polarizing cocycle, non-symmetrized)

`β : V(κ) × V(κ) → κ`, `β((a,b),(a',b')) := a b'`.
This ordering and this non-symmetrized form are fixed once and never varied.
The symmetrized alternative `ω/2` is unavailable at `p = 2` and is therefore not
an option at any characteristic in this campaign.

## D3 (the phase datum, and the two choices it hides)

A *phase datum* for `κ` is an additive character `ψ : (κ,+) → C^×` with
`ψ ≢ 1`. Write `X(κ)` for the set of such `ψ`.
The *trace-normalized family*: `Tr_{κ/F_p}(z) := z + z^p + ⋯ + z^{p^{m−1}}` for
`κ = F_{p^m}`, and `ψ_ζ := ζ^{Tr_{κ/F_p}(·)}` for `ζ` a primitive `p`-th root of
unity in `C`.
**Two named choices:** `ψ` itself, and — inside the distinguished family — `ζ`.
Neither is canonical and neither is ever suppressed. `Tr_{κ/F_p}` is canonical.

## D4 (Weyl operators and the observable algebra)

`A_ψ(V) := ⨁_{v ∈ V(κ)} C·W(v)` with product fixed on basis elements by
`W(v)W(v') := ψ(β(v,v')) W(v+v')`.
This ordering is fixed once. Depends on `κ` and `ψ` and on nothing else.

## D5 (the Heisenberg group of κ, choice-free)

`H(κ) := κ × V(κ)` with `(t,v)(t',v') := (t + t' + β(v,v'), v + v')`.
No character is chosen: `H(κ)` depends on `κ`, `D1` and `D2` alone, and
`A_ψ(V)` is its group algebra with the centre set to `ψ`.

## D6 (the characteristic-two quadratic form)

`Q : V(κ) → κ`, `Q(v) := β(v,v)`; explicitly `Q(a,b) = ab`.
Recorded because it is identically zero under any symmetrized convention and is
not zero here; it is the object that separates the characteristics.

## D7 (the Weyl frame and its automorphisms)

The *Weyl frame* is `F_ψ := { C^×·W(v) : v ∈ V(κ) } ⊂ A_ψ(V)`.
`Aut_F(A_ψ)` is the group of `C`-algebra automorphisms `α` of `A_ψ(V)` with
`α(F_ψ) = F_ψ` whose induced permutation of `V(κ)` is **`κ`-linear**. The
`κ`-linearity requirement is part of the definition, not a lemma.

## D8 (Schrödinger models, and the standard model)

For a `κ`-line `L ⊂ V(κ)` put `A_L := span_C{ W(l) : l ∈ L } ⊆ A_ψ(V)`. Given a
unital `C`-algebra character `χ : A_L → C`, the *Schrödinger model* of `(L,χ)`
is `M_{L,χ} := A_ψ(V) ⊗_{A_L} C_χ`.
The *standard model* is `M₀ := ⨁_{y ∈ κ} C·e_y` with `{e_y}` declared
orthonormal and

    W(a,b) e_y := ψ(−b(y+a)) e_{y+a},   i.e.   W(a,b) = Z(−b)X(a),

where `X(a)e_y := e_{y+a}` and `Z(b)e_y := ψ(by)e_y`.
The sign is not cosmetic: the naive `Z(b)X(a)` realizes the cocycle `−ab'`, not
`D2`'s `ab'`, and the discrepancy is invisible at `p = 2`. That `M₀` satisfies
`D4` is claim `WH-SVN`.

## D9 (the model groupoid)

`Mod_ψ(κ)` is the category whose objects are pairs `(M,π)` with `π : A_ψ(V) →
End_C(M)` a unital algebra map making `M` a simple `A_ψ(V)`-module and every
`π(W(v))` unitary, and whose morphisms are unitary intertwiners.
`PMod_ψ(κ)` is the same category with `Hom` replaced by `Hom/U(1)`.
```

---

## Patch 2 — `notation.md`

**ANCHOR (replace this exact block, header rows included):**

```
| symbol | meaning | first fixed in |
|---|---|---|

*No symbols yet.*
```

**REPLACEMENT:**

```
| symbol | meaning | first fixed in |
|---|---|---|
| `p`, `m`, `q` | prime, degree, `q = p^m` | D1 |
| `κ`, `F_p` | the finite field `F_q`; its prime field | D1 |
| `V(κ)` | `κ ⊕ κ`, the symplectic object | D1 |
| `v = (a,b)` | a vector of `V(κ)` | D1 |
| `ω` | `ω((a,b),(a',b')) = ab' − a'b` | D1 |
| `β` | `β((a,b),(a',b')) = ab'` | D2 |
| `Q` | `Q(v) = β(v,v) = ab` | D6 |
| `ψ` | a nontrivial additive character of `(κ,+)` | D3 |
| `X(κ)` | the set of nontrivial additive characters | D3 |
| `κ̂`, `V̂` | `Hom((κ,+),C^×)`, `Hom((V,+),C^×)` | D3 |
| `ζ` | a primitive `p`-th root of unity in `C` | D3 |
| `ψ_ζ` | `ζ^{Tr_{κ/F_p}(·)}` | D3 |
| `Tr_{κ/F_p}` | absolute trace `z + z^p + ⋯ + z^{p^{m−1}}` | D3 |
| `μ_p`, `μ_4`, `U(1)` | `p`-th, 4th roots of unity; unit circle | D3 |
| `W(v)` | Weyl operator / basis element of `A_ψ(V)` | D4 |
| `A_ψ(V)` | the twisted algebra `⨁_v C·W(v)` | D4 |
| `H(κ)` | the choice-free Heisenberg group `κ × V(κ)` | D5 |
| `F_ψ` | the Weyl frame `{C^×W(v)}` | D7 |
| `Aut_F(A_ψ)` | frame-preserving, `κ`-linear automorphisms | D7 |
| `L`, `A_L` | a `κ`-line in `V(κ)`; its subalgebra | D8 |
| `χ`, `C_χ` | a character of `A_L`; its 1-dimensional module | D8 |
| `M_{L,χ}`, `M₀` | Schrödinger model of `(L,χ)`; the standard model | D8 |
| `e_y`, `X(a)`, `Z(b)` | standard basis; shift and phase operators | D8 |
| `Mod_ψ(κ)`, `PMod_ψ(κ)` | the model groupoid; its projectivization | D9 |
| `P(H_ψ(κ))` | the canonical projective Hilbert space | D9 |
| `P¹(κ)` | the projective line: the `q+1` lines of `V(κ)` | D1 |
| `SL_2(κ)` | `κ`-linear automorphisms of `V(κ)` of determinant 1 | D1 |
| `O(Q)` | `{ g ∈ SL_2(κ) : Q ∘ g = Q }` | D6 |
| `s_g` | `s_g(v,v') = β(gv,gv') − β(v,v')` | D7 |
| `E` | the Weyl average `q^{-2} Σ_u W(u)(·)W(u)^{-1}` | D4 |
| `FF^±` | the category of pairs `(κ,ψ)` and character-compatible embeddings | D3 |
```

---

## Not patched, and why

- `claims/CLAIMS.md` — proposed rows are in `./CLAIMS-ROWS.md`; they enter only
  after the L6 loop, per the file's own header.
- `briefs/wh-kappa-target.md` — two of its statements are sharpened by this
  lane (the ambiguous "group preserving `ω`"; the count "`q+1` Schrödinger
  models", which counts polarizations, there being `q(q+1)` models). Both are
  recorded inside the shard and in the claim rows rather than by editing a work
  order that has already been executed against.
- `refs/LEDGER.md` — no new source was fetched by this lane, and no ledger entry
  needed correction. Note **N3** was honoured by not using the facts it flags.
