# Lane summary: operational CP/subsystem framework

No root file was edited and no claim was promoted.

## Main result

The bounded endpoint can be genuine quantum mechanics without a global strong
monoidal Hilbert fibre.  For a unitary fusion category, the family
`A_X=End_C(X)` has a faithful positive categorical trace, injective assembly
maps `A_X tensor A_Y -> A_(X tensor Y)`, and unique trace-preserving conditional
expectations.  This supplies normalised positive functionals/densities,
restriction, canonical product-subalgebra preparation, effects, and the Born
rule.  The assembly map can be proper, leaving collective fusion observables.

Arbitrary isolated CP maps compose sequentially but do not determine actions on
those collective observables.  A sufficient coherent class retains finite
charge-compatible Kraus lists (or named charge-carrying Stinespring dilations)
and therefore supplies a channel in every context.  Kraus lists compose and
tensor; general dilations compose sequentially and tensor when braiding or a
specified half-braiding supplies the environment interchange.  The lane uses
Jones--Penneys only as the precise published internal-categorical analogue,
not as an identification theorem for the object-indexed endomorphism net.

## Exact tests

- Fibonacci: `A_(tau^2)=C^2`, so the diagonal braid
  `R=diag(exp(-4pi i/5),exp(3pi i/5))` has isolated conjugation equal to the
  identity.  On `tau^3=1+2tau`, the same braid acts nontrivially on the `M_2`
  charge-`tau` block.  A normalised `|+>` density/effect changes the Born value
  from `1` to `(5-sqrt(5))/8`.  The second braid `FRF`, with the exact standard
  Fibonacci `F`, gives return probability `phi^(-2)=(3-sqrt(5))/2`.
- Proposed `q=1` net: `S -> C[Sym(S)]` over finite injections, coefficient
  trace, subgroup expectations, and disjoint-union assembly.  The local
  transposition in `C[S_2]=C^2` has trivial isolated conjugation, while in
  `C[S_3]` it conjugates `(23)` to `(13)`.  The standard `M_2` block gives the
  exact Born change `1 -> 1/4`.  The full-algebra normalised density is `3q`,
  while `q` itself is the conditioned rank-one density in the standard block.

## Boundary and handoff

The symmetric-group net proves only the operational completion of a candidate
`q=1` fibre.  The separate Hecke lane must establish the finite-`p` arithmetic
family, the invariant that remembers `p`, and the specialization mechanism.
The interface demanded here is explicit: specialize retained composition and
Kraus/dilation data before taking isolated CP shadows.

The follow-up theorem `kraus-context-faithfulness.md` removes residual
redundancy from the retained-list proposal.  For an `n`-point local support,
the Kraus Gram, stable scalar-unitary equivalence, and equality of CP actions in
all finite ambient contexts are exactly equivalent.  One `2n-1`-point context
recovers the entire Gram, and this universal bound is sharp for `n>=2`.
The sharpness lists have an explicit rational density/effect Born witness with
probability gap `tau(Delta^2)>0`.  Thus `n-1` ancillary points are exactly the
worst-case cost of exposing all local process coherence in the proposed q=1
net.  A separated final paragraph records the analogous Hecke statement only
as SKETCH for the owning lane.

`PARTIAL-MAPS.md` extends the object assignment to an actual dagger lax
symmetric monoidal functor on standard finite `F_1` normal maps (partial
injections).  A partial injection is realised by subgroup expectation,
relabeling, and subgroup inclusion.  Its empty map is the trace-and-prepare
channel, and wedge/disjoint union uses the proper collective assembly
inclusion rather than a classical C*-algebra direct sum.

Proposed definitions D1121--D1127 and candidate claim/patch anchors are in
`PATCH.md`.  Primary-source locators and hashes are in `SOURCES.md`.

Validation against the shared exact checker:

- `python3 theory/checks/f1_operational_check.py` passed all current H1--H13
  gates, including the independently added neighbouring-lane gates.
- `--red-local-collapse` failed at H5 with the mutated context probability
  `1`, and `--red-kraus` failed at H8 normalization, as intended.
- H11 passed exact sharp-bound and Born-gap tests for `n=2,3` at `q=1,2`;
  `--red-context-size` failed at H11 as intended.  These finite tests do not
  promote the general theorem.
- H12 exhaustively checked partial injections between sizes zero through three
  for composition, dagger and block naturality; `--red-partial-zero` failed on
  unitality of the empty-map reset as intended.
