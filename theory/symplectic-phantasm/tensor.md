# Direct-sum/tensor comparison with affine naturality

Lane model: `gpt-5.6-sol`, reasoning `xhigh`.

Status: PROVED as SP-TENSOR, after the single blind review and repair
recorded in `theory/verdicts/phantasm-stage1-adjudication.md`.
The admitted dependencies are SP-WEYL, SP-EGOROV and F1-FUNCT.
No genuine phase lift is chosen.

Canonical definitions: D9, D1004, D1701 and D1703.  The phase comparison already
proved in `theory/symplectic-phantasm/reuse.md` section 3 transports the
admitted configuration-product theorem `F1-FUNCT`,
`theory/sidequests/f1-cyclotomic.md` section 3.  Primary comparison SP-GH09,
Proposition `Cartesian_prop`, states a natural monoidal comparison for its
oriented canonical models; its fixed character and contravariant variance
remain source-specific.  The proof below establishes the exact covariant
algebra square in the repository's conventions and uses model uniqueness
only after that calculation.

Write `A(V)=A_(psi,beta_V)(V)` and `W_V(v)=W_(beta_V)(v)` for this proof.
For two objects define the map occurring in the canonical `SP-TENSOR` row
on D1703's Weyl basis by

    Theta_(V,W)(W_(V+W)(v,w)) = W_V(v) tensor W_W(w).

This is proof-local shorthand for the claimed comparison, not a new numbered
definition.

## SP-TENSOR: algebra, trace, naturality and projective coherence

**ASSUME** one fixed odd-characteristic finite field `k`, one fixed
nontrivial character `psi`, D9, D1701 and D1703, the `SP-WEYL` conclusions
for all spaces occurring below, the `SP-EGOROV` conclusions as an explicit
admitted dependency, and admitted `F1-FUNCT`.  **PROVE** the exact
canonical statement `SP-TENSOR`.

<1>1. **ASSUME** symplectic spaces `V,W`.  **PROVE** `Theta_(V,W)` is a
unital algebra homomorphism.

  <2>1. D1703 gives a basis indexed by `V+W`, so the displayed prescription
  extends uniquely and complex-linearly.
  **BY** D1703.

  <2>2. For `v,v' in V` and `w,w' in W`, multiplication after `Theta` gives

      psi(omega_V(v,v')/2) psi(omega_W(w,w')/2)
        W_V(v+v') tensor W_W(w+w').

  **BY** D1703's product in each tensor factor.

  <2>3. Since `psi` is additive, the scalar in `<2>2` equals

      psi((omega_V(v,v')+omega_W(w,w'))/2),

  which is D1703's multiplier for the direct-sum form of D1701.
  **BY** D1701, D1703, and the character law.

  <2>4. Thus `<2>2` is the image under `Theta` of the product of the two
  source generators.  Also `Theta(W_(V+W)(0,0))=W_V(0) tensor W_W(0)`.
  **BY** `<2>2`--`<2>3` and D1703.

  <2>5. Bilinearity extends the product equality to the full algebra.
  **BY** `<2>1` and `<2>4`.

  <2>6. **QED** `<1>1`.

<1>2. **ASSUME** `<1>1`.  **PROVE** `Theta_(V,W)` preserves the involution
and is bijective.

  <2>1. On a basis generator,

      Theta(W_(V+W)(v,w)^*)
        = W_V(-v) tensor W_W(-w)
        = (W_V(v) tensor W_W(w))^*.

  **BY** D1703 and the standard involution on a tensor-product star-algebra.

  <2>2. The tensors `W_V(v) tensor W_W(w)` form a basis of
  `A(V) tensor A(W)`, indexed by the same pairs `(v,w)` as the source basis.
  Hence `Theta` maps a basis bijectively to a basis.
  **BY** D1703 and the elementary tensor-basis construction.

  <2>3. Therefore `Theta_(V,W)` is a unital star-isomorphism.
  **BY** `<1>1`, `<2>1`, and `<2>2`.

  <2>4. **QED** `<1>2`.

<1>3. **ASSUME** `<1>2`.  **PROVE** `Theta_(V,W)` preserves the prescribed
coefficient traces.

  <2>1. On a basis tensor, the tensor-product functional is

      (tau_V tensor tau_W)(W_V(v) tensor W_W(w))
        = [v=0][w=0].

  **BY** D1703.

  <2>2. The source coefficient trace of `W_(V+W)(v,w)` has exactly the same
  value, since `(v,w)=0` exactly when `v=0` and `w=0`.
  **BY** D1703.

  <2>3. Equality on the source basis yields

      (tau_V tensor tau_W) o Theta_(V,W) = tau_(V+W).

  **BY** `<2>1`--`<2>2` and linearity.

  <2>4. Under the `SP-WEYL` matrix realization these are the normalized
  matrix traces, so this is also the trace comparison named in the
  canonical claim.
  **BY** the explicit `SP-WEYL` dependency, reuse.md section 2 `<1>3`.

  <2>5. **QED** `<1>3`.

<1>4. **ASSUME** named standard coordinates on `V` and `W`, and give the
direct sum the standard coordinates obtained by the explicit reordering

    ((a_1,b_1),(a_2,b_2)) |-> ((a_1,a_2),(b_1,b_2)).

**PROVE** the standard Hilbert model comparison is the transport of admitted
`F1-FUNCT` and intertwines `Theta` exactly.

  <2>1. Put `A_cfg=(k^m,+)` and `B_cfg=(k^n,+)` for the two configuration
  groups.  The common character has image `mu_p`, so both are objects of
  D1004 at the one fixed level `N=p`.
  **BY** reuse.md section 1 `<1>3` and D1004.

  <2>2. The admitted `F1-FUNCT` basis comparison realizes as the unitary

      J^0_(V,W): ell^2(k^(m+n)) -> ell^2(k^m) tensor ell^2(k^n),
      J^0_(V,W) delta_(x,y) = delta_x tensor delta_y.

  It sends each reference Weyl operator to the tensor of the corresponding
  reference operators.
  **BY** admitted `F1-FUNCT` section 3 `<1>3`--`<1>6`.

  <2>3. For labels `(a_1,b_1)` and `(a_2,b_2)`, the D1703 half-form cochain
  satisfies

      psi((a_1.b_1+a_2.b_2)/2)
        = psi(a_1.b_1/2) psi(a_2.b_2/2).

  **BY** reuse.md section 3 `<1>1`.

  <2>4. Multiplying the reference intertwining equation in `<2>2` by the
  phase equality in `<2>3` gives

      J^0_(V,W) pi_(V+W)(a) (J^0_(V,W))^*
        = (pi_V tensor pi_W)(Theta_(V,W)(a))

  first on Weyl generators and then on every algebra element.
  **BY** reuse.md section 3 `<1>2` and linearity.

  <2>5. The zero-configuration basis comparison is the canonical map
  `C->C`, and the half-form phase is the empty product `1`.
  **BY** D1703 and admitted `F1-FUNCT` section 3 `<1>4`.

  <2>6. **QED** `<1>4`.

<1>5. **ASSUME** affine symplectic arrows `(t,g):V->V'` and
`(s,h):W->W'`.  **PROVE** arbitrary affine naturality of `Theta` as an exact
algebra identity.

  <2>1. The direct-sum affine arrow has translation `(t,s)` and linear part
  `g direct-sum h`; on a Weyl generator its `SP-EGOROV` phase is

      psi((omega_(V')(t,g v)+omega_(W')(s,h w))).

  **BY** D1701's direct-sum form and the `SP-EGOROV` generator formula.

  <2>2. Applying `Theta_(V',W')` after that affine map therefore gives

      psi(omega_(V')(t,g v)+omega_(W')(s,h w))
        W_(V')(g v) tensor W_(W')(h w).

  **BY** `<2>1` and the defining basis prescription for `Theta`.

  <2>3. Applying `Theta_(V,W)` first and then
  `alpha_(t,g) tensor alpha_(s,h)` gives the product of the two character
  values multiplying the same tensor generator.  Additivity of `psi` makes
  that scalar exactly the one in `<2>2`.
  **BY** `SP-EGOROV` and the character law.

  <2>4. Hence the naturality square

      Theta_(V',W') alpha_((t,s),(g direct-sum h))
        = (alpha_(t,g) tensor alpha_(s,h)) Theta_(V,W)

  commutes exactly on the Weyl basis and therefore on the full algebra.
  Here `g direct-sum h` is the ordinary direct sum of the two linear maps.
  **BY** `<2>2`--`<2>3` and D1703's basis.

  <2>5. **QED** `<1>5`.

<1>6. **ASSUME** three symplectic spaces `U,V,W`.  **PROVE** the algebra
associativity diagram for `Theta` commutes exactly.

  <2>1. Let `a^S:((U+V)+W)->(U+(V+W))` be the canonical rebracketing linear
  symplectic arrow and let `a^A` be the usual tensor-algebra associator.
  Both are available from D1701's direct sums and the ordinary tensor
  product of complex algebras.
  **BY** D1701.

  <2>2. The first route

      a^A (Theta_(U,V) tensor id) Theta_(U+V,W)

  sends `W_((U+V)+W)((u,v),w)` to
  `W_U(u) tensor (W_V(v) tensor W_W(w))`.
  **BY** the basis prescription for `Theta`.

  <2>3. The second route

      (id tensor Theta_(V,W)) Theta_(U,V+W) alpha_(0,a^S)

  sends the same generator to the same tensor.
  **BY** `SP-EGOROV` for the zero-translation rebracketing arrow and the
  basis prescription for `Theta`.

  <2>4. Thus the associativity diagram commutes exactly.
  **BY** D1703's basis and `<2>2`--`<2>3`.

  <2>5. **QED** `<1>6`.

<1>7. **PROVE** the rank-zero unit and symmetry diagrams for `Theta` commute
exactly.

  <2>1. By the explicit `SP-WEYL` dependency, `A(0)=C`, with sole Weyl
  generator `1`.  For the canonical symplectic unitors
  `l^S:0+V->V` and `r^S:V+0->V`, the composites of `Theta` with the ordinary
  algebra unitors and the direct maps `alpha_(0,l^S)`, `alpha_(0,r^S)` all
  send their basis generators to `W_V(v)`.
  **BY** `SP-WEYL`, `SP-EGOROV`, and the basis prescription for `Theta`.

  <2>2. Let `c^S:V+W->W+V` exchange the two summands and let `Sigma^A`
  exchange the two tensor factors.  On a generator,

      Sigma^A Theta_(V,W)(W_(V+W)(v,w))
        = W_W(w) tensor W_V(v)
        = Theta_(W,V) alpha_(0,c^S)(W_(V+W)(v,w)).

  **BY** `SP-EGOROV` and the basis prescription for `Theta`.

  <2>3. Equality on the Weyl bases proves both unit diagrams and the
  symmetry diagram.  Together with `<1>6`, these are the exact algebra
  coherence clauses in the canonical statement.
  **BY** D1703 and `<2>1`--`<2>2`.

  <2>4. **QED** `<1>7`.

<1>8. **ASSUME** objects `(H_V,pi_V)`, `(H_W,pi_W)`, and
`(H_(V+W),pi_(V+W))` of D1703's arbitrary-rank extensions of the D9 model
groupoid.  **PROVE** there is a unique projective unitary model identification
over `Theta_(V,W)`.

  <2>1. By `<1>2`, `(pi_V tensor pi_W) o Theta_(V,W)` is a unitary
  representation of `A(V+W)` on `H_V tensor H_W`.  It is irreducible because
  `Theta` is onto and the image is the tensor of the full matrix images
  supplied by `SP-WEYL`.
  **BY** D1703, `<1>2`, and the explicit `SP-WEYL` dependency.

  <2>2. Apply the fixed-central-character model uniqueness inherited in
  `SP-WEYL` from `F1-REAL`.  There is a unitary

      J_(V,W):H_(V+W)->H_V tensor H_W

  satisfying

      J_(V,W) pi_(V+W)(a) J_(V,W)^*
        = (pi_V tensor pi_W)(Theta_(V,W)(a)),

  and any two such unitaries differ by an element of `U(1)`.
  **BY** D1703, `SP-WEYL`, and admitted `F1-REAL` section 2
  `<1>6`--`<1>8`.

  <2>3. In the standard coordinate models the unitary `J^0_(V,W)` from
  `<1>4` is one such representative.  Thus this abstract projective class
  is the transported F1-FUNCT comparison rather than a new tensor theorem.
  **BY** `<1>4` and `<2>2`.

  <2>4. Changing any of the three models by unitary intertwiners conjugates
  `J_(V,W)` by those intertwiners; its new class is forced by `<2>2` and is
  independent of all representative phases.
  **BY** D1703's extension of D9, the same substitution as `SP-EGOROV`
  `<1>8`, and `<2>2`.

  <2>5. **QED** `<1>8`.

<1>9. **ASSUME** affine arrows as in `<1>5`, their unique projective
implementers from `SP-EGOROV`, and the projective tensor identifications
from `<1>8`.  **PROVE** the model naturality square commutes projectively.

  <2>1. The composite

      J_(V',W') U_((t,s),(g direct-sum h))

  and the composite

      (U_(t,g) tensor U_(s,h)) J_(V,W)

  are unitaries from `H_(V+W)` to `H_(V') tensor H_(W')`.
  **BY** `SP-EGOROV` and `<1>8`.

  <2>2. The first composite implements
  `Theta_(V',W') alpha_((t,s),(g direct-sum h))`; the second implements
  `(alpha_(t,g) tensor alpha_(s,h)) Theta_(V,W)`.
  **BY** the intertwining equations in `SP-EGOROV` and `<1>8`.

  <2>3. Those algebra maps are equal by exact affine naturality `<1>5`.
  Fixed-central-character intertwiner uniqueness therefore gives

      [J_(V',W')] [U_((t,s),(g direct-sum h))]
        = ([U_(t,g)] tensor [U_(s,h)]) [J_(V,W)].

  **BY** `<1>5`, `<2>2`, and admitted `F1-REAL` `<1>8`.

  <2>4. Tensor product of projective classes is well-defined because
  multiplying either representative by a phase only multiplies the tensor
  representative by the product phase.
  **BY** elementary scalar centrality.

  <2>5. **QED** `<1>9`.

<1>10. **PROVE** the unit, associativity and symmetry model diagrams commute
in the `U(1)` quotient.

  <2>1. For associativity, form the two composites from
  `H_((U+V)+W)` to `H_U tensor (H_V tensor H_W)` using the two `J` maps,
  the ordinary Hilbert associator, and the projective implementer of the
  canonical symplectic rebracketing arrow.
  **BY** `<1>8` and `SP-EGOROV`.

  <2>2. The two composites in `<2>1` implement the two algebra routes in
  `<1>6`.  Those routes agree exactly, so the composites differ by one
  scalar in `U(1)` and have the same projective class.  Explicitly, with
  `a^H` the Hilbert associator,

      [a^H] [J_(U,V) tensor 1] [J_(U+V,W)]
        = [1 tensor J_(V,W)] [J_(U,V+W)] [U_(0,a^S)].

  **BY** `<1>6` and admitted `F1-REAL` `<1>8`.

  <2>3. For each unit diagram, compare the model `J` involving `H_0=C` with
  the ordinary Hilbert unitor and the projective implementer of the
  corresponding symplectic unitor.  Both routes implement the exact algebra
  map in `<1>7` `<2>1`, so their projective classes agree.  If `l^H,r^H`
  are the Hilbert unitors, this says

      [l^H] [J_(0,V)] = [U_(0,l^S)],
      [r^H] [J_(V,0)] = [U_(0,r^S)].

  **BY** `<1>7`, `<1>8`, and admitted `F1-REAL` `<1>8`.

  <2>4. For symmetry, let `Sigma^H:H_V tensor H_W->H_W tensor H_V` be the
  Hilbert flip and let `U_(0,c^S)` implement the symplectic summand exchange.
  The equality of exact algebra maps in `<1>7` `<2>2` gives

      [Sigma^H] [J_(V,W)]
        = [J_(W,V)] [U_(0,c^S)].

  **BY** `<1>7`, `<1>8`, `SP-EGOROV`, and admitted `F1-REAL` `<1>8`.

  <2>5. In standard coordinate models these same diagrams already commute
  exactly for the basis maps inherited from `F1-FUNCT`; the arbitrary-model
  statement deliberately retains only what uniqueness forces, namely their
  classes in the `U(1)` quotient.
  **BY** admitted `F1-FUNCT` section 3 `<1>4`--`<1>6` and `<1>4`.

  <2>6. No equality between chosen unitary representatives has been used or
  asserted.  Thus the proof does not smuggle in a coherent genuine Weil
  lift.
  **BY** `<2>1`--`<2>5`.

  <2>7. **QED** `<1>10`.

<1>11. `<1>1`--`<1>3` prove the trace-preserving star-isomorphism;
`<1>4` is the exact half-form transport of admitted `F1-FUNCT`; `<1>5`
proves arbitrary affine naturality; `<1>6`--`<1>7` prove exact algebra
coherence; and `<1>8`--`<1>10` prove only the projective model diagrams
licensed by finite Stone--von Neumann uniqueness.  The source operation is
the symplectic direct sum, and no additive completion of the classical
category has been constructed.  **QED** (`SP-TENSOR`, PROVED at its stated
odd-characteristic scope).
