#!/usr/bin/env bash
# scripts/check-labbook.sh
#
# The L11 lockstep gate (CLAUDE.md): "Any commit that changes
# claims/CLAIMS.md or definitions.md, or that lands a worked example or
# figure, MUST update the owning labbook section in the same commit."
#
# Exits 0 iff ALL of:
#   A. every claim id (the FIRST column of the claims/CLAIMS.md table) is
#      cited somewhere under labbook/sections/;
#   B. every definition number Dn (a "## Dn ..." heading in definitions.md)
#      is cited somewhere under labbook/sections/;
#   C. no verbatim-family environment (verbatim, lstlisting, alltt, minted)
#      appears anywhere under labbook/ (WRITING-GUIDE.md Rule 2);
#   D. labbook/main.pdf is not older than any labbook/**.tex file.
#
# Prints each missing identifier / offending file. Exits non-zero, with a
# report of every gate that failed, otherwise.
#
# claims/CLAIMS.md and definitions.md do not exist in a fresh checkout of
# this campaign (another lane owns them) -- gates A and B degrade
# gracefully in that case: "nothing to check yet", and PASS. That is a
# statement about this script not crashing or lying, not a statement that
# lockstep has been verified once those files gain rows.
#
# FORMAT ASSUMED (no other lane's format is authoritative over this script;
# see theory/lanes/bootstrap/scaffold/SUMMARY.md for the record of this
# assumption):
#   claims/CLAIMS.md  -- a markdown table; first column header "id"
#                         (case-insensitive); one claim id per data row.
#   definitions.md    -- each definition introduced by a markdown heading
#                         whose first token is "Dn", e.g. "## D1 <name>".
#
# Usage:
#   scripts/check-labbook.sh              run the real gate against this repo
#   scripts/check-labbook.sh --self-test  mutation-test the gate itself (a
#   scripts/check-labbook.sh --red        --red mode, per L1): builds a
#                                          synthetic sandbox with one induced
#                                          defect per gate (A/B/C/D) plus a
#                                          clean counterpart, and asserts
#                                          each gate fires on its mutant and
#                                          passes on the clean case. Exits
#                                          non-zero if any gate is decoration
#                                          (does not fire) or a false
#                                          positive (fires on clean input).
#   scripts/check-labbook.sh --help       this message
set -u

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

usage() {
  sed -n '2,45p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'
}

# ============================================================================
# Gate implementations. Each takes explicit paths (never hardcoded), so the
# self-test below can point them at a synthetic sandbox instead of this repo.
# Each prints its own findings and returns 0 (pass) or 1 (fail).
# ============================================================================

# gate_claims CLAIMS_FILE SECTIONS_DIR
gate_claims() {
  local claims_file="$1" sections_dir="$2"
  local rc=0

  if [[ ! -f "$claims_file" ]]; then
    echo "[gate A] $claims_file does not exist yet -- nothing to check, PASS."
    return 0
  fi

  # Extract column 2 of the SPECIFIC markdown table whose header's first cell
  # is "id" (case-insensitive). This file may contain OTHER pipe tables (a
  # status-vocabulary legend, say) that must not be mistaken for the claims
  # table just because they too start with "|" -- a real decoy encountered
  # while testing this gate, see theory/lanes/bootstrap/scaffold/SUMMARY.md.
  local ids
  ids="$(awk -F'|' '
    /^[[:space:]]*\|/ {
      col2 = $2
      gsub(/^[[:space:]]+|[[:space:]]+$/, "", col2)
      gsub(/[`*]/, "", col2)
      if (in_table) {
        if (col2 ~ /^:?-+:?$/) { next }
        if (col2 == "") { next }
        print col2
        next
      }
      if (tolower(col2) == "id") { in_table = 1 }
      next
    }
    { in_table = 0 }
  ' "$claims_file" | grep -v '^$')"

  if [[ -z "$ids" ]]; then
    echo "[gate A] $claims_file has no claim rows yet (no table headed 'id' has data rows) -- nothing to check, PASS."
    return 0
  fi

  if [[ ! -d "$sections_dir" ]]; then
    echo "[gate A] FAIL: $sections_dir does not exist, but $claims_file has claim rows."
    return 1
  fi

  while IFS= read -r cid; do
    [[ -z "$cid" ]] && continue
    if ! grep -rqF -- "$cid" "$sections_dir" 2>/dev/null; then
      echo "[gate A] MISSING claim id in $sections_dir: $cid"
      rc=1
    fi
  done <<<"$ids"

  [[ $rc -eq 0 ]] && echo "[gate A] OK: every claim id in $claims_file is cited under $sections_dir."
  return $rc
}

# gate_defs DEFS_FILE SECTIONS_DIR
gate_defs() {
  local defs_file="$1" sections_dir="$2"
  local rc=0

  if [[ ! -f "$defs_file" ]]; then
    echo "[gate B] $defs_file does not exist yet -- nothing to check, PASS."
    return 0
  fi

  local dnums
  dnums="$(grep -oE '^#{1,6}[[:space:]]+D[0-9]+' "$defs_file" 2>/dev/null \
          | grep -oE 'D[0-9]+')"

  if [[ -z "$dnums" ]]; then
    echo "[gate B] $defs_file has no '## Dn' headings yet -- nothing to check, PASS."
    return 0
  fi

  if [[ ! -d "$sections_dir" ]]; then
    echo "[gate B] FAIL: $sections_dir does not exist, but $defs_file has Dn headings."
    return 1
  fi

  while IFS= read -r dn; do
    [[ -z "$dn" ]] && continue
    if ! grep -rqE -- "\b${dn}\b" "$sections_dir" 2>/dev/null; then
      echo "[gate B] MISSING definition in $sections_dir: $dn"
      rc=1
    fi
  done <<<"$dnums"

  [[ $rc -eq 0 ]] && echo "[gate B] OK: every Dn heading in $defs_file is cited under $sections_dir."
  return $rc
}

# gate_verbatim LABBOOK_DIR
gate_verbatim() {
  local labbook_dir="$1"
  local pattern='\\begin\{(verbatim\*?|lstlisting|alltt|minted)\}'
  local rc=0

  if [[ ! -d "$labbook_dir" ]]; then
    echo "[gate C] $labbook_dir does not exist -- nothing to check, PASS."
    return 0
  fi

  while IFS= read -r -d '' f; do
    if grep -nE "$pattern" "$f" >/dev/null 2>&1; then
      echo "[gate C] FORBIDDEN environment in $f:"
      grep -nE "$pattern" "$f" | sed 's/^/    /'
      rc=1
    fi
  done < <(find "$labbook_dir" -type f -name '*.tex' -print0 2>/dev/null)

  [[ $rc -eq 0 ]] && echo "[gate C] OK: no verbatim/lstlisting/alltt/minted under $labbook_dir."
  return $rc
}

# gate_freshness LABBOOK_DIR MAIN_PDF
gate_freshness() {
  local labbook_dir="$1" main_pdf="$2"

  if [[ ! -f "$main_pdf" ]]; then
    echo "[gate D] FAIL: $main_pdf does not exist. Build: cd labbook && latexmk -pdf main.tex"
    return 1
  fi

  local stale=()
  while IFS= read -r -d '' f; do
    [[ "$f" -nt "$main_pdf" ]] && stale+=("$f")
  done < <(find "$labbook_dir" -type f -name '*.tex' -print0 2>/dev/null)

  if [[ ${#stale[@]} -gt 0 ]]; then
    echo "[gate D] FAIL: $main_pdf is older than: ${stale[*]}"
    echo "[gate D] Rebuild: cd labbook && latexmk -pdf main.tex"
    return 1
  fi

  echo "[gate D] OK: $main_pdf is not older than any $labbook_dir/**.tex file."
  return 0
}

# ============================================================================
# Real run, against this repository.
# ============================================================================
run_real() {
  local fail=0
  gate_claims    "$REPO_ROOT/claims/CLAIMS.md" "$REPO_ROOT/labbook/sections" || fail=1
  gate_defs      "$REPO_ROOT/definitions.md"   "$REPO_ROOT/labbook/sections" || fail=1
  gate_verbatim  "$REPO_ROOT/labbook"                                       || fail=1
  gate_freshness "$REPO_ROOT/labbook" "$REPO_ROOT/labbook/main.pdf"         || fail=1
  echo "----------------------------------------"
  if [[ $fail -ne 0 ]]; then
    echo "[check-labbook] FAIL"
    return 1
  fi
  echo "[check-labbook] PASS"
  return 0
}

# ============================================================================
# Self-test / --red mode (L1: "every checker ships a mutation mode that MUST
# exit non-zero"). Builds one tiny sandbox per gate with an induced defect,
# plus a clean counterpart, and asserts: the gate FAILS on the defect and
# PASSES on the clean case. Reports which gate letter caught (or missed)
# each mutant, per critic-protocol.md's reachability convention.
# ============================================================================
self_test() {
  local tmp overall=0
  tmp="$(mktemp -d)"
  trap 'rm -rf "$tmp"' RETURN

  echo "== check-labbook.sh --self-test: mutation-testing its own gates =="
  echo "sandbox: $tmp"
  echo

  # ---- Gate A: claim-id lockstep ----
  echo "--- gate A: missing claim id (expect FAIL) ---"
  mkdir -p "$tmp/A_red/claims" "$tmp/A_red/labbook/sections"
  cat >"$tmp/A_red/claims/CLAIMS.md" <<'EOF'
| id | statement | status | depends-on | proved-in | tested-in |
|----|-----------|--------|------------|-----------|-----------|
| ZZ-RED | dummy claim for self-test | CONJECTURE | | | |
EOF
  echo 'dummy section, deliberately not mentioning the id.' >"$tmp/A_red/labbook/sections/00_dummy.tex"
  if gate_claims "$tmp/A_red/claims/CLAIMS.md" "$tmp/A_red/labbook/sections"; then
    echo "[self-test] FAIL: gate A did not fire on a missing claim id (decoration)."; overall=1
  else
    echo "[self-test] OK: gate A fired on missing claim id ZZ-RED."
  fi

  echo "--- gate A: same id present (expect PASS) ---"
  mkdir -p "$tmp/A_green/claims" "$tmp/A_green/labbook/sections"
  cp "$tmp/A_red/claims/CLAIMS.md" "$tmp/A_green/claims/CLAIMS.md"
  echo 'dummy section citing \provenance{ZZ-RED}{n/a}{n/a}{n/a}.' >"$tmp/A_green/labbook/sections/00_dummy.tex"
  if gate_claims "$tmp/A_green/claims/CLAIMS.md" "$tmp/A_green/labbook/sections"; then
    echo "[self-test] OK: gate A passes once the id is cited."
  else
    echo "[self-test] FAIL: gate A false-positived on a citation that IS present."; overall=1
  fi
  echo

  # ---- Gate B: definition-number lockstep ----
  echo "--- gate B: missing Dn heading citation (expect FAIL) ---"
  mkdir -p "$tmp/B_red/labbook/sections"
  printf '## D77 A dummy definition for self-test\n\nBody.\n' >"$tmp/B_red/definitions.md"
  echo 'dummy section with unrelated prose only.' >"$tmp/B_red/labbook/sections/00_dummy.tex"
  if gate_defs "$tmp/B_red/definitions.md" "$tmp/B_red/labbook/sections"; then
    echo "[self-test] FAIL: gate B did not fire on a missing Dn citation (decoration)."; overall=1
  else
    echo "[self-test] OK: gate B fired on missing definition D77."
  fi

  echo "--- gate B: same Dn present (expect PASS) ---"
  mkdir -p "$tmp/B_green/labbook/sections"
  cp "$tmp/B_red/definitions.md" "$tmp/B_green/definitions.md"
  echo 'dummy section citing D77 in its \provenance block.' >"$tmp/B_green/labbook/sections/00_dummy.tex"
  if gate_defs "$tmp/B_green/definitions.md" "$tmp/B_green/labbook/sections"; then
    echo "[self-test] OK: gate B passes once D77 is cited."
  else
    echo "[self-test] FAIL: gate B false-positived on a citation that IS present."; overall=1
  fi
  echo

  # ---- Gate C: verbatim-family ban ----
  echo "--- gate C: a verbatim block present (expect FAIL) ---"
  mkdir -p "$tmp/C_red/labbook"
  printf 'prose\n\\begin{verbatim}\nhello\n\\end{verbatim}\nmore prose\n' >"$tmp/C_red/labbook/dummy.tex"
  if gate_verbatim "$tmp/C_red/labbook"; then
    echo "[self-test] FAIL: gate C did not fire on a verbatim block (decoration)."; overall=1
  else
    echo "[self-test] OK: gate C fired on a verbatim block."
  fi

  echo "--- gate C: no verbatim-family environment (expect PASS) ---"
  mkdir -p "$tmp/C_green/labbook"
  printf 'prose only, no banned environment.\n' >"$tmp/C_green/labbook/dummy.tex"
  if gate_verbatim "$tmp/C_green/labbook"; then
    echo "[self-test] OK: gate C passes on clean prose."
  else
    echo "[self-test] FAIL: gate C false-positived on clean prose."; overall=1
  fi
  echo

  # ---- Gate D: pdf freshness ----
  echo "--- gate D: main.pdf older than a .tex source (expect FAIL) ---"
  mkdir -p "$tmp/D_red/labbook/sections"
  : >"$tmp/D_red/labbook/main.pdf"
  touch -d '2 hours ago' "$tmp/D_red/labbook/main.pdf"
  : >"$tmp/D_red/labbook/sections/00_dummy.tex"
  touch -d '1 hour ago' "$tmp/D_red/labbook/sections/00_dummy.tex"
  if gate_freshness "$tmp/D_red/labbook" "$tmp/D_red/labbook/main.pdf"; then
    echo "[self-test] FAIL: gate D did not fire on a stale main.pdf (decoration)."; overall=1
  else
    echo "[self-test] OK: gate D fired on a stale main.pdf."
  fi

  echo "--- gate D: main.pdf newer than every .tex source (expect PASS) ---"
  mkdir -p "$tmp/D_green/labbook/sections"
  : >"$tmp/D_green/labbook/sections/00_dummy.tex"
  touch -d '1 hour ago' "$tmp/D_green/labbook/sections/00_dummy.tex"
  : >"$tmp/D_green/labbook/main.pdf"
  if gate_freshness "$tmp/D_green/labbook" "$tmp/D_green/labbook/main.pdf"; then
    echo "[self-test] OK: gate D passes when main.pdf is fresh."
  else
    echo "[self-test] FAIL: gate D false-positived on a fresh main.pdf."; overall=1
  fi
  echo

  echo "----------------------------------------"
  if [[ $overall -ne 0 ]]; then
    echo "[check-labbook --self-test] FAIL: at least one gate is decoration or a false positive."
    return 1
  fi
  echo "[check-labbook --self-test] PASS: all four gates fire on their mutant and pass on the clean case."
  return 0
}

case "${1:-}" in
  --help|-h)
    usage
    exit 0
    ;;
  --self-test|--red)
    self_test
    exit $?
    ;;
  "")
    run_real
    exit $?
    ;;
  *)
    echo "check-labbook.sh: unknown argument: $1" >&2
    usage >&2
    exit 2
    ;;
esac
