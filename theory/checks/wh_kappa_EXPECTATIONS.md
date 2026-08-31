<!-- ROLE: pre-registration for the wh-kappa falsifier. Written BEFORE
     wh_kappa_check.py existed, from briefs/wh-kappa-target.md alone.
     Lane wh-check. Nothing here was derived from any proof shard: the lane
     did not read theory/lanes/wh-kappa/prove/ or v0.1/report/. -->

# EXPECTATIONS — what each gate must produce, fixed before implementation

## Status of this file

Pre-registration. Every number below was obtained *before* `wh_kappa_check.py`
was written, either by hand from `briefs/wh-kappa-target.md` or by an
independent scratch computation using a deliberately different representation
(see "Independent scratch" below). If the checker disagrees with anything here,
the disagreement is reported as a finding in `SUMMARY.md`; the expectation is
not edited to match the code.

## Conventions taken from the brief (verbatim inputs, no other source)

- `kappa = F_q`, `V = kappa (+) kappa`, `omega((a,b),(a',b')) = a b' - a' b`.
- `beta((a,b),(a',b')) = a b'` (non-symmetrised).
- `psi_zeta(x) = zeta^{Tr_{kappa/F_p}(x)}`, `zeta` a primitive `p`-th root of 1.
- `W(v)W(v') = psi(beta(v,v')) W(v+v')`.
- `q` in {2, 3, 4, 5, 8, 9}; exact arithmetic in `Z[zeta_p]`; no tolerances.

## Derivations done by hand from those conventions

- **D-a (alternating).** `omega(v,v) = a b - a b = 0` identically, in every
  characteristic. Hence *every* cyclic subgroup and every `kappa`-line is
  `omega`-isotropic. **Consequence: "a non-isotropic line" does not exist.**
  The `--red-nonisotropic` mutation therefore cannot be a line; the closest
  realisable defect is a non-isotropic additive subgroup of order `q` (D-f).
- **D-b (polarizing identity).** `beta(v,v') - beta(v',v) = a b' - a' b = omega(v,v')`.
- **D-c (line count).** Nonzero vectors `q^2 - 1`, each line has `q - 1` of
  them, lines `= (q^2-1)/(q-1) = q+1`.
- **D-d (the model and its rank).** Take `P = kappa e1`, `Q = kappa e2`,
  `V = P (+) Q`, and put `W(u+w) e_y = psi(omega(u,y)) e_{y+w}` for `u in P`,
  `w, y in Q`. With `u=(a,0)`, `y=(0,x)`, `w=(0,b)` this is
  `W(a,b) e_x = psi(a x) e_{x+b}`, and
  `W(v)W(v') = psi(omega(u,w')) W(v+v') = psi(a b') W(v+v') = psi(beta(v,v')) W(v+v')`
  — the brief's ordering convention, on the nose. Writing `W(a,b) = D_a T_b`
  with `D_a = diag(psi(ax))_x` and `T_b` the translation by `b`: the `q` maps
  `x |-> psi(ax)` are pairwise distinct (nondegeneracy of `(a,x) |-> Tr(ax)`),
  so the `D_a` span the diagonal algebra; multiplying by the `q` translations
  gives all `q^2` matrix units. Hence **rank = q^2** and, since the `W(v)`
  already span `M_q(C)`, **commutant = centre of `M_q(C)` = scalars, dim 1**.
- **D-e (general cocycle of the builder).** For any splitting `V = P (+) Q`
  the same formula gives `W(v)W(v') = psi(omega(pi_P v, pi_Q v')) W(v+v')`, and
  `c - c^T = omega - omega|_P - omega|_Q`. So the commutation relation of
  `WH-COMM` holds **iff both `P` and `Q` are `psi(omega)`-isotropic**. This is
  what `--red-nonisotropic` breaks.
- **D-f (when a non-isotropic polarization exists).** An order-`q` subgroup of
  `V` is an `F_p`-subspace of `F_p`-dimension `n`. For `n = 1` (`q` prime) it is
  a cyclic group, i.e. a line, so by D-a it is isotropic: **the mutation is not
  constructible for `q` in {2,3,5}**, and this is a theorem, not a checker gap.
  For `n >= 2` it exists (confirmed by census below).
- **D-g (characteristic 2 blind spot of C1).** `beta^T - beta = -omega`, and at
  `p = 2`, `-omega = omega`. So the transposed-cocycle mutation satisfies the
  C1 identity exactly at `q in {2,4,8}`: **C1 cannot see `--red-cocycle` at
  characteristic 2.** C3 must catch it there.
- **D-h (C8 is vacuous at p = 2).** The primitive `p`-th roots of unity number
  `p - 1`; at `p = 2` there is exactly one (`zeta = -1`), so "two distinct
  primitive `zeta`" has no instance at `q in {2,4,8}`. The substantive content
  at every `q` is the `kappa^x`-torsor of the `q - 1` nontrivial additive
  characters `psi_c(x) = zeta^{Tr(cx)}`.
- **D-i (two isotropy notions diverge for n >= 2).** `Tr_{F_4/F_2}(1) = 1+1 = 0`,
  so the subgroup `{0,(1,0),(0,1),(1,1)}` of `F_4 (+) F_4` has
  `omega((1,0),(0,1)) = 1 != 0` (not `kappa`-isotropic) yet `psi(omega) = 1` on
  it (isotropic for the `F_p`-form `Tr . omega`). The checker must therefore
  distinguish `omega|_P = 0` from `Tr(omega|_P) = 0`; the mutation must violate
  the *strong* (`Tr`) one to actually break the Weyl relations.
- **D-j (halving).** `2` is invertible in `kappa` iff `p` is odd; the inverse is
  `(p+1)/2` embedded: `2` in `F_3` and `F_9`, `3` in `F_5`. At `p = 2`,
  `2 = 0` has no inverse and `omega/2` has no value.

## Independent scratch computation

Numbers marked [S] come from a scratch script kept outside the repo
(`scratchpad/scratch_expect.py`), written before the checker and using a
deliberately different representation, so that a shared bug is unlikely:

- roots of unity are **specialised** `zeta_p -> z in F_ell` with `z` of exact
  order `p` (`ell = 3, 7, 11` for `p = 2, 3, 5`), so all linear algebra is done
  modulo a small prime with numpy integers — not in `Z[zeta_p]`;
- field elements are coefficient tuples with a separately written reduction;
- subgroups are enumerated by RREF canonical forms.

Soundness of the specialisation, in the direction used: minors reduce, so
`rank_{F_ell} <= rank_{Q(zeta)}` and `nullity_{F_ell} >= nullity_{Q(zeta)}`.
Both quantities below are pinned exactly because each has a matching bound from
D-d (rank `<= q^2`; commutant `>= 1`, containing the identity).

One defect was found and fixed *in the scratch script* during this run: a loop
variable `c` shadowed the commutant dimension in the report line, printing
`q-1` instead of the computed value. The computation was correct; the report was
not. Recorded because it is exactly the failure mode this pre-registration
exists to catch: the first table produced was internally inconsistent
(`rank = q^2` — the operators span `M_q` — together with `commutant = q-1`,
which is impossible), and the inconsistency is what exposed it.

## Green run — expected value of every gate, per q

`|V| = q^2`; C1, C3, C4 are exhaustive over all `q^4` ordered pairs.

| q | p | n | q^2 | q^4 pairs | C1 | C2a alt | C2b nondeg | C2c bilin | C3 | C4 |
|---|---|---|-----|-----------|----|---------|------------|-----------|----|----|
| 2 | 2 | 1 | 4  | 16   | PASS | PASS | PASS | PASS | PASS | PASS |
| 3 | 3 | 1 | 9  | 81   | PASS | PASS | PASS | PASS | PASS | PASS |
| 4 | 2 | 2 | 16 | 256  | PASS | PASS | PASS | PASS | PASS | PASS |
| 5 | 5 | 1 | 25 | 625  | PASS | PASS | PASS | PASS | PASS | PASS |
| 8 | 2 | 3 | 64 | 4096 | PASS | PASS | PASS | PASS | PASS | PASS |
| 9 | 3 | 2 | 81 | 6561 | PASS | PASS | PASS | PASS | PASS | PASS |

| q | C5 rank [S] | C6 commutant dim [S] | C7a lines | C7b all iso | C8 #prim zeta | C8 #nontriv psi | C9 inverse of 2 |
|---|-------------|----------------------|-----------|-------------|---------------|-----------------|-----------------|
| 2 |  4 |  1 |  3 | yes | 1 (test vacuous) | 1 | none (p=2) |
| 3 |  9 |  1 |  4 | yes | 2 | 2 | 2 |
| 4 | 16 |  1 |  5 | yes | 1 (test vacuous) | 3 | none (p=2) |
| 5 | 25 |  1 |  6 | yes | 4 | 4 | 3 |
| 8 | 64 |  1 |  9 | yes | 1 (test vacuous) | 7 | none (p=2) |
| 9 | 81 |  1 | 10 | yes | 2 | 8 | 2 |

Subgroup census (C7d — pre-registered here, asserted by the checker) [S]:

| q | # order-q subgroups | # `omega`-isotropic (= # kappa-lines) | # `Tr.omega`-isotropic | Tr(1) |
|---|--------------------|---------------------------------------|------------------------|-------|
| 2 |    3 |  3 |   3 | 1 |
| 3 |    4 |  4 |   4 | 1 |
| 4 |   35 |  5 |  15 | 0 |
| 5 |    6 |  6 |   6 | 1 |
| 8 | 1395 |  9 | 135 | 1 |
| 9 |  130 | 10 |  40 | 2 |

Read-off, pre-registered as claims about these numbers:

- the `omega`-isotropic order-`q` subgroups are **exactly** the `q+1`
  `kappa`-lines, for every `q` (column 3 = `q+1` throughout);
- the two isotropy notions coincide iff `n = 1` (columns 3 and 4 agree exactly
  for `q = 2,3,5` and differ for `q = 4,8,9`), confirming D-i;
- for `q` prime every order-`q` subgroup is isotropic (columns 2 and 4 agree),
  confirming D-f: `--red-nonisotropic` is not constructible there.

## Pre-registered red matrix — which gate must fire, and where

Predicted before implementation. `FIRE` = the gate must report failure; `pass` =
the gate must NOT fire (a mutation that fires everything proves little, so the
passes are part of the prediction).

| mode | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | first gate |
|---|---|---|---|---|---|---|---|---|---|---|
| `--red-symmetric`    | FIRE | FIRE (C2a) | FIRE | FIRE | FIRE | FIRE | FIRE | pass | pass | C1 |
| `--red-trivial-char` | pass | pass | pass | pass | FIRE | FIRE | pass | FIRE | pass | C5 |
| `--red-cocycle`      | FIRE iff p odd | pass | FIRE | pass | pass | pass | pass | pass | pass | C1 (p odd) / C3 (p=2) |
| `--red-nonisotropic` | pass | pass | FIRE | FIRE | pass | pass | FIRE | pass | pass | C3, only q in {4,8,9} |
| `--red-dim`          | pass | pass | pass | pass | FIRE | pass | pass | pass | pass | C5 |
| `--red-halfweyl` (extra, not in the brief) | unevaluable at p=2 | pass | FIRE (p odd) | pass | pass | pass | pass | pass | FIRE at p=2 | C9 (p=2) / C3 (p odd) |

Quantitative predictions inside the red runs [S unless marked hand]:

- `--red-symmetric` uses `sigma((a,b),(a',b')) = a a' + b b'` — symmetric,
  nondegenerate, and **not** alternating (`sigma(v,v) = a^2 + b^2`), uniformly
  in `p`. This choice is forced: the obvious symmetrisation `a b' + a' b`
  *equals* `omega` at `p = 2` and would be a no-op there.
  Predicted C5 rank `= q`, C6 commutant `= q` [S]; C7 count of `sigma`-isotropic
  lines `= 1, 0, 1, 2, 1, 2` for `q = 2,3,4,5,8,9` (hand: a line is isotropic
  iff `a^2 + b^2 = 0`, i.e. iff `a = b` when `p = 2`, and iff `-1` is a square
  when `p` is odd — it is in `F_5` and `F_9`, it is not in `F_3`).
- `--red-trivial-char` predicted C5 rank `= q`, C6 commutant `= q` [S]
  (`W(a,b)` collapses to the translation `T_b`); C8 finds `0` nontrivial
  additive characters instead of `q-1`.
- `--red-cocycle` fires nothing at `q in {2,4,8}` through C1 (D-g) — the
  characteristic-2 blind spot is the point of the mode, and C3 is what covers it.
- `--red-nonisotropic` keeps `Q = kappa e2` Lagrangian and replaces `P` by the
  graph of an `F_p`-linear, non-`kappa`-linear map with `Tr(omega|_P) != 0`.
  Because `Q` stays Lagrangian the pairing `P x Q -> F_p` stays nondegenerate,
  so the mutation is **surgical**: predicted C5 rank `= q^2` and C6 commutant
  `= 1`, unchanged [S]. Not constructible for `q in {2,3,5}` (D-f) — the mode
  must say so rather than pretend to test something.
- `--red-dim` changes a *claim*, not the object: the computed rank stays `q^2`
  and is compared against the mutated claim `q^2 + 1`. It therefore fires at
  every `q` but tests only that C5 compares against a real computation.
- `--red-halfweyl` is **not one of the brief's five**. It is added because no
  brief mode reaches C9: without it C9 is decoration. It replaces `beta` by the
  symmetrised `omega/2`, which at `p = 2` requires inverting `2` and trips the
  C9 guard, and at `p` odd is a *different but internally consistent* cocycle,
  caught by C3 and not by C1.

## Gate reachability predicted before the runs

- C1: `--red-symmetric`, `--red-cocycle` (p odd only)
- C2: `--red-symmetric` only
- C3: `--red-symmetric`, `--red-cocycle`, `--red-nonisotropic` (n>=2), `--red-halfweyl` (p odd)
- C4: `--red-symmetric`, `--red-nonisotropic` (n>=2)
- C5: `--red-symmetric`, `--red-trivial-char`, `--red-dim`
- C6: `--red-symmetric`, `--red-trivial-char`
- C7: `--red-symmetric`, `--red-nonisotropic` (n>=2)
- C8: `--red-trivial-char` only
- C9: **no mode in the brief reaches it**; only the added `--red-halfweyl` does.

Two brief modes are predicted to be pairwise distinguishable from all others by
their firing sets, so no two of the five are bit-identical in effect; the closest
pair is `--red-trivial-char` and `--red-dim`, which share C5 but differ on C6/C8.
