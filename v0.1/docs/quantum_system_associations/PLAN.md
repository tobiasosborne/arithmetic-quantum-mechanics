# Quantum-System Association Meta-Plan

Status: user-directed planning scaffold for a systematic catalogue of ways to
associate quantum kinematical systems to an object `X`.

This plan deliberately avoids treating "quantisation" as a canonical functor.
The working phrase is **quantum-system association**: a reproducible workflow
that starts from specified structure on `X`, adds explicitly recorded choices,
and returns kinematical quantum data such as a Hilbert carrier, observable
algebra, Weyl-Heisenberg projective representation, Fock sector, or stabilizer
subspace. Dynamics is out of scope unless a later shard records a separate
principle.

This document is a plan, not a source of mathematical claims. Every eventual
report shard below must cite local sources, existing checked shards,
derivations, tests, or run artifacts before making substantive statements.

## Governing Rules

- Use `association`, `workflow`, or `kinematical construction` for the general
  programme. Use the legacy words `Quant1`, `Quant2`, etc. only as local
  shorthand for families of workflows.
- Each step below gives rise to one report shard. If earlier shards already
  contain the required evidence, the new shard is a review shard that places
  those results in this meta-plan.
- Review shards still need precise local anchors: shard labels, file paths,
  source locators, run bundles, or tests.
- New shards must start with conventions and sources, then a checked example
  or explicitly labelled question/proposal.
- No comparison claim such as "agrees", "reduces", "is equivalent", or
  "degenerates" is finished without a concrete object, a stated convention,
  and a checkable map or invariant.
- Finite examples should be exact whenever feasible. Floating diagnostics are
  not evidence unless the tolerance and independent invariant are recorded.

## Bead And Shard Ledger

The report shard numbers below are reserved planning targets. They may be
renumbered only by updating this plan, `report/README.md`,
`report/SHARD_CATALOG.md`, and `report.tex` in the same change.

| Step | Bead | Planned shard | Kind | Main output |
|---:|---|---|---|---|
| 01 | `aqm-qsa01` | `AQM-65-QSA-VOCABULARY` | New | Vocabulary and non-functoriality contract. |
| 02 | `aqm-qsa02` | `AQM-66-QSA-TEST-OBJECT-CATALOGUE` | New | Standard object list and example matrix skeleton. |
| 03 | `aqm-qsa03` | `AQM-67-QSA-FINITE-SET-FIRST-ASSOCIATION` | New | Formal `C^X` carrier and Gram-choice caveat. |
| 04 | `aqm-qsa04` | `AQM-68-QSA-FINITE-SET-TENSOR-SITES` | Review/New | Tensor-site systems over a finite set. |
| 05 | `aqm-qsa05` | `AQM-69-QSA-FINITE-SET-DIRECT-SUM-PARTICLE` | New | One-particle direct-sum systems. |
| 06 | `aqm-qsa06` | `AQM-70-QSA-AND-OR-MANY-PARTICLE-GRAMMAR` | New | Tensor/direct-sum grammar and finite-particle sectors. |
| 07 | `aqm-qsa07` | `AQM-71-QSA-SYMPLECTIC-FIELD-LABELS-SET` | Review | `Map(X,V)`, radicals, Weyl labels, and qudits. |
| 08 | `aqm-qsa08` | `AQM-72-QSA-BOSON-FERMION-LAYER` | Review/New | Bosonic, fermionic, and Grassmann-Weyl review plus gaps. |
| 09 | `aqm-qsa09` | `AQM-73-QSA-FUSION-CATEGORY-ENDPOINT` | New gap shard | Fusion-category endpoint requirements and deferral. |
| 10 | `aqm-qsa10` | `AQM-74-QSA-SINGLE-PARTICLE-REDUCTION` | New | Conditions under which field/tensor systems reduce to one-particle systems. |
| 11 | `aqm-qsa11` | `AQM-75-QSA-WHAT-COUNTS-AS-A-POINT` | Review/New | Underlying, rational, closed, generic, and scheme-point choices. |
| 12 | `aqm-qsa12` | `AQM-76-QSA-COTANGENT-FIRST-ASSOCIATION` | New | Cotangent phase-label workflow for geometric objects. |
| 13 | `aqm-qsa13` | `AQM-77-QSA-INTRINSIC-RELATIVE-COTANGENT` | New | Intrinsic/local versus relative cotangent data for `Spec R`. |
| 14 | `aqm-qsa14` | `AQM-78-QSA-FINITE-PHASE-WEYL-KINEMATICS` | Review/New | Weyl-Heisenberg kinematics after finite symplectic labels are fixed. |
| 15 | `aqm-qsa15` | `AQM-79-QSA-GEOMETRIC-FIELD-HOM-X-V` | Review | Geometric field spaces, sheaf sections, and local nets. |
| 16 | `aqm-qsa16` | `AQM-80-QSA-FINITE-RING-EXAMPLE-MATRIX` | New | Cross-workflow table for the standard finite rings. |
| 17 | `aqm-qsa17` | `AQM-81-QSA-RESIDUE-FIELD-SITE-ASSOCIATION` | Review/New | Residue-field sites for `Spec R` and variable residue fields. |
| 18 | `aqm-qsa18` | `AQM-82-QSA-NILPOTENT-SENSITIVE-ASSOCIATION` | Review/New | Thickened and Frobenius-ring layers versus reduced residue sites. |
| 19 | `aqm-qsa19` | `AQM-83-QSA-PRODUCT-RINGS-TENSOR-FACTORS` | Review | Product spectra, tensor factors, and product-ring edge cases. |
| 20 | `aqm-qsa20` | `AQM-84-QSA-INFINITE-RING-BOUNDARIES` | Review/New | Finite-support, quasi-local, and generic-point boundary cases. |
| 21 | `aqm-qsa21` | `AQM-85-QSA-AGREEMENT-INEQUIVALENCE-TABLE` | New | Synthesis table of agreement, inequivalence, and required choices. |
| 22 | `aqm-qsa22` | `AQM-86-QSA-DEGENERATE-OVERRESTRICTIVE-CASES` | New | Catalogue of collapsed, radical, too-small, and unsupported cases. |
| 23 | `aqm-qsa23` | `AQM-87-QSA-OPEN-PROBLEMS-NEXT-TARGETS` | New | Open problems and next catalogue targets. |

## Standard Example Families

The first catalogue should stay small enough for exact checking while still
separating the main phenomena:

- structureless finite sets with `|X| = 0, 1, 2, 3, n`;
- `k = F_3` as the running prime field;
- finite products `k^n`;
- dual numbers `k[e]/(e^2)`;
- quotient examples already used in the report, including polynomial
  quotient and thickened examples over `F_3`;
- `Z/6Z` and selected `Z/nZ` examples already present in the finite-ring
  database MVP;
- candidate two-direction local Artin examples such as quotients of
  `k[x,y]`, after a local source or exact derivation fixes the intended ideal;
- infinite boundary examples already present in the report, including
  `F_q[t]`, `F_q[x,y]`, and `Spec Z`.

If a proposed example collapses to an earlier one, the report should treat it
as a degenerate test case only after a local derivation or source anchor records
the collapse.

## Step Details

### Step 01: Association Vocabulary And Non-Functoriality

Goal: fix the language of the programme before technical comparisons begin.

Required shard content:

- distinguish quantum-system association from a canonical functorial
  quantisation claim;
- define local shorthand `Quant1`, `Quant2`, `field association`,
  `single-particle sector`, `association equivalence`, and `degenerate case`;
- record that dynamics is a later choice, not part of the kinematical output;
- state the evidence rule for every future comparison.

Acceptance:

- `CONVENTIONS.md` contains the vocabulary convention;
- the shard is explicitly a planning/convention shard;
- no mathematical equivalence is asserted without a later checked step.

### Step 02: Test Object Catalogue

Goal: freeze the first object list used by every comparison shard.

Required shard content:

- finite-set examples;
- finite-ring examples over `F_3`;
- selected product, nilpotent, quotient, and mixed-characteristic examples;
- natural infinite boundary examples;
- for each object, the planned workflows to evaluate and the local evidence
  still needed.

Acceptance:

- every object has a precise presentation or is marked as a question;
- each object points to an existing shard, finite-ring database helper, source,
  or planned derivation;
- ambiguous examples are not silently normalized.

### Step 03: Structureless Finite Set First Association

Goal: work out the minimal `C^X` association for a finite set.

Required shard content:

- define the formal carrier with basis labels indexed by `X`;
- record that an inner product/Gram matrix is an extra choice unless a later
  principle is supplied;
- treat the empty, one-point, and `n`-point cases.

Acceptance:

- no canonical Hilbert-space inner product is claimed from the set alone;
- every displayed inner product choice is labelled as extra data.

### Step 04: Structureless Finite Set Tensor-Site Association

Goal: systematize the "independent site" workflow.

Required shard content:

- choose one Hilbert space or observable algebra per site;
- form the finite tensor product and local observable inclusions;
- compare the uniform finite-qudit case with existing arithmetic-field shards.

Existing anchors:

- `AQM-14-ARITHMETIC-QUANTUM-FIELDS`;
- `AQM-22-PRIME-FIELD-ARITHMETIC-FIELDS-QUDIT-PAULIS`;
- `AQM-24-ZARISKI-OPENS-OBSERVABLE-NETS`;
- `AQM-25-QUASILOCAL-ZARISKI-ALGEBRA`.

Acceptance:

- arbitrary choices of `H_x` are explicit;
- review claims cite the exact prior shard or run artifact.

### Step 05: Structureless Finite Set Direct-Sum Particle Association

Goal: systematize the "one particle at one of many positions" workflow.

Required shard content:

- choose one internal Hilbert space per site;
- form the direct sum over sites;
- compare the special case of one-dimensional internal spaces with Step 03.

Acceptance:

- the tensor-site and direct-sum constructions are not conflated;
- agreement with Step 03 is proved only under stated choices.

### Step 06: AND/OR Many-Particle Grammar

Goal: catalogue finite combinations of tensor and direct-sum operations.

Required shard content:

- define finite grammar operations corresponding to independent coexistence
  and alternatives;
- identify finite particle-number sectors;
- separate this elementary grammar from symmetric, antisymmetric, para, and
  fusion-category enhancements.

Acceptance:

- the grammar is expressed through explicit finite Hilbert-space operations;
- any infinite-particle or completion issue is deferred.

### Step 07: Finite Symplectic Field Labels On A Set

Goal: review the already developed finite-field label-space workflow.

Required shard content:

- `Map(X,V)` or finite-support variants;
- pointwise symplectic pairing and radical quotient;
- Weyl-Heisenberg labels and finite qudit carriers;
- concrete `F_3` examples already checked.

Existing anchors:

- `AQM-14-ARITHMETIC-QUANTUM-FIELDS`;
- `runs/2026-05-24-arithmetic-quantum-fields/`;
- `AQM-22-PRIME-FIELD-ARITHMETIC-FIELDS-QUDIT-PAULIS`.

Acceptance:

- this is a review shard unless it introduces a new example;
- all finite counts point to CSV rows or prior checked shards.

### Step 08: Bosonic And Fermionic Association Layer

Goal: place the canonical bosonic and fermionic work into the association
catalogue.

Required shard content:

- review finite bosonic association via real symplectic map spaces where
  already sourced;
- review fermionic CAR and Grassmann-Weyl displacement material where already
  sourced;
- state what is not yet covered: parafermions and fusion-category variants.

Existing anchors:

- `AQM-19-CANONICAL-BOSON-FERMION-FIELD-COMPARISON`;
- `AQM-20-GRASSMANN-WEYL-FERMION-DISPLACEMENTS`;
- `AQM-21-GRASSMANN-WEYL-FERMION-DERIVATIONS`;
- `references/canonical_fields/SOURCES.md`;
- `references/supergeometry/SOURCES.md`.

Acceptance:

- review statements keep the prior source locators;
- unsupported variants are listed as gaps, not results.

### Step 09: Fusion-Category Endpoint

Goal: record the endpoint without pretending it has been developed.

Required shard content:

- explain the intended role of fusion categories as a future association
  family;
- list the required source/convention decisions for hom spaces, simple
  objects, tensor products, pivotal or spherical structure, and lattice model
  data;
- explicitly defer Levin-Wen/string-net technical claims.

Acceptance:

- no fusion-rule, `F`-symbol, or Levin-Wen Hamiltonian claim appears without a
  registered source;
- the shard is a gap shard.

### Step 10: Single-Particle Reduction

Goal: make precise when a field/tensor/Fock association reduces to a
first-association or direct-sum association.

Required shard content:

- define "single-particle sector" for the finite constructions in Steps 04-08;
- prove the comparison for finite direct sums and tensor/Fock sectors under
  stated choices;
- identify failures caused by internal Hilbert spaces, statistics, phases, or
  missing canonical inner products.

Acceptance:

- every reduction is a map between explicitly defined carriers;
- every non-reduction has a concrete obstruction.

### Step 11: What Counts As A Point

Goal: make the point-selection problem explicit before using geometry.

Required shard content:

- compare underlying set, rational points, closed points, generic points, and
  all scheme points as indexing choices;
- review existing closed-point conventions for finite Weyl sites;
- identify which choices lead to finite kinematical systems.

Existing anchors:

- `AQM-22`, `AQM-23`, `AQM-28`, `AQM-29`, `AQM-30`, and `AQM-45`.

Acceptance:

- each point convention states the class of objects where it is used;
- no generic-point representation convention is silently assumed.

### Step 12: Cotangent-Based First Association

Goal: develop the geometric `Quant1` branch.

Required shard content:

- choose a point convention;
- attach tangent and cotangent data;
- form a finite phase-label space where possible;
- state the symplectic form or the missing choice needed to obtain one.

Existing anchors:

- `AQM-58` through `AQM-63`.

Acceptance:

- tangent/cotangent definitions are sourced or derived locally;
- the symplectic pairing is explicit before any Weyl representation is used.

### Step 13: Intrinsic Versus Relative Cotangent Data

Goal: compare two legitimate cotangent choices for `Spec R`.

Required shard content:

- local/intrinsic cotangent data at a point;
- relative cotangent data such as Kaehler differentials over a base;
- examples where the two agree, differ, or one vanishes;
- implications for the associated phase-label space.

Acceptance:

- the base ring and point convention are explicit in every example;
- comparisons are backed by exact calculations or local sources.

### Step 14: Weyl-Heisenberg Kinematics From Finite Phase Spaces

Goal: consolidate the common representation-theoretic step.

Required shard content:

- once a finite symplectic label space is fixed, state the local
  Weyl-Heisenberg construction used in this project;
- separate prime-field, finite-field, finite-Frobenius-ring, and unresolved
  general finite-ring cases;
- identify where projective representation classification is already sourced.

Existing anchors:

- `AQM-31-WEYL-HEISENBERG-RESEARCH-STATUS-RINGS`;
- `references/heisenberg_weil/SOURCES.md`;
- `references/symplectic_qecc/SOURCES.md`.

Acceptance:

- the shard does not claim a complete classification over all finite rings
  unless a local source supports it;
- unresolved cases remain labelled as questions.

### Step 15: Geometric Field Association `Hom(X,V)`

Goal: review the geometric field branch under the meta-plan.

Required shard content:

- review finite point maps, closed-point residue fields, sheaf-section
  replacements, radicals, and observable nets;
- identify where the structure of `X` constrains the allowed field space;
- separate all-map, finite-support, sheaf-section, and regular-function
  choices.

Existing anchors:

- `AQM-14` through `AQM-18`;
- `AQM-24` through `AQM-30`;
- `AQM-49` through `AQM-52`.

Acceptance:

- this is primarily a review shard;
- every restriction of `Hom(X,V)` is tied to a convention or prior shard.

### Step 16: Finite Ring Example Matrix

Goal: create the central comparison table for the finite commutative ring zoo.

Required shard content:

- one row per standard ring;
- columns for points, residue fields, cotangent data, field-label data,
  nilpotent-sensitive data, and available run artifacts;
- explicit markers for unknown, blocked, degenerate, or not-applicable cases.

Existing anchors:

- finite-ring database PRD and population plan;
- `runs/2026-05-26-finite-ring-database/`;
- `CONVENTIONS.md` convention `(an)`.

Acceptance:

- no row claims a populated/audited finite-ring database until that exists;
- the table uses explicit sentinel labels for gaps.

### Step 17: Residue-Field Site Association For `Spec R`

Goal: generalize the residue-field site workflow for finite rings.

Required shard content:

- for each prime or maximal point used, attach its residue field;
- allow the target symplectic space to vary over residue fields;
- form the direct sum of local phase spaces and the resulting tensor carrier
  when finite-field Weyl data are available.

Existing anchors:

- `AQM-23-SPEC-Z6-RESIDUE-QUDIT-FACTORISATION`;
- `AQM-34` through `AQM-40`;
- finite-ring database residue quantisation helpers.

Acceptance:

- variable residue-field dimensions are explicit;
- reduced residue-site and nilpotent-sensitive layers remain separate.

### Step 18: Nilpotent-Sensitive Association

Goal: compare the reduced residue-site model with thickened ring data.

Required shard content:

- review Artin-ring/thickened Weyl examples already developed;
- state the additional character/Frobenius-ring data needed beyond reduced
  residue fields;
- compare `k[e]/(e^2)`-style examples with their reduced point.

Existing anchors:

- `AQM-36-NILPOTENT-THICKENING-WEYL-FIELDS`;
- `AQM-37-THICKENED-TN-EQUALS-1-EXAMPLES`;
- `AQM-31` for finite-ring representation status.

Acceptance:

- nilpotents are not counted as extra points unless a convention says so;
- thickened carriers cite their generating-character or obstruction status.

### Step 19: Product Rings And Tensor Factorization

Goal: review how product rings produce independent tensor factors.

Required shard content:

- review product spectra and finite product-field examples;
- compare product decompositions with tensor-site constructions;
- include edge cases where cotangent data vanish or differ from residue-site
  data.

Existing anchors:

- `AQM-40-PRODUCT-FIELD-SPECTRUM-QUDIT-STABILIZERS`;
- `AQM-58-PRODUCT-RINGS-REAL-LINE-COTANGENT`;
- finite-ring database product constructors.

Acceptance:

- product-ring tensor factorization is stated only for the selected
  association workflow;
- no universal equivalence of workflows is implied.

### Step 20: Infinite Ring Boundary Cases

Goal: mark the boundary between finite examples and infinite schemes.

Required shard content:

- review `F_q[t]`, `F_q[x,y]`, and `Spec Z` shards;
- separate finite supports, quasi-local algebras, incomplete tensor products,
  and generic-point caveats;
- state what representation conventions are missing for infinite residue
  fields or analytic completions.

Existing anchors:

- `AQM-29`, `AQM-30`, `AQM-45`, and `AQM-48`.

Acceptance:

- every infinite construction states whether it is finite-support,
  quasi-local, or a completion proposal;
- generic points do not become finite Weyl sites by default.

### Step 21: Agreement And Inequivalence Table

Goal: synthesize the comparison results.

Required shard content:

- rows for each standard object;
- columns for the association workflows;
- explicit maps/invariants witnessing agreement;
- explicit obstructions witnessing inequivalence.

Acceptance:

- the table contains no unsupported equivalence claims;
- every agreement or inequivalence links to the proving shard or run artifact.

### Step 22: Degenerate And Over-Restrictive Cases

Goal: catalogue failure modes as useful evidence.

Required shard content:

- collapsed quotient examples;
- radical symplectic forms and quotient label spaces;
- too-little-structure cases such as a bare finite set without a Gram choice;
- unsupported finite-ring or infinite-representation cases;
- distinctions between zero, empty, blocked, and not-applicable outputs.

Acceptance:

- every failure mode has a concrete example;
- degenerate cases are not silently removed from the catalogue.

### Step 23: Open Problems And Next Catalogue Targets

Goal: close the meta-plan with a prioritized gap list.

Required shard content:

- parafermions and fusion categories;
- noncommutative or nonunital rings;
- analytic manifolds and completions;
- dynamics-selection principles;
- finite-ring representation classification gaps;
- database population and audit dependencies.

Acceptance:

- open problems are phrased as questions or proposals;
- every next target names the missing source, convention, computation, or run.

## Subagent Briefing Protocol

For each step, the assigned subagent should:

1. Read `AGENTS.md`, `CONVENTIONS.md`, this plan, and the relevant existing
   shards listed in the step.
2. Treat the step as a readiness review unless explicitly asked to edit files.
3. Produce a short brief with:
   - local anchors already available;
   - missing sources or conventions;
   - concrete finite examples to check;
   - likely risks or hidden equivalence assumptions;
   - whether the shard should be review, new derivation, or gap-only.
4. Make no mathematical, physical, or numerical claim from memory.
5. Raise a new bead only when a genuinely separate blocker or source-acquisition
   task is discovered.
