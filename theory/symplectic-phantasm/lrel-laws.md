# Category laws, monoidal coherence, and the graph functor

Lane model: `gpt-5.6-sol`, reasoning `xhigh`.

Admitted companion to `lrel-reduction.md`. Sections 1--2 and all finite-linear
closure results cited below are proved in that shard. This shard completes
`SP-LREL`; see `theory/verdicts/phantasm-relations-adjudication.md`.

## 3. Category and dagger laws

**ASSUME** D1702 arrows `R:U->V`, `S:V->W`, and `T:W->X`.
**PROVE** associativity and the identity laws.

<1>1. For `(u,x)`, membership in `T o (S o R)` is equivalent to

    exists v in V, exists w in W:
      (u,v) in R, (v,w) in S, (w,x) in T.

**BY** expanding D1702's existential definition twice.

<1>2. Membership in `(T o S) o R` is equivalent to the same formula.
**BY** the same expansion, with the two bound variables introduced in the
opposite syntactic order.

<1>3. Hence `T o (S o R)=(T o S) o R`.
**BY** extensional equality and `<1>1`--`<1>2`.

<1>4. For `R:V->W`, `(v,w) in Delta_W o R` iff there exists `w'` with
`(v,w') in R` and `w'=w`; hence `Delta_W o R=R`.
**BY** D1702.

<1>5. Similarly `R o Delta_V=R`.
**BY** D1702.

<1>6. The diagonal `Delta_V` is Lagrangian in `bar(V)+V`, including
`V=0`.

  <2>1. Its form on `(v,v),(v',v')` is
  `-omega_V(v,v')+omega_V(v,v')=0`.
  **BY** D1701.

  <2>2. Its dimension is `dim V`, half of `dim(bar(V)+V)`.
  **BY** the diagonal is linearly isomorphic to `V`.

  <2>3. Isotropy plus half dimension implies the Lagrangian condition by
  section 1 `<1>6`.
  **BY** section 1.

  <2>4. **QED** `<1>6`.

<1>7. Therefore the closed Hom-classes and prescribed diagonals form a
category.
**BY** section 2 and `<1>3`--`<1>6`.

<1>8. **PROVE** converse sends arrows to arrows.

  <2>1. The coordinate exchange

      j:bar(V)+W -> bar(W)+V,  j(v,w)=(w,v)

  multiplies the ambient form by `-1`.
  **BY** direct calculation:
  `-omega_W(w,w')+omega_V(v,v')` is the negative of
  `-omega_V(v,v')+omega_W(w,w')`.

  <2>2. Multiplication of a nondegenerate alternating form by `-1` does not
  change perpendiculars; an anti-symplectic isomorphism therefore sends a
  Lagrangian subspace to a Lagrangian subspace.
  **BY** the definitions; this also holds in characteristic two.

  <2>3. The map `j` sends affine translates to affine translates and empty
  to empty.
  **BY** linearity and bijectivity.

  <2>4. Its image is exactly the relational converse `R^dagger`.
  **BY** D1702.

  <2>5. **QED** `<1>8`.

<1>9. Converse is involutive, fixes every diagonal, and satisfies
`(S o R)^dagger=R^dagger o S^dagger`.
**BY** direct expansion of ordered pairs and existential composition.

<1>10. **QED** the dagger-category laws.
**BY** `<1>7`--`<1>9`.

## 4. Direct-sum tensor and coherence

**ASSUME** arrows `R:V->W` and `R':V'->W'`.  **PROVE** their D1702 product
is an arrow `V+V'->W+W'` and supplies a dagger symmetric monoidal product.

<1>1. The prescribed coordinate reordering is

    chi: (bar(V)+W)+(bar(V')+W')
         -> bar(V+V')+(W+W'),
    chi((v,w),(v',w'))=((v,v'),(w,w')).

**BY** D1702.

<1>2. **PROVE** `chi` is symplectic.

  <2>1. Before reordering, the form is
  `-omega_V+omega_W-omega_(V')+omega_(W')` on the four factors.
  **BY** D1701.

  <2>2. After reordering, it is
  `-(omega_V+omega_(V'))+(omega_W+omega_(W'))`.
  **BY** D1701.

  <2>3. The two expressions agree term by term.
  **BY** commutativity of addition in `k`.

  <2>4. **QED** `<1>2`.

<1>3. If both relations are nonempty, their Cartesian product is an affine
translate of `dir(R)+dir(R')`, which is Lagrangian before reordering and
hence after `chi`.
**BY** section 2 `<1>2`, `<1>2`, and D1702.

<1>4. If either relation is empty, their Cartesian product is empty.
**BY** set-theoretic Cartesian product.

<1>5. Thus the product is closed on arrows.
**BY** `<1>3`--`<1>4`.

<1>6. For composable pairs, `(S+S') o (R+R')` equals
`(S o R)+(S' o R')` after the prescribed coordinate reorder.
**BY** the middle witnesses are independent pairs `(w,w')`; expanding the
existential condition gives equality, including empty factors.

<1>7. `Delta_(V+V')=Delta_V+Delta_(V')` after the same reorder.
**BY** equality of the displayed ordered pairs.

<1>8. Hence product is bifunctorial, and
`(R+R')^dagger=R^dagger+(R')^dagger`.
**BY** `<1>6`--`<1>7` and coordinatewise converse.

<1>9. The canonical vector-space rebracketing, zero-space unitors, and
summand exchange preserve the corresponding direct-sum forms.
**BY** D1701's direct-sum form and direct evaluation on pairs of vectors.

<1>10. Their graphs are D1702 arrows, and graph composition agrees with
function composition.
**BY** section 6 below `<1>1`--`<1>4`; alternatively the same graph
calculation is repeated there without using coherence.

<1>11. The pentagon, triangle, hexagon, and involutive-symmetry diagrams
commute because both routes in each diagram are graphs of the same canonical
coordinate bijection.
**BY** ordinary direct-sum tuple evaluation and `<1>10`.

<1>12. Naturality also holds for arbitrary relations.  For example, the two
associator routes relate `((u,v),w)` to `u'+(v'+w')` exactly when
`(u,u') in R`, `(v,v') in S`, and `(w,w') in T`; the symmetry routes both
exchange the two independent endpoint pairs.  The unitor cases delete the
unique zero coordinate on both routes.
**BY** D1702's Cartesian product and relational composition, using the
canonical tuple maps verified in `<1>9`.

<1>13. The tensor unit is the zero symplectic space, and tensoring with its
identity relation has the prescribed unitor behavior even for empty arrows.
**BY** D1702, `<1>7`, and the unique coordinate of `0`.

<1>14. **QED** dagger symmetric monoidal closure and coherence.
**BY** `<1>5`--`<1>13`.

## 5. Symmetric monoidal structure on the affine symmetry groupoid

**ASSUME** the repaired D1701 prescription for direct sums of affine arrows
and its zero-translation tuple coherence maps.  **PROVE** these data make
`S_k^aff` a symmetric monoidal groupoid.

<1>1. For affine symplectic arrows `f=(t,g):V->W` and
`f'=(t',g'):V'->W'`, the prescribed arrow

    f+f'=((t,t'),g+g'):V+V'->W+W'

is affine symplectic.
**BY** D1701: `g+g'` is a form-preserving linear isomorphism for the
direct-sum forms and `(t,t')` lies in the target.

<1>2. For composable `f,f'` and `h=(s,j),h'=(s',j')`,

    (h+h') o (f+f')
      =((s+jt,s'+j't'),(jg)+(j'g'))
      =(h o f)+(h' o f').

Here `(jg)+(j'g')` is the direct sum of the two displayed linear maps.
**BY** D1701's affine composition and repaired direct-sum prescriptions,
evaluated coordinatewise.

<1>3. The direct sum of the two identity arrows is the identity on the
direct-sum object, and the identity on the zero object is the tensor unit.
**BY** `((0,0),1_V+1_(V'))=(0,1_(V+V'))` and repaired D1701.

<1>4. The associator, unitors, and symmetry have zero translations and the
tuple linear parts shown in repaired D1701; those linear parts are
symplectic by section 4 `<1>9`.
**BY** repaired D1701 and section 4.

<1>5. Naturality holds for affine arrows.  For example, for
`f:U->U'`, `g:V->V'`, and `h:W->W'`, both associator routes send
`((u,v),w)` to

    (f(u),(g(v),h(w))),

and for `g:V->V'`, `h:W->W'`, both symmetry routes send `(v,w)` to
`(h(w),g(v))`.
**BY** the repaired arrow tensor and tuple maps, evaluated pointwise.

<1>6. Pentagon, triangle, hexagon, and involutive-symmetry coherence reduce
to equality of the corresponding tuple maps; all translations remain zero.
**BY** repaired D1701 and ordinary tuple evaluation.

<1>7. Every affine symplectic arrow is invertible under D1701's affine
composition, and direct sum preserves inverses.
**BY** the inverse of `(t,g)` is `(-g^(-1)t,g^(-1))`, checked in D1701's
composition formula, and the calculation is componentwise.

<1>8. **QED** `S_k^aff` is a symmetric monoidal groupoid with the repaired
owned structure.
**BY** `<1>1`--`<1>7`.

## 6. Faithful graph functor

**ASSUME** an affine symplectic arrow `f=(t,g):V->W` in D1701, acting as
`f(v)=gv+t`.  **PROVE** its graph is a D1702 arrow and the graph assignment
is a faithful symmetric monoidal functor.

<1>1. The graph is the affine translate

    Gamma_f = (0,t) + Gamma_g,
    Gamma_g = { (v,gv):v in V } subset bar(V)+W.

**BY** D1701 and the definition of a graph.

<1>2. **PROVE** `Gamma_g` is Lagrangian.

  <2>1. For two graph vectors, the ambient pairing is

      -omega_V(v,v')+omega_W(gv,gv')=0.

  **BY** `g` preserves the symplectic form, D1701.

  <2>2. Since `g` is an isomorphism, `dim V=dim W`, and
  `dim Gamma_g=dim V`, half of `dim(bar(V)+W)`.
  **BY** D1701 and injectivity of `v |-> (v,gv)`.

  <2>3. Hence `Gamma_g` is Lagrangian.
  **BY** isotropy from `<2>1` and the half-dimension argument of section 1.

  <2>4. **QED** `<1>2`.

<1>3. Therefore `Gamma_f` is an affine Lagrangian relation.
**BY** `<1>1`--`<1>2` and D1702.

<1>4. For affine symplectic arrows `f:U->V` and `h:V->W`,

    Gamma_h o Gamma_f = Gamma_(h o f),
    Gamma_(1_V)=Delta_V.

**BY** a middle witness on two functional graphs is uniquely `f(u)`, and
D1701's affine composition formula gives `h(f(u))`.

<1>5. If `Gamma_f=Gamma_h`, then for every `v`, the unique second
coordinate paired with `v` is both `f(v)` and `h(v)`; hence `f=h`.
**BY** equality of graphs and extensional equality of functions.

<1>6. The graph of `f+f'` becomes `Gamma_f+Gamma_(f')` under D1702's exact
coordinate reorder, while the graph of the zero-space identity is
`Delta_0`.
**BY** evaluation on `((v,v'),(f(v),f'(v')))` and repaired D1701--D1702.

<1>7. Graphs of the direct-sum associator, unitors, and symmetry are exactly
the coherence arrows used in section 4.
**BY** repaired D1701's zero-translation tuple maps and their underlying
coordinate functions.

<1>8. Consequently graphs define a faithful symmetric monoidal functor

    S_k^aff -> L_k^aff.

It also sends inverse affine isomorphisms to relational converses.
**BY** section 5, `<1>3`--`<1>7`, and the functional-graph identity
`Gamma_(f^{-1})=(Gamma_f)^dagger`.

<1>9. **QED** the graph clause of `SP-LREL`.
**BY** `<1>8`.

## 7. Exact canonical conclusion

<1>1. For every finite field, D1702 arrows are closed under composition.
**BY** section 2.

<1>2. They form a dagger category.
**BY** section 3.

<1>3. D1702's reordered product and zero unit make it dagger symmetric
monoidal with the canonical direct-sum coherence.
**BY** section 4.

<1>4. Graphs give the claimed faithful symmetric monoidal functor from the
affine symmetry groupoid.
**BY** sections 5--6.

<1>5. Every argument includes the zero object, empty arrows and empty
composites.  The only sign used is D1702's opposite source form, and no step
uses division or an odd-characteristic hypothesis.
**BY** sections 1--6.

<1>6. **QED** the exact current canonical `SP-LREL` statement.
**BY** `<1>1`--`<1>5` and `claims/CLAIMS.md` row `SP-LREL`.
