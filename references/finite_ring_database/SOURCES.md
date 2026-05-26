# SOURCES.md - finite commutative ring database

Topic: finite commutative unital ring catalogues, finite-ring enumeration and
isomorphism methods, and software sources for a reproducible ring database.

Retrieval date for this manifest: 2026-05-26.

## Local Sources

### Andrzej Nowicki, Tables of finite commutative local rings of small orders

- Bibliographic key: Nowicki 2018, "Tables of finite commutative local rings
  of small orders", version `tab-05`, dated 2018-08-08.
- Access route: archived author PDF. The original URL
  `https://www-users.mat.umk.pl/~anow/ps-dvi/tab-05w.pdf` returned HTTP 404 on
  2026-05-26; the archived copy was retrieved from
  `https://web.archive.org/web/20211020012605/https://www-users.mat.umk.pl//~anow/ps-dvi/tab-05w.pdf`.
- Local file:
  `references/finite_ring_database/nowicki_tables_wayback_20211020.pdf`
  (ignored by git as a third-party PDF).
- SHA256:
  `68dc427701e624ab214ddafa3e6d4218326c41abbe8533ac3b48d68744a2a61b`
- Local anchors:
  - Page 1 states that all rings in the table are commutative with unity.
  - Page 1 states that finite rings are finite products of finite local rings
    and that finite local ring orders are prime powers.
  - The tables list local ring presentations for selected orders `p^n`.
- Notes:
  License terms were not found in the file. Treat this as a source for
  provenance and manual verification. Do not bulk-import table rows into a
  redistributed database until licensing and transcription policy are recorded.

### Behboodi--Beyranvand--Hashemi--Khabazian, Classification of finite rings

- Bibliographic key: Behboodi--Beyranvand--Hashemi--Khabazian 2014,
  "Classification of finite rings: theory and algorithm".
- Venue: Czechoslovak Mathematical Journal 64 (2014), no. 3, 641-658.
- DOI/URL: DOI `10.1007/s10587-014-0124-7`; DML persistent URL
  `https://dml.cz/handle/10338.dmlcz/144050`.
- Local files:
  `references/finite_ring_database/dml_behboodi_finite_rings_article.html`;
  `references/finite_ring_database/dml_behboodi_finite_rings.pdf`
  (PDF ignored by git as a third-party PDF).
- SHA256:
  - HTML:
    `226a73ced0608e5288fc0983a33d64702a3f3e6d526b6b690be8dadad17e4c72`
  - PDF:
    `f6102cdaf26fa0056cc74cc9a5d47887c38a0237fb59df131b775312b7c8453a`
- Local anchors:
  - HTML lines 47-49 give title, keywords, and abstract metadata.
  - HTML line 182 states the abstract: classification up to isomorphism,
    quasi bases, structure and isomorphism theorems, and an algorithm.
  - PDF pages 641-644 introduce the problem, finite-ring decompositions,
    quasi bases, and structure-constant presentations.
- Notes:
  The DML PDF states personal-use access terms on page 1. Use the HTML
  metadata and local PDF only for source-grounded planning and verification.

### Blackburn--McLean, The enumeration of finite rings

- Bibliographic key: Blackburn--McLean 2021/2022, "The enumeration of finite
  rings", arXiv:2107.13215v2.
- DOI/arXiv/URL: arXiv `2107.13215`, DOI `10.48550/arXiv.2107.13215`.
- Local files:
  `references/finite_ring_database/blackburn_mclean_enumeration_finite_rings_2107.13215_abs.html`;
  `references/finite_ring_database/blackburn_mclean_enumeration_finite_rings_2107.13215_source.tex.gz`;
  extracted TeX at
  `references/finite_ring_database/blackburn_mclean_enumeration_finite_rings_2107_13215_source/enumerating-finite-rings_revised_submission.tex`.
- SHA256:
  - HTML:
    `89af3f451fbc32c42a18b79178f4797e8a388d116b4b8b700726436fb1aa5b65`
  - Source gzip:
    `e2769196871d4a4197dec2756e227029c548e4b64a6a07ff6656402ceacbe179`
  - Extracted TeX:
    `9d328c2ab5e152065bc5057ea1f9865dff9eb70ea3270f213132580f5e50fa2b`
- Local anchors:
  - HTML lines 172-180 give version, title, authors, and abstract.
  - TeX line 35 states the finite-ring and finite commutative-ring asymptotic
    enumeration results and the proof issue in earlier arguments.
  - TeX lines 65-71 state that corresponding statements hold for rings with
    identity and for commutative rings with identity.
  - TeX lines 666-689 state the commutative and commutative-with-identity
    enumeration theorem statements.
  - TeX lines 698-711 record counterexamples to a reduction of ring
    enumeration to finite-field algebra enumeration.

### Alabiad--Alkhamees, finite commutative chain rings

- Bibliographic key: Alabiad--Alkhamees 2022, "On classification of finite
  commutative chain rings".
- Venue: AIMS Mathematics 7(2), 1742-1757.
- DOI/URL: DOI `10.3934/math.2022100`;
  `https://www.aimspress.com/article/doi/10.3934/math.2022100`.
- Local file:
  `references/finite_ring_database/aims_alabiad_alkhamees_chain_rings.html`.
- SHA256:
  `6733b7bd5442d60a574868ae663990198f9e9084bc2ed78456460ab563034b97`
- Local anchors:
  - HTML lines 34-37 identify title and authors.
  - HTML lines 52-55 and 574 summarize finite commutative chain-ring
    classification by invariants and Eisenstein-polynomial data.

### GAP reference manual, rings

- Bibliographic key: GAP Reference Manual, Chapter 56, "Rings".
- Access route: official GAP documentation,
  `https://docs.gap-system.org/doc/ref/chap56_mj.html`.
- Local file:
  `references/finite_ring_database/gap_rings_chapter_56.html`.
- SHA256:
  `dda62a5baf9f9c141b9438f111377cfe728a222c793da2b09d9a5114937d88e7`
- Local anchors:
  - Lines 145 and 472-474 distinguish `IsRingWithOne`.
  - Lines 1012-1034 document `RingHomomorphismByImages` and
    `NaturalHomomorphismByIdeal`.
  - Lines 1041-1071 document the small-rings library, `SmallRing`, and
    `NumberSmallRings`.
  - Lines 1115-1131 document `DirectSum` and `RingByStructureConstants`.

### GAP reference manual, character tables

- Bibliographic key: GAP Reference Manual, Chapter 71, "Character Tables".
- Access route: official GAP documentation,
  `https://gap-system.github.io/gap/doc/ref/chap71_mj.html`.
- Local file:
  `references/finite_ring_database/gap_character_tables_chapter_71.html`.
- SHA256:
  `b75bfa15c938d64a31a99ff6090552159a358e17c9a5347636af5fd7753e26b6`
- Local anchors:
  Used as a prospective source for additive-character computations in GAP.
  Record exact method locators before relying on a specific character-table
  algorithm in implementation.

### SageMath finite rings and quotient rings

- Bibliographic key: SageMath Reference Manual, finite rings and quotient
  rings.
- Access routes:
  - `https://doc.sagemath.org/html/en/reference/finite_rings/index.html`
  - `https://doc.sagemath.org/html/en/reference/rings/sage/rings/quotient_ring.html`
- Local files:
  - `references/finite_ring_database/sage_finite_rings_index.html`
  - `references/finite_ring_database/sage_quotient_ring.html`
- SHA256:
  - Finite rings index:
    `508b046f8479b6d928b0950182c7de2ef441bb50cc9eb88ad6ea9a156320b373`
  - Quotient ring:
    `e5e11fe76fe545c8145286d37db4e94bfb65e51419e0b7843f523a46ffac267f`
- Local anchors:
  - Finite rings index lines 304-309 list the finite-rings section and
    `ZZ/nZZ` finite rings.
  - Quotient-ring page lines 518-543 document `QuotientRing(R,I,...)`.
  - Quotient-ring page lines 2073-2088 list basic quotient-ring methods such
    as `characteristic`, `defining_ideal`, `gens`, and `random_element`.

### OSCAR commutative algebra documentation

- Bibliographic key: OSCAR documentation, commutative algebra.
- Access routes:
  - `https://docs.oscar-system.org/v1/CommutativeAlgebra/intro/`
  - `https://docs.oscar-system.org/dev/CommutativeAlgebra/ideals/`
  - `https://docs.oscar-system.org/stable/CommutativeAlgebra/ModulesOverMultivariateRings/intro/`
- Local files:
  - `references/finite_ring_database/oscar_commutative_algebra_intro.html`
  - `references/finite_ring_database/oscar_ideals.html`
  - `references/finite_ring_database/oscar_modules_over_multivariate_rings_intro.html`
- SHA256:
  - Intro:
    `a1fedecdafcd6ecd14d42279767140047326c91cb8be9bc3555aef24cade7450`
  - Ideals:
    `4604753718f3ab3c098c269b941322715592da1f6b82c62ff1a6ec19004de8a0`
  - Modules:
    `351f5a32c1259a280ea542950cac60fc0a4b6b6e431ac530055fba30ba6aa075`
- Local anchors:
  The snapshots are minified single-line Documenter pages. Use the page titles
  and documented sections for polynomial rings, ideals, quotient rings or
  affine algebras, and modules over multivariate rings. Before implementation,
  pin exact OSCAR version and source-line anchors from the installed docs or
  package source.

### Nemo residue rings

- Bibliographic key: Nemo.jl documentation, "Residue rings".
- Access route: `https://nemocas.github.io/Nemo.jl/latest/residue/`.
- Local file:
  `references/finite_ring_database/nemo_residue_rings.html`.
- SHA256:
  `1a1b645d0e31e5124bbca2ea0290279eaa2197658ea90c81d738cf3ba8f38127`
- Local anchors:
  Line 2 is a minified page containing the residue-ring section. It states
  that Nemo can create residue rings `R/(a)` for an element `a`, including
  optimized `ZZ/nZZ` residue types backed by FLINT.

### FLINT modular matrix documentation

- Bibliographic key: FLINT documentation, `fmpz_mod_mat.h`.
- Access route: `https://flintlib.org/doc/fmpz_mod_mat.html`.
- Local file:
  `references/finite_ring_database/flint_fmpz_mod_mat.html`.
- SHA256:
  `3516ed73d0d95063bf80252bf346f7d90d7ddace7cc0267df97b57d9a546a124`
- Local anchors:
  - Lines 409, 443, 466, 481, 493, 506, 517, 534, and 555 mark functions
    whose modulus is assumed to be prime.
  - Lines 414-429 document strong echelon form and Howell form over
    integers modulo `n`.

### SQLite about page

- Bibliographic key: SQLite About SQLite.
- Access route: `https://www.sqlite.org/about.html`.
- Local file:
  `references/finite_ring_database/sqlite_about.html`.
- SHA256:
  `4b99169565af75a3e637a2cba19c1a3f59ab770444239931c969f94ab218357e`
- Local anchors:
  - Lines 144-146 describe SQLite as self-contained, serverless, and
    zero-configuration.
  - Line 160 states that a database with tables, indexes, triggers, and views
    is contained in a single disk file.

## Source Gaps

- OEIS count sequences for finite rings were identified as possible secondary
  count checks, but no OEIS snapshot is registered yet.
- Magma documentation was identified as an optional proprietary oracle path,
  but no local Magma source snapshot is registered yet.
- McDonald, Bini--Flamini, Ganske--McDonald, and several small-order
  classification papers are not yet acquired. Do not use them for database
  rows or completeness claims until local sources and access terms are
  registered.
