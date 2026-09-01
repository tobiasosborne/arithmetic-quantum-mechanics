<!-- ROLE: the orchestrator's ruling closing the capped L6 loop on the FCR-1
     increment. Under PRD.md the repair wave is NOT re-reviewed; it is verified
     mechanically here, and this file records what was verified, how, and what
     the labels were set to. -->

# Adjudication — `fcr-local`, round 1

Loop: prove (`fcr1/prove`) -> attack (`fcr-local-r1.md`, FAIL(OBJ-1)) ->
repair (`fcr1/repair`) -> this ruling. **Hard stop.** No FATAL was raised;
the extra-round exception does not arise.

Models: prover, critic, and repair lanes all `gpt-5.6-sol`, reasoning
`xhigh`, via `codex exec` (L7 as amended 2026-09-01); orchestrator Claude
(Fable) on the main thread. Blind lanes were enforced: the critic read the
artifact, trunk single sources, brief, sources, and checker — never the
prover's summary or reasoning; the pre-registered falsifier was written from
the brief before either shard existed. Same-family prover/critic is a known
weakness and is recorded here as on the verdict.

## What the orchestrator verified mechanically

By routes chosen to differ from the lanes' where feasible.

| # | item | route | result |
|---|---|---|---|
| R1 | the repaired falsifier | independent runs at the lane path and the trunk path | green exit 0; all NINE red modes exit 1, each at its registered gate; the two new modes (`--red-g6-arena-confusion`, `--red-profile-drop-identity`) reach the previously decorative G6 and G11 |
| R2 | the E1 model product law `Z(−b)X(a)Z(−b')X(a') = ψ(ab')Z(−b−b')X(a+a')` | symbolic hand recomputation of the exponents | exact cancellation; matches gate G4's exhaustive verification at all seven seeds |
| R3 | `L-ANN` double-annihilator duality | full ideal lattices of `Z/9` and `F_3[t]/(t³)` by hand (the critic used character-sum censuses — a different route) | `\|I\|\|Ann(I)\|=\|R\|` and `Ann(Ann(I))=I` at every ideal |
| R4 | OBJ-1's counterexample | read trunk `WH-CHOICE` directly | the trunk row's frame-preserving torsor has order `q²·\|SL₂(κ)\| = 216` at `q=3`; the bare-algebra torsor of `FCR-CHOICE` §8 is the infinite `PGL_{\|R\|}(C)`. Distinct statements; OBJ-1 sustained |
| R5 | the non-free Lagrangian `(3)⊕(3) ⊂ (Z/9)²` | direct residue computation | `ω`-values land in `9R = 0`; `Q_{β₀}` vanishes on it; the coset-freeness of `A` over `A_L` is structural (Weyl basis splits over `V/L`) |
| R6 | repaired §9 against the repaired `FCR-REG` row | clause-by-clause textual comparison in both directions | the row asserts exactly the clauses §9's two tables recover, and names the same exclusions (frame-preserving torsor; `WH-FORM`'s cocycle and automorphism-group clauses) |
| R7 | OBJ-2's inserted substep | read `FCR-GEN <1>1.<2>3` | both inclusions `S(_RR) = Ann(𝔪)` proved as the critic's own fix sketch specified |
| R8 | OBJ-3/OBJ-4 | grep audit | all nine claim rows bind `R`, `ψ`, `β` explicitly; the `q = \|R\|` collision is gone from the checker documents (`q` is `\|κ\|` only) |
| R9 | lockstep (L11) | `scripts/check-labbook.sh` + `cd labbook && make` | all four gates pass; `main.pdf` rebuilt, 43 pages, `08_local_rings` included with claim-id provenance |

## Ruling on the objections

- **OBJ-1 (MAJOR) — sustained, repair accepted.** "Specialize exactly, claim
  by claim" was stronger than the comparison performed. The repaired §9 is a
  clause-level compatibility theorem: it lists exactly the recovered clauses
  and expressly excludes what was never compared. This is precisely the
  critic's surviving weaker statement, made explicit; the marginal
  `WH-CHOICE` clauses it also lists (named data, central-character
  separation, algebra isomorphism) were independently verified by the critic
  in VERIFIED CORRECT item 7 and re-checked here (R6).
- **OBJ-2 through OBJ-5 (MINOR) — sustained, repairs accepted** as specified:
  the socle-identification leaf (R7), the closed quantifiers and the `n=\|R\|`
  rename (R8), and the two new red modes (R1).

## Ruling on the labels

The rule of the wh-kappa adjudication applies unchanged: a repaired row keeps
`PROVED` only if its statement is one the round-1 critic recomputed and left
standing, or is precisely the surviving weaker statement the critic supplied.

- `FCR-GEN`, `FCR-RAD`, `FCR-COMM`, `FCR-ALG`, `FCR-SVN`, `FCR-POL`,
  `FCR-CHOICE`, `FCR-BETA-ODD` — **PROVED.** The critic's status-register
  check placed all eight in the register of the nearest trunk PROVED rows;
  its objections to them were hygiene (OBJ-2, OBJ-3), repaired without
  touching the mathematics inside the VERIFIED CORRECT fence.
- `FCR-REG` — **PROVED on the repaired clause-level statement** (OBJ-1's
  surviving weaker statement; R6). The original "exact claim-by-claim"
  wording is dead and does not appear in the trunk row.

## Residuals filed as future work, earning no rounds (PRD)

1. The ring-side **frame-preserving isomorphism torsor** (the `WH-CHOICE`
   clause excluded from FCR-REG): the odd-field order is `q²·\|SL₂(κ)\|`;
   the local-ring analogue is unstated. Natural home: the FCR-6 dynamics
   increment, which will need the frame automorphism group anyway.
2. The critic's observation that `FCR-ALG`'s simplicity/centre/dimension
   leaves are parity-free (`2∈R^×` enters only via the β-transport to the
   reference matrix model): a scope split would strengthen the row. Do it
   when FCR-2 (residue characteristic 2) needs it, not before.
3. `WH-SYMM`'s ring analogue (what `Aut_F` is over `R`) — deferred with the
   symmetry increment, as the brief scoped.

## The increment's headline, for the record

The finite-field data `(κ, ψ, β)` generalize to a finite commutative local
ring as `(R, ψ ∈ Gen(R), β ∈ Adm(ω))`, with existence of `ψ` an honest
hypothesis: `Gen(R) ≠ ∅` iff `soc(R)` is one-dimensional over `κ` (Frobenius),
and `Gen(R)` is then a free transitive `R^×`-set — the exact generalization of
"`X(κ)` is a `κ^×`-torsor". For arbitrary `ψ` the phase radical is
`I_ψ ⊕ I_ψ`, so quantization degrades in a classified way rather than
failing silently (the FCR-3 obstruction increment starts from this). At odd
residue characteristic the whole field package survives: central simplicity,
`M_{\|R\|}(C)`, Stone–von Neumann, β-immateriality. New genuine phenomenon:
non-free Lagrangians (`soc(R)⊕𝔪` for every non-field `R`), enlarging the
Schrödinger-model catalogue beyond the free one.
