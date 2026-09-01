<!-- ROLE: campaign work order, written before the work (PRD lane discipline).
     Target: FCR-2 — residue characteristic 2. Ordered by TJO 2026-09-01
     ("FCR2 sounds ok"). -->

# Target: the polarizing-cocycle classification at residue characteristic 2

## Why this next

FCR-1 closed the odd local case: the data are `(R, ψ ∈ Gen(R), β ∈ Adm(ω))`
and at odd residue characteristic the third datum is immaterial
(`FCR-BETA-ODD`). FCR-2 is the increment where the third datum becomes real:
for `2 ∈ 𝔪` the torsor `Adm(ω)` has no antisymmetric member and the trunk's
field-level guide (`WH-BETA-c,d`, `WH-BETA-TYPE`, `WH-BETA-EPS`) says the
Heisenberg group itself moves with `β` (at `F_2`: six cocycles give `D_4`,
two give `Q_8`, separated by `Arf(Q_β)`). The question is what that dichotomy
becomes over thickened rings — `Z/4` and `F_2[t]/(t^k)` first.

This is the definition's live open piece; PRD budgeting sends the session
here. FCR-3 (non-Frobenius collapse) and FCR-4 (direct sums, the order-4
battery) stay queued behind it.

## Conventions to fix FIRST (L4)

D-numbered before use; uniform statements, with parity hypotheses displayed
per claim as in FCR-1.

1. **The quadratic datum of a cocycle over a ring.** `Q_β : V(R) → R`,
   `Q_β(v) := β(v,v)`, with the *corrected polarization identity* recorded
   as part of the definition:
   `Q_β(v+w) − Q_β(v) − Q_β(w) = 2β(v,w) − ω(v,w)`,
   and the coboundary action `Q_{β+s}(v) = Q_β(v) + s(v,v)`. (Over a field
   of characteristic 2 the `2β` term dies and `Q_β` is an ω-quadratic form —
   D6/D10 territory; over `Z/4` it does not, and no claim may silently use
   the field identity.)
2. **The square law.** In `H_β(R)`: `(t,v)² = (2t + Q_β(v), 2v)` and
   `W_β(v)² = ψ(Q_β(v)) W_β(2v)`. The field simplification `2v = 0` is a
   per-claim hypothesis, never ambient.
3. **The Gauss sum of a cocycle.**
   `ε_ψ(β) := |R|^{-1} Σ_{v ∈ V(R)} ψ(Q_β(v)) ∈ C`,
   defined for every finite local `R` and `ψ ∈ Gen(R)`; its properties are
   claims, not stipulations.
4. **Isomorphism granularity.** Classification statements must name their
   equivalence: (i) abstract group isomorphism of `H_β(R)`; (ii) isomorphism
   fixing the centre pointwise; (iii) frame equivalence of `(A_{ψ,β}, F)` à
   la `WH-BETA-LEVEL`. The field story shows these can differ; conflating
   them was the class of defect OBJ-1 caught in FCR-1.

## Statements to establish (priors, not targets)

| id | statement (short) | expected |
|---|---|---|
| `FCR2-NOANTI` | `2 ∈ 𝔪` ⇒ `Adm(ω)` has no antisymmetric member; the `Sym_R(V)`-torsor structure of `FCR-BETA-ODD <1>1` is unchanged (it used no half) | PROVED |
| `FCR2-Q` | the convention-group computations: corrected polarization identity, square law, coboundary action, `SL_2`-type transport of `Q_β` | PROVED |
| `FCR2-ALG0` | for the reference `β₀` and every `ψ ∈ Gen(R)`, in EVERY residue characteristic: `A_{ψ,β₀}` simple, centre `C·1`, `dim |R|²`, `≅ M_{\|R\|}(C)` via the fixed model; SvN for `H_{β₀}` — discharges the FCR-1 parity residual | PROVED |
| `FCR2-LEVEL` | when a frame isomorphism `W_β(v) ↦ μ(v)W_{β'}(v)` exists over `R`, and with what phase level (ring analogue of `WH-BETA-LEVEL`) | SKETCH likely |
| `FCR2-CLASS` | the census classification of `{H_β : β ∈ Adm(ω)}` at the seeds under equivalences (i) and (ii) of convention 4, with a proposed separating invariant | census PROVED; general classification may land SKETCH |
| `FCR2-EPS` | `ε_ψ(β) ∈ μ_8`, constant on the appropriate equivalence classes, reducing at `R = κ`, `p = 2` to the `±1` of `WH-BETA-EPS` (the Arf sign as the mod-2 shadow of a Brown/Gauss–Milgram-type `Z/8` invariant) | CONJECTURE unless sources carry it further |
| `FCR2-REG` | clause-level compatibility with the trunk `p = 2` field rows at their CURRENT registers (`WH-BETA-c,d` PROVED; `WH-BETA-TYPE`, `WH-BETA-EPS`, `WH-BETA-LEVEL` are SKETCH — compatibility with a SKETCH row proves nothing and must be labelled as consistency, not evidence) | PROVED (clause-level, FCR-1 style) |

Open questions the census settles before any proof lands: how many
`H_β`-classes at `Z/4` (the field has two; more are possible), whether
`ε_ψ(β)` separates them, and whether element-order profiles suffice or finer
invariants are needed.

## Seeds

`F_2, F_4` (field regression against trunk rows and `beta_census.py`);
`Z/4, F_2[ε]/(ε²)` (minimal mixed/equal pair — the worked catalogue of the
smallest-rings report is the anchor); `Z/8, F_2[t]/(t³)` (length 3);
`GR(4,2) = Z/4[x]/(x²+x+1)` (order 16) if runtime permits;
`F_2[x,y]/(x,y)²` (non-Frobenius probe: `Gen = ∅`, census only).

## Explicitly NOT claimed

No odd-characteristic content beyond regression. No direct sums (FCR-4), no
non-Frobenius quantization (FCR-3), no Spec/scheme language (FCR-5/6), no
`SL_2(R)` Weil-representation claims (the field `p=2` Weil story `WH-WEIL-*`
is regression context only), no fusion categories, no metaplectic covers.

## Pre-registered falsifier (L1; written from this brief only)

`theory/checks/fcr2_beta_check.py`, python3 + numpy, exact arithmetic in
`Z[ζ_8]` (mod `x⁴+1`) for the `Z/4` family and `Z` for the `F_2` family.

Gates (sketch — the check lane fixes the final list from this brief):
polarization-identity and square-law censuses (G1–G2); full `|R|³`-orbit
census of `H_β` isomorphism types at every seed of order ≤ 8 under
equivalences (i) and (ii), by order profiles PLUS power-map/centre-quotient
invariants, with class sizes (G3); `ε_ψ(β)` computed exactly for every `β`,
its value set, and its constancy on the G3 classes (G4); field regression at
`F_2, F_4` against `beta_census.py` expectations: the `6:2` split, `Arf`
class sizes `q(q±1)/2`, `ε = ±1` (G5); `FCR2-ALG0` trace-Gram and model
gates at `Z/4, F_2[ε], Z/8, F_2[t]/(t³)` (G6); no-antisymmetric census (G7);
`Gen(F_2[x,y]/(x,y)²) = ∅` (G8). Red modes: ≥ 6, including a fake-`ε` value,
a collapsed-classes mutation, a transposed cocycle, a halfweyl mode (must
fail differently than at odd seeds), a wrong-profile fixture, and a
field-regression mutation. RED-MATRIX mandatory.

## Sources to acquire FIRST (L3 gate for `FCR2-EPS` and `FCR2-CLASS`)

The Gauss–Milgram/Brown layer: Wall, *Quadratic forms on finite groups*
(Topology 2, 1963); Brown (Ann. of Math. 95, 1972); and — the most likely
e-print routes — the finite-quadratic-module / discriminant-form literature
(Skoruppa and collaborators on Weil representations of finite quadratic
modules; lattice-theory surveys restating Gauss–Milgram) and the
Weil-representation-over-`Z/2^k` tradition (Kloosterman-era, Szechtman et
al.). The orchestrator hunts and registers in `refs/LEDGER.md` before the
prover cites anything; claims that outrun the registered sources stay
CONJECTURE.

## Lanes and order of work (L7 as amended)

All lanes `codex exec`, `gpt-5.6-sol`, `xhigh`; blind prover/critic; the
capped loop; verdict files record models. Order: (1) sources land; (2) check
lane writes the falsifier from this brief (parallel with source hunt);
(3) prove lane; (4) one hostile round, one repair wave, mechanical
adjudication, hard stop. The smallest-rings verifier lane's confirmed
catalogue is admissible as anchored data once its checker is in trunk.
