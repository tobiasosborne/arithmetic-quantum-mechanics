# PATCH — proposed trunk integration

This lane made no trunk edits.  Apply by exact content copy and anchored
replacements; do not use line numbers.  Installing finite evidence does not
promote SP-LREL or SP-COMPACT.

## 1. Install the checker and its pre-registration

Copy exact contents:

- `theory/lanes/phantasm-relations/checker/phantasm_relations_check.py`
  to `theory/checks/phantasm_relations_check.py`;
- `theory/lanes/phantasm-relations/checker/EXPECTATIONS.md`
  to `theory/checks/phantasm_relations_EXPECTATIONS.md`.

The checker is standalone and has no imports from another lane.  The normal
session-close discovery will find it and all help-advertised `--red-*` modes.

## 2. Record SP-LREL finite evidence in the DAG

Within the block anchored by the exact heading `## SP-LREL`, replace:

    - Checks: none

with:

    - Checks: theory/checks/phantasm_relations_check.py

and replace:

    - Evidence: planned

with:

    - Evidence: draft

Replace the paragraph beginning with the exact anchor
`**Falsifier scope.** Enumerate affine Lagrangians in F2^2 and F3^2` by:

    **Falsifier scope.** Implemented: phantasm_relations_check.py G1--G5
    enumerates all zero/one-register affine Lagrangian Hom-sets over F2 and
    F3, including empty, state/effect, nonfunctional and nontransverse cases.
    All 144,806 composable pairs compare sparse existential composition with
    an independent affine-equation/dimension oracle. Identities and daggers
    are exhaustive; associativity is exhaustive for all 290,794 typed F2
    triples and uses 4,096 deterministic typed F3 triples. Direct-sum tensor,
    symmetric coherence and the faithful affine graph embedding are checked
    at the exact finite scope registered beside the checker. Finite success
    does not prove closure in arbitrary rank or over every finite field.

The existing required-mutations paragraph may remain.  Its source-sign,
empty-case and middle-quantifier defects are all executable; adjacent
expectations register the additional dagger, tensor, unit and graph controls.

## 3. Record SP-COMPACT finite evidence in the DAG

Within the block anchored by the exact heading `## SP-COMPACT`, replace its
exact `- Checks: none` and `- Evidence: planned` lines by:

    - Checks: theory/checks/phantasm_relations_check.py
    - Evidence: draft

Replace the paragraph beginning with the exact anchor
`**Falsifier scope.** Enumerate both snakes, names and unnames` by:

    **Falsifier scope.** Implemented: phantasm_relations_check.py G6--G7
    constructs D1714's opposite-form dual, graph associator/unitors/swap and
    ordered diagonal cup/cap over F2 and F3. It checks both fully typed snakes,
    eta dagger compatibility, all 466 small names and unnames including empty
    relations, the two Boolean unit scalars with lambda_0-transported tensor,
    and the true closed loop separately from its q^2 middle witnesses. The
    flat tuple representation realizes, rather than omits, the registered
    coherence graphs. Finite success does not prove dagger compactness over
    every finite field or in arbitrary rank.

The checker has explicit compact-dual, cup-order, dagger-swap, snake-wire,
loop-multiplicity, empty-name and relation-dagger mutations, alongside the
zero-unit control.  G6a--G6d give distinct dual-isotropy, cup-order,
dagger-swap and first-snake failure paths.

## 4. Update the canonical tested-in cells without promotion

In `claims/CLAIMS.md`, use the row beginning with ``| `SP-LREL` |`` as the
anchor.  Replace its final cell

    `claims/PHANTASM-DAG.md` (proposed falsifier only; none run)

with

    `theory/checks/phantasm_relations_check.py` (exact finite scope only; see DAG)

In the row beginning with ``| `SP-COMPACT` |``, replace its final cell

    `claims/PHANTASM-DAG.md` (proposed finite controls only; none run)

with the same checker-path wording.  Keep both statuses `SKETCH` until their
separate proof/review/adjudication requirements are satisfied.

## 5. Update labbook provenance for the installed finite controls

In `labbook/sections/symplectic_phantasm_contracts.tex`, replace the exact line

    \provenance{SP-LREL}{Inherited: No admitted earlier theorem claimed; remaining comparison in the DAG}{Proposed falsifier only}{SKETCH; promotion review pending}

with

    \provenance{SP-LREL}{Inherited: No admitted earlier theorem claimed; remaining comparison in the DAG}{Exact F2/F3 zero/one-register relation falsifier at its declared finite scope}{SKETCH; promotion review pending}

Replace the exact line

    \provenance{SP-COMPACT}{Source-informed construction outline in the DAG}{Proposed finite controls}{SKETCH; proof and review pending}

with

    \provenance{SP-COMPACT}{Source-informed construction outline in the DAG}{Exact F2/F3 compact-relation controls at their declared finite scope}{SKETCH; proof and review pending}

## 6. Coordinator verification after integration

Run the installed checker green and every `--help`-advertised red mode, then
run `python3 theory/checks/phantasm_contract_check.py` and the ordinary
labbook/session-close gates.  Any later admission must separately install the
proof, blind review and adjudication paths; this patch records finite draft
evidence only.
