# Blind hostile verdict — SP-SCALAR and SP-CP

Date: 2026-09-10. Critic model: `gpt-5.6-sol`, reasoning `xhigh`.
Same-family prover/critic; blind lane. I read only the literal allowlist in the
assignment, did not inspect any `theory/lanes/phantasm-processes/prover/` or
`checker/` file, and did not contact the prover.

Target hashes:

| target | SHA-256 |
|---|---|
| `scalar.md` | `f1126e855db0ec66d6929799ce7575b15cb9ee8ceb42bb4ce6a862566053bd5d` |
| `process-kraus-blocks.md` | `c4b8e406d19763a831bf89c881f9ef0a6ef3e4c8c21cec2def89f5403b333150` |
| `process-instruments.md` | `61a3765b33280df816454260d5e51d58e767f4e22ca4398e9fffcba9517776c6` |
| `symplectic_phantasm.tex` | `2183fa4d6d4695dd004b5769112b6ee7cd61010f1ed80a195df347448a823527` |
| `symplectic_phantasm_contracts.tex` | `c8ba9233291512bb8b163114b8a1bdc2cc7adebc23441122122a8153e84e6662` |
| installed checker | `2a64f59f814b99760af460a3f744ef96f83562beef55a5b4e34d30dcab87d1d0` |
| checker expectations | `b074c4abbcbafe657720cb9f3d4b6f1a8d39f0bb39590e603dfb2a7c5de82002` |

## Objections

### OBJ-1 — MAJOR — choosing an actual representative is not necessary to define a successful branch

**(a) Exact location.** Canonical `SP-SCALAR` row in `claims/CLAIMS.md`, final
sentence; `scalar.md` §5 `<1>5`--`<1>6` and §6 `<1>4`; owning labbook
proposition “Scalar normalization,” final consequence.

**(b) Independent computation.** For every nonzero D1705 class define

    N_[T](rho) = T rho T^* / ||T||^2.

If `S=cT` with `c!=0`, then `||S||^2=|c|^2||T||^2` and
`S rho S^*=|c|^2T rho T^*`, so `N_[S]=N_[T]`. Thus this is a well-defined CP
map of the projective class without selecting an actual representative. Also

    (T/||T||)^*(T/||T||) <= I,

so it is a D1706 successful branch. The zero class may be sent to the zero
branch separately. `scalar.md` §5 `<1>5` itself records exactly this
representative-independent operator-norm rule, but `<1>6` and the canonical
statement still say a branch arises *only* after choosing a representative.

Different class-invariant rules (operator norm, Hilbert--Schmidt norm, or
other homogeneous gauges) need not agree or compose functorially. Therefore
D1705 does not already stipulate a canonical lift, and the raw formula
`[T] -> Phi_T` does not descend. Those facts do not imply that choosing a
particular representative is the only way to add a lift.

**FIX DEMAND.** Replace the necessity clause everywhere by: D1705 stipulates
no actual branch; one is specified only after adding either an admissible
representative or a class-invariant normalization rule, whose functorial
compatibility is a separate obligation.

**SURVIVING WEAKER STATEMENT.** `Phi_T` is CP, is TNI iff `T^*T<=I`, and obeys
`Phi_(cT)=|c|^2Phi_T`; phases fix the map, the unnormalized formula does not
descend through `C^times`, and D1705 itself chooses no lift or probability.

### OBJ-2 — MINOR — general trace-adjoint existence is prescribed but only the CP case is constructed

**(a) Exact location.** D1706 paragraph prescribing
`Phi^(tr*):B_Y->B_X` for every complex-linear `Phi`; `process-instruments.md`
§5 ASSUME and `<1>1`--`<1>4`; labbook process proof at the paragraph beginning
“Finally, the ordinary-trace adjoint is”.

**(b) Independent computation.** The proof starts with a CP map and obtains
its adjoint from a Kraus family. D1706 quantifies over every complex-linear
map. Existence and uniqueness in that generality follow because the matrix
units of the finite direct-sum blocks make the ordinary Hilbert--Schmidt
pairings nondegenerate: the coefficient matrix of `Phi^(tr*)` is the conjugate
transpose of the coefficient matrix of `Phi`. Watrous defines this unique
adjoint for every linear map at `paper.txt` lines 1097--1105. The target proof
mentions nondegeneracy for uniqueness but never supplies this general
existence leaf or cites that locator.

**FIX DEMAND.** Add a preliminary Lamport step constructing the adjoint of an
arbitrary complex-linear block map by matrix units/nondegenerate duality, then
specialize to the Kraus formula for CP maps.

**SURVIVING WEAKER STATEMENT.** Every D1706 CP map has the displayed reverse
Kraus adjoint; it is CP, branches give subunital adjoints, channels give
unital adjoints, and the discard example proves the adjoint need not be TNI.

### OBJ-3 — MINOR — P3's only advertised mutation never reaches its Choi or completeness checks

**(a) Exact location.** `phantasm_process_check.py` `gate_p3`, especially the
`kraus-adjoint-order` type check followed by the matrix-unit, Choi-PSD and
per-input completeness assertions; `phantasm_process_EXPECTATIONS.md` P3
mutation row.

**(b) Independent computation.** The sole P3 red changes the Kraus direction
and fails immediately at the forward/reverse type assertion. It never reaches
the five matrix-unit coefficient comparisons, four independently reconstructed
Choi PSD tests, or completeness/strictness assertion. On a temporary copy I
changed the actual `x1->y0` Kraus operator from `(1/2)I_2` to `2I_2`. P1 and P2
passed; P3 passed the coefficient/Choi paths and then failed specifically at
`per-input block completeness/strictness failed`. Thus the late assertion is
live but has no advertised mutation path.

**FIX DEMAND.** Add one actual-data P3 mutation that preserves forward type
and reaches the coefficient oracle, and another overcomplete Kraus mutation
that first fails the per-input completeness assertion.

**SURVIVING WEAKER STATEMENT.** Green P3 supplies exact finite coefficient,
Choi and completeness controls; `kraus-adjoint-order` validly tests the
rectangular direction boundary.

## Independently verified correct — do not churn in repair

<!-- VERIFIED-CORRECT-BEGIN -->

### SP-SCALAR

1. For every finite auxiliary `E`, amplification of `rho -> T rho T^*` is
   conjugation by `1_E tensor T`; the quadratic-form proof includes `T=0`.
2. Rectangular index summation gives
   `Tr_K(T rho T^*)=Tr_H(T^*T rho)`.
3. TNI on all positive inputs is equivalent to `T^*T<=I`: sufficiency uses
   `Tr((I-T^*T)rho)>=0`, and necessity follows from every rank-one
   `rho=|x><x|`.
4. `Phi_(cT)=|c|^2Phi_T`, including `c=0`; phases fix the CP map, while a
   non-unit modulus changes it when `T!=0`. Zero output is never conditionally
   normalized.

### SP-CP

5. A displayed block Kraus family is CP on arbitrary amplified block inputs.
   Conversely, each component `pi_b Phi iota_a` of an intrinsic CP map is CP;
   Watrous Theorem 2.22 applies only when that component is nonzero, and the
   empty list correctly handles zero components.
6. The ordinary block trace is
   `sum_a Tr(A_a rho_a)`. Rank-one inputs supported on one block prove TNI iff
   every `A_a<=I`; the same tests prove trace preservation iff every `A_a=I`.
7. Kraus lists are presentation evidence in D1706, whose equality is equality
   of maps. `{K}` and `{(3/5)K,(4/5)K}` realize the same map without changing
   D1325's finer source equality.
8. Composite indices `(b,j,t)` and tensor indices `(j,u)` are correctly typed.
   The tensor effect identity proves contraction on every block, while the
   matrix-unit spanning argument covers entangled inputs as well as products.
9. Retained instruments have outcome-first blocks `(o,b)`, ordinary trace one
   with no `|O|` factor, sequential keys `(o,r)`, and tensor keys `(o,s)`.
   Their channel sums expand exactly as claimed.
10. The CP trace adjoint has reverse Kraus maps `K^*`; its value on identity is
    the branch effect. The adjoint of `Tr:M_2->C` maps `1` to `I_2`, so it is
    unital CP and not a reverse TNI branch.
11. FRP-CP is reused only for its admitted finite matrix calculations.
    Intrinsic ambient Kraus exhaustion neither changes D1325 equality nor
    asserts arithmetic/stabilizer source fullness.

<!-- VERIFIED-CORRECT-END -->

## Checker and mutation register

The installed hashes matched the supplied frozen values. Green exited `0`
with P1--P11 passing. Help advertised exactly seventeen named flags and no
generic `--red`; every flag exited `1` at its registered P1--P11 gate.

The paths are distinct in mutated data. In particular,
`sequential-hide-first` produces two later-only keys, whereas
`sequential-pair-order` produces four reversed keys even though both share the
same failure message. P6's path-loss and tensor-tag defects, P7's erased-block
and trace-factor defects, and P10's direction and non-TNI defects fail at
separate assertions.

Independent temporary-copy controls:

- replacing P3's `(1/2)I_2` by `2I_2` failed the late P3 completeness path;
- changing P4's actual channel weight `3/5` to `2/5` passed P1--P3 and failed
  P4's channel assertion;
- disabling only P10's non-TNI classification guard made the real
  `adjoint-is-branch` mutation survive with exit `0`.

P3's red reachability limitation is OBJ-3. No whole checker gate reduces to a
textually identical self-comparison. `RUNS.md` preserves the exact outputs.

## Quantifier, choice, source, reliance, and status checks

- The proofs quantify over arbitrary nonzero finite-dimensional Hilbert
  spaces and finite nonempty families of nonzero blocks. Zero maps/components
  remain included. No field characteristic is used in the ambient theorem.
- D1706 uses the sum of ordinary matrix traces. No normalized matrix, Weyl,
  coefficient, or uniform classical trace is substituted.
- Outcome-first, sequential and tensor order are explicit. Kraus lists used in
  proofs are choices of presentation, not retained D1706 data.
- SP-WAT18 has exactly the cited finite-dimensional scope; its Theorem 2.22
  has the handled nonzero-map hypothesis. SP-CK21 supplies only the reason
  projective scalar normalization is absent, not a branch or instrument lift.
- No proof depends on a REFUTED row, `v0.1`, an unregistered source, or a
  source-exhaustion assertion.
- Both canonical rows, DAG nodes, proof headers, labbook propositions and
  provenance remain `SKETCH`/draft. Lockstep is honest. OBJ-1 is a statement
  defect reproduced consistently in claim and labbook rather than a status
  mismatch.

SP-CP has no open FATAL or MAJOR on its canonical statement. SP-SCALAR has the
single MAJOR necessity overstatement in OBJ-1.

FAIL(OBJ-1)
