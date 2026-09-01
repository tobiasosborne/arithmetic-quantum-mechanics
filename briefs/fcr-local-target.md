<!-- ROLE: campaign work order, written before the work (PRD lane discipline).
     Target: the second increment of the north-star definition.
     Author: orchestrator, from TJO's direction of 2026-09-01. -->

# Target: the canonical quantum system of a finite local ring, odd residue characteristic

## Why this next

The reboot workflow is: incrementally re-incorporate v0.1 material with the
benefit of hindsight and rk-light rigour, adding structure gradually. The first
increment closed `Spec κ` with data `(κ, ψ, β)`. This increment adds exactly one
structure: drop "field", keep "finite, commutative, local" — deliberately
**without any Spec or scheme language**. The question is how to quantize a
finite commutative ring using only the finite-field story as guide.

The campaign order behind this brief (each its own increment, each gated):

1. **FCR-1 (this brief):** local rings, odd residue characteristic.
2. **FCR-2:** residue characteristic 2 (`Z/4`, `F_2[t]/(t^k)`, Galois rings) —
   the β-classification, expected to generalize the Arf story.
3. **FCR-3:** the non-Frobenius obstruction as a sharp non-canonicity theorem.
4. **FCR-4:** direct sums (the canonical local decomposition) and the order-4
   battery adjudicating competing definitions.

Rationale for "local first, then direct sums": a finite commutative ring is
canonically a finite product of local rings (primitive idempotents are unique),
so the local case is the only hard part — *provided* the decomposition step is
later proved choice-free (FCR-4, where `s(e_i v, e_j w) = e_i e_j s(v,w) = 0`
is the expected key lemma).

v0.1 hints (L12: hints only, nothing enters by copying): the thickened
Artin–Weyl layer (`v0.1` shards AQM-36/AQM-37, top-coefficient generating
characters for `F_3[ε]/(ε²)` and the `tⁿ = 1` family), and the open v0.1
question `aqm-qsa-collapse01` ("quotient collapse"), which FCR-3 is expected to
answer structurally.

## The pipeline this campaign follows (P1) — recorded, not canonized

TJO's preferred philosophy, recorded 2026-09-01. It is **one** philosophy,
adopted per-increment on merit, never blindly:

1. From the underlying object (here: a finite commutative ring), build a
   **symplectic object**. Classify the additional data this requires.
2. From the symplectic object, build a **Weyl–Heisenberg group-like object**
   (group here; groupoid in later generality). Classify the additional data
   this requires (cocycle/phase data).
3. **Classify the projective unitary representations** of the WH object. That
   classification *is* the quantization.

Competing definitions arising from other philosophies are kept alongside and
adjudicated on cleanliness and on **which physics they capture**. The intended
relaxation — WH group → fusion-categorical object, projective unitary reps →
module categories — is the PRD's declared endpoint and is *kept in view*;
nothing in this increment claims anything about it, but a claim whose statement
would obstruct that relaxation should say so in prose.

**Named branch point at step 1** (both P1-compliant, recorded now so the fork
is visible before either is worked):

- **Route A (this increment's primary):** the self-dual R-linear phase space
  `V(R) = R ⊕ R` with the R-valued form `ω((a,b),(a',b')) = ab' − a'b`,
  composed with an additive character `ψ`. Nondegeneracy of `ψ∘ω` is NOT free;
  classifying when it holds is claim `FCR-RAD`.
- **Route B (named competitor, deferred to FCR-4):** the Pontryagin phase space
  `V = R ⊕ R̂` with its canonical `U(1)`-valued pairing — no `ψ` at all,
  nondegenerate for *every* finite ring; the multiplication of `R` enters only
  through which symmetry group is imposed. Not worked in this increment; it is
  the control definition the order-4 battery will compare against.

## Conventions to fix FIRST (L4)

D-numbered in `definitions.md` before any proof step uses them. They must be
stated **uniformly in the residue characteristic** even though this increment
only proves theorems at odd residue characteristic: FCR-2 inherits these
conventions, and a convention that silently assumes `2 ∈ R^×` is exactly the
class of defect erratum E1 of the previous brief exists to prevent.

1. **The finite local ring datum.** `(R, m, κ = R/m, q = |κ|)`, `R` finite
   commutative unital local; the socle `soc(R) = Ann(m)`; the structure facts
   used (nilpotency of `m`, `soc(R) ≠ 0`, minimal ideals lie in `soc(R)`,
   every non-unit is a zero divisor) each cited to a registered source or
   proved inline — not from memory (L3).
2. **Characters and generating characters.** `X(R)` = nontrivial characters of
   `(R,+)`; `ψ_u := ψ(u·)` for `u ∈ R`; `I_ψ` = the largest ideal of `R`
   contained in `ker ψ`; `Gen(R) = {ψ ∈ X(R) : I_ψ = 0}`. The Frobenius
   property enters through `Gen(R) ≠ ∅`, tied to `soc(R)` in `FCR-GEN`.
3. **The symplectic object.** `V(R) = R ⊕ R`,
   `ω((a,b),(a',b')) = ab' − a'b`. Record: R-bilinear; alternating in the
   strong sense `ω(v,v) = 0`; nondegenerate over R (`ω(v,·) = 0 ⇒ v = 0`) —
   and record explicitly that this R-nondegeneracy is NOT the load-bearing
   notion; nondegeneracy of `ψ∘ω` is, and it is a theorem (`FCR-RAD`), not a
   convention.
4. **The polarizing cocycle.** `Adm(ω)` = maps `β : V × V → R`, R-bilinear,
   with `β − β^T = ω`; reference cocycle `β₀((a,b),(a',b')) = ab'`. The
   non-symmetrized convention is mandatory (the symmetrized `ω/2` exists at
   odd residue characteristic and its canonicity there is claim
   `FCR-BETA-ODD`, but the *convention* must not presuppose it).
5. **Weyl operators and the model.** `W_β(v)W_β(v') = ψ(β(v,v'))W_β(v+v')`.
   The explicit Schrödinger model is fixed by the trunk's E1 resolution and
   the prover MUST use the same one, stated in full: on `ℓ²(R)` with basis
   `{e_y}`, `X(a)e_y = e_{y+a}`, `Z(b)e_y = ψ(by)e_y`, and
   **`W_{β₀}(a,b) = Z(−b)X(a)`** (`theory/wh-kappa.md` §5 `<1>2`, `<2>3`).
   Leaving the model implicit was the E1 defect; it is not repeated.

## Statements to establish

Proposed ids and expected registers. The expected register is a prior, not a
target: if the evidence lands lower, the label lands lower.

| id | statement | expected |
|---|---|---|
| `FCR-GEN` | `Gen(R) ≠ ∅` iff `soc(R)` is simple (one-dimensional over `κ`); when nonempty, `ψ_u` is generating iff `u ∈ R^×`, and `Gen(R)` is a free `R^×`-orbit — the exact generalization of "`X(κ)` is a `κ^×`-torsor". For `R = κ` a field this reduces to the trunk's `WH-CHOICE` character count | PROVED |
| `FCR-RAD` | for arbitrary nontrivial `ψ`, the radical of `ψ∘ω` on `V(R)` is `I_ψ ⊕ I_ψ`; hence `ψ∘ω` is nondegenerate iff `ψ ∈ Gen(R)`. (The non-Frobenius consequence — every `ψ` collapses `F_3[x,y]/(x,y)²` to a proper quotient — is *recorded as a computation at that seed*, not developed; the collapse theorem is FCR-3's) | PROVED |
| `FCR-COMM` | `W_β(v)W_β(v') = ψ(ω(v,v'))W_β(v')W_β(v)` for every `β ∈ Adm(ω)`, uniformly in the residue characteristic | PROVED |
| `FCR-ALG` | for `ψ ∈ Gen(R)`, `β ∈ Adm(ω)`: `A_{ψ,β}(V(R))` is simple with centre `C·1`, `dim_C = |R|²`, `≅ M_{|R|}(C)` by a non-canonical isomorphism | PROVED |
| `FCR-SVN` | `H_β(R)` has exactly one irreducible unitary representation with central character `ψ ∈ Gen(R)` up to unitary equivalence, of dimension `|R|`; intertwiners unique up to `U(1)`; algebra automorphisms inner | PROVED |
| `FCR-POL` | Lagrangian = self-perpendicular R-submodule w.r.t. `ψ∘ω`; every Lagrangian `L` has `|L| = |R|`; `L = R⊕0` and `0⊕R` are Lagrangian; for `R` local non-field, **non-free Lagrangians exist** (expected witness: `m^j ⊕ Ann(m^j)` for suitable `j`, e.g. `(3)⊕(3) ⊂ (Z/9)²`) — the Schrödinger-model catalogue is strictly larger than the free one, while all models remain isomorphic as `A_{ψ,β}`-modules by `FCR-SVN` | PROVED at the seeds; a general census may land SKETCH |
| `FCR-CHOICE` | beyond `R` the construction depends on exactly two data, `ψ ∈ Gen(R)` and `β ∈ Adm(ω)`; distinct `ψ` give representations of the same group with distinct central characters, hence inequivalent; the algebras are isomorphic with no distinguished isomorphism | PROVED |
| `FCR-BETA-ODD` | if `2 ∈ R^×`: `ω/2` is the unique antisymmetric member of `Adm(ω)`, and `φ_s(t,v) = (t + s(v,v)/2, v)` is an isomorphism `H_β(R) → H_{β+s}(R)` fixing the centre, for every symmetric `s` — the choice of `β` is immaterial exactly as in the odd-field case | PROVED |
| `FCR-REG` | with `R = κ` a finite field of odd characteristic, every definition and claim above restricts on the nose to its `WH-*` counterpart (statement-level check, not analogy) | PROVED |

**Priors worth recording:** `Adm(ω)` is a torsor under symmetric R-bilinear
forms of size `|R|³` (the field proof should port verbatim; if it does, say so
and re-prove, do not cite the field case as if it covered rings). Chain rings
(`Z/p^k`, `F_q[t]/(t^k)`, unramified/ramified extensions) are all Frobenius;
`F_3[x,y]/(x,y)²` is the designated non-Frobenius probe.

## Seeds

`R ∈ { F_3, F_9 (field regression); Z/9, F_3[ε]/(ε²) (length 2);
Z/27, F_3[t]/(t³) (length 3); F_3[x,y]/(x,y)² (non-Frobenius probe, order 27) }`.

`Z/9` vs `F_3[ε]/(ε²)` is the minimal mixed-vs-equal-characteristic pair: same
order, same length, same residue field — the definition must treat them
uniformly while the resulting quantum systems differ (clock–shift of order 9
vs two coupled qutrit-like factors; the *precise* statement of the difference
is FCR-4/physics material, but the checker records the element-order profiles
now).

## Explicitly NOT claimed in this increment

No residue characteristic 2 (no Arf, no Brown/Gauss-sum invariants — FCR-2).
No non-Frobenius quantization proposal (only the `FCR-RAD` iff and the recorded
seed computation — FCR-3). No direct sums or products, no idempotent
decomposition (FCR-4). No `SL_2(R)`/Weil/metaplectic action and no symmetry
claims (own later increment; note `WH-SYMM`'s lesson makes this subtle and it
is deliberately deferred). No Spec, scheme, or sheaf language. No functoriality
in `R`. No fusion categories. No route-B claims. None of these words appear in
a claim row produced by this increment.

## Pre-registered falsifier (written before the proof; L1, PRD)

`theory/checks/fcr_local_check.py`, plain `python3` + `numpy`, no repo
dependency. **Exact arithmetic only:** `Z[ζ_n]` as integer vectors modulo the
`n`-th cyclotomic polynomial, `n ∈ {3, 9, 27}` as the seed requires (characters
of `(Z/9,+)` are `μ_9`-valued; of `(F_3[ε],+)` are `μ_3`-valued). A tolerance
anywhere is a design failure. Rings are represented by explicit element tables
(order ≤ 27), not by symbolic shortcuts.

| gate | asserts |
|---|---|
| G1 | character census at every seed: `\|X(R)\| = \|R\| − 1`; `I_ψ` computed for every `ψ`; `Gen(R) = {ψ_u : u ∈ R^×}` exactly, and `\|Gen(R)\| = \|R^×\|`; `Gen(F_3[x,y]/(x,y)²) = ∅` **by exhaustion**, with the maximal-ideal kernel exhibited for every `ψ` |
| G2 | `ω` is alternating (`ω(v,v) = 0` checked, not inferred), R-bilinear, R-nondegenerate; `β₀ − β₀^T = ω` exhaustively |
| G3 | radical of `ψ∘ω` equals `I_ψ ⊕ I_ψ` for **every** nontrivial `ψ` at every seed (both directions of FCR-RAD, by exhaustion) |
| G4 | the Weyl relation of D-convention 5 holds exactly in the stated model `Z(−b)X(a)`, and the FCR-COMM commutation relation follows, at every Frobenius seed with a chosen `ψ ∈ Gen(R)` |
| G5 | the `\|R\|²` Weyl operators are linearly independent; commutant of `{W(v)}` is the scalars |
| G6 | with a **non**-generating `ψ` (at `Z/9`: `ψ` with `I_ψ = (3)`), the commutant is strictly larger than the scalars, with its dimension matching `\|I_ψ\|²` |
| G7 | Lagrangian census at `Z/9` and `F_3[ε]`: enumerate ALL self-perpendicular submodules of `V(R)`, verify `\|L\| = \|R\|` for each, count free vs non-free, and verify at least one non-free Lagrangian exists; cross-check `\|L\|·\|L^⊥\| = \|V\|` on every submodule |
| G8 | for `u ∈ R^×`, `ψ_u ∈ Gen(R)` and the reps for distinct `u` have distinct central characters; for `u ∈ m`, `ψ_u ∉ Gen(R)` |
| G9 | `2 ∈ R^×` at every seed; `ω/2 ∈ Adm(ω)` is antisymmetric and is the unique antisymmetric member (census over `Adm(ω)` at `F_3`, `Z/9`, `F_3[ε]`; at order-27 seeds the torsor has `27³` members — sample the coboundary identity `φ_s` exhaustively in `s` at order ≤ 9 and on ≥ 100 pseudorandom-but-seeded `s` at order 27) |
| G10 | field regression: at `R = F_3` every gate reproduces the corresponding `wh_kappa_check.py` expectation (same counts, same model matrices) |
| G11 | element-order profiles of `H_{β₀}(R)` recorded per seed (data for the physics comparison; asserts only internal consistency: profile sums to `\|R\|³`) |

**Red modes**, each exiting non-zero, each reported with the gate that kills it:

- `--red-nongenerating` — run the FCR-ALG pipeline with a `ψ` having
  `I_ψ ≠ 0`; G5 must fire (commutant grows).
- `--red-transpose` — replace `β₀` by `β₀^T` keeping the claimed identity;
  G2 must fire at odd seeds (and the mode must NOT be silently green anywhere).
- `--red-frobenius-blind` — treat `F_3[x,y]/(x,y)²` as if it had a generating
  character (take the `ψ` with smallest `I_ψ`); G1 or G3 must fire.
- `--red-free-only` — assert every Lagrangian is free; G7 must fire.
- `--red-torsor` — assert `ψ_u` generating for some `u ∈ m`; G8 must fire.
- `--red-dim` — assert `\|R\|² + 1` independent Weyl operators; G5 must fire.
- `--red-halfweyl-drop` — omit the `/2` in `φ_s` (use `s(v,v)` in place of
  `s(v,v)/2`); G9 must fire.

`RED-MATRIX.md` is mandatory: every gate either reached by at least one
mutation or named as decoration with the mutation that would reach it. A red
mode bit-identical in effect to another is a checker defect, not a pass.

## Deliverables

1. `definitions.md` — D-numbered entries for the five convention groups above.
2. `notation.md` — every new symbol, once (`soc`, `I_ψ`, `Gen(R)`, `V(R)`, …).
3. `theory/fcr-local.md` — the Lamport-structured shard (L6b), 200–500 lines.
4. `theory/checks/fcr_local_check.py` + `fcr_local_EXPECTATIONS.md` +
   `fcr_local_RED-MATRIX.md` — green, and every red mode non-zero.
5. `theory/verdicts/fcr-local-r1.md` — the hostile verdict.
6. `theory/verdicts/fcr-local-adjudication.md` — the ruling.
7. `claims/CLAIMS.md` — rows at whatever status the loop produces.
8. `labbook/sections/08_local_rings.tex` — the owning section, in lockstep
   (L11), including the P1 pipeline statement and the route-A/route-B fork.
9. `refs/LEDGER.md` — registered sources for: generating characters /
   Frobenius rings (Wood; Honold if obtainable), finite local ring structure
   facts. **No statement in the shard may cite memory for these.**

## Lanes and models (L7 as amended 2026-09-01)

- All cognition and verifier lanes run on `codex exec`, model `gpt-5.6-sol`,
  reasoning `xhigh`; the model is recorded on every verdict. No Claude
  subagents (TJO directive, 2026-09-01).
- **check lane** writes the falsifier from THIS brief only — never from the
  prover's shard.
- **prove lane** reads: this brief, `definitions.md`, `notation.md`,
  `claims/CLAIMS.md`, `theory/wh-kappa*.md` (trunk is fair game), and
  registered sources under `refs/`. It writes ONLY inside its lane directory
  and emits `PATCH.md` (string anchors, never line numbers) + `SUMMARY.md`.
- **critic lane** is blind: it reads the shard, the checker, the single
  sources, and `refs/` — never the prover's lane, never this conversation.
  Contract: `briefs/critic-protocol.md`. It recomputes; it does not referee.
- **orchestrator** (Claude, main thread) applies patches, independently
  recomputes by routes differing from the lanes', and adjudicates. Capped
  loop per PRD: prove → attack → repair → mechanical adjudication, hard stop.

## Order of work

1. Sources land in `refs/` + `LEDGER.md` before the prover cites them.
2. Check lane (from this brief) and source acquisition run in parallel.
3. Prove lane.
4. One hostile round, one repair wave, mechanical adjudication. Hard stop.
