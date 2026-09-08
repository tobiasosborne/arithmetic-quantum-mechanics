# Frobenius and arithmetic hierarchy — capped adjudication

Date: 2026-09-08. Scope: the new arithmetic-fibre package only, following
the user's explicit plan/orchestration request and
`briefs/frobenius-hierarchy-target.md`.

Two native proof lanes, one independent checker lane and two fresh blind
critics were used. Models inherited the native runtime; no exact model name
was exposed independently. Both verdicts explicitly record same-family blind
review. There was one review of each proof artifact, one repair wave, and
root mechanical verification. No review-to-fixed-point was run.

## Decisions

All ten new rows are admitted as PROVED within their displayed hypotheses:

| rows | admitted mathematical content |
|---|---|
| FRB-TRACE, FRB-FROB | All-characteristic trace geometry, exact Frobenius/Weyl covariance and order, named basis/dual-basis atomic factorization |
| FRB-CODE | Subfield support stabilizer code and its trace-labelled logical symplectic quotient |
| FRB-TRANSFER | Inclusion and normalized trace-fibre isometries, negative Fourier comparison, named field towers and Frobenius equivariance |
| FRB-HIERARCHY | Exact level d+1 of the d-control multiplication accumulator, with no bound on d relative to p |
| FRB-NATURAL | Multiplication/Frobenius/embedding compatibility, encoded logical action and the stated coherent return probability |
| FRB-EXAMPLE | The explicit binary degree-four tower, Frobenius shear, traces, support code and distinct invariant-vector space |
| FRP-CAT | The specified small arithmetic amplitude presentation and its dagger monoidal Hilbert interpretation |
| FRP-CP | Certified retained processes, independent symmetric tensor, ordinary-trace CP realization and its explicit nonfaithfulness |
| FRP-DESCENT | Typed success/failure decoding, success-tower and independent parallel laws, Fourier decoder square and encoded gates |

Seventeen definitions, D1301--D1310 and D1321--D1327, are integrated. The
full register has 117 claims: 96 PROVED, 19 SKETCH, one CONJECTURE and one
REFUTED; there are 125 definitions. Older claim statuses are unchanged.

## Review findings and verified repairs

The frozen verdicts are `frobenius-hierarchy-algebra-r1.md` and
`frobenius-hierarchy-category-r1.md`. Both end PASS with no FATAL or MAJOR.

1. **Algebra finding 1: redundant A5 comparison.** The alleged extra
   conjugation check merely indexed the same phase table twice. The checker
   repair removes that loop and its misleading independence language, while
   retaining exact Fourier block extraction, the all-translation filtration,
   strictness and interference checks. Root inspected the complete source
   diff: only that loop and its wording changed. The 756 removed assertions
   reduce the final green count to 263857. All twenty substantive named
   mutations still reject at their intended gates.
2. **Algebra finding 2: dependency edge.** FRB-TRANSFER now explicitly lists
   FRB-CODE, whose character-sum argument its Fourier proof invokes. Root
   checked the referenced step and the resulting acyclic dependency graph.
3. **CAT-1: literal smallness.** D1325 now fixes a countable naming universe
   containing the finite field-element labels and closed under finite tuples.
   External and hidden sets are finite subsets of that set. This is carried
   into the labbook and the explicit set-encoding argument at process proof
   step `<1>0`. Finite arrays of amplitude classes form sets before taking
   hidden-index bijection quotients; no proper-class quotient is required.
   All original composition, tensor and certificate equations are unchanged.
4. **CAT-2: trace normalization.** Both the labbook and the next-stage
   proposal now state `tau(1)=1` in the trace-one-unitary implication. Root
   checked the expansion `2 tau(1)-tau(U)-tau(U*)` and the critic's ordinary
   trace counterexample. This repair does not alter an arithmetic CP theorem
   or assert existence of an endpoint.

Root also escaped literal cardinality bars in the new Markdown claim rows
and replaced draft/proof/checker locators by their installed paths. These
are transcription changes. All owning labbook status macros were promoted
in the same integration, including the supporting interference proposition.

The reviewed category source included zero/basis preparations, quantum
discard and a named coordinate circuit. The checker added its A7-PREP probe
before the category review completed. At p=2 the source coefficient field
is real; the category remains the specified arithmetic fragment and is not
claimed to contain every Clifford gate.

## Evidence versions and reproducibility

The algebra critic ran the checker with SHA256
`85636a872152f896163c2cb42cf301400f591d21d97951ab8c391fc0c7971756`,
including 19 named mutants and 264135 green assertions. The category critic
ran its successor
`f242fabfc7c124048f1f626d9f5131a44c105e6a39b7ee10d493fe9703d00777`,
which adds A7-PREP and its mutant, with 264613 green assertions.
The final reviewed-repair checker is
`946ca4584424329e85b92107664d24c89942f194de42dd0737ddc372d77d8c12`.
The A5-only repair leaves the category's reviewed A7 code unchanged.

`theory/checks/frobenius_hierarchy_check.py` is standalone. Expectations are
in `theory/checks/frobenius_hierarchy_EXPECTATIONS.md` and the companion
process expectations. The final freezer ran twenty named red subprocesses
before its green run: every red reports its intended mathematical FAIL and
exits 1; green reports PASS and exits 0. A separate copy with the intended
gate disabled reports mutated PASS and exits 0, verifying that a red flag
does not force failure independently of the mathematical gate.

Frozen final results and source checksum are under
`numerics/frobenius-hierarchy/results/`. Independent reviewer output records
are retained in its `review/` subdirectories. The verdicts preserve their
own executed version boundaries; predecessor counts are not attributed to
the final checker. Frozen lane filenames in the verdicts correspond to the
installed same-named proof shards, root definitions/claim rows and the two
new labbook sections. The four repairs above enumerate the semantic delta.

The algebra reviewer additionally used a fresh flat polynomial model of F16
and multiplication-matrix traces, including twisted field embeddings. Its
hierarchy probes reached F2 d=1..8, F3 d=1..6 and F4 d=1..4. The category
reviewer independently checked F4/F9 Weyl, Fourier-decoder, coordinate and
discard matrices, and mutated types, tensor order and Born references.
These computations corroborate the structured proofs; they do not establish
their universal quantifiers by sampling.

## Operational and endpoint scope

The amplitude source has marked field/code objects, arithmetic equations,
coefficient scalars and finite circuit syntax. Its process equality retains
external outcomes and the specified Kraus data. It is not defined by CP
equality, and its CP realization is explicitly nonfaithful. No completeness
for arbitrary complex states, all CP maps, or all stabilizer contexts is
claimed. Higher hierarchy levels label generators and are not declared
composition-closed classes.

The arithmetic package supplies no positive q-to-one specialization theorem.
`docs/research-plans/frobenius-coupled-limit.md` gives the next bounded
proposal: coupled isotropic contexts with independently named incidence and
phase data, actual arithmetic comparisons, a positive trace and six witness
tests. The existing type-C correspondence and Hecke continuous family remain
benchmarks. Individual endpoint gate lifts and formal labels do not prove
that a diagram, arithmetic operation or observed quantum distinction survives.

## Final verification

The integrated labbook builds to 128 pages. `scripts/session-close.sh` passed
18 standalone green runs and all 143 advertised checker/red-mode runs, each
with the required nonzero exit. This includes twenty distinct mutations of
the new checker and its separately advertised default alias. Root verified
all five primary-source hashes, the five proof-shard size bounds, the claim
DAG and register counts, and visually inspected the hierarchy/process pages.
The exact mode list, final checker/PDF hashes and counts are frozen in
`numerics/frobenius-hierarchy/results/SESSION-CLOSE.json`.
