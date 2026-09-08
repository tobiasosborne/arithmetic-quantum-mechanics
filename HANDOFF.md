<!-- ROLE: live state. UPDATE POLICY: every session end and every phase
     boundary. Not an authoritative source for mathematics — that is
     definitions.md, claims/CLAIMS.md, and theory/. -->

# HANDOFF — live state

Updated: 2026-09-08, field-extension and Frobenius research handoff. The
user's latest direction is recorded immediately below and takes priority
over the older next-step lists. This turn records the discussion only;
no new proof campaign or claim promotion is running. The mainline FCR-2
state remains the interrupted 2026-09-01 state.

Read order gate: `CLAUDE.md` -> **`PRD.md` (constitution; it wins)** -> this.

## Latest steering — field extensions, Frobenius and operational descent

The user wants to study the category of arithmetic quantum systems over a
fixed prime p, regard one F_(p^r) Weyl system as a composite of r atomic
p-systems, understand quantum maps to smaller fields, and determine whether
field extensions/Frobenius survive the flag construction and its p→1
specialization as a natural noncommutative Frobenius structure. They approved
the following analysis and asked that it be preserved for the next agent.

**Evidence/status boundary:** the formulas and examples below were derived
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

The two new arXiv papers were read from PDFs, with temporary extracts at
`/tmp/aqm-field-extension-reading/{shintani,vourdas}.{pdf,txt}`. These paths
are not durable source registration. Fetch into refs/, verify title/hash
and register precise locators before a formal admission relying on them.

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
