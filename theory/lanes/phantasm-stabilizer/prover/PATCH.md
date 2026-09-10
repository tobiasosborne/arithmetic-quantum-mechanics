# String-anchored coordinator patch plan

Lane model: `gpt-5.6-sol`, reasoning `xhigh`.

This lane made no trunk edits.  D1715 and the constructive SP-STAB-REL row
were registered at `SKETCH` by the coordinator while the prover pass was
active; do not insert duplicate canonical text.

## 1. Proof shards

Copy without mathematical alteration:

- `intertwiner-line.md` to
  `theory/symplectic-phantasm/stabilizer-intertwiner-line.md`;
- `functor-laws.md` to
  `theory/symplectic-phantasm/stabilizer-functor-laws.md`;
- `equivalence.md` to
  `theory/symplectic-phantasm/stabilizer-equivalence.md`.

All three remain prover-pass artifacts until the one fresh blind review and
adjudication.  SP-LREL and SP-COMPACT are explicit dependencies and must be
admitted before SP-STAB-REL can be promoted.

## 2. Canonical definition and notation audit

In `definitions.md`, anchor on

> ## D1715 (stabilizer intertwiner space)

Verify the body matches the current canonical all-origin prescription: the
equation quantifies over every `r in R` and every `(v,w) in R-R`; the empty
relation receives `{0}`; no origin, nonzero representative, or functor is
retained.  The Scope must keep every normalization and CP assertion outside.

In `notation.md`, anchor on the rows containing

> `V_n`, `omega_n`, `Omega_(m,n)`

and

> `E_p(R)`

Verify they remain aliases/owners for D1703/D1715 only.  Do not add proof-local
`psi`, `H_n`, `W_n`, support-group, projector, vectorization, or time-reversal
symbols to the global notation table.

## 3. Claim and DAG proof paths

In `claims/CLAIMS.md`, anchor on the row beginning

> | `SP-STAB-REL` |

The statement is already canonical.  After proof integration, replace only
its “proved in” draft pointer with the three integrated proof paths for blind
review.  Keep status `SKETCH` and the exact dependency list, including
SP-LREL and SP-COMPACT.

In `claims/PHANTASM-DAG.md`, anchor on

> ## SP-STAB-REL

Replace `Proof: none` by the three comma-separated integrated proof paths.
Use the repository's prover-pass/draft evidence wording.  Do not fill Review,
replace Checks, say admitted, or remove Remaining until adjudication.

## 4. Labbook lockstep

The D1715 definition, exact Scope, canonical proposition, and proposition
Scope are already registered in:

- `labbook/sections/symplectic_phantasm.tex`, anchored by
  `\begin{definition}[stabilizer intertwiner space]`;
- `labbook/sections/symplectic_phantasm_contracts.tex`, anchored by
  `\begin{proposition}[The scalar-quotient stabilizer comparison]`.

Verify those exact restatements rather than adding another copy.
`LABBOOK-FRAGMENTS.tex` supplies concise proof prose.  Integrate that proof
only with its unreviewed status visible, or after adjudication with the final
status/provenance chosen by the coordinator.

## 5. Source and structural records

`SOURCE-LOCATORS.md` records the exact local source locators and the dagger
limitation.  In `docs/research-plans/categorical-structure.md`, anchor on the
D1704--D1705 carrier row.  After adjudication, link the actual SP-STAB-REL
proof and record only the established dagger symmetric monoidal comparison.
Do not add compact preservation: the proof uses SP-COMPACT to type
vectorization but the canonical claim does not assert that the equivalence
preserves the selected cups/caps.

## 6. Scope that must survive integration

The proof is for standard objects over an odd prime field and the fixed
trace-framed character.  It treats every D1307 second-level unitary, all
arities including zero, nonfunctional relations, empty relations and empty
composites, bare converse, Hilbert adjoint, exact grouped tensor order, and
the all-invertible-complex-scalar quotient with zero separate.  It asserts no
representative norm, probability, CP semantics, compact preservation,
extension-field result, or arithmetic-source exhaustion.
