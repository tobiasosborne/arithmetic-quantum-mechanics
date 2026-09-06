# F1 sidequest — capped review adjudication

Date: 2026-09-06. Prover and independent blind critic: `gpt-5.6-sol`, xhigh.
No Astra or Claude subagents were used. One prover pass, one hostile round,
one coordinator repair and mechanical verification; no repeated critic loop.
The critic read the proof and definitions proposal, not the prover SUMMARY.
The same-family limitation is explicit.

The durable critic report is `theory/verdicts/f1-r1.md`. Its verdict was
FAIL(O1,O2,O3), with all three MAJORs confined to the proposed correspondence
definition and geometric conjecture. It verified the seven finite-kernel
claims independently and found no FATAL or MAJOR on them.

## Disposition

| objection | repair | verification / admitted scope |
|---|---|---|
| O1: orbit-set matrices are not intrinsic on arbitrary free torsors | D1007 now uses finite basis sets and explicitly framed modules S_I | Read back the stated objects and frame; no basis-independent matrix assignment is claimed |
| O2: lifted phase groupoid lacked a tensor, making strong monoidality ill-typed | D1007 now declares object/arrow tensor, canonical factor reordering, unit and symmetry | Products of the lift-cochain equations give the tensor lift equation; composition is composition of centre-fixing maps |
| O3: matrix theorem versus unspecified F1-geometric home | Removed the geometric existence clause from the admitted statement; F1-CORR is the precise algebraic projective functor, with a supporting descent-of-linear-equations argument | F1-CORR remains SKETCH. Geometric descent is an open research target, not a universal conjecture with an unnamed category |
| O4: targets of F1-FUNCT unnamed | Proof section 3 explicitly names the three monoidal groupoids | Balanced smash, central product, and Hilbert tensor agree under their displayed maps; M6 checks a nontrivial example |

The positive core admitted as PROVED comprises F1-DUAL, F1-WEYL, F1-REAL,
F1-FUNCT, F1-RING, F1-ONE and F1-MON. The proof is self-contained and
uniform in the phase level, including even levels. These are established
finite-Heisenberg facts with a cyclotomic pointed-module interpretation;
the status is not a claim of a universal F1 quantum theory.

The critic ran M1–M7 and their mutations; it also replaced the F4 generating
character by a trivial character and observed M4 fail. The coordinator
ran the entire extended checker, including the independent crowd, Hall,
frame and fusion routes. Every advertised mutation reaches its named gate.
The full repository checks and labbook build are the session-close gate.

## Supporting comparisons retained at SKETCH

F1-CROWD, F1-FRAME, F1-NORMAL, F1-HALL, F1-CAT, F1-FUSION and F1-TORUS
have explicit supporting derivations and/or precise primary-source
locators, but no dedicated hostile round; their statuses remain SKETCH.
F1-CORR's new algebraic supporting argument is also SKETCH.

One crowd scope error was repaired during coordinator recomputation:
membership of xy in the signed matrix set does not suffice for the
inherited crowd product; (xy)^(-1) must also belong to the set. Four of
the 27 signed matrices lack an internal inverse. The corrected derivation
and labbook preserve the mediator condition, including the possibility
that x*1 is empty. The concrete x(1)y(1) positive example survives.

The tensor-category formulation retains a fibre functor: the internal
endomorphisms of the simple qubit object are scalars, and its invariant
state space is zero. The full qubit observable algebra and state vectors
are recovered after applying the fibre functor. The matching central
product for independent systems is kept distinct from internal fusion.

No earlier finite-field or finite-ring claim changed status. The unfinished
FCR-2 proof lane was not admitted or modified by this sidequest.
