<!-- ROLE: live state. UPDATE POLICY: every session end and every phase
     boundary. Not an authoritative source for mathematics — that is
     definitions.md, claims/CLAIMS.md, and theory/. -->

# HANDOFF — live state

Updated: 2026-09-07, F1 sidequest (opened 2026-09-06). The mainline FCR-2 state below remains
the interrupted 2026-09-01 state: prover finished, critic not run. This
session explored the user's new sidequest and did not admit that lane.

Read order gate: `CLAUDE.md` -> **`PRD.md` (constitution; it wins)** -> this.

## F1 sidequest — comparative formulation, qubits and tensor categories

User directives: ground the work in the literature; explore all the relevant
analogies rather than selecting one prematurely; compare the qubit analogue
and tensor product in each; investigate tensor categories as possible primary
quantum objects. Sol subagents permitted, Astra and Claude subagents forbidden.
All four subagents used this session were Sol/xhigh.

Deliverables: `docs/sidequests/f1-qm.md` is the comparative research map;
`briefs/f1-sidequest.md` fixes scope. Labbook section 11, pp. 47–59 in the
59-page PDF, gives the self-contained mathematics and source links. All thirteen
new pages were visually inspected after the final typesetting fixes.
Twenty-four primary PDFs (including a separately identified discovery thesis) are local under `refs/f1/`, with URLs, hashes and
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
the lower numbers for the pending mainline. Current claim counts: 52 total,
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

**3. FCR-2 — MID-LOOP, prover done, critic NOT yet run.** This is the
next agent's first task. State:

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
