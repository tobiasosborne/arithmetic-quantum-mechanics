# Typed arithmetic process category — one capped hostile review

Date: 2026-09-08. Same-family prover/critic, blind lane. Native inherited
Codex agent through collaboration tools, no model override, no nested agent
or CLI model invocation. Exact runtime model metadata is unavailable. I read
the frozen artifacts and shared definitions/claims, not prover reasoning.

Scope: category D1321--D1327, FRP-CAT/CP/DESCENT, both structured proof
shards, the labbook draft and ENDPOINT-NEXT. Shared algebra claims remain
explicit dependencies and receive their separate review; this verdict does
not adjudicate the all-d hierarchy proof. No trunk or target file was edited.

Result: no FATAL or MAJOR on the category, realization or descent statements.
Two MINOR precision repairs are listed below. The claims remain proposals
until root adjudication and the separate algebra dependency audit.

## Numbered objections

### CAT-1 — MINOR: fix the universe of retained tag names for literal smallness

**(a) Location.** `category/DEFINITIONS-PROPOSED.md`, D1325, lines 106--109;
`category/process-category.md`, `<1>4.<2>4`, lines 83--84; the corresponding
process-object definition at `category/labbook-draft.tex`, lines 190--193.

**(b) Independent calculation.** The amplitude syntax is a set, but this
does not itself make all finite families with arbitrary retained tag sets a
set. If arbitrary set-valued names are allowed, for each ordinal alpha take
the process object with tag set `{alpha}` and the empty quantum word at its
only tag. These are pairwise different objects, since external tags are
retained. They form a proper class. The term "named" plausibly intends finite
syntactic names, but that restriction is not stated. Likewise hidden index
sets should be represented by their finite multisets of amplitude classes
when invoking a set quotient. This is a size convention, not a defect in
the composition or certificate argument.

**(c) FIX DEMAND.** Fix a set of permitted tag names closed under the finite
tuple operations used here (for example finite syntactic names and tagged
tuples), take finite tag subsets from it, and use finite multiset
representatives for hidden-index classes; carry this convention into the
labbook's process-object definition.

**(d) SURVIVING WEAKER STATEMENT.** With unrestricted finite label sets, the
same formulas give an essentially small category with the stated operations
and realization; the literal small category follows after the indicated
size convention. No external-tag equality quotient is needed.

### CAT-2 — MINOR: the endpoint's trace-one implication needs a normalized trace

**(a) Location.** `category/labbook-draft.tex`, endpoint paragraph, lines
388--392; `category/ENDPOINT-NEXT.md`, "Reference trace and the Frobenius
boundary", lines 93--96. This is a scope statement outside the structured
FRP proofs, so there is no Lamport step address.

**(b) Independent counterexample.** In `M_3(C)` use the faithful positive
ordinary trace and the unitary `U=diag(1,1,-1)`. Then `Tr(U)=1`, but `U!=1`
and `Tr((U-1)^*(U-1))=4`. The displayed expansion has general first term
`2 tau(1)`, not `2`. The intended phase trace is normalized earlier in the
endpoint proposal, but the labbook sentence says only "a faithful positive
tracial algebra" and its immediately preceding process convention uses
ordinary trace. Exact values are recorded in `trace-counterexample.json`.

**(c) FIX DEMAND.** State `tau(1)=1` in the endpoint implication and say
"faithful normalized positive trace" in the labbook sentence, or formulate
the general implication as `tau(U)=tau(1)`.

**(d) SURVIVING WEAKER STATEMENT.** For a faithful positive normalized trace,
unitarity and `tau(U)=1` imply `U=1`. More generally, `tau(U)=tau(1)` suffices
without normalization. The proposed fixed-N trace `N^(1-r)` and its stated
comparison boundary survive; no new specialization theorem follows.

## VERIFIED CORRECT — preserve these parts during repair

```text
1. Independent source and coefficient scope.
   D1322 fixes a typed, linear dagger symmetric monoidal congruence before
   H or R is defined. No relation tests CP equality. Raw terms are finite
   syntax over a set and the amplitude quotient exists. R_p contains every
   matrix entry of the listed generators: Fourier denominators are powers
   of sqrt(p), as are transfer denominators. At p=2 the realized coefficients
   are real, and full Clifford scope requiring i is explicitly excluded.

2. Arithmetic interpretation and retained code types.
   Direct basis action gives the Weyl product cocycle +Tr(ab'), exactly
   matching W=Z(-b)X(a). The mixed code relation uses T_i(b), not included
   momentum. From c_i t_i=j_i and t_i unitary one obtains c_i=j_i t_i^dagger,
   c_i^dagger c_i=1, and c_i c_i^dagger=j_i j_i^dagger at source. These
   calculations respect the distinct C_i, Q_K and Q_E types.

3. Source normalization certificates, including arbitrary branch codomains.
   Independently expanding a composite gives
     1-sum_j k_j^dagger T_(b(j)) k_j
       =(1-S)+sum_j k_j^dagger(1-T_(b(j)))k_j.
   Substitute certificates h_l^dagger h_l and g_v^dagger g_v: the composite
   certificate arrows are h_l and g_v k_j, all starting at the same input.
   For tensor, 1-S tensor T=(1-S) tensor 1+S tensor (1-T), with certificate
   arrows h_l tensor id and k_j tensor g_v. No positivity reflection or
   matrix-equality decision enters this argument. Zero deficits prove the
   normalized subcategory claims.

4. Equality, identities, associativity and interchange.
   A triple composite has intermediate labels (b,c) and one hidden index
   from each of k,l,m. Its two parenthesizations are bijective by retaining
   this full path and both have amplitude mlk. Identity composition removes
   only its singleton index. For two independent paths the tensor/composite
   bijection changes ((j,t),(j',t')) into ((j,j'),(t,t')); the amplitudes
   agree by source interchange. External tags are carried by structural
   routing arrows, not silently quotiented. No assumption that equal CP
   maps have equal Kraus lists is used.

5. CP realization and nonfaithfulness.
   Every matrix amplification is a sum of positive quadratic forms.
   Cyclic rectangular trace converts the interpreted source certificate
   into the exact sum of trace losses. Tensor equality holds on elementary
   matrix units, which span also the entangled inputs. The normalized
   singleton source processes {1} and {-1} differ: H on the empty word
   separates their amplitudes. Both realize the identity scalar CP map.

6. Preparation and quantum discard.
   b_(E,a)^dagger b_(E,a)=1 and sum_a b_(E,a)b_(E,a)^dagger=1 are explicit
   source relations. Code discard is disc_K t_i^dagger with amplitudes
   b_(K,a)^dagger t_i^dagger; its effect sum is t_i t_i^dagger=1_Ci.
   Tensoring and summing tagged inputs gives ordinary trace on every word
   and family. No all-complex-state or all-CP completeness is claimed.

7. Decoders, towers, and independent parallel output types.
   For s^dagger s=1, q=1-ss^dagger is a projection; effects of s^dagger,q
   sum to 1. The success deficit is q^dagger q and its Born probability is
   Tr(ss^dagger rho). In a tower the three effects are q_t, t q_s t^dagger,
   t p_s t^dagger, with output types Z,Y,X. They sum to 1 and the success
   amplitude is (ts)^dagger. Tensor outcomes have distinct targets XX',
   XY',YX',YY', and their effects sum to (p_s+q_s) tensor (p_t+q_t)=1.
   There is no false equality between two-outcome composite decoding and
   a retained three-history or four-outcome instrument.

8. Full Fourier and encoded-gate squares.
   From f_E j=v f_K, unitarity gives v^dagger f_E=f_K j^dagger and
   (1-vv^dagger)f_E=f_E(1-jj^dagger). These are equal amplitudes in each
   external branch, with success type Q_K and failure type Q_E. The code
   Frobenius and multiplication squares reduce to the imposed j-intertwining
   equations through t_i, without changing the logical momentum quotient.

9. Named coordinate factorization.
   Expanding a_B^dagger a_B and a_B a_B^dagger leaves basis resolutions of
   identity. For positions a=sum a_l beta_l and momenta
   b=sum b_l beta_l^dual, Tr(b(x+a))=sum_l b_l(x_l+a_l). This yields precisely
   the stated interpreted Weyl factorization. No basis independence or
   extra source Weyl equation is asserted.

10. Endpoint honesty.
    The document explicitly fixes the arithmetic field diagram and N=p,
    separates extension-field incidence q from restricted-scalar incidence p,
    and leaves its section algebra, positive trace and comparison functor to
    future construction. Its generic-q and type-C tensor cautions are sound.
    The F4 witness is real: X(1)Z(alpha)=-Z(alpha)X(1), and Frobenius moves
    |alpha> to |alpha+1>, changing the alpha-projector probability 1 to 0.
```

## Independent computations and falsifier reachability

`independent.py` is a fresh standard-library calculation, importing no
supplied finite-field or matrix helper. It uses pairs for
`F4=F2[u]/(u^2+u+1)` and `F9=F3[u]/(u^2+1)`, with exact rational arithmetic
in the cyclotomic basis `1,w`, `w^2+w+1=0`. Binary values are rational.
It verifies 256 and 6561 Weyl products respectively, every mixed inclusion
Weyl relation, Fourier unitarity, both decoder Fourier branches, projection
completeness, all basis discards on matrix units, and every coordinate Weyl
factorization. It independently finds trace-dual bases `(1+u,1)` at p=2
and `(2,u)` at p=3 for position basis `(1,u)`. In both fields the named
entangled inclusion-decoder example gives probabilities `(1/2,0,0,1/2)`.
Results are in `independent.json` and process exit records in
`independent-status.json`. Its data mutation replacing the dual basis by
the position basis exits 1 at COORDINATE-DUAL, already for p=2, a=0,b=u;
the final unmutated run exits 0.

The checker revision executed by this review has SHA256
`f242fabfc7c124048f1f626d9f5131a44c105e6a39b7ee10d493fe9703d00777`.
It includes the final preparation/discard addition. I ran all twenty reds
in actual separate subprocesses, then green: every red exits 1 at its
advertised gate, green exits 0 with 264613 assertions. `checker-runs.json`
records the complete diagnostics and counts; `run_checker.py` reproduces
the execution workflow against the installed revision. The claimed
mathematical gates and their reaching reds:

| Gate | Mutation reaching it (all exit 1) |
|---|---|
| A1-symplectic | frob-one-label |
| A1-Weyl | weyl-positive-sign |
| A2-code | code-phase-subfield |
| A2-logical | logical-momentum-inclusion |
| A3-transfer | relative-trace-projection |
| A3-Fourier | fourier-positive-kernel |
| A3-normalization | trace-fibre-unnormalized |
| A4-multiplication | multiplication-as-addition |
| A4-embedding | embedding-coefficient-swap |
| A5-upper | hierarchy-extra-register-term |
| A5-strict | hierarchy-delete-factor |
| A5-interference | interference-erase-phase |
| A6-tower | frobenius-no-shear |
| A7-types | process-wrong-target |
| A7-CP | instrument-double-success |
| A7-tower | sequential-reverse |
| A7-parallel | parallel-collapse-outcomes |
| A7-boundary | reset-global-as-local |
| A7-Fourier | fourier-failure-original-code |
| A7-PREP | discard-omit-bra |

The red dispatcher selects the relevant A-family, so the A7 reds reach A7
rather than dying in A1. Within A7 the failures are respectively rectangular
type mismatch, completeness, reversed typed composition, missing retained
tag, wrong reset output, wrong failure projector, and missing discard effect.
All A7 gates have distinct reaching mutations. The final A7 green counts are
6 type, 20 CP, 1028 tower, 2078 parallel, 2 Fourier, 1 boundary and 478 prep.

After these executions, root installed the algebra-review repair with hash
`946ca4584424329e85b92107664d24c89942f194de42dd0737ddc372d77d8c12`.
I independently compared the full delta: it only removes an A5 redundant
indexing/quotient comparison loop and adjusts its associated wording. All
A7 code is unchanged. The execution counts in this verdict belong to the
reviewed `f242fabf...` revision; validation of the subsequent A5 repair is
root's adjudication work, not an additional hostile round here.

I additionally mutated **copies**, including an independent corruption of
ground-truth data. `independent-mutations.json` records their hashes/results:

* Replacing the expected mixed-state Born weight by 3/4 reaches the later
  A7-CP probability sentinel and exits 1; the computation still produces 1/2.
* Replacing exact System equality by dimension equality reaches A7-types and
  exits 1 because an unrelated four-dimensional named source is accepted.
* Reversing the tensor Kraus factor order reaches A7-parallel and exits 1 on
  the success/failure branch's effect, after its earlier tests have passed.
* Disabling only the A7-PREP rejection in a separate copy lets
  `--red discard-omit-bra` report PASS and exit 0. Thus the installed exit
  rule does expose surviving mutants; it does not force red exit merely
  because a mutation option is present. No disabled gate was installed.

Symbolic gate audit: the success Born identity alone is rectangular trace
cyclicity, so it is not independent evidence for the named numerical weight;
the separately fixed probabilities supply that sentinel, reached above.
The Choi check constructs the CP action on matrix units separately from its
explicit vector Gram, rather than fitting an unknown positive matrix.
The direct tower amplitude in A7 is defined from the composed transfer
matrix, so that subcheck tests dagger/composition consistency; independent
direct trace transitivity resides in A3. These are correctly limited finite
checks. Neither their green outputs nor raw matrix equality establish the
abstract source category; that conclusion rests on the audited source proof.

## Status, lockstep, characteristic and reliance register

All three category claim rows are SKETCH pending this capped review and root
adjudication. Their proof headers and labbook theorem markers agree. The
definitions are marked proposals, and ENDPOINT-NEXT is explicitly a proposal
with no admitted q-to-one functor. The labbook's endpoint trace sentence
needs CAT-2; the other statement/proof/register/labbook scopes agree.

FRP-CAT/CP/DESCENT do not rely on the REFUTED `WH-FUNCT-b-SEC` row or on a
globally restriction-compatible trace character. They use the transported
relative trace, which remains nonzero and surjective when the degree is
divisible by p. I checked the D3/D8 sign and phase conventions and the
ordinary-trace distinction from D1205. The background papers registered at
2105.06244, 2304.10584 and 0705.4556 are not invoked to import completeness
or an odd-characteristic theorem into p=2. No v0.1 result supplies evidence.

The finite named field diagram, primitive root, positive square roots,
ordered words, actual embeddings, code identifications and coordinate basis
are all retained choices. No unproved independence from those choices is
claimed. A fixed higher Clifford level is only a generator label, and no
composition closure of that level is asserted. The algebra review must
still adjudicate the shared all-field identities and hierarchy claims.

Frozen category SHA256s, in target order:

```text
DEFINITIONS-PROPOSED.md 78e2808c929ff520307bad47a15cf12e777d83c545d9800d93db229a55f330b8
NOTATION-PROPOSED.md   c362ee54042399319ce41f9f862f6140e50e033d0fc03f5416485334174d0247
CLAIMS-PROPOSED.md     83d6f5cbc790e24af8d92ee8867925fa4fb08f715839d85263a3c93bba95da30
amplitude-category.md  6d23d1991dae53b0ecd109db6de2f706d1281417d0a3466bdcfdb866b78864d2
process-category.md    7bbe56694c942ee2e082f6848419d968d796c0a566d2f9c4affe677700ae483d
labbook-draft.tex      316ab280345ceb08d22f99fac03244dfba1e4bd68f4dac617d2329b8cd64ac6b
ENDPOINT-NEXT.md       66101540afe6eafe50c68e40917b1859db776d6bdc91b8e0ff3f0c0f4facfb61
```

PASS
