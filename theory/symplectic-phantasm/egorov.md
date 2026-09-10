# Affine Egorov covariance in the half-form Weyl algebra

Lane model: `gpt-5.6-sol`, reasoning `xhigh`.

Status: PROVED as SP-EGOROV, after the single blind review and repair
recorded in `theory/verdicts/phantasm-stage1-adjudication.md`.
The admitted dependencies are SP-WEYL and F1-REAL.
No genuine phase lift is chosen.

Canonical definitions: D9, D1003, D1701 and D1703.  Reused theorem: the finite
matrix realization and unitary-intertwiner uniqueness in the admitted
`F1-REAL`, `theory/sidequests/f1-cyclotomic.md` section 2, especially
`<1>5`--`<1>8`.  Primary comparisons are SP-GH07, whose Heisenberg group and
Stone--von Neumann discussion is in its section 1.1 and whose quantization
functor is Proposition `functor_prop`, and SP-GROSS06, Theorem
`thCliffordStructure` and Lemma `cliffordAffine`.  GH07's functor is
contravariant and uses oriented models; those stronger choices are not used
to alter the variance or scope of the canonical claim here.

Throughout this proof, `k` is one fixed finite field of odd characteristic,
`psi:k->U(1)` is one fixed nontrivial additive character, and every Weyl
algebra uses D1703's half-form cocycle.  For an affine symplectic arrow
`(t,g):V->W`, write the formula already owned by the `SP-EGOROV` row as

    alpha_(t,g)(W_V(v))
      = psi(omega_W(t,g v)) W_W(g v).

Subscripts on Weyl generators only display their ambient spaces.

## SP-EGOROV: exact algebra action and projective model action

**ASSUME** D9, D1701 and D1703 over the fixed pair `(k,psi)`, the `SP-WEYL`
conclusions for all spaces occurring below, and the admitted `F1-REAL` at
the finite-abelian scope named in the DAG.  **PROVE** the exact canonical
statement `SP-EGOROV`.

<1>1. **ASSUME** an affine symplectic arrow `(t,g):V->W`.  **PROVE** the
displayed generator prescription extends uniquely to a complex-linear map
`alpha_(t,g):A(V)->A(W)`.

  <2>1. D1703 says that the symbols `W_V(v)`, indexed by `v in V`, are a
  complex basis of `A(V)`.  Therefore specifying one image for each such
  symbol gives a unique complex-linear map.
  **BY** D1703.

  <2>2. The scalar `psi(omega_W(t,g v))` is defined because `g v,t in W`,
  the form is `k`-valued, and the common character is fixed on `k`.
  **BY** D1701 and D1703.

  <2>3. **QED** `<1>1`.

<1>2. **ASSUME** `<1>1`.  **PROVE** `alpha_(t,g)` preserves products.

  <2>1. For `v,z in V`, multiplying the prescribed images gives

      alpha_(t,g)(W_V(v)) alpha_(t,g)(W_V(z))
        = psi(omega_W(t,g v)+omega_W(t,g z)
              +omega_W(g v,g z)/2) W_W(g(v+z)).

  **BY** D1703's Weyl product and additivity of `psi`.

  <2>2. Bilinearity and the symplectic property of `g` turn the exponent in
  `<2>1` into

      omega_W(t,g(v+z)) + omega_V(v,z)/2.

  **BY** D1701.

  <2>3. Applying `alpha_(t,g)` after multiplying in `A(V)` gives

      alpha_(t,g)(W_V(v)W_V(z))
        = psi(omega_V(v,z)/2)
          psi(omega_W(t,g(v+z))) W_W(g(v+z)),

  which equals `<2>1` by `<2>2`.
  **BY** D1703 and `<2>2`.

  <2>4. Equality on the basis pairs extends bilinearly to all products.
  **BY** `<1>1` and `<2>3`.

  <2>5. **QED** `<1>2`.

<1>3. **ASSUME** `<1>1`.  **PROVE** `alpha_(t,g)` preserves the unit and
the involution.

  <2>1. Since `g0=0`, alternation gives `omega_W(t,g0)=0`, so
  `alpha_(t,g)(W_V(0))=W_W(0)`.
  **BY** D1701 and D1703.

  <2>2. Every value of `psi` lies in `U(1)`, hence
  `conj(psi(x))=psi(-x)`.  For a basis generator,

      alpha_(t,g)(W_V(v))^*
        = psi(-omega_W(t,g v)) W_W(-g v)
        = alpha_(t,g)(W_V(-v))
        = alpha_(t,g)(W_V(v)^*).

  **BY** D1703, additivity of `psi`, and bilinearity of `omega_W`.

  <2>3. The involution is conjugate-linear, so the equality on basis
  generators extends to all of `A(V)`.
  **BY** D1703 and `<2>2`.

  <2>4. **QED** `<1>3`.

<1>4. **ASSUME** composable affine symplectic arrows
`(t,g):V->W` and `(s,h):W->Z`.  **PROVE** exact compatibility with D1701's
semidirect-product composition.

  <2>1. On a generator, successive application gives

      (alpha_(s,h) alpha_(t,g))(W_V(v))
        = psi(omega_W(t,g v)+omega_Z(s,hg v)) W_Z(hg v).

  **BY** `<1>1` and complex linearity of `alpha_(s,h)`.

  <2>2. Because `h` is symplectic,

      omega_W(t,g v)=omega_Z(h t,hg v).

  Adding the other term and using bilinearity gives

      omega_W(t,g v)+omega_Z(s,hg v)
        = omega_Z(s+h t,hg v).

  **BY** D1701.

  <2>3. D1701 prescribes
  `(s,h) o (t,g)=(s+h t,hg)`.  Thus `<2>1`--`<2>2` give

      alpha_(s,h) alpha_(t,g)=alpha_(s+h t,hg)

  on every basis generator, hence as linear maps.
  **BY** D1701 and `<1>1`.

  <2>4. For the identity arrow, the formula gives
  `alpha_(0,1_V)(W_V(v))=W_V(v)`.  Hence identities are respected exactly.
  **BY** D1701 and `<1>1`.

  <2>5. D1701's inverse arrow is
  `(-g^(-1)t,g^(-1)):W->V`.  Applying `<2>3` in both orders gives the two
  identity maps from `<2>4`.
  **BY** D1701 and `<2>3`--`<2>4`.

  <2>6. Consequently every `alpha_(t,g)` is a unital star-isomorphism,
  with inverse `alpha_(-g^(-1)t,g^(-1))`.
  **BY** `<1>2`, `<1>3`, and `<2>5`.

  <2>7. **QED** `<1>4`.

<1>5. **ASSUME** first a pure translation and then a pure linear arrow.
**PROVE** the affine generator action separates into the Weyl translation
and the linear Egorov action without choosing phases for the latter.

  <2>1. D1703 gives `W_W(t)^*=W_W(-t)`.  Two applications of its product
  law yield

      W_W(t) W_W(v) W_W(t)^*
        = psi(omega_W(t,v)) W_W(v).

  Indeed the two half-form exponents are respectively
  `omega_W(t,v)/2` and `omega_W(t+v,-t)/2=omega_W(t,v)/2`.
  **BY** D1703 and alternation.

  <2>2. Therefore `alpha_(t,1_W)=Ad(W_W(t))`.  For a pure linear arrow,
  `alpha_(0,g)(W_V(v))=W_W(gv)`.
  **BY** `<2>1` and the canonical generator formula.

  <2>3. Exact affine composition gives

      alpha_(t,g)=alpha_(t,1_W) alpha_(0,g).

  This is an equality of algebra maps, with no choice of a Weil operator.
  **BY** `<1>4` and D1701's composition rule.

  <2>4. In standard coordinates, if `t=(r,s)` and `v=(a,b)`, the phase in
  `<2>1` is `psi(r.b-a.s)`.  This is the rank-independent translation
  covariance tested by the proposed finite falsifier.
  **BY** D1703's standard form.

  <2>5. **QED** `<1>5`.

<1>6. **ASSUME** objects `(H_V,pi_V)` and `(H_W,pi_W)` of D1703's
arbitrary-rank extensions `Mod_(psi,beta_V)(V)` and
`Mod_(psi,beta_W)(W)` of the D9 model groupoid.
**PROVE** `alpha_(t,g)` has a unitary implementer from `H_V` to `H_W`,
unique up to `U(1)`.

  <2>1. The representation `pi_W o alpha_(t,g)` of `A(V)` on `H_W` is
  irreducible: an invariant subspace for its image is invariant for
  `pi_W(A(W))`, because `<1>4` makes `alpha_(t,g)` onto.  Its Weyl generators
  are unitary because `<1>3` is star-preserving and their scalar factors
  lie in `U(1)`.
  **BY** D1703's model-groupoid extension, `<1>3`, and `<1>4`.

  <2>2. The `SP-WEYL` bridge identifies both D1703 models with the
  fixed-central-character block to which admitted `F1-REAL` section 2
  applies.  Hence there
  is a unitary `U_(t,g):H_V->H_W` satisfying

      U_(t,g) pi_V(a) U_(t,g)^*
        = pi_W(alpha_(t,g)(a))             for every a in A(V).

  **BY** D1703, the explicit `SP-WEYL` dependency, and `F1-REAL`
  `<1>6`--`<1>8`.

  <2>3. Any two such unitary intertwiners have scalar ratio in `U(1)`.
  Therefore their class `[U_(t,g)]` is unique even though no representative
  is selected.
  **BY** admitted `F1-REAL` `<1>8`.

  <2>4. Equivalently, choose any linear-part implementer `U_g` supplied by
  `<2>2` for `alpha_(0,g)`.  Then

      pi_W(W_W(t)) U_g

  implements `alpha_(t,g)` by `<1>5`; changing `U_g` by a phase changes the
  displayed operator by the same phase.
  **BY** `<1>5` and `<2>2`--`<2>3`.

  <2>5. This construction does not choose a section of a projective Weil
  representation and does not use the stronger oriented-model
  trivialization of SP-GH07.
  **BY** the construction in `<2>2`--`<2>4` and the source scope registered
  in `refs/LEDGER.md` under SP-GH07.

  <2>6. **QED** `<1>6`.

<1>7. **ASSUME** composable arrows as in `<1>4` and implementers between
three named models.  **PROVE** their composition agrees in the `U(1)`
quotient.

  <2>1. For every `a in A(V)`, repeated use of `<1>6` gives

      U_(s,h) U_(t,g) pi_V(a) (U_(s,h) U_(t,g))^*
        = pi_Z(alpha_(s,h)(alpha_(t,g)(a))).

  **BY** `<1>6`.

  <2>2. The right side is
  `pi_Z(alpha_(s+h t,hg)(a))` by the exact algebra identity `<1>4`.
  Hence both `U_(s,h)U_(t,g)` and `U_(s+h t,hg)` implement the same
  star-isomorphism between the same irreducible models.
  **BY** `<1>4` and `<2>1`.

  <2>3. Uniqueness in `<1>6` yields

      [U_(s,h)] [U_(t,g)] = [U_(s+h t,hg)].

  For the identity arrow, both an implementer and the identity operator
  implement the identity algebra map, so their projective classes agree.
  **BY** `<1>6` `<2>3` and `<1>4` `<2>4`.

  <2>4. Tensoring or composing projective classes is well-defined: replacing
  representatives by phases only multiplies the result by one phase.
  **BY** elementary multiplication in `U(1)`.

  <2>5. **QED** `<1>7`.

<1>8. **ASSUME** the two endpoint models are replaced by objects in the same
D1703 model groupoids, with morphisms
`R_V:H_V->H'_V` and `R_W:H_W->H'_W`.  **PROVE** projective implementation
is covariant under this model transport.

  <2>1. Direct substitution in `<1>6` shows that

      R_W U_(t,g) R_V^*:H'_V->H'_W

  implements the same `alpha_(t,g)` in the primed models.
  **BY** D1703's extension of D9, the intertwining equations for
  `R_V,R_W`, and `<1>6`.

  <2>2. Changing either `R` or `U_(t,g)` by a unit scalar changes the
  displayed composite only by a unit scalar.  Its projective class is
  therefore independent of all representative phases.
  **BY** scalar centrality and admitted `F1-REAL` `<1>8`.

  <2>3. Any other implementer in the primed models has the same class by
  `<1>6`.  Thus the projective construction is transported uniquely.
  **BY** `<1>6` `<2>3`.

  <2>4. **QED** `<1>8`.

<1>9. The algebra maps are exact while their unitary implementers have only
the projective composition asserted in the canonical row.  Rank zero is
included: its only translation is zero, every symplectic arrow is the
identity of the zero space, and the model is `C` by the explicit `SP-WEYL`
dependency.  No genuine phase lift or model-independent Hilbert space has
been asserted.  **QED** (`SP-EGOROV`, PROVED at its stated odd-characteristic scope).
