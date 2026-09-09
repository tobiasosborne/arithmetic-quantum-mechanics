# Independent finite verifier: relative multiplication graph

2026-09-09. Verifier lane only; no proof adjudication, promotion, trunk edit,
commit, or nested delegation. Execution used the parent-inherited Codex
verifier model configuration; no cross-family independence is asserted.
The implementation is independent of the candidate proof/implementation:
it imports only this lane's files, Python's standard library, and NumPy.
The existing positive-arithmetic checker was inspected for repository
conventions; its implementation was neither imported nor copied.

## Invocation and frozen evidence

From the repository root:

```sh
python3 theory/lanes/composite-boundary/check/standalone_composite_boundary_check.py
python3 theory/lanes/composite-boundary/check/standalone_composite_boundary_check.py --red-separate-descent
python3 theory/lanes/composite-boundary/check/standalone_composite_boundary_check.py --red
python3 theory/lanes/composite-boundary/check/freeze_results.py
```

`freeze_results.py` runs every red first, requires exit 1 and its registered
mathematical failure gate, and then requires green exit 0. It freezes actual
JSON outputs in `results/` and records source/output SHA256 digests in
`results/manifest.json`. There are **19 distinct mathematical mutations**.
Each is advertised in `--help` as a standalone `--red-<name>` flag. Plain
`--red` is a genuine alias for `--red-collective`; the earlier `--red NAME`
form remains supported. Frozen evidence executes all 19 named flags and
the plain alias without extra arguments: **20 red runs plus one green**.
No advertised red failed through a Python exception or parser error.
The first executed check was the actual collective-block red; it failed at
C1 before the first full green execution.

Promote only `standalone_composite_boundary_check.py` to the authoritative
checker directory, renaming it `composite_boundary_check.py` there if desired.
It has no lane/repository helper imports. `build_standalone.py` creates it
mechanically from the modular originals and verifies identical ASTs for
every function and class definition; consolidation changes no mathematical
gate. The frozen runs invoke this standalone executable.

Interface repair, 2026-09-09: session-close discovers red flags from help
and invokes each without an argument. The original required-argument
`--red NAME` interface would therefore have produced parser exit 2.
Only `main`'s argument parsing changed; all 25 other function/class ASTs
are unchanged. The before/after preservation check and advertised flag
inventory are frozen in `results/cli-interface-repair.json`.
The repaired standalone SHA256 is
`5816197b901d74012112d2957c5df45ad7b634b426e6c64bb46c16ed0f3df3d1`.
All 20 flags discovered by the exact session-close help regex were
executed without additional arguments and returned mathematical JSON
failures with exit 1. Green remains 76,584 exact comparisons and its
output SHA256 is unchanged:
`fa585f8e010871cc78890648a569606239a01b2e9d2c6fc433620cb5aeae5901`.

All arithmetic is exact: integer finite-field tables, rational sparse
vectors, exact Gaussian elimination, rational polynomial coefficients, and
the cyclotomic quotient Q[zeta_p]/(1+...+zeta_p^(p-1)). No floating-point
tolerance is used. Orbit vectors are represented by unnormalized orbit
sums with their exact squared norms retained; every probability restores
the normalization. Fourier matrices likewise retain the exact omitted
sqrt(|E|) factor in the probability denominator.

## Results

All six preregistered fibres pass C1--C9: **76,584 exact comparisons**.
No finite counterexample was
found. The arithmetic point uses t=p; the base cardinality remains p^s.

| E/K | (p,r,s,n) | Success at t=p | Grade-one coefficient | Conditional full / identity / dephased | Fourier return |
|---|---|---|---|---|---|
| F4/F2 | (2,2,1,2) | 1/4 | 1/2 | 1 / 0 / 1/2 | 1/4 |
| F9/F3 | (3,2,1,2) | 1/3 | 1/2 | 1 / 0 / 1/2 | 1/9 |
| F16/F2 | (2,4,1,4) | 3/16 | 1/2 | 1 / 0 / 1/4 | 1/16 |
| F16/F4 | (2,4,2,2) | 3/8 | 1 | 1 / 0 / 1/2 | 1/16 |
| F27/F3 | (3,3,1,3) | 8/27 | 2/3 | 1 / 0 / 1/3 | 1/27 |
| F8/F2 | (2,3,1,3) | 1/4 | 2/3 | 1 / 0 / 1/3 | 1/8 |

Each fibre also executes t=1,6/5,3/2. The unconditioned success at t=1
is exactly zero; conditional probabilities are evaluated only at t>1.
Every preparation norm equals c_n(t^s)/(n t^(sn)). Grade one is computed
independently from actual POS weights on individual field labels and
equals s phi(n)/n. Dephased whole-experiment grade one is smaller by n.
All relative moving-block weights c_d(t^s)/(d t^(sn)) and their leading
coefficients s phi(d)/d are checked separately.

## Gate coverage

| Gate | Executed comparison | Actual red mutations |
|---|---|---|
| C1 | S1--S4 permutation composition; dimensions 1,2,6,24; exact rank-four standard matrix block; actual 1/4 return | `collective`: replace the second collective adjacent exchange by the first local one |
| C2 | Enumerate all 29,180 actual three-register tuples across six fibres; field multiplication; actual relative orbit census; graph-predicate and simultaneous-average construction | `product`: change one used multiplication entry; `diagonal-action`: omit Frobenius on the second register |
| C3 | All graph Gram entries; actual M(I tensor U tensor I)M* action; every common matrix unit on every orbit copy; separate versus collective invariance | `identity`; `diagonal-relative`; `separate-descent`: independently average the two relative registers |
| C4 | Actual copied POS reference, preparation norms at all named t, endpoint zero, coefficient-one calculation, every copied-and-averaged block weight | `drop-grade`; `reset-reference`: insert independent reference weights for the copied controls |
| C5 | Explicit pure graph vectors and explicitly dephased computational density entries, followed by actual R and Q_(n,1) | `dephase`; `omit-invariant`: use only the diagonal final graph predicate; `normalizer`: divide the successful branch mass by an extra n |
| C6 | Actual rectangular M2 Hom blocks for a coherent duplicate; 1 versus 1/2 coherent/tagged return; primitive, averaging, final and comparison-circuit failure histories sum to one | `off-diagonal`; `omit-outcome`: delete the real primitive-failure history |
| C7 | All six named embedding maps, both F4→F16 roots, eight twisted tower paths, relative graph/action/copy squares, both averaging outcomes, actual J/V Fourier squares and V decoder outcomes | `embedding`: alter the embedded third coordinate; `wrong-sector`: send a lower primitive component to the larger primitive component |
| C8 | Full actual first-register Fourier image of every primitive graph vector, exact compressed cyclotomic phase, full and projected norms, retained failure norm | `fourier-phase`: change the actual Fourier kernel sign; `fourier-outcome`: delete its ambient failure branch |
| C9 | Actual relative permutation traces, det(I-zR) reconstructed independently from those traces, orbit-factor polynomial, common trace/pure-state moments, actual conjugation permutation multiplicities, randomization | `multiplicity`; `channel-spectrum`: assign implementer multiplicities to its conjugation channel |

The relative common-block implementer has each n-th root once; the
conjugation channel on M_n has each n-th root n times. The actual full
ordinary traces Tr(R^j), for j=0,...,n, are respectively:

```text
F4/F2:    4, 2, 4
F9/F3:    9, 3, 9
F16/F2:  16, 2, 4, 2, 16
F16/F4:  16, 4, 16
F27/F3:  27, 3, 3, 27
F8/F2:    8, 2, 2, 8
```

The prepared pure logical expectation of R^j is 1 when n divides j and
0 otherwise. The common-block ordinary trace is n times that value.
Both are recorded separately from the full multiplicity trace.

## Exact named field presentations and scope limitations

The quotient presentations are F4=F2[a]/(a²+a+1),
F8=F2[a]/(a³+a+1), F16=F2[a]/(a⁴+a+1),
F9=F3[a]/(a²+1), and F27=F3[a]/(a³+2a+1).
Every nonzero element's (|E|-1)-st power is checked to be one, so the
finite quotients are validated as fields. All roots of the source
polynomial are enumerated to obtain the named embeddings. In F16's
base-two integer encoding, the two F4 embeddings map its generator to
6 and 7. This is an explicitly named isomorphic binary tower, rather than
an assertion that these integer labels literally equal D1310's nested
pair labels. A non-prime-base relative sigma=x^4 comparison is also
executed for both embeddings F4→F16.

These checks do not prove an all-field/all-parameter theorem, positivity
for a general varying family, source-presentation soundness/completeness,
or the abstract projection/additive completion. The C6 finite matrix
calculation checks the declared coherent completion, not its universal
property. No semantic-faithfulness assertion about FRP syntax is tested.

The whole Fourier output is computed in the ambient register word; only
the stated primitive first-register compression is tested. No Fourier
closure of the common algebra is inferred. J/V comparisons are tested
on the explicitly listed finite embeddings. The checker does not identify
different random-outcome tag sets under tower maps, prove arbitrary
history comparison theorems, or require endpoint tensor/direct-sum closure.
No infinite-dimensional trace or Riemann spectral claim is assessed.

Ground-truth reading: CLAUDE.md, PRD.md, current HANDOFF.md direction,
D1301--D1308, D1331--D1334, D1501--D1503, the active work order, and the
pre-implementation SPEC.md/EXPECTATIONS.md. Passing this finite verifier
supplies falsification evidence only and makes no status adjudication.
