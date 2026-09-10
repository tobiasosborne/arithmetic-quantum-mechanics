# String-anchored completion ownership patch

Preparation model: `gpt-5.6-sol`, reasoning `xhigh`.

This lane makes no trunk, proof, claim-status, checker or Git changes.

## D1708

In `definitions.md`, replace the complete block from

> ## D1708 (bosonic Fock space and bounded second quantization)

through its Delta paragraph immediately before `## D1709` with the proposed
D1708 canonical body in `CANDIDATE.md`. Do not copy the following source-check
paragraph into the canonical body; the ledger owns locators.

Make the exact same definition and Scope replacement in
`labbook/sections/symplectic_phantasm.tex`, anchored on its D1708 Fock
definition and provenance.

In `notation.md`, anchor on the D1708 row containing

> `P_r`, `U_pi`, `Sym^r H`, `Gamma_s(H)`, `Omega`, `N_H`

and add `jmath_H`, `jmath_K`, `Exp^(alg)_(H,K)`, and `Exp_(H,K)` as the
coordinate inclusions, algebraic homogeneous exponential candidate, and its
bounded extension when it exists. The new `Exp` name is distinct from every
existing `U`-symbol. Do not label the map strong monoidal or add a coherence
claim.

No SP-FOCK statement or dependency changes. The definition points out that
the comparison direction written in the claim is the adjoint of the proposed
tensor-to-direct-sum map once unitarity is proved.

## D1711

In `definitions.md`, replace the complete D1711 block from its heading
through Delta immediately before `## D1712` with the proposed D1711 body in
`CANDIDATE.md`. Mirror it exactly in the owning labbook definition.

The existing notation row already owns `P,A_P,iota_QP,A_pr,varphi_pr,d_p,
rho_p`; extend its description to say that `iota_QP` uses increasing-order
identity insertion, including the empty stage. No new symbol is needed for
the increasing-order mark.

No SP-PRIME statement/dependency changes. The homomorphism, isometry,
inductive-limit and state-extension clauses remain proof obligations. Do not
add an inter-prime arithmetic map, factor/separating claim or modular data.

## Timing

Apply only as the ownership gate for the completion cluster after the
arithmetic landing. These definitions do not authorize proofs or status
changes by themselves.
