# SUMMARY — exact affine falsifier lane

Model: `gpt-5.6-sol`, reasoning setting `xhigh`.

The lane supplies a standalone exact checker proposal for SP-EGOROV and the
remaining affine part of SP-TENSOR. `EXPECTATIONS.md` was written and reported
before implementation. The lane did not read a prover artifact and did not
edit, stage or commit trunk files.

The checker has nine individually reachable gates:

- E1--E3 exhaust the 24-element `Sp(2,F3)`, all 216 affine arrows, every
  identity and inverse, all 46,656 semidirect products pointwise, and the
  affine Weyl-algebra identity/star/product/composition laws.
- E4--E6 independently construct the D8/D1703 translation, unnormalised
  Fourier and quadratic-shear matrices. Their covariance signs are checked in
  exact `Z[zeta_3]` or monomial exponent arithmetic.
- E7 keeps the zero symplectic space and both tensor-unit placements literal.
- E8 uses `F9=F3[u]/(u^2+1)` and the nonstandard character
  `psi_u(a+b*u)=zeta^b`; it checks 6,561 Weyl products, 6,561 translations and
  all Fourier/shear labels without collapsing to the absolute-trace character.
- E9 independently compares all 81 rank-two Weyl operators with tensor
  products, checks factor swap, and exhausts all 3,779,136 combinations of two
  affine factor arrows and two Weyl labels for tensor naturality.

No floating values enter mathematical checks, and there are no square-root
normalisations or tolerances. Fourier covariance uses `F W F^*=q W(Jv)` over
cyclotomic integers. The hot affine/tensor loops use cached label/phase tuples;
dense exact multiplication is limited to Fourier dimensions 3 and 9.

All nine advertised mutations exited 1 first at their pre-registered gates,
E1 through E9, before the first green run. The first green passed in 3.204
seconds. After correcting a two-assertion reporting undercount in E8 and
strengthening the rank-zero construction, the revised E7 red again failed at
its intended gate and final green passed in 3.172 seconds. The displayed
aggregates total 4,654,738 checks. `RUNS.md` records the commands, outputs and
timings.

The evidence is finite and negative-binding only. It does not prove the
arbitrary-rank algebra action, the uniqueness of projective implementers, a
choice of genuine Weil lift, or projective coherence in arbitrary rank. Those
remain written-proof and review obligations. `PATCH.md` gives string anchors
for installing the intended trunk filenames and recording this exact scope
without promoting either claim.
