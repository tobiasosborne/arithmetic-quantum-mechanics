<!-- ROLE: PRD for the Atlas sidequest — the certified pipeline from the
     database of all small finite commutative rings to quantum error-correcting
     codes. Ordered by TJO 2026-09-01 ("this is a major sidequest ... I
     unreasonably want everything here, from rigour, exhaustiveness, coverage,
     efficiency"). Written from the ideal artifact backwards (TJO directive:
     prior art is recon, never a ceiling); forced tradeoffs appear as NAMED
     DECISIONS, never as silent pre-shrinking. Amended only by TJO.
     Synthesized from five parallel scouting reports (enumeration, v0.1
     archaeology, quantization data layer, QECC layer, architecture),
     2026-09-01; their verified findings are marked [S1]..[S5]. -->

# The Atlas — every small commutative ring, quantized, coded, certified

## 0. The artifact

One queryable, certified object and the research it makes routine:

> **For every finite commutative unital ring `R` of order up to the horizon:
> its isomorphism class with a stored, independently re-verifiable
> certificate; a proof-carrying exhaustiveness statement that no ring is
> missing; its complete structural data (local decomposition = Spec, ideals,
> socle, characters); every quantization the trunk's definitions generate,
> with every choice exposed as a point of a named groupoid; every Lagrangian
> and isotropic submodule; and every stabilizer code those produce, with
> parameters, provenance, and the knobs that made it.**

Nothing in it is trusted because a program printed it. Every number is
theorem-backed (a trunk claim), dual-computed (two independent routes that
must agree), or certificate-carried (a stored witness a separate verifier
replays). The Atlas is to finite-ring quantum kinematics what the
SmallGroups library is to group theory — except SmallGroups asks you to
trust it, and the Atlas does not.

**What it is for.** (i) TJO's stated need: every definition of the campaign
illustrated on *every* small example, permanently, queryably. (ii) A
falsifier factory: every future increment (FCR-2..6 and beyond) gets its
census gates by query instead of bespoke enumeration. (iii) A discovery
engine: the scoping pass alone — before any pipeline exists — produced
publishable material (§2). The full Atlas industrializes that.

## 1. Why "unreasonable" is in reach

The five scouting lanes returned verified groundwork, not estimates:

- **Enumeration has a theorem-backed spine** [S1]: enumerate ONLY local
  rings of order `p^k`; every count follows by the unique local
  decomposition (Euler/multiset transform) and multiplicativity — both
  machine-checkable identities. Generation goes by ideals in a covering
  ring `GR(p^a,d)[x_1..x_r]/\mathfrak m^\ell` up to automorphism, staying in
  mixed characteristic throughout (the naive lift to `F_p`-algebras is
  *disproved* by Blackburn–McLean's appendix — four explicit
  counterexamples). Exhaustiveness is certified by a Burnside mass formula
  — `Σ |Aut(A)|/|Stab(I)|` against an independent ideal count — which
  trusts no paper and survives past the literature's edge.
- **The quantization layer is mostly choice-free and collapses** [S3]:
  Lagrangian censuses need no character and no cocycle
  (`L^{⊥_ψ} = L^{⊥_ω}` for generating ψ); representation catalogues need
  no β; and the `|R|³`-wide cocycle layer collapses to *two* rows the
  moment FCR-2's classification lands (already double-blind-confirmed at
  the census level, §2). Weyl operators are monomial: permutation +
  phase-exponent bookkeeping, never dense complex matrices.
- **The QECC dictionary is theorem-clean over Frobenius rings** [S4]:
  R-submodule `C ⊆ C^⊥` ⟺ stabilizer code; `dim = |R|^n/|C|` with |C| a
  *cardinality*, not a power of q — which is exactly where non-freeness
  creates codes no field construction reaches; the phase lift always
  exists and is itself a `|C|`-fold knob.
- **The verification style scales to bulk data** [S5]: planted faults,
  poisoned-theorem dual computations, global identities no single row can
  fake (orbit-stabilizer sums, class-count and sum-of-squares identities,
  cross-order product identities), sampled recomputation by a second
  implementation, byte-level replay determinism.
- **The graveyard is mapped** [S2]: v0.1 died of a stubbed invariant
  engine, a shadow export path, and gates that passed on empty tables.
  Those are hazards with names now, not fates.

## 2. Discoveries already banked by the scoping pass

Recorded here because they calibrate what the full Atlas will yield; each
enters the trunk only through the loop.

1. **Two published errata** [S1]: Nowicki's order-32 table double-counts
   (`E40 = E45`; `L(2,5) = 54`, confirmed three independent ways), and
   Gilmer–Mott's `p³` totals disagree with the accepted counts (their
   unital counts are right); Behboodi et al. transcribe the error.
2. **The FCR-2 classification, at census level, double-blind** [S3 + the
   codex falsifier lane, neither aware of the other]: at `2 ∈ 𝔪` the
   cocycle torsor meets exactly two Heisenberg classes, sizes
   `|R|³(q∓1)/2q`, keyed by the Arf invariant of the residue reduction of
   `Q_β` — and the Gauss sum `ε_ψ(β)` is μ₈-valued, ψ-independent, and
   **non-separating** at every thickened seed. The conjecture survives;
   its intended job does not.
3. **The stratification formula's true form** [S3]: irreducibles number
   `Σ_{χ∈R̂} |I_χ|²` — the `Ann(u)`-form is a Frobenius-only shadow and is
   provably wrong off Frobenius (116 ≠ 104 at `F₂[x,y]/(x,y)²`).
4. **Non-free stabilizer codes are new territory at parameter level**
   [S4]: over two ququart sites, codespace dimensions K ∈ {2, 8} arise
   *only* from non-free stabilizers — unreachable by any free-module or
   field construction; GLP's Conjecture 5.5 has no non-free test in the
   literature, and their char-2 phase theorem corrects the standard
   nonbinary-field formalism (KKKS) at F₄.
5. **PORC phenomena start at order p⁴** [S1]: `L(p,4) = 21 + gcd(3,p−1)`
   — the Atlas must store parametrized families per prime, not one table.

## 3. Research targets the Atlas settles (the unreasonable part)

- **`L(2,6)`**: the number of commutative local rings of order 64 —
  unknown, the last finite-type order (Poonen: rank ≥ 7 has infinitely
  many types), and it extends OEIS A127707 past its recorded wall along
  with the already-derivable terms a(81), a(125), a(243), a(625), a(2401).
- **GLP Conjecture 5.5 and its non-free blind spot**: a mass counterexample
  hunt (can any stabilizer code — free or not — beat its residue-field
  reduction?) falls out of the code layer as a stored column.
- **Classification of non-free stabilizer codes** over chain rings at small
  n: parameters, symplectic-monomial equivalence classes, and whether any
  is inequivalent to every field code under the honest equivalence.
- **The CCKS bridge**: is there a Z/4-Lagrangian-spread whose
  Gray/Teichmüller image is the Calderbank–Cameron–Kantor–Seidel
  orthogonal spread (MUBs, unitary 2-designs)? Nobody has asked.
- **The Milgram bridge**: the exact relation between `ε_ψ(β)`, the
  Strömberg/Ehlen–Skoruppa finite-quadratic-module signature, and the
  two-class invariant — with the corrected polarization identity
  (`2β − ω`) as the wrinkle the literature does not cover.
- **Physics fingerprint tables**: which rings give identical bare quantum
  systems distinguished only by imposed structure — the WH-SYMM question
  answered exhaustively rather than by example.

## 4. Architecture (seven certified stages)

Stage design, verification artifacts, and the mutation story are [S5]'s,
adopted with [S1]'s enumeration spine and [S3]'s layer ordering:

```
S0 sources & scope conventions      → LEDGER rows, Dn for "database ring"
S1 enumeration (local only)         → orbit certificates + Burnside mass formula
S2 canonicalization                 → iso certificates (positive AND negative)
S3 structural invariants            → Spec/local data FIRST, dual-computed
S4 quantization                     → groupoid-stratified, exact cyclotomic
S5 submodule/Lagrangian census      → choice-free layer, run once per ring
S6 QECC                             → codes with MacWilliams + exact-d gates
```

Bulk data lives in `numerics/atlas/` (generated-local, one new gitignore
rule); the trunk carries the builders, the reference digests, the
exhaustiveness certificates, and fast checkers with red modes. The
claims/data firewall [S5]: a CLAIMS row may cite only checker gates (C1);
committed reference CSVs are gate *fixtures* the gate recomputes — a
hand-edited fixture makes the gate fail (C2); census claims carry their
order bound inside the statement text (C3).

The mutation discipline for bulk builds — the genuinely novel verification
design: planted-fault runs, dual computations with poisoned theorem
constants, global identities (orbit-stabilizer, class-count,
sum-of-squares, cross-order product), seeded sampled recomputation by a
second implementation, and replay determinism against a byte manifest.
Every gate carries a population precondition so it can fail on an empty
database — the v0.1 lesson with teeth.

**Non-Frobenius and other blocked strata are first-class gap rows**,
counted against enumeration totals so a dropped stratum breaks a global
identity. The pipeline never quantizes a collapse quotient silently
[S3]; it records the classified degradation (`rad = I_ψ ⊕ I_ψ`, kernel
histograms) and waits for FCR-3.

**Tooling**: pure python3+numpy+stdlib-sqlite3 for everything gated
(house rule); Hecke.jl's structure-constant machinery, GAP's ModIsom
canonical forms (equicharacteristic only — its field-coefficient limit is
exactly the Blackburn–McLean trap's edge), and GAP SmallRing counts are
**oracles**: subprocess-isolated, timeout-guarded, `method='oracle'`
columns, admissible as cross-checks that may disagree, never as merge
proofs [S1, S2, S5].

## 5. Increment ladder

[S5]'s ladder with [S1]'s strategy merged in. Each rung is useful alone;
the first rung that touches mathematics ships an end-to-end thin slice
(one ring, source → certificate → Spec → quantization → Lagrangian →
code) before any bulk widening — the anti-v0.1 rule.

| id | deliverable | hard gate | size |
|---|---|---|---|
| AT-0 | scope conventions (Dn), sources registered: Nowicki (with the erratum recorded), Blackburn–McLean, Raghavendran, Gilmer–Mott (+erratum), Corbas–Williams, Alabiad et al., OEIS A127707 snapshot, Kayal–Saxena, GLP/SK (bodies already live) | LEDGER rows or explicit gap rows | S |
| AT-1 | **the thin slice**: one ring (Z/4) through every stage with every certificate type instantiated | end-to-end checker, red modes at every stage | M |
| AT-2 | all commutative unital rings of order ≤ 63, local-first, with iso + exhaustiveness certificates; reconciliation against A127707 term-by-term, GAP ≤ 15, Nowicki (expecting the 32-row mismatch, stored as the erratum) | mass-formula gate; dropped-class red mode breaks two global identities | L |
| AT-3 | structural layer for all of AT-2: Spec/local data, ideal lattices, characters, Frobenius flags — dual-computed | `dim_κ soc = 1` ⟺ `|Gen| = |R^×|` reconciliation; gap rows counted | M |
| AT-4 | quantization layer: Heisenberg invariants, catalogues (by the `Σ|I_χ|²` form), β-strata (two-row form once FCR-2 lands; full `|R|³` census below the wall), exact ε | class-count + sum-of-squares identities; regression against all existing trunk checkers | L |
| AT-5 | census layer: submodule/Lagrangian/isotropic lattices per ring, multi-site to the honest wall (`|R|^{2n} ≲ 10³` full; sampled beyond, labelled) | chain-ring closed-form gate; `soc⊕𝔪` witness gate; Frobenius duality gate | M |
| AT-6 | QECC layer: all stabilizer codes from the censuses, parameters, CSS/free/degenerate flags, reduction comparison (the Conj-5.5 column), phase-lift knob | MacWilliams gate; exact d below the wall, `d_status='bounded'` above — never an estimate | L |
| AT-7 | **order 64** (`L(2,6)`): the flagship computation, carried entirely by the mass-formula certificate (no external check exists — that is the point) | Burnside gate + replay determinism; OEIS extension drafted | L+ |
| AT-8 | labbook atlas chapter + claims rows for the scoped census statements; the open-question harvest (Conj 5.5 hunt, non-free code classification, CCKS bridge) written up at whatever status the evidence earns | lockstep gates | M |

## 6. Named decisions for TJO (tradeoffs surfaced, not baked)

1. **Horizon**: ship AT-2 at ≤ 63 (fully literature-reconciled) and treat
   64 as the flagship (AT-7)? Or demand ≤ 127 (adds `p,p²` primes and
   nothing hard beyond 64)? 128 is research-level (Poonen wall, char-2
   rank 7 open) and is *not* promised — reaching for it is a separate
   decision.
2. **Route B**: compute the Pontryagin-side quantization (`R ⊕ R̂`) for
   every ring alongside Route A, doubling the layer but making the FCR-4
   adjudication a query? (My recommendation: yes — the comparison IS the
   physics question, and the layer is cheap.)
3. **Non-Frobenius policy**: gap rows only (constitution-clean, my
   recommendation), or additionally compute the collapse-quotient
   quantizations as clearly-labelled derived rows feeding FCR-3?
4. **Distance search budget** for AT-6: exact d is exponential in n; where
   the wall sits (n ≤ 5 exact? 6?) determines whether the Conj-5.5 hunt is
   decisive or merely suggestive at first pass.
5. **Julia**: Hecke.jl has the best existing structure-constant machinery
   but reintroduces a toolchain the reboot dropped. Oracle-only (my
   recommendation), or full member of the build?

## 7. Relation to the mainline

The Atlas consumes trunk theorems (FCR-1's torsor and radical; FCR-2's
classification when it lands; FCR-3's collapse policy; FCR-4's tensor
lemma for non-local rings — until each lands, the corresponding stratum is
gap rows) and repays them: every future increment's falsifier becomes a
query, and the FCR-2 prover already starts from a double-blind census this
scoping pass produced. The mainline increments remain the source of
PROVED; the Atlas is the source of exhaustive, certified *evidence* — the
claims/data firewall keeps that distinction mechanical.

## 8. Hazards (prior art recon — bounded, not binding)

v0.1's five fatal patterns, each now a named gate design: no writer ever
written → the thin slice is increment 1; shadow export paths → CSVs are
SELECTs or gate fixtures, nothing else; vacuous acceptance → population
preconditions everywhere; stub invariants shipped as load-bearing → Spec
data is AT-3, before any bulk quantization; hand tables wearing data
costumes → every record is a function of the ring object, enforced by the
poisoned-theorem red modes. The CAS traps ([S1, S2]: GAP predicates under
`--bare`, ModIsom's field-only coefficients, Hecke's broken finite-ring
`is_isomorphic`, Magma's licensing) are quarantined by the oracle rule.
