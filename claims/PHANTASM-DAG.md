# Symplectic Phantasm argument DAG

Canonical statements and statuses live in `claims/CLAIMS.md`. This file
holds the typed contracts and remaining comparisons for the formulated
bootstrap. The September 10 reuse review is in
`docs/research-plans/symplectic-phantasm-reuse.md`. Every outline is SKETCH, not an admitted proof. The source audit
is `docs/research-plans/symplectic-phantasm-sources.md`; the staged work order
and unformulated global decision gates are in
`docs/research-plans/symplectic-phantasm.md`.

Run `python3 theory/checks/phantasm_contract_check.py`. It checks the schema,
reference resolution, dependency acyclicity, local source hashes, inherited-proof status, definition reuse, selected notation
ownership and evidence requirements, and exact statement/definition restatements in the
labbook. Input/output contracts are explicit human-readable mathematical
types; this is not a symbolic type checker or proof assistant. A green run
does not promote a claim.

A node may be drafted before its dependencies are proved, provided every
such dependency stays explicit. It may be promoted only when its proof and
review cover the exact statement and its mathematical dependencies are
PROVED (or explicitly carried as hypotheses of a separately formulated
conditional claim). The Checks field distinguishes implemented bridge probes from planned
falsifiers; every node states their scope. Existing admitted proofs are
reused at their declared scope, and Remaining records the work still owed.

For promotion, fill Proof and Review with real repository paths, replace
Checks with real executable checker paths, and record an adjudication
containing `Admitted: <claim-id>`. Drafts and implemented bridge probes use `Evidence: draft`. Promotion
evidence must say `admitted`; the proof
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
| DG-CHAR2 | SP-WEYL,SP-EGOROV,F1-REAL,F1-RING,WH-WEIL-a,WH-WEIL-c,WH-WEIL-d | SP-GH08 | Reuse the admitted characteristic-two Weyl models; specify the extra symmetry-lift and phase data without assuming a full splitting | OPEN |
| DG-REL-LIFT | SP-STAB-REL,SP-SCALAR,SP-CP,FRP-CAT,FRP-CP | SP-CK21,SP-BC24,SP-WAT18 | Scalar-retaining relation/circuit presentation, compared with the existing arithmetic source only on explicitly matched fragments | OPEN |
| DG-RIG | SP-TENSOR,SP-SUM,SP-FOCK | SP-CK21,SP-DER06,SP-JOY81 | Classical additive construction and both-product coherence contracts | OPEN |
| DG-HIGHER | SP-EGOROV,SP-TRACE,FRB-HIERARCHY,FRB-NATURAL | SP-CGK17,SP-GROSS06 | Geometric interpretation of the admitted multiplication/phase families, starting with their existing cubic example | OPEN |
| DG-GLOBAL | SP-PRIME,SP-BC-CONTROL,SP-FROB,SP-SUBSYS,DG-CHAR2,DG-REL-LIFT,DG-RIG | SP-CM04,SP-CCM07,SP-CM08 | Actual inter-prime arithmetic maps, their relations and a global algebra definition | OPEN |
| DG-MODULAR | DG-GLOBAL | SP-CM08,SP-CCM07 | Reference, GNS support, faithfulness and a precise flow/KMS comparison contract | OPEN |
| DG-SPECTRUM | DG-MODULAR | SP-CC09,SP-CCM07 | Operator, domain, trace or distribution and a formulated arithmetic comparison | OPEN |

## SP-WEYL

- Title: Weyl realization
- Status: SKETCH
- Stage: 1
- Definitions: D3,D4,D5,D8,D1001,D1002,D1003,D1701,D1703
- Dependencies: F1-DUAL,F1-WEYL,F1-REAL
- Inherited: F1-DUAL,F1-WEYL,F1-REAL
- Reuse: F1-REAL section 2 gives the full matrix image, finite SvN and U(1) uniqueness for every finite abelian A; F1-DUAL and F1-WEYL supply its pairing and cocycle.
- Remaining: Only the symplectic-coordinate reduction, half-form phase change, raw-center quotient and trace/unit identification must be assembled; the assembled claim still needs promotion review.
- Sources: SP-GH07,SP-PRASAD09,SP-GROSS06
- Inputs: (k,V,omega,psi) with p odd; standard model additionally has symplectic coordinates
- Output: A finite matrix *-algebra, coefficient/normalized matrix trace and the inherited unitary model class
- Choices: The given nontrivial character and a named symplectic coordinate map; the symmetrizing cochain; the raw-center quotient is retained
- Scope: Odd characteristic only; no preferred abstract-space basis or genuine symmetry lift is asserted.
- Proof: theory/symplectic-phantasm/reuse.md
- Review: none
- Checks: theory/checks/phantasm_reuse_check.py
- Evidence: draft

**Construction outline.** Use the structured corollary draft in theory/symplectic-phantasm/reuse.md sections 1--2. The admitted finite-abelian proof supplies the matrix/SvN conclusions; only its explicit coordinate and phase transport is new.

**Falsifier scope.** Implemented: phantasm_reuse_check.py R1--R4 compares the existing Abelian operator code with the symmetrized wavefunction, central quotient, cocycle and trace at the declared finite fields/ranks. This is a bridge falsifier, not a re-proof of F1-REAL.

**Required mutations.** Wrong dual sign, trivial character, wrong rephasing or shift, wrong cocycle, falsely injective raw center, wrong trace normalization and missing vacuum.

## SP-EGOROV

- Title: Affine symmetries and projective implementation
- Status: SKETCH
- Stage: 1
- Definitions: D1003,D1701,D1703
- Dependencies: SP-WEYL,F1-REAL
- Inherited: F1-REAL
- Reuse: F1-REAL section 2 steps 6--8 gives uniqueness and unitary implementation for the finite matrix model.
- Remaining: Check the affine semidirect-product action on the symmetrized generators in arbitrary rank and its covariance under model transport; no new finite SvN proof.
- Sources: SP-GH07,SP-GH09,SP-GROSS06
- Inputs: Affine symplectic arrow (t,g):V->W over fixed (k,psi)
- Output: alpha_(t,g):A(V)->A(W); projective unitary H(V)->H(W)
- Choices: The common character; model choices; no unrecorded phase section
- Scope: This is a covariant algebra functor and a projective implementation statement. Choosing a genuine linear lift is a separate comparison.
- Proof: none
- Review: none
- Checks: none
- Evidence: planned

**Construction outline.** F1-REAL section 2 steps 6--8 gives uniqueness and unitary implementation for the finite matrix model. Check the affine semidirect-product action on the symmetrized generators in arbitrary rank and its covariance under model transport; no new finite SvN proof.

**Falsifier scope.** Enumerate the affine group on F3^2; check the semidirect-product law and both translation and Fourier/shear covariance.

**Required mutations.** Drop the translated phase or reverse the order of the semidirect product.

## SP-TENSOR

- Title: Symplectic sum and quantum tensor compatibility
- Status: SKETCH
- Stage: 1
- Definitions: D1004,D1701,D1703
- Dependencies: SP-WEYL,SP-EGOROV,F1-FUNCT
- Inherited: F1-FUNCT
- Reuse: F1-FUNCT section 3 supplies the configuration-product Hilbert tensor, basis maps, central product and coherence.
- Remaining: Check the half-form cochain is multiplicative across factors, then extend the existing configuration-isomorphism naturality to the declared affine symplectic arrows. Do not use this SP claim to prove SP-WEYL.
- Sources: SP-GH07,SP-GH09
- Inputs: Pairs and triples of symplectic spaces and affine arrows over fixed (k,psi)
- Output: A(V+W) -> A(V) tensor A(W), natural with the affine action
- Choices: The common character and standard tensor-coordinate ordering
- Scope: The source operation is symplectic direct sum. This does not construct a coherent additive completion of the classical category.
- Proof: none
- Review: none
- Checks: theory/checks/phantasm_reuse_check.py
- Evidence: draft

**Construction outline.** Apply F1-FUNCT to the configuration product and verify psi((a.c+b.d)/2)=psi(a.c/2)psi(b.d/2). Combine the bridge with SP-EGOROV for the remaining affine naturality. A new proof of the underlying Hilbert tensor comparison is unnecessary.

**Falsifier scope.** Implemented: phantasm_reuse_check.py R5 checks the transported product against independently tensored inherited operators, including a zero factor. The full affine naturality/coherence statement still requires its written bridge.

**Required mutations.** Drop one tensor factor phase, interchange only one coordinate ordering, or replace the unit by a qudit.

## SP-LREL

- Title: Composition of affine Lagrangian relations
- Status: SKETCH
- Stage: 2
- Definitions: D1701,D1702
- Dependencies: none
- Inherited: none
- Reuse: The existing flag-context correspondences are different morphisms; no admitted affine-Lagrangian category theorem is used.
- Remaining: Derive closure by finite linear reduction and the affine empty-case law; then verify graph, dagger and tensor typing.
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

**Falsifier scope.** Enumerate affine Lagrangians in F2^2 and F3^2 and small zero/one-register Hom-sets; compare image dimensions and existential composition by independent enumeration.

**Required mutations.** Use the positive form on both source and target; discard empty composites; use a universal instead of existential middle-point condition.

## SP-STAB-REL

- Title: The scalar-quotient stabilizer comparison
- Status: SKETCH
- Stage: 2
- Definitions: D1701,D1702,D1703,D1704,D1705
- Dependencies: SP-LREL,SP-WEYL,SP-EGOROV,SP-TENSOR
- Inherited: none
- Reuse: The scalar-quotient equivalence is sourced externally; the earlier lifted-frame comparison remains a sketch and is not an admitted equivalence.
- Remaining: Match the source presentation to D1704/D1705, with the zero map and C^times quotient explicit. This is not the normalized operational lift.
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

**Falsifier scope.** Check the source generators for p=3,5, with state/effect composites, including one zero composite and two distinct nonzero norms representing the same class.

**Required mutations.** Identify zero with a nonzero scalar; compare normed representatives as if the quotient were phase-only.

## SP-SCALAR

- Title: Scalar normalization
- Status: SKETCH
- Stage: 2
- Definitions: D1326,D1704,D1705,D1706
- Dependencies: FRP-CP
- Inherited: FRP-CP
- Reuse: FRP-CP, process-category.md steps 6--8, contains the amplified-positivity and ordinary-trace calculation for realized arithmetic Kraus maps.
- Remaining: Apply that matrix calculation to an arbitrary finite T and prove the contraction iff-condition and scalar scaling. A general T gives a CP map, not automatically a TNI branch.
- Sources: SP-WAT18,SP-CK21
- Inputs: Nonzero finite Hilbert spaces H,K; an arbitrary actual linear map T:H->K; a complex scalar c
- Output: A CP map End(H)->End(K); a TNI branch exactly for T*T<=I; ordinary-trace probability scaling on admissible branches
- Choices: Actual representative and norm; ordinary trace
- Scope: Zero outcomes are retained and never conditionally normalized. This describes the additional data for an operational lift, not a claimed canonical choice of that data.
- Proof: none
- Review: none
- Checks: none
- Evidence: planned

**Construction outline.** FRP-CP, process-category.md steps 6--8, contains the amplified-positivity and ordinary-trace calculation for realized arithmetic Kraus maps. Apply that matrix calculation to an arbitrary finite T and prove the contraction iff-condition and scalar scaling. A general T gives a CP map, not automatically a TNI branch.

**Falsifier scope.** Use identity, a rank-one projection and scalar multiples 0,1/2,2 on a qutrit; compare successful probabilities with trace directly.

**Required mutations.** Treat a factor 2 as a phase; normalize a zero-probability branch.

## SP-CP

- Title: Closure and normalization of finite instruments
- Status: SKETCH
- Stage: 2
- Definitions: D1325,D1326,D1327,D1706
- Dependencies: FRP-CP
- Inherited: FRP-CP
- Reuse: FRP-CP admits composition/tensor, ordinary-trace normalization and discards for source-certified arithmetic processes.
- Remaining: Extend the target to arbitrary Hilbert blocks using the finite Kraus criterion, and verify equality-of-CP-maps and the explicitly retained outcome target. Source soundness does not supply Kraus exhaustion.
- Sources: SP-WAT18
- Inputs: Finite nonzero Hilbert block families X,Y,Z; branches B_X->B_Y; instruments with common source and target and a named finite outcome set
- Output: Composed/tensored branches and instruments; retained output direct-sum_o B_Y; trace-dual adjoints in the opposite direction
- Choices: Ordinary block trace and explicit outcome labels
- Scope: This is an ambient process theorem. It makes no claim that arithmetic or stabilizer generators exhaust these maps.
- Proof: none
- Review: none
- Checks: none
- Evidence: planned

**Construction outline.** FRP-CP admits composition/tensor, ordinary-trace normalization and discards for source-certified arithmetic processes. Extend the target to arbitrary Hilbert blocks using the finite Kraus criterion, and verify equality-of-CP-maps and the explicitly retained outcome target. Source soundness does not supply Kraus exhaustion.

**Falsifier scope.** Exact rational Kraus examples on one and two matrix blocks, including preparation, discard, branching and a non-unital state channel.

**Required mutations.** Use normalized trace in only one system; erase one outcome before summing; reverse a Kraus-adjoint factor.

## SP-SUM

- Title: Coherent sums and tagged quantum systems
- Status: SKETCH
- Stage: 3
- Definitions: D1003,D1704,D1706,D1707
- Dependencies: SP-WEYL,SP-CP,F1-REAL
- Inherited: F1-REAL
- Reuse: F1-REAL section 2 already supplies the full endomorphism algebra on each configuration space.
- Remaining: Use preparations/effects for rectangular matrix units; verify coherent versus tagged blocks and their dephasing. The complex linear hull is larger than both pure stabilizer maps and the arithmetic coefficient syntax.
- Sources: SP-CK21,SP-WAT18
- Inputs: Lists of actual stabilizer model Hilbert spaces and amplitude maps
- Output: Full coherent matrix maps and the separate tagged subalgebra/dephasing
- Choices: Block decomposition; actual scalar representatives before linear span
- Scope: Adding coherent linear combinations enlarges the pure stabilizer fragment. A classical rig source is still to be constructed.
- Proof: none
- Review: none
- Checks: none
- Evidence: planned

**Construction outline.** F1-REAL section 2 already supplies the full endomorphism algebra on each configuration space. Use preparations/effects for rectangular matrix units; verify coherent versus tagged blocks and their dephasing. The complex linear hull is larger than both pure stabilizer maps and the arithmetic coefficient syntax.

**Falsifier scope.** For H=C plus C^3, compare dimensions 16 and 10 and a cross-block coherent observable; verify dephasing removes exactly off-diagonal blocks.

**Required mutations.** Replace the coherent algebra by its tagged subalgebra; claim arbitrary coherent sums stay within the uncompleted stabilizer morphisms.

## SP-FOCK

- Title: Fock completion and the exponential law
- Status: SKETCH
- Stage: 3
- Definitions: D1010,D1708
- Dependencies: none
- Inherited: none
- Reuse: D1010 already names the one-mode polynomial domain and its Hilbert completion; no admitted general Fock functor theorem is used.
- Remaining: Establish the general contraction-domain functor and normalized exponential law from the registered Fock source. Identify the one-mode basis x^r/sqrt(r!) with the existing completion without promoting the older Hall sketch.
- Sources: SP-DER06
- Inputs: Hilbert spaces, contractions and the Hilbert Fock completion
- Output: A bounded functor, natural exponential unitary and explicit vacuum/one-mode controls
- Choices: Permutation action with inverse-index convention; Hilbert tensor normalization; contractions; the existing one-mode factorial basis
- Scope: Infinite boundedness and the completion require written arguments. No equivalence between an unspecified classical free monoid and this Hilbert construction is asserted.
- Proof: none
- Review: none
- Checks: none
- Evidence: planned

**Construction outline.** Prove norm bounds on every sector and take the Hilbert direct sum. Construct the exponential unitary with the binomial normalization and check dense finite-particle vectors, then extend by continuity.

**Falsifier scope.** Compute symmetrizers and norms through particle number four for one and two modes; distinguish the zero space from C.

**Required mutations.** Omit the binomial square root, remove the vacuum, or extend a norm-2 map as though its second quantization were bounded.

## SP-TRACE

- Title: Restriction of scalars preserves the Weyl datum
- Status: SKETCH
- Stage: 4
- Definitions: D3,D1301,D1303,D1701,D1703,D1709
- Dependencies: SP-WEYL,FRB-TRACE
- Inherited: FRB-TRACE
- Reuse: FRB-TRACE, foundation.md section 1, admits transported relative trace, surjectivity, transitivity and the trace-pairing argument.
- Remaining: Apply the admitted trace facts to arbitrary-rank symplectic spaces and a named base character, then identify the half-form Weyl products. Keep chi_(E/K) separate from the fixed psi_E.
- Sources: SP-STFIELD,SP-PRASAD09
- Inputs: E/K, an E-symplectic space and named nontrivial chi_K; chi_(E/K)=chi_K o Tr_(E/K)
- Output: An underlying K-symplectic space and exact equality of the labelled Weyl products
- Choices: The field embedding defining E/K and the K-character
- Scope: The extension degree may be divisible by the characteristic. This is restriction of scalars with a trace form, not the uncorrected inclusion of a subfield as a symplectic subsystem.
- Proof: none
- Review: none
- Checks: theory/checks/phantasm_reuse_check.py
- Evidence: draft

**Construction outline.** FRB-TRACE, foundation.md section 1, admits transported relative trace, surjectivity, transitivity and the trace-pairing argument. Apply the admitted trace facts to arbitrary-rank symplectic spaces and a named base character, then identify the half-form Weyl products. Keep chi_(E/K) separate from the fixed psi_E.

**Falsifier scope.** Implemented: phantasm_reuse_check.py R6 tests a nonstandard F9 base character inside F81, relative-trace transitivity and relative Frobenius covariance. Existing frobenius_hierarchy_check.py remains evidence for its original FRB scopes; abstract-rank claims need their written argument.

**Required mutations.** Replace trace by multiplication by the extension degree; use the restriction of psi_E to K as though it were always nontrivial.

## SP-FROB

- Title: Named arithmetic Frobenius covariance
- Status: SKETCH
- Stage: 4
- Definitions: D1301,D1302,D1303,D1703,D1709
- Dependencies: SP-WEYL,SP-EGOROV,SP-TRACE,FRB-FROB,FRB-TRACE
- Inherited: FRB-FROB,FRB-TRACE
- Reuse: FRB-FROB, foundation.md section 2, admits the absolute basis permutation, covariance and trace-dual atomic factorization; FRB-TRACE supplies the tower traces.
- Remaining: Take the s-th power and n-fold tensor, check invariance of the chosen relative character, and match the symmetrized frame. An arbitrary base character is not automatically invariant under absolute Frobenius.
- Sources: SP-STFIELD,SP-GH07
- Inputs: E/K with |K|=p^s, rank n>=0, the chosen relative character and U_(E/K,n)=(U_E^s)^tensor n
- Output: Symplectic automorphism, exact unitary covariance and invertible channel
- Choices: Coordinates and relative base field; trace-normalized character
- Scope: A smaller period is allowed. Abstract spaces require named semilinear data; Frobenius is not identified with partial trace.
- Proof: none
- Review: none
- Checks: theory/checks/phantasm_reuse_check.py
- Evidence: draft

**Construction outline.** FRB-FROB, foundation.md section 2, admits the absolute basis permutation, covariance and trace-dual atomic factorization; FRB-TRACE supplies the tower traces. Take the s-th power and n-fold tensor, check invariance of the chosen relative character, and match the symmetrized frame. An arbitrary base character is not automatically invariant under absolute Frobenius.

**Falsifier scope.** Implemented: phantasm_reuse_check.py R6 tests a nonstandard F9 base character inside F81, relative-trace transitivity and relative Frobenius covariance. Existing frobenius_hierarchy_check.py remains evidence for its original FRB scopes; abstract-rank claims need their written argument.

**Required mutations.** Replace conjugation by a partial trace or apply the Frobenius to only half the phase coordinates.

## SP-SUBSYS

- Title: Subsystem inclusion and its dual decoder
- Status: SKETCH
- Stage: 4
- Definitions: D1326,D1327,D1701,D1703,D1706,D1710
- Dependencies: SP-WEYL,SP-TENSOR,SP-CP,FRP-CP
- Inherited: FRP-CP
- Reuse: FRP-CP admits the ordinary quantum discard and its normalization on arithmetic words.
- Remaining: Construct the nondegenerate symplectic complement and compatible model unitary; identify its decoder with the existing discard in those coordinates. A support-code success map is not substituted for this partial trace.
- Sources: SP-WAT18,SP-STFIELD
- Inputs: Symplectic injection j and compatible model unitary J
- Output: iota_J:End(H_U)->End(H_V), dual D_J in the opposite direction
- Choices: Model unitary modulo overall phase; compatible tensor identifications in towers
- Scope: The complement and Weyl model compatibility must be verified. Generic field embeddings and coordinate traces are not automatically such injections.
- Proof: none
- Review: none
- Checks: none
- Evidence: planned

**Construction outline.** FRP-CP admits the ordinary quantum discard and its normalization on arithmetic words. Construct the nondegenerate symplectic complement and compatible model unitary; identify its decoder with the existing discard in those coordinates. A support-code success map is not substituted for this partial trace.

**Falsifier scope.** Use a symplectic inclusion into two F3 registers and a three-register tower; test a correlated state and the identity normalization.

**Required mutations.** Divide partial trace by the discarded dimension; use a degenerate inclusion; compose decoders with incompatible subsystem labels.

## SP-PRIME

- Title: Tensor assembly and product-state existence
- Status: SKETCH
- Stage: 5
- Definitions: D1711,D1713
- Dependencies: none
- Inherited: none
- Reuse: The earlier degree-block completion uses different algebras and embeddings; it is not a proof of this unital tensor construction.
- Remaining: Verify this specified inductive matrix system and product-state/GNS existence. Factor type and arithmetic inter-prime maps remain separate.
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

**Falsifier scope.** Use the finite prime sets empty, {2}, {3}, {2,3}, {2,3,5}; test embedding squares and compatible faithful and pure product states. Infinite conclusions need written proofs.

**Required mutations.** Use a non-unital finite embedding or an unnormalized reference density; infer faithfulness merely from cyclicity.

## SP-BC-CONTROL

- Title: Arithmetic semigroup and zeta control
- Status: SKETCH
- Stage: 5
- Definitions: D1712,D1713
- Dependencies: none
- Inherited: none
- Reuse: The earlier degree regularization has a different partition function and does not identify a Bost--Connes system.
- Remaining: Check the represented semigroup identities, invariant dynamics and trace convergence against the registered BC sources; no spectral-zero identification is included.
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

**Falsifier scope.** Check finitely supported basis vectors and rational phases with explicit support bounds, plus analytic integral bounds for the zeta tail; do not truncate the isometries into false finite-dimensional ones.

**Required mutations.** Treat mu_n as unitary, omit the 1/n root average, or identify log-energy eigenvalues with zeta zeros.
