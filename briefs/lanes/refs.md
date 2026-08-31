LANE: refs | WRITE SCOPE: refs/** only
Read briefs/lanes/RULES.md, then CLAUDE.md (esp. L3, L12) and PRD.md, then
briefs/wh-kappa-target.md.

TASK: make the first increment's mathematics citable. Under L3, no statement in
this repo may be justified from memory — standard textbook material included.
The target brief needs local sources for, at minimum:

- the finite / finite-abelian-group Stone–von Neumann theorem (uniqueness of the
  irreducible representation with a fixed nontrivial central character);
- Heisenberg groups over finite fields and their twisted group algebras
  (central simplicity, dimension `q²`, the `M_q(C)` identification);
- the Weil / metaplectic representation over a finite field, including whatever
  the source actually says about characteristic 2 and about when the projective
  representation linearises;
- additive characters of finite fields and the absolute trace pairing
  (`ψ_ζ = ζ^{Tr}`, the `κ^×`-torsor structure of nontrivial characters).

METHOD:
- Prefer arXiv e-print TeX sources: `https://arxiv.org/e-print/<id>` gives the
  source bundle; fall back to the abs page only for metadata. Store each under
  `refs/arxiv-<id>/`.
- `v0.1/references/heisenberg_weil/SOURCES.md` and
  `v0.1/references/symplectic_qecc/SOURCES.md` list papers a previous campaign
  registered. Under L12 they are POINTERS ONLY: you may use them to learn which
  arXiv ids are worth fetching, and you must re-fetch and re-verify each one
  yourself. Do not copy their bibliographic assertions.
- **Verify every id against the title extracted from the fetched source
  itself.** A mismatch is recorded in the ledger, not silently fixed.
- Compute a SHA256 for each fetched bundle.

DELIVERABLE: `refs/LEDGER.md` — a table with arXiv id (or other route),
title as verified from the source, the main TeX file, retrieval date, SHA256,
and the role it plays for this campaign. Head the file with a ROLE comment
saying that a quotation anywhere in the repo must trace to a file under
`refs/`. Where a needed source could NOT be obtained, record the gap
explicitly as a row with role `GAP — needed for <what>`; an honest gap is the
required output, a plausible-looking citation is a FATAL error.

Note: source bodies are not committed (the scaffold lane gitignores them);
`refs/LEDGER.md` is. Report in SUMMARY.md exactly which bundles are present on
disk in this container and which are gaps.
