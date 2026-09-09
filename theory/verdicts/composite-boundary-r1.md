# Composite relative boundary — single hostile verdict

2026-09-09. **Same-family prover/critic, blind lane.**

Runtime: native inherited Codex runtime; no nested CLI or agent and no model
or reasoning override. The lane was not given a trustworthy precise runtime
model identifier; it does not claim the older repository's named CLI model.
Independent probes used Python 3.12.3 and NumPy 2.4.6. Every arithmetic
comparison in the critic probe is integer, rational, or an exact cyclotomic
coefficient comparison; no floating tolerance is used.

Blindness scope: I read the target brief, protocol, four proposed mathematical
artifacts, relevant current definitions/notation/claims and their local proof
sources, and the verifier executables. I did not read the root conversation,
prover reasoning, target plan, expectations, or future summaries. The root sent
two coordination messages about a notation collision and a checker CLI repair;
neither supplied a proof argument. Same-family and shared-artifact weaknesses
remain. This is one bounded hostile pass, not an adjudication of later repairs.

**Decision: FAIL(CB-C1).** No FATAL. One MAJOR scope defect, two MINOR fixes.
The finite composite quantum milestone survives; the unqualified n=1 spectral
conditioning assertion does not. Nothing here requires endpoint tensor/sum
closure, a conventional C_1, or forgetting all characteristic data.

## Numbered objections

### CB-C1 — MAJOR: moving-sector conditioning is asserted at n=1

**(a) Location.** `docs/research-drafts/composite-boundary/02-boundary-and-spectrum.md`,
section 4, `<1>4.<2>3`, especially “Every denominator is positive”; the governing
assumption is the randomized preparation of D1607, which explicitly permits
n>=1. Also `CLAIMS-PROPOSED.md`, CMP-TRACE's unrestricted moving-sector clause,
and `DEFINITIONS-PROPOSED.md`, D1607's use of C for n>=1 although D1604 introduces
C under n>1.

**(b) Independent counterexample.** Take E=K, hence n=1, in any characteristic.
Every relative orbit has d=1, R=I, and the common algebra is M_1(C). The set
`{e:e divides n,e>1}` is empty. Thus

    sum_(e|1,e>1) phi(e)/e = 0,
    sum_(d|1,d>1) P_d = 0.

The purported conditional block-weight denominator is zero, the moving-sector
success is identically zero at every h, and D1506 gives no conditional state
for that zero profile. FRL-POS itself assumes relative degree at least two and
cannot establish the claimed positivity here. If C is extended by its displayed
label formula, its full randomized success has total weight
`t^(-s)c_1(t^s)=1`, entirely in d=1; this does not produce a rare moving sector.
The checker spectral fibres all have n>1, so their green results do not reach
this endpoint of the asserted quantifier.

**(c) FIX DEMAND.** Add n>1 explicitly to the moving-sector conditional
statement and its proof/claim row, and either define the displayed C for n>=1
or restrict the copied-mixture portion of D1607 to its actual defined domain.

**(d) SURVIVING WEAKER STATEMENT.** The ordinary implementer trace and
determinant formulas hold for every n>=1. The copied-mixture formula also holds
there if C is explicitly extended. Its faithful conditional moving-sector
trace exists for n>1, with the stated weights. CMP-BOUNDARY already assumes
n>1 and is unaffected. The finite positive composite result is not refuted.

### CB-C2 — MINOR: S_n denotes two operators of different dimensions

**(a) Location.** `DEFINITIONS-PROPOSED.md`, D1603, the line
`S_n=direct-sum_(d|n)S_d`, and D1605's parenthetical switch to the single n-cycle;
corresponding uses in `02-boundary-and-spectrum.md`, section 2 `<1>4.<2>3`.

**(b) Independent computation.** For n=2 the all-period abstract implementer
is `1 direct-sum [[0,1],[1,0]]`, a 3-by-3 matrix, while the primitive implementer
is the 2-by-2 flip. D1605's parenthetical makes the intended mathematics
recoverable, but the definition of S_d as the d-cycle conflicts with using
S_n for the larger direct sum at d=n.

**(c) FIX DEMAND.** Name the all-period implementer separately and reserve
S_d for the single d-cycle; carry that convention into the claim/proof prose.

**(d) SURVIVING WEAKER STATEMENT.** Both separately typed operators and all
asserted block actions are correct. This is a notation repair, not a change
to the boundary or spectrum.

### CB-C3 — MINOR: the frozen checker CLI does not expose the integration flags

**(a) Location.** Frozen `check/composite_boundary_check.py`, `main()`,
`parser.add_argument('--red', choices=sorted(MUTATIONS))`.

**(b) Independent recomputation.** I executed all nineteen supported
`--red NAME` invocations on a frozen copy, and every one reached its declared
mathematical gate with exit 1. The parser declaration requires an argument:
a bare `--red` cannot select a mathematical mutant, and no individual
`--red-<name>` switch exists in this frozen version. The root separately
reported that session-close requires those individually discoverable flags.
I did not read or audit the session-close script outside the target scope.

**(c) FIX DEMAND.** Expose each named mutation through the required CLI flags
and make plain `--red` select a real mathematical mutant; mechanically verify
discovery and mathematical exit paths after the reported interface-only repair.

**(d) SURVIVING WEAKER STATEMENT.** The existing explicit `--red NAME` interface
works and every declared mutant is effective. No mathematical gate repair is
required by this finding. My evidence remains tied to the frozen hashes in
`mutation-audit.json`; later CLI changes require the root's mechanical check.

## VERIFIED CORRECT — do not churn in repair

The following results were independently recomputed and analytically attacked.
They are fenced from this repair wave except for the explicit scope/notation
changes above.

1. **CMP-SOURCE.** At a fixed named arithmetic diagram, zero preparation and
Weyl translations yield every computational ket; ket-bra products give each
R_p-valued matrix unit. Finite diagonal graph predicates therefore use actual
source sums. T has coefficients 1/n, so the graph/invariant projectors belong
to the concrete amplitude source even when p divides n. No square root of an
orbit length is required in an ambient projector. Restricting actual matrices
to self-adjoint retracts preserves dagger/composition/tensor, and the retained
Kraus trace inequalities are the usual positive quadratic-form calculation.
At p=2 this remains the declared real arithmetic amplitude fragment; the
complex generated observable algebra does not assert all complex CP maps are
source operations. Uniform rational randomization can also be implemented
without adding sqrt(n) to R_p: repeat the amplitude R^j/n exactly n times for
each j. The summed channel is (1/n)sum_j Ad(R^j).

2. **CMP-REL.** The triples partition by orbit and relative k; supports of
different displayed graph vectors are disjoint. Simultaneous averaging yields
a 1/d all-ones block on each graph support. Direct composition of actual
multiplication, middle Frobenius, and inverse multiplication yields
`(x,y,z)->(x,sigma(y),z-xy+x sigma(y))`. It shifts k on the graph, and all matrix
units follow. An orbit origin never enters the sum, the predicate or the
relative index. Changing enumeration within the sum changes no matrix.
Each d|n occurs by the finite-field fixed-point count and its positive period
polynomial. Separate invariant descent on one fixed orbit produces one
uniform relative vector; joint descent produces d independent vectors.
This is an orbitwise comparison, not a collapse of each whole field algebra.

3. **CMP-BOUNDARY.** Integer matrices verify the complete Kraus identity even
on coherent input columns. In particular K_ok^*K_ok on a primitive orbit is
the invariant rank-one projector, not I/n. Applying it to the specified
period-uniform diagonal reference gives the claimed division by n. The
reference is one copied field state plus two fixed zero ancillas. Its weighted
relative-period mass follows by restricting D_E to the fixed fields of sigma^a
and finite divisor inversion: it is c_d(t^s). Thus success is
`c_n(t^s)/(n t^(sn))`, and its first nonzero coefficient is s phi(n)/n.
Both zero-ancilla maps can be included in the later fixed CP branch when
applying POS-FINITE, so the one-reference theorem applies without pretending
the ancillas are independent POS references. The primitive state on common
observables is exactly |0><0| for every h>0, not merely asymptotically.

4. The full coherent test returns 1 after R, 0 after I, and 1/n after
computational dephasing immediately before R. The last number uses the full
projector Q_(n,1), including invariant averaging; replacing it by the diagonal
graph predicate would erase this coherence distinction. Primitive-cut,
averaging, and final failures remain separate and their probabilities sum to
one. At h=0 the ordinary primitive branch is zero; its nonzero first grade
supports the stated conditional quantum remnant. Characteristic labels and
physical orbit mixtures have not been identified across p.

5. **CMP-NATURAL.** A fixed-K embedding sends every simultaneous tuple orbit
bijectively to one of the same length, and intertwines multiplication and
sigma=x^q. Averaging in a larger extension repeats the same finite orbit;
therefore it gives the same projector on embedded tuples, including tuples
outside the graph. Isometries compose strictly, and their adjoints compose
in reverse order. The decoder identity is J J^*+(I-J J^*)=I after squaring
its actual amplitudes. Sequential first-failure histories are a refinement,
not a binary composite decoder. A period-two component of F4/F2 stays period
two in F16/F2; it is annihilated by the upper period-four primitive cut.
No base-changing naturality has been established or asserted.

6. **CMP-FOURIER.** In the primitive sector n>1, y is nonzero. Keeping y,z
fixed in the first-slot Fourier kernel forces x=z/y, so all compressed
matrix entries except the matching graph entry vanish. The surviving entry
is |E|^(-1/2)psi_E(-x^2), constant under relative Frobenius because absolute
trace is invariant. Orbit multiplicities can have different phases; this
phase operator commutes with the common M_n. Its squared amplitude is I/|E|
on the entire physical primitive code, including multiplicity coherences.
The return probability and ambient complementary outcome are both retained.
There is no claim about arbitrary Fourier slots or full Fourier naturality
of the common boundary.

7. **CMP-TRACE, with CB-C1's n>1 condition.** Each d-cycle contributes d or 0
to Tr(R^j), giving q^gcd(n,j) with its actual c_d(q)/d multiplicity. Diagonalizing
a finite d-cycle gives det(I-zS_d)=1-z^d. The channel acts on pairs of
implementer eigenvectors, so its full linear-map trace is |Tr(R^j)|^2; a
single M_d channel has each d-th root d times. The copied-and-averaged weight
is c_d(t^s)/(d t^(sn)), rather than the ordinary counting trace weight.
Randomizing the relative index gives the normalized trace within each block.
For n>1 its first-grade moving weights are proportional to phi(d)/d.
For n=4 they are 1/2,1/2 on M_2,M_4, distinct from the earlier ordinary
orbit-boundary weights 1/3,2/3. No infinite spectrum is established here.

## Independent finite matrix records

`independent_probe.py` imports no prover/verifier arithmetic or graph code.
It builds polynomial fields with a different tuple ordering, composes three
ambient integer permutations, and computes incidence/Gram/Kraus matrices.
Fourier entries are coefficient counts modulo 1+zeta+...+zeta^(p-1).
It ran red before green. The red changed expected probability data and failed
at the actual full/identity/dephased Born-probability assertion.

| E/K | primitive success at t=p | first coefficient | conditional full / identity / dephased | Fourier return |
|---|---:|---:|---|---:|
| F4/F2 | 1/4 | 1/2 | 1,0,1/2 | 1/4 |
| F9/F3 | 1/3 | 1/2 | 1,0,1/2 | 1/9 |
| F16/F2 | 3/16 | 1/2 | 1,0,1/4 | 1/16 |
| F16/F4 | 3/8 | 1 | 1,0,1/2 | 1/16 |
| F8/F2 | 1/4 | 2/3 | 1,0,1/3 | 1/8 |
| F27/F3 | 8/27 | 2/3 | 1,0,1/3 | 1/27 |

Full implementer traces for j=0,...,n are respectively
`[4,2,4]`, `[9,3,9]`, `[16,2,4,2,16]`, `[16,4,16]`, `[8,2,2,8]`,
and `[27,3,3,27]`. Independent full-channel pair counts give their squares.
The complete rational event histories and phase exponents are retained in
`independent-green.json`, and the failed probability mutation in
`independent-red.txt`. These finite checks do not promote all-prime claims.

## Executable and mutation audit

The direct verifier green and a separate frozen-copy green both passed.
`run_verifier_copies.py` preserves the exact audited source files below this
critic directory and records their SHA-256 hashes in `mutation-audit.json`.
All nineteen advertised mutants exit 1 through MathematicalFailure, not the
parser or interpreter. Every C1--C9 gate is reachable by a mathematical red.

| Gate | mutants reaching it | mathematical failure |
|---|---|---|
| C1 | collective | generated standard block loses rank four |
| C2 | product; diagonal-action | multiplication entry; graph predicate invariance |
| C3 | identity; diagonal-relative; separate-descent | relative shift; loss of independent relative vectors |
| C4 | drop-grade; reset-reference | actual leading coefficient; copied-reference event norm |
| C5 | dephase; normalizer; omit-invariant | full/identity/dephased conditional probabilities |
| C6 | off-diagonal; omit-outcome | coherent Hom rank; complete retained histories |
| C7 | embedding; wrong-sector | actual embedded vector leaves required period code |
| C8 | fourier-phase; fourier-outcome | cyclotomic compression; retained probability completeness |
| C9 | multiplicity; channel-spectrum | full implementer trace; channel root multiplicities |

The identity and simultaneous-Frobenius mutations necessarily agree on the
invariant graph code, but are different ambient operators. Their coincident
restriction is the mathematical distinction under test, not two unrelated
unconditional failure switches. Other mutations change different amplitudes,
reference data, outcomes, or effects. The positive-sign Fourier mutant passes
characteristic two and then fails at the odd-characteristic compression gate;
it is not accidentally killed by an earlier binary test.

Symbolic gate audit: the C2 multiplication-entry equality is a direct check
against the defining field-table formula, so it is not by itself evidence for
the boundary witness. The substantive independent checks are the composed
relative permutation, graph shift, prepared Born probabilities, and histories.
C3 uses actual projection/action against separately indexed matrix units; C4
compares label weights against divisor polynomials; C5 compares actual Born
values against declared outcomes; C7 compares actual embeddings/trace fibres;
C8 compares an expanded Fourier vector against its compression formula; C9
compares actual permutation traces and Newton recurrence against cycle factors.
No whole advertised gate is an unfalsifiable `0==0` check. The control C1 is
previously admitted composition evidence, not the new Frobenius result.

Two additional hostile DATA mutations on separate copies, outside the declared
red switches, changed (i) the expected dephased probability from 1/n to 1/(n+1),
and (ii) the expected Fourier phase sign while leaving the executed kernel
unchanged. They failed at C5 and C8 respectively. Full exit paths and reached
check counts are in `mutation-audit.json` and individual captured JSON files.

## Status register, reliance and admission scope

All six candidate rows say SKETCH pending capped review, and both shards say
UNREVIEWED. That is honest. Their dependencies FRP-CAT/CP/DESCENT,
FRB-FROB/TRACE/TRANSFER/NATURAL, FRL-ORBIT/POS, and POS-STATE/DIAGRAM/FINITE
are current PROVED rows. I found no reliance on a REFUTED row, v0.1 content,
or an unregistered external theorem. The new finite calculations are internal
derivations using the current local sources, including the positive-reference
and orbit-boundary proofs.

The proposal and derivation agree in strength except for CB-C1 and the explicit
S_n overloading. Authoritative registries/labbook admission were outside this
lane's allowed target artifacts; this verdict does not certify their later
lockstep integration. The mathematical surviving statement is sufficient for
the agreed finite milestone after the indicated scope repair: an assembled,
positive, origin-free conditional M_n remnant with actual arithmetic Frobenius
and a coherence-sensitive test. It proves neither all-arithmetic forgetting
nor a functor defined by leading conditioning under unrestricted future maps.
Full physical profiles remain required for further continuations.

FAIL(CB-C1)
