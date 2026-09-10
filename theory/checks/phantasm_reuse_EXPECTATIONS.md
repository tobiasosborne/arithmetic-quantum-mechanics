# Phantasm reuse bridge: exact finite expectations — 2026-09-10

Registered before the first execution. This deliberately imports the
existing `f1_check.Abelian` operator implementation and the existing exact
finite-field library. The new wavefunction action is evaluated separately
on basis functions, so the test compares the proposed convention with the
admitted implementation rather than copying that implementation.

| Gate | Scope | Required mutation failures |
|---|---|---|
| R1 | Character-dual identification over F3 and F5 at ranks 0,1; F3 at rank 2; F9 at ranks 0,1; all nonzero trace-character parameters in each field | dual-sign, trivial-character |
| R2 | Same labeled operators: old Abelian action times the positive half-dot phase versus D1703's negative-phase, x-a wavefunction | rephase, position-labels |
| R3 | Exact half-form multiplication on every pair of phase labels; raw-center kernel equals ker(psi), not necessarily zero | cocycle, central-injective |
| R4 | Exact operator Gram, matrix-basis size and normalized identity trace; rank-zero configuration included | trace-normalization, vacuum |
| R5 | Symmetrizing cochain and inherited configuration-product tensor for F3 ranks 1+1, 0+1 and 1+0 | tensor-phase |
| R6 | F9 inside F81 with a non-prime-field base-character parameter: relative trace, distinct absolute/relative characters, and relative-Frobenius covariance on stated sampled operator labels and every basis state | character-conflation, relative-frobenius |

Phases are integers modulo p; traces are reduced exactly modulo the
cyclotomic polynomial using the existing implementation. There are no
floating-point comparisons or tolerances. Finite checks do not prove
arbitrary-rank statements or admit SP-WEYL/SP-TENSOR/SP-TRACE/SP-FROB.
The tests cover the bridge, not a new proof of the inherited theorems.
