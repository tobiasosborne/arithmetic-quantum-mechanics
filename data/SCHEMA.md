# data/SCHEMA.md - CSV Column Reference

Generated CSVs live under `runs/<YYYY-MM-DD>-<slug>/data/`; this file records
their schemas.

Two CSV outputs exist.

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
| `runs/2026-05-24-toric-chain-ghost-unification/data/toric_chain_ghost_unification.csv` | `scripts/lattice_codes/toric_chain_ghost_unification.jl` | Active |

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

## toric_chain_ghost_unification.csv

Produced by: `scripts/lattice_codes/toric_chain_ghost_unification.jl`
Run bundle: `runs/2026-05-24-toric-chain-ghost-unification/`
Report shard: `AQM-05-TORIC-SUPERCHARGE`
Sentinel: row 1 begins with `#` and states that this is an algebraic
chain-complex certificate.

| column | type | description |
|---|---|---|
| k | int | Linear size of the periodic square toric-code lattice. |
| nvertices | int | Number of vertices, dimension of `C_0`. |
| nedges | int | Number of edges/qubits, dimension of `C_1`. |
| nfaces | int | Number of plaquettes, dimension of `C_2`. |
| boundary_square_zero | bool | Whether `partial_1 partial_2=0`, checked as even overlap between every vertex row and face boundary column. |
| star_masks_match_boundary_one | bool | Whether the star-check supports match the rows of `partial_1`. |
| plaquette_masks_match_boundary_two | bool | Whether the plaquette-check supports match the columns of `partial_2`. |
| rank_boundary_one | int | Rank over `F_2` of `partial_1`. |
| rank_boundary_two | int | Rank over `F_2` of `partial_2`. |
| h1_dim | int | First homology dimension, `nedges - rank_boundary_one - rank_boundary_two`. |
| code_dim_from_h1_exact | string | Exact dimension `2^h1_dim` predicted for the toric-code code space. |
| cellular_supercharge_square_zero | bool | Whether the finite-cell cochain supercharge squares to zero. |
| cellular_middle_cohomology_dim | int | Middle cohomology dimension of the cellular cochain supercharge. |
| cellular_middle_cohomology_basis_count_exact | string | Exact number of middle cohomology classes, equal to `2^cellular_middle_cohomology_dim`. |
| cochain_cocycle_count_exact | string | Exact size of `ker(partial_2^T)` in the computational `Z` basis. |
| cochain_coboundary_count_exact | string | Exact size of `im(partial_1^T)`, the star-generated coboundary orbit size. |
| css_commutation_from_boundary | bool | Whether CSS commutation follows from `partial_1 partial_2=0`. |
| ghost_checks_from_chain_complex | bool | Whether the supports used in the ghost supercharge are exactly the supports determined by the boundary complex. |
