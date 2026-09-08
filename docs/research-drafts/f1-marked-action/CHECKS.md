# Implemented finite evidence for the marked right Hecke action

Prover: gpt-6-astra, xhigh. The actual root executable is
`theory/checks/f1_limit_module_check.py`. The proposed claims refer only to
its implemented M1–M3 gates, not a hypothetical larger acceptance contract.
Root owns execution, mutation records and integration of this checker.
The general theorems rest on the structured proofs.

| Gate | Actual finite comparison | Implemented data mutation |
|---|---|---|
| M1 | Sparse actual flag-vector operators on F_2^3 and F_3^3 (168 and 1404 states): T_0/T_2 quadratics, commutation, product-basis star/Gram and all four minimal product-sector traces | `--red-module-shift`: use T_1 instead of the correctly shifted T_2 |
| M2 | Antichain labels, inclusion-basis decoding, orbital valency products and ordered right-action associativity through total rank four | `--red-module-marker`: move the marked antichain outside its first block |
| M3 | Traced expectation of a positive ambient square, tested by pairing with the included product basis, normalized trace and all four sector values | `--red-module-expect`: alter a marked expectation coefficient |

M3 is a finite positive-square falsifier, not a proof of complete positivity
at all matrix levels. M2's permutation associativity is not a substitute for
the matrix-corner or balanced-induction category proof. M1 independently
constructs the actual field operators, so its Gram comparison is stronger
than checking the same presentation twice.

## Independent label/downset recomputation completed in this lane

An independent exhaustive antichain census over permutation posets gave
`dim R_0,...,dim R_4 = 1,2,7,34,209`. For each source label and each right
permutation, its proposed composite label was present in the ambient census,
and `down_(u block v)(A)=down_u(A)` held. The image counts were:

| (m,n) | Source/image dimension | Ambient dimension |
|---|---:|---:|
| (0,3) | 6 | 34 |
| (1,1) | 2 | 7 |
| (1,2) | 4 | 34 |
| (2,1) | 7 | 34 |
| (2,2) | 14 | 209 |
| (3,1) | 34 | 209 |

For each of these labels the orbital valency product was also recomputed
exactly at rational q=3/2,2,3. This checks labels and factors; it does not
independently test kernel multiplication or CP positivity. No additional
executable gate or mutation contract is introduced by this one-off census.
