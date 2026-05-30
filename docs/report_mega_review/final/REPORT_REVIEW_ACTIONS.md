# Final Report Review Actions

## Scope And Method

- Scope: final action document for the report mega-review rooted at `report.tex`.
- Inputs: 46 Wave 1 shard-pair reviews under `docs/report_mega_review/wave1/` and 4 Wave 2 syntheses under `docs/report_mega_review/wave2/`.
- Method: read `docs/report_mega_review/README.md`, `docs/report_mega_review/STATE.md`, all Wave 2 syntheses, and skimmed Wave 1 only where needed for line references.
- Command boundary: read-only inspection only (`rg`, `sed`, `nl`, `ls`, `git status`). No Julia, no `make test`, no `scripts/run_all.jl`, no `make report`, and no producer scripts.
- Severity policy: Wave 1 found Major findings and questions but no explicit Blocker labels. This backlog uses P0/P1/P2/P3 and does not invent blockers.

## Executive Summary

- P0 work is concentrated in sign/phase anchors, hard mathematical definition errors, locality-spine defects, Haah excitation-map convention, and over-strong certificate language.
- AQM-08/AQM-22/AQM-23 need one coherent Pauli/Weyl source-convention bridge before later stabilizer and residue-qudit shards cite them as stable anchors.
- AQM-25 must be rewritten around finite closed supports or restricted; the current quasi-compact-open net collapses toward the global object in affine cases.
- Several statements promote summaries, booleans, or source-local theorems into stronger local certificates or exactness claims.
- Local-net, descent, Cech, and stabilizer-gluing language must carry finite-support and phase hypotheses explicitly.
- Tangent/cotangent and de Rham shards need base, sign, rank, and phase conventions before code-parameter or stabilizer conclusions are retained.
- QSA tables need one vocabulary pass: proposal labels and ad hoc statuses should not become table status tokens without a convention update.
- AQM-89/AQM-91 need provenance tightening, qubit-versus-prime-qudit separation, and corrected Haah/Laurent exactness wording.
- Source/run/index path errors are mostly P2 cleanup after mathematical wording stabilizes.
- Mostly clean slices should be preserved: finite-set workflow basics, boson/fermion/fusion boundary caveats, finite-ring database non-overclaiming, and AQM-88/AQM-90 derivative-boundary caution language.

## Priority Table

| Priority | Meaning | Main actions |
| --- | --- | --- |
| P0 | Fix before downstream report edits rely on the affected claims. Not a blocker label. | Sign/phase anchors; definition/proof errors; locality spine; Haah excitation-map convention; certificate overclaims. |
| P1 | Major correctness, provenance, or status issues for the next editing pass. | Source-convention bridges; stabilizer descent/phase language; `Spec Z` wording; QSA vocabulary; AQM-89 provenance. |
| P2 | Reproducibility, locator, schema/index, and catalogue precision fixes. | Full paths, stale CSV paths, catalogue wording, missing source locators, stale lab-log/status text. |
| P3 | Questions or deferred clarifications. | Optional generic sectors, approximate-equivalence scope, future validation/rebuild after edits. |

## Editing Guardrails

- Do not repair report prose by weakening the repository's evidence contract. Each retained mathematical or physical claim still needs a local source, local derivation, reproducible artifact, or explicit "question/proposal" status.
- Convention edits should happen before dependent shard edits when the defect is convention-level: Pauli/Weyl signs, QSA status tokens, tangent-cotangent signs, and Haah excitation maps.
- Source acquisition or manifest updates should precede prose that upgrades a plausible claim into a sourced claim.
- Generated data and run-bundle claims should not be edited from memory; check the registered CSV, sentinel rows, schema text, and run README in the later repair pass.
- Keep finite-support, generic-sector, completion, and infinite-volume language separated. Several review findings are caused by those layers being visually merged.

## Findings By Theme

### Sign, Phase, And Convention Errors

- P0: AQM-08 has a sign/polarization inconsistency. The local commutator is `omega((x,z),(x',z')) = z*x' - x*z'` at `report/sections/08_symplectic_css_bridge.tex:51-58`, the mixed CSS pairing is `-x*z` at `report/sections/08_symplectic_css_bridge.tex:89-92`, but the later logical pairing is positive evaluation at `report/sections/08_symplectic_css_bridge.tex:222-226`. Fix the sign and logical X/Z polarization labels together.

- P0: AQM-22/AQM-23 use the local non-half Weyl convention but do not bridge it to cited source conventions. See `report/sections/22_prime_field_arithmetic_fields_qudit_paulis.tex:145-153` and `report/sections/23_spec_z6_residue_qudit_factorisation.tex:147-159`. Add one explicit source-sign conversion in AQM-22 and cross-reference it from AQM-23.

- P1: AQM-43 proves commutator preservation for trace-normalized embeddings and then claims a `*`-monomorphism at `report/sections/43_finite_field_scale_continuum_limits.tex:141-153`. For the AQM-28 non-half Weyl law, show multiplier preservation before keeping the algebra-map claim.

- P1: AQM-43 calls Frobenius a Clifford/Gaussian automorphism at `report/sections/43_finite_field_scale_continuum_limits.tex:232-250`, but AQM-42 defines symplectic morphisms as `k`-linear at `report/sections/42_gaussian_clifford_dynamics.tex:91-101`. Mark Frobenius as semilinear or `F_3`-linear unless a new convention is added.

- P1: AQM-58 and AQM-60 use opposite tangent-cotangent coordinate signs: `dp wedge dx` and `p q' - p' q` at `report/sections/58_product_rings_real_line_cotangent.tex:151-170` versus `beta(v)-alpha(w)` at `report/sections/60_tangent_weyl_operator_principle.tex:57-64`. Choose one convention and sweep coordinate examples.

### Unsupported Mathematical Claims And Provenance Gaps

- P0: AQM-17 gives the Proj stalk localization denominator incorrectly as `a,b in M` with `b notin p` at `report/sections/17_projective_line_stalks.tex:54-58`. The denominator must be a homogeneous element of the graded ring, not of the module.

- P0: AQM-07 says the number-preserving CAR bilinear cellular differential squares to zero on Fock space because `delta^1 delta^0=0` at `report/sections/07_toric_operator_relation.tex:83-95`. Either restrict to the one-particle sector or define the graded exterior-chain derivation and Koszul-sign extension.

- P0: AQM-15 proves alternation for arbitrary sums by checking pure tensors and appealing to bilinearity at `report/sections/15_projective_sheaf_fields_definitions.tex:216-228`. Supply the missing cross-term argument, including characteristic-2 sensitivity.

- P0: AQM-05 and AQM-12 overstate what run artifacts certify. AQM-05 says the CAR/projector algebra certifies `Q^2=0` and the anticommutator at `report/sections/05_toric_supercharge_checks.tex:108-121`; AQM-12 calls the Steane producer output exact validation at `report/sections/12_steane_clifford_koszul_morphisms.tex:156-162`. Reword summary booleans and checked hypotheses unless artifacts contain inspectable matrices, homotopies, contractions, or residuals.

- P1: AQM-14 through AQM-19 overuse "canonical", "standard", "recovers", and "not extra choices" around bases, frames, trace characters, and irreducible representations. Audit after sign anchors; likely source/local-derivation needs include finite symplectic normal form, trace-character comparison, and Stone-von Neumann hypotheses.

- P1: AQM-89's Shor homological-family sentence at `report/sections/89_scheme_incidence_code_sources.tex:198-200` needs precise local BMD locators in the shard and `references/toric_code/SOURCES.md` before it is used as a traceable source claim.

### Source, Run, Index, And Path Issues

- P1: AQM-00/AQM-02 are stale relative to current report scope and source provenance. Repair status/evidence wording before detailed claim edits so later readers see the right grounding contract.

- P1: AQM-02 still points Cahill-Glauber work through a stale marker-converted source path while the active source chain is the official arXiv source in the local manifest. Update the lab log or mark its chronological boundary.

- P2: AQM-12 cites `steane_clifford_koszul_morphisms.jl` without the full local producer path at `report/sections/12_steane_clifford_koszul_morphisms.tex:156-160`; use the indexed `scripts/lattice_codes/...` path style.

- P2: AQM-86 cites nonexistent top-level `data/arithmetic_quantum_field_examples.csv` at `report/sections/86_quantum_system_association_degenerate_overrestrictive_cases.tex:72-75`. The indexed artifact is under `runs/2026-05-24-arithmetic-quantum-fields/data/`.

- P2: Sweep short source/run paths after mathematical wording stabilizes. Repeated cases include Gottesman source paths, Stacks locators, regular-function CSV paths, and QSA catalogue rows.

### Local-Net, Descent, And Cech Issues

- P0: AQM-25 builds a "Zariski quasi-local" algebra over quasi-compact opens using AQM-24 finite-spectrum algebras at `report/sections/25_quasilocal_zariski_algebra.tex:84-99`. In affine cases, quasi-compact opens include a terminal/global object, so this does not model finite-region quasi-local behavior. Rewrite around AQM-28 finite closed supports or restrict AQM-25 to finite spectra.

- P1: AQM-28 provides the finite closed-support spine: closed finite-residue sites at `report/sections/28_closed_point_affine_arithmetic_fields.tex:13-18`, finite supports at `report/sections/28_closed_point_affine_arithmetic_fields.tex:83-107`, and open-local finite-support algebras at `report/sections/28_closed_point_affine_arithmetic_fields.tex:157-174`. Later locality/descent statements should cite and preserve this boundary.

- P1: AQM-41 sums over all `x in U` in the Cech decomposition at `report/sections/41_cech_cohomology_quantum_descent.tex:143-163`. Align this with finite closed supports or state the additional hypotheses.

- P1: AQM-39 displays "full global stabilizer state <=> global phased Lagrangian" at `report/sections/39_two_qutrit_stabilizer_descent_counterexample.tex:155-178`. Keep only the proved direction unless a converse theorem is cited; make overlap phase compatibility explicit.

- P1: AQM-45 says AQM-28 applies to `Spec Z` at `report/sections/45_spec_z_arithmetic_quantum_field.tex:129-138`, but AQM-28 is finite-type over finite fields. Treat `Spec Z` as a separate extension. Also replace "the profinite completion" at `report/sections/45_spec_z_arithmetic_quantum_field.tex:263-270` with the squarefree residue quotient/product action shown at `report/sections/45_spec_z_arithmetic_quantum_field.tex:225-240`.

### Tangent, Cotangent, And De Rham Issues

- P1: AQM-60 uses `Omega^1_{A/k}` while opening with only `X=Spec A` at `report/sections/60_tangent_weyl_operator_principle.tex:31-38`; AQM-63 repeats the missing base at `report/sections/63_evaluated_derham_constraints_tangent_weyl.tex:23-39`. Name the base map before quoting tangent/cotangent dimensions or Weyl carriers.

- P1: AQM-63 says arbitrary eigenvalue phases define a stabilizer subspace at `report/sections/63_evaluated_derham_constraints_tangent_weyl.tex:47-52`. Require phased-stabilizer compatibility, not just isotropy plus arbitrary phases.

- P1: AQM-54 says logical labels are controlled by `H^1_dR` at `report/sections/54_derivative_dynamics_f3_examples.tex:104-112`. For CSS logical Pauli data, distinguish encoded-count/cohomology control from the full cohomology-plus-dual/homology logical module.

- P1: AQM-57 derives `[[10,3,d]]`, `[[18,5,d]]`, and Bell-sector statements from compact row lists at `report/sections/57_derham_css_f2_entanglement_codes.tex:109-127` and `report/sections/57_derham_css_f2_entanglement_codes.tex:168-193`. Preserve these only after displaying the full `C^2` bases, row spaces, rank checks, and phase convention or deriving them locally in prose.

### QSA Status-Token Issues

- P1: AQM-85 imports AQM-84 proposal labels into the table vocabulary at `report/sections/85_quantum_system_association_agreement_inequivalence_table.tex:36-42`, while convention `(au)` restricts table status tokens at `CONVENTIONS.md:2109-2129`. Either add sanctioned labels to conventions or keep proposal categories in prose/witness columns.

- P1: AQM-85 groups algebraic generic sectors with analytic/completion blockers at `report/sections/85_quantum_system_association_agreement_inequivalence_table.tex:222-226`. Split locally recorded algebraic generic sectors for `F_q(t)` and `Q` from missing adelic, profinite, `C^*`, or infinite-volume completion conventions.

- P1: AQM-79 conflates localized regular functions on `D(h)` with finite closed support along `Z_cl(h)` at `report/sections/79_quantum_system_association_geometric_field_hom_x_v.tex:185-206`. Use separate symbols for localization and support selector; a general element of `F_q[x]_h` is not evaluable at support points dividing `h`.

- P2: Normalize ad hoc QSA tokens such as composite statuses, `blocked/database`, `not_claimed`, and `available locally` in the same pass. Preserve that `available` means local workflow anchor, not agreement or equivalence.

### New Haah/Laurent Torus Issues

- P0: Convention `(az)` gives the Haah excitation map the wrong role/domain: `epsilon_square = sigma_square^dagger lambda sigma_square` at `CONVENTIONS.md:2412-2418`. Correct it to `epsilon = sigma^dagger lambda : P_G -> R_G^2`; reserve `sigma^dagger lambda sigma = 0` for generator isotropy.

- P0: AQM-91 states finite-periodic toric exactness `ker epsilon_square = im sigma_square` at `report/sections/91_haah_laurent_torus_quant2.tex:162-186`, while the same shard later says finite-periodic logical labels live in `ker(sigma^dagger lambda)/im(sigma)` at `report/sections/91_haah_laurent_torus_quant2.tex:219-229`. Restrict equality to the source-local infinite Laurent translation ring unless a local finite-periodic check is added.

- P1: AQM-91 introduces `R_G` over `F_p` but identifies `P_G=R_G^4` with the qubit AQM-90 edge module over `F_2` at `report/sections/91_haah_laurent_torus_quant2.tex:77-102`. Specialize the toric-square bridge to `p=2` or split generic prime-qudit Laurent grammar from the qubit comparison.

- P1: AQM-89 header/catalogue wording says "checked Weyl-label targets" for Steane, Reed-Muller, Shor, and toric source conjectures at `report/sections/89_scheme_incidence_code_sources.tex:1-5`. Soften this to distinguish checked label selections from sourced targets, proposals, and unreconstructed naturality claims.

## Cross-Cutting Repair Plan

1. Repair convention scaffolding first: AQM-00/AQM-02 evidence/status wording, QSA status-token policy, and convention `(az)` for the Haah excitation map.
2. Fix sign/phase anchors before downstream stabilizer prose: AQM-08 sign and polarizations; AQM-22/AQM-23 source-sign bridge; AQM-58/AQM-60 tangent-cotangent sign; AQM-43 multiplier/Frobenius boundary.
3. Fix hard mathematical defects: AQM-17 Proj denominator; AQM-07 Fock-space nilpotence scope; AQM-15 alternation proof; AQM-25 locality construction.
4. Normalize evidence vocabulary: replace over-strong "exact certificate" and "validation certifies" language where artifacts are summary rows or checked hypotheses.
5. Repair locality/descent before expanding arithmetic-dynamics claims: finite closed-support spine, Cech finite-support hypotheses, stabilizer descent converse/phase compatibility, and `Spec Z` squarefree residue wording.
6. Repair tangent/de Rham claims: name bases/maps, choose signs, distinguish support spaces from phased stabilizers, and add visible rank/basis checks for de Rham CSS examples.
7. Repair QSA and catalogue layers: AQM-79 regular-function/support split, AQM-85 generic-sector/completion split, stale finite-set/status rows, and AQM-89/AQM-91 catalogue summaries.
8. Acquire sources or write local derivations before editing claims that need them: finite symplectic normal form, trace-character bridges, Stacks affine/Artinian locators, BMD Shor-family locators, Chinese remainder and finite-field trace/factorization facts, Haah infinite Laurent exactness lines, and de Rham rank/basis derivations.
9. Do the path/index/schema sweep after wording is stable: full local source paths, full run-bundle CSV paths, `INDEX.md` references, source manifests, and shard catalogue summaries.
10. This final review did not run Julia or rebuild the report. A later editing pass that changes report source should run normal validation/rebuild only when the hard command rule is no longer in force.

## Deferred And Non-Findings

- Wave 1 and Wave 2 found no explicit Blocker labels.
- AQM-72/AQM-73 were reported clean on boson/fermion/fusion boundary discipline; do not add parafermion, fusion-category, or Fock interpretation without new sources and conventions.
- QSA finite-set basics in AQM-66--AQM-71 were mostly healthy. Preserve direct-sum, finite-set, AND/OR, and empty-set carrier distinctions while cleaning stale statuses and tensor-product coherence wording.
- Finite-ring database overclaiming is mostly under control in AQM-80--AQM-83. Preserve the current boundary: schema-only SQLite, in-memory CSV review export, no arbitrary finite-ring decomposition claim, and no populated database claim unless a later run supplies it.
- Residue-site, nilpotent-sensitive, and product-ring layers in AQM-82--AQM-83 were found mostly clean. Do not collapse nilpotents into extra residue sites or upgrade selected workflows into arbitrary finite-ring classification.
- AQM-88 and AQM-90 are mostly doing the right thing: derivative predicates end as subsets/subgroups of Weyl labels via `pi^{-1}`, and AQM-90 warns about fibre saturation. Future shards should carry those caveats rather than cite them as a dynamical theorem.
- AQM-20/AQM-21 mostly preserve the Grassmann-valued caveat; if metadata is changed, keep "projective representation" wording subordinate to local Grassmann/ray-representation conventions.

## Reviewer Artifact Index

- Wave 2 S1, foundations/stabilizers/fields: [`docs/report_mega_review/wave2/S1_foundations_stabilizers_fields.md`](../wave2/S1_foundations_stabilizers_fields.md)
- Wave 2 S2, arithmetic locality/dynamics: [`docs/report_mega_review/wave2/S2_arithmetic_locality_dynamics.md`](../wave2/S2_arithmetic_locality_dynamics.md)
- Wave 2 S3, QSA catalogue: [`docs/report_mega_review/wave2/S3_qsa_catalogue.md`](../wave2/S3_qsa_catalogue.md)
- Wave 2 S4, new shards/cross-cutting: [`docs/report_mega_review/wave2/S4_new_shards_crosscutting.md`](../wave2/S4_new_shards_crosscutting.md)
- Wave 1 shard-pair reviews are under [`docs/report_mega_review/wave1/`](../wave1/). Use them for exact reviewer rationales and lower-priority local questions not repeated here.
