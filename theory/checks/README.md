<!-- ROLE: interface contract for falsifiers under theory/checks/, read by
     scripts/session-close.sh's checker-discovery logic and by anyone
     adding a checker here. UPDATE POLICY: amend on felt failure or TJO
     directive, dated. -->

# theory/checks/ — falsifiers

Empty right now: no claim has a checker yet because no claim exists yet
(`claims/CLAIMS.md` is not created by this lane). The first checker is
specified in `briefs/wh-kappa-target.md`
(`theory/checks/wh_kappa_check.py`); this file fixes the interface every
future checker must expose, because `scripts/session-close.sh` discovers
and drives checkers mechanically, not from a hand-maintained list.

## What lives here

One standalone falsifier per lemma-cluster (CLAUDE.md L2), named after the
shard or brief it falsifies — e.g. `wh_kappa_check.py` for
`briefs/wh-kappa-target.md`. Plain `python3`, `numpy` only (CLAUDE.md /
PRD.md model policy for mechanical work): no dependency on the rest of this
repository's code, so a checker keeps working even as shards move or get
rewritten.

Prefer exact arithmetic (integers, or a minimal-polynomial / integer-vector
representation of the relevant cyclotomic ring) over floating point
(PRD.md, "Exactness over floating point" — a tolerance anywhere is a design
smell on this campaign). Where a float genuinely cannot be avoided, the
script's `--help` text and its runtime output must state the tolerance, the
norm, and an independent invariant checked alongside it; "close enough"
with no stated tolerance is a defect, not a pass.

## The interface `scripts/session-close.sh` relies on

This is mechanical, not a suggestion: `scripts/session-close.sh` drives
every `theory/checks/*.py` file by this contract alone, with no per-checker
special-casing.

1. **Green run.** `python3 theory/checks/<name>.py`, no arguments, runs the
   full green suite and exits `0` iff every gate it defines currently
   passes; non-zero on any failure.
2. **`--help` advertises every red mode.** `python3
   theory/checks/<name>.py --help` prints usage text in which every
   mutation mode this script supports appears verbatim as a long option
   matching `--red` or `--red-<name>` (e.g. `--red`, `--red-symmetric`,
   `--red-trivial-char`, as in `briefs/wh-kappa-target.md`).
   `scripts/session-close.sh` greps this text for tokens matching
   `--red[A-Za-z0-9_-]*` and treats that as the complete list of this
   script's red modes — a red mode not named in `--help` this way is
   invisible to the session-close gate and, per L1, is decoration.
3. **Every red mode exits non-zero.** `python3 theory/checks/<name>.py
   <red-mode>` must exit non-zero (CLAUDE.md L1: "Write the failing check
   first and watch it fail"). `scripts/session-close.sh` runs every mode
   `--help` advertised and fails loudly if any of them exits `0`.
4. **Name the gate that fired.** A checker's gates should carry short ids
   (`C1`, `C2`, ... as in `briefs/wh-kappa-target.md`), and its output — on
   both green and red runs — should say which gate passed or fired. This is
   what lets a reader confirm *reachability* (`briefs/critic-protocol.md`
   Obligation 5) instead of trusting a bare exit code: "all mutants died at
   C1 and never reached the acceptance test" is exactly the kind of finding
   this convention exists to surface.

A checker that only satisfies (1) is not done. A gate with no red mode, or
a red mode `--help` does not advertise, is invisible to the session-close
gate and reads as evidence it never earned (L1).
