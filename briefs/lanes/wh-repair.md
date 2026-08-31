LANE: wh-repair | WRITE SCOPE: theory/lanes/wh-kappa/repair/ ONLY
Read briefs/lanes/RULES.md, CLAUDE.md, PRD.md, briefs/wh-kappa-target.md WITH its
errata E1-E5, refs/LEDGER.md with notes N1-N3, the shard
theory/lanes/wh-kappa/prove/wh-kappa.md, and the verdict
theory/verdicts/wh-kappa-r1.md IN FULL.

This is the single repair wave of the capped L6 loop. There is no second critic
round: the orchestrator verifies your fixes mechanically and adjudicates.

## The finding you are repairing is not a mistake to paper over. It is the result.

OBJ-1 (FATAL) is confirmed by independent orchestrator computation. Enumerating
the admissible cocycles -- every symmetric-bilinear shift `β' = β + s`, all of
which satisfy the brief's ONLY requirement `β' - β'^T = ω`:

- `p = 2`, `q = 2`: the `p^3 = 8` admissible cocycles give **6 dihedral `D_4`
  and 2 quaternion `Q_8`** Heisenberg groups. Non-isomorphic. The 6/2 split
  matches the verdict's 6-of-8 subgroup-order split exactly, and
  `|Out(D_4)| = 2`, `|Out(Q_8)| = 6` matches the two subgroup orders.
- `p = 3`: all 27 admissible cocycles give the same group.
- `p = 5`: all 125 give the same group.

So the honest structural statement, which is a POSITIVE result about the
definition and the most interesting thing this increment has produced, is:

  **The assignment depends, beyond `(κ, ψ)`, on a choice of polarizing cocycle
  `β` with `β - β^T = ω`. At odd `p` that choice is immaterial: `β = ω/2` is a
  canonical representative and all choices give isomorphic systems. At `p = 2`
  it is NOT immaterial: the admissible cocycles fall into genuinely distinct
  isomorphism classes, and the extra datum is the quadratic form
  `Q(v) = β(v,v)`.**

This is why the registered source says "for **some** non-symmetric bilinear
form β" (`refs/arxiv-0808.1664`, and see ledger note N2) -- the literature
carries the same choice. Your job is to make the campaign carry it explicitly.

## Work order

1. **Promote `β` to a named choice.** D2/D3 must declare the polarizing cocycle
   as part of the choice datum, not as a fixed convention. Every canonicity
   claim is restated as a dependence on `(ψ, β)`. Say what the family of
   choices is (a torsor under symmetric bilinear forms) and what the transition
   data is.
2. **State the dichotomy as a theorem** with the proof: odd `p` -- symmetrizing
   gives a canonical representative and all choices are equivalent; `p = 2` --
   they are not, with the invariant that separates them. Give the `p = 2`
   invariant intrinsically (the quadratic form / Arf-type invariant), not as
   "we computed 6 versus 2".
3. **Restate the characteristic-2 results relative to `β`.** The `O(Q)` claim,
   the `2(q-1)` order, and the order-4 phases are properties of `(κ, ψ, β)`.
   The orchestrator independently confirms `|O(Q) ∩ SL_2| = 2, 6, 14` at
   `q = 2, 4, 8` for D2's `β`, so the computation is right -- only its
   quantification was wrong.
4. **OBJ-2:** replace `WH-FUNCT-b`'s false "sections exist" with the verdict's
   sharper positive statement -- the sections over the inclusion poset are
   exactly the characters nontrivial on the prime field. Prove it, and check
   composition and identities.
5. **OBJ-3:** `κ`-linearity in D7 is imposed extra data; the algebra itself
   only sees `V` as an `F_p`-symplectic space, so its intrinsic symmetry group
   is the larger `Sp_{2m}(F_p)`. State this as a second canonicity finding
   rather than burying it: the `κ`-structure is not recoverable from the
   quantum system.
6. **Adopt the verdict's gifts**, with their proofs, crediting the verdict:
   OPEN-1 splits at `q = 2, 4` and genuinely needs `μ_4`; OPEN-2's answer is
   `SL_2(κ)` for all `q` (note the verdict's warning that the self-adjointness
   route is false at `p = 2`).
7. **Re-label every row.** Fifteen rows at PROVED did not survive. Each row's
   status must now match what the argument delivers AFTER these repairs, with
   the affected scope inside the statement. A row that is now conditional says
   its condition; a row whose quantifier shrank says the smaller quantifier.
8. **Fix the checker.** `theory/checks/wh_kappa_check.py` gate C7's
   ψ-isotropy sub-check is dead code (`0 != 0`) -- a gate that cannot fail, the
   exact defect class the critic protocol names. Repair it, add a red mode that
   reaches it, and add a new gate for the `β`-dependence dichotomy: over the
   admissible cocycles, the Heisenberg groups fall into one class at odd `p`
   and more than one at `p = 2`. Copy the checker into your lane dir, edit the
   copy, and list the edits in PATCH.md with string anchors.

Deliverables in your lane dir: `wh-kappa.md` (the repaired shard),
`PATCH.md` (definitions, notation, and checker edits, string-anchored),
`CLAIMS-ROWS.md` (re-labelled), `REPAIR-NOTES.md` (objection by objection: what
you changed, or why the objection does not land), `SUMMARY.md`.
