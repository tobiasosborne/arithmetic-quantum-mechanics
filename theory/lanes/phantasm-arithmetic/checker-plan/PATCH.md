# PATCH — future checker integration anchors

This lane supplies no implementation and makes no trunk/status change.

1. Proposed future files:
   `theory/checks/phantasm_arithmetic_check.py` and
   `theory/checks/phantasm_arithmetic_EXPECTATIONS.md`.
2. After implementation, anchor the SP-TRACE and SP-FROB `Checks`/tested-in
   fields and retain `phantasm_reuse_check.py` alongside the new checker. R6
   remains the existing F81/F9 bridge; do not rewrite it as the new scope.
3. Anchor SP-SUBSYS `Checks`/tested-in to the new checker only after A8--A12
   exist and every red path is observed. Keep evidence `draft` until proof
   review/adjudication.
4. Before SP-FROB promotion, apply the dependency repair already specified in
   `briefs/phantasm-arithmetic-target.md`: add D1706/SP-CP and state that reuse
   is limited to unitary-conjugation channel typing. Mirror it in the claim,
   DAG and labbook.
5. Before SP-SUBSYS proof integration, anchor on D1710 and explicitly own the
   compatibility diagram for direct versus iterated `J` data, including the
   associator and phase allowance. If that definition is not adopted, narrow
   the canonical decoder-tower clause instead.
6. Run both arithmetic checkers, the contract checker and ordinary lockstep/
   build/session-close gates after coordinator integration.
