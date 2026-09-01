<!-- ROLE: lane work order (prove lane, FCR-1). Written by the orchestrator.
     Model: gpt-5.6-sol, reasoning xhigh, via codex exec. -->

# Prove lane — the FCR-1 increment (finite local ring, odd residue characteristic)

You are the prover for the increment defined in
`briefs/fcr-local-target.md` (repo root: `/home/tobias/Projects/arithmetic-quantum-mechanics`,
four levels up from this directory).

## Read (allowed)

- `briefs/fcr-local-target.md` — THE work order: conventions to fix, the nine
  claim statements (FCR-GEN … FCR-REG) with expected registers, scope limits.
- `CLAUDE.md`, `PRD.md` — the laws. L6b (Lamport structured proofs) and L3
  (ground truth is local) bind every line you write.
- `definitions.md`, `notation.md`, `claims/CLAIMS.md` — the trunk single
  sources. Your definitions must extend them without collision (next free
  definition number is D12).
- `theory/wh-kappa.md`, `theory/wh-kappa-choice.md` — the field-case shards.
  Port arguments verbatim where they port; SAY when a proof is a port and
  re-derive it in the ring settingdo not cite the field case as if it
  covered rings.
- `refs/LEDGER.md` and the source bodies it names under `refs/` — citable
  ground truth with the exact locators recorded there. For this increment
  especially: `refs/wood-ajm-1999/` (Thm 3.10, Lemma 4.1, Ex. 4.4),
  `refs/stacks-algebra/algebra.tex` (Artinian lemmas), and the carried-over
  `1710.09884` (T-Frob), `2502.00387` (Bekka SvN for general rings),
  `0912.0574` (Prasad SvN).

## Forbidden

- Do NOT read anything under `theory/lanes/` except this directory. The check
  lane is running in parallel and you must stay blind to it.
- Do NOT write outside THIS directory (`theory/lanes/fcr1/prove/`).
- Do NOT modify trunk files; propose trunk edits via PATCH.md.
- No claim from memory: every nontrivial leaf step cites a definition number,
  a claim id, a refs/ locator, or a named computation done in the shard.
- No network.

## Deliverables (all in this directory)

1. `fcr-local.md` — the Lamport-structured theory shard (L6b), 200–500 lines,
   proving FCR-GEN, FCR-RAD, FCR-COMM, FCR-ALG, FCR-SVN, FCR-POL, FCR-CHOICE,
   FCR-BETA-ODD, FCR-REG as stated in the brief. Structure: numbered steps
   `<1>1, <1>2, …`, sub-proofs `<2>…`, explicit ASSUME/PROVE on nontrivial
   steps, terminal QED steps. Where a statement cannot be reached at the
   brief's expected register, prove the strongest true version and SAY SO —
   the label goes down, never the honesty.
2. `PATCH.md` — proposed trunk edits with STRING ANCHORS (quote the exact
   existing line the edit goes after/replaces), never line numbers, for:
   `definitions.md` (D12+: the five convention groups of the brief),
   `notation.md` (new symbols once each), `claims/CLAIMS.md` (nine new rows
   in the existing table format, statuses as the proofs actually land).
3. `SUMMARY.md` — ≤ 50 lines: per-claim outcome table (id, reached register,
   one-line reason), the sharpest thing you proved, the weakest step you had
   to admit, open questions for the critic. Record at the top:
   "Lane model: gpt-5.6-sol, reasoning xhigh, codex exec."

## Cautions (binding)

- The model convention is fixed by the trunk's E1 resolution:
  `W_{β₀}(a,b) = Z(−b)X(a)` on `ℓ²(R)`. State it; do not re-derive a
  different one.
- Uniform-in-residue-characteristic phrasing for all DEFINITIONS; theorems in
  this increment may and should assume `2 ∈ R^×` where they need it, stated
  explicitly per claim.
- FCR-POL: "Lagrangian" means self-perpendicular w.r.t. `ψ∘ω` (equivalently
  submodule with `L = L^⊥`); watch the distinction between R-nondegeneracy of
  `ω` and nondegeneracy of `ψ∘ω` (the brief's convention group 3).
- FCR-REG is a statement-level regression against the WH-* rows of
  `claims/CLAIMS.md`, claim by claim, in a table — not prose reassurance.
- Wood's "Frobenius" is defined via `R/rad ≅ soc`; the socle-simplicity form
  for commutative local R must be derived, not read into the source.
- Scope discipline: the words Spec, scheme, sheaf, direct sum/product
  decomposition, characteristic 2, Arf, fusion category appear NOWHERE in a
  claim statement you propose (prose remarks pointing at deferred increments
  are fine).

Work fully autonomously. Verify your own small computations (e.g. the Z/9
socle, the non-free Lagrangian witness, the F_3[x,y]/(x,y)² character census)
by direct enumeration in a python3 scratch script in this directory if
helpful — such scripts are scratch, not deliverables, but cite them by name
in the shard where they justify a leaf.
