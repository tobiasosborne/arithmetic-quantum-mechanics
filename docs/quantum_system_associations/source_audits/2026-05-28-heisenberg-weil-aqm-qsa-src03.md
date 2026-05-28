# aqm-qsa-src03 Heisenberg-Weil Source Audit

Date: 2026-05-28.

Scope:
`references/heisenberg_weil/SOURCES.md` and local artifacts named there.

Initial state:

- `references/heisenberg_weil/` contained only `SOURCES.md`.
- Every local archive, extracted TeX file, and PDF named in the manifest was
  missing.

Reacquisition result:

- Restored the eleven arXiv source archives from official
  `https://arxiv.org/e-print/<id>` endpoints.
- Restored the two author PDFs from the URLs recorded in the manifest.
- Restored all extracted TeX paths named in the manifest from the downloaded
  source archives.
- The restored archive/PDF SHA256 values matched the SHA256 values already
  recorded in `references/heisenberg_weil/SOURCES.md`.

Remaining source-integrity state:

- No manifest-named local source artifact remains missing after restoration.
- `references/**/*.pdf` is ignored by `.gitignore`, so the two restored PDFs
  require force-add handling if the orchestrator wants them committed.
- Extracted `.bbl` files from two arXiv bundles are also ignored by the
  repository ignore rules; they are not named in the manifest.
