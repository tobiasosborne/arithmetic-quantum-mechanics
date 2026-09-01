<!-- ROLE: lane work order (check lane, FCR-1). Written by the orchestrator.
     Model: gpt-5.6-sol, reasoning xhigh, via codex exec. -->

# Check lane — pre-registered falsifier for the FCR-1 increment

You are the independent check lane for the increment defined in
`../../../../briefs/fcr-local-target.md` (repo root: four levels up from this
directory; the repo is `/home/tobias/Projects/arithmetic-quantum-mechanics`).

## Read (allowed)

- `briefs/fcr-local-target.md` — THE specification. The falsifier is written
  from this brief alone.
- `briefs/wh-kappa-target.md` (incl. Errata) and `theory/checks/wh_kappa_check.py`
  — the previous increment's checker, for house style and for gate G10's
  regression expectations.
- `definitions.md`, `notation.md` — trunk conventions (D1–D11).
- `CLAUDE.md`, `PRD.md` — the laws you operate under (L1 red-green especially).

## Forbidden

- Do NOT read `theory/fcr-local.md` (it may not exist yet; if it does, it is
  the prover's shard and you must stay blind to it), and do NOT read any other
  directory under `theory/lanes/`.
- Do NOT write outside THIS directory (`theory/lanes/fcr1/check/`).
- No network. No floating point. No tolerances.

## Deliverables (all in this directory)

1. `fcr_local_check.py` — plain `python3` + `numpy`, no other dependencies,
   implementing gates G1–G11 and red modes exactly as specified in
   `briefs/fcr-local-target.md` §"Pre-registered falsifier". Exact arithmetic:
   elements of `Z[ζ_n]` as integer coefficient vectors modulo the n-th
   cyclotomic polynomial (n ∈ {3, 9, 27} as each seed requires). Rings as
   explicit element tables. Green run: exit 0 and print a per-gate, per-seed
   summary. Each red mode: exit non-zero, printing WHICH gate fired.
2. `fcr_local_EXPECTATIONS.md` — for every gate and seed, the expected counts
   and why the brief implies them (derive counts from first principles in the
   brief's conventions; where a count is discovered by census rather than
   predicted, say so explicitly — discovered counts are data, not checks, and
   must be cross-validated by an independent identity, e.g. |L|·|L^⊥| = |V|).
3. `fcr_local_RED-MATRIX.md` — the gate × mutation reachability matrix. Every
   gate reached by ≥ 1 mutation, or named as decoration with the mutation that
   would reach it. No red mode may be bit-identical in effect to another.
4. `SUMMARY.md` — ≤ 40 lines: what was built, final green/red exit codes
   (actually run them and paste the observed exit codes), open concerns.
   Record at the top: "Lane model: gpt-5.6-sol, reasoning xhigh, codex exec."

## Cautions from the previous increment (binding)

- Erratum E1: the Schrödinger model is `W_{β₀}(a,b) = Z(−b)X(a)` with
  `X(a)e_y = e_{y+a}`, `Z(b)e_y = ψ(by)e_y`. Implement exactly this; a sign
  convention validated at only one seed is not validated.
- Erratum E3: a gate can be blind at particular seeds (identities that
  coincide there). For each gate, note in EXPECTATIONS at which seeds it has
  discriminating power.
- E4: a sub-check no mutation reaches is decoration and must be labeled.
- Runtime discipline: order-27 seeds give 27×27 matrices over Z[ζ_27]
  (φ(27) = 18 coefficients); exhaustive pair-loops are 729² ≈ 5·10⁵ — fine.
  Anything worse than ~10⁷ elementary operations per gate must be justified
  in EXPECTATIONS or reduced (e.g. G9's sampling clause in the brief).

Work fully autonomously. Run everything before writing SUMMARY.md.
