# 2026-05-24 Steane All-Clifford Ghost Gaussians

## Question

For the Steane six-generator Koszul supercharge, make precise the statement
that an arbitrary Clifford maps Pauli products to Pauli products and that the
resulting supercharge is related to the old one by a Gaussian operation on the
ghosts.

## Command

```bash
julia --project=. scripts/lattice_codes/steane_all_clifford_ghost_gaussians.jl
```

## Outputs

- `data/steane_all_clifford_generator_summary.csv`
- `data/steane_all_clifford_generator_images.csv`
- `data/steane_ghost_gaussian_elementaries.csv`

## Headline Finding

The exact arbitrary-Clifford statement uses signed Pauli stabilizer generators.
For the transported image presentation
`(U S_1 U^dagger, ..., U S_6 U^dagger)`, physical conjugation gives an exact
chain isomorphism of Koszul supercharges with the identity ghost relabeling.
If the image stabilizer is then rewritten in another independent generator
basis, row swaps and row shears generate `GL_6(F_2)` and lift to
number-preserving fermionic Gaussian operations on the six ghosts.

The subtlety is that a row shear is not a scalar `GL_6` ghost transform against
the old projector generators. Replacing `S_a` by `S_a S_b` uses
`P(S_a S_b)=P(S_a)+S_a P(S_b)`, so the ghost Gaussian has an even
operator-valued coefficient `S_a`. On the zero-syndrome code sector this
coefficient is `+1`, reducing to the ordinary exterior action of the row
operation.
