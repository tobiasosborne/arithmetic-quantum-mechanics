# S2 Synthesis

## Inputs

Reviewed Wave 2 instructions in `docs/report_mega_review/README.md` and
`docs/report_mega_review/WAVE2_ASSIGNMENTS.md`.

Wave 1 inputs synthesized:

- `R13_24_25.md` through `R32_62_63.md`.
- Report shards AQM-24 through AQM-63 were cross-read where needed.
- Cross-check anchors included `CONVENTIONS.md`, especially conventions `(y)`,
  `(ab)`, `(ac)`, `(ag)`, `(al)`, `(ao)`, and `(av)`.

No Julia, producer script, `make test`, or source acquisition was used.

## High-Priority Findings

1. **The locality layer repeatedly outruns the finite-closed-support convention.**

   The clearest root defect is AQM-25: it indexes a "Zariski quasi-local"
   algebra by quasi-compact opens and imports AQM-24's finite tensor-product
   algebra for each such open (`report/sections/25_quasilocal_zariski_algebra.tex:84`),
   but AQM-24 only established a finite-spectrum construction. Since an affine
   scheme is itself quasi-compact, the colimit over quasi-compact opens also
   has a terminal object (`report/sections/25_quasilocal_zariski_algebra.tex:91`).
   That collapses the intended finite-region quasi-local behavior to the global
   object whenever `A(X)` exists.

   AQM-28 fixes the right convention for infinite finite-type affine schemes
   over finite fields: closed finite-residue sites only, finite supports, and
   `A(U)=colim_{S finite subset U cap |X|_cl} A(S)`
   (`report/sections/28_closed_point_affine_arithmetic_fields.tex:13`,
   `:33`-`:45`, `:157`-`:174`; `CONVENTIONS.md:748`-`:778`). Later shards
   sometimes use that repair, but several statements still revert to broader
   wording: AQM-41 sums over all points `x in U` (`41_cech_cohomology_quantum_descent.tex:143`-`:163`),
   AQM-44 states its tower theorem for arbitrary affine `Spec R` over `k`
   (`44_trace_gauges_full_continuum_towers.tex:136`-`:153`), and AQM-45 says
   AQM-28 is literally applied to `Spec Z` (`45_spec_z_arithmetic_quantum_field.tex:129`-`:138`).

   Recommended synthesis edit: first make the finite closed-support convention
   the single spine for AQM-25 and downstream locality/descent statements. Then
   treat `Spec Z` and any generic or infinite-residue sector as explicit
   extensions, not automatic cases of AQM-28.

2. **Weyl structure shifts between `k`-linear, `F_p`-linear, mixed-residue, and multiplier-level conventions.**

   Several reviewers found correct-looking statements whose proof checks only
   the wrong structure. AQM-43's trace-normalized embeddings preserve the
   commutator, but the AQM-28 Weyl law uses the non-half multiplier
   `psi(p q')`; the multiplier preservation should be shown before claiming a
   `*`-monomorphism (`report/sections/43_finite_field_scale_continuum_limits.tex:125`-`:153`;
   compare `28_closed_point_affine_arithmetic_fields.tex:122`-`:130`). AQM-43
   also calls Frobenius a Clifford/Gaussian automorphism even though AQM-42
   defines symplectic morphisms as `k`-linear maps preserving a `k`-valued form
   (`42_gaussian_clifford_dynamics.tex:93`-`:101`), while Frobenius is only
   `F_3`-linear/semilinear over `k_r` (`43_finite_field_scale_continuum_limits.tex:232`-`:250`).

   The same scalar-field drift appears in AQM-42's Gross-Hudson wording:
   it correctly warns that the prime-power dictionary is imported after an
   `F_p`-basis choice (`42_gaussian_clifford_dynamics.tex:25`-`:28`), but later
   says pure Gaussian states are "equivalently phased Lagrangian label data"
   without restating whether the Lagrangian is `F_p`-additive or intrinsic
   `k`-linear (`42_gaussian_clifford_dynamics.tex:237`-`:243`).

   Mixed-residue supports are another instance of the same pattern. AQM-28
   explicitly says the finite-support form is not one field-valued when residue
   degrees vary and uses a character-valued bicharacter instead
   (`28_closed_point_affine_arithmetic_fields.tex:93`-`:107`). AQM-60 and
   AQM-63 should not then describe arbitrary finite supports only as ordinary
   symplectic subspaces over one field (`60_tangent_weyl_operator_principle.tex:42`-`:47`,
   `:90`-`:98`; `63_evaluated_derham_constraints_tangent_weyl.tex:23`-`:52`).

   Recommended synthesis edit: introduce a short cross-reference paragraph
   wherever the scalar category changes: intrinsic `k`-linear, `F_p`-linear
   after basis choice, additive/mixed-residue with local trace characters, and
   actual multiplier preservation.

3. **Stabilizer descent and de Rham/CSS claims need phase and matrix evidence kept visible.**

   AQM-38 proves the direction "phased Lagrangian gives a full stabilizer
   state" (`report/sections/38_lagrangian_stabilizer_descent.tex:117`-`:153`).
   AQM-39 promotes this to a displayed equivalence for "full global stabilizer
   state <=> global phased Lagrangian" (`39_two_qutrit_stabilizer_descent_counterexample.tex:155`-`:178`)
   without proving or citing the converse in that shard. It also invokes phase
   compatibility for cover generation while AQM-38 defines only the fixed
   global phased-label theorem and leaves overlap phase gluing as additional
   data (`38_lagrangian_stabilizer_descent.tex:181`-`:208`).

   AQM-63 has the same phase issue in the tangent-Weyl setting: arbitrary
   eigenvalue phases do not automatically define a nonempty stabilizer
   eigenspace; they must satisfy the phased-stabilizer compatibility condition
   already recorded in `CONVENTIONS.md` (`63_evaluated_derham_constraints_tangent_weyl.tex:47`-`:52`).

   The de Rham CSS prototype is correctly labelled as a proposal, but the
   evidence chain weakens where concrete code parameters are claimed. AQM-54
   says "logical labels" are controlled by `H^1_dR`
   (`54_derivative_dynamics_f3_examples.tex:104`-`:112`), although the CSS
   logical Pauli module also includes the dual/homology side. AQM-57 derives
   ranks, Bell sectors, and `[[n,k,d]]` parameters from compact `d_1` row lists
   without recording full `C^2` bases and row-rank checks for the ten- and
   eighteen-qubit fat rectangles (`57_derham_css_f2_entanglement_codes.tex:109`-`:127`,
   `:168`-`:193`).

   Recommended synthesis edit: patch the stabilizer equivalences before
   expanding descent language. For de Rham CSS examples, require an explicit
   finite basis, row space, rank, and phase convention before code parameters
   or Bell-sector conclusions.

4. **The arithmetic-dynamics prose overstates what the constructed action sees.**

   AQM-45's closed-prime translation action is well motivated, but the
   conclusion says the infinite algebra sees "the profinite completion"
   (`report/sections/45_spec_z_arithmetic_quantum_field.tex:263`-`:270`).
   The theorem itself shows an action through the product of residue fields and
   only then through `hat Z` after coordinatewise reduction mod `p`
   (`45_spec_z_arithmetic_quantum_field.tex:225`-`:240`). This is the
   squarefree residue quotient `prod_l F_l`, not a faithful action of the full
   profinite completion.

   The same shard's optional generic `Q` sector defines `E_eta`, `ell^2(Q)`,
   and Weyl operators but then uses `A_eta` without defining whether this is an
   algebraic span, a bounded-operator algebra, or a completion
   (`45_spec_z_arithmetic_quantum_field.tex:161`-`:183`). Given the earlier
   Stone-von Neumann boundary for countable discrete rings/fields, this should
   be labelled as a separate algebraic proposal unless completed.

5. **The thickened Artin layer is locally narrower than later wording suggests.**

   AQM-36 is an `F_3[t]/(pi^e)` top-coefficient-character construction, not yet
   a general arbitrary-finite-field Artin-Weyl convention. AQM-49 states the
   thickened comparison over `k=F_Q` and imports AQM-36 directly
   (`report/sections/49_regular_functions_affine_line_weyl_labels.tex:188`-`:213`).
   AQM-51 and AQM-52 correctly warn that Artin-ring transport does not by itself
   prove default top-coefficient character covariance, but the warning should
   be attached to every concrete repeated-factor transport paragraph.

   Also, AQM-37 advertises explicit `t^3=1` and `t^6=1` jet commutator formulas
   but only displays the `t^3` formula. This is less structural than the
   convention drift above, but it is a concrete catalogue/header mismatch.

6. **The tangent-cotangent arc still has base/sign convention drift.**

   AQM-60's advertised principle uses `Omega^1_{A/k}` but begins with only
   `X=Spec A` and omits the base map (`report/sections/60_tangent_weyl_operator_principle.tex:31`-`:38`,
   `:208`-`:217`). AQM-63 repeats the same omission
   (`63_evaluated_derham_constraints_tangent_weyl.tex:23`-`:39`). This conflicts
   with convention `(ao)` and `(av)`, which require the relative cotangent
   object to be named before quoting tangent/cotangent dimensions or Weyl
   carriers (`CONVENTIONS.md:1573`-`:1606`, `:2168`-`:2171`).

   Separately, AQM-58 uses `dp wedge dx` and the pointwise form
   `p q' - p' q` (`58_product_rings_real_line_cotangent.tex:151`-`:170`),
   while convention `(ao)` and AQM-60 use
   `beta(v)-alpha(w)`, which is the opposite coordinate sign
   (`CONVENTIONS.md:1602`-`:1606`; `60_tangent_weyl_operator_principle.tex:57`-`:64`).
   This sign must be reconciled before later commutator or stabilizer phases
   mix the real CCR comparison layer with the finite tangent-Weyl recipe.

## Repeated Patterns

- **Hypothesis widening after a correct local convention.** AQM-28, AQM-36,
  AQM-42, and convention `(ao)` often state the needed boundary precisely, but
  later shards use broader phrases such as "affine scheme", "Gaussian",
  "thickened Weyl", or "subspace" without carrying the qualifier.

- **Source/provenance gaps cluster around standard algebra facts.** The most
  repeated gaps are Euclidean/PID/UFD/factorization for `k[t]` in AQM-29 and
  AQM-35, Chinese remainder in AQM-34 and AQM-49, finite-field trace
  transitivity in AQM-44, finite irreducible enumeration in AQM-47/AQM-50, and
  exact source locators for harmonic-analysis or geometry facts in AQM-33,
  AQM-53, AQM-56, AQM-57, AQM-59, and AQM-62.

- **"Label/support/ring transport" is sometimes allowed to sound like
  "operator/state/descent theorem."** This appears in state marginal gluing
  versus stabilizer-label descent, reduced affine covariance versus thickened
  Weyl covariance, de Rham support spaces versus phased CSS stabilizers, and
  evaluated one-form labels versus stabilizer eigenspaces.

- **Finite examples are mostly arithmetically sound, but their audit trails are
  uneven.** Reviewers found few numerical/arithmetic counterexamples in the
  explicit examples. The main problem is that complete enumeration, row-rank,
  or source-anchor steps are sometimes implicit.

- **Terminology drift is low-level but cumulative.** Examples include "qutrit"
  for non-`F_3` residue-qudits or 27-dimensional jet sites, reused notation
  `q_0`, "the profinite completion" for a squarefree quotient, and "logical
  labels" for only the cohomology half of CSS logical data.

## Cross-Arc Risks

- **S1/S2 boundary:** AQM-38--AQM-41 rely on stabilizer/CSS conventions from
  the earlier foundations arc. Any final action document should coordinate
  the phased-Lagrangian converse, phase-character compatibility, and CSS
  logical-module wording with S1's review of AQM-08 and related stabilizer
  shards.

- **S2/S3 boundary:** AQM-60--AQM-63 feed directly into later QSA/tangent
  catalogue shards. If the base field, mixed-residue isotropy, carrier
  dimension, and phase compatibility wording are not fixed here, later QSA
  summaries may turn a kinematical recipe into a claimed dynamics.

- **Spec(Z) and adelic language:** AQM-45's generic `Q` sector and profinite
  wording are likely to interact with later source-gated zeta/adelic claims.
  Keep the squarefree residue quotient, algebraic generic sector, adelic
  self-dual sector, and any `C^*` completion as separate objects.

- **Thickened finite-field generalization:** AQM-49 and the regular-function
  shards may be used later as evidence for arbitrary finite-field Artin Weyl
  systems. At present the checked thickened convention is `F_3`-specific unless
  a new general Frobenius-ring/generating-character convention is added.

- **No direct Wave 1 reviewer contradiction was found.** The closest apparent
  tension is R16 reporting no issue in AQM-31 while R17 flags AQM-32/AQM-33's
  stronger Stone-von Neumann boundary language. These are compatible: R16
  explicitly warned later shards to preserve the boundary, and R17 found the
  later boundary needs a weaker Bekka approximate-equivalence case named.

## Findings To Verify Before Editing

- Verify whether AQM-25 should be deleted/restricted to finite spectra or
  rewritten to use AQM-28 finite closed supports. This decision affects AQM-26,
  AQM-41, and any use of "quasi-local" over open posets.

- Check local source availability for the recurring algebra facts before
  editing prose: `k[t]` Euclidean/PID/UFD and finite-field factorization,
  Chinese remainder, trace transitivity, finite-field tower inclusion
  `F_{q^r} subset F_{q^s}` iff `r | s`, and finite irreducible counts.

- For AQM-32/AQM-33, inspect Bekka's weaker approximate-equivalence theorem and
  decide whether it is in scope for the discrete `k(t)` model or explicitly
  out of scope.

- For AQM-38/AQM-39, verify and cite a converse theorem from full stabilizer
  states to Lagrangian label spaces before keeping displayed equivalence
  language.

- For AQM-43/AQM-44, verify the exact Weyl multiplier convention used at every
  scale. Do not rely only on commutator preservation unless the half-Weyl
  normalization is explicitly adopted.

- For AQM-57, reconstruct the `C^2` bases and row ranks by hand in the report
  text before preserving the code-parameter claims. No producer rerun is
  required for the edit, but the basis/rank evidence must be visible.

- For AQM-58/AQM-60, choose the tangent-cotangent sign convention once and
  sweep all coordinate examples that compute commutator phases.

- For AQM-63, decide the category of "subspace" for mixed finite-residue
  supports: componentwise `K_P`-linear, additive, or `F_p`-linear. Then align
  isotropy and phase language with that category.

## Recommended Action Order

1. **Repair the locality spine first.** Fix AQM-25 around finite closed
   supports or finite-spectrum restriction, then sweep AQM-41, AQM-44, AQM-45,
   AQM-60, and AQM-63 for all-points/arbitrary-affine/mixed-residue wording.

2. **Normalize Weyl convention boundaries.** Patch AQM-42/AQM-43 for
   `F_p`-additive versus `k`-linear Gross/Clifford/Gaussian claims, add the
   multiplier check in AQM-43, and mark Frobenius as semilinear or `F_p`-linear
   unless a new convention is added.

3. **Fix stabilizer and phase claims.** Patch AQM-39's equivalences, define or
   defer phase descent for overlapping covers, qualify AQM-63 phase choices,
   and add all-`+1`/support-space caveats where de Rham CSS stabilizers are
   displayed.

4. **Clean up Spec(Z) and tower overstatements.** Reword AQM-45's AQM-28
   citation, define `A_eta` or mark it as a proposal, and replace "the
   profinite completion" with the squarefree residue quotient/factored action.
   Add trace-transitivity support in AQM-44 while tightening finite-residue
   hypotheses.

5. **Constrain the thickened layer.** Restrict AQM-49's thickened comparison to
   `F_3` or add a general finite-field Artin character convention; attach the
   default-character transport caveat to AQM-51/AQM-52 concrete examples; fix
   the missing AQM-37 `t^6` formula or de-advertise it.

6. **Patch de Rham/tangent auditability.** Add base fields/maps to AQM-60 and
   AQM-63, reconcile the AQM-58/AQM-60 sign, distinguish `H^1` encoded-count
   control from full logical Pauli labels, and add the missing `C^2` basis/rank
   displays in AQM-56/AQM-57.

7. **Do the provenance sweep last.** Once mathematical wording is stable, add
   precise local source locators for the repeated standard facts and replace
   manifest-only anchors in source-sensitive shards with local path plus
   theorem/section/line references.
