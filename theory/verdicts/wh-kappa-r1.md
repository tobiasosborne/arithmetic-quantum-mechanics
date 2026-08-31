<!-- ROLE: hostile critic verdict (L6, briefs/critic-protocol.md) on the
     wh-kappa prove lane. Round 1. Kept pass or fail. -->

# Verdict `wh-kappa-r1` — the Weyl–Heisenberg system of `Spec κ`

**Header (mandatory disclosures).**

- **Same-family prover/critic.** Prover and critic are the same model family.
  This is a known weakness of this campaign and is compensated mechanically,
  not by good intentions.
- **Blind lane.** I did not see the prover's reasoning and did not ask for it.
  I read `briefs/critic-protocol.md`, `CLAUDE.md`, `PRD.md`,
  `briefs/wh-kappa-target.md` (incl. errata E1–E5), `refs/LEDGER.md` (incl.
  N1–N3), `definitions.md`, `notation.md`, `claims/CLAIMS.md`, the five target
  artifacts, and the registered sources on disk under `refs/`.
  `theory/lanes/wh-kappa/prove/SUMMARY.md` was read as self-assessment, not as
  evidence.
- **Everything below was recomputed.** My scripts share no code with
  `theory/checks/wh_kappa_check.py` or with the lane's `model-ordering.py`:
  different field construction (brute-forced irreducible + full axiom check),
  phases as **exponents in `Z/2p`** (so `μ_4` is representable and nothing is
  a root-of-unity library call), ranks and commutants by specialising
  `ζ_p ↦` an element of exact order `p` in `F_ℓ` (`ℓ = 5,7,11`), which bounds
  rank from below and nullity from above — the sound direction. No floats, no
  tolerances anywhere. Scratch: `theory/lanes/wh-kappa/critic/` (gitignored).
- **Prior verdicts on this target:** none. This is round 1.

---

## What I ran, and how it exited

Pre-registered falsifier, all seven modes (`python3 -O`):

| mode | exit | gates that fired (exit *path*, not just code) |
|---|---|---|
| green | **0** | — every gate passed, `q ∈ {2,3,4,5,8,9}` |
| `--red-symmetric` | 1 | C1,C2,C3,C4,C5,C6,C7 at all `q`; **first = C1 at q=2** |
| `--red-trivial-char` | 1 | C5,C6,C8 at all `q`; **first = C5** |
| `--red-cocycle` | 1 | C3 at all `q`, C1 **only at q=3,5,9**; **first = C3 at q=2** |
| `--red-nonisotropic` | 1 | C3,C4,C7 at `q=4,8,9`; NOT CONSTRUCTIBLE at `q=2,3,5`; **first = C3 at q=4** |
| `--red-dim` | 1 | C5 only; **first = C5** |
| `--red-halfweyl` | 1 | C1,C9 at `q=2,4,8`, C3 at all `q`; **first = C1 at q=2** |

Lane computation `model-ordering.py`: green exit 0 (0 mismatches at all six
`q`); `--red-naive` exit 2, firing only at `q ∈ {3,5,9}`. Reproduced.

My own mutations, on **copies** in `theory/lanes/wh-kappa/critic/mut/`:

| mutation | kind | exit | killed by |
|---|---|---|---|
| M1 `EXPECTED_CENSUS[4] = (35,5,16)` | **data / ground truth** | 1 | C7 at `q=4` only — the census *is* binding |
| M2 `ω → a b'` (degenerate) | object | 1 | C1, then **C2b** (the sub-check RED-MATRIX calls unreachable) |
| M3 `ω → a b'^p − a' b^p` (`F_p`-bilinear only) | object | 1 | C1, **C2c**, C3, C7 |
| M4 model phase sign flip (E1 defect, in the checker's own model) | object | 1 | C3,C4 at `q=3,5,9` **only** — invisible at `p=2` |
| M5 perturb one exponent of one `W(v)` | **data, single entry** | 1 | C3,C4,C5 — the gates are real computations, not fits |
| M6 invert C7's `TR[FORM[x][y]] != 0` | probe | 1 | fires at every `q` ⇒ the original test is **constant-false** (see OBJ-5) |

Ground truth checked independently of the checker's enumerator, by closed
formula: order-`q` subgroups `= [2m,m]_p` (Gaussian binomial) `= 3,4,35,6,1395,130`;
`ω`-isotropic `= q+1`; `ψ∘ω`-isotropic `= ∏_{i=1..m}(p^i+1) = 3,4,15,6,135,40`.
**All six `EXPECTED_CENSUS` triples are correct.**

---

## Objections

### OBJ-1 — FATAL — the characteristic-2 headline is a property of `D2`'s cocycle, not of `(κ, ψ)`; three separate "no choice here" assertions are refuted by computation

**(a) Location.**
`theory/lanes/wh-kappa/prove/wh-kappa.md` §0 line "`D5` `H(κ)`, the **choice-free**
Heisenberg group"; §2 `<1>6.<2>3` ("`H(κ)` uses no character … the **group**
carries no choice"); `N-CHAR2` ("So `D2` is **forced** by `p = 2`");
§4 `<1>5.<2>3` and §4 `<1>6`; §7 `<1>5`, §7 `<1>6` ("**`μ_4` is forced**").
`CLAIMS-ROWS.md` rows `WH-CHOICE` ("Beyond `κ` the construction depends on
**exactly one** datum, `ψ ∈ X(κ)`"), `WH-WEIL-c`, `WH-WEIL-d` ("`μ_4` is
**forced, not chosen**"), `WH-POL-2`. `PATCH.md` D5/D6.

**(b) My computation.** The brief and `D2` state exactly one requirement on the
polarizing cocycle: `β` bi-additive with `β − β^T = ω`. The admissible `β` are a
torsor under the symmetric `κ`-bilinear forms — `q³` of them, all with
`β' − β'^T = ω` (I asserted this in code for every one). I enumerated, for each,
the subgroup of `SL_2(κ)` over which *some* frame automorphism has `μ_2`-valued
phases (exhaustive search over `λ`, no theory used):

| `q` | admissible `β'` | order of the `μ_2`-phase subgroup | multiplicity |
|---|---|---|---|
| 2 | 8 | **2** = `2(q−1)` | 6 |
| 2 | 8 | **6** = `2(q+1)` = `|SL_2(F_2)|` | 2 |
| 4 | 64 | **6** = `2(q−1)` | 40 |
| 4 | 64 | **10** = `2(q+1)` | 24 |

So with `β'(v,v') = ab' + a² + b²` at `q = 2` — admissible on every criterion the
brief states — **every** frame automorphism has `μ_2` phases, the subgroup is not
proper, and **no phase of order 4 is forced anywhere**. `Q'` there is
anisotropic; the two orbits are exactly the two types of quadratic form
polarizing `ω`, with orthogonal groups of order `2(q−1)` and `2(q+1)`.

Worse for "choice-free": the group `D5` builds from `β` is not even
well-defined up to isomorphism at `p = 2`. Element-order profiles of
`H_β(κ) = κ × V`:

| `q` | profile | which `β'` | |
|---|---|---|---|
| 2 | `{1:1, 2:5, 4:2}` | 6 of 8 (incl. `D2`) | dihedral `D_4` |
| 2 | `{1:1, 2:1, 4:6}` | 2 of 8 | **quaternion `Q_8`** |
| 4 | `{1:1, 2:27, 4:36}` | 40 of 64 (incl. `D2`) | |
| 4 | `{1:1, 2:3, 4:60}` | 24 of 64 | |
| 3 | one profile only, `{1:1, 3:26}` | all 27 | |
| 5 | one profile only, `{1:1, 5:124}` | all 125 | |

At odd `p` the choice is invisible; at `p = 2` it is the split/non-split
dichotomy. Cross-check: `|Out(D_4)| = 2` and `|Out(Q_8)| = |S_3| = 6`, exactly
the two `μ_2`-phase subgroup orders in the table above.

The registered source says the same thing and the shard quotes past it:
`refs/arxiv-0808.1664/WeilCharTwo12-8-08.tex:106-110` reads "`Q(v) = β(v,v)`
**for some** non-symmetric bilinear form `β`" — "for some", not "the".

Note what is **not** damaged: Thms 2, 3, 4(a)–(d), 5(b)–(e), 6(a)–(e) use only
`β − β^T = ω` and bi-additivity, so they hold verbatim for every admissible `β`.
The damage is confined to everything downstream of `D6`.

**(c) FIX DEMAND.** Name `β` as a **second datum** everywhere `ψ` is named:
delete "choice-free", "forced", "forced, not chosen"; reword `WH-CHOICE` to
"beyond `κ` and the stipulated `(D1,D2,D4)`, exactly one datum `ψ`"; and restate
`WH-WEIL-c/-d`, `WH-POL-2` and §4 `<1>6` as statements about the quadratic form
`Q = β(·,·)` with its type recorded, e.g. "`|O(Q) ∩ SL_2(κ)| = 2(q−1)` for `Q`
of hyperbolic type — the type of `D2`'s `Q(a,b) = ab` — and `2(q+1)` for the
anisotropic type, both realised by admissible cocycles".

**(d) SURVIVING WEAKER STATEMENT.** For the stipulated `D2` cocycle, every
char-2 claim in the shard is **true and I verified it numerically** (see
VERIFIED CORRECT). The invariant statement is: *at `p = 2` the frame
automorphisms with `μ_p` phases are exactly the isometries of the quadratic
form `ψ∘Q_β`; that subgroup is proper in `SL_2(κ)` for every admissible `β`
except at `q = 2` with anisotropic `Q`, where it is everything; its order is
`2(q−1)` or `2(q+1)` according to the type of `Q_β`, and both types occur.*
The `μ_4` phenomenon is real for `D2` and is **not** a characteristic-2
invariant of `(V, ω, ψ)`.

---

### OBJ-2 — MAJOR — `WH-FUNCT-b`'s "sections exist" is false in the category the shard itself defines

**(a) Location.** `wh-kappa.md` §8 `<1>3` ("a compatible system along the
cofinal tower `F_{p^{n!}}` exists by induction"); `CLAIMS-ROWS.md` row
`WH-FUNCT-b`, clause "**sections of `FF^± → {finite fields}` exist**", status
PROVED; `OPEN-3`.

**(b) My computation.** §8 `<1>2` defines the morphisms of `FF^±` as "the field
embeddings `ι` with `ψ'∘ι = ψ`". Frobenius `x ↦ x^p` **is** a field embedding
`κ → κ`, hence a morphism of the base. A section must therefore make every
`ψ_κ` Frobenius-invariant. Enumerating all additive characters:

| `κ` | Frobenius-invariant characters | of those, nontrivial on the prime field |
|---|---|---|
| `F_4` | `ψ_0` (trivial), `ψ_1 = ζ^{Tr}` | **none** |
| `F_8` | `ψ_0`, `ψ_1` | `ψ_1` |
| `F_9` | `ψ_0`, `ψ_1`, `ψ_2` | `ψ_1, ψ_2` |

At `κ = F_4` the only Frobenius-invariant nontrivial character is `ζ^{Tr}`, and
`Tr_{F_4/F_2}(1) = 0`, so it restricts **trivially** to `F_2`. A section would
then have `ψ_{F_2} = ψ_{F_4}|_{F_2}` trivial, contradicting `ψ_{F_2} ∈ X(F_2)`.
**No section exists — already on the two objects `F_2, F_4`, at `p = 2`.**
(General obstruction, same computation: Frobenius-invariance forces
`ψ_κ = ψ_{ζ^c}` with `c ∈ F_p^×`, and `Tr_{F_{p^p}/F_p} ≡ 0` on `F_p`.)

Separately, the shard's own route does not prove the row either: a compatible
system *along the tower* `F_{p^{n!}}` does not give `ψ_κ` for `κ` off the tower,
since a nontrivial character of `F_{p^{n!}}` may restrict trivially to `F_{p^n}`.

The positive half is cleaner than the shard's and I verified it: over the
**inclusion poset of subfields of a fixed `\bar F_p`** a section exists, and the
characters that work are exactly those nontrivial on the prime field. In `F_16`:
8 of the 15 nontrivial characters are nontrivial on *every* subfield, and they
are exactly the 8 with `Tr(c) ≠ 0`, i.e. nontrivial on `F_2`.

**(c) FIX DEMAND.** Replace the clause by the dichotomy: "no section exists over
`{finite fields}` with all embeddings (Frobenius obstruction, first instance
`F_2 ⊂ F_4`); over the inclusion poset in a fixed `\bar F_p` the sections are
exactly the characters `Ψ` of `(\bar F_p,+)` with `Ψ|_{F_p} ≠ 1`", and close
`OPEN-3` with it.

**(d) SURVIVING WEAKER STATEMENT.** The functor itself is intact — I verified
`W(v) ↦ W'(V(ι)v)` is a unital injective algebra map for `ι : (F_2,ψ) → (F_4,ψ_c)`,
`c ∈ {2,3}`, 0 structure-constant mismatches — and it composes and preserves
identities because it is defined on basis elements by a functor `V(−)` of
additive groups. What dies is only "sections exist"; what replaces it is
**stronger and negative-with-a-strategy**: no choice of characters whatever makes
the assignment compatible with all field embeddings, so the failure is not
special to the trace family, and the surviving forward attack is the
inclusion-poset (equivalently: a character of `(\bar F_p,+)` nontrivial on `F_p`).

---

### OBJ-3 — MAJOR — `D7`'s imposed `κ`-linearity discards most of the symmetry group, and the discarded part is invisible to the algebra

**(a) Location.** `PATCH.md` D7 ("whose induced permutation of `V(κ)` is
**`κ`-linear** … part of the definition, not a lemma"); `wh-kappa.md` §7
`<1>2.<2>1`; §1 `<1>6` (`OPEN-2`); rows `WH-WEIL-a`, `WH-FORM`.

**(b) My computation.** `A_ψ(V)` and its frame `F_ψ` are built from the abelian
group `(V,+)` and the cocycle `ψ∘β` alone: **the `κ`-module structure on `V` is
not visible to the object.** The frame-preserving automorphisms with merely
additive (`F_p`-linear) `g` are exactly `{g : ψ∘ω∘g = ψ∘ω}`, and every such `g`
lifts (`L-TRIV` applies verbatim; I checked the fibre is nonempty of size `q²`
for non-`κ`-linear samples). Exhaustive counts:

| `q` | `{g` `F_p`-lin `: ω∘g = ω}` | `|SL_2(F_q)|` | `{g : ψ∘ω∘g = ψ∘ω}` | `|Sp_{2m}(F_p)|` |
|---|---|---|---|---|
| 2 | 6 | 6 | 6 | 6 |
| 3 | 24 | 24 | 24 | 24 |
| 4 | 60 | 60 | **720** | 720 |
| 8 | 504 | 504 | **1451520** | 1451520 |
| 9 | 720 | 720 | **51840** | 51840 |

So `|Aut_frame|` without `D7`'s clause is `11520` at `q = 4` (12× the shard's
960) and `4199040` at `q = 9` (72×). Two consequences:

1. `OPEN-2` **as posed** ("which `F_p`-linear maps preserve the `κ`-valued `ω`?")
   has answer **`SL_2(κ)`, nothing more** — computed above for `q ≤ 9`, and for
   all `q` by this argument, which I checked in both characteristics: such a `g`
   is injective (if `gv = 0` then `ω(v,u) = ω(gv,gu) = 0` for all `u`), hence
   bijective; take a basis `v_1,v_2`, then for every `c, u`
   `ω(gv_i, g(cu) − c·g(u)) = ω(v_i, cu) − c·ω(v_i, u) = 0` by `κ`-bilinearity,
   and `gv_1, gv_2` span, so `g(cu) = c·g(u)` by nondegeneracy: `g` is
   `κ`-linear, and then `det g = 1` by Thm 1 `<1>5`. *Warning for the repair
   lane, since I made this mistake first:* the tempting route via "the
   `ω`-self-adjoint endomorphisms are the `κ`-scalars" is **false at `p = 2`** —
   there are `8` of them at `q = 2` (the trace-zero maps) against `2` scalars,
   and `64` against `4` at `q = 4`; it is exactly an odd-characteristic reflex.
   The hedge in §1 `<1>6` is therefore unnecessary — but it hedges the *wrong*
   question: the one that bites is `ψ∘ω`, not `ω`.
2. The `p = 2` orthogonal phenomenon **survives** in the larger group, which is
   good news the shard did not claim: at `q = 4` the `g` admitting a `μ_2`-valued
   `λ` number exactly **72 = |O⁺_4(F_2)|**, index 10 in `Sp_4(F_2)` — the same
   index as `2(q−1) = 6` inside `SL_2(F_4)`. I verified "μ_2-phase ⟺ preserves
   `ψ∘Q`" independently in that setting (72 = 72 at `q=4`, 2 = 2 at `q=2`).

**(c) FIX DEMAND.** Add to `D7` and to `WH-WEIL-a` the sentence "the
`κ`-linearity requirement is a datum the algebra does not carry; without it the
frame group is the extension of `Sp_{2m}(F_p)` by `V̂`, of order `p^{2m}|Sp_{2m}(F_p)|`",
and restate `OPEN-2` as the `ψ∘ω` question (now answered) rather than the `ω` one.

**(d) SURVIVING WEAKER STATEMENT.** `1 → V̂ → Aut_F(A_ψ) → SL_2(κ) → 1` is exact
at every characteristic **for `D7`'s `κ`-linear group** — I verified
`|Aut_F| = q²|SL_2(κ)|` with every fibre of size exactly `q²` at `q = 2,3,4`
(24, 216, 960), and surjectivity onto `SL_2` in each case. For `m = 1` — the
prime field, i.e. the campaign's declared guiding path — the two groups coincide
and nothing is lost.

---

### OBJ-4 — MINOR — §7 `<1>7.<2>1` states a false homomorphism, and skips the step that makes the true one work

**(a) Location.** `wh-kappa.md` §7 `<1>7.<2>1`: "giving an injective homomorphism
`Aut(A_ψ) → PU(M)`".

**(b) My computation.** `Aut(A_ψ) ≅ PGL_q(C)` and does not map to `PU(M)` by
`Ad`. Counterexample at `q = 2`: `T = diag(2,1)`, `π(W(1,0)) = [[0,1],[1,0]]`,
`T π(W) T^{-1} = [[0,2],[1/2,0]]`, whose singular values are `2` and `1/2`, so it
is not a scalar times a unitary. What is true is the statement two lines later
("a projective unitary representation of `Aut_F(A_ψ)`"), and it needs
`|λ(v)| = 1`, which the shard never states: taking absolute values in `(∗)` makes
`v ↦ |λ(v)|` a homomorphism from a finite group to `R_{>0}`, hence trivial.

**(c) FIX DEMAND.** Replace `Aut(A_ψ)` by `Aut_F(A_ψ)` in `<2>1` and insert the
one-line `|λ| = 1` argument before invoking Thm 5 `<1>5`.

**(d) SURVIVING WEAKER STATEMENT.** `Aut_F(A_ψ) → PU(M)` is an injective
homomorphism at every characteristic; `WH-WEIL-b`'s conclusion is unaffected.

---

### OBJ-5 — MINOR — one falsifier sub-check is a literal no-op, and it is not in the checker's own decoration inventory

**(a) Location.** `theory/checks/wh_kappa_check.py`, `gate_C7`, the
`if TR[FORM[x][y]] != 0: return False, "… not psi-isotropic"` branch (immediately
after the `FORM[x][y] != 0` guard); `theory/checks/wh_kappa_RED-MATRIX.md`,
"Sub-checks that no mutation reaches", which omits it.

**(b) My computation.** The branch is reached only when `FORM[x][y] == 0`, and
`TR[0] = 0` always, so the test simplifies to `0 != 0`. Mechanically confirmed:
inverting it to `== 0` (M6) makes it fire at **every** `q` — the branch is
executed, always with the constant value 0. It can never fail, under any
mutation of the polarization. This matters slightly more than usual because
`EXPECTATIONS.md` D-i makes the `ω`-isotropy / `Tr∘ω`-isotropy distinction a
named design point, and this is the one place the polarization check would have
tested it.

**(c) FIX DEMAND.** Reorder so the `Tr` test runs on its own (`for` the fed `P,Q`
check `Tr(form) = 0` **before or independently of** `form = 0`), or delete it and
add it to the RED-MATRIX decoration table.

**(d) SURVIVING WEAKER STATEMENT.** Everything else in C7 is real: the
`q+1` line count fires under `--red-symmetric` and `--red-nonisotropic`, and the
census is genuinely binding — my data mutation `(35,5,15) → (35,5,16)` is caught
by C7 at `q = 4` and nowhere else. All nine gates remain reachable.

---

### OBJ-6 — MINOR — lockstep: the rows are not yet true statements about files, and the pre-registered checker does not test the clause `WH-SVN` puts in its own row

**(a) Location.** `CLAIMS-ROWS.md` — every row's `proved in` cell says
`theory/wh-kappa.md`, which **does not exist** (the shard is at
`theory/lanes/wh-kappa/prove/wh-kappa.md`); every `tested in` cell holds gate ids
(`C1, C2`), not file paths, while `claims/CLAIMS.md`'s own header says "Every
row's `proved in` and `tested in` cells point at a real file. … a fabricated one
is a FATAL defect". Row `WH-SVN` ends "The standard model is `W(a,b) = Z(−b)X(a)`"
and lists `tested in: C3, C6`.

**(b) My computation.** `wh_kappa_check.py`'s `Model` builds
`W(u+w)e_y = ψ(ω(u,y))e_{y+w}`, i.e. `W(a,b)e_y = ψ(ay)e_{y+b}` — a *different*
model from `D8`'s `W(a,b)e_y = ψ(−b(y+a))e_{y+a}` (both satisfy `D4`; I checked
both). So C3 tests that *a* model realises `D4`; it does not test `D8`. The only
evidence for the `Z(−b)X(a)` clause is the lane's own `model-ordering.py`, which
under the PRD is the prover's computation, not independent evidence. I therefore
rebuilt `D8` myself, exactly: **0 violations of `D4` at `q = 2,3,4,5,8,9`** for
`Z(−b)X(a)`, and `36, 400, 3888` violations for the naive `Z(b)X(a)` at
`q = 3,5,9` with **0 at `q = 2,4,8`** — E3's asymmetry reproduced from scratch.
`SUMMARY.md` carries the conditionality once ("15 PROVED-pending-critic") and
then announces "Proved: WH-FORM … WH-FUNCT-a/b" in the next line; the strength
drifts up between the two sentences, and it is the second one a reader quotes.

**(c) FIX DEMAND.** Orchestrator: move the shard to `theory/wh-kappa.md` before
the rows land, put file paths in `tested in` (`theory/checks/wh_kappa_check.py`
with the gate ids in parentheses), and either add a gate that runs `D8`'s model
or move the `Z(−b)X(a)` clause into `D8`'s definition text where it is a
stipulation rather than a tested claim.

**(d) SURVIVING WEAKER STATEMENT.** `D8` is correct — the formula satisfies `D4`
exactly at all six `q`, and the induced-module derivation in §5 `<1>1` is right
step for step; it is the *provenance* of that clause, not its truth, that the
row misstates.

---

### OBJ-7 — MINOR — `WH-FUNCT-a`'s row asserts more than §8 `<1>1` proves

**(a) Location.** `CLAIMS-ROWS.md` row `WH-FUNCT-a`, "**The obvious functor on
finite fields does not exist**"; `wh-kappa.md` §8 `<1>1.<2>3`.

**(b) My computation.** What is proved (and I reproduced: `Tr_{F_4/F_2} ≡ 0` on
`F_2`; `Tr_{F_16/F_2} ≡ 0` on `F_4`; `Tr_{F_27/F_3} ≡ 0` on `F_3`; nonzero for
`F_2 ⊂ F_8` and `F_3 ⊂ F_9`, where `p ∤ n`) is that **the trace-normalised
family** is not restriction-compatible. "The obvious functor does not exist"
quantifies over candidates the proof never touches.

**(c) FIX DEMAND.** Scope the row to the trace-normalised family, and cite OBJ-2
for the statement that quantifies over *all* families.

**(d) SURVIVING WEAKER STATEMENT.** As written, with "the trace-normalised
family" substituted for "the obvious functor", the row is PROVED and I verified
every instance.

---

### OBJ-8 — NOTE — Lamport hygiene, and "zero admitted steps" needs one footnote

`wh-kappa.md` §5 `<1>3.<2>3` is justified by `<1>4`, which appears **after** it
(not circular — `<1>4` uses only `<1>3.<2>2` and `<2>4` — but it reads as a
leaf pointing forward, and L6b asks for the order to be the dependency order).
`L-DUAL` is stated for `κ̂` and then applied to `V̂` (§7 `<1>2.<2>3`) and to
arbitrary, possibly trivial, characters (its own `<1>1` leans on `L-VAL`, whose
index-`p` clause presupposes nontriviality); both uses are sound, neither is the
stated lemma. Finally, `L-TRIV` `<1>3` and §5 `<1>3.<2>4` both use that `C` is
algebraically closed (`p`-th roots; an eigenvalue exists). That is the one input
not derived from `D1`–`D9`; "`[ADMITTED]` steps: none" is defensible only if the
ledger names it as an ambient property of `C` rather than a quoted theorem.
**FIX DEMAND:** reorder §5 `<1>3`/`<1>4`, restate `L-DUAL` for a general finite
`F_p`-space, and add the one-line footnote to §9.
**SURVIVING:** all three steps are correct as mathematics.

### OBJ-9 — NOTE — "there are `q(q+1)` Schrödinger models" counts labels, not objects

§4 `<1>6` and row `WH-POL`. I enumerated: `q+1` lines and exactly `q` characters
per line at `q = 2,3,4,5,8,9` (models `6,12,20,30,72,90` `= q(q+1)` ✓), and
exactly 2 lines with `Q|_L = 0` in every case, with **every** character of each of
the other `q−1` lines taking a value of order 4 at `p = 2` (`q−1 = 1,3,7` ✓).
So the sharpening is arithmetically right. But by the shard's own `WH-CANON` all
`q(q+1)` are isomorphic in `Mod_ψ(κ)`; the count is of *pairs* `(L,χ)`.
**FIX DEMAND:** write "`q(q+1)` pairs `(L,χ)`, all isomorphic as `A_ψ`-modules".
**SURVIVING:** the count and the `p = 2` order-4 statement, both verified.

---

## VERIFIED CORRECT

```
Recomputed by an independent route and CONFIRMED. The repair wave should not
churn any of this.

WH-FORM   omega bilinear/alternating/nondegenerate, beta - beta^T = omega:
          re-derived; and the kappa-linear isometry group is SL_2(kappa),
          |SL_2| = 6, 24, 60, 120, 504, 720 for q = 2,3,4,5,8,9.
          BONUS: the F_p-linear isometry group of the kappa-valued omega is
          ALSO exactly SL_2(kappa) -- enumerated at q = 2,3,4,8,9 (0 of them
          fail to be kappa-linear) and proved for all q in OBJ-3, closing
          OPEN-2.

WH-COMM   the Weyl and commutation relations: exhaustive at all six q, both in
          the checker's model and in my own rebuild of D8. Uniform in p.

WH-ALG /  A_psi simple, centre C, dim q^2:  the Weyl-average proof is correct
WH-ALG-MAT and uses NO Wedderburn, NO Maschke, NO Burnside, NO Skolem-Noether,
          NO Jacobson density -- I checked every leaf. The two facts a critic
          most expects to be smuggled are genuinely derived:
            * "every automorphism is inner" comes from module uniqueness
              (Sec.5 <1>3.<2>3 -> <1>4), not from Skolem-Noether;
            * "the simple module is unique" comes from A = M^{+q} as a left
              module plus Schur, not from Wedderburn.
          No circularity: Thm 3 <- Thm 2 <- Thm 1 + L-ORTH/L-VAL; Thm 5 <- Thm 3
          + Thm 4; Thm 4 <- L-TRIV. L-TRIV itself is correct (I re-derived
          (1,u)^p = (gamma(u), pu) and the splitting).
          Numerically on MY rebuild of D8: span of the q^2 Weyl operators has
          dimension exactly q^2 and the commutant has dimension exactly 1, at
          q = 2,3,4,5,8,9 (mod ell = 5,7,11; the bound direction is sound).

WH-SVN    dimension q; uniqueness up to unitary equivalence; intertwiner unique
          up to U(1). The induced-module derivation of W(a,b) = Z(-b)X(a) is
          correct step by step, including the sign paid in <2>2, and my
          independent rebuild finds 0 violations of D4 at all six q while the
          naive Z(b)X(a) fails at q = 3,5,9 and PASSES at q = 2,4,8.

WH-POL    q+1 lines; exactly q characters per line; q(q+1) pairs; exactly two
          lines with Q|_L = 0; at p = 2 every character of each of the other
          q-1 lines has a value of exact order 4.  All enumerated.

WH-CHOICE |X(kappa)| = q-1, free transitive kappa^x action, single point at
          q = 2; distinct psi give distinct central characters. Verified.
          The coherent systems h_u = diag(u^-j, u^(j-1)) do satisfy
          beta(h_u v, h_u v') = u^-1 beta(v,v') and h_u h_u' = h_{uu'}.

WH-WEIL-a EXACT at q = 2, 3, 4 by exhaustive enumeration of pairs (g, lambda):
          |Aut_F| = 24, 216, 960 = q^2|SL_2|; the map to SL_2 is ONTO with
          every fibre of size exactly q^2; the kernel is V^ and consists of the
          Ad_{W(u)}. Surjectivity at p = 2 as well as odd p.

WH-WEIL-b the odd-p splitting alpha_g(W(v)) = psi(Q_g(v)/2) W(gv) satisfies (*)
          and alpha_g alpha_h = alpha_gh; s_gh(v,v') = s_h(v,v') + s_g(hv,hv')
          re-derived; s_g = rt aa' + st(ab' + a'b) + su bb' re-derived.

WH-WEIL-c/d  FOR D2's COCYCLE (see OBJ-1 for the scope): O(Q) cap SL_2(kappa)
          has order exactly 2(q-1) = 2, 6, 14 at q = 2, 4, 8 -- direct
          enumeration over all of SL_2, not via the rt/su formula -- consists
          exactly of diag(r, r^-1) and antidiag(s, s^-1), and is proper.
          Stronger than claimed: at p = 2, O(Q) computed inside GL_2 is already
          inside SL_2 (orders 2, 6, 14 = the same), so the intersection is
          redundant. At odd p the same set has order q-1, not 2(q-1) -- the
          shard correctly does NOT claim it there.
          "mu_2 phases <=> orthogonal" also verified in the F_p-linear setting:
          72 = |O^+_4(F_2)| of the 720 at q = 4, index 10 in both settings.

FALSIFIER The pre-registered ground truth EXPECTED_CENSUS is CORRECT: all six
          triples reproduce [2m,m]_p, q+1, prod(p^i+1). All nine gates are
          reachable; no gate is fitted (a single-entry perturbation of one Weyl
          operator is caught by C3, C4 and C5); the census is caught only by C7.
          The E3 blindness of C1 at p = 2 is real and is correctly documented.
```

---

## Open questions the critic closed (hand these to the repair wave)

- **OPEN-1** (does `1 → V̂ → Aut_F(A_ψ) → SL_2(κ) → 1` split at `p = 2`?) — **it
  splits at `q = 2` and at `q = 4`.** At `q = 2` I enumerated the group of order
  24 (element orders `{1:1, 2:9, 3:8, 4:6}`, i.e. `S_4`) and found **4 distinct
  complements** of order 6 meeting `V̂` trivially. At `q = 4` I lifted the
  presentation `A_5 = ⟨x,y | x² = y³ = (xy)⁵ = 1⟩`: of the `16×16` lifts of a
  generating pair, **64** satisfy all three relations and generate a subgroup of
  order 60 meeting `V̂` trivially. Both are complete finite checks, not samples.
  The generators of a complement necessarily use phases of order 4 — the
  splitting exists **and** needs `μ_4`, exactly as §7 `<1>6` predicts. So row
  `WH-WEIL-e` (CONJECTURE) is **settled affirmatively at `q = 2, 4`**; the
  general `p = 2` case stays open. Attack (i) of the shard's own OPEN-1 list is
  discharged; attacks (ii)/(iii) are now about the general case only.
- **OPEN-2** — answered: `SL_2(κ)`, for the `κ`-valued `ω` (OBJ-3). The
  question that actually bites is the `ψ∘ω` one, whose answer is `Sp_{2m}(F_p)`.
- **OPEN-3** — answered negatively for the full category, positively and
  explicitly for the inclusion poset (OBJ-2).
- **New open question this round raises:** which admissible `β` should the
  campaign stipulate? `D2`'s `Q(a,b) = ab` is the hyperbolic type. The
  anisotropic type gives `Q_8`-type Heisenberg groups and `2(q+1)`. There may be
  a reason to prefer hyperbolic (it is the one with two `Q|_L = 0` lines, hence
  the one that admits `D8`'s standard model at all) — that reason should be
  written down, because it is the first genuinely canonical-looking argument for
  `D2` in the shard.

---

## Status register check

Is the artifact claiming in the same register as the nearest PROVED row?
`claims/CLAIMS.md` has **no rows at all** — this increment would set the
register. `CLAIMS-ROWS.md`'s header is honest ("every 'PROVED' below is a
PROPOSAL conditional on the critic round … When in doubt, DOWN"), and the
per-row "why not higher" paragraphs are the best part of the lane's output.
`SUMMARY.md` states the conditionality once and then announces "Proved: …"
(OBJ-6); the labbook has no owning section yet, so L11 lockstep is not
satisfiable until the orchestrator lands one. Recommended landing statuses:

| row | proposed | recommended | why |
|---|---|---|---|
| `WH-FORM`, `WH-COMM`, `WH-ALG`, `WH-ALG-MAT`, `WH-SVN`, `WH-POL`, `WH-CANON`, `WH-WEIL-a`, `WH-WEIL-b`, `WH-FUNCT-b`(functor half) | PROVED | **PROVED** | recomputed, no open objection on the statement |
| `WH-CHOICE` | PROVED | **SKETCH until OBJ-1 lands**, then PROVED with `β` named | "exactly one datum" is refuted as written |
| `WH-WEIL-c`, `WH-WEIL-d`, `WH-POL-2` | PROVED | **PROVED with `Q`/`β` in the statement** (OBJ-1) | true for `D2`, false as characteristic-2 invariants |
| `WH-FUNCT-a` | PROVED | **PROVED, scoped to the trace family** (OBJ-7) | |
| `WH-FUNCT-b` (section half) | PROVED | **REFUTED**, with OBJ-2's dichotomy recorded beside it | no section exists over the stated category |
| `WH-WEIL-e` | CONJECTURE | **CONJECTURE**, with "verified at `q = 2, 4`" recorded | a finite check is not the general theorem |

The lane's own headline — "zero admitted steps, Stone–von Neumann proved rather
than cited" — **holds**. That is the strongest part of this artifact and I could
not break it. The failures are all on the canonicity side, which is where this
campaign says its product lives.

FAIL(OBJ-1, OBJ-2, OBJ-3)
