# String-anchored coordinator patch plan

Lane model: `gpt-5.6-sol`, reasoning `xhigh`.

This lane made no trunk, status, checker, or Git changes.  D1706 and its
labbook restatement are already canonical and need no prover edit.

## Weakened canonical SP-SCALAR statement

In `claims/CLAIMS.md`, anchor within the `SP-SCALAR` row on the exact old
text:

> Consequently a scalar-quotient stabilizer arrow becomes a specified successful branch only after a representative with an admissible norm is chosen; a phase change alone does not change that branch.

Replace it exactly by:

> The scalar-quotient stabilizer prescription stipulates no actual successful branch or probability. A branch can be specified using an admissible representative or an admissible class-invariant normalization rule; a phase change alone does not change the branch. Compatibility of an added normalization rule with composition is a separate obligation.

In `labbook/sections/symplectic_phantasm_contracts.tex`, use the same old
sentence as a string anchor inside the proposition titled `Scalar
normalization` and make the identical replacement. Do not change its Scope,
dependencies or status.

The exact full proposed canonical statement is therefore:

> For nonzero finite-dimensional Hilbert spaces $H,K$ and a linear map $T:H\to K$, the map $\Phi_T(\rho)=T\rho T^*$ is completely positive and is trace-nonincreasing exactly when $T^*T\leq1$. For every complex $c$, $\Phi_{cT}=\lvert c\rvert^2\Phi_T$. The scalar-quotient stabilizer prescription stipulates no actual successful branch or probability. A branch can be specified using an admissible representative or an admissible class-invariant normalization rule; a phase change alone does not change the branch. Compatibility of an added normalization rule with composition is a separate obligation.

## Proof shards

Copy without mathematical expansion:

- `scalar.md` to `theory/symplectic-phantasm/scalar.md`;
- `kraus-blocks.md` to
  `theory/symplectic-phantasm/process-kraus-blocks.md`;
- `instruments.md` to
  `theory/symplectic-phantasm/process-instruments.md`.

Keep SP-SCALAR and SP-CP at `SKETCH` for the one blind review.  Do not merge
the shards beyond the 500-line limit.

## Canonical records

In `claims/CLAIMS.md`, anchor on the rows beginning

> | `SP-SCALAR` |

and

> | `SP-CP` |

The proof paths are already staged by the coordinator. Apply the weakened
SP-SCALAR statement above, preserve the SP-CP statement, all dependencies and
both `SKETCH` statuses through adjudication.

In `claims/PHANTASM-DAG.md`, anchor on the headings `## SP-SCALAR` and
`## SP-CP`.  Replace `Proof: none` by the real proof paths and use the
repository's prover-pass evidence wording.  Do not fill Review, say admitted,
or remove the scalar/projective and source-exhaustion boundaries before
adjudication.

## Labbook

`LABBOOK-FRAGMENTS.tex` contains the proposed final SP-SCALAR proposition,
the unchanged exact SP-CP proposition, both Scope blocks, and repaired
descriptive proof prose. In
`labbook/sections/symplectic_phantasm_contracts.tex`, anchor on

> \begin{proposition}[Scalar normalization]

and

> \begin{proposition}[Closure and normalization of finite instruments]

Add the matching proof only with prover-pass/unreviewed provenance visible,
or after adjudication with the final status.  Do not duplicate or alter the
canonical statement text.

## Source and checker records

`SOURCE-REUSE.md` is the exact locator/reuse handoff.  The independent checker
and its frozen expectations remain separately owned.  Integration requires
the root's observed green and named-red records; no checker result appears in
these proof shards as mathematical evidence.

The scalar proof positively verifies operator-norm class normalization but
proves only that no branch/rule is stipulated in D1705. The CP proof first
constructs the adjoint for every linear block map and then keeps its CP
specialization ambient, not an automatic reverse branch. Preserve both scope
clauses during adjudication.
