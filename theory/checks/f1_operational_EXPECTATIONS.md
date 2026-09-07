# Operational F1 examples — finite expectations and live mutation gates

The scope was opened in briefs/f1-operational-target.md before the core
proofs arrived. Run:

    python3 theory/checks/f1_operational_check.py

The checker uses Python's rational Fractions and integer/object NumPy
arrays. It does not use floating point or tolerances. Sparse Hecke-basis
arithmetic is compared with independent finite-field flag matrices and
explicit state/process formulas.

Each H-gate is a **single final acceptance conjunction** of its diagnostic
probes. All probes run, including on mutated data; no diagnostic short
circuits the later ones. Mutation coverage below means every mathematical
acceptance gate is live. It does not mean every line, diagnostic predicate
or possible mathematical error has been independently mutated. This is
the consolidation alternative requested in critic objection O2.

## Green expectations

| Gate | Mathematical comparison and exact scope |
|---|---|
| H1 | Hecke relations, star and reduced products at q=1,2,3,5,1/2, n=2,3,4; all associativity triples at n=3 |
| H2 | All basis-pair trace Gram entries and positive diagonal for those parameters/ranks |
| H3 | The 2+2 block inclusion into H4 at q=1,2,3,1/2, its coefficient expectation, bimodule identities and selected two-by-two amplified positive inputs |
| H4 | Central sectors of dimensions 1,1,4; unlabelled overlap q/(q+1)² and marked trace 1/(q+1), at the displayed rational parameters |
| H5 | Normalized full density, isolated identity action and ambient return probability (1−2q/(q+1)²)² |
| H6 | The unitarized generators obey braid at q=1 and have the computed nonzero defect at the other sampled parameters |
| H7 | Arbitrary injection relabelling, composition and subgroup coefficient expectations in the finite set examples |
| H8 | Retained Kraus normalization, stable scalar mixing, ambient trace and parallel normalization |
| H9 | Independently enumerate 21 flags over F2³ and 52 over F3³; verify adjacency, normalized Gram, partial-flag incidence, and the six coordinate-apartment flags against the regular S3 matrices |
| H10 | The discarded Temperley–Lieb ideal is nonzero with positive coefficient-trace weight; the quotient relation has the specified parameter |
| H11 | n=2,3 and q=1,2: context size 2n−1, distinct reduced products, normalization, positive Born witness and sharpness at all smaller possible ambient sizes. Gaps: 1/2, 1/18 at q=1; 2/9, 1/441 at q=2 |
| H12 | All partial maps between sets of sizes 0 through 3: reference reset, composition and trace dagger; also the specified small disjoint-block naturality comparisons |
| H13 | Parabolic corners at q=1,2 and n=3,4: projection, normalized trace, refinement and concatenated corner tensors |
| H14 | Exact C[S6] Bell projection, full density 9P, a marginal (3/2)z, and XX=ZZ=1 with crossed correlations zero |

The H3 sample is not a census of every parabolic inclusion through level
five. H11 reaches level five only for its selected contextual expressions.
H14 uses the exchange symmetry of its formula for the second marginal;
it is not a census of all two-region states. The general proofs have their
own hypotheses and quantifiers, independent of these finite checks.

## Data mutations

Every listed mode was observed failing before its corresponding acceptance
run. The final run of all modes requires exit one, a mathematical FAIL
diagnostic and empty stderr; an accidental interpreter exception does not
count as successful falsification.

| Mode suffix after --red- | First failed gate/diagnostic | Changed data or mathematical expectation |
|---|---|---|
| product | H1 quadratic relation | Perturb the descent multiplication coefficient |
| trace | H2 trace Gram | Give nonidentity basis data trace weight |
| expectation | H3 expectation bimodule identity | Double retained nonidentity coefficients |
| overlap | H4 overlap | Erase the q-dependence |
| local-collapse | H5 context Born probability | Identify isolated channels before extension |
| unitary-braid | H6 braid defect | Demand braid after generator unitarization away from one |
| injection | H7 injection image | Ignore the specified injection image |
| kraus | H8 normalization | Use an unnormalized local list |
| flag | H9 panel quadratic | Add self-adjacency to flag data |
| tl-trace | H10 quotient identity | Discard the nonzero ideal contribution |
| context-size | H11 distinct contextual images | Demand recovery in an insufficient context |
| partial-zero | H12 empty-map unitality | Replace the reference reset by zero CP |
| corner-trace | H13 normalized corner trace | Omit the corner normalization factor |
| positive-domain | H2 strict positive diagonal | Include the negative parameter −1 |
| amplified | H3 amplified positivity | Use the nonpositive unital traced map 2 tau(·)1−E |
| density-norm | H5 full density normalization | Omit its standard-block trace scale |
| kraus-mix | H8 scalar-isometry equivalence | Mix Kraus indices by a nonisometry |
| incidence | H9 partial-flag incidence | Forget the wrong subspace |
| context-lower | H11 sharp lower bound | Extend the indistinguishability demand to the separating context |
| partial-dagger | H12 trace dagger | Use a partial map instead of its inverse |
| partial-comp | H12 partial-map composition | Omit the second factor |
| partial-lax | H12 lax naturality | Drop a wire from a disjoint assembly |
| refinement | H13 refinement containment | Reverse the refinement inclusion |
| bell-sign | H14 Bell projector | Reverse the antisymmetric correlation sign |
| apartment | H9 apartment isometry | Duplicate a coordinate-apartment flag |

All twenty-five modes are advertised through --help for recursive
session-close discovery. No checker result changes a claim's status:
the reviewed structured proofs establish the PROVED rows, while the
general-q context, partial-flag, Bell and apartment rows remain SKETCH.
