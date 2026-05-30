# S1 Synthesis

## Inputs

Reviewed Wave 2 instructions:

- `docs/report_mega_review/README.md`
- `docs/report_mega_review/WAVE2_ASSIGNMENTS.md`

Synthesized Wave 1 reviews:

- `docs/report_mega_review/wave1/R01_00_01.md`
- `docs/report_mega_review/wave1/R02_02_03.md`
- `docs/report_mega_review/wave1/R03_04_05.md`
- `docs/report_mega_review/wave1/R04_06_07.md`
- `docs/report_mega_review/wave1/R05_08_09.md`
- `docs/report_mega_review/wave1/R06_10_11.md`
- `docs/report_mega_review/wave1/R07_12_13.md`
- `docs/report_mega_review/wave1/R08_14_15.md`
- `docs/report_mega_review/wave1/R09_16_17.md`
- `docs/report_mega_review/wave1/R10_18_19.md`
- `docs/report_mega_review/wave1/R11_20_21.md`
- `docs/report_mega_review/wave1/R12_22_23.md`

Cross-read local context, read-only:

- `report.tex`
- `report/sections/00_frontmatter_status.tex` through `report/sections/23_spec_z6_residue_qudit_factorisation.tex`, selectively
- `CONVENTIONS.md`
- `INDEX.md`
- `data/SCHEMA.md`
- `references/canonical_fields/SOURCES.md`
- selected existing CSV sentinels and source/library text by inspection only

No Julia, producer script, `make test`, or source acquisition was run.

## High-Priority Findings

1. **P0: Phase and sign conventions are correct locally in places but not bridged to cited sources, creating a report-wide propagation risk.**

   AQM-08 fixes `omega((x,z),(x',z'))=z*x'-x*z'` and then computes the mixed CSS pairing as `-x*z` at `report/sections/08_symplectic_css_bridge.tex:51-58` and `:89-92`, but later states the logical pairing as positive evaluation `H^1 x H_1 -> F_p` at `:222-226`. R05 also found the logical Lagrangian names swapped relative to the shard's own `(X,Z)` labels and to the Steane convention in `CONVENTIONS.md:312-319`.

   The same sign family returns in AQM-22 and AQM-23. The local convention in `CONVENTIONS.md:563-570` and `:593-596` uses the `z*x' - x*z'` commutator form, and AQM-22/AQM-23 follow it at `report/sections/22_prime_field_arithmetic_fields_qudit_paulis.tex:145-152` and `report/sections/23_spec_z6_residue_qudit_factorisation.tex:147-159`. R12 found that the cited Ashikhmin--Knill, Gottesman, and Bombin--Martin--Delgado formulas use the opposite exponent under the same apparent `(X,Z)` reading, but the report does not state the conversion.

   **Action needed:** fix the AQM-08 sign/polarization statements first, then add one explicit source-convention bridge in AQM-22 and cross-reference it from AQM-23. Otherwise later odd-prime, residue-qudit, and stabilizer-selection shards can silently inherit a flipped phase.

2. **P0: Several claims overstate what local run artifacts certify.**

   AQM-05 says the validation script certifies `Q^2=0` and the anticommutator at `report/sections/05_toric_supercharge_checks.tex:108-121`, while the CSV sentinel says it is an algebraic certificate only with no full Hilbert or ghost matrices. The code fields appear to record consequences of commuting and squaring checks rather than matrix-level identities.

   AQM-12 is more severe: it calls the output an exact Clifford/Koszul morphism certificate in the CSV sentinel and says the producer records chain-map, homotopy, 63 contractible syndrome sectors, and cohomology data at `report/sections/12_steane_clifford_koszul_morphisms.tex:156-162`. R07 found that important fields are summary booleans or hard-coded consequences, e.g. `phase_same_q_only_after_homotopy_retract = true` and `nonzero_syndrome_blocks_contractible = true`, not explicit contraction matrices or residual checks.

   **Action needed:** introduce a consistent certificate vocabulary. Use "records checked hypotheses used by the formal proof" for summary algebraic booleans, and reserve "exact certificate" for artifacts containing inspectable identities, matrices, contractions, or residuals with a schema contract.

3. **P0: Some mathematical definitions are wrong or incomplete, not merely under-cited.**

   AQM-17 describes the Proj stalk localization for a graded module using `a,b in M` with `b notin p` at `report/sections/17_projective_line_stalks.tex:54-58`. R09 correctly flags this as wrong: the denominator must be a homogeneous element of the graded ring `S`, not of the module `M`.

   AQM-07 states that a number-preserving CAR bilinear second-quantized cellular differential squares to zero on the Fock space because `delta^1 delta^0=0` at `report/sections/07_toric_operator_relation.tex:83-95`. R04 flags that this implication is immediate only on the one-particle sector unless a graded exterior-chain derivation convention with Koszul signs is actually defined.

   AQM-15 proves alternation of a tensor-product pairing for arbitrary sums by checking pure tensors and appealing to bilinearity at `report/sections/15_projective_sheaf_fields_definitions.tex:216-228`. R08 flags the missing cross-term argument, including the characteristic-2 sensitivity.

   **Action needed:** treat these as mathematical fixes before prose cleanup. They affect definitions or proof validity in the foundations/stalk/operator layer.

4. **P1: The report repeatedly calls chosen representatives, bases, frames, or irreducible representations canonical without carrying hypotheses.**

   AQM-14 chooses a symplectic basis and trace-character Weyl model at `report/sections/14_arithmetic_quantum_fields.tex:137-146`; R08 found no local source or derivation for the finite symplectic normal-form step in the theorem as stated, nor a local trace-character bridge from the source's coordinate-dot-product convention.

   AQM-18 says germ-to-value maps are "not extra choices" at `report/sections/18_stalks_as_field_germs.tex:127-129`; R10 correctly separates the canonical residue quotient from the chosen scalar frame/representative convention recorded in `CONVENTIONS.md:457-468`.

   AQM-19 says the real-target recipe recovers the standard finite bosonic canonical field at `report/sections/19_canonical_boson_fermion_field_comparison.tex:116-128`, but the Stone--von Neumann step requires regularity and irreducibility for the one-copy Schrodinger representation. The shard states this in Lemma L2 at `:110-114` but not in T1's hypothesis.

   **Action needed:** audit words like "canonical", "standard", "recovers", and "not extra choices" in AQM-14 through AQM-19. Add the missing choices or hypotheses locally before using those statements downstream.

5. **P1: Early status and provenance shards are stale relative to the current report and can mislead later editing.**

   AQM-00 says the programme is "connecting" the main themes at `report/sections/00_frontmatter_status.tex:9-11`; R01 notes this is stronger than the repository's "possible bridges" rule. Its evidence-chain paragraph at `:26-33` also requires every substantive assertion to pass through a manifest, convention, computation link, index row, and report shard, which conflicts with the alternative grounding paths in `AGENTS.md`.

   AQM-02 stops at the 2026-05-26 minimal-fermion entry at `report/sections/02_lab_log.tex:272-279`, while `report.tex:85-122` includes AQM-54 through AQM-91. It also still points the Cahill--Glauber displacement work to a marker-converted Physical Review source at `report/sections/02_lab_log.tex:66-69`, while `references/canonical_fields/SOURCES.md:71-78` says the marker chain is unavailable and the active report locator is the official arXiv source.

   **Action needed:** update AQM-00/AQM-02/AQM-03 before detailed claim edits, because they define the reader's expectations for status, evidence, and current chronology.

## Repeated Patterns

- **Short paths where full local locators are required.** R03, R06, R07, R09, and R10 all found shortened source, producer, run, or CSV paths. Examples include `Thesis.tex` instead of `references/symplectic_qecc/gottesman_9705052_source/Thesis.tex`, `steane_clifford_koszul_morphisms.jl` instead of `scripts/lattice_codes/steane_clifford_koszul_morphisms.jl`, and `data/projective_line_...csv` instead of `runs/2026-05-24-projective-line-sheaf-fields/data/...`. `INDEX.md:40-76` and `data/SCHEMA.md:18-25` show the full registered path style.

- **Convention anchors live in `CONVENTIONS.md` but are not repeated where claims first depend on them.** This occurs for toric boundary/CSS conventions, Pauli sign conventions, trace characters, projective sheaf evaluations, local frames, and qubit fourth-root phases. The report often has the right convention somewhere, but the local shard does not carry the bridge at the first sensitive use.

- **Unsigned label calculations drift into signed/operator language.** AQM-08, AQM-12, AQM-22, and AQM-23 all have versions of this issue. The most concrete Steane case is AQM-12's transversal phase: the binary label map at `report/sections/12_steane_clifford_koszul_morphisms.tex:105-143` does not restore Gottesman's sign-sensitive encoded `P^\dagger` caveat before discussing logical action.

- **"Validation" paragraphs compress proof, script, CSV, schema, and run status into a single sentence.** This creates ambiguity about whether a run checks hypotheses, emits a summary row, or provides an independent certificate. AQM-05, AQM-09, AQM-11, and AQM-12 show the same compression at different severities.

- **Projective-line material alternates between canonical scheme language and chosen finite-table conventions.** AQM-15 through AQM-18 need sharper separation between sheaf/stalk/fiber maps and the fixed rational-point representative, local-frame, and all-weights-one evaluation conventions in `CONVENTIONS.md:438-468`.

- **Source provenance can be superseded by later audits without the lab log or source anchor list being updated.** The Cahill--Glauber marker-to-arXiv migration is the clearest instance, but R08/R10 also found omitted source locators for Stacks affine morphisms and Cahill--Glauber displacement facts.

## Cross-Arc Risks

- **Downstream finite-ring and residue-Weyl claims may cite AQM-22/AQM-23 as stable phase anchors.** Until the source-sign bridge is explicit, later finite-spectrum Weyl-net or stabilizer-selection formulas can compare against external sources with the opposite commutator exponent.

- **The logical-module wording in AQM-05 can pollute the CSS bridge.** `H_1/H^1` at `report/sections/05_toric_supercharge_checks.tex:201-202` is not a defined quotient and conflicts with the later `H^1 \oplus H_1` module at `report/sections/08_symplectic_css_bridge.tex:208-226`.

- **Ghost/cohomology language can blur physical code states with presentation-dependent derived data.** R06 found AQM-10/AQM-11 mostly correct here, but R07's AQM-12 certificate and signed-phase findings show how easy it is to overstate higher ghost sectors or presentation equivalences.

- **The projective sheaf field arc is internally promising but fragile.** The local CSV/register layer exists in `INDEX.md:48-49` and `:72-76`, but the report text must not treat finite rational-point scalar rows as intrinsic global scalar functions or canonical fiber values independent of local frames.

- **The frontmatter's overstrict evidence-chain wording can cause false negatives in later review.** If every assertion is said to need all five links in `report/sections/00_frontmatter_status.tex:26-33`, then source-only statements, local derivations, open questions, and generated-data claims are not distinguishable.

- **No direct contradiction between Wave 1 reviewers was found.** Apparent tensions are complementary: R03 questions toric run-evidence wording while R04 confirms a formal proof exists nearby; R10 says AQM-19's AQM-20 cross-reference overclaims, while R11 confirms AQM-20/AQM-21 themselves maintain the Grassmann-valued caveat.

## Findings To Verify Before Editing

- **Confirm the intended global Pauli/Weyl sign convention before changing formulas.** R05 and R12 agree that the local report convention is internally coherent in several places, but source comparisons need a deliberate bridge. Editing should not flip formulas piecemeal.

- **Decide whether AQM-07's cell-fermion construction is meant as a one-particle statement or a full exterior-chain differential.** The fix is different: restrict the claim to the one-particle sector, or define the odd derivation/Koszul-sign extension.

- **Inspect the Steane Clifford/Koszul producer contract before changing "exact certificate" language.** R07's evidence points to summary booleans, but an editor should verify whether any companion artifact, generator-map CSV, or proof text is meant to be the inspectable certificate before downgrading the claim.

- **Check the exact Stacks locator for affine morphisms before adding it to AQM-15's source list.** R08 points to `references/algebraic_geometry/stacks_project_schemes.tex:840-963`; use the manifest's current locator style when editing.

- **Verify whether AQM-02 should be current through AQM-91 or explicitly bounded.** Updating the full lab log is larger than the local S1 arc, so the safer edit may be to mark the chronological boundary and defer later entries to a separate pass.

- **Check whether catalog and shard keyword metadata also need terminology fixes.** R11 flags `projective representation` metadata for AQM-20; if report text is changed to "Grassmann-valued ray representation", the catalog keyword should follow in the same non-review edit.

## Recommended Action Order

1. **Repair status/provenance scaffolding first.** Reword AQM-00's programme and evidence-chain language; either update AQM-02 through the current report state or declare its boundary; update the Cahill--Glauber provenance to the active arXiv source chain.

2. **Fix phase/sign anchors before downstream mathematical edits.** Correct AQM-08's sign and logical polarization names; add the explicit source-sign bridge in AQM-22 and point AQM-23 to it; add the AQM-23 `p=2` unphased-representative caveat.

3. **Fix hard mathematical defects.** Correct the AQM-17 Proj denominator formula, the AQM-07 Fock-space nilpotence claim, and the AQM-15 arbitrary-sum alternation proof.

4. **Normalize evidence and certificate language.** Update AQM-05, AQM-09, AQM-11, and AQM-12 validation paragraphs so each says exactly whether the artifact is a summary, checked-hypothesis record, exact algebraic certificate, or matrix/homotopy certificate. Update schema wording if it currently promises more than the artifact contains.

5. **Add missing local source/convention anchors.** Prioritize AQM-14's finite symplectic normal form and trace-character convention, AQM-15's affine-morphism locator, AQM-19's Cahill--Glauber locators, Gottesman full local paths in Steane shards, and full run/CSV paths in AQM-16/AQM-17/AQM-18.

6. **Tighten "canonical/standard" wording.** Add the chosen-frame caveat to AQM-18, the regular irreducible hypothesis to AQM-19 T1, and the Grassmann-valued qualifier to AQM-20 metadata.

7. **Re-run the normal validation only after report edits are made by a later editing pass.** This review wave did not run Julia by instruction; any final edit pass that changes report source should rebuild/validate according to project policy.
