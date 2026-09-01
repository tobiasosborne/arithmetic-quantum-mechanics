Lane model: gpt-5.6-sol, reasoning xhigh, codex exec.

# FCR-1 prove-lane summary

| id | reached register | one-line reason |
|---|---|---|
| `FCR-GEN` | PROVED | Wood's character criterion plus a derived one-summand local Frobenius criterion gives `Gen(R)≠∅ ⇔ dim_κsoc(R)=1`, and the unit torsor follows. |
| `FCR-RAD` | PROVED | Direct computation proves the three R-valued form properties, then coordinate tests identify the phase radical as `I_ψ⊕I_ψ`. |
| `FCR-COMM` | PROVED | The ratio of the two Weyl products is `ψ(β−β^T)=ψ∘ω`, with no parity step. |
| `FCR-ALG` | PROVED | Character averaging proves central simplicity; the fixed `Z(−b)X(a)` model and odd-`2` transport give `M_{\|R\|}(C)`. |
| `FCR-SVN` | PROVED | The matrix algebra has one simple module; unitarity, phase uniqueness, and innerness are derived directly. |
| `FCR-POL` | PROVED | Character orthogonality gives `\|L\|\|L^⊥\|=\|R\|²`; double annihilators give all `I⊕Ann(I)` witnesses. |
| `FCR-CHOICE` | PROVED | The definitions name only `(ψ,β)`; central characters separate models and algebra isomorphisms form a nontrivial torsor. |
| `FCR-BETA-ODD` | PROVED | The symmetric-form torsor and `s(v,v)/2` coboundary argument port verbatim over any ring with `2∈R^×`. |
| `FCR-REG` | PROVED | A statement-level table checks D12--D16 and every FCR row against its odd-field `WH-*` counterpart. |

Sharpest result: for every non-field ring in scope, not only the two length-2
seeds, `soc(R)⊕𝔪` is a self-perpendicular non-free submodule; hence the
Schrödinger catalogue is strictly larger than the free one.

Weakest step to scrutinize: `FCR-CHOICE` gives “no distinguished
isomorphism” the precise bare-algebra meaning “no automorphism-invariant point
of the isomorphism torsor.”  It does not claim an impossibility theorem against
formulas using extra coordinates or a future naturality condition.

Open questions for the critic:

1. Does the explicit reduction of Wood's principal-decomposition definition
   to `R/𝔪≅soc(R)` fully satisfy the requested “derive, do not read in” gate?
2. Should `FCR-ALG` and `FCR-SVN` retain the displayed `2∈R^×` proof scope, or
   should the checker/source path promote their stronger parity-free versions?
3. Is the field regression mapping `FCR-RAD` to the radical leaf supporting
   `WH-FORM`/`WH-ALG` sufficiently “on the nose” despite no trunk `WH-RAD` row?
