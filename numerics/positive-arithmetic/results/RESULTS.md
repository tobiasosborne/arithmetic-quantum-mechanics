# Positive arithmetic counting theory — verification and delivery

**Final result: P1--P7 green; all 16 advertised red CLIs exit one at their
intended mathematical gates.** No floating tolerance is used. The recorded
initial `--red-mass` failed before any green run; see RED-FIRST.json.

Native inherited Codex verifier runtime. No exact backend model identifier
or separate reasoning override is asserted. No nested CLI/subagent, trunk
edit, git action, or imported prover/old-checker implementation was used.
The preregistration and its dated interface supplements are in EXPECTATIONS.md.

The recorded CLI commands ran in the isolated verifier lane; the installed
checker has the identical mathematical source and SHA256.

The checker is standalone stdlib plus numpy. Its final SHA256 is
`272148e1bf157e15d682408b92fe8eeaf43d4849b027ab64b70eaea6c5e03718`.
CLI-RESULTS.json records exact commands, exits, mathematical failure paths,
help output, and checker/expectation hashes. results.json is the complete
positive output. Run `python3 theory/checks/positive_arithmetic_check.py` from the repository root;
`--help` lists all `--red-<name>` modes and optional `--only Pn` group selection.

## Independence and exact finite scope

Polynomial fields are computed from their displayed moduli and verified by
`a^(Q-1)=1` for every nonzero quotient element. Embeddings are found from
polynomial roots, relative traces from Frobenius powers, and exact-period
classes from actual field permutations. Period polynomials are derived by
recursive subtraction of proper-divisor fixed counts, independently of the
Jordan-product coefficient formula. Taylor coefficients come from expanding
the exponential monomials, through grade six.

Fourier entries lie in an exact cyclotomic ring Q(zeta_p), reduced in the
basis 1,...,zeta_p^(p-2); phase operations use p=2,3,5. Sparse vectors retain
an explicit squared normalization denominator, so square-root amplitudes and
Born probabilities are tested exactly. The primitive root is the fixed
generator of that ring, consistently used at each level of a diagram.

| Group | Positive assertions | Exact bounded data |
|---|---:|---|
| P1 | 779 | p=2,3,5; r=1..4, Q<=625; t in {1,6/5,3/2,2,3,p}; every Frobenius power modulo r; grades 0..6 |
| P2 | 112 | F2->F4, F2->F8, F4->F16, its Frobenius-twisted embedding, F3->F9, F3->F27; density t=1,6/5,p; coefficient grades 0..6; twisted F2->F4->F16 tower |
| P3 | 11 | Actual generic F2->F8 joint support, rational t=1,6/5,3/2,2 |
| P4 | 104 | Six full mixed protocols listed below; coherent-control and leave/return examples over F4 |
| P5 | 52 | F4 reference words of m=1,2,3, grades 0..6; multiple Kraus and entangled output; F4/F2 coefficient-state tensor grades 0..6; two qubit CP process series |
| P6 | 64 | F2,F3,F4,F9; arities 1,2,3; t=6/5,p; active Taylor grades through 3; F4 multiplication-table and relative-Frobenius probes |
| P7 | 5 | Degree two at p=2 versus p=3, retaining full register and reference data |

These bounds are finite falsifiers. They establish neither all-real positivity
nor the all-field/all-CP theorem; those depend on the written derivations and
capped review. In particular they do not establish a varying-characteristic
category or a characteristic-independent endpoint.

## Positive state and the older chart continuation

The new reference passes normalization, interior faithfulness, exact uniform
comparison at t=p, and all tested Frobenius moments. Its coefficient traces
are r^k/k!, and all positive-grade coefficients are faithful on the nonzero
labels. Conditional moving-period masses recover the FRL weights.

All tested J restrictions and towers agree, including singular degrees and
the twisted embedding. Both Fourier-transported decoder branches agree with
their actual matrix conjugates. Fourier carries the zero endpoint to its
uniform coherent vector; this is not invariance of the chosen reference.

On the actual F2->F8 complementary projection, the new state gives expectation
**11/54** at t=6/5, while the old formal tracial complement is **-7/18**.
At the arithmetic point t=2 both give 1/2. The new reference is nontracial:
its expectations of E_0a E_a0 and E_a0 E_0a differ. This does not identify
the new state family with the older varying-matrix M2 chart continuation.

## Full mixed arithmetic and coherence

For each embedding choose actual a,b satisfying T(ab)=0 and T(a^q b)=1.
The tested circuit is the complete D1507 interface: select reference labels
a,b,0; use target V; relative Frobenius on the first control; multiplication;
target Fourier; retained J decoding; target F_K* on success. The controls
and all success/failure quantum outputs are retained.

Every row gives target **1** with decoder success **1**. Omitting relative
Frobenius or multiplication instead gives target **0**, still with success
one. The leading rare-preparation coefficient is computed from the input
density coefficients, not fitted to the output.

| K->E | a,b in the checker's polynomial labels | Rare order/coefficient | Success after target dephasing | Success with F_E omitted |
|---|---|---|---|---|
| F2->F4 | 2,3 | 2; 1/4 | 1/2 | 0 |
| F2->F8 | 2,2 | 2; 1/9 | 1/4 | 1/4 |
| F4->F16 | 2,3 | 2; 1/36 | 1/4 | 0 |
| F3->F9 | 4,4 | 2; 1/36 | 1/3 | 1/3 |
| F3->F27 | 3,9 | 2; 1/144 | 1/9 | 0 |
| F5->F25 | 6,14 | 2; 1/400 | 1/5 | 1/5 |

The dephased protocol still has successful target 1, but success drops to
1/kappa. With F_E omitted in the invertible-degree cases, the conditional
target is the actual Fourier state F_K*|1/n>, whose computational probabilities
are 1/q; it is not a deterministic basis label. Both failure probabilities
and this conditional phase information are checked.

A coherent F4 control superposition survives the entire mixed circuit with
rank-one return one, versus 1/2 if its output coherence is erased. A separate
coherent three-register F4 state leaves the moving sector under M and returns
under M again: full return is one, intermediate compression gives zero, and
the retained failure history returns coherently with probability one.
An actual field phase changes its rank-one Born return from one to zero.
Changing the multiplication-gate table entry (alpha^2,alpha^2) from alpha to
zero changes the full protocol output and fails P6. The field's validated
Fourier/trace tables are fixed while that gate datum is corrupted.

For F2->F4, the vector w=(0,0,1,-1) lies outside the old joint J/V support
and relative Frobenius sends it to -w. Its coherence with the zero ket gives
Born return 1/9 after Frobenius, versus one before. Its rare support has order
one and leading mass 1/2. Active multiplication has the tested order d and
conditional squared difference two; this is an arity diagnostic, not an
independent proof of a general Clifford-level classification.

## Finite operational profiles and preparation dependence

For all tested fixed CP branches, D-word coefficients and the finite L-word
profile have the same first nonzero **matrix**, event order and normalized
conditional density. Every grade 0..m is exercised for m<=3, with direct
coefficients computed through grade six. A two-register branch prepares an
entangled Bell endpoint; a sum of two Kraus branches also passes.

A first postselection retains |00> and |alpha,alpha>. Its leading conditional
state alone is |00>, which loses a subsequent rare |alpha,alpha> outcome.
The retained finite profile gives the correct subsequent order two and
coefficient 1/4. Deliberately truncating the total series at order one also
loses this outcome and fails. Equality of leading records is not equality
of the exact and profile preparations at finite positive h.

The Cauchy coefficients are independently compared with expanding the whole
product as a polynomial in t before substituting exp(h). Coefficient-state
tensor weights obey the exact binomial law. Two positive qubit CP process
series have normalizers 1+h and 1+2h, with the tested product normalizer,
pointwise composition, and cross-multiplied equality after a common positive
scalar factor. These finite tests do not by themselves prove the abstract
positive-series category.

The nonzero diagonal x=y on **independent** F4 references has order two and
leading coefficient 3/2. The same projector after the actual copy isometry
of one reference has order one and coefficient two. At t=6/5 the independent
probability is **43/1296**, whereas naive point-count continuation would give
**275/1296**. The new independent state does not preserve that naive counting
formula on arbitrary mixed loci; the prover's scope explicitly needs this
distinction.

## Residual dependence on retained characteristic

For degree two, the nonzero conditional endpoint is B_E/2. Its fixed-period
and moving-period masses are each 1/2 at both p=2 and p=3. The first conditional
Frobenius moment consequently agrees. The full quantum data do not agree:

| Observable/data | p=2 | p=3 |
|---|---:|---:|
| Register dimension | 4 | 9 |
| Probability of a specified nonzero prime-field label | 1/2 | 1/4 |
| Probability of a specified period-two label | 1/4 | 1/12 |
| Nonzero conditional-state purity | 3/8 | 1/6 |
| Zero-test probability after Fourier of the zero endpoint | 1/4 | 1/9 |

The zero reference endpoint and degree-moment formulas have their stated
common forms, while conditional densities, individual probabilities and the
arithmetic circuit tables retain p. No automatic identification is made.

## Red paths

Every row is an actual CLI exit one with a mathematical Failure result.
No red is accepted merely because an interpreter exception occurred.

| Flag suffix | First failed gate/detail |
|---|---|
| mass | P1 state normalization and positivity |
| jordan | P1 exponential derivative versus Jordan coefficient |
| moment | P1 all Frobenius power moments |
| embedding | P2 named inclusion density restriction |
| fourier-invariance | P2 Fourier transported code reference |
| tracial-complement | P3 positive new-state complement expectation |
| compression | P4 full return retains intermediate sector leakage |
| coherence | P4 coherent trace-fibre decoder success |
| fourier-phase | P4 full mixed target protocol |
| profile | P5 finite-profile leading matrix |
| total-first-order | P5 finite-profile leading matrix at a grade-two event |
| discard-later-rare | P5 later rare branch survives full profile |
| normalizer | P5 process normalizers multiply coefficientwise |
| multiplication-entry | P6 actual multiplication-table entry is observable |
| arity | P6 actual active-control mass and arity |
| erase-characteristic | P7 Fourier-zero observable retains characteristic |

All seven aggregate gates have reachable, distinct mathematical mutations.
Earlier failures within a group do not certify every later assertion in that
group independently; the exact assertion counts and paths are retained in
CLI-RESULTS.json. No claim promotion is authorized by this verifier output.

## Admission and final integration

All six POS claims are PROVED after the capped review and the D-versus-rho
coefficient wording repair. The ordinary Taylor coefficients of D_E are
positive; rho_E is the normalized Poisson mixture. The full state and
finite profile are not equal at finite h. Review/adjudication are in
`theory/verdicts/positive-arithmetic-r1.md` and
`positive-arithmetic-adjudication.md`.

The final repository run passes 22 green checkers and 190 advertised
mathematical mutation runs. `SESSION-CLOSE.json` records the exact final
inventory and source/PDF hashes. `relative-moments.json` mechanically checks
the coefficient-one corollary gcd(n,j)/n, extracted from the reviewed
Frobenius moment. The new figure is generated by
`scripts/plot-positive-arithmetic.py`; its positive curve is the explicit
F2->F8 reference calculation, not a fitted numerical model.

The goal's declared result and remaining dependence are in
`docs/research-plans/positive-counting-result.md`. The new theory supplies
one rigorous nontrivial counting/graded boundary with retained arithmetic
labels. It does not promote MIX-ALL or claim an intrinsic characteristic-one
operator category. All new labbook pages and the figure were rendered and
visually inspected before publication.
