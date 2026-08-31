#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$ROOT"

MASTER="report.tex"
SECTIONS_DIR="report/sections"
README="report/README.md"
CATALOG="report/SHARD_CATALOG.md"
MAX_LINES="${REPORT_SHARD_MAX_LINES:-280}"

failures=0

fail() {
  printf 'report shard check: %s\n' "$*" >&2
  failures=1
}

if [[ ! -f "$MASTER" ]]; then
  fail "missing master $MASTER"
fi

if [[ ! -d "$SECTIONS_DIR" ]]; then
  fail "missing sections directory $SECTIONS_DIR"
fi

if [[ ! -f "$README" ]]; then
  fail "missing report map $README"
fi

if [[ ! -f "$CATALOG" ]]; then
  fail "missing shard catalog $CATALOG"
fi

mapfile -t includes < <(
  sed -nE '/^[[:space:]]*%/!s/.*\\include\{([^}]+)\}.*/\1/p' "$MASTER"
)

if (( ${#includes[@]} == 0 )); then
  fail "$MASTER has no \\include statements"
fi

declare -A seen=()
declare -A seen_ids=()

for include in "${includes[@]}"; do
  if [[ "$include" != report/sections/* ]]; then
    fail "\\include{$include} should point under report/sections/"
    continue
  fi

  file="${include}.tex"
  if [[ -n "${seen[$file]+x}" ]]; then
    fail "$file is included more than once"
  fi
  seen["$file"]=1

  if [[ ! -f "$file" ]]; then
    fail "\\include{$include} points to missing $file"
    continue
  fi

  lines="$(wc -l < "$file")"
  if (( lines > MAX_LINES )); then
    fail "$file has $lines lines; target is about 200 and hard guard is $MAX_LINES"
  fi

  if [[ -f "$README" ]] && ! grep -Fq "\`$file\`" "$README"; then
    fail "$README does not list $file"
  fi

  id="$(sed -nE 's/^% SHARD-ID:[[:space:]]*(.+)$/\1/p' "$file" | head -n 1)"
  title="$(sed -nE 's/^% SHARD-TITLE:[[:space:]]*(.+)$/\1/p' "$file" | head -n 1)"
  keywords="$(sed -nE 's/^% SHARD-KEYWORDS:[[:space:]]*(.+)$/\1/p' "$file" | head -n 1)"
  mapfile -t summaries < <(sed -nE 's/^% SHARD-SUMMARY:[[:space:]]*(.+)$/\1/p' "$file")

  if [[ -z "$id" ]]; then
    fail "$file is missing SHARD-ID header"
  elif [[ ! "$id" =~ ^AQM-[0-9]{2}[A-Z]?-[A-Z0-9-]+$ ]]; then
    fail "$file has invalid SHARD-ID '$id'"
  elif [[ -n "${seen_ids[$id]+x}" ]]; then
    fail "duplicate SHARD-ID $id"
  else
    seen_ids["$id"]=1
    file_prefix="$(basename "$file" | cut -c1-2)"
    if [[ "$id" != AQM-"$file_prefix"-* ]]; then
      fail "$file has SHARD-ID $id, expected prefix AQM-$file_prefix-"
    fi
  fi

  if [[ -z "$title" ]]; then
    fail "$file is missing SHARD-TITLE header"
  fi

  if (( ${#summaries[@]} < 2 || ${#summaries[@]} > 3 )); then
    fail "$file must have 2-3 SHARD-SUMMARY lines; found ${#summaries[@]}"
  fi

  if [[ -z "$keywords" ]]; then
    fail "$file is missing SHARD-KEYWORDS header"
  fi

  if [[ -f "$README" && -n "$id" ]] && ! grep -Fq "\`$id\`" "$README"; then
    fail "$README does not list shard label $id"
  fi

  if [[ -f "$CATALOG" ]]; then
    for value in "$id" "$file" "$title" "$keywords"; do
      if [[ -n "$value" ]] && ! grep -Fq "$value" "$CATALOG"; then
        fail "$CATALOG does not list '$value' from $file"
      fi
    done
    for summary in "${summaries[@]}"; do
      if ! grep -Fq "$summary" "$CATALOG"; then
        fail "$CATALOG does not mirror summary from $file: $summary"
      fi
    done
  fi
done

while IFS= read -r -d '' path; do
  file="${path#./}"
  if [[ -z "${seen[$file]+x}" ]]; then
    fail "$file exists but is not included by $MASTER"
  fi
done < <(find "$SECTIONS_DIR" -type f -name '*.tex' -print0 | sort -z)

tmp="$(mktemp)"
if grep -nE '^[[:space:]]*\\(section|subsection|subsubsection|paragraph)\{' "$MASTER" >"$tmp"; then
  cat "$tmp" >&2
  fail "$MASTER contains body sectioning commands; move prose to report/sections/"
fi
rm -f "$tmp"

if (( failures != 0 )); then
  exit 1
fi

printf 'report shard check: %d shards included, labeled, cataloged, all <= %s lines\n' "${#includes[@]}" "$MAX_LINES"
