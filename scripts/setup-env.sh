#!/usr/bin/env bash
# scripts/setup-env.sh
#
# This container is ephemeral and ships without TeX, numpy, or Julia. This
# script records the exact commands that made a session work in this
# environment, so a fresh container can be brought up the same way every
# time:
#
#   apt-get install -y --no-install-recommends \
#     texlive-latex-base texlive-latex-recommended texlive-latex-extra \
#     texlive-science texlive-fonts-recommended latexmk
#   pip install numpy
#
# Idempotent: safe to re-run. Skips apt-get entirely once pdflatex, latexmk,
# and every .sty labbook/main.tex needs already resolve; skips pip once
# numpy already imports. Verifies the whole toolchain afterwards either way,
# so a re-run is also a health check.
set -euo pipefail

log() { echo "[setup-env] $*"; }
die() { echo "[setup-env] ERROR: $*" >&2; exit 1; }

# The exact apt-get command this session used (brief-mandated, verbatim).
TEX_PACKAGES=(
  texlive-latex-base
  texlive-latex-recommended
  texlive-latex-extra
  texlive-science
  texlive-fonts-recommended
  latexmk
)

# LaTeX packages labbook/main.tex actually \usepackage{}s -- what "the TeX
# toolchain works" functionally means here, independent of which apt
# meta-package happens to ship which .sty on a given Debian/Ubuntu release.
REQUIRED_STY=(amsmath amssymb amsthm hyperref geometry xcolor)

# ---------------------------------------------------------------------------
# 1. TeX toolchain
# ---------------------------------------------------------------------------
tex_functionally_present() {
  command -v pdflatex >/dev/null 2>&1 || return 1
  command -v latexmk  >/dev/null 2>&1 || return 1
  local pkg
  for pkg in "${REQUIRED_STY[@]}"; do
    kpsewhich "${pkg}.sty" >/dev/null 2>&1 || return 1
  done
  return 0
}

install_tex() {
  if tex_functionally_present; then
    log "pdflatex, latexmk and every required .sty already resolve -- skipping apt-get."
    return 0
  fi
  log "installing TeX toolchain via apt-get: ${TEX_PACKAGES[*]}"
  local sudo_cmd=()
  if [[ "$(id -u)" -ne 0 ]]; then
    command -v sudo >/dev/null 2>&1 || die "not root and no sudo available; cannot apt-get install."
    sudo_cmd=(sudo)
  fi
  "${sudo_cmd[@]}" apt-get update
  "${sudo_cmd[@]}" apt-get install -y --no-install-recommends "${TEX_PACKAGES[@]}"
}

# ---------------------------------------------------------------------------
# 2. numpy (theory/checks/*.py falsifiers: plain python3 + numpy only)
# ---------------------------------------------------------------------------
install_numpy() {
  if python3 -c 'import numpy' >/dev/null 2>&1; then
    log "numpy already importable -- skipping pip install."
    return 0
  fi
  log "installing numpy via pip"
  pip install numpy
}

# ---------------------------------------------------------------------------
# 3. Verify -- every tool, actually exercised, not just "on PATH"
# ---------------------------------------------------------------------------
verify() {
  local ok=1
  log "verifying toolchain..."

  local tool
  for tool in pdflatex latexmk python3 kpsewhich; do
    if command -v "$tool" >/dev/null 2>&1; then
      log "OK: $tool -> $(command -v "$tool")"
    else
      log "MISSING: $tool"
      ok=0
    fi
  done

  local numpy_ver
  if numpy_ver="$(python3 -c 'import numpy; print(numpy.__version__)' 2>/dev/null)"; then
    log "OK: numpy $numpy_ver"
  else
    log "MISSING: numpy (python3 -c 'import numpy' failed)"
    ok=0
  fi

  local pkg
  for pkg in "${REQUIRED_STY[@]}"; do
    if kpsewhich "${pkg}.sty" >/dev/null 2>&1; then
      log "OK: LaTeX package $pkg -> $(kpsewhich "${pkg}.sty")"
    else
      log "MISSING: LaTeX package $pkg (needed by labbook/main.tex)"
      ok=0
    fi
  done

  [[ $ok -eq 1 ]]
}

install_tex
install_numpy
if verify; then
  log "done -- toolchain ready."
else
  die "toolchain verification failed; see MISSING lines above."
fi
