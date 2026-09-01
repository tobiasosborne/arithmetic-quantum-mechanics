# String-anchored trunk patch proposed by the FCR-2 prove lane

These are proposals only; this lane makes no trunk edit.  The `PROVED` cells
are candidate post-loop registers and must not be applied until the capped
hostile review/adjudication permits them.  Every quantifier needed by a row is
inside that row.

## 1. `definitions.md`

Anchor: insert the following block immediately after the final paragraph of
`## D16 (Weyl algebra, Heisenberg group, and local Schrödinger models)`, whose
last sentence is:

> Every formula in D16 is uniform in the residue characteristic and uses no
> half.

```markdown
## D17 (quadratic datum of a local polarizing cocycle)

For D12--D16 and `β in Adm(ω)`, put
`Q_β(v):=β(v,v)` and put
`P_β(v,w):=Q_β(v+w)-Q_β(v)-Q_β(w)`.
When `2 in 𝔪`, reduction gives a map
`Q̄_β:V(κ)->κ`; define its *residue type* by
`Arf(Q̄_β):=Q̄_β(e)Q̄_β(f) in κ/℘(κ)`, computed in a symplectic
`κ`-basis, where `℘(x)=x^2+x`.  Well-definedness, the identity
`P_β=2β-ω`, and basis independence of the residue type are claims
`FCR2-Q` and `FCR2-CLASS`, not stipulations.

## D18 (Gauss sum of a local polarizing cocycle)

For every finite local ring datum D12, every `ψ in Gen(R)`, and every
`β in Adm(ω)`, define
`ε_ψ(β):=|R|^{-1} sum_{v in V(R)} ψ(Q_β(v)) in C`.
Also put `T(R):={x in R:x^2=0}` and
`C_ψ(R):=sum_{a,b in T(R)}ψ(ab)`.
No root-of-unity, reality, character-independence, or class-invariance property
is part of this definition; those are claim `FCR2-EPS`.

## D19 (three equivalence levels for the beta datum)

For `β,β' in Adm(ω)` distinguish:
(i) *abstract group equivalence*, an arbitrary group isomorphism
`H_β(R) ~= H_β'(R)`;
(ii) *centre-fixed equivalence*, such an isomorphism whose restriction to
`R x 0` is `(t,0)|->(t,0)`;
(iii) *identity-labelled frame equivalence*, a complex-algebra isomorphism
`A_{ψ,β}->A_{ψ,β'}` of the form
`W_β(v)|->μ(v)W_β'(v)` for a function `μ:V(R)->C^x`.
No implication between these levels is stipulated.

## D20 (additive exponent and phase level)

For a finite local ring `R`, let `N_R` be the exponent of its additive group,
the least positive `N` with `NR=0`, and write `mu_N` for the complex `N`-th
roots of unity.  An identity-labelled frame equivalence has *phase level
`μ_d`* when its multiplier takes values in `μ_d`.

## D21 (finite chain ring and its length)

A finite local ring datum D12 is a *finite chain ring* when its ideals are
totally ordered by inclusion.  Its *length* is the least positive integer
`ell` with `𝔪^ell=0`; thus a field has length one.
```

## 2. `notation.md`

Anchor: replace the existing row

> | `Q_β` | `Q_β(v) = β(v,v)` | D6 |

where the vertical bars are the Markdown table delimiters, by these rows:

```markdown
| `Q_β`, `P_β`, `Q̄_β` | `β(v,v)`; its polarization; its residue reduction over a dyadic local ring | D6, D17 |
```

Anchor: replace the existing row

> | `℘`, `Arf` | `℘(x) = x²+x`; the type `Q_β(e)Q_β(f) ∈ κ/℘(κ)` | D10 |

by:

```markdown
| `℘`, `Arf(Q̄_β)` | `℘(x)=x²+x`; the residue type in `κ/℘(κ)` | D10, D17 |
```

Anchor: replace the existing row beginning ``| `ε` |`` by:

```markdown
| `ε`, `ε_ψ(β)` | the field Arf sign; the local normalized Gauss sum `|R|^{-1}sum_v ψ(Q_β(v))` | D10, D18 |
```

Anchor: insert immediately after the row beginning ``| `μ_p`, `μ_4`,
`U(1)` |``:

```markdown
| `N_R`, `μ_N` | additive exponent of `R`; complex `N`-th roots of unity | D20 |
```

Anchor: insert immediately after the row beginning ``| `H_β(κ)`,
`H_β(R)` |``:

```markdown
| `~_abs`, `~_Z`, `~_F` | abstract-group, centre-fixed, and identity-labelled-frame equivalence | D19 |
```

Anchor: insert immediately after the row beginning ``| `I_ψ`, `Gen(R)` |``:

```markdown
| `T(R)`, `C_ψ(R)` | `{x:x²=0}`; `sum_{a,b in T(R)}ψ(ab)` | D18 |
```

Anchor: insert immediately after the row beginning ``| `R`, `𝔪`, `R^×` |``:

```markdown
| `ell` | length (nilpotency index of `𝔪`) of a finite chain ring | D21 |
```

## 3. `claims/CLAIMS.md`

Anchor: insert these rows immediately after the existing `FCR-REG` row and
before the end of the `## Rows` table:

```markdown
| `FCR2-NOANTI` | For every finite commutative local `R` with `2 in m`, `Adm(omega)` is a `Sym_R(V(R))`-torsor of size `|R|^3` and has no antisymmetric member | PROVED | D12, D14, D15 | `theory/fcr2-beta.md` §1 | `theory/checks/fcr2_beta_check.py` (G7) |
| `FCR2-Q` | For every finite commutative local `R`, every `beta in Adm(omega)`, all `v,w in V(R)`, and every `g in SL_2(R)`, `P_beta(v,w)=2beta(v,w)-omega(v,w)`, `Q_{beta+s}=Q_beta+s(v,v)` for symmetric `s`, `(t,v)^2=(2t+Q_beta(v),2v)`, `W_beta(v)^2=psi(Q_beta(v))W_beta(2v)`, and `Q_{beta^g}=Q_beta o g`; no field simplification is ambient | PROVED | D12--D17 | `theory/fcr2-beta.md` §2 | `theory/checks/fcr2_beta_check.py` (G1,G2) |
| `FCR2-ALG0` | For every finite commutative local `R` in every residue characteristic and every `psi in Gen(R)`, `A_{psi,beta_0}` is simple with centre `C.1`, has dimension `|R|^2`, and the fixed model identifies it noncanonically with `M_|R|(C)`; `H_{beta_0}(R)` has exactly one irreducible unitary representation with central character `psi`, of dimension `|R|`, unitary intertwiners are unique up to `U(1)`, and every complex algebra automorphism is inner | PROVED | D12--D16, FCR-GEN, FCR-RAD, FCR-COMM | `theory/fcr2-beta.md` §3 | `theory/checks/fcr2_beta_check.py` (G6) |
| `FCR2-CLASS` | For every finite commutative local `R` with `2 in m`, equal values of `Arf(bar Q_beta)` give explicit centre-fixing isomorphisms `H_beta(R)~=H_beta'(R)`, and its hyperbolic and anisotropic fibres have sizes `|R|^3(q+1)/(2q)` and `|R|^3(q-1)/(2q)`; for `F_2,F_4,Z/4,F_2[e]/e^2,Z/8,F_2[t]/t^3,GR(4,2),F_2[x,y]/(x,y)^2` these fibres are exactly the two centre-fixed and exactly the two abstract group classes, separated by the displayed element-order profiles; no general abstract converse beyond those seeds is claimed | PROVED | D12, D14--D17, FCR2-NOANTI, FCR2-Q | `theory/fcr2-beta.md` §4 | `theory/checks/fcr2_beta_check.py` (G3,G5; targets only) |
| `FCR2-EPS` | For every finite commutative local `R` with `2 in m`, every `psi in Gen(R)`, and every `beta in Adm(omega)`, `epsilon_psi(beta) in {+1,-1} subset mu_8`, is independent of `psi`, and is constant on the two residue-type fibres; it is `+1` on the hyperbolic fibre and on the anisotropic fibre is `+1` iff `C_psi(R)=|R|`, `-1` iff `C_psi(R)=|m|`; hence it separates exactly in the latter case, and for a finite chain ring of length `ell` this is exactly `ell` odd (so all even lengths are a proved non-separation family) | PROVED | D12--D18, D21, FCR-GEN, FCR2-CLASS | `theory/fcr2-beta.md` §5 | `theory/checks/fcr2_beta_check.py` (G4,G5) |
| `FCR2-LEVEL` | For every finite commutative local `R` with `2 in m`, every `psi in Gen(R)`, and all `beta,beta' in Adm(omega)`, an identity-labelled frame equivalence exists with phase level `mu_{2N_R}`; for any cyclic decomposition `V=directsum <b_i>` with `ord(b_i)=n_i`, it exists at level `mu_{N_R}` iff every `psi(-binom(n_i,2)(beta'-beta)(b_i,b_i))` has an `n_i`-th root in `mu_{N_R}`; at a characteristic-two field this is exactly the `mu_2` iff `psi o Q_beta=psi o Q_beta'`, `mu_4` always statement | PROVED | D16, D19, D20 | `theory/fcr2-beta.md` §6 | (none; field regression: `theory/checks/wh_kappa/frame_mu.py`) |
| `FCR2-REG` | For every finite field `R=kappa` of characteristic two, `FCR2-NOANTI`, `FCR2-Q`, and `FCR2-ALG0` recover the named PROVED clauses of `WH-BETA-a,c,d`, `WH-ALG`, `WH-ALG-MAT`, and `WH-SVN` on the nose; `FCR2-CLASS`, `FCR2-EPS`, and `FCR2-LEVEL` agree clause-by-clause with the current SKETCH rows `WH-BETA-TYPE`, `WH-BETA-EPS`, and `WH-BETA-LEVEL`, which is consistency and not evidence from those rows | PROVED | FCR2-NOANTI, FCR2-Q, FCR2-ALG0, FCR2-CLASS, FCR2-EPS, FCR2-LEVEL | `theory/fcr2-beta.md` §7 | `theory/checks/fcr2_beta_check.py` (G5) |
```

## 4. Owning labbook lockstep

`CLAUDE.md` L11 requires the orchestrator, when applying the definition and
claim rows, to update the owning labbook section in the same commit.  This
lane is forbidden to edit trunk and therefore does not propose a line-numbered
labbook patch.
