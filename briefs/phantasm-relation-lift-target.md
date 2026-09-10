# DG-REL-LIFT — scalar-retaining relation comparison

Planning model: `gpt-5.6-sol`, reasoning `xhigh`.

This is a bounded source/reuse and generator-matching work order. It proposes
one positive next comparison and the data a later geometric lift must carry.
It contains no proof, admission, semantic-kernel quotient, or authorization
to identify the full arithmetic source with stabilizer theory.

## Goal and fixed boundary

Work at one odd prime `p` for which `F_p` is a named object of the arithmetic
datum. Start with the matched term fragment `G_p^arith` and exact table in
`briefs/phantasm-relation-lift-generator-match.md`. Compare selected arithmetic representatives with the
D1715 intertwiner lines and with their D1706 branch normalizations.

The full `R_p` source remains outside this comparison: it has extension-field
objects, transfers, support codes, Frobenius and higher multiplication gates.
Characteristic two remains DG-CHAR2 and contributes no assumed lift here.

## Exact admitted reuse

| admitted result | reusable clause | boundary |
|---|---|---|
| FRP-CAT, `amplitude-category.md` `<1>1`--`<1>12` | small `R_p`-linear dagger symmetric monoidal source and well-defined strong dagger-monoidal Hilbert interpretation | no faithfulness, presentation completeness or full Clifford scope |
| FRP-CP, `process-category.md` `<1>1`--`<1>12` | source-certified composition/tensor, ordinary-trace CP realization, normalization and retained external tags | equal CP maps need not be source-equal; arbitrary ambient branches need not have arithmetic terms |
| SP-COMPACT | opposite-form dual, diagonal cup/cap, exact snakes, Boolean relation scalars | relation composition forgets witness multiplicity and all nonzero complex weights |
| SP-STAB-REL, `stabilizer-intertwiner-line.md` and companions | each nonempty affine relation has a one-dimensional operator line; composition, dagger and tensor match; projective equivalence has zero separate | the equivalence forgets every nonzero scalar and probability |
| SP-SCALAR | `Phi_(cT)=|c|^2Phi_T`, contraction criterion, optional class-invariant normalization with composition still separate | no branch or probability is stipulated by the projective class |
| SP-CP | intrinsic finite Kraus/channel and instrument laws with ordinary trace | no automatic branch from a relation or projective arrow |

Primary source limits remain binding. SP-CK21 `lagrel.tex` 3611--3744 gives
the odd-prime comparison only modulo invertible scalars. SP-BC24
`section_AffLagRel.tex` 143--189 gives signed relation/compact data but uses a
different time-reversal dagger. SP-WAT18 `paper.txt` 3788--4144 and
5139--5184 gives CP/Kraus/channel/instrument semantics, not a relation lift.

## Registration prerequisite

Before formulating a canonical claim, register a small definition (D1716 if
still free) owning only:

1. the odd-prime hypothesis and named `F_p` arithmetic atom;
2. the term fragment `G_p^arith` exactly as specified in
   `briefs/phantasm-relation-lift-generator-match.md`;
3. the selected terms `w_tilde`, `s_p`, `cup_p`, `cap_p` and their types;
4. the listed relation labels and the fixed opposite-space standardization
   `c(a,b)=(a,-b)`;
5. the coefficient restriction to `R_p`.

Functoriality, matrix equality, intertwiner-line membership, scalar values,
branch admissibility, fullness and faithfulness are obligations, not clauses
of the definition. Do not add arbitrary complex scalars to the source.

## One bounded positive next comparison

Proposed id `RL-GEN-MATCH` (register only after the definition above):

> For every odd prime `p` and named arithmetic datum containing `F_p`, the
> Hilbert images of the selected terms in `G_p^arith` are the actual
> representatives listed in `briefs/phantasm-relation-lift-generator-match.md` and lie in the D1715
> intertwiner lines of their listed affine Lagrangian relations. The
> generator comparisons respect dagger and ordered tensor at realized-map
> and projective equality. The unnormalized arithmetic cup/cap obey the
> Hilbert snake equations and have closed loop `p`; their `p^(-1/2)`
> normalizations are D1706 branches with loop `1` and snake scalar `p^(-1)`.
> Every displayed coefficient belongs to `R_p`. No source faithfulness,
> source-presentation completeness, or normalized functor on all relations
> is asserted.

Dependencies: FRP-CAT, FRP-CP, SP-COMPACT, SP-STAB-REL, SP-SCALAR, SP-CP,
SP-EGOROV and SP-TENSOR. Sources: SP-CK21, SP-BC24, SP-WAT18, SP-GROSS06.

### Proof split

One 250--400-line Lamport generator shard:

- derive the half-form rephasing, Fourier orientation, shear and controlled
  momentum signs on computational basis/Weyl labels;
- verify each operator satisfies the appropriate D1715 line equation;
- verify source coefficients and actual Hilbert maps, without inferring the
  converse of FRP-CAT;
- calculate cup/cap types through the opposite-space map, both snakes, loop
  and normalized branch effects;
- extend only dagger/tensor comparisons generated by the verified table.

A second proof is not justified until this finite table determines whether a
geometric amplitude-line definition can be made without additional choices.

### Exact finite falsifiers

Use exact cyclotomic/monomial matrices for `p=3,5`, ranks zero through two.
Compare arithmetic matrices, D1715 line equations and relation labels for
every listed generator. Check the source coefficients symbolically belong to
`R_p`; this is not a numerical complex-membership test.

Required real mutations, each with one first gate:

- omit the Weyl half-form coefficient;
- use `f_p` instead of `f_p^dagger` for the positive Fourier row;
- reverse the quadratic shear sign;
- omit the controlled momentum correction `b_1-b_2`;
- reverse the cup's standardized dual factor;
- replace the unnormalized loop `p` by relation truth `1`;
- assert normalized cups still have identity snakes;
- identify two unequal `R_p` source scalars projectively at source equality;
- admit an arbitrary complex scalar as an `R_p` coefficient;
- classify `m_(F_p,2)` as Clifford.

Also test a nonzero source phase pair with equal CP realization but distinct
source equality, and a non-unit scalar pair with distinct CP probabilities
but one projective class. Passing is finite evidence only.

## Data actually required for a scalar-retaining geometric lift

A weighted pair `(R,c)` is insufficient unless every intertwiner line has a
coherent chosen basis. The positive target should instead provide:

1. a one-dimensional complex Hermitian amplitude line `A(R)` for every
   nonempty affine Lagrangian relation and the zero space for the empty one;
2. bilinear composition maps
   `A(S) tensor A(R)->A(S o R)`, with the zero map for empty composites,
   associative on triples and retaining intersection/excess factors;
3. tensor comparison maps and conjugate-linear dagger maps compatible with
   the D1702 factor order;
4. chosen cup/cap elements whose snakes and closed loop record their actual
   scalars, plus separate admissible normalized branch elements;
5. a Hermitian norm so `T^*T<=1` and ordinary-trace probabilities are
   meaningful;
6. on `G_p^arith` only, an `R_p`-form/lattice mapped to the arithmetic
   coefficients and selected generator vectors.

The D1715 semantic lines and their multiplication give a benchmark for these
axioms, not a geometric construction. A later definition must build the
lines and composition factors from finite symplectic/determinant,
half-density or Gauss data and prove comparison with D1715. SP-LW14's excess
index motivates retaining intersection data but does not supply this finite
probability normalization.

Do not define the answer as `A_I/ker(H)`: that quotient merely forces
realized-map faithfulness, erases source distinctions by construction, and
does not establish geometric canonicity, coefficient descent, fullness, or
physical normalization.

## Exit and following decision

Freeze the definition, table expectations and mutations before the single
prover/review/repair loop for `RL-GEN-MATCH`. If the table passes, use its
actual loop and composition constants to choose a geometric amplitude-line
candidate in a separately registered definition. If it fails, narrow the
matched fragment or correct the generator convention; do not widen to the
full arithmetic source.

This bounded comparison advances DG-REL-LIFT by fixing the scalar data that
must survive. It does not close DG-REL-LIFT, DG-CHAR2 or DG-GLOBAL and carries
no modular or spectral consequence.
