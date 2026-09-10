# RUNS — arithmetic-interface exact falsifier

Date: 2026-09-10. Python 3.12.3, x86_64.
Model: `gpt-5.6-sol`, reasoning setting `xhigh`.

`EXPECTATIONS.md` was frozen and reported before implementation.  The lane
read no arithmetic prover artifact or notes and made no trunk change.

Commands were run from the repository root as

    PYTHONDONTWRITEBYTECODE=1 python3 \
      theory/lanes/phantasm-arithmetic/checker/phantasm_arithmetic_check.py <mode>

## Imported exact APIs

| artifact | use | SHA-256 |
|---|---|---|
| `theory/checks/wh_kappa/ff.py` | F27/F81 polynomial-table `GF` | `3b23de50f6b3a88909094f97dd21b6d3649f9ad115972f0259fb5ddb15d9944f` |
| `theory/checks/wh_kappa_check.py` | `CycRing` root convention and monomial field class | `4cad037cd7d82e8101af72def4a4abf748f671f68fda93806b24a74ed83892fa` |
| `theory/checks/phantasm_egorov_check.py` | F3 `weyl_mono` convention comparison | `2fbab5533afa672a734487ba8d9e7ac2ef60075ffddb34377932ad2bc057aa42` |
| `theory/checks/f1_check.py` | exact finite Abelian F3 phase-label set | `44bd0a30cb54fcd372dd541aa8036efa252c2e3e9decea2cc1d7929c5ef411d2` |
| `theory/checks/phantasm_reuse_check.py` | unchanged prior R6 evidence only; not imported | `3e4197ab7e98dd26ae6bce0868b56f5270c5b1bf185d1d76dc253be89a333f43` |

The two GF implementations use different verified polynomial presentations in
degrees three/four, so extension arithmetic comes only from `wh_kappa/ff.py`.
The monomial cross-check is deliberately confined to F3, where encodings
agree.  No element label is silently transferred between nonidentical field
presentations.

## All reds before first green

All twelve named actual-data modes were observed before the first green:

| mode | exit | intended first failure |
|---|---:|---|
| `trace-degree` | 1 | A1: F27 trace image/kernel/fibers or trace-one witness |
| `character-conflation` | 1 | A2: nonstandard F9 character versus fixed absolute character |
| `tower-order` | 1 | A3: wrong F81/F9 stage misses the tower trace/F9 target |
| `half-form-trace` | 1 | A4: F27/F3 rank-one half-form exponent |
| `absolute-frobenius` | 1 | A5: F81 cube is not F9-linear |
| `half-coordinate` | 1 | A6: F27 rank-one sparse covariance |
| `rank-zero` | 1 | A7: empty tensor is not the identity on C |
| `degenerate-subsystem` | 1 | A8: proposed bad subsystem/complement is not orthogonal |
| `decoder-normalized-trace` | 1 | A9: ordinary decoder differs at `E_(0,0)` |
| `decoder-direction` | 1 | A10: correlated/asymmetric decoder output |
| `decoder-phase` | 1 | A11: one-sided J phase fails cancellation |
| `decoder-tower-order` | 1 | A12: direct/iterated decoder differs at `E_(0,4)` |

The first green passed A1--A12.  Subsequent self-review replaced A3's repeated
character call by the direct character route
`Tr_81/3(u*x)`, made the D1710 complement route explicit as separate
`J_perp` then `J_(ell j)` functions, and replaced repeated dense tower-unit
decoding by an independent index formula.  A9's F3 monomial action, A8's
Abelian labels and A11's root table were then cross-checked against the pinned
imports.  Affected reds were rerun before final green.

## Disabled-guard survival controls

Each listed actual mutation was retained while only its associated acceptance
statement was temporarily disabled.  All four then survived their target gate
with exit `0`:

```text
RED SURVIVED trace-degree at A1: F27 trace image 3/kernel 9/fibers 9; Gram ranks 0,6,12
RED SURVIVED half-coordinate at A6: 648810 exhaustive-rank1/sparse-rank2 monomial covariance cases
RED SURVIVED decoder-normalized-trace at A9: 729 Weyl actions, 81 decoder units, completeness/trace and 729 dualities
RED SURVIVED decoder-tower-order at A12: explicit D1710 M3 compatibility, 729 matrix units and three tower states
```

Every guard was restored.  All twelve reds were then rerun and again exited
`1` at the intended paths above.

## Final greens and usage

Final ordinary green exited `0` in approximately 45.45 seconds; optimized
green exited `0` in approximately 41.61 seconds.  A6's 648,810 exact sparse
tuples dominate runtime.  No dense `729x729` or `6561x6561` matrix is
allocated.  Both greens printed:

```text
A1 PASS: F27 trace image 3/kernel 9/fibers 9; Gram ranks 0,6,12
A2 PASS: nonstandard F9 character and F81 composite separated; F27 restriction trivial
A3 PASS: 81 direct/iterated trace and nonstandard-character comparisons
A4 PASS: 605 half-form exponent pairs plus sparse product/star/unit/trace
A5 PASS: F27 cube/order3 and F81 ninth-power/order2 K-linearity/invariance
A6 PASS: 648810 exhaustive-rank1/sparse-rank2 monomial covariance cases
A7 PASS: rank-zero identity plus 256 rank1/2 permutation-channel controls
A8 PASS: non-coordinate j,k symplectic/orthogonal/injective with 81 unique sums
A9 PASS: 729 Weyl actions, 81 decoder units, completeness/trace and 729 dualities
A10 PASS: asymmetric product, classical correlation and Bell density decoder direction
A11 PASS: 27 Weyl-characteristic restrictions and exact J phase cancellation
A12 PASS: explicit D1710 M3 compatibility, 729 matrix units and three tower states
GREEN PASS: exact finite controls only; no claim promotion
```

Before the repair, help exposed exactly twelve named red flags. Bare `--red` and multiple-red
usage exit `2`.  Finite success does not prove any canonical claim.

## Sole A6 checker repair wave

The valid blind verdict's only checker finding was accepted. A6 now rejects
empty state collections and asserts the actual per-field/rank execution tuple

    (19683, 12393, 531441, 85293)

whose sum is 648810. New `covariance-census-loss` removes the last actual F81
rank-two state and executes every remaining comparison. It exited `1` at A6:

```text
RED CAUGHT covariance-census-loss at A6: A6 covariance census (19683, 12393, 531441, 85280), expected per-field/rank (19683, 12393, 531441, 85293)
```

Green with the intact state sets again printed exactly 648810 and exited `0`.
No required sparse label or state family was reduced.

For the requested temporary-copy control, only the new tuple guard was
disabled. The same truncated actual state collection then completed and
exited `0`:

```text
RED SURVIVED covariance-census-loss at A6: 648797 exhaustive-rank1/sparse-rank2 monomial covariance cases
```

The lane source itself was never changed for this control. Final code is
restored and frozen; root owns the installed thirteen-red and final normal/-O
battery. The previous twelve mutation paths and sparse scope are unchanged.
