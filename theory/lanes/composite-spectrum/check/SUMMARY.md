# Independent finite verification of the proposed spectral completion

2026-09-09. New artifact; not a re-review of the earlier finite construction.
Verifier lane only, with parent-inherited Codex configuration. No
cross-family independence is asserted. The checker was implemented
independently from the new proof and imports no repository helper or prior
checker. All writes are inside this lane; the earlier checker remains frozen.

## Executable and frozen result

Promotable standalone entry point:

```sh
python3 theory/lanes/composite-spectrum/check/composite_spectrum_check.py
python3 theory/lanes/composite-spectrum/check/composite_spectrum_check.py --red-drop-divisor-weight
python3 theory/lanes/composite-spectrum/check/composite_spectrum_check.py --red
python3 theory/lanes/composite-spectrum/check/freeze_results.py
```

The checker uses Python's standard library only. All calculations are exact
integer or rational operations; no floating-point tolerance is used.
Its SHA256 is
`44b68befc4627f7bbd62e17d75e25837e2dfbc30b16dbe83758e7b2d2a3b926c`.

**Green: 41,216 exact comparisons passed across S1--S7.**
All **15 advertised red flags** returned exit 1 with a JSON mathematical
failure at the registered gate: 14 named modes plus the plain alias.
No parser/interpreter failure was counted as a mathematical red.
The `identity` and `central-dynamics` modes share the same identity-action
replacement, representing the two stated interpretation errors.

`freeze_results.py` discovers flags using the actual session-close pattern
`--red[A-Za-z0-9_-]*`, invokes each without additional arguments, requires
its named gate, and runs green last. Plain `--red` aliases the real
`drop-divisor-weight` mutation; `--red NAME` also remains supported.
Actual stdout, help output and source/output hashes are in `results/`.
The manifest is `results/manifest.json`. Green output SHA256 is
`bb1b996d64edebe6d685d9ea152b6b83e82553af5ceab39c45e66feab51f19cf`.

`EXPECTATIONS.md` was written before implementation. The first executable
test was a real F4 copied-graph averaging red that rejects the missing 1/d
factor at S2. That first output and source hash are separately frozen in
`results/preregistered-first-red.json`.

## Finite findings

No counterexample was found within the declared finite scope.
The copied-reference grade calculation uses actual binary field labels,
their actual Frobenius orbits, and rational simultaneous averages of
three-register multiplication-graph tuples. The absolute-period reference
derivative is obtained from recursively constructed point-count
polynomials; its comparison totient is independently counted by listing
the integers coprime to d. No symbolic totient formula is used.

| N | Actual field size | Derived moving weights phi(d)/d | theta_N(1) |
|---|---|---|---|
| 2 | 4 | d=2: 1/2 | 1/2 |
| 3 | 8 | d=3: 2/3 | 2/3 |
| 4 | 16 | d=2: 1/2; d=4: 1/2 | 1 |
| 6 | 64 | d=2: 1/2; d=3: 2/3; d=6: 1/3 | 3/2 |
| 12 | 4096 | d=2: 1/2; d=3: 2/3; d=4: 1/2; d=6: 1/3; d=12: 1/3 | 7/3 |

The separate non-prime-base F16/F4 calculation gives raw moving grade one
equal to 1; division by base degree s=2 gives phi(2)/2=1/2, as required.

The finite corner restrictions preserve the unnormalized weights. Their
normalized-state decoding probabilities are exactly theta_N(1)/theta_M(1).
Examples: N=2→4 gives 1/2, N=2→12 gives 3/14, N=4→12 gives 3/7, and
N=6→12 gives 9/14. Normalizing these restrictions prematurely is rejected.

All seven strict divisible degree pairs among 2,3,4,6,12 execute actual
field embeddings. All 22 polynomial-generator root choices are checked,
including both F4→F16 embeddings, and all 38 possible strict three-level
embedding paths compose to an enumerated direct map. For each embedding,
the entire upper label set of period dividing N is exactly its image;
each upper length-d graph orbit for d|N is therefore checked against the
whole lower graph code, not merely one selected primitive vector.

Finite cutoffs D=2,4,8,16,32 and beta=2,3,4 execute strictly positive
ordinary densities, exact normalization, invariance, noncommuting
amplitude-square expectations, and 3-by-3 state Gram matrices. At D=4:

| beta | Exact Z_D(beta) |
|---|---|
| 2 | 199/864 |
| 3 | 985/10368 |
| 4 | 5155/124416 |

For D=4, beta=2, the regulated implementer moments are:

| j | 0 | ±1 | ±2 | ±3 | ±4 | ±6 | ±12 |
|---|---|---|---|---|---|---|---|
| moment | 1 | 0 | 108/199 | 64/199 | 135/199 | 172/199 | 1 |

They are computed using explicit positive and negative powers of the
implementing cyclic permutations. Separately, the conjugation action
permutes matrix units. At j=0 its linear-map trace is 29 for D=4,
whereas the normalized implementer expectation is 1. The largest tested
cutoff D=32 has 527 Hilbert basis states and 11,439 block-algebra matrix
units. This distinguishes the two trace types without relying on symbols.

Literal coprime counts verify every Dirichlet coefficient through k=120:
the full divisor sum is k and the moving sum is k−1. Exact beta-weighted
coefficients also agree through that bound; no decimal zeta quotient was
used or fitted. The d=1 contribution is separately tested and mutated.

For every tested beta/cutoff, the finite tail ending at 128 is bounded by
the exact rational integral telescoping expression, which is bounded by
D^(1−beta)/(beta−1). Individual summands are also checked against their
integral intervals. The frozen records retain the actual rational tail
fragments. This finite evidence does not perform passage to infinity.

The actual tensor permutation of two 2-cycles is `[3,2,1,0]`, with cycle
lengths `[2,2]`; the 4-cycle is `[1,2,3,0]`, with cycle length `[4]`.
Their determinant polynomials are respectively (1−z²)² and 1−z⁴,
recomputed from their actual permutation traces.

## Gate inventory and limitations

| Gate | Exact checks | Mutations |
|---|---|---|
| S1 | 30,059: corner linearity/projections, matrix-unit multiplication/dagger/composition, field embeddings, whole code-image equality and actual tower maps | `corner-unit` |
| S2 | 137: direct reference-grade weights, independently counted totients, randomization, unnormalized trace restriction and conditioned references | `drop-divisor-weight`, `reset-corner` |
| S3 | 6,010: actual cyclic action, rank-one displacement norm one in d=2,...,16, finite direct-sum persistence, inverse action, degree-weight centrality | `identity`, `central-dynamics` |
| S4 | 1,989: cutoff ordinary densities, exact positivity/normalization/invariance, amplitude and matrix-valued Gram probes, finite tail comparisons | `density-factor`, `negative-density`, `tail-exponent` |
| S5 | 600: unweighted and beta-weighted convolution coefficients through 120, with the missing scalar term isolated | `d1-subtraction`, `coprimality` |
| S6 | 2,418: actual implementer/conjugation permutations and all declared positive, negative, and zero moments | `zero-moment`, `channel-trace`, `negative-power` |
| S7 | 3: tensor versus 4-cycle decomposition, powers and determinant polynomials | `tensor-cycle` |

The exact field moduli, encoded as binary bit polynomials, are 0b111,
0b1011, 0b10011, 0b1000011, and 0b1000000001001. Each quotient is
independently validated by checking that every nonzero element has
(|E|−1)-st power one. Labels are this checker's explicitly named quotient
labels; no literal identification with another presentation is implied.

Finite tests do **not** prove the infinite c0 completion, minimal
unitization, scalar-tail condition, outerness, point-spectrum closure or
infinite root multiplicities, lower semicontinuity/semifiniteness of a
weight, faithfulness on the infinite unitization, convergence, or an
infinite Dirichlet/zeta identity. The matrix positivity evidence concerns
the stated finite densities and Gram probes, not an all-matrix-level
infinite proof. The centrality checks test the finite degree-weight
operators and scalar phase conjugations; they do not identify them with
the nontrivial Frobenius automorphism.

No claim is made that the infinite trace can be applied to unregularized
U^j, that endpoint tensor closure exists, or that this is a universal
completion or a Riemann-zero spectrum. General and infinite assertions
remain the responsibility of the separate proof and hostile review.
