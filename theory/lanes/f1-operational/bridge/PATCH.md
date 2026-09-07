# Proposed integration patch (for the coordinator)

No trunk file was edited.  Apply only after reconciling with the independent
Hecke-tower and contextuality lanes.

## `docs/sidequests/f1-qm.md`

**Anchor:** the paragraph beginning `North-star clarification, 7 September
2026.`

Add a compact subsection after the operational-source discussion with these
points:

- for `L=F_p^n`, `C[Flag(L)]` is a new context Hilbert space;
- flags inject equivariantly into nested commuting Weyl projector chains in
  `End(C[L])`;
- `GL(L)` is the symplectic Levi and acts by Clifford permutation unitaries;
- the Hecke algebra is the context commutant, not the original Weyl algebra;
- normalized partial-flag incidence maps give composable UCP compressions;
- abstract `H_n(p)` over `C` loses `p` unless the standard basis/module/trace is
  retained.

Use `BRIDGE.md` section 2 for the projector formulas and section 4 for the CP
maps.

**Anchor:** the roadmap row containing `Tits-lift/Fourier`.

Add two roadmap rows:

1. `Flag-Hecke/Weyl refinement`: integral `q`-deformation of the explicit
   partial-flag Hecke algebroid, compatible with controlled Weyl projectors and
   type-A direct sum.
2. `Type-C block composition`: construct a bimodule/correspondence replacing
   parabolic induction for `B_m x B_n < B_{m+n}` and test associativity.

## `labbook/sections/sidequest_f1.tex`

**Anchor:** the opening paragraph ending `do not by themselves satisfy this
operational criterion.`

Add one self-contained comparison paragraph: the finite-p flag sector is an
honest C*-quantum context system with CP refinement maps, but its Hilbert space
has dimension `[n]_p!` rather than `p^n`; it couples to AQM through controlled
stabilizer projectors.

Add a second paragraph separating the two TL boundaries:

- positive `q=1` gives `delta=2` and the `SU(2)` tensor category only after a
  rank-two quotient and Markov-state choice;
- Fibonacci is the fifth-root, `delta=phi` Jones fusion quotient;
- the canonical full-flag trace is not preserved by the TL quotient.

## Sources

Register IWAHORI64, CURTIS88, GW93, BFK00, KL08 and ILZ17 from `SOURCES.md`.
GH07, CK21 and BSS07 already have root ledger entries; reuse their existing
records and locators rather than duplicating them.

## Candidate claim scope

Admit the finite-p flag/projector/CP construction no higher than `SKETCH` until
its formulas are independently checked.  Keep the integral deformation and
type-C composition statements `CONJECTURE`.  Do not state that TL inherits the
flag trace or that either `SU(2)` or Fibonacci is the established F1 endpoint.
