# Typed classical wires and specified quantum backaction

Added during the single repair wave for core review objections CC1–CC2,
2026-09-07. These finite probes make the physical consequences of classical
routing and quantum instrument choice explicit. They do not establish the
general presentation/coherence theorem, which requires the repaired proof.

Run `python3 theory/checks/f1_limit_wiring_check.py`.

| Gate | Exact finite probe | Named mutation |
|---|---|---|
| W1 | A two-outcome C²→C³ instrument followed by a three-outcome C³→C² instrument; compare recorded sequential maps with fused lists after routing `(Q,P,O)` to `(Q,O,P)`, on a state and all input matrix units | --red-sequential-route |
| W2 | Parallel versions of those two instruments; route `(Q3,O2,Q2,P3)` to `(Q3,Q2,O2,P3)` and verify every outcome's product probability | --red-parallel-route |
| W3 | Reference traces Tr₂/2, Tr₃/3 and uniform trace on two outcomes: the full output density has quantum ratio 3/2 and classical factor 2 | --red-classical-trace |
| W4 | Independent six-element S3 convolution: derive the successful state from Kraus operator P₂, then apply the local transposition and final effect; success 2/3, conditional density 3P₂, return 1/4 and joint 1/6 | --red-backaction |
| W5 | Classical tuple associators, product-unit identification and interchange-history bijection for outcome cardinalities 2,3,2,2 | --red-history |

All numerical entries are rational Fractions. NumPy performs exact object
matrix arithmetic. The S3 calculation uses a separate direct permutation
convolution implementation, not the Hecke checker. No tolerance is used.

The W4 mutation changes the successful Kraus operator from P₂ to u₁P₂.
It preserves the POVM and completeness, but changes the subsequent joint
probability from 1/6 to 2/3. Thus the gate checks specified backaction rather
than fitting a preselected density to its own trace. W1–W2 mutations retain
the same matrix dimensions but omit the required routing permutations.

Every gate accumulates all its diagnostics and reports one acceptance
conjunction. Each red mode must exit one through a named mathematical FAIL,
without an interpreter exception. The backaction red was observed before
the first green run; the other advertised reds are likewise run before the
acceptance run. Final consolidated outcomes are recorded at adjudication.
