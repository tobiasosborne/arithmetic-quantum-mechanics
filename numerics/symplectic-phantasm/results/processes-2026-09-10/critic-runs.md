# Checker verification record

Date: 2026-09-10. Python 3.12.3, x86_64.

## Frozen identity

```text
2a64f59f814b99760af460a3f744ef96f83562beef55a5b4e34d30dcab87d1d0  theory/checks/phantasm_process_check.py
b074c4abbcbafe657720cb9f3d4b6f1a8d39f0bb39590e603dfb2a7c5de82002  theory/checks/phantasm_process_EXPECTATIONS.md
```

## Green

Exit `0`, wall time approximately 0.077 seconds.

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

## All help-advertised red modes

| mode | exit | intended observed failure |
|---|---:|---|
| `--red-scalar-modulus` | 1 | P1 scalar modulus at `c=i` |
| `--red-projective-branch` | 1 | P1 projective amplitude used as CP equality |
| `--red-contraction-reverse` | 1 | P2 contraction iff |
| `--red-zero-conditioning` | 1 | P2 explicit zero conditioning rejection |
| `--red-kraus-adjoint-order` | 1 | P3 reverse type used as forward type |
| `--red-block-normalized-trace` | 1 | P4 ordinary trace replaced in M2 block |
| `--red-kraus-list-equality` | 1 | P5 list equality substituted for map equality |
| `--red-composite-index-loss` | 1 | P6 intermediate block path lost |
| `--red-tensor-tag-order` | 1 | P6 Cartesian target tags reversed |
| `--red-retained-drop-outcome` | 1 | P7 external outcome block erased |
| `--red-retained-outcome-factor` | 1 | P7 retained trace multiplied by two |
| `--red-sequential-hide-first` | 1 | P8 earlier outcome hidden |
| `--red-sequential-pair-order` | 1 | P8 later/earlier pair emitted |
| `--red-tensor-outcome-order` | 1 | P9 listed-factor pair reversed |
| `--red-adjoint-direction` | 1 | P10 forward rather than reverse type |
| `--red-adjoint-is-branch` | 1 | P10 discard adjoint misclassified TNI |
| `--red-source-equals-cp` | 1 | P11 source equality replaced by CP equality |

Every process printed `RED CAUGHT <mode> at <intended gate>`. Help exposed no
generic `--red` token. The modes run only their registered gate, so there was
no earlier-gate masking.

## Independent `/tmp` mutations

1. Actual P3 fixture `(1/2)I_2 -> 2I_2`: P1/P2 passed, then exit `1` at
   `P3 FAIL: per-input block completeness/strictness failed`.
2. Actual P4 channel weight `3/5 -> 2/5`: P1--P3 passed, then exit `1` at
   `P4 FAIL: rational block fixture is not a channel`.
3. Disabled only P10's final non-TNI classification guard, retaining the real
   `--red-adjoint-is-branch` data: output was
   `RED SURVIVED adjoint-is-branch at P10: 25 rectangular pairing checks; CP/subunital adjoint and non-TNI discard adjoint`, exit `0`.

All copies were under `/tmp`; installed sources were unchanged.
