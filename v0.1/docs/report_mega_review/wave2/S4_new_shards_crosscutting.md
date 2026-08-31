# S4 Synthesis

## Inputs

Read under the hard command rule: no Julia, no `make test`, no
`scripts/run_all.jl`, and no producer scripts.

- Review scaffolding: `docs/report_mega_review/README.md`,
  `docs/report_mega_review/WAVE2_ASSIGNMENTS.md`.
- Direct Wave 1 inputs: `docs/report_mega_review/wave1/R45_88_89.md`,
  `docs/report_mega_review/wave1/R46_90_91.md`.
- Earlier pattern reviews cross-read for source/convention risks:
  `R02`, `R03`, `R04`, `R05`, `R06`, `R08`, `R12`, `R22`, `R30`,
  `R31`, `R32`, `R40`, `R41`, `R42`, `R43`, and `R44`.
- New shards: `report/sections/88_derivative_constraints_residue_weyl.tex`,
  `89_scheme_incidence_code_sources.tex`,
  `90_algebraic_torus_quant2.tex`, and
  `91_haah_laurent_torus_quant2.tex`.
- Maps and source/convention anchors: `CONVENTIONS.md`,
  `report/README.md`, `report/SHARD_CATALOG.md`, `report.tex`,
  `INDEX.md`, `references/lattice_stabilizer_codes/SOURCES.md`,
  `references/toric_code/SOURCES.md`,
  `references/algebraic_geometry/SOURCES.md`, and
  `references/symplectic_qecc/SOURCES.md`.

## High-Priority Findings

1. Major: AQM-91 blurs Haah's infinite Laurent-ring toric exactness with the
   finite-periodic quotient `R_G`.

   Location: `report/sections/91_haah_laurent_torus_quant2.tex:162-186`.

   The shard defines `epsilon_square : P_G -> R_G^2`, sets
   `C_comm(G)=ker epsilon_square`, and then displays
   `ker epsilon_square = im sigma_square` as the strong toric exactness
   statement. The same shard later says the quotient
   `ker(sigma^dagger lambda)/im(sigma)` is where finite-periodic logical Weyl
   labels should be recorded (`91:219-229`). The local Haah thesis locator
   registered in `references/lattice_stabilizer_codes/SOURCES.md` supports the
   source-local exactness over the translation-invariant Laurent module
   (`alg-theory.tex:1515-1567`), not an already-checked equality after imposing
   `(X^N_x-1,Y^N_y-1)`.

   Threat: this can make later arithmetic-field dynamics treat the logical
   quotient as zero by default. It also conflicts with the report's own
   finite-periodic lesson in `91:219-229`.

2. Major: AQM-91 and convention `(az)` mix generic prime-qudit `F_p` notation
   with the qubit `F_2` edge module used to identify the AQM-90 square complex.

   Location: `report/sections/91_haah_laurent_torus_quant2.tex:77-102`;
   `CONVENTIONS.md:2382-2399`.

   `R_G` is introduced over `F_p`, then `P_G=R_G^4` is identified with
   `F_2^{G x {x,y}}_q direct_sum F_2^{G x {x,y}}_p`. That identification is
   literal only after specializing the Haah label field to `p=2`, while AQM-90
   explicitly uses qubit edge labels (`90:193-220`). Generic prime-qudit
   Laurent modules and the qubit toric-square bridge need to be separated.

   Threat: this repeats the older report-wide scalar-field drift seen in
   R22 and R32, where `F_p`-additive, `k`-linear, mixed-residue, and qubit
   structures can be visually collapsed.

3. Major cross-cutting convention defect: convention `(az)` writes the Haah
   excitation map as the generator-commutation expression.

   Location: `CONVENTIONS.md:2414-2418`, compared with
   `report/sections/91_haah_laurent_torus_quant2.tex:162-179`.

   AQM-91 correctly distinguishes
   `epsilon_square = sigma_square^dagger lambda_2 : P_G -> R_G^2` from the
   isotropy equation `sigma_square^dagger lambda_2 sigma_square=0`. The
   convention currently says the excitation map is
   `sigma_square^dagger lambda sigma_square`, which has the wrong role and
   domain. Because conventions govern future shards, this is more dangerous
   than an isolated wording issue.

4. Major: AQM-89's Shor homological-family claim lacks a precise local
   source-locator chain in the shard and manifest.

   Location: `report/sections/89_scheme_incidence_code_sources.tex:198-200`.

   R45 found local BMD support at
   `references/toric_code/bombin_martin_delgado_0605094_source/HomologicalErrorCorrection6.tex:320-321`
   and `:2492-2493`, but `references/toric_code/SOURCES.md` currently lists
   different toric/homological locators. The claim is plausible and apparently
   source-local, but the report sentence is not yet traceable at the precision
   required by the repository rules.

5. Moderate-to-major status drift: AQM-89 is careful in the body, but the
   shard header/catalogue wording compresses unlike evidence states into
   "checked Weyl-label targets."

   Location: `report/sections/89_scheme_incidence_code_sources.tex:1-5`;
   `report/SHARD_CATALOG.md:803-809`.

   Steane and Reed-Muller contain local displayed label selections; Shor is a
   sourced incidence target whose natural homological surface complex is not
   reconstructed; toric needs group law, chosen generators, and face
   convention. The summary language risks upgrading "candidate source route
   plus checked label subgroup" into "scheme constructs the code."

## Repeated Patterns

- Source locator precision is still the most common traceability failure.
  The same pattern appears in R02, R03, R06, R08, R30, R44, and R45: the
  needed source often exists locally, but report prose or manifests do not
  name the local path and line range.

- Convention text can lag behind corrected shard text. R30 found tangent
  symplectic sign drift; R43 found status-token drift; R46 found `(az)` using
  the wrong Haah excitation-map formula. Convention fixes should trigger a
  sweep because later shards cite conventions as ground truth.

- Bare-object-to-structure upgrades are a recurring overclaim risk:
  `Spec(F_p)` versus the underlying set of `F_p` in R12, finite set versus
  tensor/direct-sum carriers in QSA reviews, residue site versus tangent data
  in R31/R32, bare finite scheme versus incidence complex in AQM-89, and
  coordinate Laurent ring versus translation Laurent ring in AQM-91.

- Field and scalar discipline keeps reappearing. The S4 arc adds the
  `F_p`/`F_2` Haah bridge issue to earlier `F_p`-additive versus `k`-linear
  Gaussian/stabilizer issues and mixed-residue support warnings.

- "Checked identity" and "source-local theorem" need to stay separate.
  AQM-90 checks a finite square boundary identity; Haah sources an infinite
  Laurent exactness result; finite-periodic logical quotients remain objects
  to compute or state as possible nonzero quotients.

## Cross-Arc Risks

- AQM-88 and AQM-90 are mostly doing the right thing: derivative predicates end
  as subsets/subgroups of Weyl labels via `pi^{-1}`, and AQM-90 explicitly
  warns that finite-support derivative predicates need fibre saturation. The
  risk is downstream: future shards may cite these as a dynamical principle
  without carrying the named family `F`, image definition, and fibre-saturation
  caveat.

- AQM-89 should be kept as a finite incidence precursor unless it explicitly
  cites or defers the Haah/Laurent layer. Otherwise the constant-group-scheme
  Cayley square can be mistaken for the sourced translation-invariant
  Laurent-module formalism introduced in AQM-91.

- AQM-91's exactness wording threatens adjacent sections more than AQM-90 does.
  If copied into later Haah/fracton/lattice-stabilizer discussions, it could
  erase finite periodic logical labels before any local computation or run has
  measured them.

- The convention `(az)` defect threatens every future shard that asks for
  "the excitation map." Fixing only AQM-91 would leave the wrong formula in
  the repository's convention layer.

- The source manifest for `references/lattice_stabilizer_codes/SOURCES.md`
  is strong and useful. The remaining risk is misuse: the S4 shards use Haah
  for toric/free-module grammar, not for a new Haah-code or fracton
  construction. Preserve that scope boundary.

## Findings To Verify Before Editing

- Recheck the local Haah thesis lines `alg-theory.tex:1515-1567` before
  rewriting exactness, and confirm whether the equality is being quoted only
  over the infinite translation ring.

- Recheck the orientation-equivalent toric matrix against AQM-90's edge
  convention before changing row order, bars, or `X^{-1}`/`Y^{-1}` notation.
  The reported issue is not the matrix orientation itself.

- Verify whether the intended AQM-91 bridge is qubit-only. If yes, specialize
  to `p=2` before `P_G=R_G^4 ~= F_2^{G x {x,y}}_q direct_sum ...`; if no,
  split the generic prime-qudit paragraph from the AQM-90 qubit comparison.

- Confirm the BMD Shor-family locators from R45 before adding them to
  `references/toric_code/SOURCES.md` and AQM-89.

- Confirm the Stacks Artinian locators
  `references/algebraic_geometry/stacks_project_algebra.tex:12728-12765`
  before adding them to the AQM-89 source anchors or the algebraic-geometry
  manifest.

## Recommended Action Order

1. Fix convention `(az)` first: define `epsilon = sigma^dagger lambda` as the
   excitation map and reserve `sigma^dagger lambda sigma = 0` for generator
   isotropy. Then sweep AQM-91 wording against the corrected convention.

2. Reword AQM-91 exactness so the equality is source-local over Haah's
   infinite Laurent translation ring, while finite `R_G` records the quotient
   `ker epsilon_square / im sigma_square`.

3. Split or specialize the AQM-91 `F_p`/`F_2` bridge. The safest local edit is
   to say the toric-square comparison is the `p=2` specialization and leave
   generic prime-qudit Laurent modules as a separate source-local grammar.

4. Repair AQM-89 provenance: add the Shor-family BMD locators and the Artinian
   Stacks locators where the claims are made, with matching manifest updates.

5. Soften AQM-89 and `report/SHARD_CATALOG.md` summaries so they distinguish
   checked Weyl-label selections from sourced targets, proposals, and
   unreconstructed naturality claims.

6. Add one explicit AQM-89 sentence saying the Haah/Laurent-polynomial layer is
   deferred to AQM-91, or cite the Haah manifest only for that later framing.
