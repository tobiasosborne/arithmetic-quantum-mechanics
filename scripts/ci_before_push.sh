#!/usr/bin/env bash
set -euo pipefail

if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  git diff --check
else
  printf 'ci-before-push: not a git repository, skipping git diff --check\n'
fi

scripts/check_report_shards.sh

if command -v latexmk >/dev/null 2>&1; then
  make report
else
  printf 'ci-before-push: latexmk not found, skipping report build\n'
fi

if command -v julia >/dev/null 2>&1; then
  julia --project=. -e 'using Pkg; Pkg.test()'
  julia --project=. scripts/run_all.jl --fast
else
  printf 'ci-before-push: julia not found, skipping Julia checks\n'
fi
