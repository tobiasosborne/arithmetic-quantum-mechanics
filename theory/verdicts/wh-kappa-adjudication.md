<!-- ROLE: the orchestrator's ruling closing the capped L6 loop on the
     Spec-kappa increment. Under PRD.md the repair wave is NOT re-reviewed; it
     is verified mechanically here, and this file records what was verified,
     how, and what the labels were set to. -->

# Adjudication — `wh-kappa`, round 1

Loop: prove (`wh-prove`) -> attack (`wh-kappa-r1.md`, FAIL(OBJ-1,2,3)) ->
repair (`wh-repair`) -> this ruling. **Hard stop.** The FATAL-on-a-headline
exception was available and is deliberately NOT spent: OBJ-1 was fully
diagnosed, and its repair is structural rather than exploratory.

Prover, critic and repair lanes were the same model family. Blind lanes were
enforced (the critic never saw the prover's reasoning; the falsifier was written
from the work order before either). This is a known weakness of the setup and is
recorded on every verdict.

## What the orchestrator recomputed independently

Not "reviewed" — recomputed, by routes chosen to differ from the lanes'.

| # | claim | route | result |
|---|---|---|---|
| R1 | the `q²` Weyl operators are independent | specialise `ζ_p` into `F_ℓ`, where rank can only drop | rank `= q²` at `q = 2,3,5,4,9,8`. Confirms C5 |
| R2 | the operator ordering | direct exact construction of both naive models | `Z(b)X(a)` gives `−ab'`, `X(a)Z(b)` gives `ba'`; neither is `ab'` at odd `p`. **Produced erratum E1** |
| R3 | `\|O(Q_{β₀}) ∩ SL₂\| = 2(q−1)` at `p = 2` | direct enumeration of `SL₂(κ)` | `2, 6, 14` at `q = 2,4,8`. MATCH. Formula fails at odd `p`, where the value is `q−1` — outside the claim's scope, so not a defect, but it shows the `p=2` restriction is load-bearing |
| R4 | OBJ-1: the Heisenberg group depends on `β` | enumerate every admissible `β' = β + s`, identify the group of order `pq²` by its involution count | `p=2, q=2`: **6 give `D₄`, 2 give `Q₈`** — non-isomorphic. `p=3`: all 27 one class. `p=5`: all 125 one class. **FATAL confirmed** |
| R5 | the Arf classification of the repair wave | enumerate `Q_β` and count `\|Q_β^{-1}(0)\|` | exactly two classes at `q = 2,4,8`; `\|Q_β^{-1}(0)\| = 2q−1` (isotropic) or `1` (anisotropic), i.e. `2q−2` and `0` nonzero zeros. Class sizes match the `SL₂`-orbits `q(q±1)/2` once the `q`-to-1 multiplicity of `β ↦ Q_β` is divided out — alternating shifts do not move `Q`. Stabilisers `2(q∓1)`, and the isotropic value reproduces R3 |
| R6 | the repaired falsifier | run at the trunk path, green and every advertised red mode | green exit 0; **nine** red modes all exit 1; new gates C10 and C11 reached by `--red-beta-rigid` and `--red-naive-order`. C7's dead `ψ`-isotropy branch now fires in both directions |

Three independent computations agree on the characteristic-2 dichotomy: the
critic's phase-subgroup orders (6-of-8 giving `2(q−1)`, 2 giving `6 = |SL₂(F₂)|`),
its `|Out(D₄)| = 2` / `|Out(Q₈)| = 6` cross-check, and R4's direct group
identification. The two anisotropic cocycles are exactly the `Q₈` ones, and at
`q = 2` they are the single case where `O(Q_β) ∩ SL₂` is not proper.

## Ruling on the objections

- **OBJ-1 (FATAL) — sustained, and promoted.** The work order required only
  `β − β^T = ω`, which leaves a `q³`-torsor of choices; the campaign's own
  convention hid one. The repair does the right thing: `β` becomes a datum in
  D2 on the same footing as `ψ`, and the dependence becomes a theorem with an
  intrinsic separator (the Arf invariant of `Q_β`), not a table of counts. Per
  `PRD.md` this is a *positive* structural statement about the definition, and
  it is the increment's most valuable output.
- **OBJ-2 (MAJOR) — sustained.** "Sections exist" is false and is now `REFUTED`
  in its own row, with the Frobenius obstruction and the true section set in its
  place. A refutation carrying the surviving statement is a result (L10).
- **OBJ-3 (MAJOR) — sustained.** `κ`-linearity is imposed data the algebra does
  not carry; the intrinsic group is the larger `Sp_{2m}(F_p)`. Now its own
  theorem rather than a buried hypothesis.

## Ruling on the labels

The rule applied, stated so later rounds can be held to it:

> A repaired row may keep `PROVED` only if its new statement is one the round-1
> critic actually recomputed and left standing, or is precisely the surviving
> weaker statement that critic itself supplied under objection clause (d).
> Material written **in the repair wave** has had no hostile round and is
> `SKETCH`, however complete its proof looks — the gate to `PROVED` is
> procedural, and completeness of an argument is exactly what a hostile round
> exists to doubt.

Applied: **28 rows — 22 PROVED, 4 SKETCH, 1 CONJECTURE, 1 REFUTED.**

One move needed separate scrutiny and is allowed: `WH-COMM`, `WH-ALG` and
`WH-ALG-MAT` had their quantifier *widened*, from the reference cocycle to every
`β ∈ Adm(ω)`. Widening after review is normally illegitimate. It is sound here
because the proofs never used more than `β − β^T = ω`: the commutator
`W(v)W(v')W(v)^{-1}W(v')^{-1} = ψ(β(v,v') − β(v',v)) = ψ(ω(v,v'))` depends on
`β` only through `ω`, and simplicity depends only on `ω` being nondegenerate.
The statement was narrower than the argument, not the other way round.

## Residual items — follow-ups, not rounds

1. The four `SKETCH` rows are `SKETCH` for a procedural reason only. If a later
   session wants them at `PROVED`, that is one hostile round on the choice
   shard, not new mathematics.
2. `theory/wh-kappa-choice.md` is 503 lines against L2's 500. Trim at next edit.
3. The `RED-MATRIX` decoration inventory still names sub-checks no mutation
   reaches. Closing them is checker work, not claim work.
4. `WH-WEIL-e` stays `CONJECTURE` with the verified finite instances `q = 2, 4`
   recorded inside the statement.
