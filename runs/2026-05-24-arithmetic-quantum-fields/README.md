# 2026-05-24 Arithmetic Quantum Fields

## Question

Introduce and validate the finite-field arithmetic quantum field construction:
a finite physical space `X`, an internal finite symplectic vector space `V`,
and a chosen scalar function space whose `V`-valued fields inherit a pointwise
symplectic form. The Weyl-Heisenberg displacement operators of the reduced
field space are the proposed arithmetic quantum field observables.

## Command

```bash
julia --project=. scripts/bridges/arithmetic_quantum_fields.jl
```

## Outputs

- `data/arithmetic_quantum_field_examples.csv`
- `data/arithmetic_quantum_field_bases.csv`

## Headline Finding

The exact examples over `F_3` show why "nice enough" must mean "the restricted
pointwise pairing has zero radical" or else one must reduce by the radical.
Full fields on three points give a six-dimensional nondegenerate field phase
space and `27 x 27` observable algebra. Linear fields on `F_3` are also
nondegenerate, while affine fields on `F_3` have a two-dimensional constant
radical. On the parabola `y=x^2` over `F_3`, the ambient degree-one coordinate
functions `1,x,y` already separate the three rational points and give the full
nondegenerate six-dimensional field phase space.
