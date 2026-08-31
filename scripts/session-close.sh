#!/usr/bin/env bash
# scripts/session-close.sh
#
# The mechanical part of CLAUDE.md's "Session close" checklist: runs, IN
# ORDER,
#   1. scripts/check-labbook.sh              (L11 lockstep gate)
#   2. the labbook build                     (latexmk -pdf main.tex)
#   3. every theory/checks/*.py, green
#   4. every red mode each theory/checks/*.py script advertises via --help
# and fails loudly -- prints a banner per step, stops at the first failure
# with a one-line diagnosis on stderr, and never reports success unless
# every step actually passed.
#
# Tolerates theory/checks/ being empty (the current, pre-content state):
# steps 3-4 report "nothing to run" and pass, rather than fail on an empty
# glob.
#
# This script does NOT update HANDOFF.md and does NOT run git commit/add/
# push -- those are steps 4-5 of CLAUDE.md's session close, and a
# lane-isolated repository with several checkers possibly running in
# parallel must never have a script silently commit or push a mid-flight
# state (briefs/lanes/RULES.md: "Never run git commit, git add, git push").
# This script is the gate; the human (or orchestrator) still updates
# HANDOFF.md and commits/pushes by hand once every gate below is green.
#
# A red mode is any long option matching `--red` or `--red-<name>` that a
# checker's own `--help` text advertises (see theory/checks/README.md for
# the full interface contract this relies on).
set -u

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_ROOT"

banner() { echo; echo "=== $* ==="; }
die() {
  echo "[session-close] FAILED: $*" >&2
  echo "[session-close] session is NOT closed." >&2
  exit 1
}

# ---------------------------------------------------------------------------
# 1. L11 lockstep gate
# ---------------------------------------------------------------------------
banner "1/4  scripts/check-labbook.sh"
"$SCRIPT_DIR/check-labbook.sh" || die "check-labbook.sh reported a lockstep failure (see above)."

# ---------------------------------------------------------------------------
# 2. Labbook build
# ---------------------------------------------------------------------------
banner "2/4  labbook build (latexmk -pdf main.tex)"
[[ -f "$REPO_ROOT/labbook/main.tex" ]] || die "labbook/main.tex is missing."
( cd "$REPO_ROOT/labbook" && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex ) \
  || die "labbook failed to build with latexmk -pdf main.tex."
[[ -f "$REPO_ROOT/labbook/main.pdf" ]] || die "latexmk exited 0 but labbook/main.pdf was not produced."
echo "[session-close] OK: labbook/main.pdf built."

# ---------------------------------------------------------------------------
# 3 + 4. Every theory/checks/*.py: green run, then every advertised red mode
# ---------------------------------------------------------------------------
banner "3/4 + 4/4  theory/checks/*.py -- green, then every --help-advertised red mode"
CHECKS_DIR="$REPO_ROOT/theory/checks"
shopt -s nullglob
checks=("$CHECKS_DIR"/*.py)
shopt -u nullglob

if [[ ${#checks[@]} -eq 0 ]]; then
  echo "[session-close] theory/checks/ has no *.py checkers yet -- nothing to run."
else
  for chk in "${checks[@]}"; do
    name="$(basename "$chk")"

    echo "--- $name (green run) ---"
    python3 "$chk" || die "$name failed its green run."

    echo "--- $name --help (discovering red modes) ---"
    help_out="$(python3 "$chk" --help 2>&1)" || die "$name --help itself exited non-zero."
    red_modes="$(printf '%s\n' "$help_out" | grep -oE -- '--red[A-Za-z0-9_-]*' | sort -u)"
    if [[ -z "$red_modes" ]]; then
      die "$name advertises no --red* mode in --help (L1 requires a mutation mode)."
    fi

    while IFS= read -r mode; do
      [[ -z "$mode" ]] && continue
      echo "--- $name $mode (must exit non-zero) ---"
      if python3 "$chk" "$mode" >/dev/null 2>&1; then
        die "$name $mode exited 0 -- this red mode did not fail (the gate it should trip is decoration)."
      fi
      echo "[session-close] OK: $name $mode exited non-zero as required."
    done <<<"$red_modes"
  done
fi

echo
echo "[session-close] ALL GATES PASSED."
echo "[session-close] Remaining CLAUDE.md session-close steps (manual, not run by this script):"
echo "[session-close]   - update HANDOFF.md"
echo "[session-close]   - git add / git commit / git push"
