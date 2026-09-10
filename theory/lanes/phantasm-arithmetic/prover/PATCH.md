# String-anchored arithmetic prover handoff

Lane model: `gpt-5.6-sol`, reasoning `xhigh`.

This lane makes no trunk, claim-status, checker or Git changes. The current
D1709/D1710 definitions and SP-FROB D1706/SP-CP dependency are used exactly as
registered.

Copy the proof shards without expanding scope:

- `trace.md` to `theory/symplectic-phantasm/trace.md`;
- `frobenius.md` to `theory/symplectic-phantasm/frobenius.md`;
- `subsystem-models.md` to
  `theory/symplectic-phantasm/subsystem-models.md`;
- `subsystem-decoder.md` to
  `theory/symplectic-phantasm/subsystem-decoder.md`.

In `claims/CLAIMS.md`, anchor on `SP-TRACE`, `SP-FROB`, and `SP-SUBSYS` and
replace only their draft proof pointers with the corresponding integrated
paths using unreviewed prover-pass wording. Preserve all three exact
statements, dependencies and `SKETCH` statuses.

In `claims/PHANTASM-DAG.md`, anchor on the same three headings and replace
`Proof: none` with the real paths. Keep SP-FROB's explicit SP-TRACE dependency
and its SP-CP channel-typing reuse. Do not fill Review, say admitted, remove
Remaining or promote out of dependency order before adjudication.

`LABBOOK-FRAGMENTS.tex` contains exact copies of all three canonical
proposition/Scope blocks followed by descriptive proofs. Anchor their current
propositions in `labbook/sections/symplectic_phantasm_contracts.tex`; add
proof prose only with unreviewed provenance visible, or after adjudication
with final statuses.

`SOURCE-REUSE.md` records exact reuse/source scope. The independent
arithmetic checker remains separately owned; integration requires root-owned
observed red and green records, but finite checks do not prove these claims.

Preserve the boundaries: no characteristic-two half-form, no restarted SvN,
no support-code/subsystem identification, and no global, modular or spectral
conclusion.
