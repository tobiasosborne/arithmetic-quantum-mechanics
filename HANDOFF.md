<!-- ROLE: live state. UPDATE POLICY: every session end and every phase
     boundary. Not an authoritative source for mathematics — that is
     definitions.md, claims/CLAIMS.md, and theory/. -->

# HANDOFF — live state

## Current steering — categorical structure and full campaign (2026-09-10)

TJO asked to track the structural properties the categories can carry and
their interactions, so that the arithmetic construction can develop
flexibly. `docs/research-plans/categorical-structure.md` records the
continuing questions, existing carriers and comparison tasks. Definitions
and claim statuses retain their canonical homes. The first follow-up is
the explicit compact structure, state/process correspondence and scalar
transport for Lagrangian relations; this needs a new claim before admission
and does not silently enlarge SP-LREL. The Phantasm labbook section now
records that research direction. Relevant compact/Choi source locators
were checked and added to the existing ledger entries.

TJO then authorized continued orchestration toward landing the whole
Phantasm campaign and understanding exactly whether, and where, a precise
construction aimed at Riemann zeros fails. A persistent session goal is
active. Its acceptance is rigorous construction and an exact spectral
comparison or a precisely scoped failure with a forward strategy, not a
promised Riemann-hypothesis result. Earlier paused programmes stay paused
unless they provide a named dependency. No claim or definition changed in
this steering increment.

The bounded stage-1 work order is `briefs/phantasm-stage1-target.md`.
The existing SP-WEYL corollary is in one blind critic pass; independent
lanes are drafting SP-EGOROV/SP-TENSOR and their exact falsifiers under
`theory/lanes/phantasm-stage1/`. Lane output is unadmitted until integrated
and reviewed. The current register remains 158 claims (121 PROVED,
33 SKETCH, three CONJECTURE, one REFUTED) and 173 definitions.

Verification of this steering increment passed: the contract checker,
labbook lockstep gate, real PDF build, all 27 green suites and all 270
advertised red runs. The labbook builds at 175 pages; the new discussion
on pp.166–167 has been visually inspected. The final provenance edit was
rebuilt and the lockstep and contract gates passed again.

Before the first promotion, repair the contract checker's false-promotion
mutation: an in-memory already-admitted fixture showed that it currently
changes nothing. Also keep inherited-status mutation reachability stable
when inherited claims become dependencies of admitted SP claims. The
current unpromoted repository passes; this is a required promotion guard
repair, not a mathematical objection to the Weyl corollary.

## Current state — reuse and interface repair (2026-09-10)

TJO asked to weave the already admitted results into the Phantasm plan and
double-check contracts, definition overlap and notation creep. The quest
and its sober, accretive, careful SOP remain active. The September 9
bootstrap record below is historical where this update supersedes it.

- All fourteen SP contracts now have **Inherited, Reuse and Remaining**
  fields. F1-REAL supplies the arbitrary finite-configuration matrix/SvN
  theorem; F1-FUNCT supplies the underlying tensor theorem; FRB-TRACE,
  FRB-FROB and FRP-CP are reused only at their actual scope. The
  characteristic-two and higher-gate decisions also reuse admitted results.
- `theory/symplectic-phantasm/reuse.md` contains the short **SKETCH
  corollary draft** for SP-WEYL and the half-form/tensor comparison. The
  raw k-center is reduced along psi, with kernel ker(psi); it is not
  silently identified with the faithful mu_p center of F1-REAL.
- D1701–D1713 retain their numbers and each records **Reuses and Delta**.
  D1704 reuses D1307's Pauli/hierarchy definitions. D1706 extends D1326's
  ordinary-trace target with explicit instrument typing. The algebra and
  generator names are reused; W^s distinguishes the symmetrized model.
  Its position labels now agree with D8. The fixed psi_E family is kept
  separate from chi_K and chi_(E/K), and relative Frobenius is written as
  powers/tensors of the existing absolute permutation.
- The overlap review is `docs/research-plans/symplectic-phantasm-reuse.md`.
  Old claim statements and definition bodies before the bootstrap are
  unchanged. No new claim/definition numbers or mathematical promotions
  were introduced: 158 claims (121 PROVED, 33 SKETCH, three CONJECTURE,
  one REFUTED), 173 definitions.
- `phantasm_reuse_check.py` passed **141,027 exact finite comparisons**
  against the existing Abelian implementation, including a nonstandard
  F9 base character inside F81. Its eleven advertised defects failed at
  their intended gates. The expanded contract checker passed green and
  all 21 deliberate defects, including inherited-status, missing reuse,
  definition-cycle and selected notation-ownership failures.

**Next bounded task:** finish the required promotion review of the short
SP-WEYL bridge, then the remaining affine action in SP-EGOROV and the
affine naturality comparison in SP-TENSOR. Reuse the admitted finite SvN
and configuration-product proofs rather than reopening them. A bridge
checker pass is not a promotion. The ordinary CP target does not assert
arithmetic source exhaustion; support-code success is not subsystem trace.

The updated labbook builds at **174 pages**, and its revised reuse/lemma
page was visually inspected. The full required session-close run passed
**27 green suites and 270 advertised red runs**. Frozen repair records are
in `numerics/symplectic-phantasm/results/reuse-2026-09-10/`; the earlier
bootstrap evidence remains untouched. A line-wrapping-sensitive contract
mutation was repaired and all new mutations were verified at their intended
gates. The contract checker still checks recorded interfaces, not
mathematical truth or a complete symbolic type system.

## Quest charter and initial bootstrap (2026-09-09)

TJO explicitly changed direction and named this quest. Its SOP is **sober,
accretive, and careful**. The initial guidance note is
`docs/research-plans/fundamentals-two-categories.md`; its assistant assessment
is provisional and must be checked against primary sources.

The ordered work is: download and register ground truth (TeX preferred),
register and carefully construct definitions, then plan and build all needed
lemmas through a contract-checked argument DAG under rk-light. See
`docs/research-plans/symplectic-phantasm.md`. This directive supersedes the
older current-direction language below. Composite boundaries and FCR-2 are
paused; admitted results remain available as explicitly cited dependencies.

The source/definition/planning bootstrap is registered:

- `refs/LEDGER.md`: 25 locally verified primary sources, 19 TeX and six
  PDFs, with raw and readable-body hashes. Five historical leads remain
  explicit GAPs and support no lemma. The Kapranov–Smirnov preprint gap was
  resolved using the original linked HTTP route and visual page inspection.
  Joyal’s species paper was also recovered from a researcher-hosted primary
  article copy; its Definition 1 is registered for the classical completion.
- `docs/research-plans/symplectic-phantasm-sources.md`: guidance scope audit
  and complete definition inventory, including the choices still unmade.
- `definitions.md`: D1701–D1713; `notation.md` updated. These are explicit
  stipulations, not promoted properties.
- `claims/CLAIMS.md`: fourteen new SP rows, all SKETCH. The register now
  has 158 claims: 121 PROVED, 33 SKETCH, three CONJECTURE, one REFUTED;
  there are 173 definitions. No prior mathematical status changed.
- `claims/PHANTASM-DAG.md`: fourteen lemma contracts with hypotheses,
  choices, dependencies, construction outlines and proposed falsifiers;
  seven OPEN research decision gates extend the graph. Contract checks do
  not prove the mathematical types or claims.
- `theory/checks/phantasm_contract_check.py`: schema, reference resolution,
  acyclicity, source hashes, promotion-record requirements, plan/decision
  agreement, and exact definition/claim/scope/status labbook restatements.
  The first observed run was a red cycle failure. Expectations are adjacent.
- Labbook Section 31 records the definitions and unpromoted propositions;
  the overview and root LaTeX inputs are updated.

**Next bounded task:** SP-WEYL, then SP-EGOROV and SP-TENSOR. Start from
the locally registered primary sources and the rank-one definition
conventions, not by extrapolating a rank-one theorem to arbitrary rank.
Write exact falsifier expectations before the proof lands. No mathematical
falsifier for these new lemmas has yet been implemented or run. Normalized
relation lifts, coherent classical completion, characteristic two and the
global arithmetic construction remain explicit downstream decisions.

Verification: the full repository session-close run passed **26 green
suites and 253 advertised red runs**. The final quest contract check passed
green and all **15** deliberate mutations failed at their intended gates;
a separate mutation of a canonical claim in a real temporary file copy
failed at the exact-restatement gate. The final PDF is **173 pages**, with
Section 31 on pp.166–173; the real build and final lockstep gate passed.
Frozen records are under `numerics/symplectic-phantasm/results/`. The
contract suite was rerun after the last historical source gap was resolved.

## Historical state before the pivot

Updated: 2026-09-09 (later session), fundamentals steering recorded; earlier the same day: composite boundary, degree completion and joined limit admitted.
The mainline FCR-2 state remains the interrupted 2026-09-01 state.

Read order gate: `CLAUDE.md` -> **`PRD.md` (constitution; it wins)** -> this.

## Steering 2026-09-09 — fundamentals of the two categories

TJO restated the programme from scratch and Claude assessed it. The full
record, with TJO's framing and the assessment kept separate, is
`docs/research-plans/fundamentals-two-categories.md`. No claim or definition
changed; no literature named there is yet registered in `refs/LEDGER.md`.

Decisions and positions recorded there, in one line each:

- C_p goldilocks candidate: symplectic F_q-spaces with Lagrangian
  correspondences (Weinstein category); Weyl quantisation becomes a functor
  whose image is the Gaussian operations. Nonlinear point maps do not
  quantise (Gross); higher Cliffords are nonlinear Lagrangians / the degree
  filtration on the function ring of L.
- Direct sum in Q_p needs disjoint union in C_p: C_p must be a rig category
  of symplectic finite sets, and Fock is its free commutative monoid.
- Field extensions add no quantum objects, only distinguished morphisms;
  Frobenius is already a Clifford permutation. Partial trace is dual to
  symplectic inclusion; the channel category is the stochastic closure.
- The single-prime p -> 1 limit yields Soule-type zetas 1/(s-k), never
  nontrivial zeros. The object with zeta(s) as spectral data is
  Bost-Connes, which realises TJO's powering-as-CP-map, direct-sum-as-
  particle-number and noncommutative-Frobenius-as-modular-flow intuitions.
- Proposed reframing, not yet adopted as a work order: keep Q_p per prime,
  take the restricted tensor product over all p, choose a reference state,
  study the modular flow; use the F_1 skeleton to glue primes, do not take
  p -> 1. The candidate novelty is a "symplectic Bost-Connes system".

TJO has not yet decided whether this reframing replaces the composite
p-to-one boundary programme below or runs beside it. Until that decision,
the section below remains the active goal.

## Current direction — composites before the p-to-one boundary

The user clarified the programme after reviewing the completed counting
construction. Seek a sufficiently rich arithmetic symplectic/process C_p
and quantum realization Q_p, with tensor-like and direct-sum-like
constructions BEFORE specialization. Already assembled systems may retain
quantum structure even when their isolated constituents become operationally
trivial. The meaning of that triviality must be specified; a pure reference
limit alone does not collapse the full observable algebra.

The user's FINAL clarification is essential: BOTH tensor and direct-sum
composition may disappear on Q_1. Neither their total endpoint descent nor
the existence of a conventional C_1 is required. Study the represented
composite first, then its boundary. Q_1 may initially name only surviving
quantum systems and distinguished processes, with their arithmetic origins
retained. Any additional categorical or monoidal structure is to be found,
not imposed as an acceptance gate.

A surviving actual Frobenius CP action on noncommutative quantum data is
central. The discussion treats a Frobenius/scaling connection to arithmetic
zeta spectra, ultimately the Riemann spectral picture, as a guiding research
ambition; no such identification is proved. Preserve the distinction
between a CP channel, its implementation, and its reference/spectral trace.
The functor-of-points and matrix-valued quantum-probe perspectives are
candidate ways to reconstruct the represented limit without C_1.

Concrete plan: `docs/research-plans/composite-quantum-boundary.md`.
First bounded work order: `briefs/composite-boundary-target.md`.
Start with the admitted Hecke scalar/classical/matrix composition ladder as
a control, then seek one actual arithmetic Frobenius boundary witness in
F2->F4 and F3->F9, followed by relevant tower/singular-degree tests. Keep
independent tensor, collective assembly, classical tags and coherent sums
distinct. Full mixed arithmetic compatibility must be constructed, not
inferred by juxtaposing existing endpoints.

The user explicitly made this the active goal and authorized independent
verifier and blind-critic agents. This direction takes priority over
historical "next steps" below. FCR-2 and unrelated campaigns remain paused;
no older conjecture or frozen marked-module draft has been promoted.

### First milestone — an arithmetic composite quantum remnant

Six new CMP claims and D1601--D1607 are admitted after the capped review.
At that phase the register had 141 claims: 118 PROVED, 19 SKETCH, three
CONJECTURE, one REFUTED; 157 definitions. The finite-phase PDF had 160
pages. The completed package below brings the current PDF to 166 pages.

For E/K, |K|=p^s and [E:K]=n, form three-register orbit sums
v_(O,k)=|O|^(-1/2) sum_(x in O)|x,sigma^k(x),x sigma^k(x)>.
They require no orbit origins. Simultaneous Frobenius fixes these graph
vectors, while R=M(I tensor U tensor I)M* shifts the relative index k.
Actual graph tests and this multiplication-conjugated Frobenius generate
the common M_n block on primitive relative orbits.

One copied POS reference and two fixed zero ancillas prepare that block
with probability c_n(t^s)/(n t^(sn)), of order one and coefficient
s phi(n)/n. Its common conditional state is |0><0|. The same final
coherent test has conditional probabilities 1 after R, 0 after identity,
and 1/n after computational dephasing. The ordinary primitive branch is
zero at t=1; its first grade is the noncommutative quantum remnant.
This is an orbitwise/composite descent result, not a theorem that every
full single-field observable algebra becomes scalar.

Fixed-base graph transfers compose without origin choices. Actual
first-register Fourier has code-return probability 1/|E| and its retained
orbit phase; the ambient failure is kept. The full finite implementing
spectrum has Tr(R^j)=q^gcd(n,j) and determinant
product_(d|n)(1-z^d)^(c_d(q)/d), with the channel spectrum kept distinct.
Randomized copied-reference moving weights have first coefficients
proportional to phi(d)/d, supplying the next degree-completion input.

The hostile verdict was FAIL(CB-C1) with one MAJOR degree-one scope
defect, no FATAL, and two minor notation/CLI repairs. Root closed all three
mechanically in one repair wave. Moving-sector conditioning now explicitly
requires n>1; the ordinary spectral formulas still allow n=1. Verdict and
adjudication are `theory/verdicts/composite-boundary-{r1,adjudication}.md`.
Canonical proofs are in `theory/sidequests/composite-boundary/`.

Independent finite verification: 76,584 exact comparisons over six
relative fibres, nineteen mathematical mutations and twenty CLI flags.
The complete repository suite passed 23 green runs and 210 advertised red
runs. `numerics/composite-boundary/results/SESSION-CLOSE-FINITE.json`
records this phase's source/PDF hashes; other frozen evidence is adjacent.

### Completed degree and joined-limit stages

CMP-COMPLETE/MELLIN and D1611--D1612 are now admitted after their own
capped review, followed by CMP-JOINT-LIMIT and D1621 after a separate
review. There are nine new PROVED CMP rows altogether. The current root
register is 144 claims: 121 PROVED, 19 SKETCH, three CONJECTURE, one
REFUTED, with 160 definitions. Labbook Sections 28--30 occupy pp.154--166.

Actual fixed-base arithmetic encoders induce the zero-extension corner
maps between the moving divisor-block algebras. Their derived weights
phi(d)/d are compatible. The norm completion is the c0 sum of M_d(C),
d>=2, with a faithful lower-semicontinuous semifinite trace on that
nonunital algebra. Relative Frobenius extends to an OUTER automorphism
of its minimal unitization, spatially implemented by the direct sum of
actual cyclic shifts. It is inner in the larger multiplier product;
this completion-dependent meaning of outer is explicit.

A declared central degree regulator for real beta>1 gives a faithful
invariant trace-class reference with normalizer
zeta(beta)/zeta(beta+1)-1. The implementing spectrum is the unit circle
with root-of-unity point spectrum. The logarithmic degree regulator
is central, not the Frobenius generator. No Riemann-zero spectral
identification or unregularized infinite trace is claimed.

The completed reference is also a TRACE-NORM limit of actual finite
arithmetic experiments: choose degrees 2..D with prior proportional to
d^(-beta), prepare the exact rho_(E_d)(log t), perform the copied primitive
instrument, and randomize the relative index on success. Every degree
and failed preparation history is retained. The rescaled success
v_d(t)=c_d(t^s)/(s d (t-1)t^(sd)) lies in (0,1] and extends to phi(d)/d.
This supplies a uniform summable bound and a positive normalizer floor.
Both iterated limits and every joined path D->infinity,t->1 converge to
the same rho_beta. The physical event remains rare with first-order rate
s Z_deg(beta)/(zeta(beta)-1). The randomized reference is stationary;
the earlier unrandomized |0> preparation remains the Frobenius witness.

The two later reviews found only minor cutoff/alias and exact-reference
clarifications, all mechanically closed in one wave per artifact. The
three new independent checkers passed 76,584, 41,216 and 9,272 exact
comparisons. Final executable coverage is 25 green checker runs and 237
advertised mutation runs; aliases are counted as runs, not distinct data
scenarios. The earlier full-suite snapshot's 23 checker hashes remain
unchanged, and the two later canonical checkers have their own final runs.

The goal's requirement/evidence audit is
`docs/research-plans/composite-boundary-result.md`. Its consolidated
verification is `numerics/composite-boundary/results/FINAL-VERIFICATION.json`.
Canonical proofs are the four files under
`theory/sidequests/composite-boundary/`. Historical submitted drafts remain
under `docs/research-drafts/` with READMEs pointing to the repaired versions.

The scoped exploration has supplied its finite quantum remnant, a concrete
positive completion, an arithmetic trace connection and a uniform bridge
from finite prelimit assemblies. Stronger questions remain separate:
uniqueness of the source/completion/prior; larger mixed arithmetic processes
and changing-base comparisons; global spectral structures beyond cyclic
Frobenius. C_1 and total endpoint tensor/sum operations were not required.
FCR-2, MIX-ALL, LIM-SIGNED and the frozen marked-module drafts remain at
their previous statuses and should not be resumed automatically.

## Completed goal — a positive arithmetic counting theory

The user requested an explicit goal to land a rigorous arithmetic theory
with a nontrivial useful p-to-one limit, then clarified that the minimum is
that something nontrivial remains and determining what remains is part of
the project. The completed construction is a retained-characteristic counting
specialization and finite graded operational boundary. It does not claim an
intrinsic characteristic-one field or promote the stronger MIX-ALL conjecture.

Result/acceptance record: `docs/research-plans/positive-counting-result.md`.
Work order: `briefs/positive-arithmetic-goal.md`. Six new POS claims and
D1501--D1507 are integrated, with two structured shards in
`theory/sidequests/positive-arithmetic/` and labbook Section 27, pp.146--153.
The register is now 135 claims: 112 PROVED, 19 SKETCH, three CONJECTURE,
one REFUTED; 150 definitions. No older conjecture or unrelated campaign was
silently promoted or resumed.

### The common positive theory

Fix an actual finite field E=F_(p^r) and retain its characteristic, field
tables, phase, register and all actual arithmetic operators. For h>=0 and
t=exp(h), the exact reference uses zero and nonzero Frobenius-period classes:

    D_E(h)=P0+sum_(d|r) b_d(exp h)/b_d(p) P_d,
    rho_E(h)=exp(-r h)D_E(h),
    b_1(t)=t-1; b_d(t)=c_d(t) for d>1.

The unique class-uniform reference is positive, faithful for h>0, and
rho_E(log p)=I/p^r. It is generally NOT TRACIAL. Positive ordinary Taylor
coefficients belong to D_E, while rho_E is the normalized Poisson mixture.
The coefficient A_Ek has trace r^k/k!; B_E=A_E1 is faithful on nonzero labels.

All named finite-field embeddings, including degrees divisible by p,
satisfy J_i^*D_EJ_i=D_K and J_i^*L_EJ_i=L_K. Reference code restriction,
all towers and both Fourier-transported decoder branches are coherent.
Fourier transports a reference to its actual conjugate, not to a reset
canonical reference. The exact code-success probability is exp((s-r)h).

The positive-series CP category retains the FULL actual arithmetic source,
with ordinary trace used for channel normalization. Actual amplitudes compose
coherently before any prescribed CP measurement. Coefficientwise Cauchy
composition/tensor and positive scalar normalizers supply a common positive
rule for mixed experiments; no intermediate sector compression is inserted.

### Finite sufficient boundary and the mixed protocol

For m independently prepared field references, retain

    L_word(h)=tensor_j(P_(E_j,0)+h B_(E_j)).

For EVERY nonzero fixed finite-dimensional CP branch, its output under
D_word and L_word has the same first nonzero matrix coefficient and order,
at most m. The conclusion survives every later fixed CP continuation,
independent tensor and entangling operation. Finite generated reference
protocols can preallocate their references; the bound counts those allocated
registers. Leading normalized state alone is insufficient for later rare
postselection, so the full finite profile is retained.

Every proper finite-field extension admits a,b with T(ab)=0 and
T(a^q b)=1. The actual protocol postselects E,E,K references to a,b,0,
uses target V, relative Frobenius on the first control, multiplication,
target Fourier, retained J decoding and successful inverse base Fourier.
Its rare preparation has order 2 and positive coefficient; decoder success
is 1 and target is 1. Removing Frobenius or multiplication gives target 0.
Removing Fourier gives success 1/kappa in regular degrees and 0 in singular
degrees; dephasing the coherent target gives success 1/kappa. This is a
uniform all-extension result, not a theorem inferred from a few examples.

Universal surviving data include the first nonzero-sector relative moments
Tr(sigma_(E,1) U_E^(s j))=gcd(n,j)/n for r=sn, the earlier phi(d)/(r-1)
moving-orbit blocks, code-failure leading coefficient r-s, and order d for
d independent nonzero multiplication controls. The relative moment formula
is extracted by coefficient one from the reviewed Frobenius moment; its
short derivation and mechanical finite checks are recorded.

### Scope that must stay explicit

The actual p, field multiplication tables, cyclotomic phases and register
dimensions survive as labels. Some individual probabilities and endpoint
purities distinguish p=2 and p=3. This is a counting/reference limit, not a
varying-characteristic operator category. The ordinary zero reference
endpoint is P0; the finite graded profile retains the rare conditional data.

The new rule does not continue every coupled point count by substituting
t for p. Independently prepared x=y!=0 has order 2, while an actual copied
single reference gives order 1. Coordinate unitaries transport field references
rather than resetting them to independent prime-field references. Exact
finite-h probabilities and arbitrary parameter-dependent angle/cancellation
families are outside the finite-profile adequacy claim. MIX-ALL and the
older changing-angle comparison remain open; LIM-SIGNED remains conjectural.
The new positive theory does not depend on those unresolved claims.

### Review, evidence and publication

One prover pass and one target-blind hostile review returned PASS, with one
MINOR wording fix distinguishing positive coefficients of D from those of
rho. Root applied and verified the fix; no new hostile round. All six scoped
POS statements are PROVED. Review context reuse and same-family limitations
are explicit in `theory/verdicts/positive-arithmetic-r1.md`; adjudication is
`positive-arithmetic-adjudication.md` beside it.

The new independent checker has 16 actual mathematical red modes. It tests
p=2,3,5, all seven gate groups, full mixed protocols on six extensions,
coherent inputs, later rare conditioning, and explicit residual p dependence.
Additional hostile probes include F64, a twisted embedding, and p=7.
The full repository verification passed 22 green checkers and 190 advertised
mutation runs; final PDF/lockstep checks follow the prose/figure integration.
Frozen inventories and exact outputs are in `numerics/positive-arithmetic/results/`.
The figure source is `scripts/plot-positive-arithmetic.py`; the Makefile now
tracks figure assets so changing a figure causes the PDF to rebuild.

The goal's clarified minimum is met by this complete positive counting
construction with its nontrivial graded operational content. Stronger
intrinsic or angle-compatible specializations remain separate research goals.

## Previous completed round — general Galois structure and arithmetic tower limits

The user requested informed conjectures followed by the standard prover,
verifier and hostile workflow, and insisted on general statements for arbitrary
extensions/towers. The completed work order is `briefs/arithmetic-limits-target.md`.
The new statements are in labbook Sections 24--26; Section 23 was reviewed
and its four prior sketches admitted after one checker/phase repair.

**Register:** 129 claims: 106 PROVED, 19 SKETCH, three CONJECTURE, one
REFUTED; 143 definitions. Six new positive claims were admitted in this
round and four earlier orbit claims were promoted. Two new conjectures remain.
The mainline FCR-2 and unrelated marked-module work were not resumed.

### General extension and Galois results

GAL-FUNCTOR/DESCENT/IMAGE, D1401--D1405, apply to every base field K and
all its finite separable extensions. Nonzero finite etale K-algebras close
independent tensor; their admitted maps have constant positive finite rank.
The register is ell^2(Hom_K(A,K^sep)), of dimension dim_K A. Uniform
embedding-fibre pullback is an isometry and a faithful strong symmetric
monoidal functor, with exact tower composition, G_K-equivariance, explicit
separable-closure comparisons and retained CPTP decoders. All histories and
independent outcomes are typed. The image on a field extension is the Galois
group of its normal closure, via the normal core of an embedding stabilizer;
all finite Galois levels recover G_K as a profinite inverse limit. Finite-field
primitive degree-d atoms give d-cycles and the full tower gives Z-hat.

This degree register is not the cardinality-|A| arithmetic register. Its
primitive-orbit comparison does not identify its transfers with physical
field-label J/V or the earlier divisor-block inclusion. Inseparable extensions
are outside the admitted construction: Hom_K(A,K^sep) is empty when A/K is
nonseparable, while embeddings into an algebraic closure count separable
degree. General-field Fourier/Haar data have not been supplied. A possible
inseparable follow-up was asked asynchronously; no additional such work was
assumed in this round.

### Uniform Gram sectors and the positive tower boundary

MIX-GRAM/CHART/TOWER, D1421--D1428, are admitted with explicit strata.
For every finite-field embedding of degree n>=2 and kappa=|E|/|K|,

    sqrt(kappa)(J*V)_(x,a)=delta_(a,nx).

If p does not divide n, every singular-value square is 1/kappa. If p divides
n, one square is |K|/kappa and all others zero. The code ranges intersect
in one line exactly for quadratic characteristic two. The projection algebra,
physical weights, actual Fourier/logical reflection and Frobenius restriction
are derived for every branch. On the joint support U_E factors through U_K;
for |K|=p^s, U_E^s=I there. Larger ambient Galois action requires other sectors.

The unconditioned regular support trace 2/kappa has a complementary
projection of proposed weight 1-2/kappa, negative near kappa=1. The positive
replacement conditions on the chart first. Its M2 trace is Tr/2. As the
angle c tends to one, the chart projections coalesce but their normalized
difference tends to X, while the chart Fourier factor tends to Z. The full
regular Fourier operator is Z tensor B_i, with B_i=D_n^-1 F_K retained;
logical field data have not vanished. The singular degree>2 plane and the
quadratic characteristic-two residual chart are treated separately.

For any finite tower with all extension degrees invertible in p, corrected
trace maps L=V D_n compose exactly. Direct-to-path chart connectors are
coherent under all consecutive-block refinements and intertwine actual
Fourier and Frobenius. With kappa_j=t^a_j, a_j>0, the endpoint sends

    |0> -> |0...0>,
    |1> -> sum_j sqrt(a_j/sum_i a_i) |one excitation at edge j>.

At arithmetic points a_j are the increments of prime-field extension degree.
Independent tensor keeps the full path space and its higher excitation
sectors. Retained decoder success composes; stopped histories are not the
binary composite decoder. The chart parameter varies with the logical field
factor retained: this is not a full varying arithmetic process category.

### Two precise conjectures and the next research target

MIX-ALL requires a common positive filtered realization for every finite
mixed extension diagram, including p-dividing degrees, Galois comparisons,
Fourier-transfer relations, multiplication transitions, and specified
measurement placements with all outcomes. Objects, arrows, reference weights,
mixed-moment continuation and comparison maps must actually be constructed.
Separate constant matrix envelopes do not settle it. The next test must glue
singular and regular tower diagrams and compare actual mixed circuits.

LIM-SIGNED, D1441, tests the arithmetic closure forced by F_E^2=negation.
Negation is not a field automorphism at odd p. For every odd p and all r,
the conjecture gives exact internal/external orbit counts for the commuting
Frobenius/negation action on nonzero labels. Even-period external sectors are
predicted to vanish at second order, while internal sectors vanish at first
order. In degree two the proposed counts are p-1,p-1,(p-1)^2, with signed
orbit sizes 2,2,4. Exact finite censuses and polynomial leading-coefficient
checks support the conjecture; no all-degree proof was admitted. The
characteristic-two action is different and explicitly excluded from this row.
Research rationale: `docs/research-plans/signed-orbit-filtration.md`.

### Review and verification

Three one-pass target-blind reviews were completed, each followed by at most
one repair wave. The orbit checker now applies the actual coherent channel
and rejects an independently corrupted input; the Fourier phase uses its
named root. The Galois review demanded no repair. Mixed review required the
explicit full endpoint Z tensor B_i wording. Each adjudication is in
`theory/verdicts/`; no open FATAL/MAJOR remains on admitted statements.
Runtime thread limits required reuse of unrelated reviewer contexts, without
sharing target prover reasoning; the limitation is explicit in both new
verdicts. No cross-family independence is claimed.

The independent verifier supplies exact Galois, Gram, Fourier, tangent,
all-length connector and mixed-circuit falsifiers, including an actual F81
Fourier tower, characteristic-five and twisted-embedding critic checks.
The signed conjecture has a separate bounded exact checker. Final verification
covers 21 green checkers and 174 meaningful advertised mutation runs (including
a documented alias). A wrapped help token was removed from the new CLI;
its final advertised modes were rerun and required to fail mathematical gates
with exit one, excluding parser errors. The PDF/lockstep build is checked
again after final claim promotion. Frozen evidence and current source hashes
are in `numerics/arithmetic-limits/results/`.

## Previous continuation — a positive conditional orbit prototype

The historical account below describes the 2026-09-08 draft. Its four
SKETCH statuses were promoted on 2026-09-09 as recorded above.

The user asked to become familiar with the project and continue the F1,
composition and Frobenius work, especially whether Frobenius survives p->1.
The concrete continuation is now in labbook Section 23 (starts p. 128),
`theory/sidequests/frobenius-hierarchy/orbit-boundary.md` and
`orbit-composition.md`. Work order: `briefs/frobenius-boundary-target.md`.

**Status:** four new SKETCH claims FRL-ORBIT/POS/COMP/ACTIVE and four
definitions D1331--D1334. Structured derivations and exact falsifiers are
written; no independent capped review was run and no PROVED promotion is
claimed. The register now has 121 claims: 96 PROVED, 23 SKETCH, one
CONJECTURE, one REFUTED; 129 definitions. The prior package is unchanged.

### The positive construction and what survives

For extension degree r, the number of exact-period-d Frobenius labels is
c_d(p)=sum_(e|d) mu(d/e)p^e, d|r. Choose an origin in every orbit and
retain the same full M_d(C) action on every orbit of length d. This gives
a faithful marked observable representation of O_r=direct-sum_(d|r) M_d
in End(ell^2(F_(p^r))), with Frobenius direct-sum S_d and physical trace
sum_d c_d(p)p^(-r) tr_d. It is a selected subalgebra, not the full algebra
and not Frobenius's commutant. Origin changes give explicit unitary
comparisons; selected embedded tests need not stay literally unchanged.

Continue p by t>1 at fixed r. For d>1,

    c_d(exp h)=sum_(k>=1) h^k/k! d^k product_(ell|d prime)(1-ell^(-k))

has positive terms for h>0, and c_d'(1)=phi(d). Therefore conditioning
on nonfixed *basis labels* produces the fixed positive algebra

    O_r^+=direct-sum_(d|r,d>1) M_d(C),
    omega_(r,1)=sum_(d|r,d>1) phi(d)/(r-1) tr_d,
    omega_(r,1)(u^k)=(gcd(r,k)-1)/(r-1).

All retained blocks have positive weights. Frobenius has an exact
state/effect distinction: |0><0| on a cycle block has return probability
one initially and zero after S_d. At r=2 the family is a conditional qubit
with a flip, physically the orbit (alpha,alpha^2) in F4 at p=2. At r=4
it is M2 direct-sum M4, with weights changing from (1/7,6/7) at t=2 to
(1/3,2/3) at one. The ordinary unconditioned trace quotient still deletes
all d>1 blocks. This is a different, explicitly normalized boundary rule.

### Composition and inclusion that are actually included

Independent word tensor has product conditional reference states and a
positive complex CPTP envelope with ordinary sum-of-block traces. A pair
of cycles reblocks as C^gcd(d,e) tensor C^lcm(d,e); simultaneous Frobenius
acts as identity tensor cyclic shift. Keep the multiplicity factor quantum:
for d=e=2, replacing M4 by M2 direct-sum M2 halves the return probability
of a cross-orbit superposition. Associators compare through the common
Cartesian basis and telescope, so no literal internal-label equality is used.

For standard subfields with coherent origins, r|s gives a divisor-block
encoding, retained decoder and Frobenius diagram. Conditional reference
success is (t^r-t)/(t^s-t), tending to (r-1)/(s-1). For 2|4 this is 1/3;
two independent decoders keep all four probabilities 1/9,2/9,2/9,4/9.
Success maps compose in towers. Full instruments retain their histories.
No functor realizing *every* CP-envelope map in the full arithmetic source
has been constructed. Arbitrary named embeddings need additional origin
transport; the present comparison uses standard inclusions only.
The prime-field degree r=1 has no moving-label conditional atom. At p=2,
the active inclusion 2|4 compares F4 subset F16. The F2 subset F4 map
requires retaining additional ambient fixed-label data.

### Filtration and the mixed problem that remains

The earlier nonzero-control multiplication formulas below now have a
structured derivation and checker. Their sector weight is ((Q-1)/Q)^d,
their conditional gate trace zero, and their conditional squared L2
distance from the corner identity two. Frobenius and J preserve these cuts.
Overlapping control cuts use union cardinality, not summed cardinality.
Independent moving-orbit word weights vanish to order the word length.
These are separate filtrations; neither classifies arbitrary hierarchy levels.

The orbit prototype does not yet solve the full mixed arithmetic limit.
In F4, M^(2)(alpha,alpha,alpha^2)=(alpha,alpha,0), leaving the tensor of
moving-label sectors. The existing nonzero-cut V counterexample remains.
For the moving cut and its actual Fourier transport the exact mixed trace is

    Tr(P^mov F P^mov F*)/p^r=(1-p^(1-r))^2.

This is a second-order overlap, not a commuting intersection dimension.
Next work should construct a positive mixed section algebra retaining the
orbit and Fourier charts, actual multiplication transitions, all instrument
outcomes and the admitted transfer/Fourier diagrams. The independent-phase
incidence proposal is still a distinct route; the present construction does
not prove it or identify the two routes. Review the four sketches before
promotion, concentrating on marked choices and the scope of comparisons.

### Evidence and artifacts

`theory/checks/frobenius_boundary_check.py` checks exact cyclic-word and
F4/F16 orbit counts, rational boundary weights, Jordan derivative identities,
Born witnesses, coherent cycle reblocking, actual inclusion/decoder Kraus
matrices, multiplication counts and mixed scope examples. B1--B6 pass;
each of six named mutations fails its intended gate. Frozen outputs are
`numerics/frobenius-boundary/results/checks.json`. Finite tests do not prove
the general analytic or categorical statements. The labbook has a new
self-contained five-page section. Source snapshots for Hyde's necklace
polynomials and Yoshida's gcd/lcm cycle product are registered in refs/LEDGER.md;
the matrix boundary and positivity argument are derived locally.

Final validation: the full session-close gate passed all 19 green checkers
and 149 advertised mutation modes, plus lockstep and the real PDF build.
The inventory is frozen in numerics/frobenius-boundary/results/SESSION-CLOSE.json.

## Earlier steering — higher hierarchy levels and vanishing boundary sectors

Historical discussion before the continuation above. Its active-sector
calculations now have the FRL-ACTIVE sketch and permanent falsifier; the
remaining mixed positive-boundary target is still open.

After the completed arithmetic campaign, the user asked whether this approach
is likely to give something nontrivial as p->1. They endorsed the analysis
below and explicitly requested that all these learnings be recorded for the
next agent, then committed and pushed. This update records a discussion and
a next research target; it does not launch another proof/review campaign.

**Status boundary:** the active-sector formulas below were derived in chat
by elementary counting, with the exact finite scratch checks listed below.
They are not new registered definitions or PROVED claim rows and have not
passed the capped review. The admitted register remains 117 claims and 125
definitions. Keep the existing arithmetic theorems, these new calculations,
and the proposed filtered/renormalized endpoint distinct.

### Assessment of the p-to-one programme

A nontrivial quantum endpoint is already possible in the admitted Hecke
sector: H_3(1)=C direct-sum C direct-sum M_2(C). The new question is whether
Frobenius, arithmetic multiplication, code transfers and their composition
can survive together, with positive quantum probabilities.

The ordinary normalized physical trace would collapse the new multiplication
gates under its formal continuation to one. A promising alternative is that
the hierarchy organizes successive orders of degeneration, so the useful
endpoint is filtered and retains normalized information from vanishing
sectors. This is a reasoned research hypothesis, not an existence theorem.
Confidence is stronger in some nontrivial positive boundary than in a
canonical boundary retaining exactly the desired arithmetic composition.

The fixed-phase-level plan below remains a useful controlled experiment.
Its success would establish an incidence deformation with retained quantum
phases. It would not by itself establish that all the retained field tables
or phase data are necessary, or that the resulting nontriviality comes from
the coupled arithmetic/context structure. Require actual mixed relations and
observed distinctions, then determine which retained data can be discarded.

### Active sector of a multiplication gate

Use the admitted D1308 gate on d separate control registers and one target:

    M_E^(d)|x_1,...,x_d,z> = |x_1,...,x_d,z + product_j x_j>,
    Q=|E|=p^r, d>=1.

For this discussion only, let P_(E,d) be the computational-basis projection
onto the sector where every control x_j is nonzero, with the target arbitrary:

    P_(E,d) = (1-|0><0|)^(tensor d) tensor 1.

Use the normalized ordinary matrix trace on this *whole* register word,
tau_(E,d)(a)=Tr(a)/Q^(d+1), not a Hecke coefficient trace. Then

    w_d(Q) := tau_(E,d)(P_(E,d)) = ((Q-1)/Q)^d,
    tau_(E,d)(M_E^(d)) = 1-w_d(Q),
    tau_(E,d)((M_E^(d)-1)^*(M_E^(d)-1)) = 2 w_d(Q).

Derivation: there are (Q-1)^d active control tuples and Q target labels per
tuple. A multiplication-basis label is fixed exactly when product_j x_j=0.
Outside the active sector the gate is the identity; inside it, the target
undergoes a nonzero translation, which fixes no basis label. A permutation's
ordinary trace counts fixed basis labels. Finally expand
(M-1)^*(M-1)=2-M-M^*; its normalized trace is 2-2 tau(M), since the counted
trace is real. The expression is a trace/L2 diagnostic, not an assertion of
operator-norm convergence or a complete operational limit theorem.
If a specialization preserves this limiting normalized trace and sends M
to a unitary in an endpoint algebra with faithful positive trace, that
unitary must be the identity. Without those hypotheses the counting
diagnostic is not a universal collapse theorem.

The rational count w_d(Q) has a zero of exactly order d at Q=1. Writing
Q=1+epsilon gives w_d=epsilon^d/(1+epsilon)^d. Thus, **for this particular
multiplication family**, a gate of admitted exact Clifford level d+1
disappears from this diagnostic at order d. Do not generalize this to an
equivalence between Clifford level and vanishing order for arbitrary gates.
For fixed extension degree r, formally Q=p^r also gives order d in p-1,
with leading coefficient r^d. This is formal parameter algebra: no sequence
of prime powers tends to one and no new noninteger-Q quantum fibre exists
merely because the counting function can be evaluated there.

The previously discussed physical Frobenius diagnostic is
tau(U_r)=p^(1-r). With tau(1)=1 it gives
tau((U_r-1)^*(U_r-1))=2(1-p^(1-r)), first order in p-1 for r>1.
This makes Frobenius and the first two multiplication levels a useful small
test of different degeneration orders. Their reference spaces/traces must
still be specified before comparing these quantities.

### Conditional information survives at each arithmetic fibre

P_(E,d) commutes with M_E^(d), because the controls do not change. In the
corner P End(H_E^(tensor(d+1))) P, whose identity is P, the restricted gate
u_d=P M_E^(d) P is unitary. Its normalized corner trace is

    tau_P(a) = tau_(E,d)(a)/w_d(Q),
    tau_P(u_d)=0,
    tau_P((u_d-P)^*(u_d-P))=2.

These identities hold at every arithmetic field fibre, where w_d(Q)>0.
For this diagnostic the disappearing factor lies in the sector's reference
weight; the conditional gate has a nontrivial trace signature. This does
not construct a positive limit of the corner algebras or their representations
as Q->1. A zero-weight sector is discarded by the ordinary reference-trace
quotient, so retaining it requires a separately specified normalization rule.

Frobenius preserves nonzero labels and therefore preserves P_(E,d).
For a named field embedding i:K->E, injectivity gives

    P_(E,d) J_i^(tensor(d+1)) = J_i^(tensor(d+1)) P_(K,d).

These are immediate basis-level compatibility identities to formalize in the
next campaign. They do not assert compatibility with V_i or Fourier without
further work. In particular, separate conditioning can erase information
about how sectors sit in an ambient system and how they compose. Retain
those embeddings and instruments rather than identifying isolated corners
solely because their conditional gate traces agree.

### Finite evidence and a transfer scope check

One-off exact scratch enumeration used prime fields Q=2,3,5 and d=1,2,3,4.
It counted all basis fixed points and active points, verified the displayed
whole-space traces, and found zero active fixed points in every sample.
For example, at Q=2 the weights are 1/2,1/4,1/8,1/16, the gate traces are
1/2,3/4,7/8,15/16, and the squared L2 diagnostics are 1,1/2,1/4,1/8.
No permanent new checker or formal all-field proof was admitted by this
discussion; the counting argument supplies the candidate general formula.

When preparing this handoff, the already admitted F2->F4 transfer example
also gives an immediate guard against a false next-step diagram. On one
control let P_E^nz=1-|0><0| and P_K^nz=1-|0><0|. Since
V|0>=(|0>+|1>)/sqrt(2),

    P_E^nz V|0> = |1>/sqrt(2),   V P_K^nz|0> = 0.

Thus the naive nonzero-sector intertwining valid for J fails for V. A
forward construction must track mixed sector outcomes or transported/Fourier
dual cuts, rather than impose that false equality. This supporting scope
calculation is recorded here without a new claim-status promotion.

### Next primary experiment — a filtered positive boundary

Study active-sector normalization alongside the existing coupled-incidence,
fixed-phase proposal in `docs/research-plans/frobenius-coupled-limit.md`.
The two proposals are not yet proved equivalent. A bounded first campaign:

1. Formalize P_(E,d), its corner, trace weight, restricted gate and the
   counting/vanishing formulas for d=1,2, with the precise all-field scope.
   Prove Frobenius and inclusion compatibility and preserve the V counterexample.
2. Start with F2 subset F4; retain Frobenius and M^(1), M^(2), hence the
   first- and second-order active sectors. Keep the actual field operations,
   code embeddings, positive trace conventions and measurement instruments.
3. Specify what a filtered or renormalized endpoint means: its objects,
   arrows, equality, sector weights, normalizations and comparison maps.
   An associated-graded construction is a candidate, not an established
   positive quantum category. Compare with the admitted mirabolic distinction
   between regular and singular boundary states without importing its theorem
   for this new family.
4. Test mixed products, overlapping control sets, independent tensor,
   inclusion/trace/Fourier transfers and full success/failure instruments.
   Independent reference weights multiply, but overlapping sectors can have
   different intersection weights; do not infer general filtered composition
   from the separate d-fold formulas or from the hierarchy's generator labels.
5. Require a positive CP-compatible construction with a surviving measured
   distinction on a genuinely noncommutative sector, together with the mixed
   composition diagrams. Neither a nonzero formal coefficient nor a
   conditional trace alone establishes that target.

The user regards the higher hierarchy as potentially central. The concrete
new reason is the matched interaction arity and vanishing order in this
family, not an assertion that fixed higher levels form groups/categories.
Admit any new result through the repository's normal proof/check/review
procedure and update the labbook in lockstep. This handoff-only turn changes
no mathematical registry or labbook status and leaves research for the next
agent.

## Latest completed research — Frobenius, codes and higher Clifford levels

The user approved adjusting the input category to symplectic spaces,
isotropic/Lagrangian flags and arithmetic descent data, with Frobenius
morphisms, a CP realization and enough retained arithmetic structure for a
nontrivial p-to-one endpoint. They emphasized higher Clifford *levels*, not
higher categorical groups, and explicitly requested planning/orchestration.

The staged work order is `briefs/frobenius-hierarchy-target.md`. The first
arithmetic stage is now integrated: ten new PROVED claims, seventeen numbered
definitions, five structured proof shards, one standalone exact checker,
and two self-contained labbook sections. Full register: **117 claims,
96 PROVED, 19 SKETCH, one CONJECTURE, one REFUTED; 125 definitions**.
No earlier claim status changed. The marked-module drafts remain separate.

The admitted results are:

- FRB-TRACE/FROB: all-p trace symplectic geometry, exact Frobenius/Weyl
  covariance and order, and atomic tensor factorization with a named
  position basis and trace-dual momentum basis.
- FRB-CODE/TRANSFER: the subfield support code stabilized by
  Z_E(ker Tr_E/K), logical momentum through the relative-trace quotient,
  and inclusion/normalized trace-fibre isometries with exact Fourier and
  field-tower coherence.
- FRB-HIERARCHY/NATURAL: M_E^(d) has exact prime-field Clifford level d+1
  for every p and every d>=1, commutes with simultaneous Frobenius and
  intertwines subfield encodings; its logical action has that same exact
  level. Separate registers prevent small-characteristic degree collapse.
- FRB-EXAMPLE: in F2[a]/(a²+a+1) subset K[b]/(b²+b+a), Frobenius is
  (u,v)->(u²+av²,v²), with square (u+v,v) and order four. The support code
  has dimension four; the square's invariant-vector space has dimension ten.
- FRP-CAT/CP/DESCENT: a small typed arithmetic amplitude presentation,
  source-certified CP instruments, explicit preparations/discards and
  retained decoders. Success returns the smaller register; failure retains
  the ambient register. Tower histories and independent partial successes
  are typed explicitly, and the full Fourier decoder square holds.

For d=2 the Fourier-conjugated multiplication gate on the uniform product
state has return probability (2Q-1)^2/Q^4; at Q=2 it is 9/16. This is a
specified coherent experiment, not a claimed positive q-to-one family.

The amplitude coefficient field is Q(zeta_p,sqrt(p)); at p=2 this is a real
arithmetic fragment, not the full Clifford category. Its Hilbert and CP
interpretations are not claimed faithful or complete for arbitrary complex
states/CP maps. Higher hierarchy levels label generators and are not assumed
composition-closed. General isotropic contexts attach to the objects, but
not every context has an admitted process generator. Preserve these scopes.

Two blind native critics returned PASS with no FATAL/MAJOR. Four minor fixes
were made in one repair wave: one dependency edge, a fixed countable name
universe, normalized endpoint trace language, and removal of a tautological
A5 subcheck. Root verified the fixes mechanically. Adjudication:
`theory/verdicts/frobenius-hierarchy-adjudication.md`; both detailed verdicts
are adjacent. Native agents inherited their runtime models; exact model
metadata was unavailable and this is stated on the records.

The final new checker has **263857 exact green assertions and twenty
independent named red mutations** (plain --red is an alias). The final
source hash is 946ca4584424329e85b92107664d24c89942f194de42dd0737ddc372d77d8c12.
A disabled-gate copy correctly produces mutated PASS/exit0, proving that the
red option does not force nonzero status independently of the mathematical
check. Frozen results, version boundaries and independent reviewer outputs
are in `numerics/frobenius-hierarchy/results/`.

Final verification: the integrated PDF builds to **128 pages**.
`scripts/session-close.sh` passed all **18 standalone green runs and 143
advertised red-mode runs**; every red reached a nonzero exit. The five new
proof-shard size bounds, five primary-source hashes, claim-DAG acyclicity
and register counts were checked; representative hierarchy and process pages
were visually inspected. `numerics/frobenius-hierarchy/results/SESSION-CLOSE.json`
records the exact checker/mode list and hashes. All research/review lanes
are complete. The package and its verification were committed and pushed as
`622c49c`; subsequent handoff discussions do not change that evidence.

## Companion next-stage proposal — a coupled positive incidence/phase comparison

`docs/research-plans/frobenius-coupled-limit.md` gives the next bounded
proposal and six witness tests. It separates incidence q from a retained
cyclotomic phase level N, with arithmetic comparisons q=p^r,N=p for
extension-linear contexts and q=p at the larger restriction-of-scalars rank.
It proposes coupled isotropic constraint operators, actual Frobenius and
multiplication tables, code/trace transfers and the type-C decomposable
correspondence. The positive mixed section algebra and relation-preserving
comparison functor are **not constructed or admitted** by this package.

Start with F2 subset F4, one marked code isotropic, Frobenius, multiplication,
and a binary type-C composition correspondence. Require a surviving measured
arithmetic distinction, genuine noncommutativity, a named positive reference
trace, all transfer/Fourier diagrams and composition coherence. Formal labels,
a freely adjoined matrix factor, or separately lifted endpoint gates do not
meet this target. The physical normalized trace p^(1-r) would force a
trace-one endpoint unitary to be identity; the statement requires tau(1)=1.
The fixed-N proposal retains substantial arithmetic data initially and must
be assessed as that specific comparison, not advertised as the full p->1
limit of every Weyl system. The existing positive Hecke family is the benchmark.

## Earlier discussion — field extensions, Frobenius and operational descent

The user wants to study the category of arithmetic quantum systems over a
fixed prime p, regard one F_(p^r) Weyl system as a composite of r atomic
p-systems, understand quantum maps to smaller fields, and determine whether
field extensions/Frobenius survive the flag construction and its p→1
specialization as a natural noncommutative Frobenius structure. They approved
the following analysis and asked that it be preserved for the next agent.

**Historical evidence/status boundary:** this subsection preserves the
discussion before the completed hierarchy campaign. Consult the completed
research summary above for subsequent admissions. The formulas below were derived
and discussed in chat, with the finite computations explicitly described
below. They are not new admitted definitions or PROVED claim rows. No
definitions, claim statuses or labbook sections changed in this discussion.
Separate existing results, elementary candidate constructions, literature
theorems and open compatibility problems when resuming. The preceding
categorical-limit package remains at 107 claims/108 definitions.

### 1. Extension-field Weyl systems and atomic tensor factors

Fix a primitive p-th root zeta_p and let L=F_(p^r). Use

    psi_L(x)=zeta_p^(Tr_(L/F_p)(x)),
    H_L=l2(L).

An F_p-basis e_1,...,e_r identifies H_L with (C^p)^tensor r. This is an
actual Weyl-system factorization, not merely equal Hilbert dimensions:
use the trace-dual basis e^1,...,e^r for momentum, with
Tr(e_i e^j)=delta_ij. If x=sum x_i e_i, a=sum a_i e_i and b=sum b_i e^i,
the reference convention W(a,b)=Z(-b)X(a) gives

    W_L(a,b) = tensor_i W_(F_p)(a_i,b_i).

The basis-free prime-field phase space is L direct-sum L with alternating
form Tr_(L/F_p)(ab'-a'b), of dimension 2r over F_p. This is consistent with
the existing WH-SYMM result: the Weyl algebra/frame sees the underlying
prime-field symplectic structure; the L-scalar action is additional data.
Retain that scalar action if "one extension-field system" is to be
distinguished from unstructured r-qudit kinematics. Factorization into named
atomic sites is basis-dependent. Do not silently assume a self-dual basis;
position and momentum use dual bases. Common phase centres must be matched,
as in the existing cyclotomic central-product composition.

### 2. Frobenius is reversible; fixed points and descent are different

The field Frobenius sigma(x)=x^p gives

    U_r|x> = |x^p>,
    U_r W(a,b) U_r^* = W(a^p,b^p).

Trace invariance of psi_L proves the covariance in the reference convention,
including characteristic two. In a normal basis
alpha,alpha^p,...,alpha^(p^(r-1)), U_r is a cyclic permutation of the r
prime-field tensor factors. Thus Ad(U_r) is already a distinguished
automorphism of the noncommutative algebra M_(p^r)(C) at fixed p.

For s dividing r, K=F_(p^s) is the fixed field of sigma^s, but Frobenius
itself is an automorphism L→L. Degree-reducing arrows involve trace, norm,
fixed-point constructions or quantum transfers; they are not smaller-field
Frobenius homomorphisms. In particular,

    l2(Fix(sigma^s)) is generally not Fix(U_r^s),
    Tr(U_r^s)=p^gcd(r,s).

The trace equality counts fixed computational-basis labels. It does not
identify the fixed-vector Hilbert space with the smaller-field system.
Exact F4/F2 example: take F4=F2[alpha], alpha^2=alpha+1, normal basis
(alpha,alpha^2). Frobenius is SWAP, with Hilbert trace 2 and a
three-dimensional invariant vector space, whereas l2(F2) has dimension 2.
In normal-basis bit coordinates, the smaller-field basis subspace is
span{|00>,|11>}. Galois twirling is therefore not the desired degree reduction.

### 3. Inclusion, trace, Fourier duality and quantum reduction

For a named inclusion i:K→L, s|r and d=r/s, put T=Tr_(L/K). The two
canonical isometries from H_K to H_L are

    J_i |a> = |i(a)>,
    V_T |a> = |ker T|^(-1/2) sum_(T(x)=a) |x>.

The relative trace is surjective for every finite-field extension, even
when p divides d; |ker T|=p^(r-s). With the negative Fourier kernels used
in the project, the exact identity is

    F_L J_i = V_T F_K.

It follows from Tr_(L/F_p)(i(a)x)=Tr_(K/F_p)(a T(x)) and the displayed
normalizations. Inclusions and the normalized trace-fibre isometries compose
along towers; the latter use trace transitivity and multiplication of fibre
cardinalities. Both are Frobenius-equivariant. This supplies quantum
transfers without requiring character restriction compatibility.

**Do not repeat the existing phase error:** psi_L=psi_K composed with T,
whereas psi_L restricted to K equals psi_K^d. The latter can be trivial when
p divides d. This is exactly the previously proved obstruction in
`theory/wh-kappa-choice.md` §10 and
`labbook/sections/07_functoriality.tex`; it does not obstruct the trace-dual
construction above. No global choice compatible with all field embeddings
has been obtained by this discussion.

For either isometry V, the outcome rho→V^*rho V is CP and trace-nonincreasing.
These outcomes compose along towers and tensor under independent isometries.
Keep the success effect VV^* and its probability. Here rho denotes an
ordinary density matrix with Tr(rho)=1, not a coefficient-trace density h.

A specific deterministic completion is

    D_V(rho)=V^*rho V + Tr((1-VV^*)rho) I_K/|K|.

It resets the unsuccessful component to the smaller maximally mixed state.
Its Heisenberg map is a→VaV^*+tau_K(a)(1-VV^*), which is UCP and preserves
normalized matrix traces. If V:H_K→H_L and W:H_M→H_K, direct substitution
gives D_W composed with D_V = D_(VW). Equivariance of V gives Frobenius
covariance of D_V. Thus this is a concrete tower-compatible CPTP reduction.

Its tensor scope is narrower: generally D_(V tensor W) is not
D_V tensor D_W. The first resets both outputs if either component fails;
the second preserves the successful output. For a simple counterexample,
take two inclusions C^2→C^4, a state outside the first code and a pure state
inside the second. The outputs are respectively I_4/4 and
(I_2/2) tensor |0><0|. Preserve instrument/ancilla data when asking for
monoidal compatibility; do not promote tower coherence to a monoidal theorem.

### 4. Two distinct natural flag comparisons

**Base extension at fixed field-linear dimension n.** For K⊂L, inclusion
Fl_n(K)→Fl_n(L) is an isometry on flag-basis Hilbert spaces. Relative
positions are unchanged, so compression gives the based map

    H_n(p^r) → H_n(p^s),     T_w → T_w.

At these arithmetic fibres it is a surjective, trace-preserving UCP map
(a linear bijection), generally not an algebra homomorphism. The maps
compose along field towers. This is an observable-map direction; in
Heisenberg convention its trace-dual state process has the reverse direction.
Do not confuse it with D_V's large-to-small Schrödinger reduction. Nor does
arithmetic CP alone prove CP of an interpolated map at every real parameter.

**Restriction of scalars.** An L-linear full flag in L^n has prime-field
dimensions r,2r,...,nr. It lies in the F_p partial-flag space of type
(r,...,r), with the L-scalar action retained. Compression to the
L-stable flags gives the arithmetic UCP comparison

    e_(r^n) H_(nr)(p) e_(r^n) → H_n(p^r).

Use the actual geometric partial-flag adjacency basis and normalized corner
trace when proving its properties. Source field flags are the subspaces
stable under L multiplication, not all prime-field subspaces. This
comparison does not identify the two algebras or their full context sets.

Exact example: underlying F2^4 has 35 two-dimensional subspaces, but F4^2
has only five F4-lines. Enumerating stability under multiplication by alpha
selects exactly those five. Compressing the disjoint-plane adjacency to
them gives the off-diagonal adjacency of K5. Its squared diagonal is 16
before compression and 4 after squaring the compressed operator, explicitly
showing nonmultiplicativity.

Already n=1 distinguishes the constructions:

    H_1(p^r)=C, while H_r(p) can be noncommutative.

Allowing all prime-field flags adds contexts that the extension-field-linear
flag construction omitted. The claim that an extension atom equals r atoms
must therefore specify the context structure, not only the Weyl Hilbert space.

### 5. The present commutants erase Frobenius

Frobenius preserves flag relative positions, hence

    U_Frob A_w U_Frob^(-1)=A_w.

Its induced automorphism of the current Hecke invariant-transition algebra
is trivial. After restriction to F_p, Frobenius is an F_p-linear symmetry,
so this also follows from the GL-commutant construction. The same concern
applies to invariant mirabolic orbit data: adding invariant vector kernels
does not by itself retain a nontrivial Frobenius symmetry action.

The proposed remedy is to retain the flag representation with its
semilinear/Frobenius action, or equivalent equivariant/bimodule data, before
passing to invariant observables. **Do not identify the left symmetry action
on flags with a right Hecke transition merely because both become permutation
matrices in an apartment.** The existing endpoint permutation gates do not
by themselves prove specialization of the arithmetic Frobenius operator.

### 6. What can survive at p=1, and the representation/trace test

At fixed n, H_n(p^r) specializes algebraically to C[S_n], losing r from
that isolated algebra. Restriction-of-scalars rank, the partial-flag object
(r^n), and cyclic/Galois descent data can still record the extension degree.

A concrete endpoint candidate for the degree-expansion operation is

    Rcal_d:C[S_n]→C[S_(dn)],
    w→((i,a)↦(w(i),a)),      a in {1,...,d}.

This is a unital trace-preserving star embedding, since it comes from an
injective group homomorphism. It composes as Rcal_d Rcal_e isomorphic to
Rcal_(de) under the canonical regrouping of labelled factors. In the free
symmetric composition category it sends x to x^tensor d. It is a candidate
for the restriction-of-scalars/extension-degree operation, distinct from
the degree-preserving Frobenius unitary. Its identification with arithmetic
extension/descent and its full operational compatibility remain targets.
It is not an assertion that an unknown state can be copied nonlinearly.

The quantum representation and its reference trace cannot be carried over
by mere substitution of a real dimension p. The ordinary normalized tensor
trace of the three-factor antisymmetrizer has formal continuation

    dim(wedge^3 C^p)/p^3 = (p-1)(p-2)/(6p^2),

negative for 1<p<2 (at p=3/2 it is -1/54). This cannot be a Born probability.
The positive Hecke coefficient-trace family is a different interpolation.
Use the admitted Schur-Weyl/trace comparison in
`theory/sidequests/f1-limit/schur-weyl.md`: at fixed n its coefficient trace
is the large-physical-dimension limit, not the physical-dimension-one fibre.

There is a second exact diagnostic. For the cyclic shift U_r, the normalized
Schrödinger trace is p^(1-r), with formal value 1 at p=1. In a faithful
positive tracial endpoint, a unitary with tau(U)=1 satisfies

    tau((U-1)^*(U-1))=0,

and therefore U=1. A nontrivial endpoint Frobenius consequently requires
retained categorical/descent data, a different representation/reference
trace, or a separately specified singular-sector boundary rule. This is a
conditional constraint, not a universal no-go theorem for all F1 theories.
Existing mirabolic regular-versus-singular boundary distinctions are relevant.

### 7. Literature leads and concrete next work

- A. Vourdas, *The Frobenius formalism in Galois quantum systems*,
  https://arxiv.org/abs/quant-ph/0605054. Its tensor/dual-basis and Frobenius
  discussion is directly relevant; its chosen framework assumes odd p.
- Guy Henniart and Chun-Hui Wang, *Weil representations over finite fields
  and Shintani lift*, https://arxiv.org/abs/1303.5141. Theorem 4.1 extends
  the Heisenberg-Weil representation to the Galois semidirect product and
  relates Frobenius-twisted characters to smaller-field characters by
  Shintani/Gyoja norms. The basic form is
  Tr(tilde_rho_L(sigma,g))=Tr(rho_K(N_sigma(sigma,g))). The theorem assumes
  odd cardinality; it is not a characteristic-two or CP-channel theorem.
  The norm is on twisted conjugacy classes; an uncorrected product
  g sigma(g)... need not itself be a smaller-field element in a nonabelian
  group. Section 6 treats orthogonal direct-sum compatibility.
- Stacks Project, trace and norm, https://stacks.math.columbia.edu/tag/0BIE.
- Already registered: Gurevich-Hadani 0705.4556 (monoidal quantization and
  isotropic reduction, odd characteristic), Comfort-Kissinger 2105.06244
  and Comfort 2304.10584 (Lagrangian/coisotropic stabilizer relations with
  their stated scalar/normalization scopes). See `refs/LEDGER.md`.

The two arXiv papers initially had temporary extracts under
`/tmp/aqm-field-extension-reading/`. The 2026-09-08 hierarchy campaign has
now fetched and registered durable local snapshots under
`refs/frobenius-hierarchy/1303.5141/` and `quant-ph-0605054/`; precise
locators and hashes are in refs/LEDGER.md.

Exact one-off scratch computations (not a new committed checker or a general
proof) verified F4 Frobenius=SWAP, trace 2/fixed-vector dimension 3, the
unnormalized integer Fourier inclusion/trace identity, the 35-versus-five
subspace comparison and 16-versus-four squared diagonal, and a rational
8→4→2 example of D_W D_V=D_(VW). The general formulas above require their
own structured proofs and falsifiers before promotion. The working tree
was unchanged by that exploratory discussion.

**Next primary target on resumption:** a Frobenius-equivariant extension
theory, starting with F2⊂F4⊂F16. Retain the scalar action, Frobenius
unitary, inclusion/trace transfers, both flag comparisons and every reference
trace. Prove tower composition and distinguish it from independent-system
assembly; explicitly compare Fourier-dual transfers. Determine the enriched
flag representation data needed for nontrivial Frobenius and test the
candidate p=1 degree-expansion functor against it. Do not impose commutative
diagrams that identify distinct context sets, traces or failure instruments.

For a domain closed under independent arithmetic composition, finite étale
F_p-algebras (products of finite fields) are a useful candidate to examine;
their product gives a canonical tensor decomposition of the configuration
Hilbert space. This is a suggested domain to formulate, not an admitted
functor or a replacement for the detailed tower/transfer checks above.
The five reviewed-but-unadmitted marked-Hecke-module claims below remain a
separate integration opportunity. The field-extension/Frobenius direction
is now the user's specific research priority.

## Categorical-limit package — windup 2026-09-08

The user authorized comprehensive rigorous work with Sol and occasional Astra,
then set a cutoff of 03:00 Europe/Berlin (01:00 UTC). **The cutoff was missed.**
The clock was checked again at 05:04 UTC (07:04 Berlin), after agent usage-limit
errors; research was stopped and only integration, verification and commit
were continued. Do not resume automatically. The next work needs user steering.

Delivered: 37 new PROVED claims, 62 new numbered definitions, 15 structured
proof shards under `theory/sidequests/f1-limit/`, eight new self-contained
labbook sections, a protocol figure, four retained blind verdicts and the
combined adjudication `theory/verdicts/f1-limit-adjudication.md`.
The full register is now **107 claims: 86 PROVED, 19 SKETCH, one CONJECTURE,
one REFUTED**; there are **108 definitions**. Earlier mainline/FCR-2 statuses
are unchanged. The final PDF build and full suite outcome are recorded below.

Core result: the full finite graded self-adjoint completion has positive
continuous traces, proper traced assembly inclusions and continuous UCP
expectations. Its interval and germ operational categories include normalized
states, effects, instruments, classical routing, preparations and discards.
Endpoint objects and individual finite circuits lift locally, with explicit
unitary connectors; every specified finite experiment has continuous Born
weights, and conditioning converges when the limiting event has positive
probability. No global canonical lift or lifting of arbitrary endpoint
relations is claimed. The H3 experiment explicitly uses a Lüders instrument:
preparation success 2/3, conditional return 1/4, joint endpoint probability1/6.

Additional proved results: canonical unitary cactus exchange on positive Hecke
categories; algebraic Day/right-module comparison; Schur-Weyl quotients and
physical-trace convergence; explicit rigid/TL/Fibonacci comparison data;
mirabolic vector/Weyl-Fourier identification, positive trace for every q>1,
reference GNS quotient C[S_n], and a genuinely typed regular one-sided
operational boundary functor; arithmetic type-C/affine shuffle correspondences.
The trace weight on arbitrary projection objects is `w_X`, distinct from the
existing fusion dimension `d_X`. Interval/germ Kraus equality is pointwise/
eventual coefficient-Gram equality, without continuous mixing unitaries.

Review: core Sol prover/Astra critic/Sol repair; composition Sol prover/Sol
critic/root repair; bridge Sol prover/Sol critic/Astra+root repair; Karoubi
Astra prover/Sol critic PASS. The precise fixes and scope are in adjudication.
No re-review-to-fixed-point was run. The operational wiring hypothesis W is
instantiated by D1218/CWIR-1--3, including the explicit singleton identity.

Five further marked-module claims were drafted, and their independent Sol
verdict is PASS, but **they are not admitted**: no D1271--D1276 or corresponding
claim rows entered the root registries or labbook. Their complete drafts and
verdict are preserved under `docs/research-drafts/f1-marked-action/` for the
next session. They concern R_m(q) tensor H_n(q) -> R_(m+n)(q), a right module
action, not a tensor law for two marked systems. Their checker is retained as
supporting draft evidence. This is the clearest next integration task.

Scope still excludes a universal specialization of the entire Weyl observable
algebra, every phase and all polarizations. The proved system family is the
named Hecke/flag sector with its explicit vector and polarization comparisons.
Astra and Sol agents hit the account usage limit during final integration/
review reporting. Their already written results were preserved; all agents
were interrupted at windup and no further delegation is intended.

## Latest result — a positive operational F1 subsystem family

Final categorical-limit verification (2026-09-08): the integrated PDF builds
to **114 pages**. `scripts/session-close.sh` passed all **17 standalone green
runs and 122 distinct advertised red-mode runs**; every red reached the
required nonzero exit. The final lockstep gate passed after the last LaTeX
transcription corrections. Four new primary-source hashes and all fifteen
proof-shard size bounds were verified; whitespace checks passed. The protocol
and boundary pages were visually inspected. The provisional chat tally of
121 mutations was corrected by counting the actual unique log records.
The main work is committed as `d639c5d`; this record is the final closing edit.
All research and agent work is stopped.

The user's request to chase subsystem-first QM now has a concrete candidate:
A(S)=C[Sym(S)], with coefficient-trace densities, Born effects, CP dynamics,
subgroup expectations, and proper disjoint-assembly inclusions. The source
normal-map category is FinPInj, with an actual dagger lax symmetric monoidal
functor into finite traced C*-algebras and bistochastic CP maps. The empty
partial map is the reference reset tau(a)1, not zero CP. Retained local
Kraus lists provide coherent context-sensitive processes.

Deliverables: docs/sidequests/f1-operational.md and labbook section 12,
pp. 60–70 of the 70-page PDF. The original broad comparative map remains
in docs/sidequests/f1-qm.md and section 11. The new section has an exported
subsystem-overlap figure. The eleven new pages were visually inspected;
no overfull box originates in the new section. Existing mainline typesetting
warnings were not treated as new failures.

Core results to retain:

- Positive Hecke algebras H_n(q), all real q>0, with faithful coefficient
  trace tau(T_u* T_v)=delta_uv q^length(u). At prime-power Q they are the
  GL-invariant complete-flag transition algebras (Iwahori 1964). Ordered
  block embeddings and UCP coefficient expectations are coherent.
- Algebra types H1=C, H2=C², H3=C²+M2 do not depend on q, but two overlapping
  H2 inclusions retain q through a=q/(q+1)², uniquely on q>=1. At one,
  the standard S3 block is a collective qubit. Its full coefficient-trace
  density is 3P, not P; a locally invisible transposition changes a return
  probability from one to 1/4.
- Equality of local Kraus Grams is exactly stable scalar-unitary mixing
  and equality in all finite contexts. For n>=1, an ambient size 2n−1
  suffices; for n>=2 it is sharp. Positive Born gaps at n=2,3 are 1/2
  and 1/18. The analogous positive-Hecke generalization remains SKETCH.
- Two disjoint size-three regions carry a Bell density 9P in C[S6],
  marginals (3/2)z and CHSH 2sqrt(2). This explicitly checked example
  remains supporting SKETCH, rather than a separately reviewed theorem.
- The partial-flag corner category Gamma_q is explicit over a localized
  coefficient ring; its q=1 tensor-power endomorphisms are C[S_n]. It
  has additive/idempotent completion, but rigidity is not stipulated and
  normalized systems exclude zero objects.
- Apartment compression provides a UCP arithmetic-to-endpoint comparison
  T_w(Q)->w, natural for ordered block inclusions and coefficient
  expectations. It is not multiplicative and does NOT intertwine every
  partial-flag corner compression. This limitation is displayed, not hidden.

The generic nonzero unitary-fusion-category CP construction is also proved.
Fibonacci illustrates locally invisible braids becoming visible in a larger
fusion space. Type-C flags, the Temperley–Lieb/SU(2) centralizer tower,
root-of-unity Fibonacci, and the original F1 routes remain distinct. In
particular the faithful flag trace cannot descend to a nonzero TL quotient;
that branch requires a separate Jones/Markov trace and duality conventions.

Scope: this is a flag-context sector extracted from a **named polarized**
Weyl system. The joint controlled-projector coupling is explicit, but there
is no full Weyl/phase/polarization specialization or universal uniqueness
claim. The next mathematical target is a coherent refinement/polarization
comparison that includes these couplings, alongside the type-C branch.

Review: Sol/xhigh prover and blind critic only; no Astra or Claude subagents.
One round, one repair, mechanical adjudication in
theory/verdicts/f1-operational-adjudication.md.
O1 excluded zero objects; O2 consolidated mathematical checker gates and
added deeper data mutations; O3 repaired full-density wording; O4 narrowed
sample descriptions. No open MAJOR remains on the eleven promoted rows.
Seven supporting rows stay SKETCH. Current register: **70 claims, 49 PROVED,
19 SKETCH, one CONJECTURE, one REFUTED**. Seventeen new definitions bring
the total to 46. Four admitted structured proof shards are each 200–500 lines.
There are now 38 local F1 PDFs with ledger hashes/locators, nine added here;
all hashes were checked. Source bodies remain ignored.

Verification: the new exact checker passes fourteen aggregate mathematical
gates; all twenty-five data mutations exit one with a named mathematical
failure and no interpreter exception. Expectations record exact sampling
and gate-level coverage, without claiming individual-assertion coverage.
Full repository session-close verification PASSED: all 11 standalone green
runs and all 84 advertised red modes. The final PDF rebuild and lockstep
gate also passed after the last wording changes; source hashes, local links,
claim/definition counts and the staged whitespace check passed.

## Latest F1 steering — subsystem families with genuine QM semantics

2026-09-07: the user's intended object is the category of **families of
subsystems and their composition**, rather than individual particles.
Extract enough intrinsic arithmetic structure from the p-qudit theory to
remember p, forget chosen concrete realizations, and then formulate p→1.
The endpoint MUST still be QM: density operators/normalized positive
functionals, CP dynamics, the Born rule, and compatible assembly of states
and processes. A functor realization in C*-algebraic quantum processes is
the acceptance criterion. Fib is the example of nontrivial composition;
the user has not conjectured that Fib equals the F1 endpoint.

Do not impose a strong monoidal fibre functor to ordinary Hilbert spaces
on every candidate. Proper inclusions of products of local algebras into
composite algebras allow collective fusion degrees of freedom. Merely
assigning isolated CP maps does not determine their extensions to those
degrees of freedom. Classical/combinatorial input models remain surveyed,
but are not by themselves acceptable endpoints under this clarification.

New source leads are local and registered: Comfort–Kissinger 2105.06244
(odd-prime affine Lagrangian/stabilizer process equivalence), Comfort
2304.10584 (mixed/coisotropic extension), Gurevich–Hadani 0705.4556
(monoidal quantization), Bonderson–Shtengel–Slingerland 0707.4206
(anyon density/measurement formalism), Ahmadi–Kissinger 2211.03855
(fusion-space quantum computation). That preceding turn was a conceptual scoping update;
no new theorem status was promoted and the mainline remains untouched.

## F1 sidequest — comparative formulation, qubits and tensor categories

User directives: ground the work in the literature; explore all the relevant
analogies rather than selecting one prematurely; compare the qubit analogue
and tensor product in each; investigate tensor categories as possible primary
quantum objects. Sol subagents permitted, Astra and Claude subagents forbidden.
All four subagents used this session were Sol/xhigh.

Deliverables: `docs/sidequests/f1-qm.md` is the comparative research map;
`briefs/f1-sidequest.md` fixes scope. Labbook section 11, pp. 47–59 in the
then-59-page PDF, gives the self-contained mathematics and source links. All thirteen pages of the initial section were visually inspected. The
subsequent operational clarification was checked at the opening/table
boundary, and the rebuilt section has no overflowing text.
The initial literature pass has twenty-four primary PDFs (including a
separately identified discovery thesis), local under `refs/f1/`, with URLs, hashes and
specific locators in `refs/LEDGER.md`; bodies remain git-ignored.

The broad map covers direct quantum F_un/Thas frames, pointed and cyclotomic
modules, Tits–Weyl models, bands/crowds, Hall/groupoid oscillators, quantum
tori/Habiro, lambda descent, Bost–Connes, tropical/motivic boundaries and an adjacent fermionic tensor analogy.
Positive literature anchor: Lorscheid 1201.1324 Proposition 5.5 covers the
reference UT3 Heisenberg model. The newer crowd specialization retains the
central cross-term relationally; its signed fibre has 27 points/319 triples,
Krasner eight points/152 triples. Do not call either an ordinary finite group.

Admitted core: `theory/sidequests/f1-cyclotomic.md`, seven PROVED F1 rows,
after one blind Sol critique and repair. Data are finite abelian A,
exp(A) dividing N, named phase embedding iota. The cocycle is eta(a)^(-1)
with W=Z(chi)X(a); the ring identification chi_b=psi(-b·) recovers D8/D16.
Independent-system tensor uses balanced smash and central product, not two
independent centres. Raw ring comparison is a central pushout; F4 maps its
order-64 raw group onto the order-32 phase group. The strict normalizer is
affine/quadratic, while Fourier requires sums.

Supporting comparisons are SKETCH in `theory/sidequests/f1-comparisons.md`.
The revised projective cyclotomic matrix functor is also SKETCH. Its original
unspecified geometric-category clause was rejected, not admitted as a vague
universal conjecture. `theory/verdicts/f1-r1.md` and `f1-adjudication.md`
record the capped review. Definitions use D1001–D1013, deliberately reserving
the lower numbers for the pending mainline. At that initial admission the claim counts were 52 total,
38 PROVED, 12 SKETCH, one CONJECTURE, one REFUTED; old statuses unchanged.

Qubit/tensor results worth retaining:

- Normal partial maps on the rank-two pointed set span M2(C) after complex
  realization; smash realizes as Hilbert tensor. This image is not the
  unreduced partial-injection monoid algebra. Bare pointed-set QM therefore
  need not be identified with the trivial N=1 perfect phase kernel.
- Thas's rank-two frame has N+2 rays; its two-copy frame has
  N(N+1)(N+2) nonproduct rays. At N=1: 3 one-system rays, 15 composite,
  nine products and six nonproducts. This is factorization, not a Born rule.
- Rep(D8) and Rep(Q8) have a two-dimensional object sigma with tensor square
  the four invertible characters; Shimizu 1005.4500 identifies their distinct
  Tambara–Yamagami parameters ±1/2 and indicators ±1. Fixed nontrivial
  central-character sectors are not tensor closed. Internal fusion and
  independent composition with matching central characters are different.
- A fibre functor is needed for the proposed categorical qubit:
  End_Rep(H)(sigma)=C and Hom_Rep(H)(1,sigma)=0, whereas after realization
  the full observable algebra is M2(C). Category alone does not supply all
  state vectors. Hall/Fock gives another tensor-categorical route: two
  identical bosons in two modes have dimension three, not four.

Exact checker `theory/checks/f1_check.py`: thirteen gates and thirteen named
mutations, expectations in `f1_EXPECTATIONS.md`. Session-close discovered an
existing interface mismatch: the five nested WH probes lacked --help and
ff.py is an import-only library. Help was added without changing their
mathematics; recursive discovery now excludes that one library explicitly.
Final verification: `scripts/session-close.sh` passed every standalone
checker green and every advertised red mode; the final PDF rebuild and
lockstep gate passed, as did source-hash and local-link checks.

Next F1 work should preserve the comparative scope: Tits-lift/Fourier
comparison; nonreference/characteristic-two Heisenberg geometry; geometric
meaning of additive phase kernels; central-graded tensor composition;
finite sectors and transfer maps of Bost–Connes. No universal F1 quantum
theory or preference for one approach was established.

## Where the campaign is

Three workstreams live. All pushed through commit `8f35f28` + this close.

**1. FCR-1 — CLOSED and admitted** (`a9fe59d`). Finite local rings, odd
residue characteristic: data `(R, ψ ∈ Gen(R), β ∈ Adm(ω))`;
`Gen(R) ≠ ∅ ⟺ soc(R)` simple (Frobenius), `Gen(R)` a free `R^×`-set;
`rad(ψ∘ω) = I_ψ ⊕ I_ψ`; simplicity/`M_{|R|}(C)`/SvN; non-free Lagrangians
`soc(R)⊕𝔪`. 37 claim rows (31 PROVED), D1–D16, adjudication in
`theory/verdicts/fcr-local-adjudication.md`. Labbook section 08.

**2. The smallest-rings catalogue — CLOSED** (`8a1adb2`, `eeefbb9`).
The five rings of orders 2,3,4 worked in full (groups `= UT_3(R)`; `D_4`,
`3^{1+2}_+`, three pairwise non-isomorphic order-64 groups; complete irrep
catalogues by central-character strata; Lagrangian censuses 3/4/5/7/7).
Blind-verified; checker `theory/checks/small_rings_catalogue_check.py`
(8 red modes); verdict `theory/verdicts/smallest-rings-verification.md`;
labbook section 09 (46 pp PDF).

**3. FCR-2 — MID-LOOP, prover done, critic NOT yet run.** Its review is the next mainline task after the active user sidequest. State:

- Brief `briefs/fcr2-target.md`; sources registered (Strömberg 1108.0202
  carries Milgram's μ₈ formula verbatim; Ehlen–Skoruppa 1705.04572; the
  ledger's bridge caution: polar form of `ψ∘Q_β` is `ψ∘(2β−ω)`).
- Falsifier PROMOTED and verified: `theory/checks/fcr2_beta_check.py`
  (green 56 s, nine red modes at registered gates). Census (double-blind —
  codex lane + an independent Opus probe agree exactly): at `2 ∈ 𝔪`,
  exactly two `H_β` classes, sizes `|R|³(q∓1)/2q`, keyed by residue-Arf;
  `ε_ψ(β)` is ±1, ψ-independent, class-constant, NON-separating at
  `Z/4, F_2[ε], GR(4,2)`; no antisymmetric cocycle.
- Prover deliverables COMPLETE, force-committed in the lane (NOT trunk,
  NOT reviewed): `theory/lanes/fcr2/prove/{fcr2-beta.md,PATCH.md,SUMMARY.md}`.
  All seven claims at candidate-PROVED per its SUMMARY. Its sharpest
  result REFUTES the census guess about ε-separation: for chain rings ε
  separates the two classes iff the chain length is ODD (even length ⇒
  ε = +1 on both); exact criterion for local Frobenius R:
  separation ⟺ `C_ψ(R) := Σ_{a²=b²=0} ψ(ab) = |𝔪|`
  (non-separation ⟺ `= |R|`). Its stated weakest step: abstract
  non-isomorphism outside the eight registered seeds.
- **NEXT STEP (capped loop, PRD): launch the blind critic** on
  `theory/lanes/fcr2/prove/fcr2-beta.md` + `PATCH.md`. Mirror the FCR-1
  critic work order (`briefs/lanes/fcr1-check.md` era files and
  `theory/lanes/fcr1/critic/WORK-ORDER.md` are the templates; protocol
  `briefs/critic-protocol.md`). The critic may read the promoted checker
  and census SUMMARY but not the prover's SUMMARY. Then one repair wave,
  mechanical adjudication, admission in one lockstep commit (definitions
  D17+, claims rows, labbook section 10, PDF).

## The Atlas sidequest — PRD written, awaiting TJO decisions

`docs/atlas-prd.md` (`8f35f28`): the certified pipeline
"all small commutative rings → Spec data → quantizations → Lagrangians →
QECCs". Scoped by five parallel Opus lanes; written ambition-first (TJO
directive: v0.1 is recon, never a ceiling — see memory note). Banked
during scoping: Nowicki order-32 erratum (`L(2,5)=54`), Gilmer–Mott p³
erratum, the double-blind FCR-2 census, the corrected character-indexed
stratification `#irreps = Σ_χ |I_χ|²` (Ann-form is Frobenius-only —
DERIVED, needs the loop), non-free-only code parameters K∈{2,8} over two
ququart sites, GLP Conj. 5.5's untested non-free sector. Flagship:
`L(2,6)` (order 64, unknown, extends OEIS A127707). **Five NAMED DECISIONS
for TJO in PRD §6** (horizon; Route B alongside A; non-Frobenius policy;
distance budget; Hecke.jl role). Increment ladder AT-0..AT-8; AT-1 is a
single-ring end-to-end thin slice. Do not start Atlas work before TJO
answers §6.

## Standing directives (this session, TJO)

- P1 pipeline (one philosophy, per-increment on merit); Spec framing:
  points = locality, stalks = local physics, "geometrize via Spec" =
  choosing which automorphisms are geometric; queued FCR-5/6.
- L7 amended: cognition/verifier lanes on `codex exec -m gpt-5.6-sol`,
  reasoning xhigh. No Claude subagents for lane work (Opus subagents were
  explicitly authorized for the Atlas scouting only).
- Ambition over tradeoffs: design from the ideal artifact backwards;
  forced tradeoffs are named decisions for TJO (see memory).

## Hygiene landed this session

- Session-close checker discovery now recursive (`275f279`) — the six
  `theory/checks/wh_kappa/` sub-checkers are inside the gate again; 21
  stale CLAIMS paths fixed; refs bodies for 1710.09884/2202.00248
  refetched, SHA256 match the ledger.
- Pre-reboot leftovers (top-level `.beads/`, `runs/`, `report*`,
  `references/`) deleted; unique source bodies parked under
  `v0.1/references/`; working tree clean.

## Next useful steps, in order

1. FCR-2 critic round → repair → adjudication → admission (see above).
   The prover shard is IN THE LANE ONLY; nothing in trunk claims FCR-2
   results yet. Do not let the candidate registers leak into CLAIMS.md
   without the loop.
2. TJO's five Atlas decisions (PRD §6), then AT-0/AT-1.
3. Queued mainline: FCR-3 (collapse), FCR-4 (direct sums + order-4
   battery, route A vs B), FCR-5 (Spec equivalence), FCR-6 (dynamics).
4. Filed residuals: wh-kappa's four SKETCH rows (one hostile round on
   `theory/wh-kappa-choice.md` settles them); its 503-line L2 overrun;
   ring-side frame-preserving torsor (with FCR-6); WH-SYMM ring analogue.
5. Environment notes: `scripts/setup-env.sh` in fresh containers; codex
   config defaults to gpt-5.6-sol/xhigh; network was down at session
   close — if the final `git push` failed, push first.
