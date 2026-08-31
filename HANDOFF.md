<!-- ROLE: live state. UPDATE POLICY: every session end and every phase
     boundary. Not an authoritative source for mathematics — that is
     definitions.md, claims/CLAIMS.md, and theory/. -->

# HANDOFF — live state

Updated: 2026-08-31, session 1 (the reboot session).

Read order gate: `CLAUDE.md` -> **`PRD.md` (the constitution; where it conflicts
with anything recorded here, PRD wins)** -> this file.

## Where the campaign is

Session 1 rebooted the repository. The previous lab book is frozen under
`v0.1/` and is a source of hints only (L12). The trunk is being rebuilt to
rk-light standards from an empty root.

North star: a general definition and workflow assigning canonical quantum
systems — Hilbert space, observable algebra, and where possible dynamics as
automorphisms or projective unitary representations of symmetry groups, with
fusion categories as the expected general endpoint — to arbitrary arithmetic
schemes. Guiding path: `F_p` and its canonical symplectic space `F_p x F_p`.
Product: `labbook/main.pdf`.

## Environment (this container is ephemeral)

`pdflatex`, `latexmk` and `numpy` are NOT preinstalled. `scripts/setup-env.sh`
reinstalls them; run it first in any new session. Julia is absent and is not
currently needed — checkers are plain `python3` + `numpy`, exact arithmetic.
`bd` (beads) is absent, so cross-session state lives in this file (L8).

## In flight

First increment: `briefs/wh-kappa-target.md` — the canonical quantum system of
`Spec κ` for a finite field `κ`, with every choice named. Its rows are not yet
in `claims/CLAIMS.md` and will not be until the L6 loop reports.

## Next useful steps

1. Finish the first increment's loop and admit its rows at whatever status it
   produces.
2. Only then: the general closed-point construction for an arbitrary affine
   scheme of finite type, tested against the seed case.
3. Decide, with sources in hand, whether the Weil-representation lift is stated
   for all `q` or scoped to odd `q` in the first labbook release.
