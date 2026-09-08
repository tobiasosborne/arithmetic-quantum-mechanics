# Blind adversarial verdict: arithmetic Frobenius/hierarchy package

Date: 2026-09-08. Same-family prover/critic, **blind lane**. Critic used the
native inherited model and reasoning settings; exact model metadata is not
available from the orchestration interface. No model override, nested agent,
prover conversation, or request for prover reasoning was used.

Reviewed targets, in full: the frozen `DEFINITIONS-PROPOSED.md`,
`NOTATION-PROPOSED.md`, `CLAIMS-PROPOSED.md`, `foundation.md`,
`transfers-example.md`, `hierarchy.md`, and `labbook-draft.tex` under
`theory/lanes/frobenius-hierarchy/algebra/`. All target locations below refer
to those frozen artifacts, not subsequently integrated trunk copies.
Scope: FRB-TRACE, FRB-FROB, FRB-CODE, FRB-TRANSFER, FRB-HIERARCHY,
FRB-NATURAL and FRB-EXAMPLE. This is the single capped hostile review.

The executed installed checker had SHA256
`85636a872152f896163c2cb42cf301400f591d21d97951ab8c391fc0c7971756`.
Its complete subprocess results are retained in this lane's
`checker-audit-results.json`; `reviewed_checker_85636a.py` preserves the exact
reviewed source and `run_checker_audit.py` reproduces the audit on that copy.
Root subsequently announced revision `f242fabfc7c124048f1f626d9f5131a44c105e6a39b7ee10d493fe9703d00777`,
adding category preparation/discard coverage. I do not attribute executed
evidence from the predecessor to that successor. The algebra targets stayed
frozen. The finite-result statements below bind to the reviewed predecessor.

## Findings

### 1. MINOR — A5's claimed direct conjugation comparison is an identity

**(a) Exact location.** `theory/checks/frobenius_hierarchy_check.py`, reviewed
revision, `a5`, lines 272 and 274–280, specifically the `A5-upper` assertion
whose diagnostic is `actual Pauli conjugation quotient`. The same source is
preserved at those lines in `reviewed_checker_85636a.py`.

**(b) Independent evidence.** Its assignment is
`values[i] = phase[states[i]]`. Therefore the two compared entries are
identically

```
phase[states[shift[i]]] - phase[states[i]]
values[shift[i]]       - values[i]
```

modulo p. This holds for every possible phase table and permutation, including
incorrect gate data. No data mutation can make that assertion false while
these definitions are respected. It is an indexing rewrite, not an independent
operator-conjugation computation.

This does **not** invalidate the substantive membership probe: exact Fourier
matrix blocks supply the phase data; the later difference-space filtration
can reject them; `hierarchy-extra-register-term` actually exits 1 at the
later `A5-upper` order-four-difference check with dimensions `[15,11,5,1]`.
The strictness and interference gates also have separate observed failures.
I therefore classify the redundant assertion as MINOR, not a failure of
FRB-HIERARCHY or of the decisive finite certificate.

**FIX DEMAND:** Remove this assertion and its independent-conjugation wording,
or replace it with separately constructed monomial-operator composition;
retain the Fourier extraction, filtration, and strictness gates.

**SURVIVING WEAKER STATEMENT:** The checker independently Fourier-diagonalizes
the multiplication permutation and certifies the resulting phase table by
translation filtration and strictness witnesses. This particular comparison
adds no evidence. The full mathematical theorem survives unchanged.

### 2. MINOR — The transfer row omits an explicit proof dependency

**(a) Exact location.** `CLAIMS-PROPOSED.md:13`, FRB-TRANSFER `depends on` cell;
`transfers-example.md:33`, section 1, `<1>2.<2>1`, explicitly invoking
`FRB-CODE <1>2.<2>3` for character cancellation. The shard header at line 5
correctly lists FRB-CODE, but the proposed DAG cell does not.

**(b) Independent evidence.** Fourier orthogonality uses the implication
`sum_y chi(y)=0` for nontrivial chi, obtained by translating the sum by an
element on which chi is not one. The cited derivation is present in
`foundation.md:197–202`, FRB-CODE `<1>2.<2>3`; it is not one of the named
FRB-TRACE steps. This is a missing bookkeeping edge, not an unproved lemma:
the cancellation argument itself is correct and can also be inserted locally.
Adding the edge introduces no cycle, since FRB-CODE depends only on the trace
foundation among the seven rows.

**FIX DEMAND:** Add FRB-CODE to FRB-TRANSFER's dependency cell, or include the
two-line character-sum derivation locally and remove that cross-reference.

**SURVIVING WEAKER STATEMENT:** FRB-TRANSFER is proved with the displayed
FRB-CODE character-sum dependency. Every asserted transfer identity survives
at its full stated scope.

## VERIFIED CORRECT — protected from repair churn

```text
The following statements were independently recomputed; neither finding
requires weakening or rewriting them.

1. All-characteristic trace foundation (FRB-TRACE).
   The relative trace polynomial has degree q^(d-1), leading coefficient 1,
   and fewer degrees than there are elements of E, hence is nonzero even
   when p divides d. Its q-power fixed values lie in the embedded K. A
   nonzero K-linear map to K is surjective. Fibre cardinality, double
   annihilator dimensions, and trace transitivity follow without dividing
   by d. For c != 0, multiplication by c is bijective; a trace-one u gives
   Tr(c(c^-1 u))=1. This proves nondegeneracy, and testing the two axes proves
   nondegeneracy of Omega. Alternation uses ab-ab=0 and includes p=2.

2. Exact Weyl/Frobenius phases and atomic factorization (FRB-FROB).
   On |x>, W(a,b) has phase -Tr(b(x+a)). Composing two such actions gives
   W(a,b)W(c,e)=psi(ae)W(a+c,b+e), with inverse psi(ab)W(-a,-b).
   Trace invariance under p-th power then gives exact simultaneous-label
   Frobenius covariance, with no residual scalar. Frobenius's order is r:
   t^(p^k)-t cannot vanish on p^r points for 0<k<r. Inverting the trace Gram
   matrix gives the unique momentum basis dual to the named position basis;
   Tr(b(x+a))=sum b_j(x_j+a_j) gives the asserted tensor factorization.

3. Code support and logical momentum (FRB-CODE).
   Ann(i(K))=ker T and Ann(ker T)=i(K). Character averaging therefore gives
   precisely the support-code projector and rank |K|. The phase-space
   orthogonal is i(K) direct-sum E. The map (i(a),b)->(a,T(b)) is onto,
   has kernel N, and preserves both alternating forms. Restricting the
   actual ordered Weyl action gives W_K(a,T(b)), including its phase at
   x+a. Translation preserves the code exactly when its label lies in i(K).
   Momentum inclusion instead gives d*b and collapses when p divides d.

4. Fourier signs and named towers (FRB-TRANSFER).
   The negative kernel gives F X(a)=Z(-a) F and F Z(b)=X(b) F. At x,a the
   coefficients of F_E J_i and V_i F_K have the same phase by trace duality
   and the same positive denominator because |E|=|K|*kappa_i. Each point of
   a composite trace fibre has exactly one intermediate trace label, so
   the two positive square-root factors multiply with no multiplicity or
   phase. Identity embeddings, arbitrary transported embeddings, adjoints,
   and Frobenius equivariance have the claimed types and formulas.

5. Exact hierarchy level for every p and unrestricted d (FRB-HIERARCHY).
   Full scalar phases make C_1 the Pauli group used in the proof. Clifford
   normalization is onto on the finite projective label set, establishing
   the needed inverse. Nesting, Clifford conjugation invariance, and left
   and right Pauli absorption follow by the displayed induction; they do
   not presume multiplication closure at a higher level.
   The actual target Fourier conjugate is the diagonal phase
   f=-Tr(y*x_1*...*x_d). Its coordinate expression has degree at most d+1.
   A difference lowers degree; affine phases are Paulis. This is a valid
   upper-bound induction in all characteristics. Conversely, repeated
   commutation with translations and Pauli absorption imply that a
   diagonal root-valued member of C_d has every d-fold difference constant.
   Translating each distinct control by 1 gives exactly -Tr(y), nonconstant
   by surjectivity. There is no factorial and no requirement d<p. This
   excludes C_d, hence every lower level by nesting, while Fourier
   conjugation transfers membership and exclusion to M.

6. Arithmetic naturality and the interference witness (FRB-NATURAL).
   Frobenius and embeddings preserve the exact accumulator z+product x_j.
   The same calculation with subtraction proves inverse intertwining.
   Compressing by the tensor support encoding yields M_K; the logical
   frame is the already verified trace quotient, so the logical exact
   level is d+1. Summing the target phase over y counts 2Q-1 zero-product
   control pairs. The amplitude is (2Q-1)/Q^2 and the probability its
   square. This computation supplies no endpoint specialization theorem.

7. Binary quartic example (FRB-EXAMPLE).
   An independent flat field F2[b]/(b^4+b+1), with a=b^2+b, reproduces the
   tower. Traces computed as traces of multiplication matrices agree with
   T(u,v)=v and Tr(u,v)=v+v^2. The induced squaring permutation in tower
   labels is [0,1,3,2,6,7,5,4,13,12,14,15,11,10,8,9]. Its square has four
   fixed labels and six two-cycles: invariant-vector dimension 10, support
   dimension 4. The fibre coefficients are 1/2 and 1/sqrt(8), as stated.
```

Independent executable evidence is in `independent_algebra_probe.py` and
`independent-algebra-results.json`. It imports no prover/checker helpers.
It uses flat prime-field polynomial arithmetic and multiplication-matrix
traces, including both embeddings of F4 into the flat F16 and the nonidentity
F4 automorphism. Thus the named-embedding checks are not restricted to the
constant coordinate inclusion. It checks transported trace composition,
code annihilators, all logical Weyl labels, and Fourier entry phases.

For hierarchy checks it extracts phase tables from actual Fourier-conjugated
target permutations, then independently inverts the tensor evaluation
Vandermonde matrices over F2/F3. The nonzero reduced monomials have degree
exactly d+1 and the actual d-control difference has all p distinct trace
values. Tested ranges: **F2, d=1–8; F3, d=1–6; F4, d=1–4**. These include
d greater than the characteristic. Degree data do not alone establish the
claim: the separate nonconstant-difference obstruction and the general
inductive proof above establish strictness. Independently recovered return
probabilities are 9/16, 25/81 and 49/256 at Q=2,3,4.

## Checker reachability and independent mutation audit

The reviewed installed checker passed **264135 exact assertions**, exit 0.
Every following named `--red-NAME` alias was run as an actual subprocess,
reported FAIL, and exited **1 at the listed mathematical gate**:

| mutation | observed first rejecting gate |
|---|---|
| frob-one-label | A1-symplectic |
| weyl-positive-sign | A1-Weyl |
| code-phase-subfield | A2-code |
| logical-momentum-inclusion | A2-logical |
| relative-trace-projection | A3-transfer |
| fourier-positive-kernel | A3-Fourier |
| trace-fibre-unnormalized | A3-normalization |
| multiplication-as-addition | A4-multiplication |
| embedding-coefficient-swap | A4-embedding |
| hierarchy-extra-register-term | A5-upper |
| hierarchy-delete-factor | A5-strict |
| interference-erase-phase | A5-interference |
| frobenius-no-shear | A6-tower |
| process-wrong-target | A7-types |
| instrument-double-success | A7-CP |
| sequential-reverse | A7-tower |
| parallel-collapse-outcomes | A7-parallel |
| reset-global-as-local | A7-boundary |
| fourier-failure-original-code | A7-Fourier |

Default `--red` also exited 1 at A1-symplectic. It is intentionally an alias
of the first mutation, not an additional distinct test. The red dispatcher
selects the relevant A-family; the distinct gate diagnostics above are
actual reached rejection paths, not incidental failure in an earlier family
or a command-line parser. All 19 advertised named gate IDs are reached.
Finding 1 identifies a vacuous *subcheck* under an otherwise reachable ID.

The meaningful comparisons have distinct data on their two sides: trace
annihilator enumeration versus trace kernels; physical versus logical Weyl
actions; fibre incidence matrices versus prescribed norms; finite Fourier
sums versus character identities; a concrete multiplication permutation
versus the embedding calculation; observed differences versus constant/zero
conditions; tower-coordinate formulas versus the field multiplication table.
In particular, the A5 filtration is not a polynomial fit and is not rendered
vacuous by the redundant comparison in finding 1.

Two independent mutations were made only on copies in this lane:

* Corrupting the independently supplied expected return amplitude from
  `(2Q-1)/Q^2` to `2Q/Q^2` left the observed Fourier phase table intact.
  The copy reported observed amplitude 3/4 versus expected 1, failed at
  **A5-interference**, and exited **1**. This mutates ground-truth data.
* Suppressing rejection only for A1-symplectic in another copy let the known
  `--red-frob-one-label` mutation survive. The copy reported **PASS and
  exited 0**. Thus this reviewed revision does not force failure merely
  because a red flag is present; gate survival is visible to callers.

The subprocess diagnostics, codes, and assertion counts are retained in
`checker-audit-results.json`. The copies remain scratch evidence in this
lane. No installed checker or target was edited by the critic.

## Quantifiers, canonicity, status, lockstep and reliance

All seven rows quantify over finite fields of every prime characteristic;
the proofs actually deliver that scope. For multiplication, distinct control
and target registers and the full-scalar prime-field Pauli frame are stated
in D1307–D1309, the claim row, formal proof, and labbook. None silently becomes
an odd-prime theorem or requires the extension degree to be invertible.

Named choices are consistent across the layers: p, primitive root, field
structure, computational field labels, ordered register factors, named
embedding, and positive real square roots. Atomic factorization additionally
names a position basis and uses its unique trace-dual momentum basis. The
trace-one element is existential in the strictness proof, not additional
construction data. No self-dual basis, hidden phase choice, unrestricted Weil
splitting, or all-embedding character restriction compatibility is assumed.

The seven proposed rows are all **SKETCH pending capped review/adjudication**.
Their proof headers and every associated theorem/proposition in the frozen
labbook use that same register. Every D1301–D1310 definition is restated in
the labbook. FRB-NATURAL's return witness is separately displayed but carries
the same row provenance and status. The labbook does not strengthen the
logical gate, tower, or endpoint claims. Apart from finding 2's missing DAG
edge, statement/proof/labbook strength agrees.

The nearest existing admitted claims WH-SYMM and WH-FUNCT-a/c are respected:
the prime-field frame does not recover field scalar structure, and trace
characters do not restrict compatibly along every embedding. This package
retains the scalar field data and uses the trace quotient/Fourier transfer.
It does not rely on REFUTED WH-FUNCT-b-SEC, the characteristic-two splitting
conjecture, or any v0.1 statement. D3 and D8 conventions match exactly.

I read the registered local CGK17, AND24 and ST-TRACE bodies at the cited
locators. CGK17 explicitly includes global phases in its first hierarchy
level; its multiqudit weight convention is compatible with the separate
register argument but is not needed as an imported classification theorem.
AND24's group-closure discussion is correctly restricted to contextual
motivation. ST-TRACE 0BIJ/0BIL corroborates transitivity and nondegeneracy;
the arithmetic foundation independently derives the finite-field statements.
No unregistered source supplies an essential proof step.

The finite checks support these statements without proving their universal
quantifiers; the structured arguments supply the universal proofs. No FATAL
or MAJOR mathematical objection remains on the seven proposed rows. Root
may resolve the two minor findings in the single repair wave and adjudicate
the statuses. This verdict itself does not change any status.

PASS
