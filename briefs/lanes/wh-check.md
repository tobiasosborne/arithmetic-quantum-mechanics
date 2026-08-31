LANE: wh-check | WRITE SCOPE: theory/lanes/wh-kappa/check/ ONLY
Read briefs/lanes/RULES.md, CLAUDE.md, PRD.md, then briefs/wh-kappa-target.md.

TASK: write the pre-registered falsifier `wh_kappa_check.py` **from the target
brief alone**. You must not read `theory/lanes/wh-kappa/prove/`, and you must
not read any proof shard. The checker is independent evidence; if it is written
against the prover's reasoning it is worth nothing.

Implement exactly the gates C1-C9 and the five red modes tabulated in
`briefs/wh-kappa-target.md`, over `q` in {2,3,4,5,8,9}.

Non-negotiable engineering constraints:

- `python3` + `numpy` only. No repo imports. Runs from the repository root as
  `python3 -O theory/checks/wh_kappa_check.py`.
- **Exact arithmetic. No tolerances anywhere.** Represent `Z[ζ_p]` as integer
  vectors modulo the `p`-th cyclotomic polynomial `1 + x + ... + x^(p-1)`, and
  do Weyl-operator matrix algebra exactly over that ring. If you find yourself
  writing `abs(a-b) < eps`, you have taken a wrong turn.
- Finite fields `F_q` for non-prime `q` need a real implementation — build
  `F_4`, `F_8`, `F_9` via a Conway-style irreducible polynomial you construct
  and verify irreducible in code, not one you recall.
- Green run exits 0 and prints one line per gate per `q`. Each red mode exits
  non-zero AND prints which gate killed it. `--help` lists every red mode.
- Gate reachability is part of the deliverable: produce
  `RED-MATRIX.md` in your lane dir, a table of red mode against the gate that
  actually fired, and flag any gate that no red mode reaches, and any two red
  modes whose effect is identical.

Write your own independent expectations first: before implementing, write
`EXPECTATIONS.md` recording what each gate should produce (e.g. the number of
isotropic lines for each `q`, the dimension of the span of the Weyl operators)
computed by hand or by a separate scratch computation. Then implement, and
report any disagreement between your expectations and your implementation as a
finding rather than quietly editing the expectation.

Deliverables in your lane dir: `wh_kappa_check.py`, `EXPECTATIONS.md`,
`RED-MATRIX.md`, `run-green.txt`, `run-red-*.txt`, `SUMMARY.md`.
