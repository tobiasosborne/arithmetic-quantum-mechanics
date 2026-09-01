Lane model: gpt-5.6-sol, reasoning xhigh, codex exec.

## Objection dispositions

| objection | disposition |
|---|---|
| OBJ-1 | Replaced `FCR-REG` by the clause-level theorem in `fcr-local.md` §9; it lists recovered clauses and expressly excludes the frame-preserving torsor plus the unproved form/symmetry clauses. The `PATCH.md` row matches and remains PROVED. |
| OBJ-2 | Added `S({}_RR)=Ann(𝔪)` with both inclusions as `FCR-GEN <1>1.<2>3`; the old conclusion is renumbered `<2>4`. |
| OBJ-3 | Closed all nine proposed claim rows in `PATCH.md`, explicitly binding each finite local ring and every character/cocycle/vector variable used. |
| OBJ-4 | Renamed checker ring order to `n=|R|` in code and both documents; `q` is reserved for `|κ|`, and cyclotomic order is `d`/`phase_order`. |
| OBJ-5 | Registered `--red-g6-arena-confusion` and `--red-profile-drop-identity` in code and the reachability matrix; G6 and G11 now have independent mutations. |

## Observed checker exits

| mode | exit | registered first gate |
|---|---:|---|
| green | 0 | all G1--G11 pass |
| `--red-nongenerating` | 1 | G5 |
| `--red-transpose` | 1 | G2 |
| `--red-frobenius-blind` | 1 | G1 |
| `--red-free-only` | 1 | G7 |
| `--red-torsor` | 1 | G8 |
| `--red-dim` | 1 | G5 |
| `--red-halfweyl-drop` | 1 | G9 |
| `--red-g6-arena-confusion` | 1 | G6 |
| `--red-profile-drop-identity` | 1 | G11 |

`08_local_rings.tex` compiles against the trunk preamble (standalone test exit 0).
The orchestrator must add `\input{sections/08_local_rings}` to `labbook/main.tex`.

Deviations from FIX DEMAND: none.
