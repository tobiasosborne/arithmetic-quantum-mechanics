# Single SP-STAB-REL repair wave

Date: 2026-09-10.  Repair model: `gpt-5.6-sol`, reasoning `xhigh`.

This is the sole repair requested by the valid blind verdict at
`theory/lanes/phantasm-stabilizer/blind-critic/VERDICT.md`.  It addresses its
one MINOR objection and changes no other proof, statement, hypothesis,
definition, dependency or scope.

In `equivalence.md` section 2 `<1>14`, for every rank `j>=1` define `e_j` as
the tensor of `j` D1704 computational zero preparations and set
`e_0=1_C`.  D1704 contains `e_j`, `e_j^*`, and the scalar `0:C->C`, hence it
contains

    e_n o (0:C->C) o e_m^*:H_(F_p,m)->H_(F_p,n).

This composite is the typed zero linear map because it factors through the
zero scalar, and D1715 prescribes it as the sole member of `E_p(empty)`.
The same construction is now stated in `LABBOOK-FRAGMENTS.tex`.

No verified calculation was changed.  SP-STAB-REL remains `SKETCH`, and
SP-LREL/SP-COMPACT remain explicit unpromoted dependencies.  No trunk edit,
status change, new review round, Git action, or checker claim is part of this
repair.
