# Run: 2026-05-24-steane-clifford-koszul-morphisms

## Hypothesis

For the sourced Steane presentation, a Clifford automorphism that preserves the
stabilizer subspace `L` should lift to the Koszul supercharge complex. If the
Clifford only permutes the chosen stabilizer generators, the lift should be an
exact automorphism of the same `Q` after the corresponding ghost permutation.
If it changes the generator basis non-permutatively, it should be a chain
isomorphism to the transformed presentation, and only a homotopy equivalence
after retracting both presentations to the zero-syndrome code sector.

## Command

```bash
julia --project=. scripts/lattice_codes/steane_clifford_koszul_morphisms.jl
```

## Headline Finding

Transversal Hadamard maps `X_i <-> Z_i`, so it gives an exact automorphism of
the six-ghost `Q` after swapping the `X`- and `Z`-ghosts. Transversal phase maps
`X_i -> X_i + Z_i` and `Z_i -> Z_i`, so it gives a chain isomorphism to a
different independent generator presentation of the same `L`. The comparison
back to the original `Q` is naturally by the common contraction of all 63
nonzero syndrome sectors and projection to the zero-syndrome Steane code.

## Next

Generalize the statement from these two Steane Clifford generators to arbitrary
Clifford maps between CSS stabilizer presentations.
