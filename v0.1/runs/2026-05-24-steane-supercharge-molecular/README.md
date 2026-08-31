# Run: 2026-05-24-steane-supercharge-molecular

## Hypothesis

For Gottesman's table presentation of the seven-qubit Steane CSS code, the
three binary check rows span a self-orthogonal subspace `D <= F_2^7`. The CSS
stabilizer subspace is `L = (D x 0) + (0 x D)`, the symplectic centralizer is
`L^perp = C x C` with `C = D^perp`, and the six-fermion Koszul supercharge has
degree-zero cohomology equal to the two-dimensional Steane code.

## Command

```bash
julia --project=. scripts/lattice_codes/steane_supercharge_molecular.jl
```

## Headline Finding

The run records `dim D=3`, `dim C=4`, `dim L=6`, `dim L^perp=8`, and
`dim(L^perp/L)=2`. It also records the two Hamming-code cosets supporting
Gottesman's `|0bar>` and `|1bar>` states, the four logical Pauli classes, and
the full ghost-degree cohomology dimensions
`2,12,30,40,30,12,2`.

## Next

Use this as the concrete test case when comparing the stabilizer/Koszul
supercharge to more geometric chain-complex examples.
