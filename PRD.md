<!-- ROLE: process constitution. Read after CLAUDE.md, before doing anything.
     Where this conflicts with older habits recorded in HANDOFF.md, in v0.1/,
     or in any worklog, THIS FILE WINS. Amended only by TJO. -->

# PRD — what this campaign is and how it runs

## Product

One result and one artifact.

- **The result (north star):** a general definition and workflow that assigns
  to an arbitrary arithmetic scheme one or more **canonical quantum systems** —
  kinematics (a Hilbert space), observables (an algebra), and where possible
  dynamics (automorphisms, or more generally projective unitary representations
  of symmetry groups), with fusion-categorical targets as the expected general
  endpoint. *Canonical* is not a mood: it means the assignment is stated as a
  functor, every choice it depends on is named, and a theorem says what is
  independent of those choices.
- **The concrete guiding path:** the characteristic-`p` prime field `F_p`, its
  canonical symplectic space `F_p x F_p`, and the finite Weyl–Heisenberg system
  quantizing it. Every general definition must reproduce this case on the nose,
  and is tested against it before anything else.
- **The artifact:** `labbook/main.pdf` — the complete human-readable LaTeX
  record: every definition restated in full, every result under a descriptive
  English name, honest status, provenance, and figures. It builds with
  `pdflatex` and it is never allowed to go stale (L11).

A paper is deferred. TJO decides when the definition has earned one; until
then the labbook is the deliverable.

A session that moves neither the definition nor the labbook is a failed
session, however many critic rounds it ran. Process output — verdicts, lane
logs, audit hygiene — is cost, never product.

## The two goals

1. **Rapid progress.** This is *rk-light*: an exploration campaign, not a
   formalisation campaign. If a task needs the full machinery — unbounded
   review loops, mutation-proving, meta-audits, machine-checked proof — it is
   an escalation, decided explicitly, not the default.
2. **Never admit a false result.** No statement ever carries a status stronger
   than its evidence. This is the only non-negotiable.

Every process rule in this repo must serve one of these two goals. A rule
serving neither is deleted, not obeyed.

## How goal 2 is met WITHOUT killing goal 1

**Soundness lives in the status labels, not in polish.** A claim sitting at
SKETCH or CONJECTURE forever harms no one. The only fatal sin is a wrong
label — PROVED on a false or unproved statement, or a refutation silently
ignored. Therefore:

- **Status discipline (L5).** Every claim in `claims/CLAIMS.md` carries a
  status in {PROVED, SKETCH, CONJECTURE, REFUTED}. Promotion to PROVED only
  through the capped loop below. When in doubt, the label goes DOWN.
- **The gate to PROVED** is a Lamport structured proof (L6b) that survived the
  capped hostile loop with no open FATAL/MAJOR on the promoted statement. A
  conditional PROVED must display its condition in the statement itself.
- **Falsifiers are early warning, binding in the negative.** Almost everything
  on the guiding path is a *finite* object — a finite field, a finite group, a
  finite-dimensional algebra — so an exact falsifier is unusually cheap and
  unusually sharp here. Pre-register one before the proof lands whenever the
  claim admits a computation. Passing proves nothing and promotes nothing. A
  falsifier that DISAGREES blocks promotion unconditionally, even against a
  passed proof: the statement and the probe disagree about what is being
  claimed, and that is resolved before any label moves.
- **Exactness over floating point.** On this campaign a numerical check that
  needs a tolerance is a design smell. Prefer exact integer/root-of-unity
  arithmetic; where floats are unavoidable, declare tolerance, norm, and an
  independent invariant.
- **Ground truth (L3).** Quotes from local sources under `refs/`, never from
  memory — standard mathematics included. Red-green TDD (L1) for every checker.
- **Capped hostile review (L6).** Below.

What goal 2 does NOT require: review-to-fixed-point, audits of audits,
re-review of repairs. A hostile critic always finds something; "iterate until
zero findings" never terminates.

## The capped L6 loop

Per artifact: **prove → attack → repair. Hard stop.**

- One prover pass, one hostile critic round, one repair wave.
- After the repair, the **orchestrator verifies fixes mechanically** against the
  critic's file:line claims (recomputation, checkers, falsifier) and
  adjudicates. Repairs are NOT re-reviewed by a fresh hostile pass.
- Residual objections become the claim's honest scope conditions or filed
  follow-ups. They do not extend the loop.
- **Sole exception:** an open FATAL touching a headline claim buys exactly one
  more round. "Headline" = a claim the north-star definition depends on.
- If the loop ends with unresolved MAJORs, the claim stays at SKETCH with the
  objections recorded next to it. That is a legitimate terminal state — goal 2
  is satisfied by the label, not by more rounds.
- **Rigor follows the claim's role, not the reviewer's appetite.** Headline
  claims get the full loop; supporting lemmas, conventions and checkers get one
  pass and a plain fix.

## Admitting v0.1 content (campaign-specific, L12)

`v0.1/` is a deprecated snapshot of the previous lab book, kept read-only.

**Nothing enters the trunk by copying.** A v0.1 shard is a *hint* — a pointer
to a question worth re-asking and sometimes to a source worth re-fetching. It
is never evidence, never a citation, and never a reason to skip a step. To
admit a v0.1 result: restate it against the current single sources, re-derive
it, re-register its source in `refs/LEDGER.md`, give it a checker where it
admits one, and run the L6 loop. It enters `claims/CLAIMS.md` at whatever
status that produces, frequently lower than v0.1 asserted.

Reason, on the record: v0.1's own internal review found P0-level sign,
polarization and definition defects in shards whose prose read as settled.
Its provenance discipline was real but its claims were never adversarially
recomputed. Treat every inherited statement as unreviewed.

## Negative results earn no rounds

Obstructions, no-go statements, non-canonicity certificates: these are not
progress. They are useful ONLY if they name a new strategy.

- A negative result that names a viable forward attack → the attack is
  value-gated like any lane; the negative note is recorded once and gets NO
  critic round, NO repair, NO promotion machinery.
- A negative result with no forward strategy → STOP the line and trigger a
  total re-evaluation with TJO. A beautifully verified obstruction is still an
  obstruction.
- The verification machinery exists to protect POSITIVE statements the
  definition will make. It is never spent on negative side-results.

Caveat specific to this campaign: a *sharp non-canonicity result* — "this
assignment depends on exactly this choice, and here is the groupoid it lives
in" — is a POSITIVE structural statement about the definition, not a negative
result. It gets the full loop.

## Budget and lane discipline

- **Value gate before any lane launches:** "if this converges, does the
  north-star definition or the labbook change?" No → file it, do not launch.
- **Session budget, declared at session start:** ~50% the single highest-value
  open piece of the definition, ~30% checkers, worked examples and the
  labbook, <=20% repairs and hygiene.
- **Lane isolation is mechanical, not conventional.** A parallel lane writes
  ONLY inside `theory/lanes/<campaign>/<lane>/`. A lane needing a trunk edit
  copies the file, edits the copy, and emits `PATCH.md` with **string anchors,
  never line numbers** — lines drift under concurrent edits. The orchestrator
  applies patches; lanes never commit.
- Critics may not expand scope into meta (auditing prior verdicts, process
  archaeology) unless a headline claim depends on it.

## Model policy (this environment)

- **Opus subagents for cognition-heavy work:** definitions, proofs, adversarial
  critique, adjudication.
- **Sonnet subagents for mechanical work:** checkers to spec, search, source
  fetching, labbook typesetting, catalogue and index upkeep.
- **No cross-family prover/critic split is available here.** Compensate with
  **blind lanes**: prover and critic never share a context; the critic reads
  only the artifact and the single sources, never the prover's reasoning; and
  the critic must recompute rather than referee. Every verdict records this
  limitation explicitly.
- **Lean 4 escalation** is available (`v0.1/.claude/tools/lean4`) if a claim
  ever needs machine-checked status. It is not required for PROVED.

## One record

Each event is narrated once, in its home: verdict → `theory/verdicts/`;
live state → `HANDOFF.md`; commit message <= 10 lines; user report short,
results first, process only where it changed a decision.

## Hygiene is plumbing, not progress

Gap inventories, stale pointers, checker plumbing, index upkeep: all vital,
all done promptly, and **never sold as significant**. One line or nothing.
Progress is a status change on a claim the definition rests on, a worked
example, a figure, or a labbook section — nothing else gets the word.

## Definition of a good session

At session end, both answers must be honestly yes:

1. Did the definition or the labbook move — a status changed, an example
   worked, a section written — or was an explicit recorded decision made that
   it should not?
2. Is every status label in `CLAIMS.md` still no stronger than its evidence?

Everything else — rounds survived, objections closed, lanes launched — is not
progress and is not reported as such.
