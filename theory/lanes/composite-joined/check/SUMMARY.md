# Independent verification of the finite joined preparations

2026-09-09. Third bounded artifact, independently implemented from its
proposed proof. The two earlier checkers remain unchanged. No trunk edits,
commits, nested agents, claim promotions, or proof adjudications were made.
Execution used the parent-inherited Codex verifier configuration; no
cross-family independence is asserted.

## Standalone checker and frozen evidence

```sh
python3 theory/lanes/composite-joined/check/composite_joined_check.py
python3 theory/lanes/composite-joined/check/composite_joined_check.py --red-drop-divisor
python3 theory/lanes/composite-joined/check/composite_joined_check.py --red
python3 theory/lanes/composite-joined/check/freeze_results.py
```

The promotable checker imports only Python's standard library and uses
exact integers and Fractions. No repository helper, earlier checker,
floating-point tolerance, decimal zeta value, or fitted asymptotic is used.

Standalone SHA256:
`d945e902a081db587ef8cf0f0c5344c5fa42dcdfaf06ba4d97fdeecfbff8c51f`.

**9,272 exact comparisons passed across J1--J5.** All **12 advertised
red flags** returned exit 1 with JSON status FAIL at their registered
mathematical gates: 11 named mutations and plain `--red`, which aliases
the actual `drop-divisor` mutation. The legacy `--red NAME` syntax also
remains supported. The freeze runner discovers the flags from `--help`
with the session-close regex and invokes every flag without extra arguments.
Parser errors and uncaught Python exceptions are excluded as evidence.

Actual final outputs, help and hashes are in `results/`, indexed by
`results/manifest.json`. Green stdout SHA256:
`2eb91a894097cfd663b698055989cf44cc961e4af87417b1971d14e4f266e265`.

The preregistration is `EXPECTATIONS.md`. The first executable test was
the actual F4 copied-reference red, before any green; its output and
then-current source hash are frozen in `preregistered-first-red.json`.
During implementation the first full green exposed a checker defect:
empty-vector integer zero became floating-point zero during division.
This was corrected to rational zero, with an exactness assertion on all
branch probabilities, before final freezing. That development failure is
retained separately and is not an arithmetic counterexample.

## Declared finite scope

Scalar and common-mixture probes use d=2,...,64, s=1,2 and beta=2,3,4.
The rational t values are

```text
1, 65/64, 33/32, 17/16, 9/8, 6/5, 5/4, 3/2, 2.
```

The fixed upper comparison parameter is T=2. Cutoff pairs are
(D,E)=(2,4),(4,8),(8,16),(16,32),(32,64). For each smaller cutoff,
continuity is also tested at t=1+1/m, m=4,8,16,32,64.

Actual finite arithmetic uses p=2, s=1,2 and relative d=2,3,4;
all named t values execute on F4, F8, F16, F64 and F256 as appropriate.
Physical degree-tagged mixtures use D=2,3,4 and all named beta values.
The first coefficient is derived from the actual field reference and
actual copied projection, separately from the raw t=1 event.

The fields have binary moduli 0b111, 0b1011, 0b10011, 0b1000011,
0b100011011. Every nonzero element's (|E|−1)-st power is checked to be
one. Multiplication, Frobenius, relative orbits, the copied graph,
simultaneous projector, relative permutation, computational dephasing,
and randomizer outcomes are computed on their actual finite label sets.

## Exact findings

No finite arithmetic or proposed-formula counterexample was found.
Count polynomials are obtained by divisor subtraction. Totients are
independently computed by listing coprime integers. Synthetic division
of c_d(t^s) by t−1 computes v_d(t) independently of the quotient formula,
including v_d(1)=phi(d)/d. Every sampled value is strictly positive and
at most one. The separate d=2 identity and lower normalizer bound hold:

```text
v_2(t) = (sum_(j=1)^s t^(-j))/(2s) >= 2^(-s)/2,  1<=t<=2.
```

Every actual copied preparation agrees with
c_d(t^s)/(d t^(sd)). At t=1 the physical success is zero; no normalized
raw conditional state is formed. Its separately retained first grade is
s phi(d)/d. Degree mixing uses the declared normalized d^(-beta) prior,
and the actual successful common responses agree with the stated rho_(D,t).

Example D=4, beta=2 has prior normalizer L_D=61/144, endpoint normalizer
Z_D(beta,1)=199/864, and 15 retained primitive/averaging/randomizer history
tags. Their probabilities sum exactly to one at every sampled t.

| s | t | Actual total success | First coefficient in h=log(t) |
|---|---|---|---|
| 1 | 1 | 0 | 199/366 |
| 1 | 6/5 | 2297/26352 | 199/366 |
| 1 | 2 | 235/976 | 199/366 |
| 2 | 1 | 0 | 199/183 |
| 2 | 6/5 | 146597/948672 | 199/183 |
| 2 | 2 | 1319/3904 | 199/183 |

The two measurement placements remain distinct. Before relative
randomization, the coherent full/identity/dephased comparison gives
1,0,1/d. After uniform randomization and explicit randomizer-tag discard,
the same fixed Q_1 test gives 1/d,1/d,1/d². The successful randomized
common state is tr_d and is invariant under relative Frobenius; its
single-shot response is not claimed to distinguish R from identity.
All three comparison circuits retain both final outcomes as well as the
earlier primitive and averaging failures.

Trace distances are computed as sums of absolute differences over
individual Hilbert basis eigenvalues. Every finite cutoff pair satisfies
the exact identity

```text
||rho_(D,t)-rho_(E,t)||_1 = 2 (Z_E(beta,t)-Z_D(beta,t))/Z_E(beta,t),
```

and the proposed uniform cutoff estimate. For example, D=2,E=4,beta=2
at t=1 has distance 182/199; multiplying the proposed bound by t−1
incorrectly makes its right-hand side zero and is rejected. Bounds larger
than the trivial distance bound two are retained as upper bounds, without
being treated as equalities or sharp estimates.

Finite tail fragments are checked against exact rational integral bounds,
with the explicit v_2 contribution providing a positive denominator.
No estimate is inferred from decimal fitting.

Shrinking-step comparisons use an independent finite continuity estimate
from the absolute coefficients of c_d(t^s)/(t−1). If those coefficients
are b_k, the tested bound on each v_d variation is based on
sum_k |b_k|(sd−k)/(sd), obtained from the finite powers t^(-(sd−k)).
The resulting normalized-state estimate is checked against the actual
trace distance. At D=4,beta=2,s=1 the actual distances to the endpoint are
2184/41989 at t=5/4 and 504/131539 at t=65/64; all intermediate rational
steps and their exact coefficient bounds are frozen.

The actual relative cyclic permutation preserves both cutoff densities
and their trace distance. A fixed non-diagonal projection on blocks
2,3,4 is verified by matrix multiplication, and its response differences
obey the computed trace-distance estimate.

## Coverage and limits

| Gate | Exact checks | Mathematical red modes |
|---|---|---|
| J1 | 3,420: counts, divided polynomial, endpoint grade, strict positivity, uniform v bound and v_2 normalizer | `omit-gap`, `condition-zero` |
| J2 | 1,585: actual fields and graph averaging, physical probabilities, both randomization placements, full histories and tag discard | `drop-divisor`, `reset-copy`, `drop-randomizer` |
| J3 | 1,740: declared prior ratios, normalized common mixtures, actual degree-tagged histories and total success | `wrong-prior`, `wrong-normalizer`, `lost-history` |
| J4 | 1,501: actual trace distances, tail identity, uniform cutoff bound, shrinking rational steps, relative permutation and named fixed effect | `vanishing-bound`, `operator-norm` |
| J5 | 1,026: independently retained actual first grades, nonzero success rates and endpoint conditional common states | `drop-grade` |

These finite probes do not prove uniform convergence of Z_infty, existence
or continuity of its infinite density, the infinite trace-norm estimate,
interchange of the two limits along every path, the infinite success-rate
ratio, or convergence for every bounded effect. They check finite
fragments, finite coefficient bounds and one named fixed effect. Actual
arithmetic preparations are limited to p=2, d<=4 and s<=2; the larger
degree calculations concern the specified common counting coefficients
and finite matrix mixtures, not enumerated fields of those dimensions.

No arbitrary p-dependent physical continuation, identification of field
multiplicity states at different characteristics, unique choice of degree
prior, endpoint tensor/sum closure, or Riemann-zero spectrum is asserted.
All general limit statements remain for the separate proof and review.
