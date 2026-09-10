# Phantasm process cluster — representatives, branches, and retained outcomes

Preparation date: 2026-09-10.  Planning model: `gpt-5.6-sol`, reasoning
`xhigh`.

This is the next bounded work order after the relation/stabilizer cluster.
It prepares SP-SCALAR followed by SP-CP.  It contains no proof, checker
implementation, review, status change, or authorization to resume a paused
programme.

## Result sought

The cluster must separate three levels that the current definitions already
distinguish:

1. an actual linear representative `T` and its CP map
   `rho |-> T rho T^*`;
2. a D1706 trace-nonincreasing branch, which additionally requires
   `T^*T<=1` or the multi-Kraus block analogue;
3. a D1705 projective class, which contains no preferred norm and therefore
   determines neither an actual CP map nor a success probability.

SP-SCALAR proves this separation for a one-Kraus map.  SP-CP proves the
intrinsic finite-block Kraus criterion and the closure, retained-outcome and
ordinary-trace laws of the ambient process category.  Neither result claims
that arithmetic or stabilizer syntax exhausts ambient branches.

The exact canonical statements remain the SP-SCALAR and SP-CP rows of
`claims/CLAIMS.md`.  Their current dependencies remain FRP-CP.  SP-STAB-REL
is relevant motivation for projective classes, but is not silently added as
a mathematical dependency of the scalar matrix calculation.

## Pinned source scope and exact locators

Use only the registered local SP-WAT18 and SP-CK21 bodies plus admitted local
proofs.

### SP-WAT18

Local body: `refs/symplectic-phantasm/SP-WAT18/paper.txt`.

- Lines 1148--1158 define completely positive, trace-preserving and unital
  maps.
- Lines 3626--3661 give Kraus representations and the trace-dual formula
  `Phi^*(Y)=sum_a A_a^*YB_a`.
- Theorem 2.22, lines 3785--3808, characterizes complete positivity by a
  same-family Kraus representation.
- Theorem 2.26, lines 4020--4097, proves trace preservation iff the
  ordinary-trace adjoint is unital and gives the Kraus completeness formula.
- Corollary 2.27, lines 4125--4144, specializes this to channels and
  `sum_a A_a^*A_a=1`.
- Lines 5106--5184 define instruments as CP families with a channel sum,
  give outcome probability `Tr(Phi_a(rho))`, condition only after positive
  probability, and encode the retained outcome as a classical block.

These locators supply finite-dimensional CP/Kraus/trace facts.  The local
proof must still perform the D1706 direct-sum block and outcome-index
conversion; the source does not use this repository's tagged block notation.

### SP-CK21

Local body: `refs/symplectic-phantasm/SP-CK21/lagrel.tex`.

- Lines 3611--3649 define the stabilizer target modulo every invertible
  complex scalar.
- Lines 3703--3744 state the odd-prime symmetric monoidal comparison at that
  quotient scope.

This source supports the reason normalization was forgotten.  It supplies no
canonical representative, norm, branch probability or instrument lift.

## Exact admitted reuse

The admitted proof is
`theory/sidequests/frobenius-hierarchy/process-category.md`.

| admitted clause | exact reusable content | boundary in this cluster |
|---|---|---|
| FRP-CP `<1>6` | Amplified positivity of a finite Kraus sum, block by block | The old amplitudes are arithmetic images; reuse the matrix calculation for arbitrary finite Hilbert Kraus operators, not the source-exhaustion premise |
| FRP-CP `<1>7` | `Tr(K rho K^*)=Tr(K^*K rho)` and the ordinary-trace deficit/completeness calculation | Generalize from a source certificate to the intrinsic operator inequality; do not import certificate syntax into D1706 |
| FRP-CP `<1>8` | Expansion of sequential Kraus composition and functoriality at realized-map equality | D1706 equality is actual CP-map equality, while D1325 retains source lists and external tags |
| FRP-CP `<1>9` | Distribution of tensor over finite direct sums, matrix-unit comparison, entangled-input validity and coherence | Reuse the ordinary block tensor comparison with D1706's arbitrary Hilbert blocks |
| FRP-CP `<1>10` | Normalized basis preparation and ordinary-trace discard semantics | Use as regression cases; it does not prove arbitrary-state or arbitrary-branch source generation |
| FRP-CP `<1>11` | Distinct source amplitudes can realize the same CP map | Preserve D1325 source equality while D1706 uses equality of actual CP maps |
| FRP-CP `<1>12` | Explicit external-tag retention and later forgetting only by a typed routing map | Compare to D1706's outcome-first direct-sum block, without identifying the two source categories |

D1326 fixes the sum of ordinary matrix traces.  D1706 extends exactly that
target to arbitrary nonzero Hilbert blocks.  No normalized matrix trace,
uniform classical trace, coefficient trace or Weyl trace may replace it.

## Pre-proof type repair to D1706

There is one bounded ownership gap.  The SP-CP statement refers to
trace-dual adjoints and ordered sequential outcomes, but D1706 does not name
the trace adjoint or prescribe the order of sequential/tensored outcome
pairs.  The mathematics is unambiguous, but the single-source rule requires
the convention before proof.  Extend D1706; do not allocate a new definition
number.

After the retained-version sentence, prescribe the outcome-first block
identification
\[
 \bigoplus_{o\in O}B_Y
 =\bigoplus_{(o,b)\in O\times B}\operatorname{End}(K_b),
 \qquad (\rho_o)_o=(\rho_{o,b})_{(o,b)}.
\]
For instruments $(\Phi_o)_{o\in O}:B_X\to B_Y$ and
$(\Psi_r)_{r\in R}:B_Y\to B_Z$, prescribe their sequential family to be
\[
 (\Psi_r\circ\Phi_o)_{(o,r)\in O\times R};
\]
the first component is the earlier outcome.  For independent instruments
$(\Phi_o)_{o\in O}$ and $(\Theta_s)_{s\in S}$ prescribe the tensor family
$(\Phi_o\otimes\Theta_s)_{(o,s)\in O\times S}$ in listed-factor order.

For every complex-linear map $\Phi:B_X\to B_Y$, prescribe its
ordinary-trace adjoint $\Phi^{\operatorname{tr}*}:B_Y\to B_X$ by
\[
 \sum_b\operatorname{Tr}\!\left(y_b^*\Phi(x)_b\right)
 =\sum_a\operatorname{Tr}\!\left(
   \Phi^{\operatorname{tr}*}(y)_a^*x_a\right)
 \quad(x\in B_X,\ y\in B_Y).
\]
Add `Phi^(tr*)` to the D1706 notation row.  Extend D1706's Scope by the
sentence: “The ordinary-trace adjoint is an ambient reverse-direction map;
even when it is completely positive, it is not required to be a
trace-nonincreasing branch.”  Extend Delta only to mention outcome-pair order
and the ambient trace adjoint.

No other definition repair is needed.  In particular, the retained direct
sum is again a D1706 object through the displayed `(o,b)` reindexing, and the
sequential/tensor instrument families are constructions on already defined
branches.

The adjoint boundary is material.  Ordinary discard
`Tr:M_2(C)->C` is a channel, but its trace adjoint sends `1` to `I_2` and
increases ordinary trace from `1` to `2`.  SP-CP may prove that a channel has
a unital CP adjoint; it must not claim that adjoint is automatically a D1706
branch in the reverse direction.

## Proof package A — SP-SCALAR

One Lamport shard, target 220--320 lines.

**Inputs.** Nonzero finite-dimensional Hilbert spaces `H,K`, any linear map
`T:H->K`, and `c in C`.

**Required steps.**

1. Reuse FRP-CP `<1>6`'s amplified quadratic-form calculation for the
   one-Kraus map `Phi_T(rho)=T rho T^*`, including `T=0`.
2. Use rectangular cyclic trace to prove
   `Tr(Phi_T(rho))=Tr(T^*T rho)`.
3. Prove the iff, not only sufficiency:
   `Phi_T` is trace-nonincreasing on all positive inputs iff `T^*T<=I`.
   For necessity test every rank-one positive operator `|x><x|`.
4. Prove `Phi_(cT)=|c|^2 Phi_T`, including `c=0`; prove unit-modulus changes
   leave the CP map fixed, while general invertible rescaling changes it.
5. State the exact D1705 consequence: `[T]` supplies no chosen member and no
   norm.  A nonzero class has admissible contractions after a noncanonical
   rescaling, but an actual successful branch requires choosing a particular
   representative satisfying the inequality.  The zero class gives the zero
   branch and is never conditionally normalized.

**Must not claim.** A canonical scale, a probability attached to a
projective class, or a functor from the `C^times` quotient to actual CP maps.

## Proof package B — SP-CP intrinsic block criterion

One Lamport shard, target 300--430 lines.

**Inputs.** Finite nonempty Hilbert families
`X=(H_a)`, `Y=(K_b)` and a complex-linear map `Phi:B_X->B_Y`.

**Required steps.**

1. For a displayed D1706 Kraus family, repeat the amplified positivity
   calculation blockwise.  Show the block output is CP without assuming a
   product input or one input block.
2. Conversely, for intrinsic CP `Phi`, define
   `Phi_(b,a)=pr_b o Phi o inc_a`.  Prove each component is CP and apply
   SP-WAT18 Theorem 2.22 to obtain a finite Kraus list.  Treat a zero
   component by an empty list.  Reassemble the component lists into D1706's
   `K_(b a,j)` family.
3. Prove trace nonincrease iff
   `sum_(b,j) K_(b a,j)^*K_(b a,j)<=I_(H_a)` separately for every input
   block `a`.  Necessity uses a positive input supported on that one block
   and rank-one tests.
4. Prove channel iff equality holds in every input block.  Relate this to
   the trace adjoint formula and SP-WAT18 Theorem 2.26.
5. Make Kraus-list nonuniqueness harmless: D1706 equality is equality of
   actual linear maps.  Operations are defined on maps and any selected list
   is proof data; do not replace D1325 source equality by Kraus mixing.

This shard establishes intrinsic exhaustion for the ambient finite-block
target only.  It does not establish arithmetic or stabilizer source
exhaustion.

## Proof package C — closure, instruments, and adjoints

One Lamport shard, target 320--460 lines.

**Required steps.**

1. Give composite Kraus indices `(b,j,t)` and operators
   `L_(c b,t)K_(b a,j)`.  Prove the per-input inequality and equality for
   channels.
2. Give tensor indices `(j,t)` on block
   `((b,d),(a,c))` and operator `K_(b a,j) tensor L_(d c,t)`.  Prove
   `A_a tensor B_c<=I tensor I` and channel equality.  Use the D1326/D1706
   direct-sum distribution, including entangled inputs.
3. For an instrument, show each branch is CP/TNI and the sum is a channel.
   Flatten the retained codomain with outcome-first index `(o,b)`.  Prove
   its ordinary trace is
   `sum_o Tr_Y(Phi_o(rho))=Tr_X(rho)`, with no factor `|O|`.
4. For sequential instruments use the exact external outcome pair `(o,r)`
   and branch `Psi_r o Phi_o`.  Prove the sum over all pairs is the composite
   of the two channel sums.  Never turn `o` into a hidden Kraus index.
5. For tensor instruments use `(o,s)` in listed-factor order and prove the
   sum is the tensor of the channel sums.
6. Derive
   `(Phi^(tr*)(y))_a=sum_(b,j)K_(b a,j)^*y_bK_(b a,j)`.
   Prove it is CP and reverses direction.  Prove a channel has a unital
   adjoint and a branch has a subunital adjoint.  Exhibit ordinary discard
   to show the adjoint need not be TNI and hence need not be a reverse D1706
   branch.
7. Reconcile FRP-CP exactly: arithmetic realized composition/tensor,
   ordinary trace, normalized preparations/discards and retained external
   tags are instances.  D1325 equality remains finer and the ambient theorem
   supplies no arithmetic Kraus exhaustion.

## Exact checker package

Freeze expectations before proof integration.  Proposed checker:
`theory/checks/phantasm_process_check.py`, using integer/Fraction arithmetic
and Gaussian-rational pairs where a nonreal phase is needed.  It is a finite
falsifier, not evidence for arbitrary dimension.

### Green gates

| gate | exact finite control |
|---|---|
| P1 — scalar map | On `C^3`, use `I`, `diag(1,0,0)`, and `diag(1,1/2,0)` with `c=0,1/2,2,i`; compare matrix units, `|c|^2` scaling and phase invariance |
| P2 — contraction iff | Test the same operators and rank-one rational vectors; `2I` fails TNI, contractions pass, and the zero map has zero probability without conditioning |
| P3 — block Kraus | Use `X=(C,C^2)` and `Y=(C^2,C)`; compare independently assembled matrix-unit superoperators, Choi Gram matrices and per-input completeness |
| P4 — ordinary block trace | Channel `M_2 -> M_2 direct-sum C` with Kraus `(3/5)I` into the first block and `(4/5)<0|,(4/5)<1|` into the second; ordinary output trace equals input trace and a dimension-normalized first block does not |
| P5 — Kraus equality | Compare the identity list `{I}` with `{(3/5)I,(4/5)I}` as actual CP maps while retaining them as distinct lists |
| P6 — composition/tensor | Compose and tensor rational dephasing, preparation and discard lists; independently compare on a full matrix-unit basis and verify Cartesian tag order |
| P7 — retained instrument | On `M_2`, branches `(3/5)rho(3/5)` and `(4/5)rho(4/5)` sum to the identity channel; retain two `M_2` blocks and verify trace one with no outcome-count factor |
| P8 — sequential outcomes | Follow outcomes `O=(red,blue)` with `R=(left,right)` using scalar Kraus weights `3/5,4/5` and `5/13,12/13`; retain all four outcome-first keys `(o,r)` and verify their channel sum |
| P9 — tensor outcomes | Tensor two two-outcome instruments and verify all four listed-factor keys, map equality and trace normalization |
| P10 — trace adjoint | Compare the explicit Kraus-adjoint formula against the ordinary block Hilbert--Schmidt pairing; for `Tr:M_2->C`, verify the adjoint is `lambda |-> lambda I_2`, unital and not TNI |
| P11 — admitted comparison | Re-run small D1327 basis preparation/discard and retained-tag examples through the ambient formulas, comparing actual maps while preserving source tags |

The checker should build the Kraus superoperator from one implementation and
the expected map from matrix-unit action/Choi Gram data in a separate
implementation.  Do not compare a function to a textually duplicated copy.

### Advertised named mutations

Expose only real no-argument mutation flags; do not expose a generic
`--red NAME` parser path.

| flag | first intended failure |
|---|---|
| `--red-scalar-modulus` | P1: replace `|c|^2` by `c^2`, detected at `c=i` |
| `--red-projective-branch` | P1: identify the maps for `T` and `2T` |
| `--red-contraction-reverse` | P2: reverse `T^*T<=I` |
| `--red-zero-conditioning` | P2: attempt conditional normalization of the zero branch |
| `--red-kraus-adjoint-order` | P3: use `K^*rho K` in the forward map |
| `--red-kraus-list-equality` | P5: compare Kraus lists rather than actual CP maps |
| `--red-block-normalized-trace` | P4: divide the `M_2` block trace by two |
| `--red-composite-index-loss` | P6: omit the intermediate block index from composite Kraus paths |
| `--red-tensor-tag-order` | P6: reverse only one Cartesian block-tag pair in the actual tensor construction |
| `--red-tensor-outcome-order` | P9: reverse the actual output outcome pair while leaving the block tensor intact |
| `--red-retained-drop-outcome` | P7: sum the two retained outcome blocks into one |
| `--red-retained-outcome-factor` | P7: multiply retained trace by `|O|` |
| `--red-sequential-hide-first` | P8: sum over the first outcome before output |
| `--red-sequential-pair-order` | P8: emit `(r,o)` instead of `(o,r)` |
| `--red-adjoint-direction` | P10: use `K y K^*` instead of `K^*yK` |
| `--red-adjoint-is-branch` | P10: assert the adjoint of discard is TNI |
| `--red-source-equals-cp` | P11: identify distinct D1325 source arrows from equal CP realizations |

Each caught mode must exit `1` at its one registered first gate and print
that gate. A surviving mutation must exit `0`; malformed usage or unexpected
exceptions exit `2` and are not successful mutation evidence. The
zero-conditioning mode must reach an explicit mathematical rejection, not
merely an uncaught division-by-zero exception. Observe all real red paths
before the final green record. A temporary control disabling the associated
acceptance comparison must allow its mutation to survive with exit `0`;
restore the source afterward. Mutations must change actual data or
operations used by the bulk comparison, not isolated preflight witnesses.

## Prove–attack–repair order

1. Register the minimal D1706 type repair and exact labbook restatement at
   no claim-status change.
2. Freeze checker expectations and observe every named mutation fail.
3. Prove SP-SCALAR in one 200--500-line Lamport shard.
4. Prove SP-CP in the two bounded Lamport shards described above.
5. Run one blind critic pass per claim artifact.  The critic recomputes the
   matrix and block arguments and checks the adjoint boundary; it does not
   read prover reasoning or expand into normalized stabilizer semantics.
6. Apply one repair wave, mechanically adjudicate, and promote only after
   every dependency and exact statement is admitted.  A green checker never
   promotes either claim.
7. Update the Phantasm labbook, categorical-structure comparison, DAG,
   handoff and gates in lockstep.

## Following priority under the full-campaign steering

Do not jump from this ambient process theorem to a global action.  The global
gate still lacks characteristic-two lift data, a scalar-retaining relation
lift, rig/additive decisions, prime assembly, Frobenius and subsystem maps.

The immediate follow-on should be one bounded SP-SUM pass.  It directly
consumes actual representatives and SP-CP, and resolves the already recorded
coherent-sum versus tagged-direct-sum distinction.  After that bounded pass,
prioritize the arithmetic spine `SP-TRACE -> SP-FROB` and the newly unlocked
SP-SUBSYS rather than treating Fock completion as evidence of arithmetic
globalization.  SP-FOCK and DG-RIG remain required before DG-GLOBAL. The coordinator adopts
the field-extension/subsystem comparison ahead of SP-FOCK as the next
priority; mathematical dependencies are unchanged.

Thus the proposed order is:

    SP-SCALAR, SP-CP
      -> one bounded SP-SUM closure
      -> SP-TRACE, then SP-FROB, with SP-SUBSYS after SP-CP
      -> SP-FOCK/DG-RIG and the other named global prerequisites
      -> DG-GLOBAL only when its dependency list is actually discharged.

This order answers the current full-campaign steering while preserving the
canonical DAG: it advances the immediate consumer of the process work, then
the arithmetic action needed for a meaningful global construction, without
mistaking an uncoupled tensor product or projective stabilizer equivalence for
the sought global system.

## Acceptance conditions

- D1706 owns outcome-pair order and the ordinary-trace adjoint before either
  proof cites them.
- SP-SCALAR proves the contraction iff and scalar modulus law for arbitrary
  finite dimensions, and states why D1705 has no automatic CP lift.
- SP-CP proves both directions of the intrinsic block Kraus criterion,
  composition/tensor/instrument closure, retained and sequential outcome
  indexing, and the exact trace-adjoint boundary.
- FRP-CP is reused only at its admitted arithmetic-image scope.
- Every proof shard is 200--500 lines, every claim remains honest through the
  capped loop, and exact rational checks are recorded only as finite
  falsifiers.
- No result asserts normalized stabilizer semantics, CP equality at the
  arithmetic source, extension-field stabilizer equivalence, global dynamics
  or a spectral consequence.
