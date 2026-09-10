# Composition of affine Lagrangian relations

Lane model: `gpt-5.6-sol`, reasoning `xhigh`.

Admitted proof of `SP-LREL`; capped review and mechanical repair dispositions
are in `theory/verdicts/phantasm-relations-adjudication.md`. The proof uses the definitions in D1701--D1702 and does not use a smooth canonical-
relation theorem.  Its finite-linear reduction agrees with SP-W09, section
2.1, especially the coisotropic reduction and middle-diagonal description of
composition at local source lines 421--470.  SP-LW14, lines 1571--1599 and
1874--1884, separately records that finite-dimensional linear canonical
relations compose by this reduction.  SP-CK21, lines 1737--1762 and
1807--1820, supplies the all-fields Lagrangian-relation and strong symmetric
monoidal conventions.  None of those citations supplies quantum
normalization.

Throughout this shard, perpendiculars are taken for the displayed ambient
symplectic form.  Direct-sum coordinates are kept in their displayed order.
For a nonempty affine subspace `A`, `dir(A)` denotes its unique translation
subspace.  This is proof-local shorthand, not a new canonical definition.

## 1. Finite-linear reduction lemma

**ASSUME** a finite field `k`, a finite-dimensional symplectic `k`-space
`(X,omega_X)`, a coisotropic linear subspace `C` of `X`, and a Lagrangian
linear subspace `L` of `X`.  Put `K=C^perp`, let `q:C->C/K` be the quotient,
and give `C/K` the form induced by `omega_X`.  **PROVE** that `C/K` is
symplectic and `q(L cap C)` is Lagrangian in it.

<1>1. **PROVE** `K` is contained in `C` and the form

    omega_red([c],[c']) = omega_X(c,c')

is well-defined and alternating on `C/K`.

  <2>1. Coisotropy means exactly `C^perp subset C`, so `K subset C`.
  **BY** the definition of coisotropic used in SP-W09 section 2.1 and the
  displayed assumption.

  <2>2. If `c` is changed by `u in K`, then
  `omega_X(c+u,c')=omega_X(c,c')` for every `c' in C`.
  **BY** `K=C^perp`.

  <2>3. The same is true when `c'` is changed by an element of `K`.
  **BY** bilinearity, alternation, and `<2>2` with the variables exchanged.

  <2>4. Hence the displayed formula is well-defined; bilinearity and
  alternation descend from `omega_X`.
  **BY** `<2>2`--`<2>3`.

  <2>5. **QED** `<1>1`.

<1>2. **PROVE** the induced form on `C/K` is nondegenerate.

  <2>1. Suppose `[c]` pairs to zero with every `[c']`, `c' in C`.
  Then `omega_X(c,C)=0`.
  **BY** the formula in `<1>1`.

  <2>2. Thus `c in C^perp=K`, so `[c]=0`.
  **BY** the definition of perpendicular.

  <2>3. **QED** `<1>2`.

<1>3. **PROVE** `q(L cap C)` is isotropic.

  <2>1. For `x,y in L cap C`, `omega_X(x,y)=0` because `L=L^perp`.
  **BY** D1701's Lagrangian condition.

  <2>2. Therefore `omega_red(qx,qy)=0`.
  **BY** `<1>1` and `<2>1`.

  <2>3. **QED** `<1>3`.

<1>4. Put `dim X=2N` and `dim K=r`.  **PROVE**

    dim(L cap C) = N-r+dim(L cap K).

  <2>1. For subspaces `A,B` of a finite-dimensional nondegenerate bilinear
  space,

      (A+B)^perp = A^perp cap B^perp.

  **BY** expanding the two definitions of the right and left sides.

  <2>2. Since `L=L^perp` and `K^perp=(C^perp)^perp=C`, `<2>1` gives

      (L+K)^perp = L cap C.

  **BY** D1701, nondegeneracy, and `K=C^perp`.

  <2>3. Nondegeneracy gives `dim A+dim A^perp=dim X` for every subspace
  `A subset X`.
  **BY** the rank-nullity theorem applied to
  `X -> A^*`, `x |-> omega_X(x,-)|_A`, which is onto because the ambient
  form identifies `X` with `X^*` and restriction `X^*->A^*` is onto.

  <2>4. Thus

      dim(L cap C)
        = 2N-dim(L+K)
        = 2N-(N+r-dim(L cap K)).

  **BY** `<2>2`--`<2>3`, `dim L=N`, and the subspace dimension formula.

  <2>5. Simplifying gives the asserted equality.
  **BY** `<2>4`.

  <2>6. **QED** `<1>4`.

<1>5. **PROVE** `q(L cap C)` has half the dimension of `C/K`.

  <2>1. The kernel of `q|_(L cap C)` is `L cap K`.
  **BY** `ker q=K` and `K subset C` from `<1>1`.

  <2>2. Rank-nullity and `<1>4` give

      dim q(L cap C)=N-r.

  **BY** `<2>1` and `<1>4`.

  <2>3. Since `dim C=2N-r`, one has
  `dim(C/K)=2N-2r=2(N-r)`.
  **BY** `dim C+dim C^perp=2N`, `C^perp=K`, and quotient dimension.

  <2>4. Hence the image dimension in `<2>2` is half the reduced dimension.
  **BY** `<2>2`--`<2>3`.

  <2>5. **QED** `<1>5`.

<1>6. **PROVE** `q(L cap C)` equals its perpendicular in `C/K`.

  <2>1. An isotropic subspace of a finite-dimensional symplectic space is
  contained in its perpendicular.
  **BY** the definitions of isotropic and perpendicular.

  <2>2. The perpendicular has complementary dimension, so an isotropic
  subspace of half dimension equals its perpendicular.
  **BY** the dimension identity proved in `<1>4.<2>3`.

  <2>3. Apply `<2>1`--`<2>2` using `<1>2`, `<1>3`, and `<1>5`.
  **BY** those steps.

  <2>4. **QED** `<1>6`.

<1>7. **QED** the finite-linear reduction lemma.
**BY** `<1>1`--`<1>6`.

The argument used only bilinearity, alternation, nondegeneracy, and finite
dimension.  In particular it did not divide by two, so it includes
characteristic two.

## 2. Linear and affine composition closure

**ASSUME** D1701--D1702, linear Lagrangian relations `R:V->W` and
`S:W->Z`.  **PROVE** `S o R` is a linear Lagrangian relation `V->Z`.

<1>1. Form the symplectic space

    X = bar(V) + W + bar(W) + Z

in that exact factor order, and put `L=R+S subset X`.
**BY** D1701--D1702.

<1>2. **PROVE** `L` is Lagrangian in `X`.

  <2>1. The perpendicular of a direct sum of subspaces in an orthogonal
  direct sum is the direct sum of their perpendiculars.
  **BY** expansion of the direct-sum form.

  <2>2. Hence `(R+S)^perp=R^perp+S^perp=R+S`.
  **BY** `<2>1` and the two Lagrangian assumptions.

  <2>3. **QED** `<1>2`.

<1>3. Put

    C = bar(V) + Delta_W + Z
        = { (v,w,w,z) : v in V, w in W, z in Z } subset X.

**PROVE** `C` is coisotropic and

    C^perp = { (0,w,w,0) : w in W }.

  <2>1. A vector `(v0,a,b,z0)` is orthogonal to all `(v,w,w,z) in C`
  exactly when `v0=0`, `z0=0`, and

      omega_W(a,w)-omega_W(b,w)=0 for every w.

  **BY** D1701's direct-sum and opposite forms, and their nondegeneracy on
  the unrestricted outer factors.

  <2>2. Nondegeneracy of `omega_W` makes the last condition equivalent to
  `a=b`.
  **BY** D1701.

  <2>3. Thus the displayed formula for `C^perp` holds and is contained in
  `C`.
  **BY** `<2>1`--`<2>2`.

  <2>4. The cancellation is subtraction in `k`; it remains valid when
  `char(k)=2`, where the opposite form equals the original as a function.
  **BY** the field identity `x-x=0`.

  <2>5. **QED** `<1>3`.

<1>4. **PROVE** the map

    rho:C/C^perp -> bar(V)+Z,
    rho([(v,w,w,z)])=(v,z)

is a well-defined symplectic isomorphism.

  <2>1. Two representatives have the same outer pair exactly when their
  difference is `(0,u,u,0) in C^perp`.
  **BY** `<1>3`.

  <2>2. Therefore `rho` is well-defined and injective; it is surjective by
  the representative `(v,0,0,z)`.
  **BY** `<2>1`.

  <2>3. On representatives, the form is

      -omega_V(v,v')+omega_W(w,w')
      -omega_W(w,w')+omega_Z(z,z')
      = -omega_V(v,v')+omega_Z(z,z').

  **BY** D1701 and the exact factor order in `<1>1`.

  <2>4. The right side is the form of `bar(V)+Z`, so `rho` is symplectic.
  **BY** D1701 and `<2>3`.

  <2>5. **QED** `<1>4`.

<1>5. **PROVE** `rho(q(L cap C))=S o R` as subsets of `V x Z`.

  <2>1. An element of `L cap C` has the form `(v,w,w,z)` with
  `(v,w) in R` and `(w,z) in S`.
  **BY** `L=R+S` and the definition of `C`.

  <2>2. Its image under `rho q` is `(v,z)`.
  **BY** `<1>4`.

  <2>3. Consequently `(v,z)` is in the image exactly when there exists
  `w` satisfying the two membership conditions.
  **BY** `<2>1`--`<2>2`.

  <2>4. This is exactly D1702's existential definition of `S o R`.
  **BY** D1702.

  <2>5. **QED** `<1>5`.

<1>6. The reduction lemma makes `q(L cap C)` Lagrangian, and the symplectic
isomorphism `rho` preserves the Lagrangian condition.  Therefore `S o R` is
Lagrangian in `bar(V)+Z`.
**BY** section 1, `<1>2`--`<1>5`, and preservation of perpendiculars by a
symplectic isomorphism.

<1>7. **QED** linear composition closure.
**BY** `<1>6` and D1702.

**ASSUME** now arbitrary D1702 arrows `R:V->W`, `S:W->Z`, allowing affine
translates and the empty relation.  **PROVE** `S o R` is again a D1702 arrow.

<1>8. If `R` or `S` is empty, then `S o R` is empty.
**BY** D1702's existential composition.

<1>9. Suppose both are nonempty and write
`R=r_0+R_0`, `S=s_0+S_0`, with `R_0,S_0` their Lagrangian direction
subspaces.
**BY** D1702 and uniqueness of the direction subspace of a nonempty affine
subspace.

<1>10. In the ambient `X` of `<1>1`, put `A=R+S`, an affine translate of
`L_0=R_0+S_0`.  The middle-point constraint is `A cap C`.
**BY** the definitions of affine product and `C`.

<1>11. If `A cap C` is empty, then `S o R` is empty.
**BY** the same membership equivalence as `<1>5`.

<1>12. If `A cap C` is nonempty, choose
`x_0=(v_0,w_0,w_0,z_0)` in it.  Then

    A cap C = x_0 + (L_0 cap C).

**BY** for a linear subspace `C` and affine subspace `x+L_0`, any chosen
point of their nonempty intersection translates the intersection to
`L_0 cap C`, verified by subtracting `x_0` in both directions.

<1>13. Projecting outer coordinates gives

    S o R = (v_0,z_0) + (S_0 o R_0).

**BY** `<1>5` applied to the direction subspaces and `<1>12`.

<1>14. The direction `S_0 o R_0` is Lagrangian by linear closure, so the
right side of `<1>13` is an affine Lagrangian relation.
**BY** `<1>7` and D1702.

<1>15. Thus every affine composite is either empty or an affine translate
of a Lagrangian subspace.  No transversality hypothesis was used.
**BY** `<1>8`--`<1>14`.

<1>16. **QED** composition closure, including characteristic two and all
empty cases.
**BY** `<1>15` and the final observation of section 1.
