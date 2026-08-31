LANE: scaffold | WRITE SCOPE: labbook/**, scripts/**, .gitignore, theory/checks/README.md
Read briefs/lanes/RULES.md, then CLAUDE.md and PRD.md.

TASK: build the repository's mechanical skeleton so that the gates exist before
the content does. Five deliverables, all of which must actually run.

1. `labbook/main.tex` + `labbook/sections/00_overview.tex` + `labbook/Makefile`.
   The labbook is the campaign product (L9): a human-readable LaTeX record.
   Requirements:
   - builds with `latexmk -pdf main.tex` from inside `labbook/`, producing
     `labbook/main.pdf`, with ZERO errors. Run it. If it does not build, you are
     not done.
   - amsmath/amssymb/amsthm, hyperref, geometry; theorem environments for
     definition / theorem / proposition / lemma / conjecture / scope.
   - a `\provenance{ids}{proved in}{tested by}{reviewed in}` macro rendering a
     small block after a statement.
   - status macros `\statusProved`, `\statusProvedConditional`, `\statusSketch`,
     `\statusConjecture`, `\statusRefuted` rendering as coloured labels whose
     text is exactly the CLAIMS.md status word.
   - `00_overview.tex` states the campaign's north star in two paragraphs and
     carries a status table with a single placeholder row. No mathematical
     claims: there are none yet, and inventing one is a FATAL error.

2. `labbook/WRITING-GUIDE.md` — the binding style contract, modelled on the
   rules below. The reader is a professional mathematical physicist who has NOT
   memorised campaign jargon. Rules to encode: descriptive English names for
   every definition and result, campaign ids only inside `\provenance`; NO
   verbatim/lstlisting/alltt/minted environments anywhere; real LaTeX
   mathematics, never pasted markdown; full hypotheses and exact scope, with a
   `scope` environment after each statement saying what is NOT claimed;
   definitions restated in full rather than pointed at; status words matching
   `claims/CLAIMS.md` exactly, never rounded up.

3. `scripts/check-labbook.sh` — the L11 lockstep gate. Exit 0 iff: every claim
   id in `claims/CLAIMS.md` (first table column) and every definition number
   `Dn` in `definitions.md` appears somewhere in `labbook/sections/`; AND no
   verbatim-family environment appears in the labbook; AND `labbook/main.pdf`
   is not older than any `labbook/**.tex` file. Print each missing identifier.
   It must behave correctly when CLAIMS.md and definitions.md are still empty of
   rows (exit 0, say so).

4. `scripts/setup-env.sh` — this container is ephemeral and ships without TeX,
   numpy, or Julia. Record the exact commands that made this session work:
   `apt-get install -y --no-install-recommends texlive-latex-base
   texlive-latex-recommended texlive-latex-extra texlive-science
   texlive-fonts-recommended latexmk` and `pip install numpy`. Make it
   idempotent and verify each tool afterwards.

5. `scripts/session-close.sh` — runs, in order: check-labbook.sh, the labbook
   build, every `theory/checks/*.py` in green, and every red mode those scripts
   advertise via `--help`. It must fail loudly. Tolerate the current state where
   `theory/checks/` is empty.

Also write `.gitignore`: LaTeX build artefacts, but `labbook/main.pdf` IS
committed (it is the product); `__pycache__`; `refs/**` source bodies EXCEPT
`refs/LEDGER.md` (third-party sources are not ours to redistribute); Julia
artefacts.

Do not create `claims/CLAIMS.md`, `definitions.md`, or `notation.md` — another
lane owns those. Your gate must simply behave sensibly when they are absent or
empty; say in SUMMARY.md what you assumed about their format (first-column
claim ids; `## Dn ` headings).
