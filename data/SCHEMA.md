# data/SCHEMA.md - CSV Column Reference

Generated CSVs live under `runs/<YYYY-MM-DD>-<slug>/data/`; this file records
their schemas.

One CSV output exists.

## Common Rules

- A row whose first column begins with `#` is a sentinel comment line and must
  be skipped by parsers.
- Exact values should be represented as strings in `_exact` columns.
- Floating approximations should be represented in `_float` columns.
- Residual columns must document norm, denominator, precision, and tolerance.

## CSV Schemas

| CSV path | Producing script | Status |
|---|---|---|
| `runs/2026-05-24-toric-supercharge/data/toric_supercharge_summary.csv` | `scripts/lattice_codes/toric_supercharge_validation.jl` | Active |

## toric_supercharge_summary.csv

Produced by: `scripts/lattice_codes/toric_supercharge_validation.jl`
Run bundle: `runs/2026-05-24-toric-supercharge/`
Report shard: `AQM-05-TORIC-SUPERCHARGE`
Sentinel: row 1 begins with `#` and states that this is an algebraic
certificate; no full physical or ghost Hilbert matrices are built.

| column | type | description |
|---|---|---|
| k | int | Linear size of the periodic square toric-code lattice. |
| nqubits | int | Number of physical edge qubits, equal to `2k^2`. |
| nchecks | int | Number of local star plus plaquette checks, equal to `2k^2`. |
| max_check_weight | int | Maximum number of qubits touched by a local check. |
| all_projectors_commute | bool | Whether every pair of stabilizer checks has zero binary symplectic commutator. |
| all_checks_square_to_identity | bool | Whether every stabilizer check squares to the identity in the Pauli representation used here. |
| stabilizer_rank | int | Rank over `F_2` of the binary stabilizer-check matrix. |
| independent_check_relations | int | Number of check relations, `nchecks - stabilizer_rank`. |
| logical_qubits | int | Number of encoded qubits, `nqubits - stabilizer_rank`. |
| physical_hilbert_dim_exact | string | Exact physical Hilbert-space dimension `2^nqubits`. |
| code_dim_exact | string | Exact toric-code protected-subspace dimension. |
| boundary_rank_degree_one_exact | string | Exact rank of the degree-one-to-degree-zero boundary map in the ghost formulation. |
| h0_dim_exact | string | Exact degree-zero homology/cohomology dimension selected by the local-check ghost supercharge. |
| q_square_certificate | bool | Algebraic certificate that `Q^2=0`, using commuting projectors and fermion anticommutation. |
| anticommutator_certificate | bool | Algebraic certificate that `{Q,Q^*}=sum_i P_i`, using commuting projectors and fermion anticommutation. |
| degree_zero_homology_matches_code | bool | Whether the computed degree-zero quotient dimension matches the toric-code code dimension. |
