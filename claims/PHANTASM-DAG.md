# Symplectic Phantasm argument DAG

Canonical statements and statuses live in `claims/CLAIMS.md`. This file
holds the typed contracts and remaining comparisons for the formulated
bootstrap. The September 10 reuse review is in
`docs/research-plans/symplectic-phantasm-reuse.md`. Construction outlines summarize the work; admissions rest on the linked proofs and reviews. The source audit
is `docs/research-plans/symplectic-phantasm-sources.md`; the staged work order
and unformulated global decision gates are in
`docs/research-plans/symplectic-phantasm.md`.

The continuing questions about categorical properties and their transport
are in `docs/research-plans/categorical-structure.md`. Its compact-structure
follow-up is owned by the separate SP-COMPACT claim; it does not silently
enlarge SP-LREL. Scalar and operational comparisons are the next work.

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
| SP-COMPACT | 2 | 5 |
| SP-STAB-REL | 2 | 6 |
| SP-SCALAR | 2 | 7 |
| SP-CP | 2 | 8 |
| SP-SUM | 3 | 9 |
| SP-TRACE | 4 | 10 |
| SP-FROB | 4 | 11 |
| SP-SUBSYS | 4 | 12 |
| SP-FOCK | 3 | 13 |
| SP-PRIME | 5 | 14 |
| SP-BC-CONTROL | 5 | 15 |
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
| DG-REL-LIFT | SP-COMPACT,SP-STAB-REL,SP-SCALAR,SP-CP,FRP-CAT,FRP-CP | SP-CK21,SP-BC24,SP-WAT18 | Scalar-retaining relation/circuit presentation, compared with the existing arithmetic source only on explicitly matched fragments | OPEN |
| DG-RIG | SP-TENSOR,SP-SUM,SP-FOCK | SP-CK21,SP-DER06,SP-JOY81 | Classical additive construction and both-product coherence contracts | OPEN |
| DG-HIGHER | SP-EGOROV,SP-TRACE,FRB-HIERARCHY,FRB-NATURAL | SP-CGK17,SP-GROSS06 | Geometric interpretation of the admitted multiplication/phase families, starting with their existing cubic example | OPEN |
| DG-GLOBAL | SP-PRIME,SP-BC-CONTROL,SP-FROB,SP-SUBSYS,DG-CHAR2,DG-REL-LIFT,DG-RIG | SP-CM04,SP-CCM07,SP-CM08 | Actual inter-prime arithmetic maps, their relations and a global algebra definition | OPEN |
| DG-MODULAR | DG-GLOBAL | SP-CM08,SP-CCM07 | Reference, GNS support, faithfulness and a precise flow/KMS comparison contract | OPEN |
| DG-SPECTRUM | DG-MODULAR | SP-CC09,SP-CCM07 | Operator, domain, trace or distribution and a formulated arithmetic comparison | OPEN |

## SP-WEYL

- Title: Weyl realization
- Status: PROVED
- Stage: 1
- Definitions: D3,D4,D5,D8,D9,D1001,D1002,D1003,D1701,D1703
- Dependencies: F1-DUAL,F1-WEYL,F1-REAL
- Inherited: F1-DUAL,F1-WEYL,F1-REAL
- Reuse: F1-REAL section 2 gives the full matrix image, finite SvN and U(1) uniqueness for every finite abelian A; F1-DUAL and F1-WEYL supply its pairing and cocycle.
- Remaining: None within the admitted statement. The coordinate reduction, half-form phase, raw-center quotient and trace/unit comparison have passed review; stronger symmetry lifts remain separate.
- Sources: SP-GH07,SP-PRASAD09,SP-GROSS06
- Inputs: (k,V,omega,psi) with p odd; standard model additionally has symplectic coordinates
- Output: A finite matrix *-algebra, coefficient/normalized matrix trace and the inherited unitary model class
- Choices: The given nontrivial character and a named symplectic coordinate map; the symmetrizing cochain; the raw-center quotient is retained
- Scope: Odd characteristic only; no preferred abstract-space basis or genuine symmetry lift is asserted.
- Proof: theory/symplectic-phantasm/reuse.md
- Review: theory/verdicts/phantasm-stage1-adjudication.md
- Checks: theory/checks/phantasm_reuse_check.py
- Evidence: admitted

**Construction outline.** Use the reviewed corollary proof in theory/symplectic-phantasm/reuse.md sections 1--2. The admitted finite-abelian proof supplies the matrix/SvN conclusions; only its explicit coordinate and phase transport is new.

**Falsifier scope.** Implemented: phantasm_reuse_check.py R1--R4 compares the existing Abelian operator code with the symmetrized wavefunction, central quotient, cocycle and trace at the declared finite fields/ranks. This is a bridge falsifier, not a re-proof of F1-REAL.

**Required mutations.** Wrong dual sign, trivial character, wrong rephasing or shift, wrong cocycle, falsely injective raw center, wrong trace normalization and missing vacuum.

## SP-EGOROV

- Title: Affine symmetries and projective implementation
- Status: PROVED
- Stage: 1
- Definitions: D9,D1003,D1701,D1703
- Dependencies: SP-WEYL,F1-REAL
- Inherited: F1-REAL
- Reuse: F1-REAL section 2 steps 6--8 gives uniqueness and unitary implementation for the finite matrix model.
- Remaining: None within the admitted statement. The exact affine action and projective implementation are proved for the explicitly owned arbitrary-rank model class; a genuine phase lift remains separate.
- Sources: SP-GH07,SP-GH09,SP-GROSS06
- Inputs: Affine symplectic arrow (t,g):V->W over fixed (k,psi)
- Output: alpha_(t,g):A(V)->A(W); projective unitary H(V)->H(W)
- Choices: The common character; model choices; no unrecorded phase section
- Scope: This is a covariant algebra functor and a projective implementation statement. Choosing a genuine linear lift is a separate comparison.
- Proof: theory/symplectic-phantasm/egorov.md
- Review: theory/verdicts/phantasm-stage1-adjudication.md
- Checks: theory/checks/phantasm_egorov_check.py
- Evidence: admitted

**Construction outline.** F1-REAL section 2 steps 6--8 gives uniqueness and unitary implementation for the finite matrix model. Check the affine semidirect-product action on the symmetrized generators in arbitrary rank and its covariance under model transport; no new finite SvN proof.

**Falsifier scope.** Implemented: phantasm_egorov_check.py E1--E8 enumerates all 216 affine symplectic arrows on F3^2, checks identities, inverses and all 46,656 ordered products pointwise, the induced Weyl-algebra action and independent translation, Fourier and shear covariance. It includes rank zero and a nonstandard F9 character. These finite checks do not prove the arbitrary-rank or projective-implementation statement.

**Required mutations.** Drop the translated phase or reverse the order of the semidirect product.

## SP-TENSOR

- Title: Symplectic sum and quantum tensor compatibility
- Status: PROVED
- Stage: 1
- Definitions: D9,D1004,D1701,D1703
- Dependencies: SP-WEYL,SP-EGOROV,F1-FUNCT
- Inherited: F1-FUNCT
- Reuse: F1-FUNCT section 3 supplies the configuration-product Hilbert tensor, basis maps, central product and coherence.
- Remaining: None within the admitted statement. The inherited tensor comparison, half-form transport, affine naturality and projective coherence have passed review; additive completion remains separate.
- Sources: SP-GH07,SP-GH09
- Inputs: Pairs and triples of symplectic spaces and affine arrows over fixed (k,psi)
- Output: A(V+W) -> A(V) tensor A(W), natural with the affine action
- Choices: The common character and standard tensor-coordinate ordering
- Scope: The source operation is symplectic direct sum. This does not construct a coherent additive completion of the classical category.
- Proof: theory/symplectic-phantasm/tensor.md
- Review: theory/verdicts/phantasm-stage1-adjudication.md
- Checks: theory/checks/phantasm_reuse_check.py,theory/checks/phantasm_egorov_check.py
- Evidence: admitted

**Construction outline.** Apply F1-FUNCT to the configuration product and verify psi((a.c+b.d)/2)=psi(a.c/2)psi(b.d/2). Combine the bridge with SP-EGOROV for the remaining affine naturality. A new proof of the underlying Hilbert tensor comparison is unnecessary.

**Falsifier scope.** Implemented: phantasm_reuse_check.py R5 checks the transported product against independently tensored inherited operators, including zero factors. phantasm_egorov_check.py E7/E9 checks the actual rank-zero model and tensor units, all 81 rank-two operator/tensor and swap comparisons over F3, and all 3,779,136 factorwise affine naturality cases. Arbitrary-rank and projective coherence are supplied by the written proof and review.

**Required mutations.** Drop one tensor factor phase, interchange only one coordinate ordering, or replace the unit by a qudit.

## SP-LREL

- Title: Composition of affine Lagrangian relations
- Status: PROVED
- Stage: 2
- Definitions: D1701,D1702
- Dependencies: none
- Inherited: none
- Reuse: The existing flag-context correspondences are different morphisms; no admitted affine-Lagrangian category theorem is used.
- Remaining: None within the admitted statement. Finite coisotropic reduction, affine/empty closure, source and relation monoidal data, dagger and the graph functor have passed capped review.
- Sources: SP-W09,SP-LW14,SP-CK21
- Inputs: R:V->W and S:W->Z; symplectic spaces over one finite field
- Output: S o R:V->Z in the same relation class; product and dagger laws
- Choices: Minus sign on the source form and explicit coordinate reordering
- Scope: This concerns finite linear/affine geometry, including empty relations. It does not assert a normalized quantization of those relations.
- Proof: theory/symplectic-phantasm/lrel-reduction.md,theory/symplectic-phantasm/lrel-laws.md
- Review: theory/verdicts/phantasm-relations-adjudication.md
- Checks: theory/checks/phantasm_relations_check.py
- Evidence: admitted

**Construction outline.** Reduce the product relation along the diagonal in the middle space. Prove the dimension/isotropy statement by annihilators and kernel counting; translate the affine case to the linear case when nonempty. Use ordinary relation composition for associativity.

**Falsifier scope.** Implemented: phantasm_relations_check.py G1--G5 enumerates the zero/one-register Hom-sets over F2/F3, compares all 144,806 composable pairs by sparse joins and independent affine-equation solving, all 290,794 F2 triples plus 4,096 F3 triples, and the declared tensor/graph cases. It does not prove the all-field or arbitrary-rank claim.

**Required mutations.** Use the positive form on both source and target; discard empty composites; use a universal instead of existential middle-point condition.

## SP-COMPACT

- Title: Dagger compact affine Lagrangian relations
- Status: PROVED
- Stage: 2
- Definitions: D1701,D1702,D1714
- Dependencies: SP-LREL
- Inherited: none
- Reuse: SP-LREL supplies the category, dagger, symmetric monoidal product and coherence laws; D1714 adds only the compact data and typed state/process maps.
- Remaining: None within the admitted statement. Both typed snakes, dagger compatibility, name/unname, empty preservation, the two scalars and closed-loop law have passed capped review. Quantum normalization remains separate.
- Sources: SP-CK21,SP-LW14,SP-W09
- Inputs: A finite field k; symplectic spaces V,W; D1714 cup, cap and coherence data
- Output: Dagger compact structure, typed state/process bijection, and the exact endomorphism/closed-loop scalar result with tensor transported by the unit comparison
- Choices: Opposite-form dual; displayed cup/cap factor orders; graph associator, unitors and swap; existential witness-forgetting relation convention
- Scope: Classical affine Lagrangian relations over every finite field, including characteristic two and empty relations. No quantum normalization, amplitude, probability, stabilizer equivalence or Choi theorem.
- Proof: theory/symplectic-phantasm/compact.md
- Review: theory/verdicts/phantasm-relations-adjudication.md
- Checks: theory/checks/phantasm_relations_check.py
- Evidence: admitted

**Construction outline.** Check the diagonal forms and half dimensions
directly.  Expand both snake composites as existential relations with all
coherence maps present.  Expand name and unname to show that each is the
same ordered subset under a change of type.  Classify subrelations of the
zero object and compute the loop using existence, not witness counting.

**Falsifier scope.** Implemented: phantasm_relations_check.py G6--G7 checks
both fully typed snakes and all 466 names/unnames on the zero/one-register
F2/F3 Hom-sets, including empty and nonfunctional relations. Closed loops
are checked as relations, separately from middle-witness counts.

**Required mutations.** Omit the opposite sign; reverse exactly one cup
factor; drop the swap in dagger compatibility; replace existential
witness-forgetting by the multiplicity $|V|$; or send the empty name to the
nonempty scalar.

## SP-STAB-REL

- Title: The scalar-quotient stabilizer comparison
- Status: PROVED
- Stage: 2
- Definitions: D1301,D1307,D1701,D1702,D1703,D1704,D1705,D1715
- Dependencies: SP-LREL,SP-COMPACT,SP-WEYL,SP-EGOROV,SP-TENSOR
- Inherited: none
- Reuse: The admitted SP-WEYL/SP-EGOROV/SP-TENSOR dependencies supply full-matrix Weyl models, affine graph implementers and tensor comparison. SP-LREL/SP-COMPACT supply the admitted relation and compact laws; no pre-quest proof is imported directly here.
- Remaining: None within the admitted statement. The origin-independent line, actual stabilizer membership, composition, bare dagger, tensor, recovery and every second-level unitary are covered by the reviewed constructive proof. Operational normalization remains separate.
- Sources: SP-CK21,SP-GROSS06,SP-BC24
- Inputs: An odd prime p; standard source and target ranks m,n; an affine Lagrangian relation R with the fixed trace-framed character
- Output: The constructive dagger symmetric monoidal equivalence defined by the intertwiner line, with zero separate
- Choices: D1703 Weyl phase; D1702 source sign and bare converse; grouped tensor order; quotient by every invertible complex scalar
- Scope: Standard-object props over odd prime fields, modulo all invertible complex scalars, retaining a separate zero. No norm, success probability, CP map or arithmetic-source exhaustion.
- Proof: theory/symplectic-phantasm/stabilizer-intertwiner-line.md,theory/symplectic-phantasm/stabilizer-functor-laws.md,theory/symplectic-phantasm/stabilizer-equivalence.md
- Review: theory/verdicts/phantasm-relations-adjudication.md
- Checks: theory/checks/phantasm_stabilizer_check.py
- Evidence: admitted

**Construction outline.** Construct the intertwiner space by a finite Weyl group-average projector, prove its rank-one and stabilizer properties, and verify composition, dagger, tensor and recovery at the stated scalar quotient. Check all Clifford unitaries and the opposite-space/vectorization conversion explicitly; the external symmetric-monoidal theorem alone does not provide our dagger clause.

**Falsifier scope.** Implemented: phantasm_stabilizer_check.py S1--S5 constructs all 216 projective qutrit Cliffords and 12/30 F3/F5 state rays, checks all 389 F3 relation lines and all-origin equations, all 140,101 compositions and 389 daggers, 338 state/effect tensors and 144 mixed cases. Separate zero and unequal norms are retained; F3/F5 Bell controls check unnormalized scalars. These finite cases do not prove the arbitrary-rank equivalence.

**Required mutations.** Identify zero with a nonzero scalar; compare normed representatives as if the quotient were phase-only.

## SP-SCALAR

- Title: Scalar normalization
- Status: PROVED
- Stage: 2
- Definitions: D1326,D1704,D1705,D1706
- Dependencies: FRP-CP
- Inherited: FRP-CP
- Reuse: FRP-CP, process-category.md steps 6--8, contains the amplified-positivity and ordinary-trace calculation for realized arithmetic Kraus maps.
- Remaining: None within the admitted statement. The scalar/CP/contraction calculation and corrected representative-or-class-rule consequence passed capped review. A preferred or composition-compatible normalization remains separate.
- Sources: SP-WAT18,SP-CK21
- Inputs: Nonzero finite Hilbert spaces H,K; an arbitrary actual linear map T:H->K; a complex scalar c
- Output: A CP map End(H)->End(K); a TNI branch exactly for T*T<=I; ordinary-trace probability scaling on admissible branches
- Choices: Actual representative and norm; ordinary trace
- Scope: Zero outcomes are retained and never conditionally normalized. This describes the additional data for an operational lift, not a claimed canonical choice of that data.
- Proof: theory/symplectic-phantasm/scalar.md
- Review: theory/verdicts/phantasm-processes-adjudication.md
- Checks: theory/checks/phantasm_process_check.py
- Evidence: admitted

**Construction outline.** FRP-CP, process-category.md steps 6--8, contains the amplified-positivity and ordinary-trace calculation for realized arithmetic Kraus maps. Apply that matrix calculation to an arbitrary finite T and prove the contraction iff-condition and scalar scaling. A general T gives a CP map, not automatically a TNI branch.

**Falsifier scope.** Implemented: phantasm_process_check.py P1--P2 checks the exact scalar modulus law on all qutrit matrix units, distinguishes projective representatives from actual CP maps, and compares the contraction criterion with exact rank-one probability tests including zero. Zero-probability conditioning is rejected explicitly. These finite controls do not prove the arbitrary-dimensional statement or select a representative norm.

**Required mutations.** Treat a factor 2 as a phase; normalize a zero-probability branch.

## SP-CP

- Title: Closure and normalization of finite instruments
- Status: PROVED
- Stage: 2
- Definitions: D1325,D1326,D1327,D1706
- Dependencies: FRP-CP
- Inherited: FRP-CP
- Reuse: FRP-CP admits composition/tensor, ordinary-trace normalization and discards for source-certified arithmetic processes.
- Remaining: None within the admitted statement. Intrinsic block Kraus exhaustion, ordinary-trace criteria, composition/tensor, retained outcomes and ambient adjoints passed capped review. Arithmetic-source exhaustion remains separate.
- Sources: SP-WAT18
- Inputs: Finite nonzero Hilbert block families X,Y,Z; branches B_X->B_Y; instruments with common source and target and a named finite outcome set
- Output: Composed/tensored branches and instruments; retained output direct-sum_o B_Y; trace-dual adjoints in the opposite direction
- Choices: Ordinary block trace and explicit outcome labels
- Scope: This is an ambient process theorem. It makes no claim that arithmetic or stabilizer generators exhaust these maps.
- Proof: theory/symplectic-phantasm/process-kraus-blocks.md,theory/symplectic-phantasm/process-instruments.md
- Review: theory/verdicts/phantasm-processes-adjudication.md
- Checks: theory/checks/phantasm_process_check.py
- Evidence: admitted

**Construction outline.** FRP-CP admits composition/tensor, ordinary-trace normalization and discards for source-certified arithmetic processes. Extend the target to arbitrary Hilbert blocks using the finite Kraus criterion, and verify equality-of-CP-maps and the explicitly retained outcome target. Source soundness does not supply Kraus exhaustion.

**Falsifier scope.** Implemented: phantasm_process_check.py P3--P11 checks rational/Gaussian-rational block Kraus action against independent superoperator coefficients and Choi positivity from matrix-unit outputs. It checks ordinary block traces, map/list equality, composition/tensor paths, retained and sequential/tensor outcome indices, rectangular trace adjoints, the non-TNI discard adjoint and finite D1327 comparisons. This does not prove arbitrary-dimensional Kraus exhaustion or arithmetic-source exhaustion.

**Required mutations.** Use normalized trace in only one system; erase one outcome before summing; reverse a Kraus-adjoint factor.

## SP-SUM

- Title: Coherent sums and tagged quantum systems
- Status: PROVED
- Stage: 3
- Definitions: D1003,D1704,D1706,D1707
- Dependencies: SP-WEYL,SP-CP,SP-STAB-REL,F1-REAL
- Inherited: F1-REAL
- Reuse: F1-REAL section 2 supplies the full endomorphism algebra on each configuration space. SP-STAB-REL supplies finite projective Hom-sets for the strict-enlargement scope clause; the rectangular matrix-unit argument uses actual D1704 maps directly.
- Remaining: None within the admitted statement and Scope. Actual rectangular matrix units, coherent block realization, strict pure-fragment enlargement, empty/repeated list cases and ordinary-trace dephasing passed capped review. Classical rig and arithmetic-source comparisons remain separate.
- Sources: SP-CK21,SP-WAT18
- Inputs: Lists of actual stabilizer model Hilbert spaces and amplitude maps
- Output: Full coherent matrix maps and the separate tagged subalgebra/dephasing
- Choices: Block decomposition; actual scalar representatives before linear span
- Scope: Adding coherent linear combinations enlarges the pure stabilizer fragment. A classical rig source is still to be constructed.
- Proof: theory/symplectic-phantasm/sum.md
- Review: theory/verdicts/phantasm-sum-adjudication.md
- Checks: theory/checks/phantasm_sum_check.py
- Evidence: admitted

**Construction outline.** F1-REAL section 2 already supplies the full endomorphism algebra on each configuration space. Use preparations/effects for rectangular matrix units; verify coherent versus tagged blocks and their dephasing. The complex linear hull strictly enlarges the pure stabilizer fragment; no arithmetic-source comparison is claimed here.

**Falsifier scope.** Implemented: phantasm_sum_check.py U1--U8 constructs all 169 preparation/adjoint matrix-unit words for p=3 and ranks zero through two; checks block action/composition/dagger on repeated and empty lists with explicit zero-row/column shapes; derives coherent/tagged dimensions 16/10, 25/11, 36/18 and 81/81; and checks full matrix-unit dephasing, projection completeness, unitality, idempotence, range and ordinary trace. The imported exact qutrit census supplies the finite diag(1,1,0) witness. These controls do not prove arbitrary ranks or a rig/biproduct theorem.

**Required mutations.** Replace the coherent algebra by its tagged subalgebra; claim arbitrary coherent sums stay within the uncompleted stabilizer morphisms.

## SP-FOCK

- Title: Fock completion and the exponential law
- Status: PROVED
- Stage: 3
- Definitions: D1010,D1708
- Dependencies: none
- Inherited: none
- Reuse: D1010 already names the one-mode polynomial domain and its Hilbert completion; no admitted general Fock functor theorem is used.
- Remaining: None within the admitted statement. Contraction-domain boundedness/functoriality, normalized unitary extension/naturality and zero/one-mode number-operator comparisons passed capped review. Strong monoidal coherence and a classical free-monoid comparison remain separate.
- Sources: SP-DER06
- Inputs: Hilbert spaces, contractions and the Hilbert Fock completion
- Output: A bounded functor, natural exponential unitary and explicit vacuum/one-mode controls
- Choices: Permutation action with inverse-index convention; Hilbert tensor normalization; contractions; the existing one-mode factorial basis
- Scope: Infinite boundedness and the completion require written arguments. No equivalence between an unspecified classical free monoid and this Hilbert construction is asserted.
- Proof: theory/symplectic-phantasm/fock.md
- Review: theory/verdicts/phantasm-completions-adjudication.md
- Checks: theory/checks/phantasm_completions_check.py
- Evidence: admitted

**Construction outline.** Prove norm bounds on every sector and take the Hilbert direct sum. Construct the exponential unitary with the binomial normalization and check dense finite-particle vectors, then extend by continuity.

**Falsifier scope.** Implemented: phantasm_completions_check.py F1--F3 checks rational symmetrizers through sector four in dimensions zero/one/two, sector ranks, vacuum, one-mode factorial normalization, binomial exponential norm squares and one-mode homogeneous naturality, contraction composition, and finite norm growth 1,2,4,8,16 from actual tensor powers of 2I on symmetric vectors. Bounded extension and the infinite growth conclusion remain written-proof obligations.

**Required mutations.** Omit the binomial square root, remove the vacuum, or extend a norm-2 map as though its second quantization were bounded.

## SP-TRACE

- Title: Restriction of scalars preserves the Weyl datum
- Status: PROVED
- Stage: 4
- Definitions: D3,D1301,D1303,D1701,D1703,D1709
- Dependencies: SP-WEYL,FRB-TRACE
- Inherited: FRB-TRACE
- Reuse: FRB-TRACE, foundation.md section 1, admits transported relative trace, surjectivity, transitivity and the trace-pairing argument.
- Remaining: None within the admitted statement. Arbitrary-rank trace nondegeneracy, named-character transport, exact half-form algebra comparison and compatible tower laws passed capped review.
- Sources: SP-STFIELD,SP-PRASAD09
- Inputs: E/K, an E-symplectic space and named nontrivial chi_K; chi_(E/K)=chi_K o Tr_(E/K)
- Output: An underlying K-symplectic space and exact equality of the labelled Weyl products
- Choices: The field embedding defining E/K and the K-character
- Scope: The extension degree may be divisible by the characteristic. This is restriction of scalars with a trace form, not the uncorrected inclusion of a subfield as a symplectic subsystem.
- Proof: theory/symplectic-phantasm/trace.md
- Review: theory/verdicts/phantasm-arithmetic-adjudication.md
- Checks: theory/checks/phantasm_reuse_check.py,theory/checks/phantasm_arithmetic_check.py
- Evidence: admitted

**Construction outline.** FRB-TRACE, foundation.md section 1, admits transported relative trace, surjectivity, transitivity and the trace-pairing argument. Apply the admitted trace facts to arbitrary-rank symplectic spaces and a named base character, then identify the half-form Weyl products. Keep chi_(E/K) separate from the fixed psi_E.

**Falsifier scope.** Implemented: phantasm_reuse_check.py R6 retains its F81/F9 nonstandard-character sample. phantasm_arithmetic_check.py A1--A4 adds F27/F3 degree-equals-characteristic traces, restricted Gram ranks zero/six/twelve, F3/F9/F81 tower transitivity, named-character separation, and exact rank-zero/one/two half-form product, star, unit and trace controls. These finite fields and sparse labels do not prove arbitrary-rank or all-extension statements.

**Required mutations.** Replace trace by multiplication by the extension degree; use the restriction of psi_E to K as though it were always nontrivial.

## SP-FROB

- Title: Named arithmetic Frobenius covariance
- Status: PROVED
- Stage: 4
- Definitions: D1301,D1302,D1303,D1703,D1706,D1709
- Dependencies: SP-WEYL,SP-EGOROV,SP-TRACE,SP-CP,FRB-FROB,FRB-TRACE
- Inherited: FRB-FROB,FRB-TRACE
- Reuse: FRB-FROB, foundation.md section 2, admits the absolute basis permutation, covariance and trace-dual atomic factorization; FRB-TRACE supplies the tower traces. SP-CP supplies only ambient unitary-conjugation channel typing; relative Frobenius covariance, inverse and finite power remain separate calculations.
- Remaining: None within the admitted standard-register statement. Relative-power covariance, named-character invariance, inverse channel and declared finite power passed capped review. Abstract semilinear data remain a separate choice.
- Sources: SP-STFIELD,SP-GH07
- Inputs: E/K with |K|=p^s, rank n>=0, the chosen relative character and U_(E/K,n)=(U_E^s)^tensor n
- Output: Symplectic automorphism, exact unitary covariance and invertible channel
- Choices: Coordinates and relative base field; trace-normalized character
- Scope: A smaller period is allowed. Abstract spaces require named semilinear data; Frobenius is not identified with partial trace.
- Proof: theory/symplectic-phantasm/frobenius.md
- Review: theory/verdicts/phantasm-arithmetic-adjudication.md
- Checks: theory/checks/phantasm_reuse_check.py,theory/checks/phantasm_arithmetic_check.py
- Evidence: admitted

**Construction outline.** FRB-FROB, foundation.md section 2, admits the absolute basis permutation, covariance and trace-dual atomic factorization; FRB-TRACE supplies the tower traces. Take the s-th power and n-fold tensor, check invariance of the chosen relative character, and match the symmetrized frame. An arbitrary base character is not automatically invariant under absolute Frobenius.

**Falsifier scope.** Implemented: phantasm_reuse_check.py R6 retains its selected F81/F9 relative-power sample. phantasm_arithmetic_check.py A5--A7 checks F27/F3 cube/order-three and F81/F9 ninth-power/order-two K-linearity, trace/character invariance, 648,810 exhaustive-rank-one/sparse-rank-two Weyl covariance cases with guarded per-field/rank census sizes, rank zero, bijectivity, inverse channel action and ordinary trace. No dense F81 rank-two matrix is formed; finite success does not prove arbitrary-rank covariance.

**Required mutations.** Replace conjugation by a partial trace or apply the Frobenius to only half the phase coordinates.

## SP-SUBSYS

- Title: Subsystem inclusion and its dual decoder
- Status: PROVED
- Stage: 4
- Definitions: D1326,D1327,D1701,D1703,D1706,D1710
- Dependencies: SP-WEYL,SP-TENSOR,SP-CP,FRP-CP
- Inherited: FRP-CP
- Reuse: FRP-CP admits the ordinary quantum discard and its normalization on arithmetic words.
- Remaining: None within the admitted statement. Symplectic complements, compatible model existence, observable inclusion, ordinary-trace decoder, phase independence and compatible tower laws passed capped review. Support-code success maps remain separate.
- Sources: SP-WAT18,SP-STFIELD
- Inputs: Symplectic injection j and compatible model unitary J
- Output: iota_J:End(H_U)->End(H_V), dual D_J in the opposite direction
- Choices: Model unitary modulo overall phase; compatible tensor identifications in towers
- Scope: The complement and Weyl model compatibility must be verified. Generic field embeddings and coordinate traces are not automatically such injections.
- Proof: theory/symplectic-phantasm/subsystem-models.md,theory/symplectic-phantasm/subsystem-decoder.md
- Review: theory/verdicts/phantasm-arithmetic-adjudication.md
- Checks: theory/checks/phantasm_arithmetic_check.py
- Evidence: admitted

**Construction outline.** FRP-CP admits the ordinary quantum discard and its normalization on arithmetic words. Construct the nondegenerate symplectic complement and compatible model unitary; identify its decoder with the existing discard in those coordinates. A support-code success map is not substituted for this partial trace.

**Falsifier scope.** Implemented: phantasm_arithmetic_check.py A8--A12 checks a non-coordinate F3 symplectic injection/complement, all 729 Weyl compatibility actions, ordinary decoder Kraus/index equality and trace duality, asymmetric/classically correlated/Bell inputs, Weyl characteristic restriction, phase cancellation, and an explicit three-register compatible direct/iterated decoder on 729 matrix units and three states. The M3 fixture satisfies D1710's explicit compatibility equation; it does not establish compatibility for arbitrary chosen data.

**Required mutations.** Divide partial trace by the discarded dimension; use a degenerate inclusion; compose decoders with incompatible subsystem labels.

## SP-PRIME

- Title: Tensor assembly and product-state existence
- Status: PROVED
- Stage: 5
- Definitions: D1711,D1713
- Dependencies: none
- Inherited: none
- Reuse: The earlier degree-block completion uses different algebras and embeddings; it is not a proof of this unital tensor construction.
- Remaining: None within the admitted specified system. Identity insertion, isometric C*-completion, compatible product-state extension and bounded GNS construction with a cyclic vector passed capped review. Arithmetic coupling, faithfulness, a separating vector and factor type remain separate.
- Sources: SP-CM08,SP-WAT18
- Inputs: Explicit finite matrix factors, embeddings and local density operators
- Output: A_pr, its product state and its GNS representation
- Choices: Every local dimension and state; embeddings and ordering convention
- Scope: No factor type, separating-vector property, inter-prime arithmetic process or Bost--Connes identification is asserted.
- Proof: theory/symplectic-phantasm/prime-tensor.md
- Review: theory/verdicts/phantasm-completions-adjudication.md
- Checks: theory/checks/phantasm_completions_check.py
- Evidence: admitted

**Construction outline.** Check the finite embeddings and norm independence, use positivity and norm one on the algebraic union to extend by continuity, then construct the GNS quotient and completion.

**Falsifier scope.** Implemented: phantasm_completions_check.py P1--P2 checks empty/{2}/{3}/{2,3}/{2,3,5} identity insertion for dimensions 2,3,4, all available triangles, star/product/unit on sparse witnesses, exact a*a characteristic polynomials on diagonal witnesses, faithful and pure compatible product states, positivity, GNS Gram ranks 576/192/3, cyclicity and a concrete nonseparating pure cyclic vector. Infinite completion and state extension remain written-proof obligations; no representation nonfaithfulness or factor type is inferred.

**Required mutations.** Use a non-unital finite embedding or an unnormalized reference density; infer a separating reference vector merely from cyclicity.

## SP-BC-CONTROL

- Title: Arithmetic semigroup and zeta control
- Status: PROVED
- Stage: 5
- Definitions: D1712,D1713
- Dependencies: none
- Inherited: none
- Reuse: The earlier degree regularization has a different partition function and does not identify a Bost--Connes system.
- Remaining: None within the admitted represented control. Semigroup/phase/corner/CP identities, maximal-domain self-adjointness, invariant point-norm flow and Gibbs trace convergence for real b>1 passed capped review. No global-system or zero-spectrum comparison is supplied.
- Sources: SP-BC95,SP-CM04,SP-CM08,SP-SPECTOR98
- Inputs: Concrete e(r), mu_n, H_log and real b>1
- Output: Arithmetic map identities, invariant dynamics and a convergent zeta partition function
- Choices: The chosen embedding of roots of unity, represented algebra and logarithmic energy
- Scope: The Hamiltonian has logarithmic-integer eigenvalues. No zeta-zero spectrum, universal-representation faithfulness or full KMS classification is asserted.
- Proof: theory/symplectic-phantasm/bc-control.md
- Review: theory/verdicts/phantasm-completions-adjudication.md
- Checks: theory/checks/phantasm_completions_check.py
- Evidence: admitted

**Construction outline.** Compute on each basis vector, using the finite roots-of-unity average for the corner relation. Prove point-norm continuity on generators and extend; obtain trace convergence from the scalar series.

**Falsifier scope.** Implemented: phantasm_completions_check.py B1--B4 uses symbolic positive-integer basis indices for semigroup/adjoint/range laws, including direct divisible and nondivisible adjoint-helper comparisons, rational phases and root-average divisibility, prime-valuation dynamics, symbolic corner homomorphism/compression controls, rational b=2,3 integral tail intervals and dyadic b=1 lower witnesses. It uses no finite shift truncation. Self-adjointness, continuity and trace class are written-proof obligations, and no zeta-zero spectrum is tested.

**Required mutations.** Treat mu_n as unitary, omit the 1/n root average, or identify log-energy eigenvalues with zeta zeros.
