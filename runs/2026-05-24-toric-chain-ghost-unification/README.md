# Run: 2026-05-24-toric-chain-ghost-unification

## Hypothesis

The toric-code boundary-map picture and the auxiliary-fermion supercharge
picture should be the same construction at two levels. The chain complex
`C_2 -> C_1 -> C_0` gives a cellular cochain supercharge and determines the
CSS check supports, while the ghost supercharge is the Koszul differential for
those checks.

## Command

```bash
julia --project=. scripts/lattice_codes/toric_chain_ghost_unification.jl
```

## Headline Finding

For `k=4`, the run verifies `partial_1 partial_2=0`, identifies the star
supports with rows of `partial_1`, identifies the plaquette supports with
columns of `partial_2`, computes `rank partial_1 = rank partial_2 = 15`, and
gets `dim H_1 = 32 - 15 - 15 = 2`, hence code dimension `2^2 = 4`.
It also records that the cellular cochain supercharge squares to zero and that
the `Z`-basis quotient has `2^17 / 2^15 = 4` classes.

## Next

The next refinement is to decide whether a BRST-style package with both
constraint ghosts and chain-level fields is useful, or whether the boundary
complex should remain the classical support layer under the ghost/Koszul
supercharge.
