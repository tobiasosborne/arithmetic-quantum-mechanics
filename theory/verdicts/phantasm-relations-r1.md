# Blind hostile verdict — SP-LREL and SP-COMPACT

Date: 2026-09-10. Critic model: `gpt-5.6-sol`, reasoning `xhigh`.
Same-family prover/critic; blind lane. The critic did not read the prover's
`PROPOSAL.md`, `PATCH.md`, `SUMMARY.md`, or reasoning context and did not
contact the prover.

Targets reviewed in full:

- `theory/lanes/phantasm-relations/prover/lrel-reduction.md`
- `theory/lanes/phantasm-relations/prover/lrel-laws.md`
- `theory/lanes/phantasm-relations/prover/compact.md`
- `theory/lanes/phantasm-relations/prover/LABBOOK-FRAGMENTS.tex`
- frozen checker and pre-registration at hash
  `330145e0c093b63d2dce6be150f981d56d8f906a0c36a4363c63fe8d42c547eb`

## Objections

### OBJ-1 — MAJOR — the source monoidal category of the graph functor is not defined

**(a) Exact location.** Canonical D1701, `definitions.md`, paragraph defining
`S_k^aff` (the text ending with the affine composition formula); canonical
`SP-LREL` statement, final sentence; `lrel-laws.md` §5 `<1>6`--`<1>8`.

**(b) Independent computation.** A symmetric monoidal functor requires a
monoidal source. D1701 defines `V+W`, affine arrows, composition and identities,
but never defines tensor on affine arrows or the source associator, unitors and
symmetry. The proof first uses an undefined `f+f'` at §5 `<1>6`. The intended
formula is unambiguous but is additional structure:

    (t,g) + (t',g') = ((t,t'), g+g')

with zero unit and the tuple coherence maps. Substitution gives
`Gamma_(f+f')=Gamma_f+Gamma_(f')`, but that calculation cannot type a
*symmetric monoidal* functor until these source operations are owned. This is a
canonicity/type gap, not a counterexample to the intended result.

**FIX DEMAND.** Add the affine-arrow direct sum, unit and coherence maps to
D1701 (and its exact labbook restatement), or weaken/reformulate the graph
clause until that source structure is explicitly defined; then cite the new
clauses in `lrel-laws.md` §5.

**SURVIVING WEAKER STATEMENT.** Graphs already define a faithful ordinary
functor `S_k^aff -> L_k^aff`, and they preserve the displayed standard direct
sum conditional on equipping the source with the formula above.

### OBJ-2 — MAJOR — the labbook definition drops D1714's object quantifiers

**(a) Exact location.** `LABBOOK-FRAGMENTS.tex` definition beginning at
`\begin{definition}[Compact data for affine Lagrangian relations]`, first two
sentences and the displayed `a_{U,V,W}`; compare D1714's opening sentence.

**(b) Independent computation.** D1714 fixes a finite field and
finite-dimensional symplectic spaces `U,V,W`. The proposed labbook fragment
fixes only `k` and immediately uses free variables `V`, then `U,V,W` in
`a_{U,V,W}`. Consequently the purported exact restatement is not a closed
definition: the domains of the coherence maps and the quantifier governing
the compact data are absent. The proof's formulas become well typed as soon as
the canonical quantifier is restored; no mathematical calculation needs to
change.

**FIX DEMAND.** Replace the opening by D1714's exact quantification of the
finite-dimensional symplectic spaces `U,V,W` and keep that quantifier in the
labbook definition landed with the claim.

**SURVIVING WEAKER STATEMENT.** The labbook's cup, cap, name, unname and scalar
formulas agree with D1714 after the missing object quantifiers are supplied.

### OBJ-3 — MAJOR — the runner counts a CLI usage error as an advertised red

**(a) Exact location.** Frozen `phantasm_relations_check.py` `parse_args`, the
line adding `--red` with a required `NAME`, and the repository red-discovery
contract that treats every `--help` token matching `--red[A-Za-z0-9_-]*` as a
standalone mutation.

**(b) Independent computation.** The actual `--help` stream exposes thirteen
matching tokens: the twelve named modes plus bare `--red`. Running the bare
token produces argparse usage text and exit `2` because its `NAME` is missing;
it reaches no mathematical gate and prints no intended gate. The session
runner tests only nonzero, so it would report this parse failure as a killed
mutation. The twelve real modes do each exit `1` at their registered G1--G7
targets; the defect is the thirteenth advertised path.

**FIX DEMAND.** Remove the generic `--red NAME` option from advertised help
(retain the twelve named flags), or make bare `--red` a real no-argument
mutation with a named intended gate and exit `1` through that gate.

**SURVIVING WEAKER STATEMENT.** All twelve named mutations satisfy their
registered exit and gate contracts.

### OBJ-4 — MAJOR — no advertised mutation reaches the compact dagger or snake acceptance checks

**(a) Exact location.** `phantasm_relations_check.py` G6: initial cup equality,
dagger comparison, and snake comparison; the `MUTATIONS` entries
`compact-dual` and `cup-order`; `EXPECTATIONS.md` mutation map; canonical
SP-COMPACT required mutation “drop the swap in dagger compatibility.”

**(b) Independent computation.** Both advertised G6 mutations have the same
observed path: they pass silently over `F2` where `V=bar(V)`, then fail on the
first `F3` rank-one cup equality with exactly
`cup has wrong dual/factor order`. Neither reaches cup/cap Lagrangian typing,
the dagger equality, either snake, or cardinality. The canonical required
drop-swap mutation is absent. On independent `/tmp` copies:

- replacing only the first snake's cap by the same-typed empty cap passed
  G1--G5 and the earlier G6 checks, then failed at
  `G6: one of the two compact snake equations failed`;
- removing only `sigma_(bar(V),V)` from the dagger comparison passed G1--G5,
  cup equality and Lagrangian typing, then failed at
  `G6: cup/cap dagger factor order failed`.

Thus the acceptance checks can discriminate, but their red reachability was
not registered and the two registered G6 modes are bit-identical at the gate
path that matters.

**FIX DEMAND.** Add separate advertised mutations that leave cup typing intact
and fail first at (i) compact dagger compatibility by dropping the swap and
(ii) a snake by changing one same-typed wire/cap; record and observe both
before the repaired green run.

**SURVIVING WEAKER STATEMENT.** Green G6 correctly evaluates the canonical
cup/cap, dagger and snake formulas over the zero and rank-one `F2/F3` objects;
the unregistered independent mutations show those later assertions are live.

### OBJ-5 — MINOR — one advertised G4 comparison is textually duplicated

**(a) Exact location.** `phantasm_relations_check.py` functions `tensor` and
`tensor_expected`, and G4's `actual == expected` comparison.

**(b) Independent computation.** In the nonempty green branch both functions
form the identical set

    {x[:a]+y[:c]+x[a:]+y[c:] for x in left for y in right}.

Therefore `actual == expected` simplifies definitionally to `X==X`; it is not
an independent coordinate oracle. The neighboring checks remain substantive:
`is_affine_lagrangian(actual)`, dagger compatibility, swap naturality,
associativity and interchange. The `tensor-order` mutation is caught by the
special probe before entering the large comparison loop.

**FIX DEMAND.** Replace `tensor_expected` with an independently specified
Cartesian-pair regrouping/permutation oracle, and let `tensor-order` reach that
comparison without a duplicate implementation.

**SURVIVING WEAKER STATEMENT.** G4 still supplies exact finite evidence for
Lagrangian typing and the listed tensor/dagger/naturality/coherence equations;
only the claimed independent actual/expected comparison is unsupported.

### OBJ-6 — MINOR — proof provenance contains nonexistent or noncanonical targets

**(a) Exact location.** `compact.md` §1 `<1>2` and §1 `<1>3.<2>4`, which cite
`lrel.md`; `compact.md` §7 `<1>7`, which cites `PROPOSAL.md`.

**(b) Independent computation.** The target proof is split into
`lrel-reduction.md` and `lrel-laws.md`; no reviewed `lrel.md` target exists in
this lane. The final mathematical statement is canonically owned by
`claims/CLAIMS.md`, while the lane proposal is neither a single source nor an
allowed target in this blind pass. The intended replacements are exact:
graph/coherence is `lrel-laws.md` §§4--5, the half-dimension lemma is
`lrel-reduction.md` §1 `<1>6`, and the conclusion is the canonical
`SP-COMPACT` row.

**FIX DEMAND.** Replace the two `lrel.md` citations with their actual shard
paths/step addresses and replace `PROPOSAL.md` with the canonical SP-COMPACT
claim/DAG record.

**SURVIVING WEAKER STATEMENT.** Each cited mathematical fact is present in the
reviewed shards or canonical register; this is a locator defect only.

## Independently verified correct — do not churn in repair

<!-- VERIFIED-CORRECT-BEGIN -->

1. The finite-linear reduction is correct over every field. With
   `K=C^perp`,
   `(L+K)^perp=L cap C` and
   `dim(L cap C)=N-r+dim(L cap K)`. Quotienting subtracts
   `dim(L cap K)`, leaving `N-r`, half of `dim(C/K)=2(N-r)`.
2. For composition,
   `C=bar(V)+Delta_W+Z` has
   `C^perp={(0,w,w,0)}`. The two middle terms cancel in every
   characteristic, including characteristic two, and reduction gives exactly
   the existential composite.
3. If the affine constrained intersection is nonempty, translating by one
   chosen point gives direction `L_0 cap C`; outer projection gives the
   translate of the linear composite. If it is empty, the composite is the
   retained empty arrow. No transversality is needed.
4. Associativity, identities, converse closure/involution, tensor closure,
   interchange and the target coherence diagrams reduce to the stated
   existential or tuple calculations. Graphs are Lagrangian, preserve
   composition and determine affine functions faithfully.
5. The diagonal cup/cap are half-dimensional isotropic subspaces in their
   exact opposite-form ambients. Both fully typed snakes reduce to one witness
   forced equal to the external input. The equation
   `eta_V^dagger=epsilon_V o sigma_(bar(V),V)` has correct factor types.
6. Name and unname retain exactly the same ordered subset of `V x W`, including
   nonfunctional, affine and empty relations. `End(0)` is exactly false/true;
   composition and transported tensor are Boolean conjunction; the closed
   loop is true because at least the zero vector is a witness and relations do
   not count witnesses.
7. No proof step divides by two, selects a basis/character/polarization, or
   invokes quantum normalization. The all-finite-field and characteristic-two
   scope is correct.

<!-- VERIFIED-CORRECT-END -->

## Checker and mutation register

The frozen SHA-256 matched the reported value. Green exited `0` with G1--G7
passing. All twelve named modes exited `1` at their intended gate:

| gate | named modes observed |
|---|---|
| G1 | `source-sign`, `empty-loss` |
| G2 | `middle-forall` |
| G3 | `dagger-order` |
| G4 | `tensor-order`, `zero-unit` |
| G5 | `graph-translation` |
| G6 | `compact-dual`, `cup-order` |
| G7 | `empty-name`, `loop-multiplicity`, `name-order` |

The bare `--red` parse-error path is OBJ-3. The missing later G6 reachability
is OBJ-4. The duplicated G4 comparison is OBJ-5. `RUNS.md` records outputs and
independent-copy mutations.

## Quantifier, characteristic, choice, reliance and status checks

- The mathematical proofs deliver every finite field, including `F2`, the
  zero object, empty arrows, affine translates and nontransverse composites.
- The opposite source form, tensor coordinate reorder, opposite-form dual,
  cup/cap orders and existential witness convention are explicit. OBJ-1 is the
  remaining unowned source-monoidal datum; OBJ-2 is the labbook quantifier
  loss.
- The local proofs do not depend on a REFUTED claim, `v0.1`, an unregistered
  source, SP-STAB-REL, quantum semantics or a smooth-relation theorem.
- Canonical SP-LREL and SP-COMPACT remain `SKETCH`; all proof headers and the
  labbook-fragment comment preserve that status. No premature promotion is
  claimed. The coordinator's pending multi-shard proof-path support is outside
  this verdict and is not treated as an objection.

FAIL(OBJ-1, OBJ-2, OBJ-3, OBJ-4)
