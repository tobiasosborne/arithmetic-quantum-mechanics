# F1 sidequest: exact example expectations and mutation reachability

Specification opened in `briefs/f1-sidequest.md` before the proof arrived;
extended to crowds, frame qubits, fusion and normal maps as those independent
literature routes were examined. No gate promotes a mathematical claim.

Command: `python3 theory/checks/f1_check.py`. Python standard library only;
no tolerances. Monomial phases are integer exponents. Character sums reduce
integer polynomials modulo the cyclotomic polynomial, including composite
levels four and six. None of the checks interprets q=1 as a limit of fields.

| gate | independent comparison | expected green result | mutation, first run failing |
|---|---|---|---|
| M1 | monomial composition against ordered cocycle | exact product for nine configuration/phase pairs | `--red-cocycle`: reverses cocycle; fails first at C3 |
| M2 | enumerate radical of the commutator pairing | only zero phase vector | `--red-pairing`: trivial pairing; fails at C2 |
| M3 | trace Gram matrix from actual operator entries | diagonal equal to configuration cardinality | `--red-basis`: duplicate Weyl element; fails off diagonal |
| M4 | enumerate dual labels from independent ring multiplication; compare D8/D16 entries | correct sign/order for five smallest local rings | `--red-order`: XZ for ZX; fails at F2 |
| M5 | raw central map image and kernel sizes | F4 raw order 64, image 32, kernel 2 | `--red-kernel`: claims faithful raw map; fails at F4 |
| M6 | tensor actual C2 and C3 monomial entries at common level 6 | agrees with product-configuration operator | `--red-tensor`: phase mismatch |
| M7 | Fourier support and exact Gram sums | full support, Gram cardinality times identity | `--red-fourier`: asserts monomial support |
| M8 | enumerate subsets and compare divided-power coefficients | binomial(m+n,m), 0≤m,n≤6 | `--red-hall`: discard multiplicity at (1,1) |
| M9 | creation/removal coefficients and finite-cutoff trace | CCR on tested polynomial vectors; top-state defect at a cutoff | `--red-ccr`: equate multiplicities |
| M10 | expand actual 3x3 matrix triples; compare band null formulas and crowd axioms | signed: 27 points, 319 triples, 23 inverse-bearing points; Krasner: 8 points, 152 triples, nonunique inverses | `--red-crowd`: require noncyclic permutation as well |
| M11 | enumerate projective frames and actual Kronecker image | at N=1: 3,15,9,6; at N=2: 4,40,16,24 (one/full/product/nonproduct) | `--red-frame`: declares all composite rays products |
| M12 | exact order-eight group squares and character products | four tensor-square summands; indicators +1/-1 for D8/Q8 | `--red-fusion`: equates indicators |
| M13 | enumerate normal maps and inspect realized entries | every matrix unit at ranks 2,3,4; seven partial maps at rank 2 | `--red-normal`: retains only bijections |

Configuration seeds: trivial group at level 1; C2/2, C3/3, C4/4,
(C2×C2)/2, C5/5, C6/6, (C2×C3)/6, and C2/4.
Ring seeds: F2, F3, Z4, F4=F2[a]/(a²+a+1), F2[e]/(e²).
The dual-number character in this checker takes the e coefficient; it is
explicitly named and generating, but differs from the reference character
chosen in the earlier smallest-rings display. No hidden equality is claimed.

Each mutation was run before the corresponding green acceptance run and
failed at the named gate. The checker advertises every mutation in --help
for the repository's session-close discovery. The final session-close log
is a local execution record, not a committed artifact.

Limits: M7 does not enumerate the entire strict normalizer; its general
classification is established by the separate reviewed proof. M9 is an
exact finite probe of a polynomial identity, not a Hilbert-domain proof.
M10's finite examples do not prove algebraic representability. M11 uses
the frame's factorization definition, without assuming physical
probabilities. M12 does not establish the full classification of tensor
categories; that identification is sourced to Shimizu.
