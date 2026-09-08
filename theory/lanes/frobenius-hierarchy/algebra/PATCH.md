# Root integration patch

Apply only after the capped review, one repair wave and root adjudication.
No lane file is independently admitted by this proposal.

1. In `definitions.md`, after the existing final definition whose heading
   is `## D1266`, append the definition bodies headed `## D1301` through
   `## D1310` from `DEFINITIONS-PROPOSED.md`. The category lane owns its
   separate D1321--D1339 reservation. D1311--D1319 remain unassigned.
   The anchor is the entire final D1266 block, not its line number; if
   another lane has appended definitions, append after those instead.
2. In `notation.md`, append the table from `NOTATION-PROPOSED.md` after the
   existing row beginning `| B_X, j_(X,Y)` (including its code delimiters).
   Existing symbols retain their existing context-dependent meanings.
3. In `claims/CLAIMS.md`, append the seven FRB rows from
   `CLAIMS-PROPOSED.md` beneath the existing claim table. Replace SKETCH
   only for claims the root adjudication actually promotes.
4. Install `foundation.md`, `transfers-example.md`, and `hierarchy.md`
   under `theory/sidequests/frobenius-hierarchy/` with the same filenames.
   Replace the prefix `theory/lanes/frobenius-hierarchy/algebra/` by that
   destination prefix in the claim rows and labbook provenance.
5. The checker lane proposes installing its standalone checker as
   `theory/checks/frobenius_hierarchy_check.py`. Once installed, replace
   `theory/lanes/frobenius-hierarchy/check/standalone_frobenius_hierarchy_check.py`
   in the claim rows by that existing installed path. Replace the labbook's
   prose check locators by the same path plus their advertised gate IDs.
6. Install `labbook-draft.tex` as
   `labbook/sections/sidequest_frobenius_hierarchy_algebra.tex` and add its
   input before the category lane's new arithmetic process section in
   `labbook/main.tex`. Anchor at the final existing section input; preserve
   all older inputs. Every proposed definition is fully restated and all
   results currently use `statusSketch`; promotion must update the matching
   status macros and pending-review provenance in the same edit.
7. Sources are already registered by root. The proof reads CGK17 p. 2
   equations (3)--(6) for the global-phase hierarchy convention; its
   classification theorem is not used. AND24 p. 2 supplies the composition
   boundary. ST-TRACE 0BIJ/0BIL corroborate the internally derived trace facts.

Validation requested of root: checker green and all named reds nonzero;
read-gate and labbook lockstep checks; real final PDF build; only then
adjudication/status publication according to the campaign brief.
