<!-- ROLE: lane work order (prove lane, FCR-2). Written by the orchestrator.
     Model: gpt-5.6-sol, reasoning xhigh, via codex exec. -->

# Prove lane — FCR-2 (residue characteristic 2)

You are the prover for `briefs/fcr2-target.md` (repo root:
`/home/tobias/Projects/arithmetic-quantum-mechanics`, four levels up).

## Read (allowed)

- `briefs/fcr2-target.md` — THE work order: conventions to fix (the
  quadratic datum with the corrected polarization identity, the square law,
  the Gauss sum, isomorphism granularity), the seven claim statements with
  expected registers, scope limits.
- `CLAUDE.md`, `PRD.md`, `definitions.md` (D1–D16; next free number D17),
  `notation.md`, `claims/CLAIMS.md`.
- `theory/wh-kappa.md`, `theory/wh-kappa-choice.md`, `theory/fcr-local.md` —
  trunk shards; port by re-deriving, and say when you port.
- `refs/LEDGER.md` and the bodies it names, especially the FCR-2 addendum:
  `refs/arxiv-1108.0202/` (Strömberg — Milgram's formula verbatim at label
  `eq:milgrams_formula`), `refs/arxiv-1705.04572/` (Ehlen–Skoruppa), and the
  bridge caution recorded in the ledger (the polar form of `ψ∘Q_β` is
  `ψ∘(2β−ω)`, NOT the commutator form — the finite-quadratic-module bridge
  must be constructed, not assumed).
- The promoted falsifier `theory/checks/fcr2_beta_check.py` with its
  EXPECTATIONS and RED-MATRIX, and `theory/lanes/fcr2/check/SUMMARY.md` —
  the blind census results. You may treat census numbers as TARGETS to
  prove, never as evidence.

## Census priors (targets, not evidence)

Two independent blind computations agree on all of this; your job is the
mathematics behind it:

1. At `2 ∈ 𝔪`, `Adm(ω)` has no antisymmetric member, and meets **exactly
   two** isomorphism classes of `H_β(R)` at every tested seed, with class
   sizes `|R|³(q−1)/(2q)` (anisotropic) and `|R|³(q+1)/(2q)`. The
   conjectured separating invariant: writing `β = β₀ + s`,
   `s = (α, γ, δ)` in matrix coordinates, the profile depends only on the
   residues `(ᾱ, δ̄)` and the classes are keyed by
   `Arf(Q̄_β) ∈ κ/℘(κ)` where `Q̄_β` is the residue reduction of `Q_β`.
   Prove: the two-class statement (both directions — the profile
   separation AND explicit isomorphisms within each class), the size
   formulas, and the invariance/well-definedness of the key.
2. `ε_ψ(β) := |R|^{-1} Σ_v ψ(Q_β(v))` lies in `μ_8` (observed: always
   `±1`), is independent of `ψ ∈ Gen(R)`, is constant on classes — and
   does NOT separate the classes at `Z/4`, `F_2[ε]`, `GR(4,2)`, while it
   does separate at `F_2`, `F_4`, `Z/8`, `F_2[t]/t³`. Prove the μ₈/±1
   membership, the ψ-independence, the class-constancy, and characterize
   WHEN it separates (the census suggests: separation iff length ≥ 3 or
   field — find the true statement). The non-separation is a theorem, not
   a failure; state it as one.
3. `FCR2-ALG0`: for `β₀` and `ψ ∈ Gen(R)` in EVERY residue characteristic,
   the algebra is simple, `≅ M_{|R|}(C)`, Stone–von Neumann holds — the
   FCR-1 proofs of the algebra steps used no half except in the β-transport;
   re-derive cleanly for `β₀` alone.
4. `FCR2-NOANTI`, `FCR2-Q` as in the brief. `FCR2-LEVEL` at whatever
   register you honestly reach. `FCR2-REG` as a clause-level table against
   the trunk `p = 2` rows AT THEIR CURRENT REGISTERS (compatibility with a
   SKETCH row is consistency, not evidence — label it so).

## Forbidden

Nothing else under `theory/lanes/` (the check lane's SUMMARY named above is
the single exception, as promoted census data). No writes outside THIS
directory. No trunk edits (PATCH.md proposes them). No claim from memory —
every leaf cites a D-number, claim id, refs/ locator, or named computation.
The Milgram bridge: if you cannot construct the finite-quadratic-module
correspondence rigorously from the Strömberg source, `FCR2-EPS`'s μ₈ clause
may still be proved directly (the observed values are ±1 ⊂ μ₈ — a direct
Gauss-sum computation may suffice without the bridge); claims that need the
unbuilt bridge stay CONJECTURE with the gap named.

## Deliverables (all in this directory)

1. `fcr2-beta.md` — the Lamport shard (L6b), 200–500 lines, claims
   FCR2-NOANTI, FCR2-Q, FCR2-ALG0, FCR2-CLASS (the two-class theorem),
   FCR2-EPS (now including the non-separation clause), FCR2-LEVEL,
   FCR2-REG, at whatever registers the proofs land.
2. `PATCH.md` — string-anchored trunk edits: D17+ (the quadratic datum,
   the Gauss sum, isomorphism granularity), notation rows, claim rows with
   closed quantifiers (the FCR-1 OBJ-3 lesson).
3. `SUMMARY.md` — ≤ 50 lines, per-claim outcome table, sharpest result,
   weakest step, open questions for the critic. Header: "Lane model:
   gpt-5.6-sol, reasoning xhigh, codex exec."

Scratch python for your own verification is welcome (cite by name); exact
arithmetic only. Work fully autonomously.
