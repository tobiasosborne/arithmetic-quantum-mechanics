# Phantasm reuse and overlap review — 2026-09-10

Requested by TJO after identifying that SP-WEYL substantially reuses
results already proved in the repository. All fourteen lemma contracts,
all thirteen new definition blocks, the seven decision gates and the
Phantasm notation additions were checked against the existing single
sources and the relevant admitted proof shards. No earlier claim was
reopened and no SP claim was promoted.

## Reuse that changes the work order

- F1-DUAL, F1-WEYL and F1-REAL already cover arbitrary finite abelian
  configurations. The short SP-WEYL draft uses A=(k^n,+); it adds the
  symplectic-coordinate, phase, center and trace comparisons.
- F1-FUNCT already gives the underlying configuration-product tensor and
  coherence. SP-TENSOR adds the half-form conversion and affine naturality.
- FRB-TRACE and FRB-FROB supply the finite-field trace and absolute
  permutation results. The relative power, chosen character and arbitrary
  symplectic rank are the remaining interfaces.
- FRP-CP supplies arithmetic source soundness, ordinary-trace normalization
  and discards. It does not state that every ambient CP map has an
  arithmetic source representative. D1325 source equality remains distinct
  from D1706 equality of realized CP maps.
- The characteristic-two decision reuses F1-REAL/F1-RING and the admitted
  WH symmetry results; its missing lift is not assumed from an unproved
  splitting conjecture. The higher-gate decision starts with the admitted
  FRB-HIERARCHY/FRB-NATURAL families and their existing cubic example.

The exact clauses and remaining tasks live in the DAG's Inherited, Reuse
and Remaining fields. The checker requires inherited proof nodes to be
PROVED, listed as dependencies, and attached to real proof files. This
checks the recorded reuse, not the correctness of each mathematical step.

## Definition and notation repairs

| Finding | Repair and scope |
|---|---|
| D1703 introduced another algebra/generator notation for the same Weyl construction | Reuse A_(psi,beta)(V) and W_beta(v), extending their owning notation rows to arbitrary rank |
| Bare W(a,b) named a different position-label convention from D8 | Use W^s for the symmetrized model and the explicit identity W^s(a,b)=psi(a.b/2) W_ref(a,b); its wavefunction uses f(x-a). The old bootstrap formula was valid after v maps to -v, not a refuted model |
| D1704 repeated the Pauli and Clifford definitions with new aliases | Reuse D1307's P_A and C_2(A). D1704 defines only the generated actual-amplitude category; the old hierarchy is restated in the labbook |
| D1706 repeated ordinary-trace/conditional semantics under new system symbols | Reuse B_X and Tr_X from D1326 and explicitly describe the ambient Hilbert-block extension. Instruments have common typed source/target and an explicit retained-output direct sum |
| The SP-SCALAR output called every actual T a branch | The output is a CP map; it is a TNI branch exactly when T is a contraction. The nonzero-Hilbert-space scope now agrees with D1706 |
| psi_E was both the fixed trace-family character and an arbitrary base-character extension | Keep psi_E and the fixed family unchanged; use chi_K and chi_(E/K) for the freely chosen relative datum |
| U_F concealed the relationship to existing absolute Frobenius | Use sigma_(E/K)=sigma_E^s and U_(E/K,n)=(U_E^s)^tensor n. Abstract semilinear data are still separately named |
| Fock and GNS notation had implicit components | Specify the inverse-index permutation action and name the GNS Hilbert completion H_phi. D1708 records its overlap with D1010's one-mode completion |
| Unit-norm intertwiner did not state a norm | Use the inherited assertion about unitary intertwiners |
| New definitions did not distinguish extensions from repeated foundations | Every D1701–D1713 block now names Reuses and Delta; no definition number was added or renumbered |

Bound dummy variables remain local to their typed formulas. Historical
Hecke trace/corner notation is not flattened into the ordinary arithmetic
trace convention. The selected ownership guards prevent the retired
aliases from returning; they are not a generic proof of absence of all
possible mathematical notation overlap.

## Work deliberately left separate

F1-CORR and F1-HALL remain SKETCH comparisons. Their existence does not
admit an affine-Lagrangian equivalence or the general completed Fock functor.
The graded Hecke completion, the arithmetic coefficient syntax, the complex
linear stabilizer hull, the unital prime tensor algebra and the nonunital
degree-block algebra have different objects or operations. Their contracts
retain those differences instead of importing a theorem by a shared name.

The source-certified support-code decoder is not the nondegenerate
symplectic subsystem partial trace. Likewise the degree regulator's zeta
ratio does not identify its algebra with the represented Bost–Connes control.

The new finite probes and their expected mutations are in
`theory/checks/phantasm_reuse_EXPECTATIONS.md`. Frozen checks for this repair
are stored separately from the September 9 bootstrap records, under
`numerics/symplectic-phantasm/results/reuse-2026-09-10/`.
