#!/usr/bin/env bash
set -euo pipefail

show_tool() {
  local name="$1"
  shift
  if command -v "$name" >/dev/null 2>&1; then
    printf '%-10s %s\n' "$name" "$("$@" 2>&1 | head -n 1)"
  else
    printf '%-10s not found on PATH\n' "$name"
  fi
}

show_tool julia julia --version
show_tool sage sage --version
show_tool gap gap -v
show_tool latexmk latexmk -v
show_tool bd bd --version
