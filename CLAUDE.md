<!-- ROLE: how we work in this repo. UPDATE POLICY: amend on felt failure or
     TJO directive, dated. PRD.md governs where the two ever disagree. -->

# CLAUDE.md — arithmetic-quantum-mechanics

Campaign: build a general definition and workflow assigning **canonical quantum
systems to arbitrary arithmetic schemes** — Hilbert space, observable algebra,
and where possible dynamics as automorphisms or projective unitary
representations of symmetry groups, with fusion categories as the expected
general endpoint. The concrete guiding path is `F_p` and its canonical
symplectic space `F_p x F_p`. The product is `labbook/main.pdf`.

`v0.1/` is a deprecated snapshot of the previous lab book. It is a source of
hints, never of evidence (L12).

## Read order (gate)

1. This file.
2. `PRD.md` — the process constitution. It wins over habit, over `HANDOFF.md`,
   and over anything in `v0.1/`.
3. `HANDOFF.md` — current state, next steps.
4. `notation.md`, `definitions.md` — the single sources.
5. `claims/CLAIMS.md` — the argument DAG.

## Laws (rk-light)

- **L1 — Red-green.** Every checker ships a mutation mode (`--red`, or a named
  variant) that MUST exit non-zero. Write the failing check first and watch it
  fail. "Runs without errors" is never a test. A gate that cannot fail is
  decoration; a gate no mutation reaches is worse, because it reads as
  evidence.
- **L2 — Shards 200–500 lines.** One lemma-cluster per file under `theory/`,
  one topic per labbook section.
- **L3 — Ground truth is local.** Every mathematical statement traces to a
  source under `refs/` (with page/theorem/equation), to a derivation in
  `theory/`, or to a named checker. This applies to standard textbook material
  too: "everyone knows Stone–von Neumann" is not a citation. Sources are
  registered in `refs/LEDGER.md` with title verification and retrieval route.
- **L4 — Notation and definitions are deduped.** Every symbol lives once in
  `notation.md`, every definition once in `definitions.md` as a numbered `Dn`.
  Theory shards and the labbook reference them and never redefine.
- **L5 — Claims DAG.** `claims/CLAIMS.md` holds every claim: id, statement,
  status in {PROVED, SKETCH, CONJECTURE, REFUTED}, depends-on, proved-in,
  tested-in. Markdown only, no CI machinery. Status changes only per PRD L6.
- **L6 — Capped prove → attack → repair.** One prover pass, one hostile critic
  round, one repair wave, then the orchestrator verifies fixes mechanically and
  adjudicates. Full rules in `PRD.md`; the critic contract is
  `briefs/critic-protocol.md`.
- **L6b — Lamport structured proofs.** Every rigorous argument in `theory/` is
  hierarchical: numbered steps <1>1, <1>2, sub-proofs <2>1..., explicit
  ASSUME/PROVE for each nontrivial step, terminal QED steps, and every leaf
  justified by a definition number, a claim id, or a named computation. The
  labbook may linearize; the theory shard is ground truth and stays structured.
- **L7 — Model policy.** *(Amended 2026-09-01, TJO directive.)* Cognition-heavy
  work (definitions, proofs, critique, adjudication) and verifier work run on
  `codex exec` with `gpt-5.6-sol` at `xhigh` reasoning, used extensively; the
  cross-family gain from mixing models is judged marginal. Claude orchestrates
  and may do mechanical work (search, fetching, typesetting, index upkeep)
  directly or via Sonnet. Prover and critic still run as blind lanes and the
  model of every lane is recorded on every verdict. No model drafts labbook
  prose beyond the structure the WRITING-GUIDE fixes; final register is TJO's.
- **L8 — Cross-session state → `HANDOFF.md`.** Not scratch TODO lists, not
  chat memory. (`bd` is not installed in this environment; if it is ever
  added, it takes over tracking and `HANDOFF.md` keeps only insights.)
- **L9 — The labbook is the product.** `labbook/main.pdf` builds with
  `pdflatex`; every definition restated in full, every result under a
  descriptive English name, honest status, provenance. Style contract:
  `labbook/WRITING-GUIDE.md`.
- **L10 — Honest verdicts.** A sharp refutation carrying the surviving weaker
  statement beats a pile of analogies. Structural tensions are respected, not
  papered over. A claim that "the analogy is suggestive" is not a claim.
- **L11 — Labbook lockstep.** Any commit that changes `claims/CLAIMS.md` or
  `definitions.md`, or that lands a worked example or figure, MUST update the
  owning labbook section in the same commit. `scripts/check-labbook.sh` is the
  gate and it runs at session close together with a real `pdflatex` build.
- **L12 — v0.1 is a hint, never evidence.** Nothing enters the trunk by
  copying from `v0.1/`. Restate, re-derive, re-source, check, and run the loop;
  admit at whatever status that produces. See `PRD.md`.

## Layout

    PRD.md          process constitution (north star, loop, budgets)
    notation.md     symbol table (single source)
    definitions.md  numbered definitions D1, D2, ... (single source)
    claims/         CLAIMS.md — the argument DAG
    theory/         Lamport proof shards
      verdicts/     critic verdicts and adjudications, kept pass or fail
      checks/       standalone red/green checkers (python3 + numpy only)
      lanes/        write-isolated parallel lane directories
    briefs/         work orders, written before the work
    labbook/        main.tex + sections/*.tex — the product
    numerics/       heavier computations and frozen result records
    refs/           LEDGER.md + local source snapshots (bodies not committed)
    scripts/        gates: check-labbook.sh, session close
    docs/           background framing
    v0.1/           deprecated snapshot; hints only (L12)

## Session close

1. `scripts/check-labbook.sh` — lockstep gate.
2. `cd labbook && make` — the PDF must build.
3. Every checker green, and every `--red` mode non-zero.
4. `HANDOFF.md` updated.
5. Commit and push. Work is not complete until the push succeeds.
