# RUNS — SP-SUM exact falsifier

Date: 2026-09-10. Python 3.12.3, x86_64.
Model: `gpt-5.6-sol`, reasoning setting `xhigh`.

`EXPECTATIONS.md` was written and reported before implementation.  The lane
read no SP-SUM prover artifact or notes and made no trunk change.

Commands were run from the repository root as

    PYTHONDONTWRITEBYTECODE=1 python3 \
      theory/lanes/phantasm-sum/checker/phantasm_sum_check.py <mode>

The optional U2 census imports the installed exact checker artifacts at these
observed hashes:

| imported artifact | SHA-256 |
|---|---|
| `theory/checks/phantasm_stabilizer_check.py` | `ed940fece0058840c8960b4699d8173d4e014629a205e4f0e0c6e58dee069b32` |
| `theory/checks/wh_kappa_check.py` | `4cad037cd7d82e8101af72def4a4abf748f671f68fda93806b24a74ed83892fa` |
| `theory/checks/phantasm_relations_check.py` | `bdfa9952f1b0ea496a8eb07e6c72794d173cf7aa5cd795038d6e3b800ee6cfe2` |

Only the stabilizer checker's exact `actual_families`, projective equality and
cyclotomic ring API are called directly; its imports account for the other two
hashes.

## Reds before first green

All nine help-advertised actual-data mutations were observed before the first
green:

| mode | exit | intended first failure |
|---|---:|---|
| `--red-matrix-unit-loss` | 1 | U1: rectangular words have rank 8 in shape dimension 9 |
| `--red-pure-two-unit` | 1 | U2: `diag(1,1,0)` was inserted into the actual pure census |
| `--red-coherent-tagged` | 1 | U3: actual coherent action erased the cross-summand map |
| `--red-merge-repeated` | 1 | U4: repeated positions/coherent-tagged coordinates were merged |
| `--red-empty-vacuum` | 1 | U5: empty-list zero was confused with rank-zero `C` |
| `--red-dephase-offdiag` | 1 | U6: dephasing retained matrix unit `E_(0,1)` |
| `--red-projection-loss` | 1 | U7: summand-projection Kraus family became incomplete |
| `--red-dephase-average` | 1 | U7: divided dephasing ceased to be unital |
| `--red-normalized-trace` | 1 | U8: normalized blocks replaced ordinary trace |

The first green exited `0` in 4.62 seconds with U1--U8 passing.

## Disabled-comparison survival control

Only U2's actual-census rejection was temporarily disabled while the mutation
still inserted `diag(1,1,0)` into the 360-class pure qutrit family.  The red
then exited `0`:

```text
RED SURVIVED pure-two-unit at U2: diag(1,1,0) is a rank-two coherent sum outside 360 pure qutrit classes
```

The comparison was restored immediately.  The restored mutation again exited
`1` at U2.

## Final validation

All nine mutations were rerun against final source and exited `1` at the same
paths.  Help exposes exactly nine named flags.  Bare `--red` and two
simultaneous modes exit `2` through argparse.

Final ordinary green exited `0` in 4.03 seconds and optimized green exited
`0` in 4.05 seconds.  Both printed:

```text
U1 PASS: 169 actual preparation/adjoint words; full rank for all nine rank pairs
U2 PASS: diag(1,1,0) is a rank-two coherent sum outside 360 pure qutrit classes
U3 PASS: coherent cross block, repeated-position tuple action, composition and dagger
U4 PASS: derived dimensions 16/10,25/11,36/18,81/81 with repeated positions
U5 PASS: typed 4x0,0x4,0x0 maps; empty list 0 differs from rank-zero C
U6 PASS: all 16 matrix units: ten diagonal-block fixed, six off-diagonal killed
U7 PASS: projection completeness, unitality, idempotence and rank-ten tagged range
U8 PASS: all matrix units plus rational dense controls; ordinary trace, not 2 versus 4
GREEN PASS: exact finite controls only; no claim promotion
```

These are finite exact controls.  They do not prove SP-SUM or close DG-RIG.

## Sole checker repair wave

The valid blind verdict's checker findings 1--2 were accepted.  Repair
expectations were appended before changing code.

U2 now checks the imported actual counts `(216,144,360)` and pairwise
projective distinctness of all 360 endomorphism rays before making the
rank-two exclusion statement.  The new truncated-census mutation and the
existing exclusion mutation have separate paths:

```text
RED CAUGHT census-loss at U2: U2a imported-census guard failed: expected 216 Clifford, 144 rank-one, 360 distinct endomorphism rays
RED CAUGHT pure-two-unit at U2: U2b diag(1,1,0) was misclassified as an actual pure stabilizer amplitude
```

U7 now supplies its actual shortened `used` projection tuple to identity,
idempotence and range dephasing calls as well as completeness.  Its intended
first failure remains:

```text
RED CAUGHT projection-loss at U7: U7a summand-projection Kraus family is incomplete
```

With only U7a temporarily disabled, the same shortened family reached the
next actual-operation comparison and exited `1`:

```text
RED CAUGHT projection-loss at U7: U7b block dephasing is not unital
```

For the exit-interface control, only U2a was temporarily disabled while the
actual endomorphism census stayed truncated.  The mutation then survived U2
and exited `0`:

```text
RED SURVIVED census-loss at U2: diag(1,1,0) is a rank-two coherent sum outside 360 pure qutrit classes
```

Both guards were restored.  All ten final help-advertised modes then exited
`1` at their intended gates; the original nine paths were preserved except
for their added U2a/U2b and U7a/U7b subcheck labels.  Final ordinary green
exited `0` in 4.49 seconds and optimized green exited `0` in 3.92 seconds,
with U1--U8 output unchanged.  Help exposes exactly ten supported flags.
