# Symplectic Phantasm argument DAG

Canonical statements and statuses live in `claims/CLAIMS.md`. This file
holds the typed contracts and construction outlines for the formulated
bootstrap. Every outline is SKETCH, not an admitted proof. The source audit
is `docs/research-plans/symplectic-phantasm-sources.md`; the staged work order
and unformulated global decision gates are in
`docs/research-plans/symplectic-phantasm.md`.

Run `python3 theory/checks/phantasm_contract_check.py`. It checks the schema,
reference resolution, dependency acyclicity, local source hashes, status and
evidence requirements, and exact statement/definition restatements in the
labbook. Input/output contracts are explicit human-readable mathematical
types; this is not a symbolic type checker or proof assistant. A green run
does not promote a claim.

A node may be drafted before its dependencies are proved, provided every
such dependency stays explicit. It may be promoted only when its proof and
review cover the exact statement and its mathematical dependencies are
PROVED (or explicitly carried as hypotheses of a separately formulated
conditional claim). Proposed falsifiers below have not yet been implemented
or run; they must never be reported as test evidence.

For promotion, fill Proof and Review with real repository paths, replace
Checks with real executable checker paths, and record an adjudication
containing `Admitted: <claim-id>`. Evidence must say `admitted`; the proof
must have a structured QED. Mechanical checks establish only that these
records exist and agree. Human mathematical review remains indispensable.

<!-- PHANTASM-ORDER-BEGIN -->
| claim | stage | priority |
|---|---|---|
| SP-WEYL | 1 | 1 |
| SP-EGOROV | 1 | 2 |
| SP-TENSOR | 1 | 3 |
| SP-LREL | 2 | 4 |
| SP-STAB-REL | 2 | 5 |
| SP-SCALAR | 2 | 6 |
| SP-CP | 2 | 7 |
| SP-SUM | 3 | 8 |
| SP-FOCK | 3 | 9 |
| SP-TRACE | 4 | 10 |
| SP-FROB | 4 | 11 |
| SP-SUBSYS | 4 | 12 |
| SP-PRIME | 5 | 13 |
| SP-BC-CONTROL | 5 | 14 |
<!-- PHANTASM-ORDER-END -->

## Decision gates extending the graph

These are OPEN research tasks, not mathematical claims. Their dependencies
and source identifiers are checked with the lemma DAG. Each completed gate
must register its output definitions and newly formulated lemmas before a
downstream mathematical assertion is admitted. Full work orders appear in
`docs/research-plans/symplectic-phantasm.md`.

| decision | dependencies | sources | required output | state |
|---|---|---|---|---|
| DG-CHAR2 | SP-WEYL,SP-EGOROV | SP-GH08 | Characteristic-two central-extension and phase datum with comparison contracts | OPEN |
| DG-REL-LIFT | SP-STAB-REL,SP-SCALAR,SP-CP | SP-CK21,SP-BC24,SP-WAT18 | Actual normalized relation/circuit presentation and composition laws | OPEN |
| DG-RIG | SP-TENSOR,SP-SUM,SP-FOCK | SP-CK21,SP-DER06,SP-JOY81 | Classical additive construction and both-product coherence contracts | OPEN |
| DG-HIGHER | SP-EGOROV,SP-TRACE | SP-CGK17,SP-GROSS06 | Phase-precision-aware higher-gate datum and a typed cubic example | OPEN |
| DG-GLOBAL | SP-PRIME,SP-BC-CONTROL,SP-FROB,SP-SUBSYS,DG-CHAR2,DG-REL-LIFT,DG-RIG | SP-CM04,SP-CCM07,SP-CM08 | Actual inter-prime arithmetic maps, their relations and a global algebra definition | OPEN |
| DG-MODULAR | DG-GLOBAL | SP-CM08,SP-CCM07 | Reference, GNS support, faithfulness and a precise flow/KMS comparison contract | OPEN |
| DG-SPECTRUM | DG-MODULAR | SP-CC09,SP-CCM07 | Operator, domain, trace or distribution and a formulated arithmetic comparison | OPEN |

## SP-WEYL

- Title: Arbitrary-rank Weyl realization
- Status: SKETCH
- Stage: 1
- Definitions: D4,D1701,D1703
- Dependencies: none
- Sources: SP-GH07,SP-PRASAD09,SP-GROSS06
- Inputs: (k,V,omega,psi) with p odd; standard model additionally has symplectic coordinates
- Output: A finite matrix *-algebra, normalized trace and projective unitary model
- Choices: Nontrivial character and any model coordinates; half-form normalization
- Scope: Odd characteristic only; no preferred abstract-space basis or genuine symmetry lift is asserted.
- Proof: none
- Review: none
- Checks: none
- Evidence: planned

**Construction outline.** Check the bilinear cocycle and adjoint identities; prove character orthogonality and trace orthogonality of the displayed operators. Count the basis, identify the full matrix algebra, and specialize the primary Stone–von Neumann argument. Compare the actual rank-one cocycle with D4.

**Falsifier to implement.** Exact roots-of-unity comparisons for p=3,5, ranks 0,1,2, plus F9 rank one; measure basis rank and commutators independently.

**Required mutations.** Replace the nontrivial character by the trivial character; flip the half-form sign only in the model; omit the rank-zero unit.

## SP-EGOROV

- Title: Affine symmetries and projective implementation
- Status: SKETCH
- Stage: 1
- Definitions: D1701,D1703
- Dependencies: SP-WEYL
- Sources: SP-GH07,SP-GH09,SP-GROSS06
- Inputs: Affine symplectic arrow (t,g):V->W over fixed (k,psi)
- Output: alpha_(t,g):A(V)->A(W); projective unitary H(V)->H(W)
- Choices: The common character; model choices; no unrecorded phase section
- Scope: This is a covariant algebra functor and a projective implementation statement. Choosing a genuine linear lift is a separate comparison.
- Proof: none
- Review: none
- Checks: none
- Evidence: planned

**Construction outline.** Substitute into the two Weyl products, then compute the phase under (s,h) after (t,g). Apply matrix-algebra implementation and uniqueness from SP-WEYL. Translate the contravariant Gurevich–Hadani convention by inversion on isomorphisms.

**Falsifier to implement.** Enumerate the affine group on F3^2; check the semidirect-product law and both translation and Fourier/shear covariance.

**Required mutations.** Drop the translated phase or reverse the order of the semidirect product.

## SP-TENSOR

- Title: Symplectic sum and quantum tensor compatibility
- Status: SKETCH
- Stage: 1
- Definitions: D1701,D1703
- Dependencies: SP-WEYL,SP-EGOROV
- Sources: SP-GH07,SP-GH09
- Inputs: Pairs and triples of symplectic spaces and affine arrows over fixed (k,psi)
- Output: A(V+W) -> A(V) tensor A(W), natural with the affine action
- Choices: The common character and standard tensor-coordinate ordering
- Scope: The source operation is symplectic direct sum. This does not construct a coherent additive completion of the classical category.
- Proof: none
- Review: none
- Checks: none
- Evidence: planned

**Construction outline.** Factor the cocycle and coefficient trace. Check all coherence diagrams on a spanning Weyl tensor, then pass to irreducible models using uniqueness up to phase.

**Falsifier to implement.** Use three F3 rank-one registers and the zero register; test generator tensors and flips by exact arithmetic.

**Required mutations.** Drop one tensor factor phase, interchange only one coordinate ordering, or replace the unit by a qudit.

## SP-LREL

- Title: Composition of affine Lagrangian relations
- Status: SKETCH
- Stage: 2
- Definitions: D1701,D1702
- Dependencies: none
- Sources: SP-W09,SP-LW14,SP-CK21
- Inputs: R:V->W and S:W->Z; symplectic spaces over one finite field
- Output: S o R:V->Z in the same relation class; product and dagger laws
- Choices: Minus sign on the source form and explicit coordinate reordering
- Scope: This concerns finite linear/affine geometry, including empty relations. It does not assert a normalized quantization of those relations.
- Proof: none
- Review: none
- Checks: none
- Evidence: planned

**Construction outline.** Reduce the product relation along the diagonal in the middle space. Prove the dimension/isotropy statement by annihilators and kernel counting; translate the affine case to the linear case when nonempty. Use ordinary relation composition for associativity.

**Falsifier to implement.** Enumerate affine Lagrangians in F2^2 and F3^2 and small zero/one-register Hom-sets; compare image dimensions and existential composition by independent enumeration.

**Required mutations.** Use the positive form on both source and target; discard empty composites; use a universal instead of existential middle-point condition.

## SP-STAB-REL

- Title: The scalar-quotient stabilizer comparison
- Status: SKETCH
- Stage: 2
- Definitions: D1701,D1702,D1703,D1704,D1705
- Dependencies: SP-LREL,SP-WEYL,SP-EGOROV,SP-TENSOR
- Sources: SP-CK21,SP-BC24
- Inputs: Standard affine relation prop over F_p; p an odd prime
- Output: Equivalence to the scalar-quotient stabilizer prop
- Choices: Generator conventions, Fourier sign and the C^times quotient including a separate zero
- Scope: The comparison is modulo all invertible complex scalars and is only formulated here for prime fields. It is not a probability-preserving instrument functor.
- Proof: none
- Review: none
- Checks: none
- Evidence: planned

**Construction outline.** Transcribe the source presentation and its generator map; match its Weyl/Clifford normalization to ours. Verify defining relations, fullness and faithfulness with the source theorem at its exact scalar scope.

**Falsifier to implement.** Check the source generators for p=3,5, with state/effect composites, including one zero composite and two distinct nonzero norms representing the same class.

**Required mutations.** Identify zero with a nonzero scalar; compare normed representatives as if the quotient were phase-only.

## SP-SCALAR

- Title: Scalar normalization
- Status: SKETCH
- Stage: 2
- Definitions: D1704,D1705,D1706
- Dependencies: none
- Sources: SP-WAT18,SP-CK21
- Inputs: An actual finite linear map T:H->K and a scalar c
- Output: The typed branch Phi_T:End(H)->End(K) and its probability scaling
- Choices: Actual representative and norm; ordinary trace
- Scope: Zero outcomes are retained and never conditionally normalized. This describes the additional data for an operational lift, not a claimed canonical choice of that data.
- Proof: none
- Review: none
- Checks: none
- Evidence: planned

**Construction outline.** Apply the Kraus criterion and trace duality; test the inequality against all pure states. Compute the scalar factor before taking a quotient.

**Falsifier to implement.** Use identity, a rank-one projection and scalar multiples 0,1/2,2 on a qutrit; compare successful probabilities with trace directly.

**Required mutations.** Treat a factor 2 as a phase; normalize a zero-probability branch.

## SP-CP

- Title: Closure and normalization of finite instruments
- Status: SKETCH
- Stage: 2
- Definitions: D1706
- Dependencies: none
- Sources: SP-WAT18
- Inputs: Finite systems H,K,L and typed Kraus branches/instruments
- Output: Composed/tensored branches, channels, retained instruments and contravariant adjoints
- Choices: Ordinary block trace and explicit outcome labels
- Scope: This is an ambient process theorem. It makes no claim that arithmetic or stabilizer generators exhaust these maps.
- Proof: none
- Review: none
- Checks: none
- Evidence: planned

**Construction outline.** Use the Choi/Kraus criterion block by block. Compose Kraus operators, sum normalization operators and keep the outcome indexing; derive the adjoint using the nondegenerate trace pairing.

**Falsifier to implement.** Exact rational Kraus examples on one and two matrix blocks, including preparation, discard, branching and a non-unital state channel.

**Required mutations.** Use normalized trace in only one system; erase one outcome before summing; reverse a Kraus-adjoint factor.

## SP-SUM

- Title: Coherent sums and tagged quantum systems
- Status: SKETCH
- Stage: 3
- Definitions: D1704,D1706,D1707
- Dependencies: SP-WEYL,SP-SCALAR,SP-CP
- Sources: SP-CK21,SP-WAT18
- Inputs: Lists of actual stabilizer model Hilbert spaces and amplitude maps
- Output: Full coherent matrix maps and the separate tagged subalgebra/dephasing
- Choices: Block decomposition; actual scalar representatives before linear span
- Scope: Adding coherent linear combinations enlarges the pure stabilizer fragment. A classical rig source is still to be constructed.
- Proof: none
- Review: none
- Checks: none
- Evidence: planned

**Construction outline.** Construct each matrix unit from computational preparations, effects and Weyl translations. Count all matrix entries, identify the diagonal blocks and write the dephasing Kraus projections.

**Falsifier to implement.** For H=C plus C^3, compare dimensions 16 and 10 and a cross-block coherent observable; verify dephasing removes exactly off-diagonal blocks.

**Required mutations.** Replace the coherent algebra by its tagged subalgebra; claim arbitrary coherent sums stay within the uncompleted stabilizer morphisms.

## SP-FOCK

- Title: Fock completion and the exponential law
- Status: SKETCH
- Stage: 3
- Definitions: D1708
- Dependencies: none
- Sources: SP-DER06
- Inputs: Hilbert spaces, contractions and the Hilbert Fock completion
- Output: A bounded functor, natural exponential unitary and explicit vacuum/one-mode controls
- Choices: Hilbert tensor normalization; contraction domain; vacuum sector
- Scope: Infinite boundedness and the completion require written arguments. No equivalence between an unspecified classical free monoid and this Hilbert construction is asserted.
- Proof: none
- Review: none
- Checks: none
- Evidence: planned

**Construction outline.** Prove norm bounds on every sector and take the Hilbert direct sum. Construct the exponential unitary with the binomial normalization and check dense finite-particle vectors, then extend by continuity.

**Falsifier to implement.** Compute symmetrizers and norms through particle number four for one and two modes; distinguish the zero space from C.

**Required mutations.** Omit the binomial square root, remove the vacuum, or extend a norm-2 map as though its second quantization were bounded.

## SP-TRACE

- Title: Restriction of scalars preserves the Weyl datum
- Status: SKETCH
- Stage: 4
- Definitions: D1701,D1703,D1709
- Dependencies: SP-WEYL
- Sources: SP-STFIELD,SP-PRASAD09
- Inputs: E/K, an E-symplectic space and a nontrivial K-character
- Output: An underlying K-symplectic space and exact equality of the labelled Weyl products
- Choices: The field embedding defining E/K and the K-character
- Scope: The extension degree may be divisible by the characteristic. This is restriction of scalars with a trace form, not the uncorrected inclusion of a subfield as a symplectic subsystem.
- Proof: none
- Review: none
- Checks: none
- Evidence: planned

**Construction outline.** Use the separable trace pairing to test each nonzero vector against a scaled partner. Apply trace transitivity and commute division by two with trace; check equality on every basis product.

**Falsifier to implement.** Use F9/F3 and F27/F3, including degree three in characteristic three; compare trace matrices and character exponents.

**Required mutations.** Replace trace by multiplication by the extension degree; use the restriction of psi_E to K as though it were always nontrivial.

## SP-FROB

- Title: Named arithmetic Frobenius covariance
- Status: SKETCH
- Stage: 4
- Definitions: D1703,D1709
- Dependencies: SP-WEYL,SP-EGOROV,SP-TRACE
- Sources: SP-STFIELD,SP-GH07
- Inputs: A standard E-register and relative Frobenius over K
- Output: Symplectic automorphism, exact unitary covariance and invertible channel
- Choices: Coordinates and relative base field; trace-normalized character
- Scope: A smaller period is allowed. Abstract spaces require named semilinear data; Frobenius is not identified with partial trace.
- Proof: none
- Review: none
- Checks: none
- Evidence: planned

**Construction outline.** Use invariance of field trace under relative Frobenius, then apply the permutation to the displayed Schrödinger formula. Check the iterate on field elements.

**Falsifier to implement.** Enumerate covariance in F9/F3 and F27/F3; include both fixed and nonfixed labels.

**Required mutations.** Replace conjugation by a partial trace or apply the Frobenius to only half the phase coordinates.

## SP-SUBSYS

- Title: Subsystem inclusion and its dual decoder
- Status: SKETCH
- Stage: 4
- Definitions: D1701,D1703,D1706,D1710
- Dependencies: SP-WEYL,SP-TENSOR,SP-CP
- Sources: SP-WAT18,SP-STFIELD
- Inputs: Symplectic injection j and compatible model unitary J
- Output: iota_J:End(H_U)->End(H_V), dual D_J in the opposite direction
- Choices: Model unitary modulo overall phase; compatible tensor identifications in towers
- Scope: The complement and Weyl model compatibility must be verified. Generic field embeddings and coordinate traces are not automatically such injections.
- Proof: none
- Review: none
- Checks: none
- Evidence: planned

**Construction outline.** Prove the orthogonal decomposition, use SP-TENSOR for existence of J, and evaluate trace duality and Weyl coefficients. Compare nested decoders on elementary tensors.

**Falsifier to implement.** Use a symplectic inclusion into two F3 registers and a three-register tower; test a correlated state and the identity normalization.

**Required mutations.** Divide partial trace by the discarded dimension; use a degenerate inclusion; compose decoders with incompatible subsystem labels.

## SP-PRIME

- Title: Tensor assembly and product-state existence
- Status: SKETCH
- Stage: 5
- Definitions: D1711,D1713
- Dependencies: none
- Sources: SP-CM08,SP-WAT18
- Inputs: Explicit finite matrix factors, embeddings and local density operators
- Output: A_pr, its product state and its GNS representation
- Choices: Every local dimension and state; embeddings and ordering convention
- Scope: No factor type, separating-vector property, inter-prime arithmetic process or Bost--Connes identification is asserted.
- Proof: none
- Review: none
- Checks: none
- Evidence: planned

**Construction outline.** Check the finite embeddings and norm independence, use positivity and norm one on the algebraic union to extend by continuity, then construct the GNS quotient and completion.

**Falsifier to implement.** Use the finite prime sets empty, {2}, {3}, {2,3}, {2,3,5}; test embedding squares and compatible faithful and pure product states. Infinite conclusions need written proofs.

**Required mutations.** Use a non-unital finite embedding or an unnormalized reference density; infer faithfulness merely from cyclicity.

## SP-BC-CONTROL

- Title: Arithmetic semigroup and zeta control
- Status: SKETCH
- Stage: 5
- Definitions: D1712,D1713
- Dependencies: none
- Sources: SP-BC95,SP-CM04,SP-CM08,SP-SPECTOR98
- Inputs: Concrete e(r), mu_n, H_log and real b>1
- Output: Arithmetic map identities, invariant dynamics and a convergent zeta partition function
- Choices: The chosen embedding of roots of unity, represented algebra and logarithmic energy
- Scope: The Hamiltonian has logarithmic-integer eigenvalues. No zeta-zero spectrum, universal-representation faithfulness or full KMS classification is asserted.
- Proof: none
- Review: none
- Checks: none
- Evidence: planned

**Construction outline.** Compute on each basis vector, using the finite roots-of-unity average for the corner relation. Prove point-norm continuity on generators and extend; obtain trace convergence from the scalar series.

**Falsifier to implement.** Check finitely supported basis vectors and rational phases with explicit support bounds, plus analytic integral bounds for the zeta tail; do not truncate the isometries into false finite-dimensional ones.

**Required mutations.** Treat mu_n as unitary, omit the 1/n root average, or identify log-energy eigenvalues with zeta zeros.
