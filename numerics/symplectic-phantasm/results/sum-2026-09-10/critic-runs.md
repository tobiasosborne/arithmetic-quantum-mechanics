# Checker verification — SP-SUM

Date: 2026-09-10. Model: `gpt-5.6-sol`, reasoning `xhigh`.
All modified checkers below were temporary `/tmp` copies. The installed source
was not changed.

## Frozen files and imported dependency

| file | SHA-256 |
|---|---|
| `theory/symplectic-phantasm/sum.md` | `11ce000439fa096c2264bc9dca3f38953e198d74c940ade7df94c8761f6c1f06` |
| `theory/checks/phantasm_sum_check.py` | `655af7eadda3991ab2eebabf14d21b0ea255bf35337e5ea12e6507e9a6b742fd` |
| `theory/checks/phantasm_sum_EXPECTATIONS.md` | `ab5d9ed46580e51b5bfbac1f76299964b304f90d463ec7d465b5df22f5dc7a85` |
| imported `phantasm_stabilizer_check.py` | `ed940fece0058840c8960b4699d8173d4e014629a205e4f0e0c6e58dee069b32` |
| imported `wh_kappa_check.py` | `4cad037cd7d82e8101af72def4a4abf748f671f68fda93806b24a74ed83892fa` |

`--help` exposed exactly nine no-argument red flags and `--root`.

## Advertised red runs, before green

Command form:

    python3 theory/checks/phantasm_sum_check.py --red-<name>

| flag | exit | observed path | seconds |
|---|---:|---|---:|
| `coherent-tagged` | 1 | `RED CAUGHT ... at U3` | 0.375 |
| `dephase-average` | 1 | `RED CAUGHT ... at U7` | 0.273 |
| `dephase-offdiag` | 1 | `RED CAUGHT ... at U6`, first witness `E_(0,1)` | 0.283 |
| `empty-vacuum` | 1 | `RED CAUGHT ... at U5` | 0.262 |
| `matrix-unit-loss` | 1 | `RED CAUGHT ... at U1`, rank 8 of 9 | 0.282 |
| `merge-repeated` | 1 | `RED CAUGHT ... at U4` | 0.324 |
| `normalized-trace` | 1 | `RED CAUGHT ... at U8` | 0.255 |
| `projection-loss` | 1 | `RED CAUGHT ... at U7`, completeness | 0.298 |
| `pure-two-unit` | 1 | `RED CAUGHT ... at U2` | 5.983 |

No mutant failed at a wrong gate and no exception path produced exit 2.

## Green runs

    python3 theory/checks/phantasm_sum_check.py

Exit 0 in 5.37 seconds: U1 through U8 and final green all passed.

    python3 -O theory/checks/phantasm_sum_check.py

Exit 0 in 4.40 seconds with the same U1--U8 report. The checker does not rely
on Python assertions.

## Symbolic gate simplification

| gate | non-tautological comparison | registered red reachability |
|---|---|---|
| U1 | preparation/adjoint words versus literal rectangular units, then exact row rank versus shape dimension | deleting a rank-two preparation gives rank 8 rather than 9 |
| U2 | exact imported cyclotomic census versus a fixed diagonal; independent rational matrix-unit reconstruction | inserting the diagonal gives a direct ray match |
| U3 | dense block placement versus tuple action on every source basis vector; separate composition and dagger formulas | diagonal-only realization erases the explicit cross block |
| U4 | ranks of enumerated coherent/tagged coordinate families versus dimensions from the unmodified ordered list | merging equal-rank positions changes actual dimensions |
| U5 | realized empty block arrows versus independently typed empty rectangles; dagger/product and singleton-H0 controls | assigning dimension one to the empty list changes every shape |
| U6 | projection formula on all matrix units versus an owner-index oracle | added `P0 A P1` survives on `E_(0,1)` |
| U7 | projection products versus identity; map action versus identity/idempotence and independently enumerated tagged range | loss fails completeness; averaging fails unitality first |
| U8 | dephased block-trace sum versus ordinary coherent trace | normalized block trace changes the identity from 4 to 2 |

At U3 lines 395--397, the green equality `actual == realize(cross)` is
textually identical when no mode is active. Its rank conjunct only detects
erasure. I did not count this as an independent oracle. U3 remains substantive
because lines 399--415 compare dense placement with a separately implemented
tuple action on a larger repeated-position fixture, then compare independent
composition and dagger constructions.

Every U1--U8 gate has at least one advertised mutation. The two U7 reds are
not bit-identical: projection loss changes a completeness sum; averaging
changes all dephasing outputs and first fails unitality.

## Independent data mutations on copies

Starting from the frozen source, I changed one data-generating expression per
copy and ran the ordinary green path with `--root`:

| mutation | exit/path | meaning |
|---|---|---|
| replace `j+amount` by `j-amount` in qutrit shifts | 1, U1 wrong entry pattern | basis-label sign is checked |
| place every block at source offset zero | 1, U3 tuple-action disagreement | block offsets are checked independently |
| retain only the first coordinate of each summand projection | 1, U6 at `E_(1,2)` | projection support is checked by the owner oracle |
| omit the last diagonal entry in ordinary `rtrace` | 1, U8 | ordinary coherent trace is compared independently |

## Survivors and acceptance paths

- Disabling only U6's matrix-unit equality made the actual
  `--red-dephase-offdiag` data mutation reach `RED SURVIVED` and exit 0.
- Disabling only U7's completeness comparison made
  `--red-projection-loss` reach `RED SURVIVED` and exit 0. This also exposed
  that the shortened family is not passed into the later dephasing calls.
- Truncating U2's local census to `endos[:1]` left the entire green run at exit
  0 and still printed “outside 360 pure qutrit classes.” This is the false
  acceptance recorded as objection 1.

The exact independent recomputation script in `/tmp/sp_sum_independent.py`
used only `Fraction` arithmetic for coordinate/block calculations and an
independent cross-multiplication predicate for the imported cyclotomic census.
It reported the 169 words, all four dimension rows, ten/six dephasing units,
typed empty shapes, 360 current census rays, and zero diagonal-ray hits.
