# F1 sidequest: arithmetic subsystem diagrams with quantum semantics

Opened 2026-09-07. The user explicitly asks to chase the category-first
idea: preserve the family of subsystems and its composition, extract the
arithmetic parameter, and seek a p=1 endpoint with density operators,
CP dynamics, Born probabilities and nontrivial composite quantum algebras.
Fibonacci is a test of composition, not a prescribed F1 answer.

## Concrete target for this increment

Develop and compare a **flag/Hecke context sector** and its quantum
operational net. This is an extraction from polarized finite-field AQM,
not an assertion that flag wavefunctions are the original Weyl wavefunctions.
The desired positive result has three parts:

1. Positive type-A Hecke algebras H_n(q), canonical flag trace, contiguous
   parabolic embeddings and conditional expectations, with q=1 equal to
   C[S_n]. The q=1 finite-set/injection net has scalar one-site algebra,
   a two-sector two-site algebra, and an M2 sector at three sites.
2. The two overlapping H2 subalgebras of H3 remember q≥1 through the
   intrinsic rank-one overlap q/(q+1)^2, although the abstract algebras are
   independent of q. This is the decisive arithmetic-memory test.
3. Keep local Kraus data, not only their isolated CP action. A central
   unitary of H2 has trivial isolated conjugation but a nontrivial action
   in H3; at q=1 an exact Born probability changes from 1 to 1/4.
   Give a coherent sufficient class of local CP operations in all contexts.

## Boundaries and parallel work

All subagents are Sol/xhigh, with no descendants. Lanes are isolated:

- `theory/lanes/f1-operational/hecke/`: positive tower and overlap theorem.
- `theory/lanes/f1-operational/cp/`: operational net, Kraus context data and
  independent Fibonacci comparison.
- `theory/lanes/f1-operational/bridge/`: exact extraction from Weyl AQM,
  type-C alternative and Temperley–Lieb/SU(2) comparison.

The coordinator implements exact independent checks, reconciles the
sources, writes the labbook and runs the capped hostile review on the
headline positive result. About half the work goes to mathematics and
sources, a third to checks/examples/labbook, and the remainder to review.
The lower-level FCR-2 lane remains untouched.

The full finite-p AQM recovery and a universal F1 specialization remain
separate questions. No family of matrix algebras of noninteger dimension
is postulated. No unitary Hecke braid or symmetric assembly is assumed
for q≠1. Type-C block inclusions and a change from the canonical flag
trace to a Temperley–Lieb Markov trace require their own justification.

## Pre-registered falsifiers

Use q=1,2,3,5 and 1/2, n≤4. Algebra computations use rational coefficients
in the permutation basis, with right simple multiplication

`T_w T_i=T_(w s_i)` on an ascent, and
`T_w T_i=(q-1)T_w+q T_(w s_i)` on a descent.

Compare this independent implementation to theorem formulas:

- quadratic/braid/far-commutation, associativity and star;
- exact canonical Gram form and positivity;
- block inclusions, trace, coefficient-projection expectation, bimodule
  identities and positivity on the commutative H2×H2 test subalgebra;
- central idempotents of H3, its 1+1+4 algebra dimensions, and overlap
  q/(q+1)^2 in the unique matrix block;
- local CP invisibility versus collective Born probability (1-2a)^2;
- failure of braid for the unitarized generators away from q=1;
- q=1 arbitrary finite injections and subgroup expectations;
- normalized Kraus lists, scalar-isometry invariance, and local extension;
- independent flag adjacency matrices for F2^3 and F3^3, including their
  normalized matrix trace and Hecke relations;
- Temperley–Lieb relation after its explicit quotient, distinguishing
  the faithful flag trace from a separate quotient-compatible trace.

Every implemented gate gets a named mutation, run failing first. Use
exact integers/rationals; passing examples do not promote a theorem.

## Deliverables

The source ledger, a new mathematical labbook section, a compact research
report with precise constructions and limits, structured proof shards,
and an exact checker with recorded expectations. Reserve D1101+ for the
Hecke definitions and D1121+ for operational definitions; statuses follow
the existing project vocabulary and review rule.
