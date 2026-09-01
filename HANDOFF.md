<!-- ROLE: live state. UPDATE POLICY: every session end and every phase
     boundary. Not an authoritative source for mathematics — that is
     definitions.md, claims/CLAIMS.md, and theory/. -->

# HANDOFF — live state

Updated: 2026-09-01, session 2 (the FCR-1 session).

Read order gate: `CLAUDE.md` -> **`PRD.md` (the constitution; where it conflicts
with anything recorded here, PRD wins)** -> this file.

## Where the campaign is

Two increments closed. Session 1 (2026-08-31) rebooted the repository and
closed `Spec κ` for a finite field — see `theory/verdicts/wh-kappa-*`.
Session 2 (2026-09-01) closed **FCR-1: finite commutative local rings at odd
residue characteristic**, the first v0.1-material re-derivation increment.
The previous lab book stays frozen under `v0.1/` (hints only, L12).

Standing directives recorded this session (TJO):

- **P1 pipeline** (one philosophy, adopted per-increment on merit, never
  blindly): object → symplectic object (classify required data) →
  Weyl–Heisenberg group-like object (classify cocycle/phase data) → classify
  projective unitary representations = the quantization. Fusion-categorical
  relaxation is the declared endpoint, kept in view, claimed nowhere yet.
  Recorded in `briefs/fcr-local-target.md`.
- **Model policy (L7 amended):** cognition-heavy and verifier lanes run on
  `codex exec`, model `gpt-5.6-sol`, reasoning `xhigh`. No Claude subagents.
- **Spec framing (agreed):** Spec R geometrizes a finite ring only as a
  locally ringed space — points carry locality, stalks (full local rings,
  not residue fields) carry the local quantization; choosing Spec is
  choosing which automorphisms count as geometric, so the ring enters the
  physics through dynamics (WH-SYMM). Queued as FCR-5/FCR-6 in the brief.

## The FCR-1 increment, closed

One full capped loop: prove -> one hostile round (`fcr-local-r1.md`,
FAIL(OBJ-1): the regression claim overclaimed) -> one repair wave ->
mechanical adjudication (`theory/verdicts/fcr-local-adjudication.md`).

**The result.** `(κ, ψ, β)` generalizes to `(R, ψ ∈ Gen(R), β ∈ Adm(ω))`
with existence of `ψ` an honest hypothesis: `Gen(R) ≠ ∅` iff `soc(R)` is
one-dimensional over `κ` (Frobenius; Wood Thm 3.10 + a derived local socle
criterion), and `Gen(R)` is a free transitive `R^×`-set. For arbitrary
nontrivial `ψ` the phase radical is `I_ψ ⊕ I_ψ` — quantization degrades in a
classified way (the non-Frobenius probe `F_3[x,y]/(x,y)²` has `Gen = ∅` by
exhaustion). At odd residue characteristic the whole field package survives:
central simplicity, `M_{|R|}(C)`, Stone–von Neumann, β-immateriality via
`ω/2`. New phenomenon: **non-free Lagrangians** (`soc(R)⊕𝔪` for every
non-field `R`), strictly enlarging the Schrödinger-model catalogue. The
mixed-vs-equal-characteristic distinction is visible physics: gate G11's
element-order profiles separate `Z/9` (`{1,3,9}`-orders) from `F_3[ε]`
(exponent 3).

**State:** 37 claim rows — 31 PROVED, 4 SKETCH, 1 CONJECTURE, 1 REFUTED
(the nine new `FCR-*` rows all PROVED, `FCR-REG` on its repaired clause-level
statement). D1–D16 in `definitions.md`. Labbook 43 pages, lockstep gates
green, `main.pdf` rebuilt. Falsifier `theory/checks/fcr_local_check.py`:
green at 7 seeds, NINE red modes each dying at its registered gate.
Sources: Wood AJM 1999 (full text, MUSE) and a Stacks algebra snapshot
registered in `refs/LEDGER.md` with locators.

## Next useful steps

1. **FCR-2** (residue characteristic 2): `Z/4`, `F_2[t]/(t^k)`, Galois
   rings; the β-classification, expected to generalize Arf — prior:
   the `WH-BETA-EPS` Gauss sign should become an eighth root of unity
   (Brown/Gauss–Milgram); needs sources before claims.
2. **FCR-3** (non-Frobenius obstruction as sharp non-canonicity) and
   **FCR-4** (direct sums; cross-term-vanishing lemma; the order-4 battery
   `{F_4, Z/4, F_2[ε], F_2⊕F_2}` adjudicating route A vs route B).
3. **FCR-5/FCR-6** (Spec equivalence theorem; dynamics via Aut(R) on Spec)
   — queued in `briefs/fcr-local-target.md` §campaign order.
4. Filed residuals earning no rounds (see adjudication): ring-side
   frame-preserving torsor (goes with FCR-6); parity-free scope split of
   `FCR-ALG` (goes with FCR-2); `WH-SYMM` ring analogue (symmetry increment).
5. Old wh-kappa follow-ups unchanged: one hostile round on
   `theory/wh-kappa-choice.md` would settle its four SKETCH rows; it is 503
   lines against L2's cap; the wh-kappa RED-MATRIX still names unreached
   sub-checks.
6. `scripts/setup-env.sh` first in any new container (TeX, latexmk, numpy;
   no `bd`). Codex is available on this host (`codex exec`, config defaults
   to `gpt-5.6-sol` xhigh). Untracked pre-reboot leftovers `.beads/` and
   `runs/` still sit at top level — TJO to decide (move into `v0.1/` or
   delete).
