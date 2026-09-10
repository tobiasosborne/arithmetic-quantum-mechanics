# Blind hostile verdict — SP-TRACE, SP-FROB, SP-SUBSYS

Date: 2026-09-10. Critic model: `gpt-5.6-sol`, reasoning `xhigh`.
This was the sole same-family prover/critic pass under a literal blind lane. I
did not read arithmetic prover/checker lane artifacts, source-reuse notes,
patches, summaries, hidden reasoning, or root reasoning.

Frozen targets checked:

- `trace.md`: `bc866d7dc3ced40e1fc05d267bf2f98698130c849fc69be8ba13d4df67a5a84a`;
- `frobenius.md`: `104797e27041bfa3004402bd3c9204174f426ca6dfa539313ff824d6af880669`;
- `subsystem-models.md`: `03d9466a51f68434f10d8bef7ab63f33e758a015d3d4294722f62e862aef639d`;
- `subsystem-decoder.md`: `a0335511700a45e832ed9ac09f1534413c1771a66a79dae97b813d9bccc0641f`;
- checker: `047f6948b9abfa65691213a489a8816a4a9b916d9070c11f73a4bd28d23ffa4c`;
- expectations: `7e3cc7f9ff96bc123d9055bca0095612e7705b076ccada8c63f8f56e7e829f2d`.

I treated admitted FRB-TRACE, FRB-FROB, SP-WEYL, SP-TENSOR, SP-CP, and
FRP-CP only at their registered scopes and did not re-review them. SP-FROB is
mathematically conditional on its explicit still-unpromoted SP-TRACE
dependency and must be promoted after it. No REFUTED row is used.

## Separate dispositions

| claim | mathematical disposition | condition |
|---|---|---|
| SP-TRACE | PASS | admitted FRB-TRACE and SP-WEYL |
| SP-FROB | PASS | promote only after SP-TRACE; SP-CP supplies channel typing only |
| SP-SUBSYS | PASS | admitted SP-WEYL, SP-TENSOR, and SP-CP |

## Numbered objections

### 1. MINOR — a redundant direct dependency is cited but not registered

**(a) Location.** `theory/symplectic-phantasm/subsystem-decoder.md`, section 5
`<1>2`, lines 239--242, versus the canonical SP-SUBSYS dependency lists in
`claims/CLAIMS.md:290` and `claims/PHANTASM-DAG.md:403--405`.

**(b) Independent computation.** Section 5 needs only the definition-level
boundary that a D1327 code decoder has success amplitude `s^*`, residual
projection `1-ss^*`, and a retained failure output. D1327 lines 1932--1940
states all of this directly. The added citation to admitted FRP-DESCENT is
therefore unnecessary, is omitted from the final QED dependency list, and is
not registered as a direct SP-SUBSYS dependency.

**FIX DEMAND.** Delete `/FRP-DESCENT` from section 5 `<1>2`; do not enlarge the
canonical dependency list for a definition-level comparison.

**SURVIVING WEAKER STATEMENT.** The entire SP-SUBSYS argument, including its
support-code boundary, follows from the dependencies already registered.

### 2. MINOR — A6 accepts a vacuous covariance census

**(a) Location.** `theory/checks/phantasm_arithmetic_check.py`,
`covariance_case` and `gate_a6`, lines 389--421; EXPECTATIONS A6; the DAG
falsifier record at `claims/PHANTASM-DAG.md:394`.

**(b) Independent computation.** A6 increments and prints `total` but never
checks its registered value. On a temporary copy I replaced the actual state
census at line 398 by the empty tuple. The complete checker exited 0 and
printed `A6 PASS: 0 exhaustive-rank1/sparse-rank2 monomial covariance cases`.
The intended current split is 19,683 and 12,393 F27 cases plus 531,441 and
85,293 F81 cases, totaling 648,810.

**FIX DEMAND.** Assert the four per-field/rank census sizes or the total
648,810, and add a real census-loss red whose first failure is A6.

**SURVIVING WEAKER STATEMENT.** The frozen current source actually executed
all 648,810 registered cases and they passed; this remains finite evidence and
does not carry the arbitrary-rank proof.

## Independently verified correct

<!-- VERIFIED-CORRECT-BEGIN -->

### SP-TRACE

- `trace.md` section 1 `<1>1`--`<1>6` correctly uses trace surjectivity rather
  than `d*x`: scaling a nonzero symplectic pairing to a trace-one scalar proves
  nondegeneracy in every rank even when the characteristic divides `[E:K]`.
- Section 2 correctly proves nontriviality for every named nontrivial
  `chi_K`, without identifying it with the fixed absolute character.
- Section 3 `<1>1`--`<1>10` gives exact equality of the two half-form
  multipliers, stars, units, Weyl bases, and coefficient traces. Rank zero is
  the identity on `C`; characteristic two is explicitly excluded here.
- Section 4 is correctly typed for a tower only when the intermediate
  character is induced from the named bottom character. Under that necessary
  compatibility, trace transitivity makes the two identity-label maps equal.

### SP-FROB

- `frobenius.md` sections 1--2 correctly prove that `x -> x^|K|` is a
  K-linear automorphism, preserves the relative trace and every relative
  named character, and has `[E:K]`th power identity. No minimal period is
  asserted.
- Section 3's basis calculation transforms both translation and phase
  coordinates and gives exact covariance in D1703's sign/half convention.
  It applies to standard `E^n` registers only; abstract spaces retain D1709's
  requirement for a separately named semilinear datum.
- Section 4 correctly uses one unitary Kraus operator for the ordinary-trace
  channel, constructs the adjoint inverse, and handles the empty tensor at
  rank zero. SP-CP supplies typing only.

### SP-SUBSYS

- `subsystem-models.md` section 1 proves the nondegenerate orthogonal direct
  sum for every symplectic injection, including zero retained or complement
  rank. The displayed sum map preserves the form exactly.
- Sections 2--4 correctly use the admitted full-matrix tensor model and
  unitary-model uniqueness to obtain `J`, the combined-complement unitary,
  and all four iterated J maps. The staged and direct routes implement the
  same Weyl labels, hence differ by exactly one allowed phase.
- `subsystem-decoder.md` sections 1--3 correctly type the observable map in
  the forward direction and the decoder in the reverse direction. The Kraus
  rows give ordinary partial trace, completeness, trace preservation,
  trace-duality, Weyl-characteristic restriction, and phase cancellation.
- Section 4 uses the full D1710 compatibility equation, the explicit
  reassociation, and the complement unitary's transported basis. It proves
  both inclusion and decoder tower laws and makes no claim for incompatible
  independently chosen model data.
- The support-code success map remains distinct from this trace-preserving
  tensor decoder. No field embedding is silently treated as a symplectic
  subsystem.

### Shared scope and lockstep

- The choices are explicit: named base character for trace/Frobenius;
  standard coordinates for `U_(E/K,n)`; common character, irreducible model
  spaces, model unitary up to phase, and full iterated compatibility for the
  subsystem.
- The four proofs, exact CLAIMS rows, DAG, definitions/notation, and integrated
  labbook statements agree in strength. The GF libraries are compared only
  on their common prime-field F3 encoding.
- No result is extended to a characteristic-two half-form, arbitrary abstract
  Frobenius without data, global assembly, normalized decoder, or support-code
  identification.

<!-- VERIFIED-CORRECT-END -->

## Quantifier and status register

The written proofs cover all finite extensions and ranks at the exact odd
characteristic scope, not only F27/F3 and F81/F9. The subsystem theorem covers
all odd-characteristic finite fields and all compatible D1710 model data, not
only the F3 permutation fixture. A separate F4/F2 computation confirms that
the classical trace may remain nontrivial while `Tr(1)=0`; the missing half in
characteristic two correctly blocks the quantum half-form claim.

All three canonical rows, four proof headers, DAG entries, and labbook
propositions remain SKETCH/draft with review pending. This is the honest
register before repair and adjudication. This verdict performs no promotion.

PASS
