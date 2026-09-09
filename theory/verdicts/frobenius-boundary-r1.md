# Frobenius orbit boundary — hostile verdict

Date: 2026-09-09. **Same-family prover/critic, blind lane.**

Critic execution: inherited native Codex runtime. The exact backend model ID
and a separate reasoning-level override are not exposed to this lane, so none
is asserted. The artifacts identify their author as root Codex runtime. No
cross-family independence is claimed; no nested CLI or subagents were used.
The critic read the artifacts and single sources, not the prover's reasoning.

Scope: admission of `FRL-ORBIT`, `FRL-POS`, `FRL-COMP`, `FRL-ACTIVE` against
D1331--D1334. This is one bounded hostile pass. No earlier verdict specifically
on these two orbit shards was located. Older Frobenius results were consulted
only as admitted dependencies, not reopened. All writes are in this lane.

## Decision

The mathematical arguments survive at their explicitly stated finite-field
scope. **FRL-COMP has one MAJOR checker defect requiring repair before
admission.** The other three rows have no open FATAL or MAJOR from this pass.
There is one MINOR Fourier-definition mismatch in the labbook. No theorem
counterexample was found. The existing SKETCH labels are honest.

## Numbered objections

### O1 — MAJOR: the advertised B4 quantum-coherence acceptance gate is a no-op

**(a) Exact location.**
`theory/checks/frobenius_boundary_check.py`, `b4`, lines 171--177, particularly
`out = dephased if args.red_coherence else rho` and the next assertion.
The mathematical witness is `orbit-composition.md`, Section 2,
`<1>4.<2>1`--`<2>2`, lines 110--120. The checker claim is
`frobenius_boundary_EXPECTATIONS.md`, B4, lines 20--24, and the B4 evidence
pointer in `claims/CLAIMS.md`, `FRL-COMP`, line 195.

**(b) Independent computation and mutation.**
In green mode the acceptance expression simplifies literally to
`np.array_equal(rho, rho)`. No reblocking matrix or channel is applied. The
following dephased-return check computes a meaningful number, but does not
validate a coherent output or the purity of its input.

Set `v=(1,1,0,0)` and change only the submitted state data from
`rho=np.outer(v,v)` to `rho=np.diag(v*v)` in a lane copy. The whole checker
still exits **0** through B1--B6. Worse, the same copy with
`--red-coherence` also exits **0**: its already diagonal `rho` equals
`dephased`, so the nominal red ceases to be red. This is a change to the
ground-truth state, not to the assertion or its expected answer.

The correct unnormalized pure state has
`v.T rho v/4=1`; the mutated state has `v.T rho v/4=1/2`. Both have
`v.T dephased v/4=1/2`, explaining why the second submitted check misses
the mutation. The first is exactly the acceptance test that should reject it.

An independent probe constructs the actual permutation matrix B by following
the pair cycles, computes `B*(B^* rho B)*B^*`, and tests its return
probability. It also transports every matrix unit for d,e=1..6. Green passes.
Deleting the cross-multiplicity entries between the two B transports exits
nonzero at `ACTUAL_REBLOCK_COHERENCE`, with observed probability 1/2 instead
of 1. Thus the positive theorem is correct, but the submitted coherence
evidence is not the claimed channel test.

**(c) FIX DEMAND.** Apply the actual B matrix to the state/matrix units, mutate
the multiplicity-coordinate channel, and compare the transported result to an
independent fixed Born expectation; ensure the diagonal-input data mutation
also fails, then rerun green and all named reds.

**(d) SURVIVING WEAKER STATEMENT.** The exact CRT bijection, intertwining,
quantum matrix-algebra identity, and written 1 versus 1/2 coherence witness
survive. The current submitted B4 certifies its combinatorial tests and the
dephased scalar, but does not certify preservation of coherence by a computed
reblocking channel. FRL-COMP's mathematical scope need not be weakened; its
admission evidence needs this local repair.

### O2 — MINOR: the labbook silently specializes the named Fourier root

**(a) Exact location.**
`labbook/sections/sidequest_frobenius_boundary.tex`, definition of
Multiplication cuts and Fourier-transported sectors, line 265, uses
`exp(-2*pi*i*Tr(xy)/p)`. D1301 and D1306 instead retain an arbitrary named
primitive root `zeta_p` and use `psi_E(-xy)=zeta_p^(-Tr(xy))`. D1334 refers
to that F_E. The corresponding argument is `orbit-composition.md`, Section 5,
`<1>3`, lines 243--250, which correctly invokes D1306.

**(b) Independent computation.**
Let p=3, E=F9, write `omega=exp(2*pi*i/3)`, and take the allowed named root
`zeta_3=omega^2`. Since `Tr_(F9/F3)(1)=2`, the x=y=1 entry prescribed by
D1306 is `omega^2/3`; the labbook's entry is `omega/3`. They are distinct.
This does not change any squared Fourier-entry modulus or the asserted
overlap. It is an explicit special-root formula that fails to restate the
retained phase datum, rather than an unnamed choice needed by the theorem.

**(c) FIX DEMAND.** Restate the labbook Fourier kernel as
`zeta_p^{-Tr_(E/F_p)(xy)}` or `psi_E(-xy)`, referring to the already named
phase datum.

**(d) SURVIVING WEAKER STATEMENT.** The displayed exponential formula is
correct when the named root is the standard `exp(2*pi*i/p)`; the stated
Fourier overlap and all four FRL scalar/operator claims remain true for
every allowed named primitive root.

## VERIFIED CORRECT — fenced against unnecessary repair

```text
V1. ALL p AND r: absolute-Frobenius orbit count and representation.
For each d|r, X^(p^d)-X divides X^(p^r)-X and has derivative -1,
including p=2. Its roots in E number p^d. Recursive subtraction over
proper divisors gives A_d=p^d-sum_(e|d,e<d) A_e, hence the displayed
Moebius polynomial. An orbit contributes one copy of C^d, so the same
a_d repeats A_d/d times. Its trace contribution is (A_d/d)Tr(a_d).
This establishes the represented normalized trace, not only a word census.

Independent quotient-field census (a separate generic polynomial engine):
 F4 : {1:2, 2:2};       F8 : {1:2, 3:6};
 F16: {1:2, 2:2, 4:12}; F9 : {1:3, 2:6};
 F27: {1:3, 3:24};      F81: {1:3, 2:6, 4:72};
 F25: {1:5, 2:20}.
Each quotient model was checked to have inverses by a^(Q-1)=1 for all
nonzero a. The census was compared to recursive fixed-count inversion,
not to a copied implementation of mu. Fixed powers, represented traces,
and conjugation under a change of exactly one orbit origin all passed.

V2. ALL REAL t>1: positivity, normalization, and the conditional endpoint.
For d>1, write t=exp(h). The kth coefficient of c_d(exp(h)), k>=1,
is sum_(e|d) mu(d/e)e^k=d^k product_(ell|d)(1-ell^(-k))>0.
There are finitely many exponential summands, so their series can be
combined absolutely. The first coefficient is phi(d), by excluding
multiples of each prime divisor. For example d=6 gives c_6=t^6-t^3-t^2+t,
first derivative 2 and second logarithmic derivative 24.
Divisor inversion gives sum_(d|r)c_d=t^r, hence all conditional weights
are positive and sum to one. Cancellation of the simple t-1 factors gives
phi(d)/(r-1) uniformly for any fixed integer r>=2. At r=6 the d=2,3,6
weights are 1/5,2/5,2/5. No finite sample is used to prove all-real positivity.

V3. MOMENTS AND PHYSICS.
Tr(S_d^k)/d is the indicator of d|k, also for k=0 and negative k.
Summing divisor weights yields both displayed gcd formulas. A rank-one
state/effect E00 in any d>1 block has probabilities 1 and 0 before/after
the forward shift, and does not commute with that shift. On d=r the
coordinate projections have r distinct iterates, proving exact order r
of both the unitary and its conjugation channel. The unconditioned
t=1 null ideal is precisely all d>1 blocks. The active projection removes
fixed labels, while a uniform superposition on each moving orbit remains
Frobenius-invariant. These two notions were not confused.

V4. CP CATEGORY AND COHERENCE.
Composition and tensor of CPTP maps preserve complete positivity and
ordinary sum-of-blocks trace. Word/tag reassociation and symmetry are
actual coordinate permutations. Equality is equality of maps, not a
projective quotient. Reference states are specified on words and tensor
as normalized densities; no default probability distribution on tags is
needed or silently supplied. Pointwise continuous CPTP families form the
stated section category, with evaluation preserving tensor and composition.
Finite branch probabilities are continuous; division requires positive
limiting event probability, exactly as stated.

The pair permutation has invariant j-i mod g. Choosing its residue a,
then solving k=i mod d, k=j-a mod e, gives exactly one k mod l. Hence
B is unitary, transports shifts, and identifies full M_de with M_gl.
The multiplicity is quantum. Actual matrix-unit transport independently
passed for d,e=1..6, and the two-cycle coherent/dephased return values
were recomputed as 1 and 1/2.

For the triple d=e=h=2 the left map sends (a,b,k) to
(k,a+k,b+k), whereas the right sends it to (k,a+k,a+b+k), modulo 2.
Thus literal internal labels disagree. The connector sends left labels
(a,b,k) to right labels (a,b-a,k). This agrees through the common ordered
Cartesian basis. General connectors T_c^* T_b telescope, so their
pentagon and transported action identities hold for arbitrary arities.

V5. UNIFORM STANDARD-SUBFIELD INCLUSION.
In F_(p^s), a full orbit lies in F_(p^r) iff d|r. Its multiplicity
c_d(p)/d is independent of the ambient degree. Thus a model density rho_d
is represented physically by rho_d/(c_d(p)/d) on every such orbit,
with unchanged ordinary trace and observable pairing. Zero-block encoding
and the retained physical decoder agree on these states, not on an
unstated extension to all physical CP operations.
This also checks directly for F4 inside F16 and F9 inside F81, using
the fixed points of sigma^2 in the larger quotient-field model.

The projections e_(r,s) select entire central blocks. Therefore the two
decoder outputs sum to the original trace, even on general block
off-diagonal matrix units. Tower success restrictions are intersections
of divisor sets; encodings compose by insertion. Product decoders have
four independently retained tags. Sum of success weights is h_(r,s);
normalizing yields sigma_(r,t). The h products cancel along every r|s|v,
and their endpoint values are (r-1)/(s-1), with no bound on r,s,v.

V6. ALL FINITE FIELDS AND ALL ARITIES.
There are (Q-1)^d Q active basis labels for multiplication, all translated
without a fixed target. The remaining labels are fixed. The permutation
trace is thus 1-((Q-1)/Q)^d. Every moved basis column has squared
displacement 2; this independently gives the whole and conditional L2
formulas. The gate keeps controls fixed, so the corner is reducing and
the restricted operator is unitary. Field embeddings preserve zero and
nonzero labels, and preserve products and sums, proving the inclusion
square without a characteristic or arity restriction.
Independent finite permutation-column computations for Q=2,3,4,9 and
d=1,2,3 checked the traces, squared norms, cuts and Frobenius square.
The written field-axiom proof, not those examples, delivers all Q,d.

Coordinate indicator multiplication gives P_A P_B=P_(A union B); labels
are counted once. For Q=t^r the leading term is r^|A union B| times
(t-1)^|A union B|. Independent moving-word weights have leading coefficient
product(r_j-1) and order n, including the empty product/order zero.
The F4 multiplication and trace-fibre counterexamples are correct.
For any permitted Fourier character, all entries have modulus 1/sqrt(Q);
an m-label cut therefore has overlap m^2/Q^2. Taking m=p^r-p yields
w_r(p)^2. This is an overlap of projections, not a claim about intersection.
```

## Checker execution, symbolic audit, and reachability

The submitted checker was run unchanged with `python3`, green and every
advertised red. It uses integers, Fractions and integer object matrices;
no tolerance-dependent conclusion is involved.

| Mode | Exit | First failing gate; preceding gates reached |
|---|---:|---|
| green | 0 | B1--B6 all pass |
| `--red-count` | 1 | B1 exact-period count at (p,r,d)=(2,2,2) |
| `--red-weight` | 1 | B2 positive normalized weight at r=2,t=1, weight 2; B1 passes |
| `--red-frobenius` | 1 | B3 Born distinction; B1--B2 pass |
| `--red-coherence` | 1 | B4 coherent-reblocking equality; B1--B3 pass |
| `--red-decoder` | 1 | B5 decoder Kraus completeness; B1--B4 pass |
| `--red-overlap` | 1 | B6 overlap uses union; B1--B5 pass |

The six mutations are distinct: polynomial count, endpoint weight, shift,
dephasing, retained failure Kraus operator, and overlap exponent. No entire
B1--B6 group is unreachable. However, a first failure does not imply that
every subsequent assertion in its group has been tested by that red.

| Gate group | Symbolic content and reachability limits |
|---|---|
| B1 | Enumerated periods/fixed powers versus divisor formulas; quotient-field inverses and periods. Nontrivial comparisons. `--red-count` dies in the word census before the concrete-field assertions. Independent bad-modulus mutation reaches and kills `field inverse`. |
| B2 | Jordan product versus divisor derivative; endpoint/positive weights; moment divisor sum versus gcd expression. Nontrivial evaluations of the written identities. `--red-weight` first dies at normalization, so its red does not separately certify the later moment assertion. All-real positivity remains a written proof. |
| B3 | `Tr(E00^2)=1` is a fixed state convention; `Tr(E00 U E00 U*)=0` depends on U and kills the red. The later commutator and U^d=I assertions are not separately reached by the named red. U^d=I tests divisibility of order, while exact order is delivered by the written rank-one orbit argument. |
| B4 | CRT bijection and shift/triple transport genuinely inspect computed maps. The nominal red is injected only after those tests. The coherent acceptance simplifies to rho=rho in green: O1. The later dephasing scalar is a real calculation, but survives a wrong input state. The submitted finite triple test transports to the same Cartesian set/action; the general pentagon is the separate telescoping proof. |
| B5 | The scalar ratio tower product cancels algebraically and alone is no independent tower test. Independent divisor sums and actual insertion matrices/matrix-unit channels provide the substantive checks. `--red-decoder` first dies before reconstruction and before the separately constructed tensor branches. The independent dropped-tensor-branch mutation reaches the four-branch matrix-unit acceptance test. |
| B6 | Enumerated control/target counts versus closed formulas, union indicator counts, and exact F4 Fourier entries/overlap are substantive. `--red-overlap` dies before the subsequent mixed-scope sentinels. The independent wrong-cut mutation reaches and kills the final Fourier overlap test. The hardcoded V column is a small witness calculation, not a general transfer-construction test. |

Unreached later assertions above are not presented as independently protected
by the original named reds. They need not be turned into a new exhaustive
mutation project: the local B4 acceptance defect is the repair required here.
Other written universal arguments and substantive matrix-unit checks survive.

Independent runs are reproducible with:

`python3 theory/lanes/arithmetic-limits/orbit-critic/independent_probe.py`

The probe imports no submitted checker helper. It creates only lane copies.

| Independent mutation | Exit | Actual path |
|---|---:|---|
| B4 input `rho=diag(v*v)` | 0 | Entire submitted green escapes: O1 |
| Same data copy, `--red-coherence` | 0 | Entire nominal red escapes: O1 |
| F4 modulus x^2+x+1 replaced by x^2+1 | 1 | B1 `field inverse` |
| Zero actual `(success,failure)` tensor branch Kraus matrix | 1 | B5 `four-branch tensor matrix-unit channel`, after scalar and single-decoder gates |
| Change Fourier cut from rank 2 to rank 3 | 1 | B6 `F4 Fourier active overlap`, after previous gates |
| Dephase independently computed multiplicity-coordinate state | 1 | Independent `ACTUAL_REBLOCK_COHERENCE`, probability 1/2 instead of 1 |

## Quantifiers, choices, comparison, and reliance

- **FRL-ORBIT:** every prime p and every finite extension degree r>=1.
  The argument uses absolute p-Frobenius. Actual field tests include odd
  characteristic nonprime fields independently; they support, but do not
  replace, the uniform polynomial argument. The r=1 scalar case is valid.
- **FRL-POS:** every fixed r>=2 and every real t>=1. The proof establishes
  the full real interval by a convergent series. It does not claim uniform
  analytic bounds as r tends to infinity, or a prime sequence tending to one.
- **FRL-COMP:** finite words/tagged families, all complex CPTP maps on the
  specified fixed block algebras, and continuous pointwise CPTP families.
  Arithmetic comparison has coherent origins in standard subfields of one
  finite ambient field, uniformly for every r|s and tower. This is not a
  construction on arbitrary named embeddings, arbitrary Galois closures,
  infinite fields, or all arithmetic gates. The user's desired broader
  extension theory is a new target, not a defect in these explicit bounds.
- **FRL-ACTIVE:** every finite field Q=p^f, every d>=1, separate control and
  target registers, and the stated ordinary trace. The homogeneous-word
  overlap formula uses the common Q of the section's standing assumption.
  No replacement by arbitrary unequal register fields is implied.

The required choices are exposed: the field register and its computational
labels, named primitive root for Fourier, an origin in every Frobenius orbit,
standard subfield inclusion, ordered tensor factors, actual CRT residue
representatives, and external outcome tags. There is no basis/ordering of the
set of equal-length orbits required to define repeated block action. Origin
change is only orbitwise unitary comparison, and may change the physical
embedded subalgebra. Category morphisms are explicitly CPTP maps; its
evaluation is an actual functor. Frobenius is a distinguished channel, not
an asserted natural transformation commuting with every CPTP map. No hidden
choice or unjustified canonicity theorem was found. O2 is the one restatement
of a named choice that requires correction.

`FRB-TRACE`, `FRB-FROB`, `FRB-TRANSFER`, `FRB-NATURAL`, and
`FRB-HIERARCHY` are PROVED in the register. No step of the target relies on a
REFUTED row or on v0.1 content. Hyde and Yoshida are registered in
`refs/LEDGER.md`; their local introduction and printed p.127, Section 2.2,
respectively contain the claimed comparison formulas. The positive trace,
matrix representation, and quantum coherence results are correctly identified
as local derivations rather than attributed to those sources.

## Lockstep and status register check

All four claim rows, both shard status paragraphs, and all four labbook
propositions say SKETCH/pending review. Their scopes agree about the marked
observable family, fixed-label removal, lack of a full arithmetic realization,
standard-inclusion restriction, retained histories, and distinction between
active counts and arbitrary Clifford levels. D1331--D1334 are definitions,
not circular assertions that the desired theorems hold. The nearest admitted
arithmetic FRB/FRP rows are PROVED with explicit data and scope; the new rows
do not borrow that status. O1 is a mismatch between advertised and actual
checker evidence; O2 is a local definition-restatement mismatch.

After the single repair wave, the orchestrator can mechanically verify O1's
actual-channel and changed-data failures and O2's kernel spelling. A new
hostile round is unnecessary. This pass supports admission of FRL-ORBIT,
FRL-POS, and FRL-ACTIVE at their existing scope; FRL-COMP requires O1 closed.

FAIL(O1)
