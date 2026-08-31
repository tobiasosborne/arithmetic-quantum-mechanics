#!/usr/bin/env bash
set -euo pipefail

show_tool() {
  local name="$1"
  shift
  local command_name="$1"
  if command -v "$command_name" >/dev/null 2>&1; then
    local output
    if output="$("$@" 2>&1 | head -n 1)"; then
      printf '%-10s %s\n' "$name" "$output"
    else
      printf '%-10s version check failed: %s\n' "$name" "${output:-no output}"
    fi
  else
    printf '%-10s not found on PATH\n' "$name"
  fi
}

show_julia_package() {
  local package="$1"
  if ! command -v julia >/dev/null 2>&1; then
    printf '%-10s not checked: julia not found on PATH\n' "$package"
    return 0
  fi

  local output
  if output="$(julia --startup-file=no --project=. -e '
package = ARGS[1]
path = Base.find_package(package)
if path === nothing
    println("not available in active Julia environment")
else
    println("available at " * path)
end
' "$package" 2>&1)"; then
    printf '%-10s %s\n' "$package" "$output"
  else
    printf '%-10s package check failed: %s\n' "$package" "${output:-no output}"
  fi
}

show_python() {
  if command -v python >/dev/null 2>&1; then
    show_tool python python --version
  elif command -v python3 >/dev/null 2>&1; then
    show_tool python python3 --version
  else
    printf '%-10s neither python nor python3 found on PATH\n' python
  fi
}

show_tool julia julia --version
show_tool sage sage --version
show_tool gap gap -v
show_python
show_tool sqlite3 sqlite3 --version
show_julia_package Oscar
show_julia_package Nemo
show_tool latexmk latexmk -v
show_tool bd bd --version
