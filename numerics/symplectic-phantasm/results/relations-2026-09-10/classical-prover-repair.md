# Single repair wave for SP-LREL and SP-COMPACT

Date: 2026-09-10.  Repair model: `gpt-5.6-sol`, reasoning `xhigh`.

This is the sole prover repair wave authorized against
`theory/lanes/phantasm-relations/critic/VERDICT.md`.  It addresses OBJ-1,
OBJ-2, and the proof-locator part of OBJ-6.  The independent checker lane owns
OBJ-3--OBJ-5.  No trunk edit, status promotion, re-review, or change to the
critic-verified mathematical calculations is made here.

## OBJ-1: own the source monoidal structure in D1701

In `definitions.md`, anchor on the exact sentence

> Composition is $(s,h)\circ(t,g)=(s+ht,hg)$ and the identity is $(0,1_V)$.

Insert immediately after it:

```latex
For affine arrows $(t,g):V\to W$ and $(t',g'):V'\to W'$, prescribe
\[
 (t,g)\oplus(t',g')=((t,t'),g\oplus g'):
 V\oplus V'\longrightarrow W\oplus W'.
\]
The monoidal unit is the zero space with identity $(0,1_0)$.  For
symplectic spaces $U,V,W$, prescribe the associator, left and right unitors,
and symmetry to be the zero-translation affine arrows whose linear parts are
\[
\begin{aligned}
 a_{U,V,W}&:(U\oplus V)\oplus W\longrightarrow U\oplus(V\oplus W),
 &((u,v),w)&\longmapsto(u,(v,w)),\\
 \lambda_V&:0\oplus V\longrightarrow V,&(0,v)&\longmapsto v,\\
 \rho_V&:V\oplus0\longrightarrow V,&(v,0)&\longmapsto v,\\
 \sigma_{V,W}&:V\oplus W\longrightarrow W\oplus V,&(v,w)&\longmapsto(w,v).
\end{aligned}
\]
```

The words “prescribe” and “zero-translation” are essential: D1701 owns the
source data, while SP-LREL proves bifunctoriality and coherence.

In the D1701 Delta field, anchor on

> **Delta.** Arbitrary-rank finite symplectic objects and affine symmetry arrows; the rank-one field and local-ring forms retain their existing meanings.

Replace it by:

> **Delta.** Arbitrary-rank finite symplectic objects and affine symmetry arrows, together with their direct-sum symmetric monoidal data; the rank-one field and local-ring forms retain their existing meanings.

In `notation.md`, replace the D1701 affine-groupoid row containing
`S_k^aff` by a row whose meaning also includes the displayed direct sum of
affine arrows.  Replace the D1714 coherence row containing
`a_(U,V,W)` by:

> | `a_(U,V,W)`, `lambda_V`, `rho_V`, `sigma_(V,W)` (relation coherence) | zero-translation affine tuple coherence maps and their graph associator, left/right unitors and swap | D1701,D1714 |

This records the source affine arrows first and their D1714 graph images
without introducing a second symbol family.

In `labbook/sections/symplectic_phantasm.tex`, anchor on the exact D1701
sentence

> Composition is $(s,h)\circ(t,g)=(s+ht,hg)$ and the identity is $(0,1_V)$.

Insert the same displayed D1701 text before `\end{definition}`.  Update its
provenance Reuses/Delta wording in lockstep with the single source.

The repaired `lrel-laws.md` now has a separate section 5.  It checks affine
arrow tensor against composition and identities, proves source naturality and
tuple coherence, and only then concludes that graphs form a faithful
symmetric monoidal functor.  Its graph tensor and coherence leaves cite the
repaired D1701 clauses explicitly.

## OBJ-2: exact D1714 labbook quantification

`LABBOOK-FRAGMENTS.tex` has been rebuilt to begin its D1714 restatement with
the current canonical opening:

```latex
Fix a finite field $k$ and finite-dimensional symplectic $k$-spaces $U,V,W$.
Use the affine Lagrangian relation prescription for arrows between these
spaces. Prescribe the compact dual of $V$ to be the existing
opposite-form object $\overline V$.
```

The remainder is the current canonical D1714 body through the single
transported-scalar prescription, followed by its exact current Scope.  The
free-object-variable defect is therefore removed; no compact calculation
changed.

## OBJ-6: canonical proof locators

The repaired `compact.md` makes these exact replacements:

- nonexistent `lrel.md` sections 4--5 becomes `lrel-laws.md` sections 4--5;
- nonexistent `lrel.md` section 1 `<1>6` becomes
  `lrel-reduction.md` section 1 `<1>6`;
- the final `PROPOSAL.md` justification becomes the canonical
  `SP-COMPACT` row in `claims/CLAIMS.md` and its
  `claims/PHANTASM-DAG.md` contract;
- the introduction likewise names the canonical claim and DAG rather than
  treating the lane proposal as ground truth.

## Mechanical repair checks

After these lane edits:

- `lrel-reduction.md`, `lrel-laws.md`, and `compact.md` remain within the
  200--500 line shard limit;
- no `lrel.md` proof citation remains;
- no `PROPOSAL.md` citation remains in `compact.md`;
- D1714's repaired lane labbook fragment binds `U,V,W` before first use;
- every status remains `SKETCH` pending coordinator adjudication.
