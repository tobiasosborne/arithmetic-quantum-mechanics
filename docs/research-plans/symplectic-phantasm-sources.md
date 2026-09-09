# Symplectic Phantasm: guidance audit and definition inventory

Source-first bootstrap, 2026-09-09. This audits
`fundamentals-two-categories.md`; it does not rewrite the historical note.
Bibliographic truth, routes, hashes and locators live in `refs/LEDGER.md`.
The SP source identifiers below resolve there. Downloaded material is
evidence only within the scope actually inspected.

## Ground-truth coverage

The initial retrieval registers 25 primary sources, 19 as TeX and six as
PDF. The Bost–Connes original is an author-hosted scan: its first page was
visually inspected, and detailed searchable formulas come from the
Connes–Marcolli book and primary Q-lattice paper. Kapranov–Smirnov was also
recovered as a scan after the linked HTTP route succeeded; its title page
and §1.4 were visually inspected. Existing source bodies were refetched
when needed; the deprecated snapshot was not used as evidence. Joyal’s
original species paper was subsequently recovered from a researcher-hosted
academic copy; its title page and Definition 1 were checked.

Every literature lead named in the guidance is represented in the ledger,
including the historical GAP records below. Those gaps do not support a
bootstrap lemma. Re-fetch with `python3 scripts/fetch-phantasm-sources.py`;
verify the recorded hashes before citing a new download. A changed version
must be inspected and registered, not silently substituted.

## Corrections and scope to carry forward

| Guidance item | Ground truth and current treatment | Sources / next obligation |
|---|---|---|
| A one-dimensional symplectic input gives a qudit | Use symplectic dimension two, or rank one; the zero-dimensional phase space quantizes to the tensor unit | D1701, D1703; SP-WEYL |
| Canonical finite-field quantization | Fix the character. The Gurevich–Hadani construction is for odd characteristic, uses oriented models, and states a contravariant functor; inversion converts the groupoid convention | SP-GH07, SP-GH09; SP-EGOROV |
| No cocycle needs to be carried | Algebra automorphisms and projective implementers are distinct from a chosen genuine lift. Translations retain the Heisenberg central extension even when a Weil action linearizes | SP-GH07, SP-PRASAD09; SP-EGOROV |
| Lagrangian correspondences are the goldilocks category | Register the finite linear/affine relation candidate with sign, composition and empty relation explicit. Category laws belong to a lemma | SP-W09, SP-LW14, SP-CK21; SP-LREL |
| Quantization of all relations is exactly Gaussian operations | The directly relevant stabilizer equivalence is for odd prime dimensions modulo invertible scalars. It does not retain norm or success probability. Gaussian must be defined before another equality of categories is claimed | SP-CK21, SP-BC24, SP-BCL22; SP-STAB-REL and DG-REL-LIFT |
| Nonlinear maps do not quantize | Gross constrains Wigner-positivity-preserving unitaries in a specified odd-dimensional representation. This is not a theorem about every possible quantization of nonlinear geometry | SP-GROSS06; DG-HIGHER |
| Higher Cliffords are degree-k nonlinear Lagrangians | The diagonal classification tracks phase precision and polynomial exponents. Finite-field functions have polynomial identities; the full hierarchy is not automatically a composition-closed class | SP-CGK17; existing D1307, D1309; DG-HIGHER |
| Direct sum forces disjoint union and a rig category | Separate coherent Hilbert sums, tagged algebra sums and tensor product. A classical rig completion is a construction to select and prove, not a consequence of notation | D1707; SP-SUM; DG-RIG |
| Fock is the free commutative monoid | Specify algebraic symmetric algebra versus completed symmetric Fock Hilbert space, normalized symmetric tensors and the class of bounded second-quantized maps. Zero and one-dimensional one-particle spaces differ | SP-DER06; D1708; SP-FOCK |
| Extensions add no quantum objects | Restriction of scalars with the trace form gives a local Weyl comparison; field presentations and distinguished maps remain data | SP-STFIELD, SP-PRASAD09; D1709; SP-TRACE |
| Frobenius is canonical on every symplectic space | Coordinatewise Frobenius is explicit on a standard field register. On an abstract space, specify semilinear descent data; it is not supplied by the bare vector space | D1709; SP-FROB |
| Forgetting an extension or powering is partial trace | Scalar restriction preserves the underlying phase-set size; Frobenius is bijective. A partial trace requires a specified tensor subsystem and has its own direction and normalization | SP-STFIELD, SP-WAT18; D1710; SP-SUBSYS |
| Stochastic closure gives all Gaussian channels | Unitary mixtures are only one channel construction. Preparations, discards, outcomes and their normalization must be specified; no exhaustion theorem is assumed | SP-WAT18, SP-BC24; SP-CP and DG-REL-LIFT |
| Q is a category and a C-star algebra | Keep the quantum category and the chosen algebra assembled from its systems as different typed objects | D1704–D1707, D1711; DG-GLOBAL |
| Nonuniform product states give Powers factors | A reference state and the infinite system must be specified. Nonuniformity alone is not a factor-type classification; no type is asserted for the quest | SP-CM08; SP-POWERS67 GAP; DG-MODULAR |
| A GNS state supplies the desired modular Frobenius | Separate GNS from cyclic/separating or faithful-normal-state hypotheses. The physical flow, modular flow, sign and inverse-temperature scaling require a theorem | SP-CM08, SP-CCM07; D1713; DG-MODULAR |
| Single-prime p-to-one can never see nontrivial zeros | Polynomial counting gives the stated restricted type of zeta comparison. Connes–Consani explicitly discuss generalized counting distributions and the completed Riemann zeta; there is no blanket exclusion covering all F1 approaches | SP-SOULE04, SP-DEITMAR05, SP-CC09, SP-CC10; later spectral contract |
| BC realizes powering and a zeta partition function | Use the actual semigroup isometries, adjoint CP maps, Hamiltonian and convergence domain. A zeta partition function does not identify the spectrum with zeta zeros | SP-BC95, SP-CM04, SP-CM08; D1712; SP-BC-CONTROL |
| A symplectic BC system is definable and novel | This is a research proposal. The product, inter-prime arithmetic maps, state and comparison to known Q-lattice/endomotive systems must be supplied before an existence or novelty assertion | SP-CM04, SP-CCM07; DG-GLOBAL |

## Definition inventory

The constructed bootstrap definitions are stipulations, with their
properties explicitly assigned to unpromoted lemma contracts. Definition
origins below are comparisons, not claims that an external source uses our
exact symbols, variance or phase convention.

| Guidance concept | Canonical location | Origin / remaining contract |
|---|---|---|
| Symplectic objects, rank, linear and affine symmetries | D1701 | Generalizes D1; SP-GH07, SP-W09; arbitrary-rank scope explicit |
| Linear/affine Lagrangian correspondences | D1702 | SP-W09, SP-CK21; relational closure is SP-LREL |
| Character, Weyl algebra, Heisenberg system and Hilbert realization | D3 and D1703 | Generalizes D4; SP-PRASAD09, SP-GH07; odd half-form convention explicit |
| Actual pure stabilizer amplitudes | D1704 | D1307 Pauli/Clifford convention; SP-GROSS06, SP-CK21 |
| Scalar-quotient stabilizer comparison | D1705 | SP-CK21; retains zero separately; not used as a probability space |
| CP maps, channels, instruments, tagged systems | D1706 | Generalizes D1326 to an ambient finite setting; SP-WAT18 |
| Coherent sums and the candidate additive completion | D1707 | Explicit matrix completion; relation to arithmetic disjoint union remains DG-RIG |
| Bosonic Fock space and second quantization | D1708 | SP-DER06; algebraic and completed domains distinguished |
| Field extension, trace form and Frobenius datum | D1709 | Generalizes D1301–D1303; SP-STFIELD |
| Subsystem inclusion and partial trace | D1710 | SP-WAT18; not a replacement definition for existing arithmetic code transfers |
| Tensor assembly across primes, product reference and GNS | D1711 and D1713 | SP-CM08; elementary finite matrix construction, no BC identification |
| BC benchmark, powering maps and energy | D1712 | SP-BC95, SP-CM04, SP-CM08; concrete represented benchmark only |
| C-star dynamics, KMS state, GNS and modular datum | D1713 | SP-CM08, SP-CCM07; full modular comparison is DG-MODULAR |
| Higher Clifford hierarchy and phase differences | Existing D1307 and D1309 | SP-CGK17; no duplicate definitions; nonlinear geometric source pending DG-HIGHER |
| Gaussian processes | No new definition adopted | Compare SP-BCL22 and SP-BC24 with the exact circuit/instrument choice at DG-REL-LIFT |
| Combinatorial species | SP-JOY81 §1.1, Definition 1 registered as a source definition; no quantum comparison adopted | A finitary species is an endofunctor of finite sets and bijections; DG-RIG must specify its role |
| Classical rig / symplectic finite sets or varieties | No new definition adopted | DG-RIG must specify objects, morphisms, both products and distributivity |
| F1 skeleton, extensions, zeta and symplectic Weyl-group analogy | Source definitions registered; no unified quest definition adopted | SP-SOULE04, SP-DEITMAR05, SP-CC09, SP-CC10; SP-KS95; SP-TITS57 gap below |
| Symplectic BC system and its spectral operator | No definition yet | DG-GLOBAL and DG-SPECTRUM must turn the proposed target into an actual mathematical object |

## Historical leads with missing primary bodies

All entries are registered as GAP in `refs/LEDGER.md`; none is a theorem
dependency. Bibliographic metadata or another author's citation does not
fill the gap. These can be retrieved when their precise comparison becomes
the next useful task; they do not block the local Weyl definitions.

| Identifier | Guidance lead | Attempt and available control |
|---|---|---|
| SP-TITS57 | Tits, Sur les analogues algébriques des groupes semi-simples complexes | ULB primary bibliographic record retrieved, but it offers no source body; no equation Sp over F1 equals a Weyl group is admitted |
| SP-JULIA90 | Julia, Statistical Theory of Numbers | Publisher metadata located; CERN download route returned a browser challenge; SP-SPECTOR98 supplies a separately fetched arithmetic-gas control |
| SP-BB91 | Bakas–Bowick, Curiosities of arithmetic gases | CERN preprint record located; retrieval returned a browser challenge; no inaccessible result is used |
| SP-SPECTOR90 | Spector, Supersymmetry and the Möbius inversion function | Euclid candidate returned HTML rather than a PDF; original body unresolved; SP-SPECTOR98 is a distinct paper |
| SP-POWERS67 | Powers, Representations of uniformly hyperfinite algebras and their associated von Neumann rings | Annals primary metadata located; original full text not retrieved; no factor classification imported |
