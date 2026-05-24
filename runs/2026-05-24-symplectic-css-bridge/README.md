# Run: 2026-05-24-symplectic-css-bridge

## Hypothesis

The cellular chain-complex construction of a toric CSS code is the same data
as an isotropic stabilizer subspace in the finite symplectic Pauli module. For
prime qudit dimension `p`, oriented boundary matrices over `F_p` should satisfy
`partial_1 partial_2 = 0`, and the rowspace
`row(partial_1) x 0 + 0 x row(partial_2^T)` should be isotropic.

## Command

```bash
julia --project=. scripts/lattice_codes/symplectic_css_bridge_validation.jl
```

## Headline Finding

For `k=4` and `p in {2,3,5}`, the checker verifies
`partial_1 partial_2 = 0`, CSS isotropy in the symplectic module, ranks
`rank partial_1 = rank partial_2 = 15`, middle homology dimension `2`, and
encoded Hilbert-space dimension `p^2`.

## Next

Generalize the checker from the oriented torus to arbitrary finite cell
complexes and compare with a Sage/GAP homology computation when those tools are
available on PATH.
