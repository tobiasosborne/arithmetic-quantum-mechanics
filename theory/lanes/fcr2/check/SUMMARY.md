Lane model: gpt-5.6-sol, reasoning xhigh, codex exec

# FCR-2 check-lane summary

Green: `python3 fcr2_beta_check.py` exited `0`; measured wall time `34.94 s`.
Exact explicit ring tables, integer/`Z[zeta8]` arithmetic, no floats or tolerances.

## Discovered headline data

- `Z4`: 2 centre-fixed and 2 abstract `H_beta` classes, sizes `48:16`.
  `epsilon` value set is `{+1}` for either generating character; it is class-constant but does **not** separate the classes.
- `F2[e]/e2`: 2 centre-fixed and 2 abstract classes, sizes `48:16`.
  `epsilon` value set is `{+1}` for either generating character; it is class-constant but does **not** separate the classes.
- `F2,F4`: class sizes `6:2` and `40:24`; `epsilon={+1,-1}` separates, reproducing the field regression.
- `Z8,F2[t]/t3`: class sizes `384:128`; `epsilon={+1,-1}` separates.
- `GR(4,2)`: the deterministic 128-beta sample has two signature populations `89:39`; this is not a complete class census.  All 4096 betas have `epsilon=+1` for all 12 generating characters.
- Non-Frobenius probe: 2 abstract/centre-fixed classes of sizes `384:128`, but `Gen=empty` by all-character exhaustion.
- Order profiles distinguish both observed types at every seed; power-map and centre/quotient invariants independently corroborate them.
- No seed has an antisymmetric admissible cocycle.

## Actually run red exits

- `--red-fake-epsilon`: `1` (G4); `--red-collapse`: `1` (G3).
- `--red-transpose`: `1` (G1); `--red-halfweyl`: `1` (G7).
- `--red-profile`: `1` (G3); `--red-field`: `1` (G5).
- `--red-square`: `1` (G2); `--red-model-sign`: `1` (G6).
- `--red-frobenius-blind`: `1` (G8).
