<!-- lane wh-check | write scope theory/lanes/wh-kappa/check/ -->

STATUS: DONE

- `wh_kappa_check.py` implements C1-C9 over `q` in {2,3,4,5,8,9} in exact `Z[zeta_p]`
  arithmetic (integer vectors mod `Phi_p`; fields built and verified in code). Green run
  exits 0 in 0.5 s; AST audit finds zero true-division nodes, zero float literals, no
  `abs/round/complex` — there is no tolerance to argue about.
- All six red modes exit non-zero, and **all nine gates are reachable**; no two modes have
  the same firing set (checked mechanically, min symmetric difference 9). Details and the
  full matrix in `RED-MATRIX.md`.
- **C9 is reached by none of the brief's five mutations.** I added `--red-halfweyl`
  (symmetrised `omega/2`), flagged as an addition everywhere; without it C9 is decoration.
  Five *sub-checks* (C2b, C2c, C7d census, three of C8's, C9's odd branch) remain unreached
  by any mutation and are named as decoration in `RED-MATRIX.md` rather than sold as tested.
- Findings for the prover/critic, not repairs to make here: (i) **"a non-isotropic line"
  does not exist** — `omega` is alternating, so every line is isotropic; `--red-nonisotropic`
  must use a non-isotropic order-`q` *subgroup*, which exists only for `n >= 2`, and is
  reported NOT CONSTRUCTIBLE (a theorem, verified by census) at `q = 2,3,5`. (ii) **C1 is
  blind to the transposed cocycle at `p = 2`** since `-omega = omega`; only C3 catches
  `--red-cocycle` at `q = 2,4,8`. (iii) C8's literal "two distinct primitive `zeta`" test is
  vacuous at `p = 2`; the substantive content is the `kappa^x`-torsor of `q-1` characters.
  (iv) `omega`-isotropy and `psi(omega)`-isotropy differ for `n >= 2` (`Tr_{F_4/F_2}(1) = 0`).
- `EXPECTATIONS.md` was written first and every pre-registered number matched, including the
  hand-derived `--red-symmetric` line counts `1,0,1,2,1,2` and the census triples. One
  cosmetic deviation recorded, not edited away: `--red-halfweyl` reports C1 before C9 at
  `p = 2` (same C9 guard, numeric gate order).
- No `PATCH.md`: nothing outside my scope needs editing. The checker is a new file destined
  for `theory/checks/wh_kappa_check.py` — copy it there unchanged (no repo imports, runs
  from any cwd, `--help` lists every mode).
- Independence: written from `briefs/wh-kappa-target.md` alone. I did not read
  `theory/lanes/wh-kappa/prove/` (it did not exist when I started and I did not look later),
  any proof shard, or `v0.1/`. Passing proves nothing and promotes nothing (PRD).
