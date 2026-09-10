# Proposed integration patch for SP-EGOROV and SP-TENSOR

This lane does not edit trunk.  Apply these changes only after the independent
checker artifacts and the blind critic disposition are available.  All
canonical statuses remain `SKETCH` during proof integration unless the full L6
promotion conditions are separately met.

## 1. Add the proof shards

Copy this lane's files without mathematical changes:

- `sp-egorov.md` to `theory/symplectic-phantasm/egorov.md`;
- `sp-tensor.md` to `theory/symplectic-phantasm/tensor.md`.

The copied headers deliberately retain the actual lane model and reasoning
setting.  During integration, replace only their lane-relative status wording
if the adjudication justifies it.

## 2. Update the canonical claim proof pointers without promotion

In `claims/CLAIMS.md`, use this exact string inside the `SP-EGOROV` row as the
anchor:

    `claims/PHANTASM-DAG.md` (SP-EGOROV outline only; no admitted proof)

Replace only that proved-in cell with:

    `theory/symplectic-phantasm/egorov.md` (prover draft; not admitted)

In the `SP-TENSOR` row, use this exact string as the anchor:

    `claims/PHANTASM-DAG.md` (SP-TENSOR outline only; no admitted proof)

Replace only that proved-in cell with:

    `theory/symplectic-phantasm/tensor.md` (prover draft; not admitted)

Do not change either row's statement, dependencies, or `SKETCH` status in this
mechanical proof-pointer patch.  The checker lane may separately supply a real
tested-in path; this prover lane makes no proposal about that path.

## 3. Update the SP-EGOROV DAG proof record

In `claims/PHANTASM-DAG.md`, locate the block beginning with the exact heading:

    ## SP-EGOROV

Within that block, replace the exact line:

    - Proof: none

with:

    - Proof: theory/symplectic-phantasm/egorov.md

Within the same block, replace:

    - Evidence: planned

with:

    - Evidence: draft

Retain `- Review: none` until the blind critic report exists.  Retain the
checker field until the independent checker lane supplies its final path and
scope.  The `Remaining` field should continue to record the unfulfilled blind
review and the explicit `SP-WEYL` dependency unless adjudication resolves them.

## 4. Update the SP-TENSOR DAG proof record

In `claims/PHANTASM-DAG.md`, locate the block beginning with the exact heading:

    ## SP-TENSOR

Within that block, replace the exact line:

    - Proof: none

with:

    - Proof: theory/symplectic-phantasm/tensor.md

The existing line `- Evidence: draft` already has the correct unpromoted value.
Retain it until adjudication.  Retain `- Review: none` and the existing bridge
checker path until their owning lanes are integrated.  The `Remaining` field
should continue to name review and any checker-confirmed obligations that have
not been discharged.

## 5. Definition and notation result

No change to `definitions.md` or `notation.md` is proposed.  The formula for
`alpha_(t,g)` is already part of the canonical `SP-EGOROV` statement and its
notation row.  Direct sums of affine arrows are constructed from D1701 inside
the proof.  `Theta_(V,W)`, the model intertwiners `J_(V,W)`, and the standard
associators/unitors/flips are bound proof witnesses; none requires a new
numbered definition for the exact current claims.

## 6. Labbook lockstep after adjudication

If either canonical claim statement, status, or proof scope changes during
adjudication, use the Section 31 proposition text containing the exact claim id
as the string anchor and update its statement/status/provenance in the same
trunk change.  This lane does not propose pre-emptive labbook prose or a status
promotion.
