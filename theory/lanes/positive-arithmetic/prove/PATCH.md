# Positive arithmetic prover integration instructions

This lane performed one prover pass only. All six positive claims remain
SKETCH until the one blind review, one repair wave and root adjudication.
The lane changed no trunk files or git state. Native inherited runtime,
no model overrides, nested CLI or nested agents.

## Copy targets

- `reference-and-protocol.md` ->
  `theory/sidequests/positive-arithmetic/reference-and-protocol.md`.
- `finite-operational-boundary.md` ->
  `theory/sidequests/positive-arithmetic/finite-operational-boundary.md`.
- `labbook-draft.tex` ->
  `labbook/sections/sidequest_positive_arithmetic_reference.tex`.

Replace the shards' definition-source string `DEFINITIONS-PROPOSED.md`
with `../../../definitions.md` when integrated. Do not copy the standalone
compile wrapper or its build products into labbook. They validate the
self-contained section against the shared existing preamble.

## Registry string anchors

In `definitions.md`, append the seven numbered definition blocks of
`DEFINITIONS-PROPOSED.md` after the exact final D1441 sentence
`the negation action is identity at p=2.`. Omit the lane draft preface.
D1508--D1519 are unallocated.

In `notation.md`, append the table from `NOTATION-PROPOSED.md` after the
table containing the unique row beginning
`| \`Gamma_r^sgn, A_d^sgn, B_d^sgn, J_2(m)\` |`.
Keep J_k(d) distinct from J_i and B_E distinct from the prior B_i.

In `claims/CLAIMS.md`, append a topic heading
`## Positive arithmetic references and finite operational profiles — 2026-09-09`
after the full table containing the unique row beginning `| \`MIX-ALL\` |`.
Copy all six rows from `CLAIMS-PROPOSED.md`, adjusting proof/checker paths
to their integrated locations. Keep their statuses at SKETCH until root's
adjudication; these rows do not promote or settle MIX-ALL.

## Labbook string anchor

After `\input{sections/sidequest_arithmetic_limit_conjectures}` in
`labbook/main.tex`, add

    \input{sections/sidequest_positive_arithmetic_reference}

The section label is `sec:positive-arithmetic-reference`. Its six
`\statusSketch` occurrences correspond one-to-one to the six positive
claim rows. If promoted, change registry and labbook together, replace
the opening pending-review sentence, and give actual adjudication paths
in place of `pending` provenance. Every definition/result has a scope block.

## Evidence and scope to retain

The independent check lane owns `positive_arithmetic_check.py`,
`EXPECTATIONS.md`, red-first mutation outputs and the frozen results.
`CHECKER-REQUIREMENTS.md` here is the early interface, not duplicate evidence.
The verifier reported exact mixed-protocol success on
F4/F2,F8/F2,F16/F4,F9/F3,F27/F3,F25/F5, including actual Fourier phases,
and exact finite-profile tests through grade six on up to three references.
Use its final summary for the definitive mutation count and filenames.

In HANDOFF's current-state paragraph record the new positive nontracial
reference, finite sufficient profile, all-degree tower restrictions and
the uniform mixed protocol. Retain the scope distinctions: fixed actual p,
copied versus independent references, transported versus reset coordinate
references, state deformation versus MIX angle deformation, and leading
operational adequacy versus equality of all finite-h probabilities.

The positive-series category is an exact family envelope. The finite
profile is a substantive bounded sufficient statistic for all fixed future
CP branches and finite generated protocols; leading normalization alone
is not functorial under rare postselection. No characteristic-free category
or automatic identification with earlier angle limits is asserted.

Root runs the ordinary session-close and review/adjudication gates after
integration. No active-goal completion is authorized by this lane's summary.
