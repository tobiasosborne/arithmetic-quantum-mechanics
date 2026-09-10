# String-anchored completion prover handoff

Lane model: `gpt-5.6-sol`, reasoning `xhigh`.

This lane makes no trunk, claim-status, checker or Git changes. D1708 and
D1711 are used exactly as registered.

Copy the proof shards without scope expansion:

- `fock.md` to `theory/symplectic-phantasm/fock.md`;
- `prime-tensor.md` to `theory/symplectic-phantasm/prime-tensor.md`;
- `bc-control.md` to `theory/symplectic-phantasm/bc-control.md`.

In `claims/CLAIMS.md`, anchor on `SP-FOCK`, `SP-PRIME`, and
`SP-BC-CONTROL`; replace only the draft proof pointers with the corresponding
integrated paths using unreviewed prover-pass wording. Preserve all exact
statements, dependencies and `SKETCH` statuses.

In `claims/PHANTASM-DAG.md`, anchor on the same three headings and replace
`Proof: none` with those paths. Do not fill Review, say admitted, remove
Remaining or add dependencies before the single blind review and
adjudication.

`LABBOOK-FRAGMENTS.tex` contains exact copies of each canonical proposition
and Scope followed by prose and LaTeX at the binding writing-guide register.
Anchor the existing propositions in
`labbook/sections/symplectic_phantasm_contracts.tex`; add proofs only with
unreviewed provenance visible, or after adjudication with final statuses.

`SOURCE-REUSE.md` records the precise primary locators and analytic
boundaries. The independent checker remains separately owned. Finite red and
green runs are required for integration but cannot establish completion,
self-adjointness, continuity, state extension, GNS boundedness or trace-class
convergence.

Preserve the exclusions: no strong-monoidal/coherence claim, Hall promotion,
inter-prime arithmetic coupling, state/representation faithfulness,
separating vector, factor/KMS classification, universal BC faithfulness,
global/modular comparison or zeta-zero spectrum.
