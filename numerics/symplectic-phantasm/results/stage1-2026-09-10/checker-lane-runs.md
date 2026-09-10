# RUNS — SP-EGOROV / affine SP-TENSOR falsifier

Date: 2026-09-10. Python 3.12.3, x86_64. Base commit `853c564` with
concurrent coordinator changes left untouched. Model: `gpt-5.6-sol`, `xhigh`.

The pre-registration in `EXPECTATIONS.md` was written and reported to the
coordinator before `egorov_tensor_check.py` was created. All advertised red
modes below were then run before the first green run.

Commands were run from this lane with

    python3 egorov_tensor_check.py \
      --root /home/tobias/Projects/arithmetic-quantum-mechanics <mode>

## First red matrix, before green

The checker-internal elapsed time ends at the intended failing gate. The wall
time includes interpreter startup and import of the existing exact arithmetic
library.

| mode | exit | first output failure | intended-gate output | checker time | wall time |
|---|---:|---|---|---:|---:|
| `--red-sp-enumeration` | 1 | `E1 FAIL: symplectic census is 48, expected 24` | `CAUGHT AT INTENDED GATE E1` | 0.000 s | 127 ms |
| `--red-semidir-order` | 1 | `E2 FAIL: composition mismatch ...` | `CAUGHT AT INTENDED GATE E2` | 0.036 s | 143 ms |
| `--red-alpha-phase` | 1 | `E3 FAIL: alpha composition mismatch ...` | `CAUGHT AT INTENDED GATE E3` | 0.981 s | 1,081 ms |
| `--red-translation-sign` | 1 | `E4 FAIL: translation covariance failed at t=(0, 1),v=(1, 0)` | `CAUGHT AT INTENDED GATE E4` | 1.712 s | 1,864 ms |
| `--red-fourier-sign` | 1 | `E5 FAIL: Fourier covariance failed at (0, 1)` | `CAUGHT AT INTENDED GATE E5` | 2.024 s | 2,165 ms |
| `--red-shear-half` | 1 | `E6 FAIL: shear covariance failed at r=1,v=(1, 0)` | `CAUGHT AT INTENDED GATE E6` | 2.197 s | 2,321 ms |
| `--red-zero-qudit` | 1 | `E7 FAIL: rank-zero Hilbert dimension claimed as 3` | `CAUGHT AT INTENDED GATE E7` | 2.160 s | 2,293 ms |
| `--red-f9-character` | 1 | `E8 FAIL: F9 character table (0,2,1,0,2,1,0,2,1) != (0,0,0,1,1,1,2,2,2)` | `CAUGHT AT INTENDED GATE E8` | 2.156 s | 2,318 ms |
| `--red-tensor-phase` | 1 | `E9 FAIL: rank-two affine naturality failed` | `CAUGHT AT INTENDED GATE E9` | 3.244 s | 3,420 ms |

For each row after E1, stdout also showed every preceding gate as `PASS`.
The E9 mutation, for example, passed E1--E8 before E9 fired. Its E8 aggregate
was then displayed as 13,451; the two-count reporting repair described below
had not yet been made. The shell loop itself exited zero only because it
recorded each expected checker exit instead of using `set -e`.

## First green run

Exit `0`, checker time 3.204 s, wall time approximately 3.4 s.

```text
phantasm_egorov_check mode=green
exact arithmetic only; finite success does not prove or promote a claim
E1 PASS: 24 symplectic matrices, 216 affine arrows; 1944 form checks [1944 checks; 0.002s]
E2 PASS: 216 inverses; 46,656 products and 419,904 point checks [420552 checks; 0.823s]
E3 PASS: 9 identity, 1,944 star, 17,496 product and 419,904 composition cases [439353 checks; 0.908s]
E4 PASS: 81 independent monomial conjugation equalities [81 checks; 0.001s]
E5 PASS: F*F=3I and 9 exact Fourier covariance equalities [10 checks; 0.001s]
E6 PASS: 2 unitary and 18 exact shear covariance checks [20 checks; 0.000s]
E7 PASS: literal rank-zero affine/Weyl object and both tensor units [21 checks; 0.000s]
E8 PASS: psi_u table, 81 additivity, 6,561 Weyl products, 6,561 translations, 81 Fourier and 162 shear covariances [13451 checks; 0.161s]
E9 PASS: 81 operator tensors, 81 swaps and 3,779,136 all-factor affine naturality cases [3779298 checks; 1.308s]
PASS: SP-EGOROV / affine SP-TENSOR finite falsifier [3.204s total]
```

The E8 count label above came from the first green executable and omitted two
table assertions from its displayed aggregate, though both assertions ran.
That reporting defect was repaired immediately by changing only the aggregate
from 13,451 to 13,453; no mathematical test changed. The post-repair green run
is recorded below.

## Optimized-mode green run before the reporting repair

Command:

    PYTHONDONTWRITEBYTECODE=1 python3 -O egorov_tensor_check.py \
      --root /home/tobias/Projects/arithmetic-quantum-mechanics

Exit `0`, checker time 3.290 s before the aggregate-only repair. Every gate
and mathematical comparison matched the first green run. A final ordinary
green rerun after that reporting repair is required and recorded at the end
of this file.

## Destination-layout import probe

An ephemeral directory under `/tmp` was given the intended layout
`theory/checks/{phantasm_egorov_check.py,wh_kappa_check.py}`. Running
`phantasm_egorov_check.py --red-sp-enumeration` without `--root` located the
adjacent exact arithmetic library and exited 1 at E1 as intended (0.000 s
checker time). This confirms the proposed trunk copy resolves its import.

## Final post-reporting-repair run

Self-review replaced E7's literal zero-arrow assertion with empty-coordinate
enumeration, point action, composition, exhaustive inverse search and an
independently constructed one-dimensional Weyl operator. Before green, the
revised `--red-zero-qudit` again exited 1 at intended E7 after E1--E6 passed
(1.737 s checker time). The following green then exited `0` in 3.172 s
(approximately 3.4 s wall time).

```text
phantasm_egorov_check mode=green
exact arithmetic only; finite success does not prove or promote a claim
E1 PASS: 24 symplectic matrices, 216 affine arrows; 1944 form checks [1944 checks; 0.004s]
E2 PASS: 216 inverses; 46,656 products and 419,904 point checks [420552 checks; 0.836s]
E3 PASS: 9 identity, 1,944 star, 17,496 product and 419,904 composition cases [439353 checks; 0.893s]
E4 PASS: 81 independent monomial conjugation equalities [81 checks; 0.001s]
E5 PASS: F*F=3I and 9 exact Fourier covariance equalities [10 checks; 0.001s]
E6 PASS: 2 unitary and 18 exact shear covariance checks [20 checks; 0.000s]
E7 PASS: enumerated rank-zero affine/Weyl object and both tensor units [27 checks; 0.000s]
E8 PASS: psi_u table, 81 additivity, 6,561 Weyl products, 6,561 translations, 81 Fourier and 162 shear covariances [13453 checks; 0.161s]
E9 PASS: 81 operator tensors, 81 swaps and 3,779,136 all-factor affine naturality cases [3779298 checks; 1.277s]
PASS: SP-EGOROV / affine SP-TENSOR finite falsifier [3.172s total]
```

Displayed gate aggregates total 4,654,738 checks. Several aggregate rows count
the named exhaustive families rather than every scalar subassertion inside
their setup guards.
