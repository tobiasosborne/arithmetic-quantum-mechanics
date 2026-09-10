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
bounded lemma clusters. The local Weyl/affine/tensor and relation/compact/
stabilizer clusters, scalar/process comparison and coherent/tagged sums are
admitted, together with trace restriction, relative Frobenius and subsystem
decoders, Fock completion, prime assembly and the represented BC control.
The characteristic-two and scalar-retaining interfaces are next, with the
global arithmetic action and reference state as the major construction to earn.

## Construction order and acceptance gates

| Stage | Concrete deliverable | Exit condition |
|---|---|---|
| 0. Ground truth | Primary-source ledger, scope corrections and complete inventory of the note's definition requests | Every named literature lead is either locally verified or an explicit GAP; all sources used in the first cluster are local |
| 1. Local objects and symmetries | Arbitrary-rank finite symplectic spaces, odd-characteristic Weyl algebra, affine Egorov action and direct-sum/tensor comparison | Typed contracts and proofs for SP-WEYL, SP-EGOROV and SP-TENSOR, with rank-zero and rank-one regressions |
| 2. Relations and quantum processes | Affine Lagrangian relations, scalar-quotient stabilizer comparison, actual amplitude and instrument semantics | SP-LREL, SP-COMPACT, SP-STAB-REL, SP-SCALAR and SP-CP; scalar recovery and success probabilities explicitly distinguished |
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
| DG-REL-LIFT | SP-COMPACT, SP-STAB-REL, SP-SCALAR, SP-CP, FRP-CAT, FRP-CP | Compare the existing scalar-retaining arithmetic source on matched fragments, then choose the required relation enrichment; its higher gates and coefficient restrictions prevent identifying the entire source with pure stabilizer theory |
| DG-RIG | SP-TENSOR, SP-SUM, SP-FOCK | Choose formal additive completion, disjoint unions, or another explicit classical construction; prove distributivity and the quantum comparison without assuming all coherent sums preserve the stabilizer fragment |
| DG-HIGHER | SP-EGOROV, SP-TRACE, FRB-HIERARCHY, FRB-NATURAL; SP-CGK17 | Start from the admitted multiplication/phase families and their d=2 cubic example. The new work is their nonlinear geometric interpretation and any needed extension, with phase precision and composition explicit |
| DG-GLOBAL | SP-PRIME, SP-BC-CONTROL, SP-FROB, SP-SUBSYS, DG-CHAR2, DG-REL-LIFT, DG-RIG | Give the actual inter-prime arithmetic maps and their composition laws; an uncoupled product alone does not define a symplectic Bost–Connes system |
| DG-MODULAR | DG-GLOBAL | Choose a reference state, construct GNS, identify the support and faithfulness conditions, prove the dynamical/KMS relation with its sign and temperature scaling; factor type is an output |
| DG-SPECTRUM | DG-MODULAR | Define the operator, its domain, trace/distribution and arithmetic comparison; separate partition function, implementing spectrum, channel spectrum and zeros |

## Stage 1 completed — 2026-09-10

**SP-WEYL → SP-EGOROV → SP-TENSOR** are admitted through
`theory/verdicts/phantasm-stage1-adjudication.md`, following one blind
review and one repair wave per artifact. SP-WEYL is the structured
corollary in `theory/symplectic-phantasm/reuse.md`: F1-REAL applies to
A=(k^n,+), and F1-DUAL/F1-WEYL supply the character and cocycle data.
The bridge supplies symplectic coordinates, half-form rephasing, the
raw-center quotient and trace/unit match, preserving the admitted finite
Stone–von Neumann theorem.

SP-EGOROV proves the affine action and its projective implementation.
SP-TENSOR uses F1-FUNCT for the configuration-product comparison and adds
the half-form phase, affine naturality and projective coherence. Do not depend on
SP-TENSOR to establish SP-WEYL; the admitted F1-FUNCT is a separate node.
The local Gurevich–Hadani sources remain comparison references for a
preferred genuine lift and its oriented, contravariant model conventions.

The exact bridge probes are `theory/checks/phantasm_reuse_check.py`, with
scope and mutations registered beside it. They compare the existing
Abelian implementation with the symmetrized wavefunction, and distinguish
a general relative character from the fixed absolute-trace family.
The new `theory/checks/phantasm_egorov_check.py` supplies exact affine and
tensor naturality probes at its declared scope. Finite passes do not prove
the arbitrary-rank statements. The later relation-cluster admission is
recorded below; the current remaining statuses are in the canonical DAG.
D1703 explicitly extends D9's unitary models and projectivization while
keeping the standard coordinate construction separate.

The Inherited, Reuse and Remaining fields of the argument DAG are the
canonical reuse record. D1701–D1713 have Reuses and Delta fields; the
notation review is summarized in `symplectic-phantasm-reuse.md`. No new
claim or definition numbers were needed for this repair.

## Relation and compact comparison completed — 2026-09-10

SP-LREL, SP-COMPACT and SP-STAB-REL are admitted in that dependency order
through `theory/verdicts/phantasm-relations-adjudication.md`. D1701 now
owns the source monoidal data, D1714 the explicit compact data, and D1715
the stabilizer intertwiner line. The classical conclusions include every
finite field; the constructive quantum equivalence is restricted to odd
prime standard objects modulo all invertible complex scalars. Its zero
class stays separate. The exact source convention comparison is in
`stabilizer-source-comparison.md`.

## Scalar normalization and finite instruments completed — 2026-09-10

SP-SCALAR and SP-CP are admitted through
`theory/verdicts/phantasm-processes-adjudication.md`, reusing FRP-CP's
ordinary-trace matrix calculations. D1706 now owns the outcome-pair order
and ambient trace adjoint. The scalar consequence was corrected after
review: an admissible class-invariant normalization rule can specify a
branch without selecting a representative. The quotient itself stipulates
no rule, and composition compatibility remains a separate obligation.
The instrument theorem does not identify ambient CP equality with
arithmetic-source equality or assert source exhaustion.

## Coherent and tagged sums completed — 2026-09-10

SP-SUM is admitted through `theory/verdicts/phantasm-sum-adjudication.md`.
D1707 owns the arrow realization, typed empty-list maps and ordered-summand
dephasing. The completion realizes all complex linear maps; the tagged
algebra remains the chosen block-diagonal subalgebra. The proof retains
standard coordinates and the block decomposition. It makes no arithmetic
source comparison and does not close DG-RIG.

## Arithmetic interfaces completed — 2026-09-10

SP-TRACE, SP-FROB and SP-SUBSYS are admitted through
`theory/verdicts/phantasm-arithmetic-adjudication.md`, with SP-TRACE admitted
before SP-FROB. D1710 owns the explicit common-character irreducible models,
complement comparison and compatible iterated encodings up to phase.
SP-FROB records SP-CP only for unitary-channel typing. The proof covers
extension degrees divisible by the characteristic and preserves named
character choices. The tensor decoder uses ordinary trace and remains
distinct from a support-code success map.

## Completion controls completed — 2026-09-10

SP-FOCK, SP-PRIME and SP-BC-CONTROL are admitted through
`theory/verdicts/phantasm-completions-adjudication.md`. D1708 owns the
normalized homogeneous exponential formula and its direction; D1711 owns
increasing-prime identity insertion. Written proofs carry the Hilbert and
C*-completions, product-state/GNS construction, maximal logarithmic-operator
domain, point-norm dynamics and Gibbs trace convergence. The prime product
and the represented BC control remain distinct constructions.

All fifteen bootstrap claims are now proved. This does not close the seven
design gates or construct an operator whose spectrum consists of zeta zeros.

## Next bounded work — characteristic two and retained scalars

Use `briefs/phantasm-char2-target.md`, its prepared interface proposal, and
`docs/research-plans/phantasm-char2-source-comparison.md`. Register the new
definitions and claims before proof work. The proposed source retains
cocycle-defect lifts and implementing phases; no splitting is stipulated.
GH08's raw Witt-center kernel must be compared after its chosen character,
not identified by name with the classical affine translation space.

The following scalar-retaining comparison is prepared in
`briefs/phantasm-relation-lift-target.md` and its generator table. It starts
on a named odd-prime arithmetic fragment, preserves coefficient restrictions
and source equality, and does not identify the entire arithmetic source with
pure stabilizer theory. DG-RIG must then specify the compatible additive
construction before DG-GLOBAL supplies actual arithmetic maps and a state.

TJO asked which step would be most consequential after the category work.
The target is one explicit global arithmetic action with a reference state:
its algebra, arithmetic generators, action on local observables and
composition laws must be specified. Calculate that model's dynamics before
claiming any spectral content. The field-extension and subsystem comparisons
reuse admitted local work; a Bost--Connes zeta partition function alone does
not discharge the separate zero-comparison gate.
