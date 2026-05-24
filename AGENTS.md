# AGENTS.md - guidance for AI agents working on arithmetic-quantum-mechanics

This repository is a mathematical research-notebook workspace. Its main
artifact is the sharded LaTeX lab book rooted at `report.tex`; body prose lives
under `report/sections/`. The programme is to investigate possible bridges
between Weil conjectures and zeta functions, arithmetic quantum mechanics,
supersymmetric quantum mechanics, and Kitaev/Levin-Wen/toric-code style
topological lattice models.

Treat this as a reproducible research workspace, not as a casual scripting
repo. The central failure mode to avoid is a plausible mathematical, physical,
or numerical claim with no traceable source, run, convention, or checked
invariant in the lab book's evidence chain.

The connection between the themes above is a research programme, not a settled
claim. Write speculative links as questions, proposals, or hypotheses until a
local source, local derivation, or reproducible run supports them.

## Entry Point

Before adding mathematical content, numerical claims, scripts, or generated
artifacts, read:

1. `AGENTS.md`
2. `README.md`
3. `CONVENTIONS.md`
4. `report/README.md` and `report/SHARD_CATALOG.md`
5. `report.tex` and the relevant shard under `report/sections/`
6. `INDEX.md`
7. `scripts/README.md` before script, run-bundle, CSV, or figure work
8. `data/SCHEMA.md` before CSV-producing or CSV-consuming work
9. The relevant `runs/<YYYY-MM-DD>-<slug>/README.md`
10. The relevant local source manifest under `references/**/SOURCES.md`

Bootstrap exception: agents may improve scaffolding documents such as
`AGENTS.md`, `CONVENTIONS.md`, `INDEX.md`, `data/SCHEMA.md`, report maps, run
README files, and source manifests. Do not add substantive scientific claims
until the relevant source, convention, and reproducibility path exist.

## The Three Laws

**Law 1 - Ground truth before claims.** No definition, theorem, physical
dictionary, normalization, diagnostic result, literature summary, or report
statement is allowed from memory. It must cite a local source, a checked local
derivation, a test, or a reproducible run artifact. If the source is not local
yet, acquire and register it first, or record the gap and stop.

**Law 2 - Conventions before derivations.** Every notational, sign, grading,
gauge, indexing, tolerance, modelling, or data-layout choice must be recorded
in `CONVENTIONS.md` before relying on it.

**Law 3 - Reproducibility is part of the result.** The lab book, code, scripts,
tests, CSVs, figures, source manifests, and run bundles form one research
record. A script that produces data must have a run bundle, schema entry, index
entry, command line, and headline finding. A numerical claim must be backed by
an invariant, known value, source citation, or independently checkable script
output.

If a fast path conflicts with any law, follow the law.

## Rules

0. **The Laws apply always.** A correct-looking formula, spectrum, matrix,
plot, or analogy without provenance is not finished work.

1. **Fail fast, fail loud.** Do not silently coerce notation, skip missing
citations, ignore sentinel caveats, or treat failed checks as warnings.

2. **Be skeptical.** Verify previous-session claims, generated data, OCR or
extraction, summaries, and your own memory against current local files.
Conversation context is not ground truth.

3. **All scientific bugs are convention bugs until proved otherwise.** For
inconsistencies, first check normalization, grading, Frobenius convention,
Hamiltonian sign, supercharge adjoint convention, anyon label order, F/R-symbol
gauge, lattice orientation, boundary conditions, residual normalization, and
CSV sentinel rows.

4. **Acquire sources before using them.** Store new papers, books notes, PDFs,
or source snapshots under `references/<topic>/`, update that topic's
`SOURCES.md` with bibliographic data, DOI/arXiv/URL, retrieval date, access
route, and SHA256, and keep fetched source files append-only. Prefer arXiv,
publisher pages, books the user has access to, or lawful institutional access.
Do not use pirate sources.

5. **Citation format is local and precise.** Mathematical and physical claims
should cite a local path plus page, theorem, equation, section, line number,
test name, or checked script output. Report claims should point to the
producing script and run-bundle artifact through `INDEX.md`.

6. **Docs move with content.** If a change introduces a term or convention,
update `CONVENTIONS.md`. If it adds or changes a script/run, update
`scripts/run_all.jl`, the run README, `INDEX.md`, and `data/SCHEMA.md` in the
same change. If it changes report conclusions, update a report shard or record
the deferred report work in `HANDOFF.md`.

7. **Use red-green or port-and-verify.** For new code, write or identify the
failing invariant first, make it pass, then refactor. For porting mathematics
from a paper, port faithfully, encode the invariant, and verify against
examples, independent computations, or tests where feasible.

8. **"Runs without errors" is not a test.** A useful test asserts a
mathematical or physical invariant: Euler factor identities, functional
equation normalization, Betti-number or trace checks, supercharge nilpotence,
Hamiltonian positivity, Witten-index stability, fusion-rule consistency,
projector idempotence, commutation relations, or agreement with a cited
example.

9. **Use established tools, but verify the local contract.** Julia, Sage, GAP,
and other CAS or numerical tools are welcome. Still test the project-specific
convention layer around any library result.

10. **Maintain the lab book.** `report.tex` is the master include-order file.
Body prose belongs in `report/sections/*.tex` and is mapped by
`report/README.md` plus `report/SHARD_CATALOG.md`. Do not commit rebuilt PDF
or LaTeX artifacts.

11. **Respect run-bundle discipline.** Create
`runs/<YYYY-MM-DD>-<slug>/{data,figures}/` and its `README.md` before writing a
producing script. Scripts must write only through project helpers or their
equivalent and must never write generated data to top-level `data/` or
`figures/`.

12. **Keep generated data intentional.** Do not blindly stage or copy all of
`runs/`. Review CSV/SVG diffs and preserve `#`-prefixed CSV sentinel lines.

13. **Keep files shardable and indexed.** Keep report shards near 200 lines
when possible. Update `INDEX.md` whenever adding scripts, outputs, figures, or
run bundles.

14. **Track work with Beads when initialized.** If `.beads/` exists, use `bd`
for persistent work tracking. Do not maintain persistent project state in ad
hoc TODO lists. Do not run multiple `bd` commands in parallel; the embedded
backend uses an exclusive lock.

15. **No remote automation by default.** The project convention is local
validation. Do not add `.github/workflows/` or other remote automation unless
the user asks for it.

16. **Session close discipline.** Before ending a substantive session, run the
relevant validation commands, update manifests/conventions/schema/index/report
handoff as needed, and check the working tree if this directory has been
initialized as a git repo.

## Project-Specific Risks

- **Zeta normalizations are convention-sensitive.** Record the variety or
scheme, base field, Euler factor convention, local/global normalization,
Frobenius direction, variable names, and functional-equation shift before using
a zeta-function formula.
- **Cohomological trace formulas need grading discipline.** Record whether a
trace is on cohomology, compact-support cohomology, chain-level complexes, or a
finite approximation. Alternating signs and Tate twists must be explicit.
- **Arithmetic-QM analogies can overstate.** Distinguish a literal Hilbert
space/Hamiltonian construction from a formal spectral analogy or dictionary.
- **Supersymmetric QM signs matter.** Record the grading, adjoint, domain,
boundary conditions, supercharge normalization, and Hamiltonian convention
before using Witten-index or ground-state claims.
- **Toric-code and Levin-Wen data are lattice-convention-sensitive.** Record
orientation, star/plaquette naming, boundary type, fusion category, pivotal or
spherical convention, and whether the model is a quantum double, Drinfeld
center, or string-net construction.
- **Finite precision is not exact evidence.** Exact arithmetic from Sage/GAP or
symbolic certificates should be used where feasible; floating diagnostics must
declare tolerance, norm, denominator, and independent invariant.

## Layout

Use this layout:

- `report.tex` plus `report/sections/*.tex` for the sharded lab book
- `report/README.md` and `report/SHARD_CATALOG.md` for report navigation
- `references/<topic>/SOURCES.md` for source provenance
- `scripts/{arithmetic,susy,lattice_codes,bridges}/` for producers and helpers
- `scripts/run_all.jl` as the canonical local driver
- `runs/<YYYY-MM-DD>-<slug>/{data,figures}/` for generated artifacts
- `data/SCHEMA.md` for CSV column contracts
- `INDEX.md` for script/output/report navigation
- `docs/NUMERICAL_NOTES.md` and `HANDOFF.md` for session-facing research state
