# Mechanical repair demands — string anchors only

No trunk patch has been applied by the critic.

## O1 — submitted coherence checker

Target: `theory/checks/frobenius_boundary_check.py`.

Anchor: `v = np.array([1, 1, 0, 0], dtype=object)` through
`print("B4 PASS: coherent CRT reblocking, ternary transport and dephasing sentinel")`.

Replace the identity green path with an actual matrix/channel calculation:

1. Build the permutation matrix for B_(2,2) from the submitted pair map.
2. Compute the multiplicity-coordinate state `B.T @ rho @ B`.
3. For `--red-coherence`, delete only its entries between distinct
   multiplicity factors. Green retains the matrix.
4. Transport the result back with B and compare its return probability with
   the independently fixed value 1. The red must give 1/2 and fail.
5. Check transport of off-diagonal matrix units across multiplicity sectors;
   do not substitute the input state directly for a purported channel output.
6. A copy changing only `rho = np.outer(v, v)` to `rho = np.diag(v * v)`
   must exit nonzero even without any red flag. Keep an independent expected
   Born value so the expected state cannot be silently changed with the data.

Update `theory/checks/frobenius_boundary_EXPECTATIONS.md` at the anchor
`* B4: the CRT cycle-pair bijection` to describe the actual channel test.
Run submitted green and all six named red modes after repair. No mathematical
change to `orbit-composition.md`'s coherent-reblocking proof is required.

## O2 — named Fourier phase in the labbook

Target: `labbook/sections/sidequest_frobenius_boundary.tex`.

Anchor:

`$F_E|x\rangle=Q^{-1/2}\sum_y\exp(-2\pi i\operatorname{Tr}_{E/\mathbb F_p}(xy)/p)|y\rangle$`

Replace with:

`$F_E|x\rangle=Q^{-1/2}\sum_y\zeta_p^{-\operatorname{Tr}_{E/\mathbb F_p}(xy)}|y\rangle$`

The surrounding definition already refers to the arithmetic field register;
one short phrase may recall that `zeta_p` is its named primitive root.
No change to the overlap formula or its proof is needed.
