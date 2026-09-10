# PATCH — planning and source-locator anchors

This planning lane makes no canonical edit.

## Watrous locator refinement

In `refs/LEDGER.md`, anchor on `### SP-WAT18`. In its `Verified locators:`
paragraph, add:

    §2.2, “The completely dephasing channel,” equation (2.162), printed
    pp.94--95: the standard-basis channel deletes off-diagonal entries and
    fixes diagonal entries.

In the Scope paragraph, add that the arbitrary block-dephasing formula used by
SP-SUM is rederived locally from orthogonal block projections; equation
(2.162) is the one-dimensional-block model, not a quoted block theorem.

## Conditional D1707 ownership patch

Before proof integration, anchor on D1707's sentence
`Realize a list as H=`. If the coordinator chooses definition ownership,
extend D1707 with the block action

    (T_(ji))(xi_i)_i=(sum_i T_(ji)xi_i)_j

and, for nonempty lists, name the summand projections and prescribe
`Delta_X(A)=sum_i P_i A P_i`. Add only the owned symbols to `notation.md` and
restate them in the labbook. If the coordinator instead expands the canonical
claim, put the same formulas there. Do not leave “realizes” or
“corresponding dephasing” without an explicit map.

No status, DAG evidence, or proof path should change from this planning lane.
