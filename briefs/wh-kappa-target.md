<!-- ROLE: campaign work order, written before the work (PRD lane discipline).
     Target: the first increment of the north-star definition. -->

# Target: the canonical quantum system of `Spec κ`, κ a finite field

## Why this first

The north star assigns canonical quantum systems to arbitrary arithmetic
schemes. `Spec κ` for `κ = F_q` a finite field is the seed case named in the
north star: it is the smallest nontrivial arithmetic scheme, its associated
symplectic object `κ ⊕ κ` is forced rather than chosen, and everything later —
closed points of a general scheme, thickenings, sheaf-valued label spaces,
fusion-categorical targets — must restrict to it. If the general definition
does not reproduce this case on the nose, the general definition is wrong.

This increment establishes the seed case **with every choice named**, because
the product word is *canonical* and the campaign is worthless if that word is
used loosely.

## Conventions to fix FIRST (L4; nothing may be derived before these are recorded)

These go in `definitions.md` as numbered definitions before any proof step uses
them. They are chosen to be **uniform in the characteristic, `p = 2` included**.

1. **The symplectic object.** `V(κ) = κ ⊕ κ` with
   `ω((a,b),(a',b')) = a b' − a' b`. Record: `κ`-bilinear; *alternating* in the
   strong sense `ω(v,v) = 0` (which in characteristic 2 is a strictly stronger
   requirement than antisymmetry, and must be checked, not inferred);
   nondegenerate.
2. **The polarizing cocycle.** `β((a,b),(a',b')) = a b'`, so that
   `β(v,v') − β(v',v) = ω(v,v')`. This *non-symmetrized* convention is
   mandatory: the symmetrized "half-Weyl" convention `ω/2` does not exist at
   `p = 2`, and silently inheriting an odd-characteristic convention is exactly
   the defect this campaign is built to avoid.
3. **The phase datum.** An additive character `ψ : (κ,+) → C^×`. The
   distinguished family is `ψ_ζ = ζ^{Tr_{κ/F_p}(·)}` where `Tr_{κ/F_p}` is the
   absolute trace (canonical) and `ζ` is a primitive `p`-th root of unity in `C`
   (**a choice**). Name it as a choice everywhere; do not let it become
   invisible.
4. **Weyl operators.** `W(v)W(v') = ψ(β(v,v')) W(v+v')`. Fix this ordering once.

## Statements to establish

Proposed ids and the register each is expected to reach. The expected register
is a prior, not a target: if the evidence lands lower, the label lands lower.

| id | statement | expected |
|---|---|---|
| `WH-FORM` | `ω` is `κ`-bilinear, alternating (`ω(v,v)=0`), nondegenerate, for every finite `κ` including `p=2`; `β − β^T = ω`; the group preserving `ω` is `SL_2(κ)` | PROVED |
| `WH-COMM` | `W(v)W(v') = ψ(ω(v,v')) W(v')W(v)`, uniformly in `p` | PROVED |
| `WH-ALG` | `A_ψ(V) := C_ψ[V]` (twisted group algebra for the cocycle `ψ∘β`) is central simple of dimension `q²` over `C`, hence `≅ M_q(C)` — **using no polarization** | PROVED |
| `WH-SVN` | up to unitary equivalence there is exactly one irreducible unitary representation of the Heisenberg group with central character `ψ`, of dimension `q` | PROVED |
| `WH-POL` | `ω`-isotropic `κ`-lines are in bijection with `P¹(κ)`, so there are exactly `q+1` Schrödinger models; the intertwiner between two models is unique up to a phase | PROVED |
| `WH-CHOICE` | the assignment depends on exactly one datum beyond `κ`, a nontrivial `ψ`; the nontrivial additive characters form a `κ^×`-torsor; distinct choices give abstractly isomorphic algebras with **no distinguished isomorphism** — so the assignment lands in a groupoid, not in a category of Hilbert spaces | PROVED |
| `WH-WEIL` | `SL_2(κ)` acts on `A_ψ(V)` by `C`-algebra automorphisms, and by Stone–von Neumann this lifts to a projective unitary representation on the model space | expect PROVED for the algebra action, **lower** for the lift; the cocycle's triviality is characteristic-sensitive and is NOT to be asserted |

`WH-WEIL`'s second half is the one most likely to come back at SKETCH. That is
an acceptable outcome; asserting it is not.

## Explicitly NOT claimed in this increment

No schemes beyond `Spec κ`. No non-reduced rings, no thickenings, no products,
no sheaf-valued label spaces, no general closed-point construction, no
Frobenius or Galois action, no fusion categories, no continuum or scale limits,
no zeta or Weil-conjecture content. None of these words appear in a claim row
produced by this increment.

## Pre-registered falsifier (written before the proof; L1, PRD)

`theory/checks/wh_kappa_check.py`, plain `python3` + `numpy`, no repo
dependency. **Exact arithmetic only:** represent `Z[ζ_p]` as integer vectors
modulo the `p`-th cyclotomic polynomial and compute Weyl matrices exactly. A
tolerance anywhere in this checker is a design failure.

Run over `q ∈ {2, 3, 4, 5, 8, 9}` — prime and non-prime, even and odd.

| gate | asserts |
|---|---|
| C1 | `β(v,v') − β(v',v) = ω(v,v')` for all pairs, exhaustively |
| C2 | `ω(v,v) = 0` for all `v` (**checked, not inferred**); `ω` nondegenerate |
| C3 | `W(v)W(v') = ψ(β(v,v')) W(v+v')` exactly in the Schrödinger model |
| C4 | the commutation relation of `WH-COMM` |
| C5 | the `q²` Weyl operators are linearly independent over `C`, hence span `M_q(C)` |
| C6 | the commutant of `{W(v)}` is the scalars (irreducibility) |
| C7 | the isotropic `κ`-lines number exactly `q+1` |
| C8 | two distinct primitive `ζ` give representations with **distinct central characters**, hence not unitarily equivalent, while the algebras are abstractly isomorphic |
| C9 | at `p = 2` the symmetrized cocycle is unavailable: `2` is not invertible in `κ`, and the naive `ω/2` convention has no value — the gate fires if any code path tries to form it |

**Red modes**, each of which must exit non-zero, and each of which must be
reported with the gate that killed it:

- `--red-symmetric` — replace `ω` by a symmetric form; C2 must fire.
- `--red-trivial-char` — take `ζ = 1`; C6 must fire (the algebra goes commutative).
- `--red-cocycle` — use `β(v,v') = a'b` while keeping the claimed identity; C1 must fire.
- `--red-nonisotropic` — feed a non-isotropic line as a polarization; C3 or C7 must fire.
- `--red-dim` — assert `q²+1` independent Weyl operators; C5 must fire.

A red mode that is bit-identical in effect to another red mode is a defect in
the checker, not a pass.

## Deliverables

1. `definitions.md` — D-numbered entries for the four conventions above.
2. `notation.md` — every symbol used, once.
3. `theory/wh-kappa.md` — the Lamport-structured shard (L6b).
4. `theory/checks/wh_kappa_check.py` — the falsifier, green and every red mode.
5. `theory/verdicts/wh-kappa-r1.md` — the hostile verdict.
6. `claims/CLAIMS.md` — rows at whatever status the loop produces.
7. `labbook/sections/…` — the owning section, in lockstep (L11).
8. `refs/LEDGER.md` — registered sources for Stone–von Neumann (finite),
   twisted group algebras, and the Weil representation. **No statement in the
   shard may cite memory for these.**

## Order of work

Sources land before the proof cites them. The checker is written **from this
brief**, not from the prover's shard, so that it is independent evidence. The
critic sees the shard and the checker, never the prover's reasoning.

---

## Errata (orchestrator, 2026-08-31, after wave-1 verification)

These correct defects in the brief above. They are binding; where an erratum
contradicts the original text, the erratum wins.

**E1 — the brief under-specified the operator model, and the omission hides in
characteristic 2.** The brief fixes the cocycle identity `β − β^T = ω` and the
Weyl relation `W(v)W(v') = ψ(β(v,v')) W(v+v')` with `β(v,v') = a b'`. Those are
mutually consistent. But the brief never says *which* Schrödinger model realizes
them, and the two naive models do not. Writing `X(a)|y> = |y+a>` and
`Z(b)|y> = ψ(by)|y>`, an independent orchestrator computation over
`q ∈ {2,3,4,5,8,9}` (exact, by specialising `ζ_p` to an element of order `p` in
`F_ℓ`) gives

- `W(a,b) = Z(b)X(a)`  =>  cocycle `−a b'`,
- `W(a,b) = X(a)Z(b)`  =>  cocycle `b a'`,

and **neither is `a b'` in odd characteristic**. Both naive orderings in fact
polarize `−ω`, not `ω`. The prover must therefore state the model explicitly and
pick one of: (i) `W(a,b) = Z(−b)X(a)`, equivalently replacing `ψ` by `ψ̄`;
(ii) restate D3 as `β(v,v') = b a'` and carry `β − β^T = −ω`; (iii) flip the sign
convention of `ω`. Any is acceptable; leaving it implicit is not, and whichever
is chosen must be the one the checker runs.

The point of method: at `p = 2` all three options coincide, because `−1 = 1`. A
sign convention validated only in characteristic 2 is not validated.

**E2 — C7 does not test isotropy.** Since `ω` is alternating, `ω(v,v) = 0` for
every `v`, so *every* `κ`-line in `V` is isotropic and the count `q+1` is just
`|P¹(κ)|`. The gate tests line-counting, not isotropy, and `WH-POL` must be
stated as a claim about maximal isotropic (Lagrangian) subspaces, with the
observation that in a two-dimensional symplectic space every line is one. The
brief's `--red-nonisotropic` mutation is consequently ill-posed for lines: the
check lane correctly redirected it to non-isotropic order-`q` *subgroups*, which
exist only for `q` non-prime, and verified their non-existence by census at
`q ∈ {2,3,5}` rather than asserting it.

**E3 — C1 is blind at `p = 2`.** `β^T − β = −ω = ω` in characteristic 2, so C1
cannot distinguish `β` from its transpose exactly where the campaign most needs
it. At `q ∈ {2,4,8}` only C3 catches a transposed cocycle. C1 alone would
certify the wrong convention in the characteristic this increment exists to
protect. This is the mirror image of E1, and together they say: **each
characteristic conceals a different sign defect, so no convention is validated
until it is validated in both.**

**E4 — C9 was decoration as specified.** None of the brief's five mutations
reaches it. The check lane added `--red-halfweyl` to reach it and flagged the
addition. Five sub-checks remain unreached by any mutation and are named as
decoration in the lane's `RED-MATRIX.md`, each with the mutation that would
reach it; closing those is follow-up work, not a blocker for this increment.

**E5 — C8's literal form is vacuous at `p = 2`** (there is only one primitive
square root of unity). Its substantive content is the `κ^×`-torsor of the `q−1`
nontrivial characters, and that is what `WH-CHOICE` must be tested against.
