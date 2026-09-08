# Frobenius boundary finite checks — 2026-09-08

Status: finite evidence for FRL-ORBIT, FRL-POS, FRL-COMP and FRL-ACTIVE,
all registered as SKETCH pending independent capped review.

Run `python3 theory/checks/frobenius_boundary_check.py`. Preregistered
scope and mutations are in `theory/checks/frobenius_boundary_EXPECTATIONS.md`.
`checks.json` records the actual stdout, exit code and SHA256 of the checker.

| Gate | Result | Mutation and observed failure |
|---|---|---|
| B1: period counts | PASS; cyclic words, F4 and F16 | `--red-count`: wrong period-two count |
| B2: positive weights | PASS; exact rational samples and Jordan derivatives | `--red-weight`: weights no longer sum to one |
| B3: quantum Frobenius | PASS; rank-one Born distinction | `--red-frobenius`: identity loses the distinction |
| B4: composition | PASS; CRT reblocking, ternary shift and coherent multiplicity | `--red-coherence`: cross-orbit matrix entries lost |
| B5: descent | PASS; tower matrices, Kraus completeness and all four tensor branches on matrix units | `--red-decoder`: failure deletion violates completeness |
| B6: active cuts | PASS; field multiplication, overlaps and mixed examples | `--red-overlap`: shared control incorrectly counted twice |

All arithmetic in these probes is exact; no floating-point tolerance is used.
The all-real positivity argument, general cyclic counts and categorical
coherence live in the structured theory shards and are not inferred from
these samples. The first deliberately wrong count was observed to fail before
the proof shards were written. This record is not an independent review.

The labbook section is Section 23, pp. 128--132. Its five pages were rendered
and visually inspected; the real LaTeX build succeeds. Existing layout/font
warnings elsewhere in the labbook were not changed by this work.

The complete repository session-close run passed: 19 green checker
runs and 149 expected nonzero mutation runs, plus the lockstep gate and
real PDF build. The run inventory is frozen in SESSION-CLOSE.json.
