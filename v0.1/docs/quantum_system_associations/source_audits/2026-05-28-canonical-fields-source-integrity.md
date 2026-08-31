# 2026-05-28 canonical-fields source-integrity audit

Scope: blocker `aqm-qsa-src01` initially, then follow-up
`aqm-qsa-src04` for the remaining Cahill--Glauber chain. The initial pass was
restricted to `references/canonical_fields/` plus this audit note. The
follow-up migrated active Cahill--Glauber locators in report shards `AQM-20`
and `AQM-21` to a lawful official arXiv source artifact. Report maps were not
edited.

## Restored artifacts

The following files were missing at session start and were restored from
official arXiv e-print routes. The restored SHA256 hashes match the preexisting
manifest hashes in `references/canonical_fields/SOURCES.md`.

| Key | Restored local artifacts | Official route | SHA256 |
|---|---|---|---|
| `derezinski-ccr-car-2005` | `references/canonical_fields/derezinski_math_ph_0511030_source.tar`; `references/canonical_fields/derezinski_math_ph_0511030_source/derezinski.tex`; `references/canonical_fields/derezinski_math_ph_0511030_source/svmult.cls` | `https://arxiv.org/e-print/math-ph/0511030v2` | `739bee04644cdd516bb56b011803e845ebce4a7064c6ae6bbb90d7618d6e7c29` |
| `bekka-stone-von-neumann-2025` | `references/canonical_fields/bekka_2502_00387_source.tar`; `references/canonical_fields/bekka_2502_00387_source/CCR-GeneralRings-v5.tex` | `https://arxiv.org/e-print/2502.00387v1` | `c0515c59a93bb8c7a609dd0bf49b5d07f807cafdc5b8b821a20286d92cdf7413` |
| `keyl-schlingemann-gar-2009` | `references/canonical_fields/keyl_schlingemann_0906_2929_source.tar`; `references/canonical_fields/keyl_schlingemann_0906_2929_source/fidelity_arXiv.tex` | `https://arxiv.org/e-print/0906.2929v1` | `9fc5c0ee71fb2a0175e80fd36b86ceb471ff979142d2c3628bdaa9e251450f52` |
| `bravyi-flo-lagrangian-2004` | `references/canonical_fields/bravyi_quant_ph_0404180_source.tar`; `references/canonical_fields/bravyi_quant_ph_0404180_source/v2.tex` | `https://arxiv.org/e-print/quant-ph/0404180v2` | `25fdbb88a947ca27ea2fa9f41f2c85a86cfce6d8933fe6a9157acde6f584b840` |

## Cahill--Glauber follow-up

The exact recorded Cahill--Glauber APS/marker chain remains unavailable, but
it is no longer an active report-locator blocker. Automated official APS/DOI
retrieval was retried on 2026-05-28 with a browser-style user agent and still
returned HTTP 403. The active source chain was migrated to the official arXiv
`physics/9808029v1` e-print source.

Stored fallback artifacts:

| Local artifact | Official route | SHA256 |
|---|---|---|
| `references/canonical_fields/cahill_glauber_physics_9808029v1_source.tex.gz` | `https://arxiv.org/e-print/physics/9808029v1` | `a7cebc6a28ed2b78e73a778c27b14720ee89a117779bdf4c22bbc72b869cb402` |
| `references/canonical_fields/cahill_glauber_physics_9808029v1_source/fxxx.tex` | extracted from the official arXiv e-print source | `221e579194d960dd8c177014073114747878d016601c8fc042cddbc9e28469f3` |

Active TeX locators now recorded in `references/canonical_fields/SOURCES.md`:
`fxxx.tex:323-335`, `fxxx.tex:337-365`, `fxxx.tex:603-643`,
`fxxx.tex:367-390`, `fxxx.tex:391-414`, `fxxx.tex:416-464`,
`fxxx.tex:815-833`, and `fxxx.tex:835-854`.

Historical unavailable artifacts retained for provenance:

| Missing artifact | Manifest evidence |
|---|---|
| `references/canonical_fields/PhysRevA.59.1538.pdf` | Recorded PDF hash: `cd093edeecac3107a236e9f066e606eb076f24256931fa1d9023412587794dcd` |
| `references/canonical_fields/physrevA_59_1538_marker/PhysRevA.59.1538/PhysRevA.59.1538.md` | Recorded marker Markdown hash: `5e1c1c47fb9a97d22f1333ccb3a49921e92414377a51fe88c8c4f5013d483197` |
| `references/canonical_fields/physrevA_59_1538_marker/PhysRevA.59.1538/metadata.json` | Path inferred from the marker-output layout; recorded marker metadata hash: `648026a99f88461209d74cf4942f6f37adbebdc26f3cab818f3d2cc3bc99444f` |

Official routes checked:

| Route | Result |
|---|---|
| `https://doi.org/10.1103/PhysRevA.59.1538` | Official DOI route identified. |
| `https://link.aps.org/doi/10.1103/PhysRevA.59.1538` | Automated `curl --head` returned HTTP 403 in this environment. |
| `https://journals.aps.org/pra/pdf/10.1103/PhysRevA.59.1538` | Automated `curl --head` returned HTTP 403 in this environment. |
| `https://arxiv.org/abs/physics/9808029` | Official arXiv record reachable; it names the same title/authors and related DOI. |
| `https://arxiv.org/pdf/physics/9808029v1` | Reachable, but temporary hash check produced `9d51289336395f6991f37fe834e866c6fdfb7d1dc73421eaa9f98f0cbc5e2f86`, not the recorded APS PDF hash. Not stored because the TeX source is available. |
| `https://arxiv.org/e-print/physics/9808029v1` | Reachable and stored as the active source artifact for `AQM-20` and `AQM-21`; SHA256 `a7cebc6a28ed2b78e73a778c27b14720ee89a117779bdf4c22bbc72b869cb402`. |

Conclusion: the exact recorded Cahill--Glauber PDF and marker extraction were
not restored. The active report citations were lawfully migrated to official
arXiv source locators. The old APS PDF and marker hashes remain useful only if
a future browser or institutional-access pass tries to restore the historical
artifact chain exactly.

`marker_single` was not available on `PATH` during this audit; `pdftotext` was
available. Regenerating the existing marker Markdown therefore needs either a
local marker installation or a decision to replace marker line locators with
locators from a different lawful extraction.

## Recommended closeout

`aqm-qsa-src04` can close on the migration path: `AQM-20` and `AQM-21` no
longer depend on the missing marker extraction. If `aqm-qsa-src01` was scoped
to restoring or replacing missing active canonical-field source chains, it can
also close. A future task is needed only if the project specifically wants to
restore the historical APS PDF/marker chain in addition to the official arXiv
source chain.
