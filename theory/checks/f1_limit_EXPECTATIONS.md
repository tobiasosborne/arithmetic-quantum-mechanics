# Operational categorical limit — preregistered exact probes

Opened 2026-09-07 before the new proofs landed. This document records the
finite computations expected to falsify erroneous formulations; it is not
evidence for general continuity or categorical coherence theorems.

## Planned independent gates

| Gate | Mathematical data and comparison | Mutation |
|---|---|---|
| L1 | Rational Hecke coefficient multiplication evaluated before/after products and ordered block assembly | Alter a descent coefficient |
| L2 | Continuous normalized preparations from b* b / tau(b* b), including a rank-three collective block | Omit the trace factor |
| L3 | Exact instrument completeness, sequential composition, and total outcome probability | Remove an outcome |
| L4 | Typed corner refinement and the normalized-density dual ratio P_source/P_target | Omit or invert the ratio |
| L5 | Three-constituent refinement/preparation, local process and contextual Born witness at rational parameters approaching one | Collapse the local process before context extension |
| L6 | Local Gram recovery matrix and a nonzero minor at the endpoint | Use too few ancillary constituents |
| L7 | Exact unitary-reflection braid defect and endpoint symmetry | Demand the generic defect vanish |
| L8 | Tensor permutation representation, kernel/faithfulness examples, and cycle-count normalized traces | Drop a tensor cycle or replace finite-d trace by the coefficient trace |
| L9 | Composition of subgroup expectations and state preparation; comparison under the named trace | Use the wrong reference trace |
| L10 | Rank-one mirabolic adjacency, projection trace, and the null-sector limit | Retain a positive reference weight in the null sector |
| L11 | Vanishing-success instrument with two distinct conditional subsequences | Omit branch-probability normalization |
| L12 | Intersection-pattern upper triangular vector orbits and antichain valency factors | Alter the field-size exponent |
| L13 | Positive polar longest words, interval cactus relations, and block naturality | Use raw longest words as unitary reversals |
| L14 | Assembly/split retraction and retained-local-process compatibility | Identify collective coarse graining with identity |

The checker advertises each actual red mode through --help and reports a
named mathematical failure with exit code one, not an interpreter
exception. Existing operational Hecke, Bell, flag, partial-map and contextual
examples remain covered by f1_operational_check.py. Passing samples do not
promote a claim.

## Required worked protocol

Start with a named partial-flag corner/reference preparation, refine to a
three-constituent context, prepare the standard-block rank-one state by a
CP outcome, apply the retained adjacent local unitary, and measure its
return effect. Track every outcome probability and corner normalization.
The endpoint must agree with the existing density 3P and return 1/4.
For a postselected limit, record the strictly positive limiting success
probability. A separate vanishing-success example must demonstrate why
that hypothesis cannot be silently omitted.

## Implemented samples and mutation observations

`python3 theory/checks/f1_limit_check.py` uses a small polynomial coefficient
ring for the base-change calculation and rational arithmetic for all
evaluated operators and probabilities. No numerical tolerance is used.

- L1: all 36 basis products in H3 at q=1,3/2,2,3; all H2 left-block
  basis products in H4 at those parameters (160 probes).
- L2–L5,L7: q=1,101/100,11/10,3/2,2,3. Positive-square preparation,
  a four-outcome composed instrument, partial-corner refinement, and the
  stated collective protocol. Endpoint success/return/joint are 2/3,1/4,1/6.
- L6: n=2,3 and q=1,101/100,2, every local basis pair in the selected
  ambient context of size 2n-1. It tests the displayed unit minor, not all
  ambient observables or all n.
- L8: every permutation at n=1,2,3,4 and d=1,2,3,4. Enumerated tensor
  fixed points independently supply traces; rational Gram ranks test the
  representation image dimension. The alternating projection supplies an
  explicit quotient witness when d<n.
- L9: d=2,3,4,10,100, the trace-pairing equations for the expectation of
  (23) onto the algebra spanned by 1,(12). Its value is d^-1 times identity,
  whereas the coefficient-trace expectation is zero.
- L10: independent rank-one affine adjacency matrices at Q=2,3,5;
  reference-state weights at q=1,101/100,3/2,2, including normalized
  complementary-sector densities with a pole at one.
- L11: n=2,...,12 with rational amplitudes t=2n/(n²+1) and
  c=(n²-1)/(n²+1). On the collective qubit use success Kraus t times
  identity/transposition according to parity, and failure Kraus c times
  identity. Exact operator multiplication checks completeness and computes
  conditional return probabilities 1 and 1/4 while success tends to zero.
  The general failure of convergence requires a written continuous
  interpolation argument; finite samples alone do not prove it.
- L12: every w in S_n at n=1,2,3, over F2 and F3. Enumerate all matrices
  in B intersect wBw^-1 and their vector orbits. Compare their exact support
  sets, partition, and sizes with antichain/downset formulas (190 probes).
- L13: n=2,3,4 and q=1,4,9. Rational spectral interpolation constructs
  the polar longest word. Every candidate spectral projection is checked
  self-adjoint/idempotent, their sum is identity, and the positive weighted
  sum squares to T_w0^2. These certificates justify the finite polar
  calculation without an assumed spectral formula. All nested/disjoint
  interval relations and generating block-naturality squares are tested.
- L14: every basis element of H3 at q=1,101/100,2, with the 2+1 block
  expectation: idempotence, trace preservation, local-unitary compatibility,
  and its nonidentity action on the collective generator (23).

The first eleven red modes and green run were observed on 2026-09-07;
L12's exponent mutation was then separately observed failing before its
first acceptance run. L13's raw-longest-word mutation was likewise observed
failing before its first acceptance run, as was L14's false collective
identity. Final consolidated verification
follows admission.

| Mode | First failed gate | Mutated mathematical data |
|---|---|---|
| --red-descent | L1 | Numeric descent coefficient q becomes q+1 |
| --red-density | L2 | Omit positive-square density normalization |
| --red-outcome | L3 | Remove the final composed instrument outcome |
| --red-corner-ratio | L4 | Omit the source/target trace ratio |
| --red-context | L5 | Replace retained ambient local unitary by identity |
| --red-ancilla | L6 | Use size 2n-2 instead of 2n-1 |
| --red-braid | L7 | Replace the generic braid defect by zero |
| --red-cycle | L8 | Decrease the fixed-point cycle exponent by one |
| --red-reference-trace | L9 | Use coefficient expectation at finite d |
| --red-null-weight | L10 | Give the null reference sector weight 1/2 at one |
| --red-postselection | L11 | Divide a branch probability by one instead of its success probability |
| --red-valency | L12 | Increase the vector-orbit field-size exponent by one |
| --red-polar | L13 | Omit the positive absolute-value normalization |
| --red-collective-identity | L14 | Replace a proper collective coarse graining by identity |

Each gate evaluates all its listed probes before its final conjunction is
reported. Mutation reachability is claimed at the gate level, not for every
individual diagnostic or source-code branch. Some mutations also trigger
later dependent gates; those additional failures are expected.
