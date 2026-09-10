# Checker verification — arithmetic interfaces

Date: 2026-09-10. Model: `gpt-5.6-sol`, reasoning `xhigh`.
All mutations below used temporary `/tmp` copies. Installed proof and checker
files were not modified.

## Hashes

| artifact | SHA-256 |
|---|---|
| `trace.md` | `bc866d7dc3ced40e1fc05d267bf2f98698130c849fc69be8ba13d4df67a5a84a` |
| `frobenius.md` | `104797e27041bfa3004402bd3c9204174f426ca6dfa539313ff824d6af880669` |
| `subsystem-models.md` | `03d9466a51f68434f10d8bef7ab63f33e758a015d3d4294722f62e862aef639d` |
| `subsystem-decoder.md` | `a0335511700a45e832ed9ac09f1534413c1771a66a79dae97b813d9bccc0641f` |
| `phantasm_arithmetic_check.py` | `047f6948b9abfa65691213a489a8816a4a9b916d9070c11f73a4bd28d23ffa4c` |
| expectations | `7e3cc7f9ff96bc123d9055bca0095612e7705b076ccada8c63f8f56e7e829f2d` |
| imported `f1_check.py` | `44bd0a30cb54fcd372dd541aa8036efa252c2e3e9decea2cc1d7929c5ef411d2` |
| imported `phantasm_egorov_check.py` | `2fbab5533afa672a734487ba8d9e7ac2ef60075ffddb34377932ad2bc057aa42` |
| imported `wh_kappa_check.py` | `4cad037cd7d82e8101af72def4a4abf748f671f68fda93806b24a74ed83892fa` |
| imported `wh_kappa/ff.py` | `3b23de50f6b3a88909094f97dd21b6d3649f9ad115972f0259fb5ddb15d9944f` |

## Advertised reds before green

`--help` exposed exactly twelve named no-argument red flags and `--root`.

| red | exit and intended path | seconds |
|---|---|---:|
| `absolute-frobenius` | 1 at A5, F81/F9 K-linearity | 0.429 |
| `character-conflation` | 1 at A2, named/fixed character separation | 0.434 |
| `decoder-direction` | 1 at A10, asymmetric retained factor | 0.366 |
| `decoder-normalized-trace` | 1 at A9, first unit `E_(0,0)` | 0.303 |
| `decoder-phase` | 1 at A11, one-sided J phase | 0.276 |
| `decoder-tower-order` | 1 at A12, unit `E_(0,4)` | 0.257 |
| `degenerate-subsystem` | 1 at A8, orthogonality | 0.175 |
| `half-coordinate` | 1 at A6, F27 rank-one covariance | 0.236 |
| `half-form-trace` | 1 at A4, F27 rank-one exponent | 0.368 |
| `rank-zero` | 1 at A7, empty-tensor identity | 0.264 |
| `tower-order` | 1 at A3, wrong F81/F9 trace stage | 0.207 |
| `trace-degree` | 1 at A1, trace image/fibers | 0.217 |

No red reached a wrong gate or exception exit 2.

## Greens

The ordinary command exited 0 in 43.67 seconds; `python3 -O` exited 0 in
45.22 seconds. Both reported A1--A12, including 605 A4 exponent pairs,
648,810 A6 covariance cases, 729 A9 Weyl actions/81 decoder units/729
dualities, and 729 A12 tower matrix units. Peak RSS was below 39 MB.

## Gate simplification and reachability

| gate | independent comparison | red path |
|---|---|---|
| A1 | actual trace image/fibers/witness; separately reduced Gram ranks | trace-degree |
| A2 | additivity/nontriviality and named character versus absolute restriction | character-conflation |
| A3 | separately coded direct/iterated traces and character route | tower-order |
| A4 | E-character/half then trace versus trace/half/base-character; separate sparse product/star/trace | half-form-trace |
| A5 | K-linearity, trace/character invariance, order, semilinear form identity | absolute-frobenius |
| A6 | permutation conjugation action versus Weyl action with both transformed labels | half-coordinate |
| A7 | singleton rank zero, permutation period/inverse, and diagonal-status trace | rank-zero |
| A8 | independent j/k formulas, forms, cross-pairing, and sum census | degenerate-subsystem |
| A9 | imported F3 convention, J Weyl action, Kraus/index decoder, completeness and trace duality | decoder-normalized-trace |
| A10 | three transported inputs versus literal expected retained states | decoder-direction |
| A11 | characteristic functions in exact Eisenstein arithmetic and quadratic phase cancellation | decoder-phase |
| A12 | three separately coded permutations and direct versus sequential partial trace | decoder-tower-order |

A2's green conjunct `actual(witness)==canonical(witness)` is textually a
self-fit because `actual=canonical` in green. The same gate remains substantive:
it separately proves nontriviality and disagreement with the fixed character,
and the mutant changes `actual` and fails the conjunction. A7's matrix-unit
trace check reduces to preservation of diagonal status under an already
verified bijection; it is a valid consequence, not an independent unitarity
test. No other green comparison reduces to identical expressions.

Disabled only at the named comparison, the registered mutations reached the
acceptance path:

| control | result |
|---|---|
| A1 disabled with `trace-degree` | exit 0, `RED SURVIVED` (0.147 s) |
| A6 disabled with `half-coordinate` | exit 0 after 648,810 cases (24.574 s) |
| A9 disabled with normalized decoder | exit 0, `RED SURVIVED` (1.303 s) |
| A12 unit comparison disabled with tower-order | exit 0, `RED SURVIVED` (0.166 s) |

Every A1--A12 gate has an advertised red. The twelve mutations alter distinct
field, character, form, permutation, geometry, phase, or decoder data.

## Independent data mutations

| temporary data change | actual result |
|---|---|
| replace the final F27 trace conjugate `x^9` by a duplicate `x^3` | exit 1 at A1 |
| replace the alternating minus in the symplectic form by plus | exit 1 at A4 sparse product |
| change the complement momentum from `(-v,v)` to `(v,v)` | exit 1 at A8 orthogonality |
| duplicate one Kraus environment row and omit another | exit 1 at A9 completeness |

The ordinary paths for these copies failed nonzero at the displayed gates.

For the negative acceptance control behind objection 2, replacing A6's actual
state census by `()` made the complete checker exit 0 in 3.595 seconds while
printing `A6 PASS: 0 ... cases`. The current unmodified source did execute
648,810 cases; the missing guard concerns future acceptance reachability.

The independent recomputation script used the audited finite-field API but
separate trace, rank, character, subsystem-inverse, and tower formulas. Cross-
library Weyl comparison remained restricted to prime-field F3 encodings.
