# SUMMARY — exact stabilizer/relation comparison lane

Model: `gpt-5.6-sol`, reasoning setting `xhigh`.

The lane supplies a standalone exact checker proposal for SP-STAB-REL.
`EXPECTATIONS.md` was written and reported before implementation.  The matrix
side was prepared first; D1715-dependent work waited for the canonical
definition and refined claim.  Their `Omega=-omega_m+omega_n`, all-origin,
fixed-character and no-normalization conventions matched the independently
derived projector.  No prover or source-audit lane was read, and no trunk file
was edited, staged or committed.

S1 constructs D1703 Weyl, Fourier and shear matrices over exact
`Z[zeta_p]`.  A matrix-generator closure independently finds all 216 qutrit
projective Clifford classes and the actual Clifford orbit of `delta_0` gives
12 qutrit stabilizer rays; the limited F5 orbit gives 30.  S2 forms all 144
ordered stabilizer outer-product classes and verifies that their union with
the Cliffords has 360 nonzero one-register endomorphism classes.  Exact entry
cross-products implement the full `C^times` quotient, identify `A` with `2A`,
and retain zero separately.

S3 constructs D1715's unnormalized character projector on
`conjugate(H_m) tensor H_n`, scans its actual columns, and unvectorizes.  For
every nonempty zero/one-register F3 relation it checks every origin and every
direction equation, exact origin independence,
`P_R^2=|L|P_R`, and `Tr(P_R)=|L|`, certifying a one-dimensional image.  Empty
relations give zero.  The four mapped Hom censuses are exactly
`2,13,13,361` and agree projectively with independently generated actual
families; all 216 graphs give Clifford classes and all 144 non-graph
endomorphisms give rank-one amplitudes.  All 31 F5 states are also compared.

S4 exhausts all 140,101 typed F3 compositions and all 389 daggers.  It checks
an orthogonal state/effect zero and two unequal nonzero overlap representatives
that become the same projective scalar.  S5 checks all 169 state tensors, all
169 effect tensors, 144 selected zero/scalar/state/effect/graph/rank-one mixed
tensors, and the F3/F5 vectorized identity as the Bell cup.  Using the explicit
Bell representative, cap-after-cup is the retained scalar `p`, whose
projective class is the unique nonzero unit scalar.

After the one checker repair wave, all eighteen advertised actual-data
mutations exit `1` at their intended S1--S5 gates.  S3 construction defects
now propagate through the real catalog and fail distinct nonzero, all-origin,
projector, origin, empty, actual-family and F5-orbit subchecks.  Product-order,
zero-product and transpose defects now reach S4's exhaustive typed loops;
tensor order reaches the 169-state tensor loop.  The tautological cup point-set
comparison was removed, while a new F5 cap-weight mutation reaches the final
retained-scalar check.  Temporarily disabling only that check made the red
survive with exit `0`; restoring it returned exit `1`.  Bad usage exits `2`.
Ordinary and optimized greens pass in a runtime suitable for the repository
suite.  `RUNS.md` records exact paths and `PATCH.md` gives string-anchored
integration instructions.

This finite evidence does not prove general fullness, faithfulness,
stabilizer-generator membership or equivalence for every odd prime and rank.
It chooses no normalized representative and supplies no probabilities, CP
maps, Choi construction or arithmetic-source comparison.
