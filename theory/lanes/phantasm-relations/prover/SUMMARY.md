# Prover summary

Lane model: `gpt-5.6-sol`, reasoning `xhigh`.

The lane supplies a complete prover-pass argument for the exact existing
`SP-LREL` statement and a source/definition-first proposal and proof for the
separate `SP-COMPACT` claim.  It made no trunk edit, status promotion, Git
action, checker claim, or quantum-process assertion.

The composition proof is finite linear algebra.  For
`L=R direct-sum S` in
`bar(V)+W+bar(W)+Z`, it reduces along
`C=bar(V)+Delta_W+Z`.  It proves
`C^perp={(0,w,w,0)}` and identifies `C/C^perp` symplectically with
`bar(V)+Z`.  For a general coisotropic `C`, Lagrangian `L`,
`K=C^perp`, `dim X=2N`, and `dim K=r`, the key calculation is

    dim(L cap C)=N-r+dim(L cap K),
    dim q(L cap C)=N-r=dim(C/K)/2.

Thus the relational composite is Lagrangian without transversality.  A
nonempty affine fiber intersection is a chosen point plus the linear
intersection; an empty fiber gives the retained empty relation.  The
companion shard proves associative existential composition, identities,
converse dagger, reordered direct-sum tensor and coherence, and the faithful
graph functor.  No step divides by two, so characteristic two is included.

Proposed D1714 prescribes only the opposite-form dual, graph tuple maps,
ordered diagonal cup/cap, fully unital name/unname, and the transported
scalar tensor.  The separate claim proves both snakes with every associator
and unitor shown, the dagger equation, and the inverse Hom-set bijection.
It classifies endomorphisms of `0` as exactly the empty relation and
`Delta_0`: composition and
`lambda_0 o (s direct-sum t) o lambda_0^(-1)` have Boolean multiplication,
and the closed cup--cap loop is `Delta_0` because relational composition
forgets the number of witnesses.

Artifacts:

- `PROPOSAL.md`: exact real-LaTeX definition, claim row, scope, Reuses/Delta,
  and DAG contract;
- `lrel-reduction.md`: 306-line Lamport reduction/composition shard;
- `lrel-laws.md`: 255-line Lamport category/coherence/graph shard;
- `compact.md`: 424-line Lamport compact-structure shard;
- `LABBOOK-FRAGMENTS.tex`: concise copy-ready proof and definition fragments;
- `PATCH.md`: string-anchored coordinator integration plan.

Mechanical validation performed in the lane: all proof shards are within
the required 200--500 line range and `git diff --check` reports no whitespace
errors.  No finite checker result is presented as proof.  The independent
checker lane owns executable expectations, and both claims remain subject to
the scheduled single blind review and adjudication.  The only formal
dependency added is `SP-COMPACT -> SP-LREL`; it prevents compact promotion
until the existing relation claim is admitted.

The authorized single repair wave is recorded in `REPAIR.md`.  It adds the
previously unowned direct-sum symmetric monoidal data for the affine symmetry
groupoid to the proposed D1701 patch, proves those source laws before using
the graph functor, restores D1714's `U,V,W` quantifiers in the lane labbook
fragment, and replaces stale proof locators.  It does not alter the
critic-verified reduction, affine, compact, or scalar calculations.
