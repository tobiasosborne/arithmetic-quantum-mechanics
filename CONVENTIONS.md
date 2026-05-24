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

## (i) Toric-Code Stabilizer Convention

For the first toric-code run, use the square `k x k` lattice with periodic
boundary conditions and one qubit on each oriented edge. There are `2k^2`
qubits: horizontal edges and vertical edges.

For a vertex `s`, the star operator `A_s` is the product of Pauli `X` over the
four incident edges. For a plaquette `p`, the plaquette operator `B_p` is the
product of Pauli `Z` over the four boundary edges. The code space is the common
`+1` eigenspace of all `A_s` and `B_p`.

Source: `references/toric_code/kitaev_quant_ph_9707021_source/anyons.tex`,
lines 189-222.

The positive Hamiltonian used in this repo is the shifted penalty

```text
H_TC = sum_s (I - A_s)/2 + sum_p (I - B_p)/2.
```

It has the same ground space as Kitaev's `H_0 = -sum_s A_s - sum_p B_p`
from equation (4), lines 328-337 of the same source.

## (j) Finite Supercharge Convention

For a finite-dimensional Hilbert space, a supercharge is a matrix `Q` with
`Q^2 = 0`. Its adjoint is written `Q^*`. The associated positive Hamiltonian
is `{Q,Q^*} = Q Q^* + Q^* Q`.

For the first toric-code run, `Q` is a local-check ghost/Koszul supercharge on
the enlarged Hilbert space `ghost Fock space tensor physical qubits`:

```text
Q = sum_i c_i^* P_i,
```

where `i` runs over all vertex and plaquette checks, `P_i=(I-S_i)/2` is the
projector onto the violated-check eigenspace, and `c_i^*` creates the auxiliary
fermion associated to check `i`. The abstract fermion modes satisfy
`c_i c_j^* + c_j^* c_i = delta_ij` and anticommute otherwise.

With this convention, `{Q,Q^*}=H_TC tensor I_ghost`. Restricted to the ghost
vacuum sector this is the physical shifted toric-code Hamiltonian. This proves
a local-check ghost formulation, not a purely physical-qubit supercharge.

The elementary meaning of cohomology for this `Q` is defined in report shard
`AQM-05-TORIC-SUPERCHARGE` before the term is used substantively.

## (k) Toric Chain-Complex/CSS Convention

The homological toric-code layer uses the `F_2` chain complex

```text
C_2 --partial_2--> C_1 --partial_1--> C_0,
```

where `C_2` is spanned by plaquettes, `C_1` by edges/qubits, and `C_0` by
vertices. Over `F_2`, signs and orientations drop out.

The CSS check matrices are:

```text
H_X = partial_1
H_Z = transpose(partial_2)
```

so the CSS commutation condition is exactly

```text
H_X * transpose(H_Z) = partial_1 * partial_2 = 0.
```

There is a finite-cell cochain supercharge already at this level:

```text
Q_cell = delta^0 + delta^1,  delta^0 = transpose(partial_1),
delta^1 = transpose(partial_2).
```

Its square is zero because `partial_1 * partial_2 = 0`, and its middle
cohomology is `ker(delta^1) / im(delta^0)`.

This boundary-map layer is not itself the quantum stabilizer supercharge from
convention (j). It is the cellular skeleton. It determines the supports of the
local checks used in the ghost/Koszul supercharge:

```text
Q = sum_v c_v^* (I - A_v)/2 + sum_f b_f^* (I - B_f)/2,
```

where the `A_v` supports are rows of `partial_1` and the `B_f` supports are
columns of `partial_2`.

Source: `references/toric_code/bombin_martin_delgado_0605094_source/HomologicalErrorCorrection6.tex`,
lines 2050-2140, and `references/toric_code/error_correction_zoo_toric.yml`,
lines 20-39.
