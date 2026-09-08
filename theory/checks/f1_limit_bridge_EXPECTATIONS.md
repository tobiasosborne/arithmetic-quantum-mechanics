# Complete finite bridge probes after the single review repair

The original bridge specification requested seven mathematical gates. They
are now implemented across two standalone exact checkers:

- `f1_limit_mirabolic_check.py`: B1, B2, B4, B7.
- `f1_limit_bridge_check.py`: B3, B5, B6.

The earlier lane executable covered only B3/B5/B6. Its broader specification
is superseded by this actual execution contract. No missing gate or parsing
failure is counted as a successful red mutation.

| Gate | Actual implemented sample | Data mutation |
|---|---|---|
| B1 | All seven rank-two affine orbitals over F2 and F3: difference-kernel convolution, physical adjoint, constant valencies and every orbital trace Gram pair | --red-mir-kernel omits the intermediate vector from convolution |
| B2 | Over F2/F3 in rank two: Rosso generator quadratic, independent controlled flag-line averaging projection and trace, invariant-word closure and full generated dimension seven | --red-mir-line uses a fixed coordinate line |
| B3 | Every subspace in dimensions one and two over F2/F3: Fourier/annihilator identity and Fourier square. Coordinate complete flags for every permutation through rank five: dual-reversal rank matrices and relative-position conjugation | --red-fourier changes an annihilator; --red-dual-reversal omits reversal of a flag index |
| B4 | Over F2/F3 in rank two: vector expectation as a complete dephasing Kraus list, physical trace and Hecke bimodule identity. All rank-two endpoint products/Gram entries reconstructed exactly from Q=2,3,5,7 | --red-mir-expect retains vector coefficients |
| B5 | Sp4(F2): 720 symplectic matrices, 15 Lagrangians, 45 isotropic flags, 18 decomposable flags, 8 full and 16 local orbitals, scaled UCP trace-adjoint pair | --red-typec-scale omits inverse corner fraction |
| B6 | Nested versus ternary shuffle bijections for ranks (1,1,1),(1,1,2),(1,2,1); every signed permutation in thin block factorizations of ranks (1,1),(1,2),(2,2),(1,3) | --red-shuffle changes an expanded letter; --red-thin-block changes a sign in the recovered subgroup factor |
| B7 | Affine rank1+rank1 over F2/F3: full ranks12/36, decomposable ranks8/18, 16 product-shuffle orbital matrices, transitive average, scaled unit and every 7×16 trace-adjoint pairing | --red-affine-dec omits inverse decomposable fraction |

The mirabolic kernel check compares direct Rosso convolution sums with
ordinary kernel matrix products at a reference row. Transitivity determines
all rows. Orbital construction uses explicit linear transporters and the
intersection-of-Borels antichain labels; the projection is built separately
by translating along the actual flag line.

The rank-two endpoint interpolation is exact, not an extrapolation guess.
Rosso's structure coefficients are polynomials. Each arithmetic coefficient
counts intermediate flag-vector points and is bounded by Q²(Q+1), so its
polynomial degree is at most three. Four distinct arithmetic fibres determine
its value at one. The resulting multiplication is checked on every basis
pair: deleting the five vector-labelled directions gives C[S2], and the
endpoint Gram radical has exactly those five directions. This is only a
rank-two computation; the general statement rests on the orbit-valency proof.

B3 uses Q[zeta_3] as rational pairs and unnormalized Fourier matrices divided
by Q^n after conjugation. Every other quantity is an integer or Fraction.
No floating-point tolerance is used. The first attempt to add dual reversal
had a Python scope error; that interpreter failure was repaired and was not
counted as mutation evidence. The subsequently observed mathematical red
fails exactly the dual flag rank-matrix relation.

Both checker green runs and all eight original advertised red modes were run
during repair. The ninth thin-block mutation was then observed failing before
its acceptance run. Every red exits one with a named mathematical FAIL and no interpreter
exception. Final session-close repeats the complete advertised suite.

Passing these finite probes does not prove CP at a nonarithmetic parameter,
all-rank polynomial identities, the operational germ category, or global
coherence. Those claims require the structured proofs and their explicit
domains. In particular, mere positivity at prime powers is not sufficient
for positive boundary evaluation.
