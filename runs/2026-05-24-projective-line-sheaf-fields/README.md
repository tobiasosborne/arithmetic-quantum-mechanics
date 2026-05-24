# Projective-Line Sheaf Fields

## Question

For projective arithmetic spaces, what replaces the naive finite-set
`Map(X,V)` field space? This run checks the first explicit answer for
\(\mathbf P^1_{\mathbb F_3}\): use global sections of the sheaves
\(\mathcal O(d)\), tensor with \(V=\mathbb F_3^2\), evaluate at rational
points, and rank the induced pointwise symplectic form.

## Command

```bash
julia --project=. scripts/bridges/projective_line_sheaf_fields.jl
```

## Outputs

- `data/projective_line_sheaf_field_summary.csv`
- `data/projective_line_sheaf_field_basis_rows.csv`

## Headline Finding

The sheaf choice matters. For \(d=1\), the two scalar sections evaluate
independently on \(\mathbf P^1(\mathbb F_3)\), but their all-weights-one
pointwise scalar pairing is zero, so the whole \(V\)-valued field space is
radical. For \(d=2\), the induced scalar Gram form is nondegenerate. For
\(d=4\), global sections already outnumber the four rational points, so
evaluation has a scalar kernel.

## Caveat

This is a finite rational-point field algebra, not the full scheme-theoretic
sheaf. The chosen pointwise pairing uses fixed affine-chart representatives
and weights all rational points by \(1\).
