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
| R4 | Exact operator Gram, actual zero-label operator versus the identity, and entry-derived normalized matrix traces versus the coefficient functional on every Weyl label; rank-zero configuration included | trace-normalization, vacuum |
| R5 | Symmetrizing cochain and inherited configuration-product tensor for F3 ranks 1+1, 0+1 and 1+0 | tensor-phase |
| R6 | F9 inside F81 with a non-prime-field base-character parameter: relative trace, distinct absolute/relative characters, and relative-Frobenius covariance on stated sampled operator labels and every basis state | character-conflation, relative-frobenius |

Phases are integers modulo p; traces are reduced exactly modulo the
cyclotomic polynomial using the existing implementation. There are no
floating-point comparisons or tolerances. Finite checks do not prove
arbitrary-rank statements or admit SP-WEYL/SP-TENSOR/SP-TRACE/SP-FROB.
The tests cover the bridge, not a new proof of the inherited theorems.

## R4 repair after the single Weyl review — 2026-09-10

The critic found that the old family-size and `dim/dim` subchecks were
constructed identities. Retain the substantive Gram computation and replace
those subchecks by an independent comparison of the actual zero-label
operator with the identity matrix, followed by matrix traces computed from
the diagonal entries of every operator and compared with D1703's coefficient
functional. Divide those actual cyclotomic trace coefficients by the Hilbert
dimension using exact fractions.

The vacuum defect changes the phase of the actual rank-zero operator at
the R4 gate, so the identity comparison must reject it. The normalization
defect changes the expected coefficient functional on the zero label from
one to the Hilbert dimension, testing confusion with ordinary trace; a
positive-rank identity witness must reject it. Neither defect deletes a
preconstructed operator list or merely changes a selected denominator.
These revised expectations are recorded before executing the repaired gate.
