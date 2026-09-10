# Sole SP-SCALAR/SP-CP prover repair wave

Date: 2026-09-10. Repair model: `gpt-5.6-sol`, reasoning `xhigh`.

This repair responds only to OBJ-1 and OBJ-2 in
`theory/lanes/phantasm-processes/critic/VERDICT.md`. The independent checker
owner handles OBJ-3. No critic-verified matrix, Kraus, trace, composition,
tensor, instrument or discard calculation was changed.

## OBJ-1 — weakened scalar-quotient consequence

`scalar.md` no longer says an actual representative is necessary. It proves
two positive constructions:

1. choose any representative satisfying `T^*T<=1`;
2. add the class-invariant operator-norm rule
   `N_[T](rho)=T rho T^*/||T||^2` on nonzero classes.

For `S=cT`, numerator and denominator both scale by `|c|^2`, so the second
rule is representative-independent. The normalized effect is
`T^*T/||T||^2<=1`, so it is TNI. The zero class remains separate and may be
sent to the zero branch. D1705 itself stipulates neither construction nor a
probability. Compatibility of an added rule with composition remains a
separate obligation; no functor or normalization no-go is claimed.

`LABBOOK-FRAGMENTS.tex` uses the exact proposed weaker canonical consequence
and includes this supporting computation.

## OBJ-2 — general trace-adjoint construction

`instruments.md` section 5 now starts with an arbitrary complex-linear block
map. Ordinary block matrix units give its coefficient matrix `C`; defining
the adjoint on output units with coefficients `conjugate(C_(q,p))` constructs
the conjugate-transpose coefficient matrix. Orthonormality proves the D1706
pairing identity, and positive definiteness proves uniqueness. Only afterward
does section 6 specialize to a CP Kraus family and retain the reviewed
reverse-Kraus, subunital/unital and discard calculations.

The source locator SP-WAT18 `paper.txt` 1097--1105 is added to
`SOURCE-REUSE.md`. The labbook fragment presents the same general
matrix-unit construction. Its auxiliary space in the CP proof is explicitly
finite-dimensional, and no definition IDs occur outside provenance.

Both canonical statuses remain `SKETCH` until coordinator adjudication. This
is the sole repair wave; no new review, proof scope, definition, trunk edit,
status change, checker claim or Git action is included.
