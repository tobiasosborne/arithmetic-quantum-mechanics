# Categorical structure and its transport

TJO steering, 2026-09-10, following the question about cups, caps and the
Choi correspondence: understand and track the possible structural
properties of the categories, and their interactions, so that the right
structure can be found flexibly as the arithmetic construction develops.
This is a continuing research direction within the Symplectic Phantasm.
The SP-WEYL → SP-EGOROV → SP-TENSOR cluster is now admitted. The next
bounded task is SP-LREL and the compact-structure follow-up below, under
`../../briefs/phantasm-relations-target.md`.

## What the record should answer

For a specified category and a proposed structural adjective, ask what
data and laws it requires, what it enables, and what happens to it under
the actual comparison functors. Track combinations of properties as well
as individual properties. A term shared by two constructions is a question
about their comparison, not evidence that their structures agree.

The vocabulary is open and grows with the research. The first questions
below select useful entry points; they are not an exhaustive classification
of categorical structures or an assertion that every candidate has them.

## One mathematical record

Definitions, including precise meanings of newly used structural terms,
belong in `../../definitions.md`; symbols in `../../notation.md`;
mathematical statements and statuses in `../../claims/CLAIMS.md`; source
scope and locators in `../../refs/LEDGER.md`. This plan records questions
and links, without maintaining a competing truth table.

For each property under investigation, record:

| Item | Required content |
|---|---|
| Exact carrier | Definition of the category: objects, arrows, equality, coefficient domain and characteristic restrictions; distinguish any subcategory or quotient |
| Structure | Named data, their types, axioms and coherence diagrams; distinguish existence from a chosen structure and from uniqueness |
| Evidence | Existing claim and proof clauses that apply, exact local source scope, remaining argument, and a small witness or falsifier where useful |
| Comparison | A specified functor with source, target and variance; whether preservation, reflection or creation of this structure is claimed, and the exact strict, coherent or projective sense |
| Interaction | Implications or compatibility conditions involving other recorded properties, with their own claim dependencies; unresolved combinations remain questions |
| Research use | The construction or calculation this property would enable, the information a change of category would retain or lose, and the next useful comparison |

Read statuses from the linked canonical claims. An uninvestigated property
is not false, and a source theorem is not automatically a theorem about
our category. If a new combination needs another datum, name it in a
definition before assigning the adjective. A failed candidate should lead
to a revised construction or a stated choice; it does not start a separate
obstruction-review campaign.

## Initial questions, grouped by mathematical role

| Role | Properties and distinctions to investigate | What their interaction should resolve |
|---|---|---|
| Composition and exchange | Monoidal, braided, symmetric; strict structure versus coherent comparison maps | Which independent assemblies and exchanges the arithmetic maps respect |
| Reversal and bending wires | Dagger, duals, rigid, compact closed, dagger compact; pivotal, spherical and traced structures when needed | State/process correspondence, evaluation, closed diagrams, and compatibility of duality with the dagger |
| Scalars and combinations | Scalar monoid, enrichment over a named semiring or field, positivity and convex structure | Which sums and rescalings are available, and what a scalar quotient forgets |
| Sums and completion | Products, coproducts, biproducts, additive and idempotent completions; two monoidal products and distributivity | Whether a proposed sum is coherent, classically tagged or a classical source construction, and how it interacts with tensor and duality |
| Quantum processes | CP branches, normalized channels, retained instruments, discard and causal structure | Which operations remain available after normalization, and whether daggers, cups and caps still have the required types and normalization |
| Representation targets | Linear, abelian, semisimple, rigid, fusion, dagger and C*-categorical conditions | Which hypotheses a proposed representation category actually satisfies, including the role of its unit, simple objects and realization functor |
| Completion and dynamics | Hilbert completion, bounded morphisms, continuity and specified states | Which finite constructions extend and what analytic hypotheses are newly required; distinguish properties of a category from those of an associated algebra or representation |

Each row is an investigation agenda. In particular, the words in a row do
not assert equivalence or simultaneous compatibility. Record the actual
implication or comparison only when its definitions and evidence exist.
Keep categorical traces, ordinary matrix traces and normalized reference
functionals distinct until their comparison is stated and proved. Likewise,
specify the monoidal product whenever asking whether a unit is terminal,
an object is dualizable or a direct sum is a biproduct.

## Starting carriers and comparison tasks

| Existing carrier | Structural questions to track | Current homes for the work |
|---|---|---|
| Symplectic symmetry groupoids, D1701 | Direct-sum coherence and which new arrows are needed for states, effects and duality | SP-EGOROV, SP-TENSOR; F1-FUNCT only at its configuration-isomorphism scope |
| Affine Lagrangian relation candidate, D1702 | Category laws, converse dagger, opposite-form duals, diagonal cups/caps and state/process correspondence | SP-LREL; compact structure requires an explicit additional claim before admission |
| Actual stabilizer amplitudes and their scalar quotient, D1704–D1705 | Dagger and tensor transport, duality, scalar monoids and normalization lost under the quotient | SP-STAB-REL, SP-SCALAR, DG-REL-LIFT |
| Coherent completion and tagged observable systems, D1707 | Linear combinations, biproduct questions, tensor distributivity, idempotent splitting and the relation to a classical sum | SP-SUM, DG-RIG; do not identify a tagged observable algebra with a coherent one |
| Ordinary-trace quantum branches and instruments, D1706 | Ambient branches versus channels, outcome retention, discard, dagger and compact-structure compatibility | SP-CP, SP-SUBSYS; distinguish realized CP equality from D1325 source equality |
| Arithmetic amplitudes and source-certified processes, D1321–D1327 | Which structures the arithmetic presentation carries and its interpretation preserves or forgets | FRP-CAT, FRP-CP, FRP-DESCENT at their admitted scope; DG-REL-LIFT for matched fragments |
| Phase representation categories and their central sectors, D1011 | Internal tensor, matching external products, closure of a selected sector, fusion hypotheses and the role of the realization functor | F1-CAT remains SKETCH; reuse F1-WEYL/F1-FUNCT/F1-REAL without promoting the categorical comparison by association |
| Fock and prime assembly data, D1708, D1711–D1713 | Domains of functorial completion and the extra state/dynamical choices | SP-FOCK, SP-PRIME, DG-GLOBAL, DG-MODULAR; a chosen algebra is not itself a replacement category |

## First established comparisons

Read the current status and exact hypotheses from the linked canonical
claims and proofs. These entries explain how the stage-1 results answer
part of the structural questions; they do not introduce another status
register.

| Comparison | Structure supplied by the existing claim | Choice or remaining boundary |
|---|---|---|
| SP-WEYL, `../../theory/symplectic-phantasm/reuse.md` sections 1–2 | Full matrix realization with faithful normalized trace; unitary model uniqueness and phase ambiguity made explicit | Fixed odd-characteristic field and nontrivial character; named coordinates only for the standard formula |
| SP-EGOROV, `../../theory/symplectic-phantasm/egorov.md` | Exact covariant affine algebra action and composition; unique projective unitary implementation and model transport | D1703 owns the arbitrary-rank extension of D9; no genuine phase section has been selected |
| SP-TENSOR, `../../theory/symplectic-phantasm/tensor.md` | Natural trace-preserving direct-sum/tensor comparison with exact algebra associativity, units and symmetry; projective model coherence | Uses F1-FUNCT at its admitted scope; coherent additive completion and duality are separate next questions |

## First concrete follow-up: cups, caps and scalar transport

The discussion identifies a useful extension of the relation cluster.
SP-CK21 explicitly discusses compact closure and currying in §2; the
registered odd-prime stabilizer comparison in §4 is modulo invertible
scalars. The following are proof tasks, not new admitted conclusions:

1. After the D1702 category laws, formulate the opposite-form dual and
   diagonal cup/cap data, with factor orders, the zero-space unit, dagger
   compatibility, both snake equations and affine/empty cases explicit.
   The existing SP-LREL statement does not yet include this compact claim.
2. Formulate the induced correspondence between an arrow and a state of
   the combined dual-input/output object. Match operator vectorization and
   the CP Choi construction separately; record the relevant dual or
   conjugate Hilbert-space convention.
3. Compute scalar endomorphisms of the unit and closed cup/cap diagrams in
   the relation, actual-amplitude and scalar-quotient settings. Compare
   both normalized and unnormalized Hilbert representatives, their snake
   equations and their admissibility as physical branches.
4. Use that comparison to specify what a scalar-retaining relation lift
   must carry at DG-REL-LIFT, and what a proposed additive completion must
   preserve at DG-RIG. Register any additional definitions and claims
   before extending the DAG; do not silently enlarge an existing claim.

The same method should accompany later lemma clusters: update the relevant
questions when a result establishes a property or changes a comparison.
Keep the human-readable account in the Phantasm labbook section. A small
Markdown record suffices; an interactive explorer can follow once there
are enough proved relationships to make its queries useful.
