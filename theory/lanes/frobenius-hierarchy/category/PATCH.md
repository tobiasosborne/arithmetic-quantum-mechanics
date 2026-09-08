# Root integration patch proposal

Only root applies these changes. This lane has written only its declared
category directory and has not staged, committed, or changed trunk files.

1. At the end of `definitions.md`, after the existing final definition and
   the algebra lane's D1301--D1310 block, append exactly the D1321--D1327
   definition bodies from DEFINITIONS-PROPOSED.md. Do not copy the lane-status
   preamble. D1311--D1319 and D1328--D1339 remain unallocated in this proposal.
2. At the end of `notation.md`, append the notation table from
   NOTATION-PROPOSED.md. The explicitly scoped symbols coexist with the
   older Hecke notation; shared finite-field symbols remain the algebra
   lane's single proposal.
3. Append the FRP-CAT, FRP-CP and FRP-DESCENT rows in CLAIMS-PROPOSED.md to
   `claims/CLAIMS.md`. They are SKETCH proposals until the one hostile
   review/repair/root adjudication. Change status only as adjudicated.
   Replace proof paths beginning `category/` with the installed path below.
   Use the checker's actual gate names, especially A7-types, A7-CP,
   A7-tower, A7-parallel and A7-Fourier; A7-PREP is a requested small final
   extension for the explicit discard primitive, not yet certified here.
4. Install the two 200--500-line Lamport shards `amplitude-category.md` and
   `process-category.md` under `theory/sidequests/frobenius-hierarchy/` or a
   root-chosen common campaign directory. Resolve relative references to the
   installed companion shard. Definitions then refer to trunk D1321--D1327,
   replacing the lane-definition preamble with the installed registry path.
5. Copy `labbook-draft.tex` to a new owning section, for example
   `labbook/sections/26_arithmetic_processes.tex` if that name is free. Add
   its input after the algebra campaign section in `labbook/main.tex`.
   The source-string anchor is `\\end{document}`: insert both new inputs
   before it in the desired campaign order, without copying the temporary
   `review-build.tex` wrapper. Replace the human-readable proof/checker
   provenance locators with installed paths and the final review locator.
   Keep all three status macros aligned with the adjudicated registry rows.
6. Keep ENDPOINT-NEXT.md as the named next-stage proposal in the campaign
   directory. It does not add an admitted claim or specialization definition.
   Its independent incidence/phase parameters, coupled constraints, type-C
   correspondence, trace boundary and six exact witnesses are substantive
   next-stage data. Cite its durable path from the new HANDOFF section.
7. CHECKER-REQUIREMENTS.md is the preregistered operational interface sent to
   the checker lane; preserve it beside the checker's frozen expectations.
   No category-owned checker is proposed, because A7 already owns these
   independent computations. The standalone TeX wrapper and its generated
   files are local review artifacts, not product source.

Validation already performed: standalone pdflatex build using the actual
labbook preamble, producing a six-page review PDF. Full lockstep/build and
complete green/red session-close runs belong to root after integration.

Native model convention on every proposal: inherited native Codex runtime,
no override or nested CLI, with exact model identifier unavailable to the lane.
