# Proposed ownership and work-order anchors

No canonical file is changed by this planning lane.

1. `definitions.md`, anchor `## D1708 (bosonic Fock space and bounded second
   quantization)`: after the `Gamma_s(T)` formula, add the named normalized
   homogeneous map `U_(H,K):Gamma_s(H) tensor Gamma_s(K) ->
   Gamma_s(H direct-sum K)` from BRIEF, including its slot order and vacuum/
   zero convention. Mark unitarity and naturality as SP-FOCK obligations.

2. `notation.md`, anchor the D1708 row: add `U_(H,K)` as the normalized
   exponential-law candidate, distinct from later rig data.

3. `definitions.md`, anchor D1711's sentence
   `iota_(QP)(a)=a tensor 1 with the required coordinate reordering`: replace
   it by the increasing-prime simple-tensor formula in BRIEF. Keep the same
   map name and scope.

4. `refs/LEDGER.md`, anchor SP-DER06: sharpen the locators to lines
   1814--1829, 1843--1851, 1871--1875, 1911--1964, 2019--2038, and
   2051--2090. Anchor SP-CM08 with lines 23015--23025, 23106--23114,
   23930--23947, and 30474--30493; state that separating is not inherited for
   arbitrary states. Anchor SP-CM04 with lines 1763--1783 and 1829--1837.

5. Create future canonical proof shards `fock.md`, `prime-tensor.md`, and
   `bc-control.md`; create `phantasm_completions_check.py` and its expectations.
   Register proof/review/check paths only after artifacts exist. Preserve all
   three SKETCH/planned statuses during proving.

6. Do not add SP-JOY81, SP-SPECTOR98, a factor-classification source, or a
   modular theorem as a dependency of these exact local proofs. Do not modify
   DG-RIG, DG-GLOBAL, DG-MODULAR, or DG-SPECTRUM in this campaign.
