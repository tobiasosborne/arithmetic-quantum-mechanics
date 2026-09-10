# Single repair wave for the affine and tensor review

Date: 2026-09-10. Actual model: `gpt-5.6-sol`, reasoning `xhigh`.

This is the authorized repair of O1 only. O2 belongs to the independent
checker repair. The verdict marked the algebra calculations, signs,
composition, naturality, and coherence correct, so they are not reopened.
No trunk file or claim status is changed by this lane.

## D1703: exact replacement and anchors

In `definitions.md`, under the exact heading

    ## D1703 (odd-characteristic Weyl datum in arbitrary rank)

replace

    An abstract-space model additionally names a symplectic coordinate
    identification. At $n=0$ use $H_{k,0}=\mathbb C$ and the empty tensor.

with

    At $n=0$ use $H_{k,0}=\mathbb C$ and the empty tensor. Transporting
    this standard formula to an abstract symplectic space requires a named
    symplectic coordinate identification.

    Independently of such a coordinate choice, extend D9's model-groupoid
    prescription to arbitrary rank. `Mod_{ψ,β_V}(V)` has objects `(H,π)`,
    where `H` is a finite-dimensional complex Hilbert space and
    `π:A_{ψ,β_V}(V)→End_C(H)` is a unital `*`-representation whose
    underlying module is simple and for which every `π(W_{β_V}(v))` is
    unitary. Its morphisms `U:(H,π)→(H',π')` are unitary intertwiners
    satisfying `Uπ(a)=π'(a)U` for every `a∈A_{ψ,β_V}(V)`; identities and
    composition are the ordinary identities and composition of unitary
    maps. `PMod_{ψ,β_V}(V)` has the same objects and each Hom-set is the
    quotient by `U↦λU` for `λ∈U(1)`, with
    `[U']∘[U]=[U'∘U]`. When `V=V(k)` has rank one and
    `β_V=ω_V/2`, this is D9's existing model groupoid; D9's rank-one
    categories for other polarizing cocycles retain their meaning.

This separates the coordinate construction of the standard formula from
the arbitrary models quantified by the claims.

Still within D1703, replace the exact scope

    **Scope.** The half-form convention excludes characteristic two. The finite-abelian realization is already admitted; SP-WEYL records its coordinate, phase and central-quotient transport.

with

    **Scope.** The half-form convention excludes characteristic two. Named symplectic coordinates belong only to the construction and transport of the standard formula; they are not data of an arbitrary object of `Mod_{ψ,β_V}(V)`. The finite-abelian realization is already admitted; SP-WEYL records its coordinate, phase and central-quotient transport.

Replace

    **Reuses.** D3,D4,D5,D8,D1001,D1002,D1003,D1301,D1701.

with

    **Reuses.** D3,D4,D5,D8,D9,D1001,D1002,D1003,D1301,D1701.

Replace

    **Delta.** Extend the existing Weyl algebra notation to arbitrary rank and fix a symmetrized model by rephasing D8, without reversing position labels.

with

    **Delta.** Extend the existing Weyl algebra notation and D9's unitary model groupoid/projectivization to arbitrary rank, and fix the coordinate standard model by rephasing D8 without reversing position labels. Arbitrary model objects do not require the standard coordinates.

D9 itself remains unchanged. The extension specializes to D9 only at the
rank-one half-form cocycle and preserves D9's other rank-one categories.

## Notation owner

In `notation.md` replace the exact row

    | `Mod_{ψ,β}(κ)`, `PMod_{ψ,β}(κ)` | the model groupoid; its projectivization | D9 |

with

    | `Mod_{ψ,β}(κ)`, `PMod_{ψ,β}(κ)`; `Mod_{ψ,β_V}(V)`, `PMod_{ψ,β_V}(V)` | the rank-one model groupoid and its projectivization; their arbitrary-rank half-form extension | D9,D1703 |

This extends the existing owner row and creates no duplicate.

## Claim and DAG dependency citations

In the `SP-WEYL`, `SP-EGOROV`, and `SP-TENSOR` rows of
`claims/CLAIMS.md`, replace only these depends-on cells:

    D3,D4,D5,D8,D1001,D1002,D1003,D1701,D1703,F1-DUAL,F1-WEYL,F1-REAL
    D1003,D1701,D1703,SP-WEYL,F1-REAL
    D1004,D1701,D1703,SP-WEYL,SP-EGOROV,F1-FUNCT

respectively by

    D3,D4,D5,D8,D9,D1001,D1002,D1003,D1701,D1703,F1-DUAL,F1-WEYL,F1-REAL
    D9,D1003,D1701,D1703,SP-WEYL,F1-REAL
    D9,D1004,D1701,D1703,SP-WEYL,SP-EGOROV,F1-FUNCT

The statements and `SKETCH` cells remain unchanged.

In `claims/PHANTASM-DAG.md` use the headings `## SP-WEYL`,
`## SP-EGOROV`, and `## SP-TENSOR` as block anchors. Add D9 to each block's
`Definitions` line, yielding respectively

    - Definitions: D3,D4,D5,D8,D9,D1001,D1002,D1003,D1701,D1703
    - Definitions: D9,D1003,D1701,D1703
    - Definitions: D9,D1004,D1701,D1703

No other DAG field changes for O1.

## Proof repairs made in this lane

The proof computations are untouched. In `sp-egorov.md`, D9 was added to the
definition citations; `<1>6` now quantifies over objects of D1703's
arbitrary-rank `Mod` groupoids, and `<1>8` types `R_V,R_W` as their
morphisms. In `sp-tensor.md`, D9 was added to the citations and the three
models in `<1>8` are now objects of those groupoids. D1703 is cited at the
corresponding leaves. There are no changes to either proof's `<1>1`--`<1>5`,
composition equations, signs, phases, or coherence equations.

## Exact labbook restatement

The updated `labbook-stage1.tex` begins with an inclusive string-anchor
replacement for the D1703 tail, scope, and provenance in
`labbook/sections/symplectic_phantasm.tex`. It restates exactly the model
objects, unitary intertwiners, ordinary composition, and `U(1)` quotient,
and adds D9 to the reuse provenance.

The Weyl proof now begins “If \(V\) is nonzero...” and treats the zero
coordinate map separately. The Egorov and tensor proof quantifiers refer to
the newly owned groupoids. The three proof insertions retain their exact
provenance anchors and all existing `\statusSketch{}` macros.

O1 is closed once these blocks are integrated and mechanically verified.
No genuine phase lift is introduced. O2 is untouched here.
