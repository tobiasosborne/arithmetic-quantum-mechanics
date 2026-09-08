# Composition/comparison lane summary

Status: prover submission complete; frozen for blind review.  No trunk file
was edited and no claim is proposed above `SKETCH` before the capped review.

## Result

The universal finite composition category is now explicit.  For a
multiplicative sequence `A_*`, the contravariant functor convention produces
right `A_n`-modules, and Day tensor is the induction

    (M tensor N) tensor_(A_m tensor A_n) A_(m+n).

For the positive Hecke sequence, finite-dimensional modules are all
projective.  Consequently its finite Davydov--Molev Schur--Weyl category is
strong-monoidally equivalent to the additive Karoubi completion of the raw
Hecke skeleton.  D1141's `Gamma_q` has the same completion because its
complete-flag object has corner idempotent one in every degree.  The proof
tracks the exact map `alpha |->e_alpha H_n`, arrow direction
`e_beta H_n e_alpha`, and the balanced induction isomorphism.

The source convention is translated exactly by

    q_project=v^2,             T_project=v t_source.

The algebraic Hecke braid generator is nonunitary away from one.  Its
spectral sign

    u_i=(2T_i+1-q)/(q+1)

is unitary but has defect

    u_i u_(i+1) u_i-u_(i+1)u_i u_(i+1)
      =-((q-1)^2/(q+1)^2)(u_i-u_(i+1)).

A genuine positive replacement exists.  If `D_n=T_(w0)` and
`J_n=D_n(D_n^2)^(-1/2)`, then

    sigma_(m,n)=J_(m+n)(J_m tensor J_n)

is a canonical unitary coboundary commutor.  The proof establishes
longest-element centrality, naturality, symmetry, both cactus paths,
parabolic and arbitrary Karoubi-corner compatibility, and identifies
`sigma` as the polar unitary of the standard block braid.  It is canonical
and continuous on `q>0`, symmetric at `q=1`, and analytic fibre structure
rather than an asserted morphism over the generic localized ring.

At the symmetric endpoint, the typed Schur--Weyl maps

    C[S_n] -> End_(U(d))((C^d)^tensor n)

are surjective and coherently multiplicative.  Their kernel is the sum of
partition blocks with more than `d` rows, equivalently the ideal generated
by the `(d+1)`-antisymmetrizer; faithfulness holds exactly for `d>=n`.
Normalized tensor trace is

    tr_(d,n)(sigma)=d^(cycles(sigma)-n)

and converges at fixed `n` to coefficient trace.  The physical conditional
expectation is a Gram projection, not coefficient deletion: for the
sentinel inclusion `<(12)><S_3`,

    E_d((23))=d^(-1)1.

The proof gives the general coefficient bound
`1/(d-(|K|-1))` and a normalized Born-probability error estimate.

Rigid and fusion branches now list their exact additional data.  Rigidity
requires dual objects, cups/caps, zigzags, and pivotal/dagger conventions.
Temperley--Lieb requires a tensor ideal plus Jones--Markov trace; the
faithful flag trace cannot descend.  At `q=1`, flag weights `(1/2,1/2)`
differ from the physical `d=2` weights `(3/4,1/4)`.  Fibonacci further
requires the order-five root, Jones trace-radical quotient, and even
subcategory; it is not the `q=1` positive-real fibre.

## Artifacts

- `DEFINITIONS-PROPOSED.md`: D1221--D1239.
- `UNIVERSAL-CATEGORY.md`: 314-line structured proof.
- `UNITARY-EXCHANGE.md`: 350-line structured proof.
- `SCHUR-WEYL.md`: 336-line structured proof.
- `FUSION-BOUNDARIES.md`: 318-line structured proof.
- `CLAIMS-PROPOSED.md`: eight exact claim rows, all `SKETCH` pending review.
- `FALSIFIERS.md`: exact green and reachable red specifications.
- `SOURCES.md`: hashes, scope, and primary-source locators.

## Verification

The independent root checker was run after the proofs froze:

    python3 theory/checks/f1_limit_check.py

It passed all gates, including L7 (six exchange-defect probes), L8 (164
Schur/trace probes), L9 (15 physical-expectation probes), and L13 (175 exact
polar/cactus/naturality probes).  The four relevant mutations were also run
and exited one at their intended gates:

    --red-braid             -> L7
    --red-cycle             -> L8
    --red-reference-trace   -> L9
    --red-polar             -> L13

These finite computations support the examples; the uniform conclusions
rest on the structured proofs.

## Integration notes

- Replace the provisional `LC` labels in `FALSIFIERS.md` and
  `CLAIMS-PROPOSED.md` by root checker gates: `LC4->L7`,
  `LC6/LC8->L8`, `LC9->L9`, `LC5->L13`; the purely categorical `LC1--LC3`
  remain written proof obligations unless root assigns new gates.
- In the current ledger entry for `1008.3739`, section 2.1 begins on
  **printed p. 6**, formula (2.1) is on printed p. 7, and the discussion
  continues through p. 8.  `SOURCES.md` uses these printed-page locators.
- `SOURCES.md` records that the Davydov--Molev PDF prints its parameter as
  `q`; this lane renames it `v` before applying `q_project=v^2`.
- The operational core may use D1230's commutor for canonical positive-fibre
  block exchange, while leaving cross-degree preparation/discard and the CP
  envelope in its own definitions.
