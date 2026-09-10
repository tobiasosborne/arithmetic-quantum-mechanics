# String-anchored coordinator patch plan

Lane model: `gpt-5.6-sol`, reasoning `xhigh`.

This lane made no trunk edits.  The coordinator registered D1714 and
SP-COMPACT at `SKETCH` while the lane was active.  The registration anchors
below are an audit record; do not insert a second copy.  The remaining patch
is proof integration after reconciliation with the independent checker
contract.

## 1. Proof shards

Copy these lane artifacts without changing their mathematical content:

- `lrel-reduction.md` to
  `theory/symplectic-phantasm/lrel-reduction.md`;
- `lrel-laws.md` to `theory/symplectic-phantasm/lrel-laws.md`;
- `compact.md` to `theory/symplectic-phantasm/compact.md`.

Keep the existing `SP-LREL` status at `SKETCH` and the proposed
`SP-COMPACT` status at `SKETCH` through the prover pass.  The proof fields may
point at these paths for review, but promotion requires the scheduled blind
review and adjudication.

## 2. Definition and notation registration

In `definitions.md`, the new block is already anchored after the full D1713
block ending in the string

> **Delta.** Extend the state conventions to a general C*-algebra and specify GNS and modular hypotheses; no new finite Born normalization is introduced.

Verify that the following D1714 block matches the clean body in `PROPOSAL.md`
and contains only one scalar-tensor prescription.  Its graph tuple maps are
prescriptions; their symplecticity is proved in `compact.md`.

In `notation.md`, the D1714 ownership rows are already anchored after the row
containing

> `alpha_(t,g)`

Verify ownership for
`a_(U,V,W), lambda_V, rho_V, sigma_(V,W), eta_V, epsilon_V`, and the
name/unname brackets.  Do not introduce a `V^*` alias, fresh scalar symbols,
or a symbol for the transported scalar tensor.

## 3. Canonical claims and DAG

In `claims/CLAIMS.md`, the new row is already anchored after the complete row
beginning

> | `SP-LREL` |

Verify it against the one-line `SP-COMPACT` row in `PROPOSAL.md`.  Its
dependency list contains `SP-LREL`; the headline is unconditional and its
status remains `SKETCH`.

In the `PHANTASM-ORDER` table of `claims/PHANTASM-DAG.md`, the new node is
already anchored after

> | SP-LREL | 2 | 4 |

Verify `SP-COMPACT` occurs next and the priorities of the old later nodes are
incremented.  Its full DAG contract is already before the heading

> ## SP-STAB-REL

and uses comma-separated IDs only in `Definitions`, `Dependencies`,
`Inherited`, and `Sources`.  After proof integration, replace its `Proof:
none` with the compact proof path for review; do not change evidence to
admitted or fill the review field during this pass.

For the existing `SP-LREL` node, anchor on

> - Remaining: Derive closure by finite linear reduction and the affine empty-case law; then verify graph, dagger and tensor typing.

After integrating the prover artifact, the coordinator may replace `Proof:
none` by the two LREL proof paths and `Evidence: planned` by the repository's
standard draft/prover-pass wording.  Do not alter the statement, scope,
dependencies, or status before review.

## 4. Labbook lockstep

Use `LABBOOK-FRAGMENTS.tex` as copy-ready prose, while preserving the exact
canonical restatements chosen by the coordinator.

In `labbook/sections/symplectic_phantasm.tex`, the definition is already
registered before

> \subsection{Shared register and hierarchy conventions}

Verify its exact definition, scope, and provenance.  Keep source locators in
provenance or the ledger rather than in the canonical definition metadata.

In `labbook/sections/symplectic_phantasm_contracts.tex`, the compact
proposition is already anchored after the existing block ending

> \provenance{SP-LREL}{Inherited: No admitted earlier theorem claimed; remaining comparison in the DAG}{Proposed falsifier only}{SKETCH; promotion review pending}

Verify the canonical claim text and exact scope.  The concise proof fragments
may accompany the propositions only with the prover-pass/unreviewed status
visible.  The coordinator should replace that wording after adjudication
rather than pre-promote either result.

## 5. Structural-plan link

In `docs/research-plans/categorical-structure.md`, anchor on

> compact structure requires an explicit additional claim before admission

Replace that planning sentence with a link to the registered `SP-COMPACT`
node and retain its `SKETCH`/dependency boundary.  In the numbered compact
follow-up, record the two-element relational scalar result separately from
the later actual-amplitude and scalar-quotient computations.

## 6. Scope that must survive integration

The LREL proof covers every finite field, including characteristic two,
zero spaces, empty arrows/composites, affine translates, nonfunctional
relations, associativity, converse dagger, reordered direct-sum tensor,
coherence, and the faithful graph functor.  The compact claim adds the exact
opposite-form dual, displayed cup/cap orders, both fully unital snakes,
dagger compatibility, name/unname, empty and affine cases, and the
transported scalar tensor.  It adds no quantum normalization, amplitude,
probability, stabilizer equivalence or Choi theorem.
