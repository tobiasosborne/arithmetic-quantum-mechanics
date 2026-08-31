# Run: 2026-05-24-css-supercharge-symplectic-dictionary

## Hypothesis

For a CSS stabilizer code over a prime field, the ghost/Koszul supercharge is
determined by a choice of generators for the isotropic stabilizer subspace
`L <= F_p^n x F_p^n`. Its degree-zero cohomology should have dimension
`p^(n-dim L)`, while the logical Pauli module has dimension
`2(n-dim L) = dim(L^perp/L)`.

## Command

```bash
julia --project=. scripts/lattice_codes/css_supercharge_symplectic_dictionary.jl
```

## Headline Finding

The run checks the Steane CSS code over `F_2` and a qutrit CSS toy code over
`F_3`. In both cases CSS isotropy certifies `Q^2=0` and the anticommutator
certificate, while the degree-zero supercharge count agrees with the
stabilizer code dimension.

## Next

Extend the producer to parse arbitrary CSS matrices from a small data file once
we start collecting non-toric examples.
