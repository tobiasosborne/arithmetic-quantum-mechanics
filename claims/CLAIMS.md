<!-- ROLE: the argument DAG (L5). One row per claim. Status changes only through
     the capped L6 loop of PRD.md; verdict files live in theory/verdicts/.
     Authoritative statuses: PROVED | SKETCH | CONJECTURE | REFUTED.
     Conditional, empirical, under-review and future-work qualifiers belong in
     the statement prose, NEVER as additional status values. -->

# Claims DAG

## Status vocabulary

| status | means |
|---|---|
| `PROVED` | a Lamport-structured proof survived the capped L6 loop with no open FATAL or MAJOR on this statement. A conditional result displays its condition inside the statement and is still written `PROVED`. |
| `SKETCH` | an argument exists and is written down, but the loop ended with an unresolved MAJOR, or a step is admitted. A legitimate terminal state. |
| `CONJECTURE` | believed or wanted, with no argument that survived a round. Evidence from a passing falsifier does not change this. |
| `REFUTED` | a counterexample or a fatal objection landed. The row stays, with the surviving weaker statement recorded beside it. Nothing may depend on a REFUTED row. |

Rules that are not negotiable:

- When in doubt, the label goes DOWN.
- A passing falsifier promotes nothing. A disagreeing falsifier blocks promotion
  unconditionally, even against a proof that passed review.
- No row may be justified by `v0.1/` (L12). Inherited statements are re-derived
  or they are not here.
- Every row's `proved in` and `tested in` cells point at a real file. An empty
  `tested in` is honest; a fabricated one is a FATAL defect.

## Rows

| id | statement (short) | status | depends on | proved in | tested in |
|---|---|---|---|---|---|

*No rows yet. The first increment is `briefs/wh-kappa-target.md`; its rows enter
here only after the L6 loop reports, at whatever status that produces.*
