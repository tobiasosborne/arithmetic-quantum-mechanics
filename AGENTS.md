# Arithmetic quantum mechanics — agent entry point

The active quest is **The Hunting of the Symplectic Phantasm**, adopted by
Tobias on 2026-09-09. Read `CLAUDE.md`, `PRD.md`, the opening of `HANDOFF.md`,
and `docs/research-plans/symplectic-phantasm.md` before substantive work.

The initial guidance is `docs/research-plans/fundamentals-two-categories.md`.
It is a record of ideas and an earlier assistant's assessment, not evidence.
The new SOP is **sober, accretive, and careful**: retrieve primary sources
(TeX preferred), verify and register their actual scope, construct explicit
definitions, then discharge a concrete argument DAG in dependency order.
Run the quest's contract checker as well as the existing labbook gates.
A passing contract check is not a mathematical proof.

The contract command is `python3 theory/checks/phantasm_contract_check.py`.
On a fresh checkout, first run `python3 scripts/fetch-phantasm-sources.py`;
source bodies are deliberately ignored by Git, and the checker verifies
their recorded hashes. The next bounded proof cluster is SP-WEYL, then
SP-EGOROV and SP-TENSOR, as specified in the quest work order. The
2026-09-10 reuse correction is binding: SP-WEYL is a corollary of the
admitted finite-abelian F1-REAL, and SP-TENSOR reuses F1-FUNCT. Consult the
DAG's Inherited/Reuse/Remaining fields and each definition's Reuses/Delta
before proposing new foundational work. The bridge draft and exact
conversion probes are in `theory/symplectic-phantasm/reuse.md` and
`theory/checks/phantasm_reuse_check.py`.

Preserve admitted earlier results and their provenance. The composite
counting-boundary programme and FCR-2 are paused; historical work orders do
not authorize resuming them. The relation to the Riemann hypothesis is a
motivation, not a result. Do not silently adopt assertions from the initial
guidance, especially about quantization of relations, phase quotients,
Gaussian channels, scalar restriction, Fock space, or modular flow.

`definitions.md`, `notation.md`, `claims/CLAIMS.md`, and `refs/LEDGER.md` are
the single sources. The PDF in `labbook/` is the product. The capped
prove–attack–repair rule and honest statuses remain binding; finite tests
and literature analogies do not promote claims. `v0.1/` supplies hints only.
