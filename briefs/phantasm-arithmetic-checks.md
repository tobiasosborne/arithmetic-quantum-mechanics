<!-- ROLE: pre-implementation specification for the arithmetic-interface
     falsifier. No checker or proof existed in this lane when written. -->

# EXPECTATIONS — trace, relative Frobenius, and subsystems

Date: 2026-09-10. Model: `gpt-5.6-sol`, reasoning `xhigh`.

This specifies finite negative-binding tests for SP-TRACE, SP-FROB and
SP-SUBSYS. It is not a proof or promotion record. Reuse exact `GF`, Abelian,
cyclotomic and monomial-operator APIs already under `theory/checks/`; form no
floating value or tolerance. New code must be a separate checker so the
existing `phantasm_reuse_check.py` remains unchanged and retains its scope.

## Existing R6 coverage, not new evidence

R6 currently constructs `F81`, finds its `F9` fixed subfield, chooses a
nonstandard `F9` character, and checks
`chi_9(Tr_(81/9)x)=Tr_(81/3)(parameter*x)`. It also tests selected
`#F9`-power wavefunction covariance and kills character conflation and use of
the absolute `p`-power. R6 does not test F27/F3, trace-form nondegeneracy,
arbitrary ranks, full half-form structure constants, channels, non-coordinate
subsystems, correlated inputs or decoder towers.

## Exact field models

Use `wh_kappa.ff.GF`, which represents `F_(p^d)` as verified prime-field
polynomial tables.

- `F27/F3`: `Tr(x)=x+x^3+x^9`. Expected image size 3, kernel size 9, every
  fiber size 9, and `Tr(1)=0` because the extension degree equals the
  characteristic. This is the mandatory degree-divisible-by-p control.
- `F81/F9`: identify `F9={x:x^9=x}` and use `Tr(x)=x+x^9`; image and kernel
  sizes are 9. Choose `u in F9\F3` and
  `chi_9(y)=zeta_3^Tr_(9/3)(u*y)`, not the fixed absolute character.
- Tower `F3 subset F9 subset F81`: exhaustively check
  `Tr_(81/3)=Tr_(9/3) o Tr_(81/9)` on all 81 elements and the corresponding
  character equality. Keep field elements in their actual embedded subsets.

Audit each constructed field before using it. Tests of restriction use ranks
`0,1,2`; at rank two use basis Gram matrices and sparse labels rather than
enumerating `E^4`.

## Gates and green expectations

### A1 — trace is not degree multiplication

For F27/F3 check the exact image/kernel/fibers above, `Tr(1)=0`, and exhibit a
named element with trace 1. Build the restricted symplectic Gram matrix on
the prime-field coefficient basis for ranks 0, 1 and 2; expected matrix ranks
are 0, 6 and 12.

### A2 — named characters remain distinct

Check the F81/F9 nonstandard `chi_9` is additive and nontrivial, its composite
with relative trace is nontrivial, and it differs from the fixed absolute
character on an explicit F9 witness. Also check that restricting the F27
absolute trace character to F3 is trivial although the named base character
is not.

### A3 — tower trace and character transitivity

Check both trace routes and both character routes on every F81 element.
Use separately coded direct power sums and iterated subfield operations.

### A4 — half-form Weyl identity under restriction

For F27/F3 and F81/F9 compare independently

    chi_(E/K)(omega_E(v,w)/2)
    =chi_K(Tr_(E/K)(omega_E(v,w))/2).

Check product, star, unit and coefficient trace at ranks 0,1,2. Exhaust all
basis pairs and a deterministic mixed-label set; rank-two matrices remain
sparse monomial `(permutation, exponent)` objects.

### A5 — relative Frobenius and character invariance

For `sigma=x^3` on F27/F3 and `sigma=x^9` on F81/F9 check K-linearity,
relative-trace invariance, named-character invariance, symplecticity, and
orders 3 and 2 respectively on every field element/basis pair.

### A6 — sparse Weyl covariance in both phase coordinates

Using
`W(a,b)e_y=chi(-b*(y+a)+a*b/2)e_(y+a)`, compare conjugation by the basis
permutation `|y>->|sigma(y)>` with `W(sigma(a),sigma(b))`. Exhaust rank one;
at rank two check all Hilbert basis states for zero, coordinate-basis, mixed
and cross-coordinate labels. Expected Hilbert dimensions are 1/27/729 and
1/81/6561; never allocate dense matrices of dimensions 729 or 6561.

### A7 — rank zero and unitary channel control

At rank zero verify the Hilbert permutation and state channel are literal
identities on C. At ranks one and two verify the field permutation is
bijective, its declared period is identity, conjugation preserves ordinary
trace on selected matrix units, and inverse conjugation composes exactly.

### A8 — non-coordinate F3 subsystem geometry

Use grouped phase labels `(a_1,a_2;b_1,b_2)` and the configuration matrix
`M=[[1,0],[1,1]]`. Its cotangent lift gives

    j(a,b)=(a,a;b,0),       k(u,v)=(0,u;-v,v).

Check `j` and `k` are symplectic, orthogonal, injective, and their images sum
uniquely to V2. The bad control maps `(a,b)` into the configuration half and
must fail symplecticity/nondegeneracy.

### A9 — compatible model and ordinary decoder

Let `J|x_1,x_2>=|x_1,x_1+x_2>`. Check all rank-one Weyl generator labels in

    J(W_U(u) tensor W_W(w))J^*=W_V(j(u)+k(w)).

With Kraus rows `(I tensor <e|)J^*`, check completeness, CP action on matrix
units, ordinary trace preservation, and trace duality with
`iota_J(a)=J(a tensor I)J^*`. Dividing the partial trace by 3 must fail.

### A10 — decoder direction on correlated inputs

Use `J`-transported versions of `|0,1><0,1|`, the classical correlated state
`(1/3)sum_x|x,x><x,x|`, and the Bell density
`(1/3)sum_(x,y)|x,x><y,y|`. Check decoder outputs, including `I_3/3` for the
Bell state, and compare trace duality on all qutrit matrix units. Tracing the
retained factor instead of the complement must fail the asymmetric state.

### A11 — Weyl restriction and phase cancellation

For every U Weyl label and the three correlated inputs check

    Tr(D_J(rho)W_U(u))=Tr(rho W_V(j(u))).

Replace `J` by `zeta_3 J` and check both `iota_J` and `D_J` are unchanged.
A mutation using the phase on only one side must fail exactly.

### A12 — compatible decoder tower

On three F3 registers use the configuration permutation
`M3(x1,x2,x3)=(x1,x1+x2,x1+x2+x3)`. Factor it as the two compatible
permutations `M2` on the first pair and then addition of the second output to
the third. On matrix units plus asymmetric correlated and GHZ-type rational
densities, compare direct trace over the last two factor coordinates with the
two sequential decoders under the displayed associator. A mutation swapping
the retained factor with the first discarded factor must fail.

## Pre-registered real mutation map

| mode | actual mutation | first gate |
|---|---|---|
| `--red-trace-degree` | replace F27 trace by `3*x=0` | A1 |
| `--red-character-conflation` | use restricted fixed absolute character as base character | A2 |
| `--red-tower-order` | substitute `x+x^3` for the F81/F9 trace stage | A3 |
| `--red-half-form-trace` | omit `1/2` on the restricted-form side | A4 |
| `--red-absolute-frobenius` | use `x^3` instead of `x^9` over F81/F9 | A5 |
| `--red-half-coordinate` | apply sigma only to the translation coordinate | A6 |
| `--red-rank-zero` | replace the empty tensor identity by a qutrit permutation | A7 |
| `--red-degenerate-subsystem` | use the configuration-half injection | A8 |
| `--red-decoder-normalized-trace` | divide partial trace by complement dimension | A9 |
| `--red-decoder-direction` | trace the retained factor | A10 |
| `--red-decoder-phase` | phase only one occurrence of J/J* | A11 |
| `--red-decoder-tower-order` | exchange retained and first discarded tower factors | A12 |

Each flag must exit 1 first at its named gate; surviving mutations exit 0 and
bad usage/unexpected exceptions exit 2. Run only the target gate in red mode.
Add disabled-guard survival controls for A1, A6, A9 and A12 before final green.

## Canonical interface gaps

1. The arithmetic brief identifies a planned dependency repair: SP-FROB's
   unitary-channel clause uses D1706/SP-CP, but its canonical definition/DAG
   fields do not yet name that reuse. Register it before promotion; this
   specification does not change dependencies.
2. SP-SUBSYS says “compatible iterated tensor decompositions,” but D1710 owns
   only one decomposition and one `J`. Before proof integration, own the exact
   two-stage/direct unitary diagram and associator, or narrow the tower clause.
   A12 tests the explicit `M3` instance only and cannot define compatibility.

Passing these finite gates proves none of the arbitrary-rank, all-extension or
general subsystem claims. It supplies no characteristic-two half-form,
support-code identification, global prime assembly or spectral result.
