# CONVENTIONS - arithmetic-quantum-mechanics

<!--
ROLE: Notational, sign, grading, gauge, modelling, tolerance, and data-layout
      choices specific to this repository.
UPDATE POLICY: New conventions are appended with explicit reasoning. Changing
      an existing convention requires a sweep of every file that follows it.
TRIGGER: Any new representational choice; any imported content that uses a
      non-canonical convention.
-->

## Status

Initial scaffold declared on 2026-05-24. The project has not yet fixed
substantive zeta-function, supersymmetric-QM, or lattice-model conventions.
Until an entry below fixes a convention, report text must state the convention
as unknown or source-dependent.

## (a) Claim Status Labels

Every substantive statement in the report should be readable as one of:

| Label | Meaning |
|---|---|
| `Question` | A research question with no asserted truth value. |
| `Proposal` | A working construction or analogy awaiting evidence. |
| `Source-local` | A claim copied or paraphrased from a registered local source. |
| `Checked` | A claim verified by a local derivation, test, or run artifact. |
| `Rejected` | A proposal ruled out by a local source, derivation, or run. |

Reasoning: the project deliberately spans arithmetic geometry, quantum
mechanics, and topological lattice models; status labels prevent analogies from
being mistaken for results.

## (b) Report Master And Shard IDs

`report.tex` is the only LaTeX master. It should contain the preamble, global
macros, include order, bibliography hook, and `\end{document}`. Body prose
belongs in `report/sections/*.tex`.

Shard IDs have the form `AQM-NN-SHORT-LABEL`, where `NN` matches the two-digit
filename prefix. The stable source maps are `report/README.md` and
`report/SHARD_CATALOG.md`.

## (c) Source Manifests

Every source topic under `references/<topic>/` should contain a `SOURCES.md`
manifest. Each acquired source entry should record:

| Field | Required content |
|---|---|
| Citation key | Stable local key used in notes. |
| Bibliographic data | Author, title, venue/version, year. |
| Locator | DOI, arXiv ID, URL, ISBN, or other access route. |
| Retrieved | Date acquired in `YYYY-MM-DD` format. |
| Local file | Relative path under `references/`. |
| SHA256 | Hash of the stored source file or snapshot. |
| Notes | Relevant theorem/equation/section locators. |

Fetched source files are append-only. Corrections go in the manifest or a new
snapshot, not by editing the fetched file.

## (d) Run Bundles

Generated artifacts live under:

```text
runs/<YYYY-MM-DD>-<slug>/
  README.md
  data/
  figures/
```

The slug is lowercase kebab case and names the question being probed. Top-level
`data/` and `figures/` are documentation placeholders, not output targets.

## (e) CSV Sentinel Comment Lines

A CSV row whose first column begins with `#` is a sentinel comment line, not
data. It carries caveats such as supersession status, negative-control status,
or missing-tool status. Parsers must skip such rows and schema entries must
document them.

## (f) Tool Dispatch

`scripts/run_all.jl` is the canonical local driver. Registered entries declare
their tool explicitly when the extension is ambiguous. Supported initial tools:

| Tool | Executable | Use |
|---|---|---|
| Julia | `julia` | Numerical linear algebra, package tests, plotting helpers. |
| Sage | `sage` | Exact arithmetic, finite fields, zeta examples, algebraic geometry probes. |
| GAP | `gap` | Finite groups, fusion/category-adjacent algebra, exact combinatorics. |
| Shell | `bash` | Small orchestration checks only. |

If a tool is optional and missing, the producer must either skip explicitly
with a clear note or fail before writing partial artifacts.

## (g) Exact And Floating Columns

When a generated CSV needs both exact and numerical values, use separate
columns:

| Suffix | Meaning |
|---|---|
| `_exact` | String representation of the exact value in the producing tool. |
| `_float` | Floating approximation. |
| `_residual` | Declared normed error, with denominator documented in schema. |

Floating diagnostics must state the tolerance, norm, denominator, precision,
and whether the result is a positive test or a negative control.

## (h) Unfixed Core Conventions

The following are intentionally not fixed yet:

- Frobenius direction and zeta-function variable normalization.
- Cohomology type and trace sign convention.
- Hilbert-space completion and Hamiltonian sign for arithmetic-QM models.
- Supersymmetric grading, adjoint, and boundary-domain conventions.
- Toric-code/star-plaquette orientation and boundary convention.
- Levin-Wen fusion-category gauge, pivotal/spherical structure, and F/R data.

Do not silently choose any of these. Add a new convention entry before using
one in a derivation or script.
