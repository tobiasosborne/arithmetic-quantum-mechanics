# The Hunting of the Symplectic Phantasm

Adopted by TJO on 2026-09-09. Active quest; earlier composite-boundary and
FCR-2 work orders are paused. The SOP is **sober, accretive, and careful**.

## Purpose and initial guidance

Build a precise classical arithmetic category and a quantum realization,
with their composition, field-extension and Frobenius structures explicit.
Investigate assembly across primes and comparison with Bost–Connes only
after the local constructions and their interfaces are established. The
Riemann hypothesis motivates the quest; no spectral identification is an
input assumption or a promised consequence.

The initial guidance is `fundamentals-two-categories.md`. Its user framing
and assistant assessment remain distinct. Adopting the note authorizes
investigating its ideas; it does not endorse its mathematical assertions.
`symplectic-phantasm-sources.md` records the source audit and definition map.

## SOP and durable records

1. Retrieve primary source bodies under `refs/`, preferring TeX. Inspect the
   actual title, authors, hypotheses and theorem/equation locators. Register
   routes, hashes and scope in `refs/LEDGER.md`. A missing source has a GAP
   entry and cannot support a claim. Citation discovery is not verification.
2. First inventory the admitted results and existing definitions. Record
   the exact reusable clauses and the remaining comparison; ground truth
   includes admitted local proofs. Then fix a small definition layer. Every object, Hom-set, composition, unit,
   variance, involution, scalar quotient and named choice must be visible.
   Put stipulations in `definitions.md` and symbols in `notation.md`.
   Properties such as closure, canonicity and positivity belong to claims.
3. Record each formulated lemma in `claims/CLAIMS.md` and its contract in
   `claims/PHANTASM-DAG.md`. State its inputs, output, dependencies, source
   scope, proof task and falsifier before attempting promotion. Undefined
   research choices are decision gates, not conjectural theorems.
4. Work in dependency order on one bounded cluster. Supply Lamport proofs,
   preregister exact finite falsifiers and observe their mutations fail.
   A finite pass supplies evidence at its stated scope, not a proof.
5. For promotion use one prove pass, one blind hostile attack, one repair
   wave and mechanical adjudication under PRD L6. Preserve unresolved
   objections by narrowing the statement or leaving its status unpromoted.
6. Keep the owning labbook section in the same change as the definitions,
   claims and examples. Run the argument-contract check, lockstep gate and
   real PDF build; record the next bounded task in `HANDOFF.md`.

This is rk-light: Markdown is the argument record, with a small local
contract checker. No theorem prover, CI service or repeated review campaign
is required. Contract checks validate references,
types as declared, dependency order and evidence/status consistency. They
cannot decide whether a proof is mathematically correct.

## Tracking categorical structure — TJO steering, 2026-09-10

Understand and track the structural properties the categories can carry,
their interactions, and their transport through the comparison functors,
so that the arithmetic construction can develop flexibly. The working
record is `categorical-structure.md`. It starts with cups/caps and the
state/process correspondence, then links scalar normalization, sums,
duality and quantum-process structure to the existing research gates.

For each adjective, specify the exact category and extra data, the laws,
the evidence and what it enables. For each comparison, specify what is
preserved or forgotten and in what sense. Definitions and claim statuses
remain in their single sources. The record is an open research agenda,
not an assertion that all desired structures coexist. It accompanies the
bounded lemma clusters; SP-WEYL → SP-EGOROV → SP-TENSOR remains next.

## Construction order and acceptance gates

| Stage | Concrete deliverable | Exit condition |
|---|---|---|
| 0. Ground truth | Primary-source ledger, scope corrections and complete inventory of the note's definition requests | Every named literature lead is either locally verified or an explicit GAP; all sources used in the first cluster are local |
| 1. Local objects and symmetries | Arbitrary-rank finite symplectic spaces, odd-characteristic Weyl algebra, affine Egorov action and direct-sum/tensor comparison | Typed contracts and proofs for SP-WEYL, SP-EGOROV and SP-TENSOR, with rank-zero and rank-one regressions |
| 2. Relations and quantum processes | Affine Lagrangian relations, scalar-quotient stabilizer comparison, actual amplitude and instrument semantics | SP-LREL, SP-STAB-REL, SP-SCALAR and SP-CP; scalar recovery and success probabilities explicitly distinguished |
| 3. Two sums and particle sectors | Coherent Hilbert sums, classical tags, and bosonic Fock construction on a stated class of maps | SP-SUM and SP-FOCK; decide what additional classical completion is wanted before calling it a rig quantization |
| 4. Arithmetic extensions | Restriction of scalars, named Frobenius and subsystem decoding | SP-TRACE, SP-FROB and SP-SUBSYS; extension-degree-divisible-by-characteristic examples included |
| 5. Global control objects | A specified inductive tensor product with product reference, and a concrete Bost–Connes benchmark | SP-PRIME and SP-BC-CONTROL; distinguish the two algebras and their dynamics |
| 6. The phantasm construction | A proposed global arithmetic algebra or category carrying compatible noncommutative arithmetic processes | Resolve the global design gates below, add its precise definition and expand the DAG before proving anything about it |
| 7. Spectral investigation | A named operator/flow, representation, state, trace or regularization, and exact arithmetic comparison formula | Establish domains and convergence first; any relation to zeta zeros gets a separate explicit claim and evidence |

Stages may share established dependencies; numerical order is a priority,
not permission to assume earlier exit conditions. Stage 1 starts at odd
characteristic to expose a clean normalization. Characteristic two remains
a required design gate for a claim about all primes, with its distinct
central extension and quadratic data recorded. It is not silently included
by applying a formula containing one half.

## Decisions that must earn their own definitions

These are research tasks, not admitted mathematical assertions. Their
completion expands the argument DAG; the current DAG is exhaustive for the
formulated bootstrap, not for an as-yet undefined global construction.

| Gate | Prerequisites | Required decision and reviewable output |
|---|---|---|
| DG-CHAR2 | SP-WEYL, SP-EGOROV, F1-REAL, F1-RING, WH-WEIL-a, WH-WEIL-c, WH-WEIL-d; SP-GH08 source audit | Reuse the admitted characteristic-two models. Specify the additional symmetry-lift/phase data; the general splitting conjecture is not an established input |
| DG-REL-LIFT | SP-STAB-REL, SP-SCALAR, SP-CP, FRP-CAT, FRP-CP | Compare the existing scalar-retaining arithmetic source on matched fragments, then choose the required relation enrichment; its higher gates and coefficient restrictions prevent identifying the entire source with pure stabilizer theory |
| DG-RIG | SP-TENSOR, SP-SUM, SP-FOCK | Choose formal additive completion, disjoint unions, or another explicit classical construction; prove distributivity and the quantum comparison without assuming all coherent sums preserve the stabilizer fragment |
| DG-HIGHER | SP-EGOROV, SP-TRACE, FRB-HIERARCHY, FRB-NATURAL; SP-CGK17 | Start from the admitted multiplication/phase families and their d=2 cubic example. The new work is their nonlinear geometric interpretation and any needed extension, with phase precision and composition explicit |
| DG-GLOBAL | SP-PRIME, SP-BC-CONTROL, SP-FROB, SP-SUBSYS, DG-CHAR2, DG-REL-LIFT, DG-RIG | Give the actual inter-prime arithmetic maps and their composition laws; an uncoupled product alone does not define a symplectic Bost–Connes system |
| DG-MODULAR | DG-GLOBAL | Choose a reference state, construct GNS, identify the support and faithfulness conditions, prove the dynamical/KMS relation with its sign and temperature scaling; factor type is an output |
| DG-SPECTRUM | DG-MODULAR | Define the operator, its domain, trace/distribution and arithmetic comparison; separate partition function, implementing spectrum, channel spectrum and zeros |

## First bounded work order — revised for reuse, 2026-09-10

Take **SP-WEYL → SP-EGOROV → SP-TENSOR** as a sequence of explicit
comparisons with admitted results. SP-WEYL already has a structured
corollary draft in `theory/symplectic-phantasm/reuse.md`: F1-REAL applies to
A=(k^n,+), and F1-DUAL/F1-WEYL supply the character and cocycle data.
The new work is symplectic coordinates, the half-form rephasing, the
raw-center quotient, and the trace/unit match. Review that bridge rather
than reopening the finite Stone–von Neumann theorem.

SP-EGOROV then checks the affine action and its projective implementation.
SP-TENSOR uses F1-FUNCT for the configuration-product comparison and adds
the half-form phase and affine naturality checks. Do not depend on
SP-TENSOR to establish SP-WEYL; the admitted F1-FUNCT is a separate node.
The local Gurevich–Hadani sources remain comparison references for a
preferred genuine lift and its oriented, contravariant model conventions.

The exact bridge probes are `theory/checks/phantasm_reuse_check.py`, with
scope and mutations registered beside it. They compare the existing
Abelian implementation with the symmetrized wavefunction, and distinguish
a general relative character from the fixed absolute-trace family.
They do not prove the infinite or categorical claims. All assembled SP
rows stay SKETCH pending their required promotion review.

The Inherited, Reuse and Remaining fields of the argument DAG are the
canonical reuse record. D1701–D1713 have Reuses and Delta fields; the
notation review is summarized in `symplectic-phantasm-reuse.md`. No new
claim or definition numbers were needed for this repair.
