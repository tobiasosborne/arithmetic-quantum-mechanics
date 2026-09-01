<!-- ROLE: the single source for numbered definitions (L4). Every definition
     lives here exactly once, as a "## Dn (short name)" heading. Theory shards,
     checkers and the labbook cite Dn and never redefine.
     A definition is a STIPULATION and needs no source. The moment it asserts a
     property (nondegeneracy, uniqueness, a dimension), that property is a CLAIM
     and belongs in claims/CLAIMS.md with evidence. -->

# Definitions

## Conventions governing this file

1. One numbered definition per heading, `## Dn (short descriptive name)`.
2. Numbers are never reused and never renumbered. A superseded definition is
   marked superseded in place, with a pointer to its replacement.
3. Every definition must be stated **uniformly in the characteristic** or must
   say explicitly which characteristics it excludes and why. Silently
   odd-characteristic conventions are the campaign's designated foot-gun: the
   symmetrized "half" convention `ω/2` does not exist at `p = 2`.
4. Every choice a definition depends on — a character, a root of unity, a
   polarization, an ordering, a basis — is named in the definition itself, not
   in a remark. The product word of this campaign is *canonical*; an unnamed
   choice makes it a lie.
5. Any commit changing this file updates the owning labbook section in the same
   commit (L11).

## D1 (the symplectic object of a finite field)

For a finite field `κ`, put `V(κ) := κ ⊕ κ` and define `ω : V(κ)×V(κ) → κ` by
`ω((a,b),(a',b')) := a b' − a' b`.
Stipulation only; that `ω` is `κ`-bilinear, satisfies `ω(v,v) = 0` and is
nondegenerate is claim `WH-FORM`. Uniform in the characteristic; `p = 2` is in
scope.

## D2 (admissible polarizing cocycles, and the choice of one)

`Adm(ω) := { β : V(κ)×V(κ) → κ  |  β is κ-bilinear and β − β^T = ω }`.
A *polarizing cocycle* is a choice of element `β ∈ Adm(ω)`, and it is a **datum
of the construction, on the same footing as the character `ψ` of D3** — not a
convention. `β₀((a,b),(a',b')) := a b'` is the *reference* cocycle: a label for
the torsor of D2, not a canonical point of it.
The symmetrized alternative `ω/2` lies in `Adm(ω)` at odd `p` only, and is
unavailable at `p = 2`; that `Adm(ω)` is a torsor of size `q³`, that `ω/2` is
its unique antisymmetric point at odd `p`, and that at `p = 2` it splits into
two isomorphism types are claims `WH-BETA-a`, `-b`, `-c`.

## D3 (the phase datum, and the two choices it hides)

A *phase datum* for `κ` is an additive character `ψ : (κ,+) → C^×` with `ψ ≢ 1`.
Write `X(κ)` for the set of such `ψ`.
The *trace-normalized family*: `Tr_{κ/F_p}(z) := z + z^p + ⋯ + z^{p^{m−1}}` for
`κ = F_{p^m}`, and `ψ_ζ := ζ^{Tr_{κ/F_p}(·)}` for `ζ` a primitive `p`-th root of
unity in `C`.
**Two named choices:** `ψ` itself, and — inside the distinguished family — `ζ`.
Neither is canonical and neither is ever suppressed. `Tr_{κ/F_p}` is canonical.

## D4 (Weyl operators and the observable algebra)

For `ψ` as in D3 and `β ∈ Adm(ω)` as in D2,
`A_{ψ,β}(V) := ⨁_{v ∈ V(κ)} C·W_β(v)` with product fixed on basis elements by
`W_β(v)W_β(v') := ψ(β(v,v')) W_β(v+v')`.
This ordering is fixed once. Depends on `κ`, `ψ` and `β`, and on nothing else.

## D5 (the Heisenberg group of a polarizing cocycle)

`H_β(κ) := κ × V(κ)` with `(t,v)(t',v') := (t + t' + β(v,v'), v + v')`.
It uses no character; it does depend on `β`, and at `p = 2` its isomorphism
class does (claim `WH-BETA-f`). `A_{ψ,β}(V)` is its group algebra with the
centre set to `ψ`.

## D6 (the quadratic form of a polarizing cocycle)

`Q_β : V(κ) → κ`, `Q_β(v) := β(v,v)`; for the reference cocycle,
`Q_{β₀}(a,b) = ab`.
Identically zero under any symmetrized convention, and not zero here; at `p = 2`
it is the object that separates the members of `Adm(ω)`.

## D7 (the Weyl frame and two automorphism groups)

The *Weyl frame* is `F := { C^×·W_β(v) : v ∈ V(κ) } ⊂ A_{ψ,β}(V)`.
`Aut_F(A)` is the group of `C`-algebra automorphisms `α` with `α(F) = F`.
`Aut_F^κ(A) ⊆ Aut_F(A)` is the subgroup whose induced permutation of `V(κ)` is
`κ`-linear. The `κ`-linearity is **imposed data**: the algebra and its frame are
built from `(V,+)` and `ψ∘β` alone and do not carry the `κ`-module structure
(claim `WH-SYMM`).

## D8 (Schrödinger models, and the standard model)

For a `κ`-line `L ⊂ V(κ)` put `A_L := span_C{ W_β(l) : l ∈ L }`. Given a unital
`C`-algebra character `χ : A_L → C`, the *Schrödinger model* of `(L,χ)` is
`M_{L,χ} := A_{ψ,β}(V) ⊗_{A_L} C_χ`.
The *standard model* (for `β = β₀`) is `M₀ := ⨁_{y ∈ κ} C·e_y` with `{e_y}`
declared orthonormal and

    W(a,b) e_y := ψ(−b(y+a)) e_{y+a},   i.e.   W(a,b) = Z(−b)X(a),

where `X(a)e_y := e_{y+a}` and `Z(b)e_y := ψ(by)e_y`. **This is a stipulation.**
The sign is not cosmetic: the naive `Z(b)X(a)` realizes the cocycle `−ab'`, and
the discrepancy is invisible at `p = 2`. That `M₀` satisfies D4 is checked by
gate `C11` of `theory/checks/wh_kappa_check.py` and derived at `WH-SVN`.

## D9 (the model groupoid)

`Mod_{ψ,β}(κ)` is the category whose objects are pairs `(M,π)` with
`π : A_{ψ,β}(V) → End_C(M)` a unital algebra map making `M` a simple module and
every `π(W_β(v))` unitary, and whose morphisms are unitary intertwiners.
`PMod_{ψ,β}(κ)` is the same category with `Hom` replaced by `Hom/U(1)`.

## D10 (Artin–Schreier map, and the type of a polarizing cocycle)

`℘ : κ → κ`, `℘(x) := x² + x`. **[p = 2]** the *type* of `β ∈ Adm(ω)` is
`Arf(Q_β) := Q_β(e)·Q_β(f) ∈ κ/℘(κ)` computed in any symplectic `κ`-basis
`(e,f)` of `V(κ)` (`ω(e,f) = 1`). That this is independent of the basis, that
`κ/℘(κ)` has exactly two elements, and that both types occur are claims
`WH-BETA-e`, `-f`.

## D11 (the level-`μ_p` frame)

`F^{(p)}_{ψ,β} := { ζ^j W_β(v) : j ∈ Z/p, v ∈ V(κ) } ⊂ A_{ψ,β}(V)^×`, the finite
group of Weyl unitaries with phases in `μ_p = ψ(κ)`.
Recorded separately from `F` (D7) because the two behave differently: claim
`WH-BETA-h` says `(A,F)` does not depend on `β` while `F^{(p)}` does, at `p = 2`.

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
