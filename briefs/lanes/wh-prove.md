LANE: wh-prove | WRITE SCOPE: theory/lanes/wh-kappa/prove/ ONLY
Read briefs/lanes/RULES.md, CLAUDE.md, PRD.md, then briefs/wh-kappa-target.md.

TASK: produce the Lamport-structured proof shard for the first increment, plus
the definition and notation entries it needs, as a patch proposal.

Deliverables, all inside your lane dir:

1. `wh-kappa.md` — the shard (L6b). Numbered steps `<1>1`, `<1>2`, sub-proofs
   `<2>*`, explicit ASSUME/PROVE on every nontrivial step, terminal QED steps.
   Every leaf justified by a D-number, a registered source in `refs/LEDGER.md`
   with its location, or a named computation. Target 200-500 lines (L2).
2. `PATCH.md` — the proposed additions to `definitions.md` and `notation.md`,
   keyed by string anchors (never line numbers). The four conventions of the
   target brief become D-numbered definitions; every symbol you use becomes a
   notation row.
3. `CLAIMS-ROWS.md` — the rows you propose for `claims/CLAIMS.md`, each with the
   status YOU think the evidence supports, and one sentence per row saying why
   not higher.
4. `SUMMARY.md` per RULES.md.

The hard parts, which are the reason this lane is Opus and not mechanical:

- **Characteristic 2 is in scope and is not a footnote.** Every statement is
  either uniform in `p` or explicitly scoped. `ω(v,v) = 0` must be *proved*
  where it is used, not inferred from antisymmetry. The non-symmetrized cocycle
  `β((a,b),(a',b')) = a b'` is mandatory precisely because `ω/2` is meaningless
  at `p = 2`; if any step needs `1/2`, that step is scoped to odd `p` and says
  so in the statement.
- **Canonicity is the product.** For each construction, state exactly which
  choices it depends on and prove the independence you claim. Where a
  construction depends on a choice, say what structure the family of choices
  carries (a torsor, a `P¹(κ)` of polarizations) and what the transition maps
  are. "Canonical" without a named category, named morphisms, and a checked
  naturality square is not a result — write it as a definition plus a
  conjecture instead.
- **The functoriality question is open and you should treat it as open.** The
  target brief does not claim functoriality in `κ`; do not smuggle it in. If
  you find the natural candidate map and it fails, that failure — stated
  sharply, with the surviving weaker statement — is a better deliverable than
  a vague success.
- **L3 binds you absolutely.** Stone-von Neumann, central simplicity of twisted
  group algebras, the Weil representation: cite `refs/LEDGER.md` entries with
  the theorem or page you actually read in the local file. If a needed source
  is recorded as a GAP there, you may still give the argument, but the step is
  marked ADMITTED and the affected claim row's proposed status drops to SKETCH.
  Asserting a textbook theorem from memory is the one unrecoverable error in
  this lane.

Do not write the checker; an independent lane writes it from the brief so that
it is independent evidence. Do not edit anything outside your lane dir.
