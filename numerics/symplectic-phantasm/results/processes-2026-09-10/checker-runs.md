# RUNS — SP-SCALAR / SP-CP exact falsifier

Date: 2026-09-10. Python 3.12.3, x86_64.
Model: `gpt-5.6-sol`, reasoning setting `xhigh`.

`EXPECTATIONS.md` was written and reported to the coordinator before
`phantasm_process_check.py` existed.  This lane read no process prover
artifact and made no trunk change.

Commands were run from the repository root as

    PYTHONDONTWRITEBYTECODE=1 python3 \
      theory/lanes/phantasm-processes/checker/phantasm_process_check.py <mode>

## Advertised reds before first green

All seventeen modes advertised by the final brief were run before the first
green attempt.  Each exited `1` at its registered gate:

| mode | first mathematical failure |
|---|---|
| `scalar-modulus` | P1: modulus law failed at actual `c=i` matrix-unit data |
| `projective-branch` | P1: projective representative equality was used as CP-map equality |
| `contraction-reverse` | P2: contraction iff disagreed with actual rank-one probabilities |
| `zero-conditioning` | P2: zero-probability conditioning was not explicitly rejected |
| `kraus-adjoint-order` | P3: rectangular adjoint construction had reverse type `Y->X`, expected `X->Y` |
| `block-normalized-trace` | P4: normalized `M2` trace replaced the ordinary block trace |
| `kraus-list-equality` | P5: equal CP maps were distinguished by nonunique lists |
| `composite-index-loss` | P6: intermediate-block path collision lost a Kraus contribution |
| `tensor-tag-order` | P6: actual Cartesian target tags/matrix-unit action disagreed |
| `retained-drop-outcome` | P7: outcome-first external blocks were erased |
| `retained-outcome-factor` | P7: retained trace gained the outcome-count factor |
| `sequential-hide-first` | P8: earlier/later outcome keys were not retained |
| `sequential-pair-order` | P8: later/earlier keys replaced `(o,r)` |
| `tensor-outcome-order` | P9: actual outcome keys were not in listed-factor order |
| `adjoint-direction` | P10: rectangular adjoint retained forward type `X->Y` |
| `adjoint-is-branch` | P10: discard adjoint was incorrectly classified TNI |
| `source-equals-cp` | P11: equal realizations identified distinct D1325 source records |

The zero-conditioning red reached an explicit returned datum and gate failure;
no division was attempted.  Both rectangular-adjoint reds were typed map
comparisons and exited through mathematical gates, not shape exceptions.

## First green attempt and local oracle correction

The first green correctly stopped at P3.  The independent coefficient oracle
assigned rather than accumulated output coefficients as it advanced from
source block `x0` to `x1`, so the later zero input block erased the earlier
contribution.  The concrete witness was input matrix unit `x0:E_(0,0)`:
dense output weights were `9/25` and `16/25`, while the oracle returned zero.

The oracle was repaired to accumulate across source blocks.  No production
Kraus code or expected mathematics changed.  The P3 rectangular mutation
again exited `1`, then green passed P1--P11.  P10 was subsequently given an
explicit `3i/5` rectangular Kraus coefficient, as already required by the
pre-registration; both P10 reds remained at their intended paths.

## Disabled-comparison survival control

Only P2's zero-conditioning acceptance comparison was temporarily disabled,
while the mutation still returned `attempted-zero-conditioning`.  The red then
exited `0`:

```text
RED SURVIVED zero-conditioning at P2: five contraction cases and 28 exact rank-one inputs; zero conditioning rejected
```

This verifies the session-close survival interface.  The comparison was
restored immediately; the restored red again exited `1` at P2.

## Final red and green records

All seventeen modes were rerun against restored final source.  Every mode
exited `1` at the same intended path listed above.  Help exposes exactly those
seventeen named flags and no generic red placeholder.  Bare `--red` and two
simultaneous red flags both exited `2` through argparse.

Final ordinary green exited `0` in 0.55 seconds, and `python3 -O` green exited
`0` in 1.24 seconds.  Both printed:

```text
P1 PASS: 108 exact scalar/matrix-unit comparisons; projective class separated
P2 PASS: five contraction cases and 28 exact rank-one inputs; zero conditioning rejected
P3 PASS: 5 block matrix units, four independent Choi PSD tests, per-input completeness
P4 PASS: ordinary trace channel; block weights 9/25+16/25=1
P5 PASS: {I} equals {(3/5)I,(4/5)I} as maps on four matrix units
P6 PASS: two-path composition, prep/dephase/discard, and full tensor matrix units
P7 PASS: two outcome-first M2 blocks; channel sum and retained trace one
P8 PASS: four earlier/later outcomes with exact probabilities summing to one
P9 PASS: four listed-factor tensor outcomes; independent map action and trace one
P10 PASS: 25 rectangular pairing checks; CP/subunital adjoint and non-TNI discard adjoint
P11 PASS: basis preparations/discard, retained decoder tags, and finer source equality
GREEN PASS: exact finite controls only; no claim promotion
```

All mathematical values are exact `Fraction`/Gaussian-rational data.  Green
is finite negative-binding evidence only and does not prove SP-SCALAR or
SP-CP.

## Sole P3 checker repair wave

The valid blind verdict's OBJ3 requested two real P3 paths.  Their
expectations were appended before implementation.  Both new modes were then
observed before repaired green:

```text
RED CAUGHT kraus-forward-transpose at P3: P3a coefficient-action failed at x1:E_(0,1)
RED CAUGHT kraus-overcomplete at P3: P3c per-input block completeness/strictness failed
```

`kraus-forward-transpose` keeps the actual map typed `X->Y` and transposes the
input only in the real `x1->y0` production component.  It reaches the
off-diagonal matrix-unit comparison.  `kraus-overcomplete` replaces the
actual `(1/2)I_2` component by `2I_2` in the common fixture: all five P3a
coefficient comparisons and four P3b Choi PSD tests pass before the P3c
effect deficit fails.

The repaired green passed P1--P11.  For the required survival control, only
P3c was temporarily disabled while the actual `2I_2` Kraus data remained:

```text
RED SURVIVED kraus-overcomplete at P3: 5 block matrix units, four independent Choi PSD tests, per-input completeness
```

After restoring P3c, all nineteen advertised modes were run.  Every mode
exited `1` at its registered gate; the original seventeen paths were
unchanged, and `kraus-overcomplete` again failed P3c.  Final ordinary green
exited `0` in 0.60 seconds and optimized green exited `0` in 1.25 seconds,
with the P1--P11 output above.  Help exposes exactly nineteen flags; bare and
multiple-red usage exit `2`.
