# HANDOFF.md

Session-state file for incoming agents. This is not an authoritative source for
mathematical claims; use `report.tex`, `INDEX.md`, `CONVENTIONS.md`, and local
source manifests for that.

## Current Frontier

Initial infrastructure is in place for a lab-book style research workspace
about Weil/zeta functions, arithmetic quantum mechanics, supersymmetric quantum
mechanics, and Kitaev/Levin-Wen/toric-code models. The current arithmetic-field
frontier is projective: `AQM-15-PROJECTIVE-SHEAF-FIELD-DEFINITIONS` and
`AQM-16-PROJECTIVE-LINE-SHEAF-FIELD-CALCULATION` replace naive projective
`Hom(X,V)` by chosen sheaf-section spaces \(H^0(X,\mathcal L)\otimes V\), and
`AQM-17-PROJECTIVE-LINE-STALKS` works out the rational-point stalks whose
residues give the finite evaluation rows.

## Most Recent Session

**2026-05-24 - Lab-book scaffold created.**

- Created the sharded LaTeX master `report.tex` with five initial shards under
  `report/sections/`.
- Added report navigation files, scientific-practice guidance, conventions,
  an index manifest, source/reference placeholders, run-bundle discipline, and
  data/figure placeholders.
- Added a minimal Julia package scaffold, local script runner, report-shard
  checker, Makefile, and local CI script.
- Local tool check found Julia, LaTeX `latexmk`, and `bd`; `sage` and `gap`
  were not on PATH in this shell.

**2026-05-24 - Toric-code ghost supercharge run added.**

- Registered Kitaev's arXiv TeX source bundle under
  `references/toric_code/`.
- Added the convention `Q=sum_i c_i^* P_i`, one auxiliary fermion per local
  stabilizer check, with `P_i=(I-S_i)/2`.
- Implemented an algebraic validator that avoids full Hilbert matrices. For
  `k=4` it checks commuting local stabilizers, rank `2k^2-2`, code dimension
  `4`, and the CAR/projector certificates for `Q^2=0` and
  `{Q,Q^*}=H_TC`.
- Added the boundary-map unification: the chain complex
  `C_2 -> C_1 -> C_0` gives `H_X=partial_1`, `H_Z=partial_2^T`, so
  `partial_1 partial_2=0` is the CSS commutation condition and its rows/columns
  are exactly the ghost-supercharge check supports.
- Added a full proof in `AQM-06-TORIC-CHAIN-GHOST-PROOF`: cellular classes
  `[a] in ker(delta^1)/im(delta^0)` map to normalized orbit sums in the code
  space, and the ghost anticommutator follows from the CAR and commuting
  projectors.
- Added `AQM-07-TORIC-OPERATOR-RELATION`: `Q_cell` is not a low-ghost
  restriction of `Q_gh`; instead `delta^0` induces star translations,
  `delta^1` induces plaquette syndrome multiplication, and `Q_gh` is the
  Koszul differential for those projector equations.
- Added `AQM-08-SYMPLECTIC-CSS-BRIDGE`: the CSS chain complex produces an
  isotropic stabilizer subspace `L`, and the logical Pauli module is
  `L^perp/L = H^1 x H_1`; a new exact Julia run checks this over
  `F_2`, `F_3`, and `F_5`.
- Added `AQM-09-SYMPLECTIC-SUPERCHARGE-DICTIONARY`: for any CSS stabilizer
  subspace `L`, a chosen basis gives a ghost/Koszul supercharge whose
  degree-zero cohomology is the stabilizer code and whose logical Pauli action
  is `L^perp/L`.
- Added `AQM-10-STEANE-SYMPLECTIC-MOLECULAR` and
  `AQM-11-STEANE-SUPERCHARGE-COHOMOLOGY`: the Gottesman-table Steane code is
  now worked out at vector-space, stabilizer, fermion, supercharge, and
  cohomology level, with an exact run bundle.
- Added `AQM-12-STEANE-CLIFFORD-KOSZUL-MORPHISMS`: transversal Hadamard is an
  exact automorphism of the written Steane `Q` after ghost swap; transversal
  phase is a chain isomorphism to a changed generator presentation and a
  homotopy equivalence back through the common zero-syndrome retract.
- Added `AQM-13-CLIFFORD-GROUP-GHOST-GAUSSIAN-THEOREM`: arbitrary Clifford
  covariance is stated for signed Pauli stabilizer presentations, while
  stabilizer presentation changes lift to number-preserving ghost Gaussians;
  the Steane validation checks all 56 H/P/CNOT Clifford generators and the 45
  elementary GL6 ghost moves.
- Added `AQM-14-ARITHMETIC-QUANTUM-FIELDS`: finite arithmetic quantum fields
  are proposed as Weyl-Heisenberg displacement systems for reduced pointwise
  symplectic function spaces `E <= Map(X,V)`. The validation run gives exact
  `F_3` examples for finite sets, vector spaces, and simple arithmetic
  varieties.
- Added `AQM-15-PROJECTIVE-SHEAF-FIELD-DEFINITIONS` and
  `AQM-16-PROJECTIVE-LINE-SHEAF-FIELD-CALCULATION`: Stacks Project TeX sources
  are registered locally for presheaves, sheaves, Proj, projective space,
  varieties, twists, and projective-space cohomology. The new exact run checks
  \(\mathbf P^1_{\mathbb F_3}\), \(H^0(\mathcal O(d))\otimes\mathbb F_3^2\),
  finite rational-point evaluations, radicals, and reduced Weyl counts for
  `d=0..4`.
- Added `AQM-17-PROJECTIVE-LINE-STALKS`: the same run now records one symbolic
  germ row for every monomial section at each rational point, including the
  local ring, local frame, maximal ideal, and residue value.
- Added `AQM-18-STALKS-AS-FIELD-GERMS`: the phrase "field at the point" is now
  fixed as stalk equals local field germ, while fiber/residue equals sampled
  field value.  The shard tabulates every scalar residue for the
  \(\mathbf P^1_{\mathbb F_3}\), \(d=0,\ldots,4\), examples.

## Next Useful Steps

1. Acquire and register core local sources before adding content claims.
2. Decide first fixed conventions: zeta normalization, Frobenius direction,
   SUSY-QM grading/signs, and lattice-model boundary/orientation conventions.
3. Create the first run bundle only when there is a concrete source-backed
   invariant to compute.
