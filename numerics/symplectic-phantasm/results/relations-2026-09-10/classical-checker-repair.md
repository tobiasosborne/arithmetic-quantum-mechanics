# REPAIR — one classical checker repair wave

Date: 2026-09-10. Repair model: `gpt-5.6-sol`, reasoning `xhigh`.
Input: `theory/lanes/phantasm-relations/critic/VERDICT.md`.

This file records the single repair wave authorized after the blind review.
Only OBJ-3--OBJ-5 concern this checker lane.  OBJ-1, OBJ-2 and OBJ-6 belong to
the canonical/prover integration owned by the coordinator and prover repair.
No trunk file, mathematical claim, status or finite scope was changed here.

## OBJ-3 — repaired

The unsupported generic `--red NAME` argument was removed.  `--help` now
advertises exactly fourteen concrete named mutation flags and no bare
`--red`/placeholder.  Bare `--red`, an unknown red name, and multiple red
flags are usage errors with exit `2`.  Every advertised token reaches actual
mathematical data and a registered gate.

## OBJ-4 — repaired

G6 was split into named acceptance paths without changing the green formulas:

- G6a tests actual cup/cap affine Lagrangian typing, so `compact-dual` first
  fails the odd-characteristic diagonal isotropy test.
- G6b tests the exact ordered cup/cap types, so `cup-order` first fails there
  after its reversed diagonal passed isotropy.
- G6c tests `eta_V^dagger=epsilon_V o sigma_(bar(V),V)`.  The new
  `dagger-swap` mutation literally omits the swap, retaining epsilon's
  reversed source type, and first fails G6c.
- G6d and G6e test the snakes separately.  New `snake-wire` replaces only the
  first snake's cap by the same-typed empty relation and first fails G6d.
- G6f retains the independent cardinality check.

An initially attempted same-typed no-block-swap graph survived: the diagonal
cup is pointwise fixed by block swap.  This exposed why that mutation did not
model literal omission and was corrected before green.  Independently
disabling only G6c made the corrected red survive with exit `0`; after
restoration it failed G6c with exit `1`.

## OBJ-5 — repaired

`tensor_expected` no longer duplicates the production point-set
comprehension.  It independently encodes each relation as a Boolean matrix
with target rows and source columns, forms the Boolean Kronecker product, and
decodes its true entries through the ordered direct-sum bases.  The
`tensor-order` mutation now changes every sampled production tensor and
reaches this G4a oracle directly.  The neighboring affine typing,
tensor/dagger, swap, associativity and interchange checks are unchanged.

## Verification

The changed/new mutations were observed before repaired green.  All fourteen
advertised reds then exited `1` at their intended gates.  Bare help-placeholder
usage exited `2`.  The repaired ordinary green exited `0` in 17.73 seconds;
G1--G7 retained all previously registered finite counts.  The exact commands
and named paths are appended to `RUNS.md`.

The finite checker remains negative-binding evidence only.  It does not prove
SP-LREL or SP-COMPACT and does not alter their all-finite-field scope.
