# Integration patch: Galois embedding registers

All changes below are instructions to the root. This lane makes no trunk
edits and no git actions. Use string anchors, never line numbers.

1. In `definitions.md`, locate the unique concluding string
   `labels, and Fourier-transported nonfixed labels are not identified.`
   at the end of D1334. Append the D1401--D1405 sections from
   DEFINITIONS-PROPOSED.md after that section. If root has already appended
   another lane's definitions, append these five once in the chosen numeric
   ordering without modifying either lane's definitions. D1406--D1409 stay unused.

2. In `notation.md`, locate the table row beginning
   `| \`P_(E,d)^nz, tau_(E,d), v_(E,d), tau_(E,d)^nz, P_A^nz, P_r^dual\` |`.
   Insert NOTATION-PROPOSED.md's table after that table, retaining explicit
   `emb` superscripts to distinguish the cardinality registers. S_d retains
   D1331's existing global meaning; do not add a conflicting symbol row.

3. In `claims/CLAIMS.md`, locate the unique row beginning `| \`FRL-ACTIVE\` |`.
   After that section append a section named
   `## Galois embedding registers — 2026-09-09` and the three proposed rows.
   Replace short proof paths by the permanent shard paths below and resolve
   the checker path to `theory/checks/arithmetic_limits_check.py` at integration.
   The rows stay SKETCH unless root's capped adjudication admits them; all
   eventual status changes must also update the corresponding labbook macros.

4. Copy `embedding-functor.md` and `galois-image-orbits.md` to
   `theory/sidequests/arithmetic-limits/` with those names. Their definition
   reference header must then point to the single-source `definitions.md`,
   not to this lane. Add root's actual review/adjudication locator in their
   header after the capped review; retain the scope statements and provenance.

5. Copy `labbook-draft.tex` to
   `labbook/sections/sidequest_galois_embedding_registers.tex`.
   In `labbook/main.tex`, after the unique anchor
   `\input{sections/sidequest_frobenius_boundary}` insert
   `\input{sections/sidequest_galois_embedding_registers}`.
   The draft already names the permanent proof/checker paths. Replace
   provenance's `pending` with the actual verdict/adjudication file after
   review. The opening sentence about awaiting review must then be updated.
   Add an overview row/paragraph if required by root's combined integration.

6. Source bodies and LEDGER registration are root-owned and already fetched.
   Exact new locators used: Milne FT v5.10 Theorem 6.10, Proposition 8.6,
   Corollary 8.7, Proposition 8.9, Corollary 8.10, Proposition 8.20,
   Theorem 8.21, Remark 3.18, Propositions 4.19--4.20, Corollary 4.21,
   Proposition 4.23; Stacks 04JI Lemma 58.2.2 (03QR), and 0BMI
   Lemmas 9.22.1--9.22.3/Theorem 9.22.4. Root's LEDGER entry should
   include these locators rather than only a generic source title.

7. Preserve the check lane's independent G1--G3 preregistration, green and
   named red outputs, especially the nonuniform-fibre and full-history
   coherence tests. The lane-specific checker requirements here are the
   formula interface, not an assertion that the checker has already passed.
   Run root's lockstep/PDF/session-close checks after integration.

No existing claim is strengthened by this patch. The new Galois system has
dimension dim_K(A), not the cardinality of A. It does not identify the
primitive orbit comparison with D1304's J/V or D1333's divisor-block maps.
