<!-- ROLE: edits to files OUTSIDE this lane's write scope, keyed by STRING
     ANCHORS, never line numbers (PRD lane discipline). The orchestrator applies
     these. Nothing here has been written to the trunk by this lane. Lane
     wh-repair, the single repair wave of the capped L6 loop. -->

# PATCH — `definitions.md`, `notation.md`, the falsifier, and the RED-MATRIX

Five targets. Patch 1 and 2 **supersede the prove lane's**
`theory/lanes/wh-kappa/prove/PATCH.md`, which was written before OBJ-1 and
declares `β` a fixed convention; apply this one instead, or (if that one was
already applied) use the per-definition replacements in Patch 1b.

Patch 5 is not a file edit: it is the list of files this lane produces that
belong under `theory/`.

---

## Patch 1 — `definitions.md`, if it is still empty

**ANCHOR (replace this exact line):**

```
*No definitions yet.*
```

**REPLACEMENT:**

```
## D1 (the symplectic object of a finite field)

For a finite field `κ`, put `V(κ) := κ ⊕ κ` and define `ω : V(κ)×V(κ) → κ` by
`ω((a,b),(a',b')) := a b' − a' b`.
Stipulation only; that `ω` is `κ`-bilinear, satisfies `ω(v,v) = 0` and is
nondegenerate is claim `WH-FORM`. Uniform in the characteristic; `p = 2` is in
scope.

## D2 (admissible polarizing cocycles, and the choice of one)

`Adm(ω) := { β : V(κ)×V(κ) → κ  |  β is κ-bilinear and β − β^T = ω }`.
A *polarizing cocycle* is a choice of element `β ∈ Adm(ω)`, and it is a **datum
of the construction, on the same footing as the character `ψ` of D3** — not a
convention. `β₀((a,b),(a',b')) := a b'` is the *reference* cocycle: a label for
the torsor of D2, not a canonical point of it.
The symmetrized alternative `ω/2` lies in `Adm(ω)` at odd `p` only, and is
unavailable at `p = 2`; that `Adm(ω)` is a torsor of size `q³`, that `ω/2` is
its unique antisymmetric point at odd `p`, and that at `p = 2` it splits into
two isomorphism types are claims `WH-BETA-a`, `-b`, `-c`.

## D3 (the phase datum, and the two choices it hides)

A *phase datum* for `κ` is an additive character `ψ : (κ,+) → C^×` with `ψ ≢ 1`.
Write `X(κ)` for the set of such `ψ`.
The *trace-normalized family*: `Tr_{κ/F_p}(z) := z + z^p + ⋯ + z^{p^{m−1}}` for
`κ = F_{p^m}`, and `ψ_ζ := ζ^{Tr_{κ/F_p}(·)}` for `ζ` a primitive `p`-th root of
unity in `C`.
**Two named choices:** `ψ` itself, and — inside the distinguished family — `ζ`.
Neither is canonical and neither is ever suppressed. `Tr_{κ/F_p}` is canonical.

## D4 (Weyl operators and the observable algebra)

For `ψ` as in D3 and `β ∈ Adm(ω)` as in D2,
`A_{ψ,β}(V) := ⨁_{v ∈ V(κ)} C·W_β(v)` with product fixed on basis elements by
`W_β(v)W_β(v') := ψ(β(v,v')) W_β(v+v')`.
This ordering is fixed once. Depends on `κ`, `ψ` and `β`, and on nothing else.

## D5 (the Heisenberg group of a polarizing cocycle)

`H_β(κ) := κ × V(κ)` with `(t,v)(t',v') := (t + t' + β(v,v'), v + v')`.
It uses no character; it does depend on `β`, and at `p = 2` its isomorphism
class does (claim `WH-BETA-f`). `A_{ψ,β}(V)` is its group algebra with the
centre set to `ψ`.

## D6 (the quadratic form of a polarizing cocycle)

`Q_β : V(κ) → κ`, `Q_β(v) := β(v,v)`; for the reference cocycle,
`Q_{β₀}(a,b) = ab`.
Identically zero under any symmetrized convention, and not zero here; at `p = 2`
it is the object that separates the members of `Adm(ω)`.

## D7 (the Weyl frame and two automorphism groups)

The *Weyl frame* is `F := { C^×·W_β(v) : v ∈ V(κ) } ⊂ A_{ψ,β}(V)`.
`Aut_F(A)` is the group of `C`-algebra automorphisms `α` with `α(F) = F`.
`Aut_F^κ(A) ⊆ Aut_F(A)` is the subgroup whose induced permutation of `V(κ)` is
`κ`-linear. The `κ`-linearity is **imposed data**: the algebra and its frame are
built from `(V,+)` and `ψ∘β` alone and do not carry the `κ`-module structure
(claim `WH-SYMM`).

## D8 (Schrödinger models, and the standard model)

For a `κ`-line `L ⊂ V(κ)` put `A_L := span_C{ W_β(l) : l ∈ L }`. Given a unital
`C`-algebra character `χ : A_L → C`, the *Schrödinger model* of `(L,χ)` is
`M_{L,χ} := A_{ψ,β}(V) ⊗_{A_L} C_χ`.
The *standard model* (for `β = β₀`) is `M₀ := ⨁_{y ∈ κ} C·e_y` with `{e_y}`
declared orthonormal and

    W(a,b) e_y := ψ(−b(y+a)) e_{y+a},   i.e.   W(a,b) = Z(−b)X(a),

where `X(a)e_y := e_{y+a}` and `Z(b)e_y := ψ(by)e_y`. **This is a stipulation.**
The sign is not cosmetic: the naive `Z(b)X(a)` realizes the cocycle `−ab'`, and
the discrepancy is invisible at `p = 2`. That `M₀` satisfies D4 is checked by
gate `C11` of `theory/checks/wh_kappa_check.py` and derived at `WH-SVN`.

## D9 (the model groupoid)

`Mod_{ψ,β}(κ)` is the category whose objects are pairs `(M,π)` with
`π : A_{ψ,β}(V) → End_C(M)` a unital algebra map making `M` a simple module and
every `π(W_β(v))` unitary, and whose morphisms are unitary intertwiners.
`PMod_{ψ,β}(κ)` is the same category with `Hom` replaced by `Hom/U(1)`.

## D10 (Artin–Schreier map, and the type of a polarizing cocycle)

`℘ : κ → κ`, `℘(x) := x² + x`. **[p = 2]** the *type* of `β ∈ Adm(ω)` is
`Arf(Q_β) := Q_β(e)·Q_β(f) ∈ κ/℘(κ)` computed in any symplectic `κ`-basis
`(e,f)` of `V(κ)` (`ω(e,f) = 1`). That this is independent of the basis, that
`κ/℘(κ)` has exactly two elements, and that both types occur are claims
`WH-BETA-e`, `-f`.

## D11 (the level-`μ_p` frame)

`F^{(p)}_{ψ,β} := { ζ^j W_β(v) : j ∈ Z/p, v ∈ V(κ) } ⊂ A_{ψ,β}(V)^×`, the finite
group of Weyl unitaries with phases in `μ_p = ψ(κ)`.
Recorded separately from `F` (D7) because the two behave differently: claim
`WH-BETA-h` says `(A,F)` does not depend on `β` while `F^{(p)}` does, at `p = 2`.
```

## Patch 1b — `definitions.md`, if the prove lane's patch was already applied

Replace, heading and body, each of the following blocks by the corresponding
`D2`, `D5`, `D6`, `D7`, `D8` **from Patch 1**, and append `D10`, `D11` after
`D9`. Anchors are the exact heading lines of the prove lane's patch:

| anchor line | action |
|---|---|
| `## D2 (the polarizing cocycle, non-symmetrized)` | replace the whole `## D2 …` block with Patch 1's `## D2 (admissible polarizing cocycles, and the choice of one)` |
| `## D4 (Weyl operators and the observable algebra)` | replace body: `A_ψ(V)` becomes `A_{ψ,β}(V)`, `W` becomes `W_β`, and the dependence line reads "Depends on `κ`, `ψ` and `β`" |
| `## D5 (the Heisenberg group of κ, choice-free)` | replace with Patch 1's `## D5 (the Heisenberg group of a polarizing cocycle)` — **the words "choice-free" are the defect OBJ-1 names** |
| `## D6 (the characteristic-two quadratic form)` | replace with Patch 1's `## D6 (the quadratic form of a polarizing cocycle)` |
| `## D7 (the Weyl frame and its automorphisms)` | replace with Patch 1's `## D7 (the Weyl frame and two automorphism groups)` |
| `## D8 (Schrödinger models, and the standard model)` | replace the sentence beginning `That `M₀` satisfies` with Patch 1's version (adds the C11 pointer, and marks the model a stipulation) |
| `## D9 (the model groupoid)` | replace `Mod_ψ(κ)`/`PMod_ψ(κ)`/`A_ψ(V)` by `Mod_{ψ,β}(κ)`/`PMod_{ψ,β}(κ)`/`A_{ψ,β}(V)`; then append `D10`, `D11` after this block |

---

## Patch 2 — `notation.md`

**ANCHOR (replace this exact block, header rows included):**

```
| symbol | meaning | first fixed in |
|---|---|---|

*No symbols yet.*
```

**REPLACEMENT:**

```
| symbol | meaning | first fixed in |
|---|---|---|
| `p`, `m`, `q` | prime, degree, `q = p^m` | D1 |
| `κ`, `F_p` | the finite field `F_q`; its prime field | D1 |
| `V(κ)` | `κ ⊕ κ`, the symplectic object | D1 |
| `v = (a,b)` | a vector of `V(κ)` | D1 |
| `ω` | `ω((a,b),(a',b')) = ab' − a'b` | D1 |
| `Adm(ω)` | the admissible polarizing cocycles | D2 |
| `Sym(V)` | the symmetric `κ`-bilinear forms on `V(κ)` | D2 |
| `β`, `β₀` | a chosen polarizing cocycle; the reference one `ab'` | D2 |
| `Q_β` | `Q_β(v) = β(v,v)` | D6 |
| `℘`, `Arf` | `℘(x) = x²+x`; the type `Q_β(e)Q_β(f) ∈ κ/℘(κ)` | D10 |
| `ε` | the sign in `q^{-1}Σ_v W_β(v)² = ε·1` at `p = 2` | D10 |
| `ψ` | a nontrivial additive character of `(κ,+)` | D3 |
| `X(κ)` | the set of nontrivial additive characters | D3 |
| `κ̂`, `V̂` | `Hom((κ,+),C^×)`, `Hom((V,+),C^×)` | D3 |
| `ζ` | a primitive `p`-th root of unity in `C` | D3 |
| `ψ_ζ`, `Tr_{κ/F_p}` | `ζ^{Tr(·)}`; the absolute trace | D3 |
| `μ_p`, `μ_4`, `U(1)` | `p`-th, 4th roots of unity; unit circle | D3 |
| `W_β(v)` | Weyl operator / basis element of `A_{ψ,β}(V)` | D4 |
| `A_{ψ,β}(V)` | the twisted algebra `⨁_v C·W_β(v)` | D4 |
| `H_β(κ)` | the Heisenberg group `κ × V(κ)` of `β` | D5 |
| `F`, `F^{(p)}` | the Weyl frame; the level-`μ_p` frame | D7, D11 |
| `Aut_F(A)`, `Aut_F^κ(A)` | frame-preserving automorphisms; those with `κ`-linear `g` | D7 |
| `L`, `A_L` | a `κ`-line in `V(κ)`; its subalgebra | D8 |
| `χ`, `C_χ` | a character of `A_L`; its 1-dimensional module | D8 |
| `M_{L,χ}`, `M₀` | Schrödinger model of `(L,χ)`; the standard model | D8 |
| `e_y`, `X(a)`, `Z(b)` | standard basis; shift and phase operators | D8 |
| `Mod_{ψ,β}(κ)`, `PMod_{ψ,β}(κ)` | the model groupoid; its projectivization | D9 |
| `P(H_ψ(κ))` | the canonical projective Hilbert space | D9 |
| `P¹(κ)` | the projective line: the `q+1` lines of `V(κ)` | D1 |
| `SL_2(κ)` | `κ`-linear automorphisms of `V(κ)` of determinant 1 | D1 |
| `Sp_{2m}(F_p)` | isometries of the `F_p`-form `ψ∘ω` on `V(κ)` | D7 |
| `O(Q_β)` | `{ g : Q_β ∘ g = Q_β }` | D6 |
| `s_g`, `Q_g` | `s_g(v,v') = β(gv,gv') − β(v,v')`; `Q_g(v) = s_g(v,v)` | D7 |
| `E` | the Weyl average `q^{-2} Σ_u W(u)(·)W(u)^{-1}` | D4 |
| `FF^±` | pairs `(κ,ψ)` and character-compatible embeddings | D3 |
```

---

## Patch 3 — `theory/checks/wh_kappa_check.py`

Nine anchored edits. Each anchor block occurs **exactly once** in the round-1
file — verified mechanically in this lane, `python3` counting occurrences of each
anchor string in `theory/checks/wh_kappa_check.py` (P3.8's block is quoted whole
because its final line alone occurs twice) —
the applied result is `theory/lanes/wh-kappa/repair/wh_kappa_check.py`, which
the orchestrator may also copy over wholesale. Green run: exit 0, 1.8 s, all
six `q`. Every red mode, old and new, exits 1 (table at the end of this patch).

**P3.1 — the gate list in the module docstring.** ANCHOR:

```
  C9  at p=2 the symmetrized cocycle is unavailable: 2 is not invertible and no
      code path may form omega/2
A0 is an arithmetic self-test layer (ring, field, model), NOT one of the nine.
"""
```

REPLACEMENT: the same text with these lines inserted before the `A0` line:

```
  C10 the polarizing cocycle beta is a DATUM, not a convention: over the
      admissible kappa-bilinear beta' = beta + s the Heisenberg groups
      H_beta' = kappa x V fall into exactly ONE isomorphism class at odd p and
      exactly TWO at p = 2, split by the Arf invariant of Q'(v) = beta'(v,v),
      with the pre-registered counts of EXPECTED_BETA
  C11 the standard model of D8, W(a,b) = Z(-b)X(a), realises D4 exactly at every
      q, while the naive Z(b)X(a) fails at odd p and PASSES at p = 2 (E1+E3)
```

**P3.2 — three new modes.** ANCHOR (the last entry of `MODES` and its closing
brace):

```
    "--red-halfweyl":
        "EXTRA, not one of the brief's five: use the symmetrized cocycle omega/2; "
        "C9 must fire at p=2. Added because no mode in the brief reaches C9",
}
```

REPLACEMENT: the same, with `--red-psi-polarization`, `--red-beta-rigid` and
`--red-naive-order` inserted before the `}` — copy them verbatim from the lane's
`wh_kappa_check.py`.

**P3.3 — two flags on `Setting`.** ANCHOR:

```
        self.claimed_span_dim = q * q + 1 if mode == "--red-dim" else q * q
```

REPLACEMENT: that line followed by

```
        self.beta_rigid = (mode == "--red-beta-rigid")
        self.model_order = "naive" if mode == "--red-naive-order" else "d8"
```

**P3.4 — OBJ-5, the dead `ψ`-isotropy branch of `gate_C7`.** ANCHOR (this exact
block, which occurs once):

```
    P, Q = pol
    for name, G in (("P", P), ("Q", Q)):
        if len(set(G)) != q:
            return False, "polarization %s does not have q elements" % name
        for x in G:
            for y in G:
                if int(S.VADD[x, y]) not in set(G):
                    return False, "polarization %s is not a subgroup" % name
                if FORM[x][y] != 0:
                    return False, ("polarization %s is not isotropic: form = %d "
                                   "at (%s,%s)" % (name, FORM[x][y],
                                                   divmod(x, q), divmod(y, q)))
                if TR[FORM[x][y]] != 0:
                    return False, "polarization %s is not psi-isotropic" % name
```

REPLACEMENT: the corresponding block of the lane's file, which (i) closes the
subgroup test in its own loop, (ii) runs the `Tr(form) = 0` test **first and on
its own**, (iii) runs the `form = 0` test after it, with a message naming the
distinction. The old branch was reachable only when `FORM[x][y] == 0`, where
`TR[0] = 0`, i.e. it read `0 != 0`.

**P3.5 — a builder for the new polarization mutation.** ANCHOR:

```
def subspaces_dim(p, m, k):
```

REPLACEMENT: the function `psi_isotropic_polarization(S)` from the lane's file,
followed by that same `def subspaces_dim(p, m, k):` line.

**P3.6 — the two new gates.** ANCHOR:

```
# --------------------------------------------------------------------------
# A0.4  Model self-tests: monomiality, dense cross-check, unitarity
# --------------------------------------------------------------------------
```

REPLACEMENT: `EXPECTED_BETA`, `gate_C10`, `gate_C11` from the lane's file,
followed by that same three-line banner.

**P3.7 — `usage()`.** ANCHOR:

```
    for name in ("green", "--red-symmetric", "--red-trivial-char", "--red-cocycle",
                 "--red-nonisotropic", "--red-dim", "--red-halfweyl"):
```

REPLACEMENT: the same tuple extended by `"--red-psi-polarization",
"--red-beta-rigid", "--red-naive-order"`.

**P3.8 — the driver's polarization mutation.** ANCHOR (this exact block, which
occurs once; note that its last line occurs twice in the file, so the block must
be matched whole):

```
        constructible = True
        if mode == "--red-nonisotropic":
            P, Q, desc = nonisotropic_polarization(S)
            if P is None:
                constructible = False
                P, Q = standard_polarization(S)
                log("q=%-2d MUTATION NOT CONSTRUCTIBLE: %s" % (q, desc))
                notes.append((q, desc))
            else:
                log("q=%-2d mutation: %s" % (q, desc))
        else:
            P, Q = standard_polarization(S)
```

REPLACEMENT: the lane's version, which dispatches to
`nonisotropic_polarization` or `psi_isotropic_polarization` by mode and keeps
the NOT-CONSTRUCTIBLE reporting unchanged.

**P3.9 — the gate list.** ANCHOR:

```
                 ("C7", lambda s, m: gate_C7(s, m, (P, Q))),
                 ("C8", gate_C8), ("C9", gate_C9)]
```

REPLACEMENT:

```
                 ("C7", lambda s, m: gate_C7(s, m, (P, Q))),
                 ("C8", gate_C8), ("C9", gate_C9),
                 ("C10", gate_C10), ("C11", gate_C11)]
```

### Patch 3 — evidence (every mode re-run after the edits; logs in `runs/`)

| mode | exit | gates that fired (`q`) |
|---|---|---|
| green | **0** | — (1.8 s, `q ∈ {2,3,4,5,8,9}`) |
| `--red-symmetric` | 1 | C1,C2,C3,C4,C5,C6,C7 at all `q` |
| `--red-trivial-char` | 1 | C5,C6,C8 at all `q`; **C11 at 3,5,9** |
| `--red-cocycle` | 1 | C3 all `q`, C1 at 3,5,9; **C11 at all `q`** |
| `--red-nonisotropic` | 1 | C3,C4,C7 at 4,8,9 — **C7 now fires on the ψ branch** |
| `--red-dim` | 1 | C5 at all `q` |
| `--red-halfweyl` | 1 | C1,C9 at 2,4,8; C3 all `q`; **C11 at all `q`** |
| `--red-psi-polarization` (new) | 1 | C3,C7 at 4,8,9 — **ψ branch PASSES, κ branch fires** |
| `--red-beta-rigid` (new) | 1 | C10 at all `q` |
| `--red-naive-order` (new) | 1 | **C11 at 3,5,9 only** |

Three consequences worth recording. (i) OBJ-5 is closed in both directions: one
mutation makes the `ψ`-isotropy branch **fail**, another makes it **pass while
its neighbour fails**, so it is a discriminating test and not a constant. (ii)
`C11` makes the transposed-cocycle mutation detectable at `p = 2` as well
(`--red-cocycle` now fires at `q = 2,4,8`), which erratum E3 recorded as a
blind spot of C1. (iii) No two modes have the same firing set.

---

## Patch 4 — `theory/checks/wh_kappa_RED-MATRIX.md`

**ANCHOR (append after this exact final line of the file):**

```
`{2, 3, 5}` — matched the pre-registration exactly.
```

**APPEND:**

```

---

## Round-1 repair addendum (lane `wh-repair`, after `theory/verdicts/wh-kappa-r1.md`)

Three modes and two gates were added, and one sub-check was repaired. **None of
the three modes and neither gate is pre-registered**: they were written after
the verdict, so under `PRD.md` they are regression tests, and a green result on
them promotes nothing. They are recorded here so that no reader mistakes them
for pre-registered evidence.

    python3 -O wh_kappa_check.py --red-psi-polarization   # exit 1
    python3 -O wh_kappa_check.py --red-beta-rigid         # exit 1
    python3 -O wh_kappa_check.py --red-naive-order        # exit 1

| gate \ mode | psi-polarization | beta-rigid | naive-order |
|---|---|---|---|
| C3 Weyl relation | 4,8,9 | - | - |
| C7 polarization + census | **4,8,9 (κ-isotropy branch)** | - | - |
| C10 β-dichotomy (new) | - | **2,3,4,5,8,9** | - |
| C11 D8's standard model (new) | - | - | **3,5,9** |
| exit code | 1 | 1 | 1 |

**The `C7` repair (verdict OBJ-5).** The `Tr(FORM) != 0` sub-check sat inside
the `FORM != 0` branch, where `FORM` is 0 and `TR[0] = 0`: it read `0 != 0` and
could not fail. It now runs first and on its own. It is reached in both
directions: `--red-nonisotropic` (a polarization with `Tr(ω) ≠ 0`) makes it
**fire**, and `--red-psi-polarization` (a polarization that is ψ-isotropic but
not κ-isotropic — these exist only for `q` non-prime, 15 against 5 order-`q`
subgroups at `q = 4`) makes it **pass** while the κ-isotropy branch fires. The
row "Sub-checks that no mutation reaches" no longer needs an entry for it.

**A side finding of `--red-psi-polarization`, recorded rather than acted on.**
C3 fires under it, so a ψ-isotropic-but-not-κ-isotropic summand does **not**
give a model satisfying D4: ψ-isotropy is necessary but not sufficient. The
brief's E2 discussion left this open; the answer is now on the record.

**Two additions to the decoration inventory, and one removal.** Removed: the
C7 ψ-isotropy branch (now reached, above). Added, both from the new gates:
`C10`'s odd-`p` branch is reached only by `--red-beta-rigid`, which reaches it
by shrinking the enumerated torsor rather than by mutating an object; and
`C11`'s "at `p = 2` the two orderings must agree" clause is not reached by any
mutation (a mutation making the two orderings differ at `p = 2` would have to
break `−1 = 1`).
```

---

## Patch 5 — files to promote out of this lane

| lane file | destination | note |
|---|---|---|
| `wh-kappa.md` | `theory/wh-kappa.md` | §0–§5 + the shared ledger; 420 lines |
| `wh-kappa-choice.md` | `theory/wh-kappa-choice.md` | §6–§11; 503 lines. **The split is required by L2** (200–500 lines/shard): the repaired argument is 923 lines and does not fit in one file. The pair is cited as one shard throughout |
| `CLAIMS-ROWS.md` | rows into `claims/CLAIMS.md` | after adjudication; `proved in` cells already name the two destinations above, per OBJ-6 |
| `beta_census.py`, `frame_mu.py`, `fp_symmetry.py`, `funct_sections.py`, `split24.py`, `ff.py` | `theory/checks/` or `numerics/` | orchestrator's call; each is standalone `python3` (no numpy), green exit 0, every red mode exit 1, logs in `runs/` |

## Not patched, and why

- `briefs/wh-kappa-target.md` — its `WH-CHOICE` row ("exactly one datum") is
  refuted by `WH-BETA`; the brief has already been executed against and the
  correction lives in the shard, in `CLAIMS-ROWS.md` and in the errata pattern
  the orchestrator already uses. A sixth erratum, if wanted, is one line: *the
  polarizing cocycle of convention 2 is a datum, not a convention.*
- `theory/checks/wh_kappa_EXPECTATIONS.md` — this lane deliberately does not
  edit the check lane's pre-registration record. The honest statement about
  `C10`/`C11` not being pre-registered is in Patch 4 instead, in the file that
  documents reachability.
- `refs/LEDGER.md` — no new source was fetched; `N1`, `N2`, `N3` are all
  honoured (N2 is now the epigraph of `WH-BETA`).
