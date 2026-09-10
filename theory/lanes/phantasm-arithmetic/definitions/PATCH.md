# String-anchored definition/interface patch plan

Preparation model: `gpt-5.6-sol`, reasoning `xhigh`.

This lane makes no trunk, proof, checker, claim-status or Git changes.

## D1710

In `definitions.md`, replace the complete block from

> ## D1710 (a specified quantum subsystem decoder)

through its `**Delta.**` paragraph immediately before `## D1711` with the
complete proposed D1710 body in `CANDIDATE.md`. Do not append only the final
equation: the shared model spaces, complement types, pure-tensor
reassociation, phase allowance, rank-zero convention and Scope obligations
must land together.

Make the exact same full-body and Scope replacement in
`labbook/sections/symplectic_phantasm.tex`, anchored on

> \begin{definition}[a specified quantum subsystem decoder]

and its D1710 provenance block.

In `notation.md`, anchor on the existing D1710 row containing

> `j`, `J`, `iota_J`, `D_J`

and extend it to own `ell`, `W_j`, `W_ell`, `W_(ell j)`, `J_j`, `J_ell`,
`J_(ell j)`, and `J^perp_(j,ell)` for the typed iterated datum. Do not add a
new associator symbol: the definition displays the ordinary pure-tensor
reassociation explicitly. `lambda` remains a bound phase and needs no global
notation row.

No canonical SP-SUBSYS statement or dependency changes. Its existing
“compatible iterated tensor decompositions” clause is now owned by D1710;
the comparison-map, existence, phase-independence and decoder-composition
properties remain obligations.

## SP-FROB channel-typing dependency

In `claims/CLAIMS.md`, anchor on the `SP-FROB` row. Add `D1706` and `SP-CP`
to its depends-on field only; preserve the statement, status and proof/check
pointers.

In `claims/PHANTASM-DAG.md`, anchor on `## SP-FROB` and make these exact
field changes:

- `Definitions:` add `D1706`;
- `Dependencies:` add `SP-CP`;
- `Reuse:` append “SP-CP supplies only the ambient unitary-conjugation
  channel typing; the relative Frobenius covariance, inverse and finite power
  are separate SP-FROB calculations.”

Mirror the dependency/provenance change beside the SP-FROB proposition in
`labbook/sections/symplectic_phantasm_contracts.tex`. Do not change its
statement, Scope or `SKETCH` status. SP-CP is already admitted, but the added
dependency records the exact reuse route rather than promoting SP-FROB.

## Timing

Apply this definition/interface patch only as preparation for the arithmetic
cluster after the planned SP-SUM pass. It authorizes no arithmetic proof or
status change by itself.
