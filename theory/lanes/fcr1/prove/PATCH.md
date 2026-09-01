# Proposed trunk patch for FCR-1

These are proposals only.  Apply them to trunk after the capped review loop.
Every edit uses an exact string anchor from the current trunk; no line number is
an edit anchor.

## `definitions.md`

**INSERT AFTER the exact existing paragraph:**

> Recorded separately from `F` (D7) because the two behave differently: claim
> `WH-BETA-h` says `(A,F)` does not depend on `β` while `F^{(p)}` does, at `p = 2`.

**INSERT:**

```markdown
## D12 (finite commutative local ring datum)

A *finite local ring datum* is `(R,𝔪,κ,q)` with `R` a finite commutative
unital local ring with `1≠0`, `𝔪` its unique maximal ideal, `κ:=R/𝔪`, and
`q:=|κ|`; write `R^×` for its unit group.
For an ideal `I⊆R`, put `Ann(I):={r∈R:rI=0}` and
`soc(R):=Ann(𝔪)`.  These are stipulations.  Nilpotence of `𝔪`, nonvanishing of
the socle, and the other finite-local structure properties are established in
`FCR-GEN`, not assumed here.  Uniform in the residue characteristic.

## D13 (characters and generating characters of a finite local ring)

Let `R̂:=Hom((R,+),C^×)` and `X(R):=R̂∖{1}`.  For `ψ∈X(R)` and `u∈R`, put
`ψ_u(x):=ψ(ux)`.  Define
`I_ψ:=Σ{I⊆R : I is an ideal and I⊆ker ψ}`, the largest ideal contained in
`ker ψ`, and `Gen(R):={ψ∈X(R):I_ψ=0}`.  A member of `Gen(R)` is a
*generating character*.  Uniform in the residue characteristic; existence is
not stipulated and is claim `FCR-GEN`.

## D14 (the symplectic object and phase perpendicularity over a local ring)

For D12 put `V(R):=R⊕R` and
`ω((a,b),(a',b')):=ab'−a'b`.  Given `ψ∈X(R)`, write
`B_ψ(v,w):=ψ(ω(v,w))` and, for an `R`-submodule `L⊆V(R)`,
`L^{⊥_ψ}:={v∈V(R):B_ψ(v,l)=1 for every l∈L}`.  A *Lagrangian* is an
`R`-submodule with `L=L^{⊥_ψ}`; put `rad(B_ψ):=V(R)^{⊥_ψ}`.  R-bilinearity,
strong alternation,
R-nondegeneracy of `ω`, and nondegeneracy of `B_ψ` are claims, not
stipulations; `B_ψ`, not R-nondegeneracy alone, is the load-bearing pairing.
Uniform in the residue characteristic.

## D15 (admissible polarizing cocycles over a local ring)

For D14,
`Adm(ω):={β:V(R)×V(R)→R | β is R-bilinear and β−β^T=ω}`.
Put `Sym_R(V(R)):= {s:V(R)×V(R)→R | s is R-bilinear and s=s^T}`.
A *polarizing cocycle* is a named choice `β∈Adm(ω)`.  The reference member is
`β₀((a,b),(a',b')):=ab'`.  This is the non-symmetrized convention: no inverse
of `2` is assumed.  Uniform in the residue characteristic.

## D16 (Weyl algebra, Heisenberg group, and local Schrödinger models)

For D12--D15 define
`A_{ψ,β}(V(R)):=⨁_{v∈V(R)}C·W_β(v)` by
`W_β(v)W_β(v'):=ψ(β(v,v'))W_β(v+v')`, and define
`H_β(R):=R×V(R)` by
`(t,v)(t',v'):=(t+t'+β(v,v'),v+v')`.
For an `R`-submodule `L` put
`A_L:=span_C{W_β(l):l∈L}`; given a unital algebra character
`χ:A_L→C`, put `M_{L,χ}:=A_{ψ,β}(V(R))⊗_{A_L}C_χ`.

The fixed reference model is `ℓ²(R)=⨁_{y∈R}C·e_y`, with `{e_y}` declared
orthonormal,
`X(a)e_y:=e_{y+a}`, `Z(b)e_y:=ψ(by)e_y`, and, exactly,

    W_{β₀}(a,b):=Z(−b)X(a),
    W_{β₀}(a,b)e_y=ψ(−b(y+a))e_{y+a}.

The sign and ordering are stipulations inherited from D8's E1 resolution.
Every formula in D16 is uniform in the residue characteristic and uses no
half.
```

## `notation.md`

**REPLACE the exact existing row:**

```markdown
| `κ`, `F_p` | the finite field `F_q`; its prime field | D1 |
```

**WITH:**

```markdown
| `κ`, `F_p` | the finite field `F_q` and its prime field; for D12, `κ=R/𝔪` is the residue field | D1, D12 |
```

**INSERT AFTER that replacement:**

```markdown
| `R`, `𝔪`, `R^×` | a finite commutative local ring; its maximal ideal; its unit group | D12 |
| `soc(R)`, `Ann(I)` | `Ann(𝔪)`; the annihilator of an ideal `I` | D12 |
```

**REPLACE the exact existing row:**

```markdown
| `V(κ)` | `κ ⊕ κ`, the symplectic object | D1 |
```

**WITH:**

```markdown
| `V(κ)`, `V(R)` | `κ⊕κ`; `R⊕R`, the field and local-ring symplectic objects | D1, D14 |
```

**REPLACE the exact existing row:**

```markdown
| `v = (a,b)` | a vector of `V(κ)` | D1 |
```

**WITH:**

```markdown
| `v = (a,b)` | a vector of the current `V(κ)` or `V(R)` | D1, D14 |
```

**REPLACE the exact existing row:**

```markdown
| `ω` | `ω((a,b),(a',b')) = ab' − a'b` | D1 |
```

**WITH:**

```markdown
| `ω` | `ω((a,b),(a',b'))=ab'−a'b` over the current `κ` or `R` | D1, D14 |
```

**INSERT AFTER that replacement:**

```markdown
| `B_ψ`, `rad(B_ψ)`, `L^{⊥_ψ}` | `ψ∘ω`; its radical; phase-perpendicular of an `R`-submodule | D14 |
| `L_*` | the non-free Lagrangian `soc(R)⊕𝔪` when `R` is not a field | FCR-POL |
```

**REPLACE the exact existing row:**

```markdown
| `Adm(ω)` | the admissible polarizing cocycles | D2 |
```

**WITH:**

```markdown
| `Adm(ω)` | the admissible polarizing cocycles over the current `κ` or `R` | D2, D15 |
```

**REPLACE the exact existing row:**

```markdown
| `Sym(V)` | the symmetric `κ`-bilinear forms on `V(κ)` | D2 |
```

**WITH:**

```markdown
| `Sym(V)`, `Sym_R(V(R))` | symmetric bilinear forms over `κ`; over `R` | D2, D15 |
```

**INSERT AFTER that replacement:**

```markdown
| `s`, `φ_s` | a symmetric form; `(t,v)↦(t+s(v,v)/2,v)` when `2∈R^×` | FCR-BETA-ODD |
```

**REPLACE the exact existing row:**

```markdown
| `β`, `β₀` | a chosen polarizing cocycle; the reference one `ab'` | D2 |
```

**WITH:**

```markdown
| `β`, `β₀` | a chosen polarizing cocycle; the reference one `ab'`, over the current base | D2, D15 |
```

**REPLACE the exact existing row:**

```markdown
| `ψ` | a nontrivial additive character of `(κ,+)` | D3 |
```

**WITH:**

```markdown
| `ψ` | a nontrivial additive character of the current `(κ,+)` or `(R,+)` | D3, D13 |
```

**INSERT AFTER the exact existing row:**

```markdown
| `X(κ)` | the set of nontrivial additive characters | D3 |
```

**INSERT:**

```markdown
| `R̂`, `X(R)`, `ψ_u` | all additive characters of `R`; the nontrivial ones; `ψ(u·)` | D13 |
| `I_ψ`, `Gen(R)` | largest ideal in `ker ψ`; the generating characters | D13 |
```

**REPLACE the exact existing row:**

```markdown
| `W_β(v)` | Weyl operator / basis element of `A_{ψ,β}(V)` | D4 |
```

**WITH:**

```markdown
| `W_β(v)` | Weyl operator / basis element of `A_{ψ,β}(V)` over the current base | D4, D16 |
```

**REPLACE the exact existing row:**

```markdown
| `A_{ψ,β}(V)` | the twisted algebra `⨁_v C·W_β(v)` | D4 |
```

**WITH:**

```markdown
| `A_{ψ,β}(V)` | the twisted Weyl algebra over the current base | D4, D16 |
```

**REPLACE the exact existing row:**

```markdown
| `H_β(κ)` | the Heisenberg group `κ × V(κ)` of `β` | D5 |
```

**WITH:**

```markdown
| `H_β(κ)`, `H_β(R)` | the Heisenberg groups `κ×V(κ)` and `R×V(R)` | D5, D16 |
```

**REPLACE the exact existing row:**

```markdown
| `L`, `A_L` | a `κ`-line in `V(κ)`; its subalgebra | D8 |
```

**WITH:**

```markdown
| `L`, `A_L` | a field line or local-ring submodule; its Weyl subalgebra | D8, D14, D16 |
```

**REPLACE the exact existing row:**

```markdown
| `χ`, `C_χ` | a character of `A_L`; its 1-dimensional module | D8 |
```

**WITH:**

```markdown
| `χ`, `C_χ` | a character of `A_L`; its 1-dimensional module | D8, D16 |
```

**REPLACE the exact existing row:**

```markdown
| `M_{L,χ}`, `M₀` | Schrödinger model of `(L,χ)`; the standard model | D8 |
```

**WITH:**

```markdown
| `M_{L,χ}`, `M₀` | Schrödinger model of `(L,χ)`; the field standard model | D8, D16 |
```

**REPLACE the exact existing row:**

```markdown
| `e_y`, `X(a)`, `Z(b)` | standard basis; shift and phase operators | D8 |
```

**WITH:**

```markdown
| `ℓ²(R)`, `e_y`, `X(a)`, `Z(b)` | local reference space; standard basis; shift and phase operators | D8, D16 |
```

**REPLACE the exact existing row:**

```markdown
| `E` | the Weyl average `q^{-2} Σ_u W(u)(·)W(u)^{-1}` | D4 |
```

**WITH:**

```markdown
| `E` | the Weyl average `\|V\|^{-1}Σ_uW(u)(·)W(u)^{-1}` over the current base | D4, FCR-ALG |
```

## `claims/CLAIMS.md`

**INSERT AFTER the exact existing row:**

```markdown
| `WH-FUNCT-d` | Over the inclusion poset of the subfields of a fixed `\bar F_p`, the compatible systems `(ψ_κ)` are **exactly** the restrictions of the additive characters `Ψ` of `(\bar F_p,+)` with `Ψ\|_{F_p} ≠ 1` | PROVED | D3 | `theory/wh-kappa-choice.md` §10 `<1>4` | `theory/checks/funct_sections.py` (F4) |
```

Use the same backticks and Markdown escaping conventions as the surrounding
table when applying the following nine rows:

```markdown
| `FCR-GEN` | For a finite commutative local `R`, `Gen(R)≠∅` iff `soc(R)` is one-dimensional over `κ`; when nonempty, for any `ψ∈Gen(R)`, `ψ_u` is generating iff `u∈R^×`, and `Gen(R)` is a free `R^×`-orbit; at `R=κ` this is the `q−1` character clause of `WH-CHOICE` | PROVED | D12, D13 | `theory/fcr-local.md` §1 | `theory/checks/fcr_local_check.py` (G1,G8) |
| `FCR-RAD` | The form `ω` is `R`-bilinear, strongly alternating, and `R`-nondegenerate; for any nontrivial `ψ∈X(R)`, `rad(ψ∘ω)=I_ψ⊕I_ψ`, so `ψ∘ω` is nondegenerate iff `ψ∈Gen(R)` | PROVED | D12--D14, FCR-GEN | `theory/fcr-local.md` §2 | `theory/checks/fcr_local_check.py` (G2,G3) |
| `FCR-COMM` | For every `β∈Adm(ω)`, `W_β(v)W_β(v')=ψ(ω(v,v'))W_β(v')W_β(v)`, uniformly in the residue characteristic | PROVED | D14--D16 | `theory/fcr-local.md` §3 | `theory/checks/fcr_local_check.py` (G2,G4) |
| `FCR-ALG` | If `2∈R^×`, `ψ∈Gen(R)`, and `β∈Adm(ω)`, then `A_{ψ,β}(V(R))` is simple with centre `C·1`, has complex dimension `\|R\|²`, and is non-canonically isomorphic to `M_{\|R\|}(C)` | PROVED | FCR-RAD, FCR-COMM, FCR-BETA-ODD | `theory/fcr-local.md` §5 | `theory/checks/fcr_local_check.py` (G5,G6) |
| `FCR-SVN` | If `2∈R^×` and `ψ∈Gen(R)`, `H_β(R)` has one irreducible unitary representation with central character `ψ` up to unitary equivalence, of dimension `\|R\|`; intertwiners are unique up to `U(1)`, and every complex algebra automorphism of `A_{ψ,β}` is inner | PROVED | FCR-ALG | `theory/fcr-local.md` §6 | `theory/checks/fcr_local_check.py` (G4,G5) |
| `FCR-POL` | If `2∈R^×` and `ψ∈Gen(R)`, every self-perpendicular `R`-submodule `L⊆V(R)` has `\|L\|=\|R\|`; the coordinate axes are such submodules; if `R` is not a field then `soc(R)⊕𝔪` is a non-free example, and all induced Schrödinger models are isomorphic as `A_{ψ,β}`-modules | PROVED | FCR-GEN, FCR-RAD, FCR-ALG, FCR-SVN | `theory/fcr-local.md` §7 | `theory/checks/fcr_local_check.py` (G7) |
| `FCR-CHOICE` | If `2∈R^×` and `Gen(R)≠∅`, beyond `R` the presentation has exactly the data `ψ∈Gen(R)` and `β∈Adm(ω)`; distinct `ψ` give inequivalent representations of the same `H_β(R)`, while the bare algebras are isomorphic and their isomorphism torsor has no automorphism-invariant point | PROVED | FCR-GEN, FCR-ALG, FCR-SVN, FCR-BETA-ODD | `theory/fcr-local.md` §8 | `theory/checks/fcr_local_check.py` (G8,G9) |
| `FCR-BETA-ODD` | If `2∈R^×`, `Adm(ω)` is a torsor of size `\|R\|³` under `Sym_R(V(R))`, `ω/2` is its unique antisymmetric member, and `φ_s(t,v)=(t+s(v,v)/2,v)` is a centre-fixing isomorphism `H_β(R)→H_{β+s}(R)` for every symmetric `s` | PROVED | D14--D16 | `theory/fcr-local.md` §4 | `theory/checks/fcr_local_check.py` (G9) |
| `FCR-REG` | For `R=κ` a finite field of odd characteristic, D12--D16 and FCR-GEN through FCR-BETA-ODD specialize exactly, claim by claim, to the field definitions and the `WH-*` rows tabulated in the proof | PROVED | FCR-GEN, FCR-RAD, FCR-COMM, FCR-ALG, FCR-SVN, FCR-POL, FCR-CHOICE, FCR-BETA-ODD | `theory/fcr-local.md` §9 | `theory/checks/fcr_local_check.py` (G10) |
```
