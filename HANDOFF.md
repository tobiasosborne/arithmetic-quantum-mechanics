# HANDOFF.md

Session-state file for incoming agents. This is not an authoritative source for
mathematical claims; use `report.tex`, `INDEX.md`, `CONVENTIONS.md`, and local
source manifests for that.

## Current Frontier

**Derivative constraints on residue Weyl elements:** `AQM-88-DERIVATIVE-CONSTRAINTS-RESIDUE-WEYL`
is the active corrected shard for the user's coarse dynamics direction.  The
new convention is `CONVENTIONS.md` `(aw)`: a named regular coordinate family
`F <= A` and derivative predicate `P` produce a selected label subset
`C_P(S,F) <= E_S`, hence selected elements `pi^{-1}(C_P(S,F))` in the
residue Weyl-Heisenberg group.  The shard's examples show that
`Z/6Z` gives qubit-factor tensor qutrit-factor Weyl kinematics with no
derivative rejection, dual numbers have derivative data but no reduced
residue rejection, and `F_3[t]/(t^2(t-1))` has genuine shallow-depth
selection/rejection that disappears after enlarging the map family.

**New user-directed meta-plan frontier:** the quantum-system association
programme is scaffolded in
`docs/quantum_system_associations/PLAN.md` and
`AQM-64-QUANTUM-SYSTEM-ASSOCIATION-META-PLAN`. The planned shard chain is
tracked by Beads `aqm-qsa01` through `aqm-qsa23`. These beads are planning and
review/new-shard tasks; they should not assert new mathematics without local
sources, conventions, checked derivations, tests, or run artifacts.
`AQM-65-QSA-VOCABULARY` records the Step 01 vocabulary contract, and
`AQM-66-QSA-TEST-OBJECT-CATALOGUE` records the Step 02 object catalogue/status
matrix.  `AQM-67-QSA-FINITE-SET-FIRST-ASSOCIATION` records the Step 03
structureless finite-set carrier convention and checked empty, one-point, and
`n`-point derivation, with the Gram matrix explicitly marked as extra data.
`AQM-68-QSA-FINITE-SET-TENSOR-SITES` records the Step 04 tensor-site workflow:
one finite-dimensional Hilbert carrier or observable algebra per finite-set
site is explicit extra data; tensor products and tensor-by-identity inclusions
are formal finite-dimensional bookkeeping; AQM-14, AQM-22, AQM-24, AQM-25,
and AQM-40 are used only as anchored uniform-qudit/review cases, not as a
general bare-set theorem.  `AQM-69-QSA-FINITE-SET-DIRECT-SUM-PARTICLE`
records the Step 05 direct-sum particle workflow: after adding one internal
finite-dimensional complex carrier or Hilbert space per site, the carrier is
the finite direct sum over sites; empty and one-point cases are explicit; the
workflow is kept separate from AQM-68 tensor-site coexistence; and comparison
with AQM-67's formal carrier is only a vector-space identification after
choosing one-dimensional internal carriers and per-site basis vectors, with
Hilbert inner products still extra data.  `AQM-70-QSA-AND-OR-MANY-PARTICLE-GRAMMAR`
records the Step 06 finite AND/OR grammar: atoms are finite-dimensional
carriers already supplied by AQM-68/AQM-69, AND is finite tensor/coexistence,
OR is finite direct-sum/alternative, and particle-count sectors are identified
by a recursive finite grading.  The shard explicitly defers infinite-particle
completions and separates this elementary grammar from symmetric,
antisymmetric, para, Fock, and fusion-category enhancements.
`AQM-71-QSA-SYMPLECTIC-FIELD-LABELS-SET` records the Step 07 review of
`Map(X,V)`, finite-support variants, pointwise pairings, radical quotients,
Weyl labels, and checked `F_3` CSV rows.  `AQM-72-QSA-BOSON-FERMION-LAYER`
records the Step 08 review of finite bosonic real symplectic CCR fields,
finite fermionic CAR/Clifford fields, and Grassmann-Weyl displacement calculus
inside the Grassmann-extended CAR algebra; parafermion, fusion-category, and
finite AND/OR equivalence variants remain explicit gaps.
`AQM-73-QSA-FUSION-CATEGORY-ENDPOINT` records Step 09 as a gap shard only:
fusion categories are kept as a future association family, while hom spaces,
simple objects, tensor/fusion rules, associator/F-symbol data, pivotal or
spherical structure, optional braiding and R-symbol data, lattice/string-net
input, Hilbert carrier choices, local constraints, Hamiltonians/projectors,
and quantum-double/Drinfeld-center claims all remain deferred until sources
and conventions are registered.  `AQM-74-QSA-SINGLE-PARTICLE-REDUCTION`
records Step 10 as a finite carrier-map inventory: the direct-sum particle
carrier is its own single-particle sector, AQM-70 degree-one sectors and the
site-option expression compare to it by explicit maps, the one-dimensional
internal-space case compares with AQM-67 only after basis/unit and Gram
choices, and tensor, field-label, CCR/CAR/Fock, statistics, phase, and
missing-Gram obstructions remain boundaries rather than general reductions.
`AQM-75-QSA-WHAT-COUNTS-AS-A-POINT` records Step 11 as a point-selection
synthesis: underlying sets, rational points, closed points, generic points,
and all scheme points are separate indexing choices with named object classes.
Closed finite-residue points remain the finite Weyl-site convention for the
current arithmetic shards; rational points are finite truncations when
selected; generic and infinite-residue sectors remain gaps unless an explicit
separate representation or completion convention is fixed.
`AQM-76-QSA-COTANGENT-FIRST-ASSOCIATION` records Step 12 as the geometric
first-association workflow: after AQM-75 point selection, convention `(ao)`
attaches \(T^*_{X/k,x}\), \(T_{X/k,x}\), the phase label
\(T_{X/k,x}\oplus T^*_{X/k,x}\), and the canonical symplectic pairing before
using finite Weyl-Heisenberg carriers.  It inventories only the local
AQM-58--AQM-63 examples; intrinsic-versus-relative cotangent choices remain
for Step 13, and finite-ring database-backed cotangent rows remain pending
`aqm-qsa-frcot01`.  `AQM-77-QSA-INTRINSIC-RELATIVE-COTANGENT` records Step 13:
convention `(av)` separates intrinsic/local cotangent
\(\mathfrak m_x/\mathfrak m_x^2\) from relative Kahler cotangent
\(\Omega^1_{A/B}\otimes_A\kappa(x)\) over a named base \(B\).  It gives exact
local examples where they agree, where changing the base removes one tangent
direction, and where the relative cotangent over \(\mathbb Z\) vanishes while
the intrinsic local cotangent is nonzero.  Finite-ring database-backed
cotangent rows remain pending `aqm-qsa-frcot01`.  `AQM-78-QSA-FINITE-PHASE-WEYL-KINEMATICS`
records Step 14 as the common Weyl-Heisenberg representation step after finite
phase labels are fixed.  It separates finite-field vector-space carriers,
finite Frobenius-ring Pauli/stabilizer support, Solomon-style generalized
finite Heisenberg cases, and unresolved all-finite-ring classification gaps;
it also keeps Clifford/Weil classification and dynamics separate from the
Pauli/error-basis layer.  `AQM-79-QSA-GEOMETRIC-FIELD-HOM-X-V` records Step
15 as a review of the geometric field-space branch: finite all-map and
structured subspace choices, closed-point finite-support residue fields,
projective sheaf-section replacements, regular-function profiles versus
finite smearings, rational truncations, radicals, and observable nets.  It
keeps `Hom(X,V)` as a prompt label only, with the actual field-space
restrictions tied to conventions `(q)`, `(r)`, `(v)`, `(w)`, `(y)`, `(ak)`,
and `(al)` plus AQM-14--AQM-18, AQM-24--AQM-30, AQM-49--AQM-52, AQM-75, and
AQM-78.  `AQM-80-QSA-FINITE-RING-EXAMPLE-MATRIX` records Step 16 as a
gap-aware finite-ring synthesis matrix.  It separates point/residue,
cotangent-first, field-label, and nilpotent-sensitive rows for
`\mathbb F_3`, `\mathbb F_3^2`, `\mathbb Z/6\mathbb Z`,
`\mathbb F_3[e]/(e^2)`, `\mathbb F_3[t]/(t^3)`, `t^n=1` examples,
`\mathbb F_3[u,v]/(u^2,v^2)`, `\mathbb Z/4\mathbb Z`, and the blocked
`\mathbb F_2[x]/(x^2+x)` quotient-collapse candidate.  It keeps the
2026-05-26 finite-ring database run at schema-only SQLite plus in-memory MVP
review-export status, and carries blockers `aqm-qsa-frres01`,
`aqm-qsa-frcot01`, `aqm-qsa-artin01`, and `aqm-qsa-collapse01`.
`AQM-81-QSA-RESIDUE-FIELD-SITE-ASSOCIATION` records Step 17 as a Review/New
residue-site workflow for sourced finite cases only: choose the finite
prime/maximal points being used, attach each residue field `\kappa(x)`, form
local labels `\kappa(x)^2`, carriers `\ell^2(\kappa(x))`, and local algebras
`End(\ell^2(\kappa(x)))`, then assemble finite supports by direct sums of
local phase groups and tensor products of local carriers.  It highlights
`\mathbb Z/6\mathbb Z` as a mixed-residue warning
`\mathbb F_2^2 \oplus \mathbb F_3^2` with
`\ell^2(\mathbb F_2) \otimes \ell^2(\mathbb F_3)`, not one common-field
vector space.  It keeps `\mathbb Z/4\mathbb Z` and
`\mathbb F_3[\epsilon]/(\epsilon^2)` database rows blocked by
`aqm-qsa-frres01` except for explicitly local anchors, and leaves nilpotent
Artin-Weyl carriers to Step 18.  `AQM-82-QSA-NILPOTENT-SENSITIVE-ASSOCIATION`
records Step 18 as a Review/New comparison between reduced residue-site
models and the locally developed thickened Artin/Frobenius-ring Weyl layer.
It uses AQM-31, AQM-36, AQM-37, AQM-80, and AQM-81 only: dual numbers and the
`t^n=1` family are available because AQM-36 supplies the top-coefficient
generating-character proof, while arbitrary finite rings, two-direction Artin
examples, and certified generating characters beyond those local examples
remain blocked.  Nilpotents are not extra points in this convention; they are
local jet/internal degrees at existing reduced points, or they remain a gap.
`AQM-83-QSA-PRODUCT-RINGS-TENSOR-FACTORS` records Step 19 as a Review shard
for the product-field residue-site workflow.  It uses AQM-40 to keep
`\Spec(k^n)` as `n` residue-field Weyl tensor factors, uses AQM-68 to compare
that selected workflow with structureless finite-set tensor sites, and uses
AQM-58/AQM-80 to keep zero cotangent labels and database/helper gaps visible.
It treats `\mathbb Z/6\mathbb Z` only as the existing mixed-residue warning
and carries quotient-collapse, arbitrary residue decomposition/order,
database cotangent rows, and unsupported thickened product layers as gaps.
`AQM-84-QSA-INFINITE-RING-BOUNDARIES` records Step 20 as a Review/New boundary
shard.  It classifies `\Spec\mathbb F_q[t]`, `\Spec\mathbb F_q[x,y]`, and
`\Spec\mathbb Z` constructions as finite-support, algebraic quasi-local,
reference-vector incomplete tensor, formal infinite-volume,
generic-sector proposal, or completion proposal.  It keeps generic points out
of the finite Weyl-site layer by default and records missing conventions for
infinite residue fields, analytic/local completions, `C^*`-completions,
adeles/profinite sectors, and generic-point Hilbert spaces.
`AQM-85-QSA-AGREEMENT-INEQUIVALENCE-TABLE` records Step 21 as a New
gap-first synthesis shard.  It uses convention `(au)` status
tokens, aggregates only locally witnessed agreements/inequivalences from
AQM-65--AQM-84, rejects dimension equality as agreement evidence, and carries
blockers `aqm-qsa-src02`, `aqm-qsa-frres01`, `aqm-qsa-frcot01`,
`aqm-qsa-collapse01`, and `aqm-qsa-artin01`.
`AQM-86-QSA-DEGENERATE-OVERRESTRICTIVE-CASES` records Step 22 as a New
failure-mode catalogue.  It keeps collapsed presentations, radical quotients,
too-little-structure cases, zero cotangent labels, nilpotent-forgetting
reduced rows, mixed-residue not-applicable readings, unsupported quotient
collapse candidates, and infinite-representation boundaries visible as
separate status rows.  `AQM-87-QSA-OPEN-PROBLEMS-NEXT-TARGETS` records Step
23 as the first-pass closing gap ledger.  It prioritizes source/convention
acquisition, finite-ring database/residue/cotangent audits, quotient collapse
and two-direction Artin examples, finite Weyl representation-classification
boundaries, single-particle/Fock/statistics comparisons, infinite/generic and
analytic completions, dynamics selection, and noncommutative/nonunital
extension questions.  It carries `aqm-qsa-src02`, `aqm-qsa-frres01`,
`aqm-qsa-frcot01`, `aqm-qsa-collapse01`, and `aqm-qsa-artin01` without
reinterpretation.  Do not promote the AQM-85 ledger, AQM-86 failure-mode
catalogue, or AQM-87 gap ledger to final equivalence or no-go theorems
without new local maps, invariants, obstructions, sources, or runs.

**Next-agent default task:** continue the finite commutative ring database
implementation chain, not older report-frontier material, unless the user
redirects. Start from `docs/finite_commutative_ring_database_prd.md`,
`docs/finite_commutative_ring_database_implementation_plan.md`, convention
`(an)` in `CONVENTIONS.md`, the current Beads state, and the finite-ring run
bundle at `runs/2026-05-26-finite-ring-database/`. The main finite-ring chain
has progressed through acceptance bead `aqm-6t4`, and the order-1 GAP-enabled
validation bead `aqm-tcv` is closed. The current finite-ring follow-up
`aqm-cbz` replaces the conservative order-1 GAP status limitation with exact
element-level `SmallRing` identity status counts for orders `1..15`, using the
registered `Elements(R)`, equality, multiplication, and identity-law source
locators. This is still installed-tool metadata only: no presentations are
imported, no SQLite rows are written, and no populated/audited finite-ring
database completeness claim is available. Do not add report shards from this
slice unless a later task asks for report integration.

Initial infrastructure is in place for a lab-book style research workspace
about Weil/zeta functions, arithmetic quantum mechanics, supersymmetric quantum
mechanics, and Kitaev/Levin-Wen/toric-code models. The current arithmetic-field
frontier is projective: `AQM-15-PROJECTIVE-SHEAF-FIELD-DEFINITIONS` and
`AQM-16-PROJECTIVE-LINE-SHEAF-FIELD-CALCULATION` replace naive projective
`Hom(X,V)` by chosen sheaf-section spaces \(H^0(X,\mathcal L)\otimes V\), and
`AQM-17-PROJECTIVE-LINE-STALKS` works out the rational-point stalks whose
residues give the finite evaluation rows.

The current canonical-field comparison frontier is
`AQM-19-CANONICAL-BOSON-FERMION-FIELD-COMPARISON`: finite bosons fit the
field-label recipe by taking `Map(X,R_q x R_p)` with the summed real symplectic
form and applying Stone-von-Neumann uniqueness, while finite fermions fit via
CAR/Clifford data on `Re(Z x conjugate(Z))` and antisymmetric Fock space.

The sharper Grassmann-Weyl result is now split across
`AQM-20-GRASSMANN-WEYL-FERMION-DISPLACEMENTS` and
`AQM-21-GRASSMANN-WEYL-FERMION-DERIVATIONS`: after converting the local
`PhysRevA.59.1538.pdf` with `marker`, the report records and proves the
positive Cahill-Glauber theorem.  The abstract Grassmann displacement symbols
have the unitary representation
`D(gamma)=exp(sum_i (a_i^* gamma_i - gamma_i^* a_i))` in the
Grassmann-extended finite CAR algebra, with the Grassmann-valued ray product.
The ordinary complex Hilbert-space scalar-projective version remains a
boundary caveat, not the main theorem.

The latest arithmetic-field frontier is
`AQM-22-PRIME-FIELD-ARITHMETIC-FIELDS-QUDIT-PAULIS`: for a prime field
`F_p`, `Spec(F_p)` is one point and gives one qudit, while the underlying set
`F_p` has `p` points.  Taking `E=Map(F_p,F_p^2)` with the quotient-field target
`Frac(F_p)^2=F_p^2` gives exactly the standard odd-`p` qudit Pauli group and
the same projective qubit labels with the usual fourth-root phase adjustment.
Actual stabilizer codes require an extra isotropic label subspace and phases.

The newest finite-spectrum calculation is
`AQM-23-SPEC-Z6-RESIDUE-QUDIT-FACTORISATION`: `Spec(Z/6Z)` has two prime
ideals `(2)` and `(3)` with residue fields `F_2` and `F_3`.  The residue-field
Weyl label group is `F_2^2 direct_sum F_3^2`, but the Hilbert space is the
tensor product `C^2 tensor C^3`, not the direct sum `C^2 direct_sum C^3`.
Consequently the observable algebra is `M_2(C) tensor M_3(C) ~= M_6(C)`.

The newest Zariski-locality convention is
`AQM-24-ZARISKI-OPENS-OBSERVABLE-NETS`: for a finite affine spectrum,
open sets carry the algebras acting nontrivially on those open sets,
`U |-> A(U)`, giving covariant inclusions.  The tempting assignment
`U |-> A(X \ U)` is recorded as a closed-complement/vanishing-locus support
assignment and is contravariant in opens.

The quasi-local algebra convention is now
`AQM-25-QUASILOCAL-ZARISKI-ALGEBRA`: build the primary algebra as the filtered
colimit over quasi-compact Zariski opens, `colim_U A(U)`.  Closed complements
are not discarded, but are reindexed by closed supports `Z` ordered by
inclusion and treated as a separate closed-support/defect construction.

The presheaf/cosheaf frontier is now
`AQM-26-PRESHEAVES-COSHEAVES-OBSERVABLE-NETS`: the open-local observable
assignment is a precosheaf/local net of unital `*`-algebras, not an ordinary
cosheaf in that category.  The obstruction is explicit for
`Spec(Z/6Z)`: ordinary cosheaf gluing would use `M_2 *_C M_3`, while the
physical algebra is `M_2 tensor M_3`.  The Weyl label assignment
`E(U)=direct_sum_{x in U} E_x` is the cosheaf-like layer.

The newest state-side shard is
`AQM-27-STATE-PRESHEAF-QUASILOCAL-ALGEBRA`: local quantum states form a
presheaf of convex sets by restriction along algebra inclusions.  They are not
generally a sheaf: marginals do not determine correlations, and compatible
overlapping marginals can fail to glue.  For the algebraic quasi-local algebra,
`State(A_qloc(X))` is the inverse limit of the local state spaces.

The newest stabilizer local-to-global layer is
`AQM-38-LAGRANGIAN-STABILIZER-DESCENT` and
`AQM-39-TWO-QUTRIT-STABILIZER-DESCENT-COUNTEREXAMPLE`: a phased Lagrangian
label subspace is a full stabilizer state, while zero descent defect is the
extra condition that the stabilizer is generated from a chosen cover.  The
explicit two-qutrit `F_3` Lagrangian generated by `(1,0,-1,0)` and
`(0,1,0,1)` is a full global stabilizer with no nonzero one-site stabilizer
labels, so the broad equivalence between full stabilizer choice and
local-to-global gluing is rejected in that form.

The newest finite-spectrum product example is
`AQM-40-PRODUCT-FIELD-SPECTRUM-QUDIT-STABILIZERS`: for `R = k^n`, the
arithmetic space is `X = Spec(R)`, which has `n` discrete points with residue
field `k`, not `q^n` points.  The resulting residue-qudit field is exactly the
ambient `n` `q`-level qudit Weyl/Pauli net; stabilizer codes remain extra
isotropic additive label subgroups plus phases.

The newest affine arithmetic-field layer is
`AQM-28-CLOSED-POINT-AFFINE-ARITHMETIC-FIELDS`,
`AQM-29-SPEC-FQ-T-ARITHMETIC-FIELD`, and
`AQM-30-SPEC-FQ-XY-ARITHMETIC-FIELD`: for affine schemes of finite type over
`F_q`, finite Weyl/qudit sites are closed points with finite residue fields.
Generic and curve-generic points still control the Zariski geometry, but they
are not finite Weyl sites until an infinite-residue representation convention
is added.  `Spec(F_q[t])` gives one `q^deg(pi)`-level qudit for each monic
irreducible `pi`; `Spec(F_q[x,y])` gives a full closed-point quasi-local
algebra whose rational-point truncation is only the finite `q^2`-site
subtheory.

The newest affine-line symmetry layer is
`AQM-46-AFFINE-LINE-SYMMETRY-WEYL-NET`,
`AQM-47-F3-AFFINE-LINE-SYMMETRY-EXAMPLE`, and
`AQM-48-F3-FULL-AFFINE-LINE-NET-HILBERT-ACTION`: for
\(\mathbf A^1_{\mathbb F_q}\), the base-preserving automorphism group is
proved to be \(x\mapsto ax+b\), with \(a\in\mathbb F_q^\times\) and
\(b\in\mathbb F_q\).  The action on a closed point \((\pi)\) sends it to
\((a^{\deg\pi}\pi((X-b)/a))\), and the induced residue-field isomorphisms
push Weyl labels forward to give covariant local-net automorphisms.  On finite
supports these are implemented by tensor-factor permutation and residue-field
relabeling unitaries; in odd characteristic this is the finite Clifford
implementation covered by the Gross convention.  The \(\mathbb F_3\) rational
three-site shard is explicitly only a finite-support truncation.  The full
\(\mathbb F_3\) shard gives the countable closed-point algebra, the
zero-reference incomplete tensor Hilbert representation, the implementing
unitaries, and the generic-point caveat.

The newest regular-function layer is
`AQM-49-REGULAR-FUNCTIONS-AFFINE-LINE-WEYL-LABELS` and
`AQM-50-F3-REGULAR-FUNCTIONS-LINE-BY-LINE`.  It records that regular functions
on the affine line give residue profiles, usually with cofinite closed support,
not quasi-local Weyl observables.  A polynomial \(h\) gives a finite quantum
system only when used as a support selector \(Z_{\rm cl}(h)\); reduced smeared
operators depend on labels modulo \(\operatorname{rad}(h)\), while repeated
factors are visible only in the Artin-ring thickened layer.

The newest affine action on regular functions is
`AQM-51-REGULAR-FUNCTION-AFFINE-SYMMETRY-ACTION` and
`AQM-52-F3-REGULAR-FUNCTION-SYMMETRY-LINE-BY-LINE`.  The rule is
`g_#F = F circ g^(-1)` and `g_#h = h circ g^(-1)`.  Residue profiles transform
by the same `S_g` relabelling as closed-point Weyl labels, so
`alpha_g(W_h^red(F,G)) = W_(g_#h)^red(g_#F,g_#G)`.  The Artin-ring factors
`F_q[x]/(pi^e)` are transported to `F_q[x]/((pi^g)^e)` with the exponent
preserved; thickened Weyl covariance still requires transported generating
characters or an explicit dual momentum correction.

The newest fermion groundwork is
`AQM-53-MINIMAL-FERMION-GEOMETRY-CATALOGUE`.  It registers local sources for
supergeometry, spin structures, and logarithmic forms, then separates ordinary
points, even nilpotents, odd superpoints, cotangent parity shifts, and
spin/log-spin data.  The current convention says that `Spec(F_3)` has zero
forced fermion modes, while `Spt_(F_3)`,
`Pi Omega^1_(F_3[epsilon]/epsilon^2/F_3)`, and the log-spin datum
`(P^1_(F_3), {0,infty}, O)` each provide one catalogue mode.

The newest planning-and-implementation frontier is the finite commutative ring
database. The PRD lives at `docs/finite_commutative_ring_database_prd.md`; the
implementation plan lives at
`docs/finite_commutative_ring_database_implementation_plan.md`; Beads tracks
the mainline chain `aqm-pa0` through `aqm-6t4`. Current implementation state:
convention `(an)` fixes the zero-ring policy, generated SQLite artifact policy,
build rerun policy, schema-integrity split, and MVP helper scopes; the code now
has canonical JSON/ID helpers, a structure-constant ring model, manual MVP
constructors, invariant helpers, certificate verification, bounded dedup,
residue and thickened-Frobenius quantisation helpers, prime-field Weyl matrix
metadata, optional GAP and quotient helper status paths, `run_all`/export
wiring, and an audit gate. The run bundle
`runs/2026-05-26-finite-ring-database/` records passing acceptance for the
schema-only SQLite smoke build and in-memory CSV review exports. The SQLite
file remains local/ignored and contains one `build_run` row with zero `ring`
and `presentation` rows; no populated/audited ring database or completeness
claim exists yet, and report integration is deferred.

## Most Recent Session

**2026-05-28 - QSA Step 23 open problems and next targets.**

- Implemented `AQM-87-QSA-OPEN-PROBLEMS-NEXT-TARGETS`.
- The shard closes the first QSA pass as a gap/synthesis ledger, not a
  derivation or theorem shard.  It prioritizes missing source/convention
  acquisition, finite-ring database and audit dependencies, quotient collapse
  and two-direction Artin examples, finite Weyl/projective representation
  boundaries, single-particle/Fock/statistics comparison boundaries,
  infinite/generic/analytic completions, dynamics-selection principles, and
  noncommutative/nonunital extension questions.
- It carries blockers `aqm-qsa-src02`, `aqm-qsa-frres01`,
  `aqm-qsa-frcot01`, `aqm-qsa-collapse01`, and `aqm-qsa-artin01` without
  reinterpretation.  It adds no source, convention, script, generated data,
  Beads update, or `report.pdf` rebuild.

**2026-05-28 - QSA Step 22 degenerate and over-restrictive cases.**

- Implemented `AQM-86-QSA-DEGENERATE-OVERRESTRICTIVE-CASES`.
- The shard catalogues concrete failure modes from existing QSA anchors:
  missing Gram choices for bare finite sets, empty-versus-zero edge cases,
  radical quotient label spaces, zero cotangent labels for fields and product
  fields, `\mathbb Z/6\mathbb Z` presentation collapse warnings, blocked
  quotient-collapse candidates, reduced layers forgetting nilpotents, mixed
  residue `not_applicable` readings, and infinite-representation boundaries.
- It preserves blockers `aqm-qsa-src02`, `aqm-qsa-frres01`,
  `aqm-qsa-frcot01`, `aqm-qsa-collapse01`, and `aqm-qsa-artin01`.  It adds
  no source, convention, script, generated data, Beads update, or
  `report.pdf` rebuild.

**2026-05-28 - QSA Step 20 infinite ring boundaries.**

- Implemented `AQM-84-QSA-INFINITE-RING-BOUNDARIES`.
- The shard reviews `\Spec\mathbb F_q[t]`, `\Spec\mathbb F_q[x,y]`, and
  `\Spec\mathbb Z` using existing AQM-25, AQM-29, AQM-30, AQM-45, AQM-48,
  AQM-75, and AQM-79 anchors.
- It separates finite-support truncations, algebraic quasi-local
  closed-point algebras, reference-vector incomplete tensor representations,
  formal infinite-volume regular-function profiles, generic-sector proposals,
  and completion proposals.  It adds no new source, convention, run, data, or
  `report.pdf` rebuild in this delegated shard.

**2026-05-28 - QSA Step 19 product rings and tensor factors.**

- Implemented `AQM-83-QSA-PRODUCT-RINGS-TENSOR-FACTORS`.
- The shard is a Review shard for selected product-field/residue-site tensor
  factors only.  It records that `\mathbb F_3^n` gives `n` qutrit residue
  factors in the AQM-40 workflow, while AQM-58 gives zero cotangent-first
  labels for `k^n`.
- It compares this with AQM-68 by naming the extra product-ring data: spectrum
  points, discrete topology, residue fields, Weyl carriers, and local
  endomorphism algebras.  It keeps `\mathbb Z/6\mathbb Z` as a mixed-residue
  warning, not a general quotient-collapse theorem, and carries database,
  cotangent, and thickened-product gaps forward.  `report.pdf` was not rebuilt
  in this delegated shard.

**2026-05-28 - QSA Step 18 nilpotent-sensitive association.**

- Implemented `AQM-82-QSA-NILPOTENT-SENSITIVE-ASSOCIATION`.
- The shard is Review/New for locally established thickened examples only.
  It compares AQM-81's reduced residue-site carriers with AQM-36/AQM-37
  thickened Artin carriers, especially
  `\mathbb F_3[\epsilon]/(\epsilon^2)` and the `t^n=1` family.
- It records that thickened Weyl systems require generating-character or
  finite Frobenius-ring data beyond the residue fields.  It explicitly keeps
  nilpotents as local jet/internal degrees at existing points, not as extra
  points.  Arbitrary finite rings, two-direction Artin rows, and generating
  characters beyond the local AQM-36 examples remain blocked.  `report.pdf`
  was not rebuilt in this delegated shard.

**2026-05-28 - QSA Step 17 residue-field site association.**

- Implemented `AQM-81-QSA-RESIDUE-FIELD-SITE-ASSOCIATION`.
- The shard is Review/New for sourced finite cases only.  It defines the
  selected-site workflow: finite displayed prime/maximal points, residue
  field at each point, local `K_x^2` finite-field phase labels,
  `\ell^2(K_x)` carriers, local matrix algebras, and finite-support assembly
  by direct sums of local phase groups plus tensor products of carriers.
- It records mixed residue fields as finite abelian direct sums and tensor
  factors over their own residue fields, using `Z/6Z` as the warning example.
  It does not claim a general finite-ring decomposition algorithm, populated
  database evidence, deterministic site ordering, dynamics, stabilizers, or
  Clifford data.  Reduced residue sites remain separate from the nilpotent
  Artin-Weyl layer planned for Step 18.  `report.pdf` was not rebuilt.

**2026-05-28 - QSA Step 16 finite ring example matrix.**

- Implemented `AQM-80-QSA-FINITE-RING-EXAMPLE-MATRIX`.
- The shard is a synthesis matrix only: it adds no source, convention, script,
  run bundle, generated data, or populated database claim.  It uses explicit
  `available`, `blocked`, `unknown`, `not_applicable`, and `degenerate`
  report-planning tokens, and says these are not CSV sentinels.
- The tables keep reduced residue-site, cotangent-first, field-label, and
  nilpotent-sensitive workflows separate.  They use local anchors AQM-23,
  AQM-34--AQM-37, AQM-40, AQM-58, and AQM-76--AQM-79, plus the schema-only
  finite-ring run README and in-memory review CSVs.  General finite-ring
  residue decomposition, database cotangent columns, two-direction Artin
  standardization, and quotient-collapse examples beyond `Z/6Z` remain
  blocked by their QSA beads.  `report.pdf` was not rebuilt.

**2026-05-28 - QSA Step 15 geometric field association Hom(X,V).**

- Implemented `AQM-79-QSA-GEOMETRIC-FIELD-HOM-X-V`.
- The shard is review-only: it adds no source, no convention, no run
  artifact, and no general `Hom(X,V)` quantisation claim.  It treats
  `Hom(X,V)` as the Step 15 prompt label and separates the local replacements:
  `Map(X,V)` and chosen finite subspaces from AQM-14/AQM-71, closed-point
  finite-support residue labels from AQM-28--AQM-30, rational truncations from
  AQM-16/AQM-30/AQM-75, projective sheaf-section fields from AQM-15--AQM-18,
  and regular-function profiles/reduced smearings from AQM-49--AQM-52.
- It records that finite Weyl kinematics begins only after the relevant
  radical, support, or finite phase-label condition is resolved, with AQM-78
  as the common Weyl-Heisenberg boundary.  Gaps are carried to QSA Steps 16,
  17, and 20.  `report.pdf` was not rebuilt.

**2026-05-28 - QSA Step 13 intrinsic versus relative cotangent.**

- Implemented `AQM-77-QSA-INTRINSIC-RELATIVE-COTANGENT`.
- Added convention `(av)` distinguishing intrinsic/local cotangent
  `m_x/m_x^2` from relative Kahler cotangent
  `Omega^1_(A/B) tensor_A kappa(x)` over an explicit base `B`.
- The shard compares `F_3`, `F_3^n`, `F_3[e]/(e^2)`, `F_3[t]/(t^3)`,
  `F_3[u,v]/(u^2,v^2)`, the same two-direction ring relative to
  `F_3[u]/(u^2)`, and `Z/4Z` over `Z`.  It records the resulting changes to
  `V_x`, `V_x^*`, symplectic label dimensions, and finite Weyl carrier sizes,
  while leaving database-backed cotangent rows, dynamics, Hamiltonians, de
  Rham CSS completions, and generic/infinite-residue representations as gaps.
  No Beads commands were run; the orchestrator owns Beads for this thread.
  `report.pdf` was not rebuilt.

**2026-05-28 - QSA Step 12 cotangent-first association.**

- Implemented `AQM-76-QSA-COTANGENT-FIRST-ASSOCIATION`.
- The shard places convention `(ao)`'s tangent-cotangent Weyl workflow into
  the QSA catalogue as a geometric first-association workflow: select
  finite-residue points under AQM-75 discipline, attach
  `T^*_(X/k,x)` and `T_(X/k,x)`, form
  `T_(X/k,x) direct_sum T^*_(X/k,x)`, record the canonical symplectic
  pairing, and only then use finite Weyl-Heisenberg carriers when the
  residue field is finite.
- It inventories only local AQM-58--AQM-63 examples, uses AQM-63 only for the
  optional exact-one-form cotangent constraint compatibility statement, and
  leaves intrinsic-versus-relative cotangent choices and finite-ring
  database-backed cotangent rows as gaps.  No Beads commands were run; the
  orchestrator owns Beads for this thread.  `report.pdf` was not rebuilt.

**2026-05-28 - QSA Step 11 what counts as a point.**

- Implemented `AQM-75-QSA-WHAT-COUNTS-AS-A-POINT`.
- The shard compares underlying element sets, rational points, closed points,
  generic points, and all scheme points as distinct indexing choices.  It
  reviews AQM-22, AQM-23, AQM-28, AQM-29, AQM-30, AQM-45 and conventions
  `(t)`, `(u)`, `(y)`, and `(ai)`.
- It records that finite kinematical systems arise from finite underlying
  sets with finite added data, finite rational supports, finite closed
  supports, or finite closed spectra.  Infinite closed-point sets are
  quasi-local filtered systems; generic/infinite-residue points and analytic
  completions remain explicit gaps.  No Beads commands were run; the
  orchestrator owns Beads for this thread.

**2026-05-28 - QSA Step 10 single-particle reduction.**

- Implemented `AQM-74-QSA-SINGLE-PARTICLE-REDUCTION`.
- The shard defines the single-particle sector for AQM-69 direct-sum
  particles, AQM-70 degree-one grammar sectors, and the AQM-70 site-option
  expression.  It gives explicit maps from the direct-sum alternatives
  carrier to those named degree-one carriers, and compares with AQM-67 only in
  the one-dimensional internal-space case after basis/unit and Gram choices.
- It records tensor coexistence, finite field-label/Weyl tensor products,
  stabilizer phases, CAR/Fock statistics, Grassmann multipliers, and missing
  Gram choices as boundaries.  The only AQM-19/AQM-72 Fock comparison made is
  the explicit one-particle carrier map `Map(X,K) -> direct_sum_x K`; no
  reduction of the full CCR/CAR/Fock layers is claimed.  No Beads commands
  were run; the orchestrator owns Beads for this thread.

**2026-05-28 - QSA Step 09 fusion-category endpoint.**

- Implemented `AQM-73-QSA-FUSION-CATEGORY-ENDPOINT`.
- The shard is intentionally a gap shard, not a technical fusion-category
  shard.  It explains the intended role of fusion categories as a future QSA
  association family and lists required source/convention decisions for hom
  spaces, simple objects, tensor products/fusion rules, associator/F-symbol
  data, pivotal/spherical structure, optional braiding/R-symbol data,
  lattice/Levin-Wen/string-net data, Hilbert carriers, and local constraints.
- It explicitly defers Levin-Wen/string-net technical claims, fusion-rule
  computations, F-symbol equations, Hamiltonians/projectors, and
  quantum-double/Drinfeld-center claims.  No Beads commands were run; the
  orchestrator owns Beads for this thread.

**2026-05-28 - QSA Step 08 boson/fermion association layer.**

- Implemented `AQM-72-QSA-BOSON-FERMION-LAYER`.
- The shard is a review shard only: it places the AQM-19 finite bosonic real
  symplectic CCR layer, AQM-19 finite fermionic CAR/Clifford layer, and
  AQM-20/AQM-21 Grassmann-Weyl displacement calculus into the QSA catalogue
  with active local source locators.
- The Cahill-Glauber anchors use the official arXiv
  `physics/9808029v1` source extraction
  `references/canonical_fields/cahill_glauber_physics_9808029v1_source/fxxx.tex`;
  the historical APS/marker chain remains source-integrity provenance only.
- Parafermion, fusion-category, and finite AND/OR equivalence variants are
  recorded as gaps, not results.  No Beads commands were run; the
  orchestrator owns Beads for this thread.

**2026-05-28 - QSA Step 06 finite AND/OR many-particle grammar.**

- Implemented `AQM-70-QSA-AND-OR-MANY-PARTICLE-GRAMMAR` and convention
  `(at)`.
- The shard defines a finite carrier grammar with `AND = tensor` for
  coexistence and `OR = direct_sum` for alternatives, built only from
  finite-dimensional carriers already introduced in AQM-68/AQM-69.  It
  identifies finite particle-count sectors by recursive grading, records
  one-particle alternatives, site-option expressions, labelled-slot tensor
  sectors, and finite truncated many-sector expressions, and explicitly
  defers infinite-particle completions.
- The shard keeps this elementary grammar separate from symmetric,
  antisymmetric, para, Fock, and fusion-category enhancements, and does not
  import canonical-field equivalence claims from AQM-19.
- No Beads commands were run; the orchestrator owns Beads for this thread.

**2026-05-28 - QSA Step 05 finite-set direct-sum particle.**

- Implemented `AQM-69-QSA-FINITE-SET-DIRECT-SUM-PARTICLE` and convention
  `(as)`.
- The shard defines the one-particle-at-one-of-many-sites carrier as
  `direct_sum_x K_x` or `direct_sum_x H_x` only after adding internal carriers
  or Hilbert spaces per site, distinguishes it from the AQM-68 tensor-site
  carrier, handles empty and one-point edge cases, and compares the
  one-dimensional internal-space case with AQM-67 only after explicit basis
  or unit-vector choices.
- No Beads commands were run; the orchestrator owns Beads for this thread.

**2026-05-28 - QSA Step 04 finite-set tensor sites.**

- Implemented `AQM-68-QSA-FINITE-SET-TENSOR-SITES` and convention `(ar)`.
- The shard keeps arbitrary site Hilbert spaces or observable algebras as
  explicit extra data for a finite set, forms only finite tensor products and
  tensor-by-identity inclusions, distinguishes the construction from AQM-67's
  formal carrier, and cites AQM-14/AQM-22/AQM-24/AQM-25/AQM-40 only as local
  anchors for structured qudit cases.
- No Beads commands were run; the orchestrator owns Beads for this thread.

**2026-05-26 - Exact GAP small-ring identity status counts.**

- Resolving `aqm-cbz` by replacing the conservative order-1 GAP
  `SmallRing` status limitation with exact element-level identity detection
  for `max_order` values `1..15`.
- The generated GAP script enumerates `Elements(R)` for each `SmallRing(s,i)`,
  tests every candidate by the two-sided identity law `e*x=x=x*e`, rejects
  multiple detected identities, and combines exact unitality with
  `IsCommutative(R)` for `scoped_commutative_unital_count`. `SmallRing(1,1)`
  is counted by this same identity law under the local zero-ring policy.
- The helper remains status metadata only: no SQLite writes, no structure
  constants, no imported presentations, no certificates, no run artifacts,
  and `certifies_completeness=false`.
- GAP-enabled validation with
  `/nix/store/6pk86ycv8x8xaw1a76chmxv23w61l52r-gap-4.15.1/bin/gap` returned
  scoped commutative-unital counts
  `[1,1,1,4,1,1,1,10,4,1,1,4,1,1,1]` and total counts
  `[1,2,2,11,2,4,2,52,11,4,2,22,2,4,4]` for orders `1..15`.
- Validation:
  `PATH="/nix/store/6pk86ycv8x8xaw1a76chmxv23w61l52r-gap-4.15.1/bin:$PATH" julia --project=. -e 'using Pkg; Pkg.test()'`
  passed, including `finite ring database GAP small-ring import status` with
  `63` passes; `git diff --check` was clean.

**2026-05-26 - Conservative GAP small-ring status limitation.**

- Resolving `aqm-f8p` by limiting
  `finite_ring_gap_small_ring_import_status(max_order; ...)` to `max_order=1`.
  Requests beyond order `1` now fail loudly until exact element-level
  unit-detection/import is available.
- The status helper remains installed-tool metadata only: `gap --bare -q`,
  `SmallRing(1,1)` counted by the local zero-ring policy,
  `certifies_completeness=false`, and no imported presentations.
- Validation: `julia --project=. -e 'using Pkg; Pkg.test()'` passed; on this
  host the GAP testset reported `41` passes and `1` broken skip because GAP is
  not on `PATH`.
- Next finite-ring follow-up should be the exact unit-detection/import path
  needed before any GAP scoped counts beyond order `1`, not broad report work.

**2026-05-26 - GAP-enabled finite-ring small-ring validation.**

- Closed `aqm-tcv`: with `PATH` prefixed by the Nix GAP 4.15.1 store path,
  `Sys.which("gap")` resolved and
  `finite_ring_gap_small_ring_import_status(1; gap_path=Sys.which("gap"))`
  returned `status="reconciled"`, `total_count=1`,
  `scoped_commutative_unital_count=1`, nonempty `tool_version`, and the local
  GAP source locator.
- The helper now invokes GAP as `gap --bare -q` for status metadata, avoiding
  package autoload/startup failures observed in the local Nix GAP build. It
  counts `SmallRing(1,1)` under the local zero-ring convention while keeping
  the `IsRingWithOne(R) && IsCommutative(R)` filter for other rings.
- Tightened tests for GAP command/script shape, fail-loud parser paths, source
  locator coverage, and the GAP-available order-1 scoped count. GAP-enabled
  `julia --project=. -e 'using Pkg; Pkg.test()'` passed, with the GAP testset
  reporting `45` passes and no skip; `scripts/run_all.jl --fast` passed with
  `12 ok, 0 failed, 0 skipped`; `git diff --check` was clean.
- Raised `aqm-f8p` because direct GAP probes under `--bare` showed
  `IsRingWithOne(SmallRing(s,i))` returning false for sampled orders `2..5`.
  Do not rely on GAP scoped counts beyond the order-1 smoke until an exact
  unit-detection/import path exists.

**2026-05-26 - Finite-ring database Steps 05-18 acceptance outcome.**

- Continued the mainline finite-ring chain from `aqm-0zl` through acceptance
  bead `aqm-6t4`. Canonical JSON and ID hashing now cover presentation, ring,
  certificate, and quantisation payloads.
- Added the structure-constant model, manual MVP constructors, invariant
  helpers, verifier-checked isomorphism certificates, and bounded dedup search.
  Invariants filter candidate comparisons; verifier-approved certificates prove
  MVP merges.
- Added MVP residue and thickened-Frobenius quantisation helpers. Unavailable
  cases emit explicit obstruction/blocking rows, and the zero ring remains
  `not_applicable_until_layer_semantics` with no Hilbert-space claim.
- Added optional prime-field Weyl matrix metadata, GAP small-ring status, and
  quotient-constructor status helpers. The later `aqm-tcv` validation now
  covers the GAP-enabled order-1 status branch; `aqm-f8p` limits broader GAP
  scoped counts pending exact unit-detection/import.
- Recorded the rerun policy and schema-integrity split in convention `(an)`:
  build fails on an existing SQLite file unless `--force`; stable relational
  checks live in schema, while canonical JSON and open/evolving status tokens
  are audit-owned.
- Wired the schema-only build, audit gate, and in-memory CSV exports into
  `scripts/run_all.jl`, `INDEX.md`, and `data/SCHEMA.md`.
- Acceptance recorded in `runs/2026-05-26-finite-ring-database/README.md`:
  `julia --project=. scripts/run_all.jl --fast` passed with `12 ok, 0 failed,
  0 skipped`; `git diff --check` was clean; and
  `julia --project=. -e 'using Pkg; Pkg.test()'` passed with the existing GAP
  availability check still marked Broken/`@test_skip`.
- Audit summary from the orchestrator run:
  `finite_ring_db_audit.jl: ok ... tables=11/11 schema_version=1 build_runs=1
  json_cells=2`.
- Current boundary: `finite_rings.sqlite` is schema-only/local/ignored with
  `build_run=1`, `ring=0`, and `presentation=0`. CSV data rows are
  `ring_summary=12`, `ring_presentations=13`,
  `ring_isomorphism_certificates=1`, `ring_quantization_summary=26`, and
  `ring_quantization_obstruction=18`. This is not a populated/audited
  finite-ring database and makes no completeness claim; no report shard was
  added.

**2026-05-26 - Finite-ring database orchestration through build CLI skeleton.**

- Worked as orchestrator with serial subagent delegation, then stopped by user
  request before implementing `aqm-0zl`.
- Closed `aqm-pa0`: convention `(an)` now includes
  `finite_ring_db.zero_ring_policy = include` and
  `finite_ring_db.sqlite_commit_policy = local_run_artifact_until_release_policy`.
  The one-element zero ring is included in finite-ring DB scope/MVP, sourced
  to local GAP and Stacks locators. Generated `finite_rings.sqlite` files are
  local run artifacts until a release artifact policy exists.
- Raised `aqm-3cm` for zero-ring invariant-field conventions before manual
  constructors need `characteristic_exact`, residue, or quantisation decisions.
- Closed `aqm-8dl`: added Base-only finite-ring DB source/tool preflight
  helpers and tests. The source contract requires 15 tracked finite-ring
  source files and treats the two ignored local PDFs as documented non-required
  local artifacts. Tool preflight reports `julia`, `gap`, `sage`, `python`,
  `sqlite3`, `Oscar`, and `Nemo` as available/missing with version/path or
  skip reason. `scripts/tool_versions.sh` now reports `python`, `sqlite3`,
  `Oscar`, and `Nemo` too.
- Closed `aqm-4fi`: added `FiniteRingDatabaseSchema.jl` with the ten PRD
  tables, PRD foreign keys exactly as written, a
  `finite_ring_database_schema_version` table at version `1`, and a `sqlite3`
  CLI migration helper. Tests cover idempotent migration and rejection of an
  invalid `ring_presentation_link`.
- Raised `aqm-4eq` for later schema/audit decisions: whether
  `ring_presentation_link.certificate_id` should become a foreign key, where
  invariant at-least-one-reference checks belong, and which enum/JSON
  integrity checks should live in schema versus audit.
- Closed `aqm-775`: added `scripts/arithmetic/finite_ring_db_build.jl`, a
  schema-only CLI accepting `--run runs/<slug>`, `--max-order`, `--sources`,
  and `--help`. It checks for `README.md` before any write, migrates the
  schema, inserts one conservative `build_run` row, and writes no ring rows.
  Tests cover bad arguments, missing-README no-write behavior, and a valid
  temporary run bundle with one `build_run` row and zero `ring` rows.
- Raised `aqm-zky` for build CLI rerun/overwrite semantics; duplicate `run_id`
  failure is intentionally not solved in the skeleton.
- Validation run after the latest changes:
  `git diff --check`; `bash scripts/tool_versions.sh`;
  `julia --project=. -e 'using Pkg; Pkg.test()'`. The Julia tests included
  real `sqlite3` schema migration, foreign-key rejection, and temporary build
  CLI run-bundle checks. No temporary `runs/2099-01-01-frdb-cli-*` directories
  remained after tests.

**2026-05-25 - Canonical boson/fermion field comparison.**

- Added `references/canonical_fields/SOURCES.md` and local arXiv source bundles
  for Derezinski's CCR/CAR/Fock notes, Bekka's Stone-von-Neumann source, and
  Keyl-Schlingemann's Grassmann-CAR/GAR source.
- Added convention `(s)` for finite canonical boson/fermion comparison:
  bosons use real symplectic map spaces and Weyl CCR; fermions use CAR over a
  real Hilbert label space and antisymmetric Fock space.
- Added `AQM-19-CANONICAL-BOSON-FERMION-FIELD-COMPARISON`, proving the finite
  bosonic fit, deriving the finite exterior-algebra CAR, and separating the
  Grassmann-GAR calculus from a direct Stone-von-Neumann target replacement.
- Added Bravyi's `quant-ph/0404180` source, copied the local
  `PhysRevA.59.1538.pdf`, converted it with `marker`, and added
  `AQM-20-GRASSMANN-WEYL-FERMION-DISPLACEMENTS` plus
  `AQM-21-GRASSMANN-WEYL-FERMION-DERIVATIONS`, proving the positive
  Grassmann-extended CAR unitary representation of fermion displacement
  operators and recording the ordinary-Hilbert-space caveat.
- Added `AQM-22-PRIME-FIELD-ARITHMETIC-FIELDS-QUDIT-PAULIS`, proving that the
  all-map arithmetic field on the underlying set of `F_p` reproduces the
  ambient odd-prime-dimensional qudit Pauli group, with the qubit phase caveat,
  while `Spec(F_p)` gives only the one-qudit version.
- Added `AQM-23-SPEC-Z6-RESIDUE-QUDIT-FACTORISATION`, computing
  `Spec(Z/6Z)` and proving that the qubit/qutrit local factors combine by
  tensor product under Weyl quantization.
- Added `AQM-24-ZARISKI-OPENS-OBSERVABLE-NETS`, proving that finite
  Zariski-open observable algebras form a covariant Weyl algebra net under
  `U |-> A(U)`, while `U |-> A(X \ U)` is a contravariant closed-support
  convention.  The shard works out the field edge case and all opens of
  `Spec(Z/6Z)`.
- Added `AQM-25-QUASILOCAL-ZARISKI-ALGEBRA`, fixing the directed-system choice
  for the primary quasi-local algebra as quasi-compact opens ordered by
  inclusion, with closed supports recorded as the secondary directed system.
- Added Curry's arXiv source bundle under `references/cosheaves/` and
  `AQM-26-PRESHEAVES-COSHEAVES-OBSERVABLE-NETS`, defining presheaves, sheaves,
  precosheaves, and cosheaves before proving the observable-net/cosheaf
  distinction.
- Added `AQM-27-STATE-PRESHEAF-QUASILOCAL-ALGEBRA`, sourced from Derezinski
  and Gottesman density-matrix conventions, proving the state presheaf,
  non-sheaf marginal counterexamples, and the inverse-limit description of
  states on the algebraic quasi-local algebra.
- Added convention `(y)` and shards
  `AQM-28-CLOSED-POINT-AFFINE-ARITHMETIC-FIELDS`,
  `AQM-29-SPEC-FQ-T-ARITHMETIC-FIELD`, and
  `AQM-30-SPEC-FQ-XY-ARITHMETIC-FIELD`, extending the finite residue-qudit
  construction to affine finite-type schemes over `F_q`.  The report now works
  out `Spec(F_q[t])` and `Spec(F_q[x,y])` at the level of points, residue
  fields, Weyl-Heisenberg labels, local algebras, state inverse limits, and
  the boundary between quasi-local finite-support fields and formal regular
  polynomial profiles.

**2026-05-24 - Lab-book scaffold created.**

- Created the sharded LaTeX master `report.tex` with five initial shards under
  `report/sections/`.
- Added report navigation files, scientific-practice guidance, conventions,
  an index manifest, source/reference placeholders, run-bundle discipline, and
  data/figure placeholders.
- Added a minimal Julia package scaffold, local script runner, report-shard
  checker, Makefile, and local CI script.
- Local tool check found Julia, LaTeX `latexmk`, and `bd`; `sage` and `gap`
  were not on PATH in this shell.

**2026-05-24 - Toric-code ghost supercharge run added.**

- Registered Kitaev's arXiv TeX source bundle under
  `references/toric_code/`.
- Added the convention `Q=sum_i c_i^* P_i`, one auxiliary fermion per local
  stabilizer check, with `P_i=(I-S_i)/2`.
- Implemented an algebraic validator that avoids full Hilbert matrices. For
  `k=4` it checks commuting local stabilizers, rank `2k^2-2`, code dimension
  `4`, and the CAR/projector certificates for `Q^2=0` and
  `{Q,Q^*}=H_TC`.
- Added the boundary-map unification: the chain complex
  `C_2 -> C_1 -> C_0` gives `H_X=partial_1`, `H_Z=partial_2^T`, so
  `partial_1 partial_2=0` is the CSS commutation condition and its rows/columns
  are exactly the ghost-supercharge check supports.
- Added a full proof in `AQM-06-TORIC-CHAIN-GHOST-PROOF`: cellular classes
  `[a] in ker(delta^1)/im(delta^0)` map to normalized orbit sums in the code
  space, and the ghost anticommutator follows from the CAR and commuting
  projectors.
- Added `AQM-07-TORIC-OPERATOR-RELATION`: `Q_cell` is not a low-ghost
  restriction of `Q_gh`; instead `delta^0` induces star translations,
  `delta^1` induces plaquette syndrome multiplication, and `Q_gh` is the
  Koszul differential for those projector equations.
- Added `AQM-08-SYMPLECTIC-CSS-BRIDGE`: the CSS chain complex produces an
  isotropic stabilizer subspace `L`, and the logical Pauli module is
  `L^perp/L = H^1 x H_1`; a new exact Julia run checks this over
  `F_2`, `F_3`, and `F_5`.
- Added `AQM-09-SYMPLECTIC-SUPERCHARGE-DICTIONARY`: for any CSS stabilizer
  subspace `L`, a chosen basis gives a ghost/Koszul supercharge whose
  degree-zero cohomology is the stabilizer code and whose logical Pauli action
  is `L^perp/L`.
- Added `AQM-10-STEANE-SYMPLECTIC-MOLECULAR` and
  `AQM-11-STEANE-SUPERCHARGE-COHOMOLOGY`: the Gottesman-table Steane code is
  now worked out at vector-space, stabilizer, fermion, supercharge, and
  cohomology level, with an exact run bundle.
- Added `AQM-12-STEANE-CLIFFORD-KOSZUL-MORPHISMS`: transversal Hadamard is an
  exact automorphism of the written Steane `Q` after ghost swap; transversal
  phase is a chain isomorphism to a changed generator presentation and a
  homotopy equivalence back through the common zero-syndrome retract.
- Added `AQM-13-CLIFFORD-GROUP-GHOST-GAUSSIAN-THEOREM`: arbitrary Clifford
  covariance is stated for signed Pauli stabilizer presentations, while
  stabilizer presentation changes lift to number-preserving ghost Gaussians;
  the Steane validation checks all 56 H/P/CNOT Clifford generators and the 45
  elementary GL6 ghost moves.
- Added `AQM-14-ARITHMETIC-QUANTUM-FIELDS`: finite arithmetic quantum fields
  are proposed as Weyl-Heisenberg displacement systems for reduced pointwise
  symplectic function spaces `E <= Map(X,V)`. The validation run gives exact
  `F_3` examples for finite sets, vector spaces, and simple arithmetic
  varieties.
- Added `AQM-15-PROJECTIVE-SHEAF-FIELD-DEFINITIONS` and
  `AQM-16-PROJECTIVE-LINE-SHEAF-FIELD-CALCULATION`: Stacks Project TeX sources
  are registered locally for presheaves, sheaves, Proj, projective space,
  varieties, twists, and projective-space cohomology. The new exact run checks
  \(\mathbf P^1_{\mathbb F_3}\), \(H^0(\mathcal O(d))\otimes\mathbb F_3^2\),
  finite rational-point evaluations, radicals, and reduced Weyl counts for
  `d=0..4`.
- Added `AQM-17-PROJECTIVE-LINE-STALKS`: the same run now records one symbolic
  germ row for every monomial section at each rational point, including the
  local ring, local frame, maximal ideal, and residue value.
- Added `AQM-18-STALKS-AS-FIELD-GERMS`: the phrase "field at the point" is now
  fixed as stalk equals local field germ, while fiber/residue equals sampled
  field value.  The shard tabulates every scalar residue for the
  \(\mathbf P^1_{\mathbb F_3}\), \(d=0,\ldots,4\), examples.
- Added `AQM-31-WEYL-HEISENBERG-RESEARCH-STATUS-RINGS`,
  `AQM-32-WEYL-HEISENBERG-REPRESENTATIONS-FOR-KT`, and
  `AQM-33-FULL-DUAL-LOCAL-MODELS-FOR-KT`: the report now has a sourced
  research-status map for LCA, locally compact ring, finite Frobenius-ring,
  finite Clifford/Weil, local-field, and adelic Weyl-Heisenberg results.  It
  defines the algebraic \(k(t)\) Heisenberg group, proves the concrete
  Schrödinger representation on \(\ell^2(k(t))\) is unitary and irreducible,
  and separates that result from the full LCA Stone-von Neumann theorem and
  from local or adelic completions.  The worked \(k=\mathbb F_3\) examples
  compute explicit rational-function commutation phases.
- Added `AQM-34-F3-POLYNOMIAL-QUOTIENT-ARITHMETIC-FIELDS` and
  `AQM-35-TN-EQUALS-1-F3-ARITHMETIC-FIELD`: finite coordinate rings
  \(\mathbb F_3[t]/(p)\) are now worked out from the factorization of \(p\),
  with complete residue-field Weyl-Heisenberg representations, open-local
  algebras, state restrictions, and the nilpotent/reduced quotient boundary.
  The \(t^n=1\) case records \(t^n-1=(t^m-1)^{3^{v_3(n)}}\), the factor-degree
  count via \(\operatorname{ord}_d(3)\), and examples \(n=1,2,3,4,6\).
- Added `AQM-36-NILPOTENT-THICKENING-WEYL-FIELDS` and
  `AQM-37-THICKENED-TN-EQUALS-1-EXAMPLES`: nilpotent thickenings now have a
  separate finite local Artin-ring Weyl layer.  For
  \(A=\mathbb F_3[t]/(\pi^e)\), the top-coefficient character is proved
  generating, \(W(q,p)\) on \(\ell^2(A)\) is an irreducible projective unitary
  Weyl representation, and \(\mathfrak m\)-adic jets pair from the outside in.
  For \(t^n=1\), the thickened Hilbert dimension is \(3^n\), while the reduced
  residue layer has dimension \(3^{n/3^{v_3(n)}}\).
- Added convention `(ac)` plus `AQM-38-LAGRANGIAN-STABILIZER-DESCENT` and
  `AQM-39-TWO-QUTRIT-STABILIZER-DESCENT-COUNTEREXAMPLE`: stabilizer descent is
  now separated from the Lagrangian/full-stabilizer condition.  Vanishing
  defect is exactly cover-generation of the stabilizer labels, and the
  two-qutrit entangled stabilizer over `F_3` gives a concrete nonzero-defect
  counterexample.
- Added convention `(ad)` plus `AQM-40-PRODUCT-FIELD-SPECTRUM-QUDIT-STABILIZERS`:
  `Spec(k^n)` is a finite discrete `n`-point spectrum with residue fields
  `k`, so the arithmetic field is the standard ambient `n`-qudit Weyl/Pauli
  net.  The shard separates this ambient system from the later choice of
  stabilizer subgroup and phases.
- Added convention `(ae)` plus `AQM-41-CECH-COHOMOLOGY-QUANTUM-DESCENT`:
  Stacks Cohomology is now registered locally for Cech complexes,
  refinements, and ordered cochains.  The shard proves finite-cover Cech
  acyclicity of the full residue-label cosheaf and separates the quantum
  counterparts: stabilizer descent as an abelian cokernel, states as marginal
  comparison, and observables as the ordinary-algebra-colimit to physical-net
  comparison.
- Added convention `(af)` plus `AQM-42-GAUSSIAN-CLIFFORD-DYNAMICS`: Gross's
  finite Hudson arXiv source is registered locally.  The shard proves that
  odd-characteristic half-Weyl symplectic morphisms induce unital
  `*`-monomorphisms of Weyl observable algebras, symplectic automorphisms give
  Gaussian/quasi-free dynamics, and Gross's Clifford theorem gives projective
  unitary implementations.  Gross-Hudson fixes the finite odd-qudit
  Gaussian-state dictionary as pure stabilizer states.
- Added convention `(ag)` plus `AQM-43-FINITE-FIELD-SCALE-CONTINUUM-LIMITS`:
  finite-field extension rank now defines scales
  `X_r = X_0 x_Fq F_(q^r)`.  Base change of schemes is canonical, but the
  absolute-trace Weyl phases create an obstruction: naive diagonal label maps
  multiply commutators by `s/r`.  Trace-normalized embeddings using trace-one
  elements fix this, canonically on the prime-to-`p` subtower.  For
  `Spec(F_3)`, the justified canonical continuum algebra is
  `colim_{3 not| r} M_(3^r)(C)`, and Frobenius acts compatibly by
  `W(q,p) -> W(q^3,p^3)`.
- Added convention `(ah)` plus `AQM-44-TRACE-GAUGES-FULL-CONTINUUM-TOWERS`:
  the arbitrariness in full finite-field continuum towers is now formalized as
  trace gauge freedom.  A coherent trace-density system `(a_r)` with
  `Tr_{F_(q^s)/F_(q^r)}(a_s)=a_r` always exists by a factorial-tower
  trace-surjectivity construction.  It gives coherent scalars
  `c_(s,r)=a_s/a_r` and hence coherent full-tower Weyl-net embeddings.  For
  `p | s/r`, no relative-Frobenius-fixed trace-one scalar exists, so Frobenius
  is naturally gauge-covariant rather than strict on an arbitrary full-tower
  presentation.
- Added convention `(ai)` plus `AQM-45-SPEC-Z-ARITHMETIC-QUANTUM-FIELD`:
  `Spec(Z)` now has a closed-prime residue-qudit AQF with one `l`-level qudit
  at each rational prime and an optional separate generic `Q` Weyl sector.
  The shard proves that `z -> z+1` is not a scheme automorphism of `Spec(Z)`.
  It then defines the internal residue-translation action of `Z` on the
  prime-qudit algebra, proves the finite-support profinite periods, and proves
  that nonzero translations are not implemented in the `|0>` incomplete tensor
  sector.

## Next Useful Steps

1. Acquire sources for adelic self-dual models and Bost--Connes-style
   arithmetic \(C^*\)-dynamical systems before turning the `Spec(Z)`
   speculative questions into claims.
2. Decide whether the next \(k(t)\) layer should be the local completion
   \(k((t^{-1}))\), the finite-place family, or the adele ring.
3. Decide whether thickened state restriction should use explicit jet partial
   traces, conditional expectations to the reduced sublayer, or both.
4. Decide whether to linearize the state marginal comparison using ordered
   real vector spaces of Hermitian functionals, or keep it as a convex
   feasibility problem.
5. Extend stabilizer descent from finite vector spaces to mixed residue fields,
   finite Frobenius modules, and overlapping-cover phase compatibility.
6. Extend dynamics beyond the odd finite-field half-Weyl case: even
   characteristic, mixed residue fields, finite Frobenius modules, and
   support-preserving versus nonlocal global symplectic automorphisms.
7. Decide whether to keep full finite-field continuum limits gauge-covariant,
   or impose a specific additional Frobenius-compatible gauge-fixing rule where
   possible.
8. Decide first fixed conventions: zeta normalization, Frobenius direction,
   SUSY-QM grading/signs, and lattice-model boundary/orientation conventions.
9. Create the first run bundle only when there is a concrete source-backed
   invariant to compute.
