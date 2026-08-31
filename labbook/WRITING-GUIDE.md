<!-- ROLE: binding style contract for everything under labbook/**.tex.
     UPDATE POLICY: amend on felt failure or TJO directive, dated. -->

# WRITING-GUIDE.md — the labbook's binding style contract

The reader is a professional mathematical physicist who has **not** memorised
this repository's jargon and has never seen `claims/CLAIMS.md`,
`definitions.md`, or any brief under `briefs/`. Every section must be
readable, and checkable, on its own terms by that reader. Where this guide
and habit disagree, this guide wins; where this guide and `CLAUDE.md`/
`PRD.md` disagree, `CLAUDE.md`/`PRD.md` win (they are amended only by TJO).

The macros and environments named below are defined once, in
`labbook/main.tex`'s preamble; do not redefine them locally in a section
file.

## Rule 1 — descriptive English names; campaign ids live only in `\provenance`

Every definition and every result gets a real, descriptive English name of
its own — "the polarizing cocycle of a symplectic space over a finite
field," not "D2"; "uniqueness of the finite Weyl representation," not
"WH-SVN." Campaign identifiers — claim ids from `claims/CLAIMS.md`,
`Dn` numbers from `definitions.md` — are bookkeeping. They appear **only**
inside the `\provenance{ids}{proved in}{tested by}{reviewed in}` block that
follows a statement (and its `scope` block, where present), never inside a
theorem heading, never inside the running prose the reader has to parse to
follow the mathematics.

## Rule 2 — no verbatim-family environments, anywhere

`\begin{verbatim}`, `\begin{lstlisting}`, `\begin{alltt}`, `\begin{minted}`
(starred or otherwise) are banned from every file under `labbook/`, no
exception. This is mechanically enforced by `scripts/check-labbook.sh`. A
lab book is mathematics, not a code listing: if an algorithm needs
describing, describe it in prose and mathematics, or name the script under
`scripts/` or `theory/checks/` that carries it and cite that script by path.

## Rule 3 — real LaTeX mathematics, never pasted markdown

Every piece of mathematics is real LaTeX: inline `$...$`, displayed
`\[...\]`, `align`, `gather`, and friends from `amsmath`. Markdown residue —
bare `*emphasis*` asterisks, backticked identifiers standing in for actual
math, a dash-bullet list doing the job of a numbered hypothesis list — does
not belong in a `.tex` file. A derivation that started life in a markdown
scratch file (a lane's `SUMMARY.md`, a shard draft, a verdict) is
**retypeset** for the labbook, never pasted.

## Rule 4 — full hypotheses; a `scope` block after every statement

State every hypothesis inside the statement itself. No "as before," no
hypothesis left implicit because it is "obvious from context" — the reader
has not read the context. Immediately after every `theorem` / `proposition`
/ `lemma` / `definition` / `conjecture`, an (unnumbered) `scope` environment
records, in a sentence or two, exactly what is **not** claimed: excluded
cases, generalisations not yet established, a choice the statement secretly
depends on. `scope` is never omitted as a shortcut; if nothing beyond the
stated hypotheses is excluded, it says exactly that — "no restriction beyond
the hypotheses above" — rather than being left out.

## Rule 5 — definitions restated in full, never pointed at

A section that *uses* a definition restates it in full — English gloss and
LaTeX — even though `definitions.md` already has it verbatim under some
`Dn`. The reader should never have to leave the PDF to know what a symbol
means. The restatement must reproduce `definitions.md` exactly (not a
paraphrase that can drift out of sync with the single source); `\provenance`
still cites `Dn`, for bookkeeping, after the restatement.

## Rule 6 — status words match `claims/CLAIMS.md` exactly; never rounded up

Use `\statusProved`, `\statusProvedConditional`, `\statusSketch`,
`\statusConjecture`, or `\statusRefuted` — and use the one matching the
**current** row of `claims/CLAIMS.md` for that claim id, not the status
hoped for, and not the status that was true when the section was first
drafted if it has since moved (promotion and demotion both apply, PRD.md
"Status discipline"). A `\statusProvedConditional` claim's statement text
must display its condition explicitly (PRD.md); the label itself never grows
a fifth word to carry it. A labbook section reading `\statusProved` while
`claims/CLAIMS.md` reads `SKETCH` for the same id is an L11 lockstep failure
whether or not `scripts/check-labbook.sh` happens to catch it — the
mechanical gate checks that the id is *cited*, not that the *status word* on
the page still agrees; that agreement is a per-edit obligation, not
something to lean on the gate for.

## Worked contrast

**Bad** (jargon-first, definition merely pointed at):

> By WH-FORM, β is a valid cocycle; see D2.

**Good** (descriptive name first, definition restated, ids relegated to
provenance):

> *The polarizing cocycle of a symplectic space over a finite field.*
> Fix a finite field `κ` and its symplectic space `V(κ) = κ ⊕ κ` with
> alternating form `ω`. The polarizing cocycle is the `κ`-bilinear map
> `β : V(κ) × V(κ) → κ` with `β(v,v') − β(v',v) = ω(v,v')` for all `v,v'`.
> [... statement, proof or sketch, scope block ...]
> `\provenance{D2, WH-FORM}{theory/wh-kappa.md}{theory/checks/wh_kappa_check.py}{theory/verdicts/wh-kappa-r1.md}`

## Checklist before a section lands

- [ ] Every definition/result has a descriptive English name; no campaign id
      appears outside a `\provenance` block.
- [ ] No `verbatim`/`lstlisting`/`alltt`/`minted` anywhere in the file.
- [ ] Every equation is real LaTeX math; no markdown syntax survives.
- [ ] Every statement's hypotheses are stated in full; a `scope` block
      follows every statement.
- [ ] Every definition used is restated in full, matching `definitions.md`.
- [ ] Every status label matches the current `claims/CLAIMS.md` row exactly.
- [ ] `scripts/check-labbook.sh` exits 0 and `cd labbook && latexmk -pdf
      main.tex` still exits 0.
