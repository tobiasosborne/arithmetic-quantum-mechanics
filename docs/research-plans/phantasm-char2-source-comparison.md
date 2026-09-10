# DG-CHAR2 source and reuse ledger

## Already admitted

- F1-REAL, `theory/sidequests/f1-cyclotomic.md` section 2 `<1>1`--`<1>8`,
  works for every finite abelian configuration group and even cyclotomic
  level. It gives trace orthogonality, the full matrix image, irreducibility,
  model dimension, and `U(1)` uniqueness. It does not choose symmetry lifts.
- F1-RING, the same file section 4 `<1>1`--`<1>6`, identifies the reference
  field/ring Schrödinger model with the finite-abelian model, including p=2.
  Its direct statement is one ring register; all-rank tensor needs the fixed-
  level F1-FUNCT theorem or a new proof.
- F1-FUNCT, section 3 `<1>1`--`<1>6`, gives the central product and Hilbert
  tensor comparison at fixed N. DG-CHAR2 currently omits it and must register
  it before using level-four tensor coherence.
- L-TRIV, `theory/wh-kappa.md` lines 83--94, trivializes a symmetric complex
  2-cocycle on any finite exponent-p abelian group. At p=2 its basis proof
  chooses square roots of `mu_2` values, so the cochain may be taken in
  `mu_4`; it does not produce a multiplicative section in g.
- WH-WEIL-a, `theory/wh-kappa-choice.md` section 8 `<1>2`--`<1>3`, proves the
  exact frame-automorphism extension and lift existence for rank-one `k^2` at
  every characteristic.
- WH-WEIL-c/d, section 8 `<1>5`--`<1>6`, prove at rank one that `mu_2` phases
  occur exactly on `O(Q_beta)` and order-four phases are forced off it, with
  the q=2 anisotropic exception recorded. They are regressions and proof
  templates; their statements do not already quantify over arbitrary rank.
- SP-WEYL and SP-EGOROV remain odd-characteristic results. Their algebra,
  affine-action and projective-model interfaces are the shapes to extend, not
  lemmas that can be applied at p=2.

## SP-GH08 actual scope

Local source: `refs/symplectic-phantasm/SP-GH08/source.tex`, SHA-256
`4b5b7ff9fb9a90fb17c02d4cc6fdfccedea36129042e1ba2e291d51df3117b23`.

- Lines 616--634 choose an unramified 2-adic extension and the length-two
  ring `R=O_K/m_K^2`, with trace to Z/4.
- Lines 638--674 choose a free symplectic R-lift, a Lagrangian splitting and
  its nonsymmetric beta. These are extra data, not consequences of V alone.
- Lines 678--695 define the R-central Heisenberg group.
- Lines 699--729 define source `ASp(V)` as pairs `(g,alpha)` satisfying the
  R-valued defect equation and composition, with exact sequence
  `0->Hom(V,R)->ASp(V)->Sp(V)->1`. This `ASp` is not D1701's already split
  affine group `V semidirect Sp(V)`.
- Lines 747--792 state Stone--von Neumann and construct a projective
  representation of source ASp by one-dimensional intertwiner lines.
- Lines 794--801 state the central `mu_4` extension AMp and its linear
  representation.
- Lines 805--828 require the free Witt symplectic lift and produce a pullback
  over `Sp(tilde V)`. This is not a theorem that ASp splits over every
  `Sp(V)`.

The paper supports retaining a defect lift and a central phase extension. It
does not support applying `omega/2`, forgetting beta/Witt choices, or replacing
the nonsplit extension by D1701 affine coordinates.

## Exact remaining positive comparison

The proposed category lives after a chosen complex central character: its
kernel is `Hom((V,+),mu_2)`, and nondegeneracy of `psi o omega` can identify
that kernel with V. GH08's raw kernel is `Hom(V,R)` before applying its
central character. These groups must not be equated.

Because the additive group V has exponent two, every raw homomorphism
`V->R` lands in the two-torsion subgroup `R[2]=2R`. Applying GH08's chosen
trace character gives a map

    Hom(V,R) -> Hom(V,mu_2).

Its kernel is not automatically trivial: for extension degree greater than
one the trace character itself has a nonzero additive kernel. Thus the
phase-level translation kernel can at most be identified with a computed
image/quotient of the raw kernel, even though the source calls its central
character faithful in its representation-theoretic convention.

For named source data, the proof task is:

1. identify `2R` with the residue-field phase subgroup and match the chosen
   beta cocycle with the proposed scalar Weyl cocycle;
2. send `(g,alpha)` to `(g,r_alpha)` by applying the named central character;
3. compute the kernel and image of this map rather than assuming them;
4. compare its projective Egorov line with the F1-REAL intertwiner line by
   uniqueness;
5. state only the resulting map from GH08 AMp into the relevant implementer
   extension unless a stronger quotient/isomorphism is actually proved.

This comparison is positive and bounded. It may recover a finite `mu_4`
linear refinement on its image, while the main all-rank carrier already gives
exact algebra maps and projective/channel actions without a general split.
