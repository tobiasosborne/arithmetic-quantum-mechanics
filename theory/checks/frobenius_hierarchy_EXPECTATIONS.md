# Frobenius hierarchy checker expectations

Preregistered 2026-09-08 before checker implementation. Lane: independent
native Codex checker, inherited model/reasoning; no prover proof drafts used.
Source interface: `briefs/frobenius-hierarchy-target.md`, D1--D8, and messages
specifying the full scalar Pauli frame and the typed operational interface.
Finite passes are falsifiers, not general proofs or promotion decisions.

All arithmetic will use integers modulo p, exact cyclotomic coefficients,
Fractions, and positive square-root normalization denominators. No tolerance.
Fresh field arithmetic is implemented here; no external helper dependency.
F16 is constructed over F4 exactly as in A6, not as an unrelated field table.

| gate | preregistered green expectation | named data mutation and intended failure |
|---|---|---|
| A1-symplectic | Absolute trace pairing is nondegenerate, alternating and Frobenius invariant in F2,F3,F4,F8,F9,F16 | `frob-one-label`: leave momentum unchanged in the proposed Frobenius phase-space map; fail symplectic invariance |
| A1-Weyl | Direct basis actions satisfy the reference cocycle and Frobenius conjugation including odd characteristic | `weyl-positive-sign`: replace Z(-b)X(a) by Z(b)X(a); fail the reference cocycle in F3 |
| A2-code | Enumerate all +1 phase labels and vectors; get support i(K), rank |K|, projector average, and trace-labelled logical momenta | `code-phase-subfield`: use i(K) as the phase stabilizer labels for F2->F8; fail annihilator/support |
| A2-logical | Compressed physical W(i(a),b) has logical label (a,Tb), and momentum fibres are exactly cosets of ker T | `logical-momentum-inclusion`: use included momentum instead of a trace-dual lift in F2->F4; fail logical action |
| A3-transfer | Relative trace is onto, K-linear, Frobenius equivariant and transitive; J,V compose along F2->F4->F16 | `relative-trace-projection`: replace trace by coefficient projection; fail trace pairing |
| A3-Fourier | Negative-kernel F_E J = V F_K with denominator squares |E|=(|E|/|K|)|K|; Fourier is unitary | `fourier-positive-kernel`: reverse E kernel only in F3->F9; fail Fourier phase equality |
| A3-normalization | Fibre columns have norm one and tower denominators multiply | `trace-fibre-unnormalized`: omit fibre normalization; fail V*V=I |
| A4-multiplication | Gate is a permutation, equals supplied multiplicative increment, commutes with Frobenius and intertwines field inclusion on basis states | `multiplication-as-addition`: replace product by sum; fail multiplicative gate datum |
| A4-embedding | F4->F16 encoded multiplication has exact output support and logical action | `embedding-coefficient-swap`: swap tower coordinates of embedded outputs; fail intertwining |
| A5-upper | Exact target-Fourier blocks diagonalize the gate; all-translation finite-difference span filtration certifies the resulting phase table at C_(d+1) for prime p=2,3 and d=1..4 | `hierarchy-extra-register-term`: inject a phase depending on one extra independent register; fail claimed upper level |
| A5-strict | Observed d-fold mixed differences of the tabulated Fourier phase remain nonconstant; another trace-dual shift gives a nonzero scalar; exclude C_d, including separate-register degree 3/4 in small characteristic | `hierarchy-delete-factor`: erase one control factor from the phase table; fail strict-level exclusion |
| A6-tower | Exhaustively match sigma(a0,b0)=(a0^2+a*b0^2,b0^2), sigma^2=(a0+b0,b0), exact order four | `frobenius-no-shear`: delete a*b0^2; fail direct square comparison |
| A7-types | Matrix shapes match named source/target; sequential composition rejects mismatched typed systems | `process-wrong-target`: replace a decoder target with the source name; fail type check |
| A7-CP | Explicit retained Kraus branches give exact positive Gram representations, completeness, success effects and ordinary trace probabilities | `instrument-double-success`: double the success Kraus coefficient; fail completeness |
| A7-tower | Success decodes and declared deterministic reset reductions compose on every matrix unit | `sequential-reverse`: reverse a valid decoder sequence; fail source/target matching |
| A7-parallel | Independent instruments retain ordered outcome pairs and agree with tensor branch maps, including entangled input | `parallel-collapse-outcomes`: identify distinct ordered outcome pairs; fail retained outcome routing |
| A7-boundary | A global reset differs from independent local resets on a concrete product state | `reset-global-as-local`: substitute global reset for local reset; fail independent tensor output |

Implementation may add subgates and finite samples, but changes to these
expectations must be explained. Every named red is run before the final green,
must exit nonzero at its listed mathematical gate, and is frozen with its
diagnostic. Ordinary matrix traces are kept separate from normalized Hecke
coefficient traces. Global phases are ignored only for hierarchy membership.

Additional expectation registered before implementing it (algebra lane's
supporting FRB-NATURAL witness): A5-interference sums the actually computed
phase table of F_z M^(2) F_z* over the uniform coherent input. For Q=2,3,4,
the return amplitude must be (2Q-1)/Q^2 and the probability its square.
Mutation `interference-erase-phase` replaces that phase table by zero; it must
fail A5-interference, distinguishing this arithmetic gate from identity.

Final interface additions registered before implementation: A6-tower will
enumerate sigma^2 orbits in F16, requiring ten invariant-vector orbits and
four fixed basis labels (the F4-supported code). A7-Fourier will check both
branches of D_V F_E=(F_K direct-sum F_E) D_J for F2->F4, including the failure
projectors. Mutation `fourier-failure-original-code` substitutes Q_J for Q_V
on the left failure branch and must fail A7-Fourier.

Root-requested exit-status repair sentinel (specified before its repair):
the process exit must depend only on mathematical PASS/FAIL. In a temporary
copy, disable the A1-symplectic rejection and run `--red-frob-one-label`;
the surviving mutation must report PASS and exit 0. The distributed checker
must retain every gate and have no gate-disabling runtime option.

Final bounded category addition, specified by D1327 and preregistered in
`category/CHECKER-REQUIREMENTS.md` before implementation: A7-PREP checks
normalized computational-basis preparations and the hidden basis-bra discard
in F2,F3,F4,F8,F9,F16. The discard Kraus effects must sum to identity and its
action on every matrix unit must be the ordinary trace. Mutation
`discard-omit-bra` removes one hidden basis bra and must fail A7-PREP.

Formal review repair AC1: the A5-upper description above is narrowed to the
surviving exact computation. An indexing comparison of two expressions for
the same translation difference added no evidence and was removed. A5 still
extracts the actual Fourier blocks and tests the resulting phase table by
all-translation filtration and separate strictness witnesses; it does not
claim an additional independently computed Pauli-conjugation comparison.
