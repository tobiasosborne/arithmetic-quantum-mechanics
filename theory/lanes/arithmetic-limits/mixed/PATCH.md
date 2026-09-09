# Mixed lane integration patch

One prover pass is complete. All three positive rows remain SKETCH until
the root's one blind critic round, one repair wave and adjudication.
MIX-ALL remains CONJECTURE independently of the positive rows' outcome.
The lane has changed no trunk file and made no commit.

## Files to copy

- Copy `gram-and-chart.md` to
  `theory/sidequests/frobenius-hierarchy/gram-and-chart.md`.
- Copy `coherent-towers.md` to
  `theory/sidequests/frobenius-hierarchy/coherent-towers.md`.
- Copy `labbook-draft.tex` to
  `labbook/sections/sidequest_arithmetic_fourier_charts.tex`.
- Do not copy `compile-draft.tex` or its build products into the labbook;
  the wrapper only validates this self-contained section with the shared
  preamble. The section compiled to seven pages with pdflatex.

In the theory copies replace the draft definition-source string
`DEFINITIONS-PROPOSED.md` by `../../../definitions.md`. Preserve named
computation labels and structured step numbers for the blind review.
Update the opening status only after adjudication.

## Definition registry anchor

In `definitions.md`, insert all definition blocks starting at the exact
anchor `## D1421 (joint arithmetic code and Gram datum)` in this lane's
`DEFINITIONS-PROPOSED.md`, through the end of D1428, before the trunk
anchor `## D1441 (signed Frobenius orbit count candidates)`.
Do not insert the lane preface. D1429 remains unallocated.
This leaves the separate Galois reservation D1401--D1409 untouched.

## Notation registry anchor

In `notation.md`, insert the table in `NOTATION-PROPOSED.md` immediately
before the table containing the unique row beginning
`| \`Gamma_r^sgn, A_d^sgn, B_d^sgn, J_2(m)\` |`.
The plain symbol `T_i` remains the D1303 relative trace; `mathcal T_i`
is the new orthogonal frame. The cardinality Q is never reused as a
projection symbol. Retain the clarification paragraph if useful.

## Claims registry anchor

In `claims/CLAIMS.md`, insert a new topic heading and the four proposed
rows from `CLAIMS-PROPOSED.md` before the exact anchor
`## Signed arithmetic orbit refinement — 2026-09-09`.
Use full integrated proof/checker paths. The checker gates are F1,F2 for
MIX-GRAM; F2,R1,R2 for MIX-CHART; F3,R3 for MIX-TOWER. The independent
checker has no gates called T1 or T2. M1 is a necessary finite-fibre
diagnostic for MIX-ALL, never a verification of the open existence claim.
Replace the descriptive Galois dependency of MIX-ALL with the precise
admitted GAL claim IDs when those are settled.

## Labbook entry anchor

In `labbook/main.tex`, add

    \input{sections/sidequest_arithmetic_fourier_charts}

after the exact anchor
`\input{sections/sidequest_frobenius_boundary}` and after the new Galois
section if root chooses that sequence. The new section's label is
`sec:arithmetic-fourier-charts`.
After review, update its three `\statusSketch` labels and all corresponding
registry rows in lockstep only as the adjudication permits; leave its
`\statusConjecture` unchanged. Replace `pending` provenance entries with
the actual adjudication reference. Update the opening review sentence.

## Evidence and live-state anchors

The independent verifier owns checker integration and frozen outputs; see
`../check/SUMMARY.md`, `../check/EXPECTATIONS.md`, `../check/results.json`
and `../check/CLI-RESULTS.json`. No duplicate checker was written here.
The independent results cover the actual F81 tower and characteristic-three
singular residual reflection as well as the initial five embeddings.

In HANDOFF, use the new live-state paragraph after its top `Updated:`
record, not a second historical narrative. Record the three branch scopes,
the all-length invertible-degree connector, the retained logical Fourier
factor, and the open all-characteristic tower/multiplication construction.
The early unconditioned trace stress has one mathematical home in
gram-and-chart.md, section 5; it is not a new negative campaign.

Run root's required lockstep/PDF/checker gates after integration. The
lane's passing build and the verifier's finite results do not authorize
PROVED promotion without the capped review.
