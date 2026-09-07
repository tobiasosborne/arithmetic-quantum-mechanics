# Hostile verdict: F1 operational subsystem family

**Verdict date:** 2026-09-07
**Model:** `gpt-5.6-sol`, `xhigh`
**Review mode:** same-family prover/critic, blind lane; no prover `SUMMARY.md` or
`PATCH.md` was read.  One capped review only.

Targets reviewed: the Hecke definition/claim proposals and structured proof,
the CP operational proof, the `q=1` Kraus-context theorem, the partial-injection
endpoint functor, the exact checker, and the two lane source manifests with
their local primary bodies.  New theorem statuses remain candidate-only;
checker agreement is not treated as proof.

## Numbered objections

### O1 — MAJOR: D1121 admits the zero object, for which its normalized trace and state semantics are undefined

**Exact location.** `theory/lanes/f1-operational/cp/cp-operational.md`, D1121
lines 16--30, especially the definition `tau_X=Tr_X/d_X` at line 23;
CPOP-1 `<1>3.<2>3`; CPOP-2 `<1>2` and `<1>5`--`<1>7`.

**Independent counterexample.** Take the unitary fusion category of
finite-dimensional Hilbert spaces and the tensor-closed replete object family
containing both `1` and `0`.  This satisfies the stated D1121 hypotheses.  For
`X=0`, `A_X=End(0)` is the zero algebra, `1_X=0`, and
`d_X=Tr_X(1_X)=0`.  Thus `tau_X=Tr_X/d_X` is `0/0`; there is no normalized
state with value one on a unit; and the Hilbert-space inner product used in
CPOP-2 is unavailable.  The positivity sentence in CPOP-1 that every simple
weight is positive does not repair the empty multiplicity decomposition of
the zero object.

**FIX DEMAND.** Require every object of `S` to be nonzero (equivalently
`d_X>0`) and propagate that hypothesis through D1121--D1124 and CPOP-1--3.

**SURVIVING WEAKER STATEMENT.** CPOP-1--3 are valid for a tensor-closed
replete family of nonzero objects; positivity of categorical dimension also
shows tensor products remain nonzero.

### O2 — MAJOR: the exact checker violates the required mutation-reachability contract

**Exact location.** `theory/checks/f1_operational_check.py`, assertions at
lines 124--138 (H1--H2), 150--171 (H3), 188--218 (H4--H6/H10), 239--261
(H7--H8), 279--291 (H9), 300--331 (H11), 350--366 (H12), and 383--392
(H13); red-mode registration at lines 398--409.

**Independent computation.** Green exits zero.  Each shipped red mode exits
one at the following first reachable assertion:

| mode | first failing path |
|---|---|
| `--red-product` | H1 quadratic, line 124 |
| `--red-trace` | H2 Gram, line 133 |
| `--red-expectation` | H3 right bimodule, line 158 |
| `--red-overlap` | H4 overlap, line 198 |
| `--red-local-collapse` | H5 context probability, line 208 |
| `--red-unitary-braid` | H6 braid defect, line 212 |
| `--red-injection` | H7 injection image, line 239 |
| `--red-kraus` | H8 normalization, line 250 |
| `--red-flag` | H9 panel quadratic, line 279 |
| `--red-tl-trace` | H10 quotient identity, line 217 |
| `--red-context-size` | H11 distinct contextual images, line 314 |
| `--red-partial-zero` | H12 empty-map unitality, line 350 |
| `--red-corner-trace` | H13 normalized corner trace, line 385 |

Consequently no shipped mutation reaches, among others, H1 braid/far/star/
associativity; H2 strict positivity; H3 inclusion, commuting blocks,
trace/fixed-point, left bimodule, or amplified positivity; H4 central
projection/rank or marked trace; H5 unitary/local identity/normalization; H7
composition or subgroup expectation; H8 scalar-isometry, ambient trace, or
parallel normalization; H9 braid/Gram/flag count/partial-flag incidence; H10
positivity of the discarded ideal; H11 normalization, reduced-product, Born,
and lower-bound assertions; H12 dagger, composition, or lax naturality; or H13
projection, refinement, or tensor-concatenation assertions.  I also mutated
the flag incidence data on a temporary copy from orthogonality `x dot y=0` to
`x dot y=1`; H9 failed at the panel quadratic, so that particular data path is
live.  It does not cure the uncovered paths.

**FIX DEMAND.** Give every acceptance assertion a data mutation that reaches
that assertion (or consolidate assertions into genuinely single gates), and
record each mutation's first failing path.

**SURVIVING WEAKER STATEMENT.** The green run is exact sample evidence for
the displayed `q,n,Q` values, and all thirteen existing red modes do fail; the
checker is not yet an L1-compliant promotion gate for every advertised
subclaim.

### O3 — MINOR: the proposed low-level claim calls `P_2` a preparation without its coefficient-trace normalization

**Exact location.** `theory/lanes/f1-operational/hecke/CLAIMS-PROPOSED.md`,
`F1-HCK-LOW` row; compare `hecke-operational.md` `<1>18` and
`<1>20.<2>4`--`<2>6`, and the normalized density used by checker H5 at lines
200--208.

**Independent computation.** In the block decomposition from `<1>18`,
`tau_3=alpha chi_+ + beta chi_- + gamma Tr_2` with
`gamma=q/(1+q+q^2)`.  Since `P_2` is rank one in the standard block,
`tau_3(P_2)=gamma`, not one.  The full coefficient-trace density of the state
`phi_2(x)=Tr_2(P_2x_std)` is
`h=P_2/gamma=((1+q+q^2)/q)P_2`.  At `q=1` this is `3P_2`, agreeing with the
group-algebra normalization in CPOP-5.  The proof uses the correctly normalized
functional; only the proposed row conflates the effect, block density, and
full-algebra density.

**FIX DEMAND.** State that `P_2` is the effect and the ordinary `M_2`-block
density, while `P_2/gamma` is its density relative to `tau_3`.

**SURVIVING WEAKER STATEMENT.** The Born values `1` and
`(1-2q/(q+1)^2)^2` are exactly correct for the state `phi_2` and effect `P_2`.

### O4 — MINOR: proposed claim rows do not point to the checker that now exists and overdescribe one check scope

**Exact location.** `theory/lanes/f1-operational/hecke/CLAIMS-PROPOSED.md`,
the `tested in` cells of `F1-HCK-POS` through `F1-HCK-Q`, especially
`F1-HCK-TOWER`; compare `theory/checks/f1_operational_check.py` H1--H9 and
H11.

**Independent computation.** The rows still say `proposed ... checker` rather
than name `theory/checks/f1_operational_check.py`.  The tower row promises a
parabolic checker through total level five, while `block_tests` uses only
`H_2(q) tensor H_2(q) -> H_4(q)`.  H11 does use `H_5` for selected context
calculations at `n=3`, but it does not check all parabolic tower assertions
through level five.

**FIX DEMAND.** Replace the placeholders with the real checker path and exact
gate/sampling scope; do not describe H11's selected level-five context probe as
a general parabolic-level-five check.

**SURVIVING WEAKER STATEMENT.** All proposed rows remain honestly `SKETCH`,
and the existing checker supplies the narrower exact evidence stated in its
own output.

## Independently verified correct — do not churn in repair

<!-- BEGIN VERIFIED-CORRECT: repair should not rewrite these arguments -->

1. **Hecke positivity for every real `q>0`.**  The weighted regular basis has
   Gram diagonal `q^ell(w)`, and the two-string calculation makes every
   self-adjoint generator symmetric.  Therefore
   `tau(x^*x)=sum_w |c_w|^2 q^ell(w)` is faithful.  This proves the finite
   C*-algebra result beyond the prime-power flag realizations; no sampled
   checker value is used for the quantifier.

2. **Exact flag commutant and trace convention.**  `GL(L)`-orbits on pairs of
   complete flags are indexed by `S_n`; their adjacency kernels form the full
   commutant, transpose sends `A_w` to `A_(w^-1)`, and only `A_e` has diagonal
   entries.  Thus normalized operator trace equals the coefficient trace.
   Iwahori's Proposition 1.4/Corollary 1.5 and Lemma 3.1/Theorems 3.2, 4.1 at
   the manifest locators support the commutant and presentation claims.  The
   independent `F_2^3` and `F_3^3` constructions give 21 and 52 flags and the
   exact Hecke Gram respectively.

3. **Ordered tower and UCP expectations.**  Contiguous block permutations
   give injective trace-preserving star-homomorphisms.  Coefficient deletion is
   the trace-orthogonal projection.  Umegaki's trace-pairing characterization
   identifies it with the faithful conditional expectation; matrix
   amplification of the same projection proves complete positivity.  Both
   three-block inclusion routes send a basis tensor to `T_(u x v x w)`, and
   both expectation routes retain exactly `S_l x S_m x S_n`.  This is genuine
   ordered coherence.  It does not provide a block swap, as the artifact
   correctly says.

4. **Low-dimensional arithmetic memory.**  The displayed two-dimensional
   representation gives `H_3(q)=C direct-sum C direct-sum M_2(C)` for every
   `q>0`.  In the matrix block,
   `P_1=diag(1,0)` and
   `P_2=[[a,c],[c,1-a]]`, with
   `a=q/(q+1)^2` and `c^2=a(1-a)`.  The four unlabelled overlaps are
   `a,a,1-a,1-a`; since `a<=1/4`, their minimum is `a`, which recovers exactly
   `{q,q^-1}` and recovers `q` after the mark `q>=1`.  Conjugation by
   `2P_1-1` changes the return probability from one to `(1-2a)^2`.

5. **Marked trace, reciprocal symmetry, and the `q=1` fibre.**  The calculation
   `tau_2((T_1+1)/(q+1))=1/(q+1)` is exact.  The map
   `T_i -> -q S_i` is a trace-preserving star-isomorphism from `H_n(q)` to
   `H_n(q^-1)`, and `H_n(1)=C[S_n]`.  The finite-set assignment
   `S -> C[Sym(S)]` is functorial for injections; coefficient projections obey
   subgroup-tower composition.  Disjoint assembly is coherent: on group
   elements both sides of
   `i_(f disjoint g) mu_(S,T)=mu_(S',T')(i_f tensor i_g)` are the same
   permutation extended by identity, and the empty set supplies the unit.

6. **Kraus morphism quotient and exact context bound.**  In KCF-1 the map
   `(h,k)->h^-1 g k` is injective because the constructed involution has
   `H intersect gHg^-1={1}`.  Hence one `2n-1`-point observable recovers every
   Kraus Gram coefficient.  Equality of finite Gram families is exactly stable
   scalar-unitary mixing after zero padding, and this equivalence is a
   composition/tensor congruence.  For every smaller possible ambient set,
   the trivial/sign cross terms vanish by the nontrivial support intersection.
   Independent group-algebra enumeration gives 4 distinct words and Born gap
   `1/2` for `n=2`, and 36 distinct words and gap `1/18` for `n=3`.  The state
   `rho=1+Delta` is positive because `Delta` is the difference of two effects,
   and its probability gap is the strictly positive `tau(Delta^2)`.  KCF-1's
   `q=1` statement has no mathematical objection in this round and is suitable
   for a claim row/promotion after ordinary adjudication.  Its final `q>0`
   Hecke extension remains correctly labelled `SKETCH`.

7. **Normalization across the two constructions.**  The generic categorical
   lane consistently uses unnormalized `Tr_X` and `Tr_X(rho)=1`; the Hecke and
   group-algebra lanes consistently use normalized coefficient trace `tau` and
   `tau(h)=1`.  They describe the same positive functional after the rescaling
   `h=d_X rho`.  CPOP-4 uses `(0,P/phi)` for categorical trace, while CPOP-5
   uses `3q_23` for the normalized coefficient trace.  O3 is only the proposed
   row's wording.

8. **Sourced supporting comparisons.**  The local source hashes match both
   manifests.  Stinespring supports the CP/dilation interpretation, and the
   Jones--Penneys citations are explicitly used only as an internal-algebra
   analogue.  The Fibonacci source displays the stated `phi`, `F`, and braid
   phases; the two exact probabilities recompute to `(5-sqrt(5))/8` and
   `(3-sqrt(5))/2`.  These generic-fusion/Fibonacci claims may remain
   supporting `SKETCH`; they are not needed to promote the Hecke or KCF
   headlines.

9. **Partial-injection F1 endpoint.**  PMAP-1 is correct.  On a group-basis
   permutation `sigma`, `R(f)` retains it exactly when
   `supp(sigma) subset dom(f)` and then relabels it by the partial bijection.
   For composable partial injections the survival condition becomes
   `supp(sigma) subset dom(f) intersect f^-1(dom(g))`, exactly the domain of
   `gf`; hence `R(g)R(f)=R(gf)`.  Coefficient inclusion and expectation are
   adjoint for the normalized trace, so partial inverse is sent to trace
   adjoint.  The same support test proves laxator naturality, while the empty
   partial map sends `a` to `tau_S(a)1_T`, which is UCP and composes as the
   categorical zero morphism requires.  Thus PMAP-1 supplies an actual dagger
   lax symmetric monoidal functor on `FinPInj`; it has no mathematical
   objection in this round and may be promoted after ordinary adjudication.

<!-- END VERIFIED-CORRECT -->

## Quantifier, canonicity, reliance, and status-register check

- The Hecke proof really covers all real `q>0`; the flag interpretation is
  correctly restricted to prime-power `Q`.  The exact tests include `q=1/2`
  and the flag tests include characteristic two.  KCF-1 has the correct split
  between `n>=1` for recovery and `n>=2` for sharpness.
- PMAP-1 includes empty source/target sets and all partial injections.  Its
  empty-domain map is correctly the trace-and-prepare channel, not the zero
  linear map; ordinary functoriality does not require preserving an enriched
  additive zero.
- The complete-flag context algebra depends on the named field and named
  Lagrangian `L`.  No independence of `L`, equivalence with the full
  Weyl--Heisenberg theory, symmetric Hecke assembly for `q!=1`, or universal
  geometric `F_1` specialization is claimed.  The boundary is honest.
- The ordered Hecke assembly is strictly coherent.  The finite-injection
  `q=1` assembly also satisfies functoriality, unit, associativity, symmetry,
  and naturality on basis permutations.  Retained Kraus data makes sequential
  and disjoint-support parallel composition well defined; isolated CP-shadow
  equality does not, as both the Hecke and symmetric-group witnesses show.
- No reviewed step depends on a `REFUTED` row or on `v0.1`.  The primary-source
  bodies and hashes match the manifests.
- Root `claims/CLAIMS.md` contains no new operational claims.  The Hecke
  proposal keeps every row at `SKETCH`, and the CP/KCF/PMAP files explicitly
  call their theorems candidates.  This is honest relative to the nearest
  `PROVED` register.  O1 blocks CPOP-1--3 as presently quantified; O2 blocks
  treating the checker as a fully compliant promotion gate.  KCF-1 and PMAP-1
  themselves survive this mathematical review, but checker agreement alone is
  not their proof.

FAIL(O1,O2)
