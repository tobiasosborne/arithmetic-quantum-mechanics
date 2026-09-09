# General Galois embedding registers — hostile verdict

Date: 2026-09-09. **Same-family prover/critic, target-blind lane.**

Model metadata: native inherited Codex runtime; this lane has no separately
verified backend model identifier or reasoning override to report. No nested
CLI, model override, or subagents were used. The prover artifacts likewise
report native inherited Codex execution; no cross-family independence is
claimed.

**Context limitation:** a fresh reviewer thread was unavailable because the
runtime reached its thread limit. Root reused this earlier orbit-review
context. That context contained no Galois prover reasoning. This review read
only the Galois artifacts, definitions/registries, brief, local sources, and
verifier interface. Thus target blindness was preserved, but this was not a
fresh-context critic. The already adjudicated FRL repairs were not re-reviewed.

Scope: the three proposed SKETCH rows `GAL-FUNCTOR`, `GAL-DESCENT`, and
`GAL-IMAGE`; D1401--D1405; both Galois shards and the labbook draft. The
shared checker was frozen at SHA256
`df49c8f3149c4ae896290c8a9514a5042e5b81c1af2e68d1b20c6a9521f46e62`.
The lane copy and verifier's live file had this same hash after testing.

## Decision

**PASS. No FATAL, MAJOR, or MINOR objection remains on the stated claims.**
The written proofs establish the uniform statements, rather than inferring
them from the finite samples. This supports admission of all three claims
at their proposed scope. The two NOTE findings below preserve material
scope boundaries; neither requires repair.

## Numbered hostile findings

### N1 — NOTE: replacing constant rank by arbitrary étale maps breaks the rule

**(a) Location.** `DEFINITIONS-PROPOSED.md`, D1401, lines 11--15;
`embedding-functor.md`, Section 1, `<1>2.<2>1`--`<2>3`, lines 44--56, and
`<1>6.<2>1`--`<2>2`, lines 100--110. These restrictions agree with
`CLAIMS-PROPOSED.md`, GAL-FUNCTOR, line 8, and labbook lines 37--39, 69--71.

**(b) Independent attack.** Over any field K, the split étale map
`K^2 -> K^3`, `(a,b) -> (a,b,b)`, has embedding restriction `[0,1,1]`.
Its incidence Gram matrix is `diag(1,2)`, so no common positive scalar
normalizes both columns. Individually normalizing these fibres, then
composing with the normalized `2->1` pullback, gives squared coefficients
`(1/2,1/4,1/4)`, whereas direct normalized pullback from three points to one
gives `(1/3,1/3,1/3)`. The proposed category correctly excludes this map.
Conversely the allowed module ranks multiply under both composition and
tensor, and therefore do not produce this defect after closure.

**(c) FIX DEMAND.** None; retain the existing constant-positive-rank
condition and its all-components meaning during integration.

**(d) SURVIVING STATEMENT.** GAL-FUNCTOR survives unchanged for all permitted
étale maps and all finite separable field towers. It does not extend by the
same normalization to all finite étale algebra homomorphisms.

### N2 — NOTE: full stopped histories must not be collapsed into a binary decoder

**(a) Location.** `DEFINITIONS-PROPOSED.md`, D1403, lines 54--62;
`embedding-functor.md`, Section 3, `<1>14.<2>2`--`<2>3`, lines 221--232, and
`<1>15.<2>1`--`<2>2`, lines 237--246; labbook lines 181--185, 202--208.

**(b) Independent attack.** In the cyclic tower 1|2|4, write the normalized
isometries s,t and put `R=t Q_s t*`, `Q=I-tt*`. In the ordered four-point
basis, `v=(1,-1,1,-1)` lies in Ran(R), while `w=(1,1,-1,-1)` lies in Ran(Q).
Both have squared norm four and they are orthogonal. For
`rho=|v+w><v+w|/8`, binary failure preserves rho and has return probability
one. Re-encoding and merging the stopped failure histories gives
`R rho R+Q rho Q`, with return probability **1/2**. Both outputs have trace
one. This independent equal-sector witness differs from the submitted
checker's valid 5/9 witness and confirms the typed-history scope.

**(c) FIX DEMAND.** None; preserve every indicated failure register and tag,
and retain the explicit exclusion of full binary-decoder equality.

**(d) SURVIVING STATEMENT.** Exact success-map tower composition, stopped
CPTP histories, and all independent paired outputs survive unchanged.
Discarding history labels cannot restore coherences erased by measurement.

## VERIFIED CORRECT — do not churn these statements in integration

```text
V1. UNIFORM FIBRES AND THE CATEGORY, OVER EVERY BASE FIELD.
After scalar extension, the finite etale algebra A is Omega^(X_A), with
|X_A|=dim_K A. An allowed algebra map acts by coordinate repetition along
R_f. The component idempotent at sigma therefore cuts out exactly the
Omega-vector space on R_f^(-1)(sigma). B~A^r makes its dimension r on
every component. This proves uniform surjectivity, n_B=r*n_A, and
injectivity of the allowed algebra map without choosing a module basis.

For a finite product of fields, finite locally free constant rank r is
equivalent to a free module of rank r: take a vector-space basis on each
factor to prove existence, without using it in s_f. Composing module
isomorphisms gives rank multiplication. Tensoring them over K gives
B tensor D~(A tensor C)^(r_f*r_k). Finite etale tensor closure, nonzero
dimensions, and rank-one structural algebra isomorphisms give precisely
the symmetric monoidal category claimed. Every finite separable field
tower belongs to it, including towers over imperfect fields.

V2. DIRECTION, EXACT NORMALIZATION, AND FAITHFULNESS.
Algebra f:A->B gives the restriction R_f:X_B->X_A. Its Hilbert pullback
s_f goes H_A->H_B, so it is covariant in algebra maps. Disjoint fibres
give s_f* s_f=I. In a composite each top embedding has exactly one
intermediate restriction; hence its coefficient is 1/sqrt(r_f*r_h),
not a multiple of that coefficient. This proves strict tower equations.
Every row of the nonnegative incidence matrix names its unique source
label. Equality of s_f and s_k recovers R_f=R_k and then f=k by the
registered embedding-set anti-equivalence. Faithfulness is not fullness,
and no reconstruction from an unmarked abstract matrix algebra is claimed.

V3. MONOIDAL AND CLOSURE COMPARISONS.
An algebra map A tensor_K C->Omega is uniquely a pair of maps from the
factors. Its restriction fibres are Cartesian products, so the positive
square roots multiply exactly. On any ordered tensor tuple every route
sends the tuple to product_j sigma_j(a_j); this proves naturality and
the pentagon, unit, and symmetry diagrams on all basis vectors.

Postcomposition by a named closure isomorphism eta bijects embedding
sets and restriction fibres and preserves those coefficients. It obeys
W_eta U(g)=U'(eta*g*eta^-1) W_eta and W_theta W_eta=W_(theta eta).
If eta' differs, W_eta'=U'(eta' eta^-1) W_eta. Conjugation takes finite
point stabilizers to finite point stabilizers, hence also transports the
Krull topology. No unique closure comparison is asserted or needed.

V4. GALOIS-EQUIVARIANT CPTP DESCENT.
Each Kraus conjugation is positive under every matrix amplification.
The retained decoder amplitudes are s_f* and Q_f, so their squared sum
is P_f+Q_f=I. The encoder satisfies s_f* s_f=I, and success is TNI.
Equivariance of s_f makes P_f,Q_f invariant and intertwines both output
branches in their different, explicitly named types.

D_f(E_f(rho))=(rho,0). For I/n_B, success is I_(n_A)/n_B with probability
n_A/n_B=1/r_f and conditional density I/n_A. Rank-one arrows have zero
failure probability, with no division by zero prescribed. A stopped
two-step tower has amplitudes s_f* s_h*, Q_f s_h*, Q_h; their squared
sum is I. Refining any success output preserves completeness, proving
arbitrary finite stopped histories. Tensor Kraus completeness factors
as (P_f+Q_f) tensor (P_k+Q_k)=I on all inputs, including entangled ones.
Only the specified independent maximally mixed inputs force product
reference probabilities. No state-factorization claim is made for
entangled inputs, and the independent decoder retains four output types.

V5. NONABELIAN CORE AND THE ACTUAL NORMAL CLOSURE.
For a field A, embeddings form G_K/H by extension to the separable
closure. A group element fixes every coset iff it lies in every conjugate
of H. Fixing every embedding is the same as fixing every tau(A) pointwise,
and hence the compositum N_A pointwise. The compositum is finite separable;
its pointwise stabilizer is the open normal core C_A. Infinite Galois
correspondence therefore gives N_A/K finite Galois and
Im(U_A)~G_K/C_A~Gal(N_A/K), via the displayed restriction map.
Changing the chosen embedding conjugates H but does not change its core.

For a field arrow f:A->B every embedding of A extends to B. Thus all
conjugate images generating N_A lie in N_B, so C_B subset C_A and the
finite action images have the claimed canonical restriction quotient.
This works for named field embeddings, not only one chosen inclusion.

Independent nonabelian computations used S3 generated by a 3-cycle and
a transposition, with quotient g->g(2), rather than the submitted coset
ordering. The order-two stabilizer has trivial core, the three-point
action has image order six, and the six-to-three normalized pullback
has reference success 1/2. Every decoder matrix unit and both branches
intertwine the action. Two independent decoders have probabilities
(1/4,1/4,1/4,1/4). A second S3 test uses normal H=A3: its core has order
three, its image has order two, and success is 1/3. The core is not
being hard-coded to be trivial.

A concrete characteristic-zero field realization is Q(cuberoot(2))/Q.
The cubic has no rational root, hence is irreducible. With real alpha
and a primitive cube root omega, N=Q(alpha,omega) has degree six: adjoining
omega to the real cubic field has degree two. Cycling alpha to omega*alpha
and complex conjugation generate S3. The extension degree is three,
Aut_Q(Q(alpha)) is trivial, and the detected normal-closure group has
order six. Thus none of these three quantities has been conflated.

V6. PROFINITE RECOVERY AND SEPARABILITY.
Every finite Galois subfield E of Omega is an allowed object with normal
closure E. These fields are directed by composita and their union is Omega.
The admitted restriction maps are the finite Galois inverse-system maps.
Compatible automorphisms on these fields define one automorphism on the
union: values agree in a common finite level, preserve field operations,
and have a compatible inverse. This proves the set/group inverse-limit
identification. Finite-level kernels give exactly the Krull neighbourhood
basis, proving the topological identification as well.

Nothing here supplies an infinite-dimensional Hilbert register or Haar
data, or reconstructs G_K from bare unmarked matrix algebras. A finite
nonseparable field cannot embed into K^sep, because the image of every
element would be separable over K. The theorem correctly excludes it.
Its scope includes every finite separable extension over every imperfect
base; it does not require perfectness of that base.

V7. FINITE-FIELD CYCLE COMPARISON AND TRANSFERS.
Over F_p, the d embeddings of a degree-d field are Frob_p^j tau_0.
Evaluation at a primitive element is injective because that element
generates the field, and its image is exactly the length-d orbit.
It transports Frobenius to S_d and ordinary normalized block density
I/d to I/d. Origin and primitive-element changes give precisely the
explicit unitaries in the shard. No primitive multiplicative generator,
root of unity, field-vector-space basis, or ordering of all embeddings
is needed for the underlying construction.

An independent quotient-field calculation in F4, F9, and F25 constructed
the two actual algebra embeddings from the two roots of the quadratic
and checked primitive evaluation and Frobenius intertwining. The Hilbert
dimensions are 2, while the field-label dimensions are 4,9,25.
Characteristic two is included directly.

For d|e and a named embedding with Frobenius shift h, restriction sends
j to j+h mod d, so pullback selects j congruent to source-h. Direct
matrix tests covered all 1,325 shifted two-stage cyclic towers with top
degree <=12; incidence products and normalization ranks agreed. These
finite samples supplement the all-degree coefficient proof.

Independent tensor is degree multiplication and retains the full M_de.
The simultaneous cyclic action has gcd(d,e) orbits of length lcm(d,e),
but the cross-orbit matrix units remain quantum. The comparison is an
orbit-type and block-trace comparison, not D1301's cardinality register,
D1304's physical J/V, D1333's divisor-block map, or boundary mixture weights.
```

## Checker execution, symbolic audit, and mutation reachability

The unchanged shared checker was copied into this lane before execution.
Every actual CLI mode was run in a separate process, and all 22 reds exited
one at the intended mathematical gate. Green exited zero. Exact commands,
full outputs, counts and hash are in `checker-runs.json`. The other mixed
F/R/M gates were executed as part of that shared CLI contract; their
mathematical claims were not added to this Galois review's scope.

| Galois red | First failure | Reached counts at failure |
|---|---|---|
| `--red omit-normalization` | G1, S3 pullback squared norm | G1=1 |
| `--red coset-label` | G1, S3 regular/coset equivariance | G1=4 |
| `--red cyclic-only-image` | G1, S3 normal core and image | G1=8 |
| `--red omit-tensor-outcome` | G2, four typed outcomes | G1=231, G2=470 |
| `--red erase-orbit-coherence` | G2, cross-orbit Born coherence | G1=231, G2=6955 |
| `--red merge-tower-histories` | G2, tower merged failures lose cross terms | G1=231, G2=6959 |
| `--red admit-nonuniform` | G3, nonuniform normalized pullbacks fail composition | G1=231, G2=6960, G3=1 |

These seven are distinct mutations of normalization, coset data, acting
group, tensor tag list, quantum coherence, history output, and fibre data.
No entire G1/G2/G3 group is untouched by a red. A first failure does not
protect every later assertion in its group; the following audit distinguishes
actual mathematical comparisons from implied identities.

- **G1:** the incidence Gram, actual regular/coset equivariance, conjugated
  subgroup intersection and distinct permutation image genuinely use computed
  data. The reference success trace follows from the already checked Gram,
  and is not a second independent rank proof. The cyclic incidence product
  is independently compared with the direct quotient map. The named S3
  mutations die before those cyclic tests; the independent shifted-tower
  enumeration above supplies separate finite evidence.
- **G2:** matrix-unit traces, output equivariance, nonzero retained failures,
  four typed outcomes and completeness are actual matrix tests. Tensor
  matrix-unit factorization is the elementary identity for the constructed
  Kronecker matrices; it must be read together with single-decoder validity
  and the separate completeness gate. It is not an independent definition of
  some unspecified arithmetic tensor operation. The ternary direct incidence
  array checks the Cartesian indexing independently.
- **G2 coherence:** in green, `actual=rho`, so the first scalar assertion is
  `Tr(rho^2)=1`, not `rho==rho`. Along with the independently dephased return
  1/2 it tests the stated coherent full-matrix witness. No uncomputed
  reblocking channel is advertised here. Replacing the pure state data with
  its diagonal part fails this gate, as independently verified below.
- **G2 histories:** the actual typed Kraus list has its own completeness
  test. The later comparison of stopped versus binary failure is a genuine
  comparison of distinct maps on a fixed input. The named history red reaches
  that comparison. Its final-success transpose equation is algebraically
  forced once the incidence tower equation is valid; it is not a new proof
  of tower normalization.
- **G3:** the nonuniform example compares nonidentical rational column
  squares. Its common-scalar impossibility follows from the two unequal
  diagonal Gram entries, not merely from a slogan about finite maps.
  The submitted late F4 dimension sentinel runs during full green in
  `finite_fields`, not in the `--red admit-nonuniform` route. No dedicated
  original red first-fails at that sentinel. Independent actual embedding
  computations for p=2,3,5 verify that comparison directly; the universal
  degree/cardinality distinction remains a written proof.

The shared green counts were G1=231, G2=6960, G3=3, F1=61, F2=1212,
R1=3, R2=131, F3=22, R3=16, M1=5. The remaining reds all exited one at:

| Mutation | First failing gate/detail |
|---|---|
| trace-fibre-label | F1 actual F2->F4 trace-fibre Gram |
| wrong-gram-branch | F1 squared singular spectrum |
| omit-degree-scaling | F2 logical D_n correction |
| fourier-sign | F2 F_E J = V F_K character/scalar equality |
| fourier-scaling | F2 F_E V = J F_K character/scalar equality |
| wrong-failure-projector | F2 Fourier decoder retained failure amplitude |
| residual-fourier-reflection | F2 residual Fourier block retains logical reflection |
| physical-support-rank | R1 generic physical support complement must be negative near one |
| compress-mixed-transition | M1 intermediate compression changes M^2 return |
| omit-tangent-normalization | R2 tangent/Fourier involutions |
| collapse-tangent-algebra | R2 tangent/Fourier involutions |
| tangent-fourier | R2 induced chart Fourier interchanges the two projections |
| incomplete-tangent-instrument | R2 tangent instrument completeness |
| tower-degree-scaling | F3 actual F3->F9->F81 corrected transfers compose |
| tower-connector-coefficient | R3 connector squared coefficients normalize |

### Independent data mutations on copies

`independent_probe.py` imports no submitted helper. It also makes the
following separately mutated copies of the frozen checker; every listed
failure is a mathematical assertion, not an interpreter exception:

| Ground-truth data mutation | Exit and actual gate |
|---|---|
| Keep all four tensor tags but zero the actual sf Kraus numerator | 1, G2 tensor Kraus completeness; gets past tag-count gate |
| Replace the pure cross-orbit rho by its diagonal part | 1, G2 cross-orbit Born coherence |
| Change nonuniform fibre data from (1,2) to (1,3) | 1, G3 individual pullback remains isometric; gets past first nonuniform gate |
| Zero the intermediate-failure numerator in the actual three-history list | 1, G2 actual typed stopped-history Kraus completeness |
| Independent probe substitutes binary output for stopped-history data | 1, independent HISTORY_DATA Born gate |

Reproduce with
`python3 theory/lanes/arithmetic-limits/galois-critic/independent_probe.py`.
Its mathematical positive calculations exit zero; its separate history red
exits nonzero. Full mutation records are in `independent-mutations.json`.

## Quantifiers, canonicity, reliance, and lockstep

**Quantifiers.** GAL-FUNCTOR and GAL-DESCENT cover every field K, every
nonzero finite étale object, every permitted constant-positive-rank map,
and every finite allowed tower/tensor word. The proof uses neither a
characteristic restriction nor perfectness. GAL-IMAGE covers every finite
separable field extension; its normal closure may be nonabelian. The
profinite assertion uses the whole directed set of finite Galois subfields,
not a bounded list. The finite-field orbit comparison is stated over F_p
for every prime p and degree d. Inseparable and infinite algebraic degree
are outside the finite-register claim, explicitly, rather than silently
treated as finite separable degree. General base-change functoriality,
Fourier/Haar data, and full arithmetic gate limits are not claimed.

**Choices and source/target.** K and a separable closure are named; a closure
comparison eta is named when used. The basis is indexed by embeddings with
counting measure, requiring neither an ordering nor a K-basis of A. The
positive real square root fixes transfer phases over C independently of the
characteristic of K. Tensor comparison is the canonical Cartesian map.
Galois stabilizer calculations name tau_0; the resulting normal core and
normal closure do not depend on it. The primitive comparison additionally
names a primitive element and cyclic origin, with explicit transport under
changing either. External outcome tags and their quantum types are retained.
The functor's source and target and its actual naturality equations are
specified. No unnamed canonicity choice was found.

**Reliance.** The source bodies registered as STACKS-04JI, STACKS-0BMI and
MILNE-FT-5.10 were read at the cited results: Milne 8.6--8.10, 8.20--8.21,
6.10, Remark 3.18, and 4.19--4.23; Stacks 58.2.2 and 9.22.2--9.22.4.
They contain the exact algebra/Galois equivalence, closure, and inverse-limit
inputs used here. The Hilbert normalization, CP, and history arguments are
local derivations. No unregistered result, REFUTED row, or v0.1 assertion
is needed. D1327 is used as a schema and is also rechecked directly in full
complex matrices; there is no claim of an arithmetic source realization.
D1331--D1332 are only the cycle-block definitions for the comparison.

**Lockstep/status register.** The proposed definitions, notation, three
claim rows, both structured-shard headers and labbook's three theorem
macros agree in strength and remain SKETCH/pending review. All material
conditions occur in the statements or their adjacent explicit scope:
constant positive rank, named closure comparison, full quantum orbit
coherence, retained histories, all finite separable bases, normal-closure
image, and degree versus cardinality. The nearest admitted FRP/FRL rows are
PROVED in trunk with their own stated scopes. This package does not borrow
their status or silently import their field-label comparison maps. The
integration PATCH preserves review/status lockstep and permanent provenance
paths. No statement or status divergence requiring a repair was found.

One bounded hostile pass is complete. No repair wave is demanded for this
Galois package; root may adjudicate admission at exactly its current scope.

PASS
