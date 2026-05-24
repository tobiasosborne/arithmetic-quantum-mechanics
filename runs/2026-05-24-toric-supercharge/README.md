# Run: 2026-05-24-toric-supercharge

## Hypothesis

For a finite `k x k` toric-code Hamiltonian, attach one auxiliary fermion to
each local stabilizer check. The shifted positive stabilizer Hamiltonian should
be writable as `{Q,Q^*}` for the local-check ghost supercharge
`Q=sum_i c_i^* P_i`, where `P_i` projects onto a violated stabilizer check.
In degree zero, meaning physical states with no ghost label attached, the
closed states `Qv=0` should be exactly the toric-code code space.

## Command

```bash
julia --project=. scripts/lattice_codes/toric_supercharge_validation.jl
```

## Headline Finding

For `k=4`, the validation works algebraically with binary stabilizer masks; it
does not build the `2^32` physical Hilbert matrix or the ghost-Fock matrix. It
verifies commuting local checks, stabilizer rank `30`, code dimension `4`, and
the CAR/projector certificates for `Q^2=0` and
`Q Q^* + Q^* Q = H_TC`.

## Next

This run uses auxiliary fermions/ghosts. The next question is whether there is
a useful purely physical-qubit supercharge, or whether the ghost-extended
formulation is the correct local-check supersymmetric package.
