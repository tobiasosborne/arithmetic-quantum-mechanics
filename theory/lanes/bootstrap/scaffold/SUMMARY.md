STATUS: DONE

Established: labbook/{main.tex,Makefile,sections/00_overview.tex,WRITING-GUIDE.md} build clean -- `cd labbook && latexmk -pdf main.tex` and `make` both exit 0, "Output written on main.pdf (2 pages...)", zero warnings, verified clean-room; all \provenance/\status* macros and all 6 theorem envs compile (throwaway fixture, not shipped in labbook/).
scripts/check-labbook.sh, session-close.sh, setup-env.sh are +x and exit 0 now; each mutation-tested for real: check-labbook.sh --self-test fires+passes on all 4 gates; session-close.sh run against 4 fake checkers (green-pass, green-fail, red-that-wrongly-passes, no-red-advertised), each dying with the right diagnosis.
Caught and fixed a real bug in gate A itself: its naive "any pipe line" parser misfired when claims/CLAIMS.md appeared mid-session with a decoy status-vocabulary table; now keys off the header row whose first cell is literally "id".
Assumed formats (no other lane's format is authoritative): claims/CLAIMS.md table headed "id"; definitions.md "## Dn " headings. Both degrade to a graceful PASS today (absent/empty).
Overview states the north star only, one placeholder status row, no invented claim or definition.
.gitignore: I wrote the 4-category version; superseded mid-session by a concurrent, broader, functionally-superset version -- kept per instructions, not reverted. Flag for TJO/orchestrator: it also silently ignores labbook/figures/*.pdf and numerics/**/*.pdf (untested, not fixed by me).
No PATCH.md: nothing outside my write scope was touched.
