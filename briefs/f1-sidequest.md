# Sidequest: arithmetic quantum mechanics over the field with one element

Opened 2026-09-06 at the user's request. This is an exploratory sidequest;
it does not replace the finite-ring campaign or authorize the Atlas work.

The user asks for a literature-grounded deep dive across **all the relevant
analogies**, with a precisely formulated conjectural or provable formulation
of quantum mechanics over `F_1` as its north star. Do not select one model
prematurely. Sol subagents are permitted; Astra and Claude subagents are not.

## North-star clarification — 2026-09-07

The user has sharpened the target: the primary object is the **family of
subsystems and their assembly rules**, not a single-particle quantum system.
The p=1 endpoint must admit an operational realization by C*-algebras,
normalized positive linear functionals/density operators, CP dynamics and
the Born rule. The category should retain enough arithmetic structure to
remember p before any p→1 specialization is attempted.

Fibonacci is the guiding example of nonstandard composition, not a proposed
identification with the F1 endpoint. A strong monoidal fibre functor to
ordinary Hilbert spaces is not a universal requirement. Local observable
algebras may embed properly into the algebra of a composite. The realization
must include compatible channel extensions and preparations, not only
unrelated algebras or CP maps at each isolated object.

First distinguish coherent Hilbert direct sums from classical C*-algebra
direct sums, arithmetic subsystems from arbitrary encoded subspaces, and
ordinary functorial realization from preservation of the standard tensor
product. Existing combinatorial/classical models are possible inputs; their
native state sets alone do not satisfy the new endpoint criterion. Preserve
positivity and normalized probabilities as acceptance tests for any proposed
specialization. No unspecified analytic limit of primes is assumed.

## Success criteria

1. Explain the project's distinction between an arithmetic base and complex
   amplitudes before comparing it with quantum theories whose amplitudes are
   themselves over `F_q` or `F_1`.
2. Compare the developed routes: thin geometry/Tits–Weyl models, pointed
   monoids, cyclotomic extensions and absolute quantum theory, finite
   Heisenberg representations, Hall algebras/categorical oscillators,
   Frobenius/lambda descent, Bost–Connes endomotives, and toric/analytic
   and tropical connections. Identify adjacent motivic QFT separately.
3. For each, identify states, observables, phases, composition, symmetries,
   dynamics, realization functors, and what the source actually establishes.
4. State several precise candidate formulations and their comparison
   problems. Establish a finite positive bridge where feasible without
   treating that bridge as the whole answer.
5. Add a self-contained, clearly marked labbook section and rebuild the PDF.
   Every new result has an honest status; existing statuses are unchanged.

## Evidence and work allocation

Approximately half the work is source reading and mathematical synthesis;
roughly a third is worked examples, exact checks, and the labbook. Review
and housekeeping use the remainder. Primary bodies are stored under `refs/`
and indexed with retrieval route, SHA256 and theorem/section locators in
`refs/LEDGER.md`. No claim of an exhaustive survey of every F1 paper is made.

Independent Sol/xhigh lanes, isolated under `theory/lanes/f1/`:

- `landscape`: primary F1 geometry and existing absolute quantum proposals.
- `prove`: finite cyclotomic Heisenberg bridge, structured derivation.
- `hall`: Hall/groupoid/categorical Heisenberg and Fock literature.
- A subsequent blind critic reads the proposed mathematical artifact,
  source bodies and checker, without the prover's reasoning or SUMMARY.

The coordinator researches arithmetic descent, endomotives and adjacent
analogies, reconciles evidence, builds the checker, and writes the deliverable.
The capped review rule applies to positive results proposed for PROVED.

## Pre-registered exact finite checks

For a finite abelian configuration group `A` of exponent dividing `N`, use
`A^vee=Hom(A,mu_N)` and `W(a,chi)=Z(chi)X(a)`; the multiplication cocycle is
`c((a,chi),(b,eta))=eta(a)^(-1)`. The finite-ring identification is
`b -> (x -> psi(-bx))`, recovering the root project's exact reference sign.

Test `A=0, C2, C3, C4, C2×C2, C5, C6, C2×C3`, with appropriate `N`,
including a phase extension `C2` at `N=4`. Gates compare independently
constructed monomial operators and abstract group products, compute the
commutator radical, and verify the Weyl basis by exact character sums.
Compare finite-ring operators for the five rings of orders 2, 3 and 4;
explicitly check the nonfaithful additive-character kernel for `F4`.
Check tensor products and the absence of a monomial Fourier transform.

Also check Hall/binomial coefficients and the oscillator commutator on
individual polynomial basis vectors, keeping the infinite-domain statement
separate from finite truncation. Polynomial counting specializations are
not limits of Hilbert spaces or of group objects.

Each independent gate gets a named mutation, run first and required to
fail at that gate. Roots of unity use exact integer polynomial arithmetic.
Passing examples prove nothing by themselves.

## Persistent homes

- Comparative research map and roadmap: `docs/sidequests/f1-qm.md`.
- Structured mathematics: `theory/sidequests/f1-*.md`.
- Checker: `theory/checks/f1_check.py` and its expectation/mutation record.
- Sidequest definitions: reserved `D1001` onward in `definitions.md`, to
  avoid colliding with the unadmitted finite-ring lane's proposed numbers.
- Claim ids: `F1-*`, grouped as a sidequest in `claims/CLAIMS.md`.
- Human-readable product: `labbook/sections/sidequest_f1.tex`, included
  after the current ring sections; `labbook/main.pdf` rebuilt in lockstep.

## North-star acceptance test

A candidate must specify its input category, target category, realization
functor, named phase/polarization data, and the exact recovered quantum
system. A broad statement about all F1 schemes remains a research target
until its domain and comparison maps can be defined. No universal
Stone–von Neumann or Weil theorem is inferred from a Weyl-group analogy.
