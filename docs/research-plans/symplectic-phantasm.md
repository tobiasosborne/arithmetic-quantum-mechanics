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
2. Fix a small definition layer. Every object, Hom-set, composition, unit,
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
contract checker. No theorem prover, CI service, repeated review campaign,
or speculative taxonomy is required. Contract checks validate references,
types as declared, dependency order and evidence/status consistency. They
cannot decide whether a proof is mathematically correct.

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
| DG-CHAR2 | SP-WEYL, SP-EGOROV; SP-GH08 source audit | Specify characteristic-two phase/central-extension data and compatibility with the odd-prime package; retain the existing characteristic-two claims at their present scope |
| DG-REL-LIFT | SP-STAB-REL, SP-SCALAR, SP-CP | Choose a decorated relation or circuit presentation retaining amplitudes, zero maps and probabilities; state normalization/composition laws and compare exactly with the scalar-quotient source |
| DG-RIG | SP-TENSOR, SP-SUM, SP-FOCK | Choose formal additive completion, disjoint unions, or another explicit classical construction; prove distributivity and the quantum comparison without assuming all coherent sums preserve the stabilizer fragment |
| DG-HIGHER | SP-EGOROV, SP-TRACE; SP-CGK17 | Specify polynomial functions and phase precision, finite-field polynomial identities, allowed nonlinear data and composition closure; first work one cubic phase example, then decide the correct general claim |
| DG-GLOBAL | SP-PRIME, SP-BC-CONTROL, SP-FROB, SP-SUBSYS, DG-CHAR2, DG-REL-LIFT, DG-RIG | Give the actual inter-prime arithmetic maps and their composition laws; an uncoupled product alone does not define a symplectic Bost–Connes system |
| DG-MODULAR | DG-GLOBAL | Choose a reference state, construct GNS, identify the support and faithfulness conditions, prove the dynamical/KMS relation with its sign and temperature scaling; factor type is an output |
| DG-SPECTRUM | DG-MODULAR | Define the operator, its domain, trace/distribution and arithmetic comparison; separate partition function, implementing spectrum, channel spectrum and zeros |

## First bounded work order

After this bootstrap is registered, take **SP-WEYL → SP-EGOROV → SP-TENSOR**.
The product is a checked local quantization contract for arbitrary rank,
with a worked one-qudit and two-qudit example. Use the canonical algebra
assignment and projective unitary implementers first; any preferred genuine
Hilbert-space lift is an additional comparison with Gurevich–Hadani's
oriented models, including their contravariant convention.

Preread the local SP-GH07, SP-GH09 and SP-PRASAD09 source locators, the
definitions listed in the DAG, and the existing rank-one conventions in D3 and D4.
Write the exact falsifier expectations before the proof lands. The proof
must identify the rank-one specialization with the current Weyl conventions,
include the zero-dimensional unit, and verify the affine semidirect-product
law and monoidal coherence. Do not add all-prime assembly or higher gates
to this first work order.

The source and definition bootstrap makes no claim promotion. Subsequent
agents record completed nodes, residual scope and the next ready node in
`HANDOFF.md`, preserving the single statements in the canonical claim table.
