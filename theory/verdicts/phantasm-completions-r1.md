# Blind hostile verdict — SP-FOCK, SP-PRIME, SP-BC-CONTROL

Date: 2026-09-10. Critic model: `gpt-5.6-sol`, reasoning `xhigh`.
This was the sole same-family prover/critic pass under a literal blind lane. I
did not read completion prover/checker lane contents, notes, patches,
summaries, source-reuse records, root result notes, or hidden reasoning.

Frozen targets checked:

- `fock.md`: `10b05e43ba54e12ca7d4c6c9bb2551976d5ddb040b075cdda7312fb04318358e`;
- `prime-tensor.md`: `45eda8795015d244722b8543e8d798aaad4dd66859a440f8dcafd5636c495ad7`;
- `bc-control.md`: `629d0900be215a7b61128bb456804a6a5564397931cdeac46b77c94004d85210`;
- checker: `de4ed53d12be8e8a7414b28aec57ce0bad8b617f804e57deec418c6baefceaa8`;
- expectations: `a4fe32ea5d163d1430961f05ac4d8f8281573954ee6c7fa6381dbf91b953cf0b`.

## Separate dispositions

| claim | disposition | proof repair needed |
|---|---|---|
| SP-FOCK | PASS | none |
| SP-PRIME | PASS | none |
| SP-BC-CONTROL | PASS | none |

## Numbered objections

### 1. MINOR — F3 reports `2I` sector norms without applying `2I`

**(a) Location.** `theory/checks/phantasm_completions_check.py`, F3,
`tensor_power` and `gate_f3`, lines 257--282, especially the constructed tuple
at lines 280--281; compare EXPECTATIONS F3 and
`claims/PHANTASM-DAG.md:342`.

**(b) Independent computation.** The contraction composition checks apply
`tensor_power` only to `a=diag(1,1/2)`, the swap, and their composite. The
advertised expansive norms are then assigned as `tuple(2**r)` and compared
with the literal `(1,2,4,8,16)`. On a temporary copy I replaced the entire
`tensor_power(a,r)` implementation by the identity matrix of the right size.
The complete checker still exited 0 and still printed the `2I` norm claim.

**FIX DEMAND.** Apply the actual tensor power of `2I` to a normalized symmetric
test vector (or compute its restricted Gram action) and add a tensor-collapse
red whose first failure is F3.

**SURVIVING WEAKER STATEMENT.** The frozen checker genuinely tests finite
sector preservation/composition for its two contraction fixtures; the written
proof independently establishes the unbounded `||T||>1` conclusion.

### 2. MINOR — B1 never checks `mu_n^*` on a nonmultiple

**(a) Location.** `theory/checks/phantasm_completions_check.py`, B1,
`mu_star` and `gate_b1`, lines 462--486, especially lines 479--485; compare
EXPECTATIONS B1.

**(b) Independent computation.** B1 checks `mu_n^*(mu_n(k))=k`, but its
nonmultiple expectation is compared only with the separate `q_action`; it
never asserts `mu_star(n,k) is None` when `n` does not divide k. On a temporary
copy I made `mu_star(5,k)` return floor division on nonmultiples. The complete
checker exited 0, including B1's advertised “adjoint laws” report. A broader
floor-division mutation happened to fail later at B3, not at B1.

**FIX DEMAND.** Compare `mu_star(n,k)` directly with the divisible/nondivisible
oracle for all B1 samples and add an adjoint-divisibility red targeted to B1.

**SURVIVING WEAKER STATEMENT.** B1 correctly tests the semigroup law,
left-inverse law on the range, and proper range projections; the written BC
proof derives the full adjoint formula from basis inner products.

### 3. NOTE — the main labbook still calls the installed controls “in preparation”

**(a) Location.** `labbook/sections/symplectic_phantasm.tex:87`, versus the
implemented falsifier entries at `claims/PHANTASM-DAG.md:342,446,472` and the
three integrated contract provenances.

**(b) Independent computation.** The frozen checker exists, all nine gates
run green, and all thirteen advertised reds reach their intended gates. The
main overview provenance still says “Finite controls in preparation.” All
claim statuses remain honestly SKETCH, so this is stale evidence wording
rather than a mathematical or status defect.

**FIX DEMAND.** Change the overview evidence phrase to “Exact finite/symbolic
controls; review pending” during the repair wave.

**SURVIVING WEAKER STATEMENT.** The labbook statements, scopes, proofs, and
SKETCH statuses otherwise agree with CLAIMS and the DAG.

## Independently verified correct

<!-- VERIFIED-CORRECT-BEGIN -->

### SP-FOCK

- `fock.md` section 1 `<1>1`--`<1>14` correctly proves that the permutation
  average is the symmetric-sector projection, contractions give a bounded
  norm-one direct-sum operator because of the vacuum, identities/composition
  hold sectorwise, and every bounded map of norm greater than one has
  unbounded sector norms.
- Section 2's shuffle-coset calculation gives exactly
  `n!m!/(n+m)!`; distinct occupation patterns are orthogonal even for
  arbitrary Hilbert spaces. Sections 3--4 correctly extend the algebraic
  isometry onto the Hilbert completions and prove two-variable naturality for
  contractions. No unproved strong-monoidal coherence adjective is added.
- Section 5 correctly separates the zero Hilbert space from the vacuum
  sector, identifies the normalized D1010 basis with the one-mode sectors,
  and transports the exact weighted domain and eigenvalues of particle number.

### SP-PRIME

- `prime-tensor.md` section 1 proves the increasing-slot maps are injective
  isometric unital star-homomorphisms and verifies all embedding triangles,
  including the empty scalar stage.
- Section 2 constructs a well-defined normed algebraic direct limit. The
  finite-stage C-star identity, continuous product/star, and common unit pass
  to its completion.
- Section 3 proves finite product-state positivity, norm one, compatibility,
  and unique continuous positive extension. No infinite product-state theorem
  is silently imported from the finite source locator.
- Section 4 correctly proves Cauchy--Schwarz, the left-ideal property of the
  GNS null space, bounded left multiplication, star representation, cyclicity,
  and the double commutant. The explicit pure local state gives a cyclic but
  nonseparating vector without asserting state or representation nonfaithfulness.

### SP-BC-CONTROL

- `bc-control.md` sections 1--2 derive the semigroup, adjoint, phase and root-
  average identities on the infinite basis without finite-shift truncation.
- Section 3 proves `nu_n` is a star-isomorphism onto the `q_n` corner and
  `L_n` is an algebra-preserving unital CP compression. It correctly refuses
  multiplicativity of `L_n`.
- Section 4 computes the adjoint domain of the diagonal logarithmic operator;
  equality of maximal domains proves self-adjointness.
- Section 5 first proves generator invariance, then extends isometrically to
  the represented C-star algebra and uses a uniform approximation estimate
  for point-norm continuity.
- Section 6 uses the integral test to prove trace-class convergence for every
  real `b>1`, identifies the diagonal trace with the prescribed zeta series,
  and normalizes the positive density. Nothing is inferred at `b=1` or about
  zeta zeros.

### Sources, choices, and lockstep

- The proofs use SP-DER06 only for the registered Fock comparison, SP-WAT18
  only for finite product states, SP-CM08 only at its norm/GNS and represented
  BC scope, and SP-CM04/CM08 for the displayed BC formulas. No separating,
  factor, KMS, universal-faithfulness, or spectral conclusion is imported.
- All choices are explicit: contractions and positive factorial square roots;
  local dimensions/densities and increasing prime order; the represented BC
  root-of-unity embedding, logarithmic energy, and real `b>1`.
- Apart from objection 3's evidence phrase, definitions, notation, CLAIMS,
  DAG, proof shards, and integrated labbook agree in statement and Scope.

<!-- VERIFIED-CORRECT-END -->

## Quantifier and status register

SP-FOCK covers arbitrary complex Hilbert spaces and contractions, not only
finite dimensions. SP-PRIME covers every stipulated positive trace-one local
density, including rank-deficient choices, and all finite prime stages before
completion. SP-BC-CONTROL acts on the actual infinite `l2(N_>0)` representation
for every integer n and every real `b>1`. The p=2/p=3 finite controls test
dimensions/primes/shifts two and three but carry none of these infinite
quantifiers.

All three proof headers, CLAIMS rows, DAG entries, and propositions remain
SKETCH/draft pending review. This is honest relative to admitted neighboring
claims. This verdict performs no promotion.

PASS
