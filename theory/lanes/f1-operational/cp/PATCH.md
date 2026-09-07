# Proposed admission patch (string anchors only)

This file is instructions for the orchestrator.  It does not authorize a lane
write outside this directory.

## 1. Definitions

Target: `definitions.md`.

Anchor: the complete D1013 definition ending with
`Its clock/shift realization is claim F1-TORUS.`

Action: append condensed versions of candidate definitions D1121--D1125 from
`cp-operational.md`, D1126 from `kraus-context-faithfulness.md`, and D1127
from `PARTIAL-MAPS.md`.
Preserve all named choices: positive spherical trace,
associators, conditional expectations, stable scalar-unitary Kraus equivalence,
environment interchange data, and the coefficient trace of the symmetric-group
net.  Do not define arbitrary isolated CP maps as tensorable processes.

## 2. Claims

Target: `claims/CLAIMS.md`.

Anchor: the final row/group of existing `F1-*` claims.

Suggested candidate rows, subject to the capped proof/critic loop:

- `F1-OP-ALG`: CPOP-1 and CPOP-2, categorical endomorphism algebras,
  trace-preserving assembly expectations, states/preparation/Born semantics.
- `F1-OP-PROC`: CPOP-3, coherent retained Kraus processes and scoped dilation
  composition.
- `F1-OP-FIB`: CPOP-4, exact failure of isolated-channel tensor congruence and
  its two Born witnesses.
- `F1-OP-SYM`: CPOP-5, finite-injection symmetric-group quantum net and exact
  `S_2 -> S_3` Born witness.
- `F1-OP-KCF`: KCF-1, equality of the q=1 Kraus Gram, stable scalar-unitary
  equivalence, and all-context operational equivalence, with sharp universal
  ambient bound `2n-1` and constructive density/effect Born separation.
- `F1-OP-PMAP`: PMAP-1, the dagger lax symmetric monoidal functor from finite
  partial injections to traced finite C*-algebras and bistochastic CP maps.

Do not label any row PROVED until the required blind critic and repair wave are
complete.  The finite-`p` Hecke family and p-memory invariant belong to the
other lane and are dependencies, not claims of this shard.

## 3. References

Target: `refs/LEDGER.md`.

Anchor: the existing F1 entry for `2211.03855`.

Action: add the Jones--Penneys `1611.04620v2` entry using the title, PDF hash,
retrieval URL, and locators in `SOURCES.md`; move its PDF/text into the normal
`refs/f1/1611.04620/` layout if admitted.  Existing 0707.4206 and 2211.03855
entries need only gain the more precise equation locators from `SOURCES.md`.

## 4. Sidequest research map

Target: `docs/sidequests/f1-qm.md`.

Anchor: heading `## Precise north stars and comparison problems`.

Action: before that heading, add a short section whose conclusions are:

1. `X -> End_C(X)` is an observable net with proper assembly inclusions and
   canonical trace expectations.
2. Its states and Born pairing are ordinary finite-dimensional C*-quantum
   mechanics with categorical charge weights.
3. Process composition uses retained Kraus/dilation/context data; isolated CP
   shadows cannot be the morphism quotient.
4. The concrete `q=1` operational candidate is the finite-injection net
   `C[Sym(S)]`, conditional on the separate arithmetic specialization result.
5. Its exact process quotient is the admissible Kraus Gram; `n-1` ancillary
   points suffice and are sometimes necessary to distinguish an `n`-point
   local process.
6. Standard `F_1` normal maps act functorially by expectation, relabeling, and
   inclusion; the empty map is trace-and-prepare and wedge has a proper lax
   assembly map.

Include the exact Fibonacci and `S_2 -> S_3` witnesses, but do not identify
Fibonacci with the `F_1` endpoint.

## 5. Labbook lockstep

Target: `labbook/sections/sidequest_f1.tex`.

Anchor: heading `\subsection{Precisely formulated outputs and open comparisons}`.

Action: insert the condensed operational theorem, definitions of density/effect
and Born pairing, the symmetric-group worked example, the partial-injection
functor, and the exact Kraus-Gram quotient with sharp `2n-1` context theorem
immediately before this heading.
State status honestly after the capped loop, then rebuild `labbook/main.pdf`
and inspect the added pages.  Avoid any assertion that all CP maps extend
canonically or that the Hecke specialization was proved in this lane.
