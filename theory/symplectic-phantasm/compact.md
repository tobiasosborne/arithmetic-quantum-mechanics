# Compact data and state/process correspondence

Lane model: `gpt-5.6-sol`, reasoning `xhigh`.

Admitted proof of `SP-COMPACT`, using the admitted `SP-LREL` dependency.
The exact statement and contract remain in their canonical registers; capped
review and repair dispositions are in
`theory/verdicts/phantasm-relations-adjudication.md`.

Canonical data are D1701--D1702 and D1714.  SP-CK21, section 2 at
local line 1860, states compact closure and currying for its linear
Lagrangian-relation convention.  SP-LW14, local lines 1571--1581, records
opposite-form duals and diagonal unit/counit for linear canonical relations.
The calculations below establish the precise D1702 affine/empty, factor,
dagger, unitor and scalar conventions locally.

Write relation elements with their typed endpoints: for example
`(0,(v,v)) in eta_V` and `((v,v),0) in epsilon_V`.  All `0` entries are the
unique vector of the zero space.  This shorthand introduces no new
canonical symbols.

## 1. Coherence and Lagrangian typing

**ASSUME** a finite field `k`, D1714, and the `SP-LREL` conclusion
for the D1702 category.  **PROVE** the prescribed coherence maps, cup and
cap have the required types in `L_k^aff`.

<1>1. **PROVE** the tuple maps `a`, `lambda`, `rho`, and `sigma` prescribed
in D1714 are symplectic linear isomorphisms.

  <2>1. For `a_(U,V,W)`, both source and target forms evaluate on the tuple
  entries as

      omega_U(u,u')+omega_V(v,v')+omega_W(w,w').

  **BY** D1701's direct-sum form and the D1714 tuple map.

  <2>2. The map `a` and its inverse are the two bracketings of the same
  tuple, hence are linear inverse maps.
  **BY** direct tuple evaluation.

  <2>3. Since the zero-space form vanishes, each of `lambda_V` and `rho_V`
  and its displayed inverse preserves `omega_V`.
  **BY** D1701 and D1714.

  <2>4. For `sigma_(V,W)`, the source pairing
  `omega_V(v,v')+omega_W(w,w')` equals the target pairing after exchange.
  The exchange is its own linear inverse.
  **BY** D1701, D1714, and commutativity of addition in `k`.

  <2>5. **QED** `<1>1`.

<1>2. The graphs of these maps are affine Lagrangian relations, and their
graph composites obey the ordinary direct-sum coherence diagrams.
**BY** the explicit `SP-LREL` dependency, specifically the graph and
coherence clauses proved in `lrel-laws.md` sections 4--6.

<1>3. **PROVE** `eta_V:0->bar(V)+V` is a linear Lagrangian relation.

  <2>1. Its ambient symplectic space is `bar(V)+V`, and its direction is
  the diagonal `D_V={(v,v):v in V}`.
  **BY** D1702's morphism convention and D1714.

  <2>2. On diagonal vectors the ambient form is

      -omega_V(v,w)+omega_V(v,w)=0.

  **BY** D1701.

  <2>3. Thus `D_V` is isotropic.  Its dimension is `dim V`, exactly half
  of `dim(bar(V)+V)`.
  **BY** the diagonal is linearly isomorphic to `V` and D1701.

  <2>4. A half-dimensional isotropic subspace of a finite-dimensional
  symplectic space is Lagrangian.
  **BY** `lrel-reduction.md` section 1 `<1>6`.

  <2>5. Therefore `eta_V` is a D1702 arrow of the stated type.
  **BY** `<2>1`--`<2>4` and D1702.

  <2>6. **QED** `<1>3`.

<1>4. **PROVE** `epsilon_V:V+bar(V)->0` is a linear Lagrangian relation.

  <2>1. The ambient symplectic space for this morphism is

      overline(V+bar(V))+0 = bar(V)+V.

  **BY** D1702's opposite-source convention and D1701's opposite and
  direct-sum forms.

  <2>2. Under this exact source order, D1714's pairs `((v,v),0)` give the
  diagonal in `bar(V)+V`.
  **BY** D1714.

  <2>3. That diagonal is Lagrangian by `<1>3.<2>2`--`<1>3.<2>4`.
  **BY** those steps.

  <2>4. Therefore `epsilon_V` is a D1702 arrow of its stated type.
  **BY** D1702.

  <2>5. **QED** `<1>4`.

<1>5. The proofs of `<1>3`--`<1>4` use the cancellation `x-x=0`, not
division by two.  They include characteristic two and `V=0`.
**BY** inspection of the displayed form calculations.

<1>6. **QED** all D1714 maps are correctly typed D1702 arrows.
**BY** `<1>2`--`<1>5`.

## 2. The first snake

**ASSUME** `x in V`.  Consider the fully typed D1714 composite

    V --rho_V^(-1)--> V+0
      --(1_V+eta_V)--> V+(bar(V)+V)
      --a_(V,bar(V),V)^(-1)--> (V+bar(V))+V
      --(epsilon_V+1_V)--> 0+V
      --lambda_V--> V.

**PROVE** this relation is `1_V`.

<1>1. The graph of `rho_V^(-1)` relates `x` only to `(x,0)`.
**BY** D1714.

<1>2. The product `1_V+eta_V` relates `(x,0)` to

    (x,(u,u))

for every `u in V`.
**BY** D1714's diagonal cup and D1702's product of relations.

<1>3. The graph of `a^(-1)` relates this only to `((x,u),u)`.
**BY** the exact D1714 tuple map.

<1>4. The relation `epsilon_V+1_V` accepts `((x,u),u)` exactly when
`x=u`, and then relates it to `(0,u)`.
**BY** D1714's cap `((v,v),0)` and the identity relation on the last
factor.

<1>5. The graph of `lambda_V` takes `(0,u)` to `u`.
**BY** D1714.

<1>6. Consequently the composite relates `x` to `y` exactly when there is
`u` with `x=u=y`, which is exactly `Delta_V`.
**BY** `<1>1`--`<1>5` and existential relational composition from D1702.

<1>7. Hence

    lambda_V o (epsilon_V+1_V) o a_(V,bar(V),V)^(-1)
      o (1_V+eta_V) o rho_V^(-1) = 1_V.

**BY** `<1>6` and D1702's identity.

<1>8. **QED** the first fully typed snake equation.
**BY** `<1>7`.

## 3. The second snake

**ASSUME** `x in bar(V)`, meaning the underlying vector `x in V` with the
opposite form.  Consider

    bar(V) --lambda_(bar(V))^(-1)--> 0+bar(V)
      --(eta_V+1_(bar(V)))--> (bar(V)+V)+bar(V)
      --a_(bar(V),V,bar(V))--> bar(V)+(V+bar(V))
      --(1_(bar(V))+epsilon_V)--> bar(V)+0
      --rho_(bar(V))--> bar(V).

**PROVE** this relation is `1_(bar(V))`.

<1>1. The graph of `lambda_(bar(V))^(-1)` relates `x` only to `(0,x)`.
**BY** D1714.

<1>2. The product `eta_V+1_(bar(V))` relates `(0,x)` to
`((u,u),x)` for every `u in V`.
**BY** D1714 and D1702.

<1>3. The associator graph relates this only to `(u,(u,x))`.
**BY** D1714.

<1>4. The relation `1_(bar(V))+epsilon_V` accepts this tuple exactly when
`u=x`, and then produces `(u,0)`.
**BY** D1714's exact cap order.

<1>5. The graph of `rho_(bar(V))` sends `(u,0)` to `u`.
**BY** D1714.

<1>6. Thus the composite relates `x` to `y` exactly when
`x=u=y`, so it is the diagonal relation on `bar(V)`.
**BY** `<1>1`--`<1>5` and D1702.

<1>7. Hence

    rho_(bar(V)) o (1_(bar(V))+epsilon_V)
      o a_(bar(V),V,bar(V)) o (eta_V+1_(bar(V)))
      o lambda_(bar(V))^(-1) = 1_(bar(V)).

**BY** `<1>6`.

<1>8. **QED** the second fully typed snake equation.
**BY** `<1>7`.

## 4. Dagger compatibility and compact dual coherence

**PROVE** the D1714 cup and cap are compatible with D1702's dagger and the
opposite-form dual.

<1>1. Relational converse sends

    eta_V = { (0,(v,v)) : v in V }

to the relation `{((v,v),0):v in V}` from `bar(V)+V` to `0`.
**BY** D1702 and D1714.

<1>2. The swap `sigma_(bar(V),V)` sends `(v,v)` in `bar(V)+V` to the same
ordered diagonal pair in `V+bar(V)`.
**BY** D1714's tuple map.

<1>3. Therefore

    eta_V^dagger = epsilon_V o sigma_(bar(V),V).

**BY** `<1>1`--`<1>2`.

<1>4. Taking daggers and using the explicit `SP-LREL` dagger monoidal laws
also gives

    epsilon_V^dagger = sigma_(bar(V),V) o eta_V.

**BY** `<1>3`, involutivity, and self-adjointness of the swap graph.

<1>5. Directly, `eta_V^dagger=epsilon_(bar(V))` and
`epsilon_V^dagger=eta_(bar(V))`, after the exact double-opposite
identification.
**BY** D1701 gives `overline(bar(V))=V`; compare the ordered diagonal sets.

<1>6. On objects,

    overline(overline(V))=V,  overline(0)=0,
    overline(V+W)=bar(V)+bar(W)

with equality of the prescribed forms.
**BY** D1701 and multiplication of the form by `-1` twice.

<1>7. In the symmetric direct-sum category, the standard reversal
comparison from `bar(V)+bar(W)` to `bar(W)+bar(V)` is D1714's swap graph;
its coherence is part of the `SP-LREL` dependency.
**BY** D1714 and `SP-LREL`.

<1>8. The two snakes and `<1>3` provide the compact and dagger-compatible
axioms for the chosen dual, with the associator and unitors shown rather
than suppressed.
**BY** sections 2--3 and the definition of dagger compact data.

<1>9. **QED** dagger compact compatibility.
**BY** `<1>3`--`<1>8`.

## 5. Name and unname

**ASSUME** a D1702 arrow `R:V->W`.  **PROVE** its D1714 name has exactly
the same ordered subset of `V x W`.

<1>1. The cup relates `0` to `(v,v)` for every `v in V`.
**BY** D1714.

<1>2. The relation `1_(bar(V))+R` relates `(v,v)` to `(v,w)` exactly when
`(v,w) in R`.
**BY** D1702's product and identity.

<1>3. Hence

    (0,(v,w)) in name(R) iff (v,w) in R.

**BY** `<1>1`--`<1>2` and existential composition.

<1>4. If `R` is empty, its name is empty; if it is an affine Lagrangian
translate, its name is that same affine subset of `bar(V)+W`, now typed as
a state.
**BY** `<1>3` and D1702.

<1>5. **QED** the name calculation.
**BY** `<1>3`--`<1>4`.

**ASSUME** a D1702 state `Q:0->bar(V)+W`.  **PROVE** its D1714 unname has
exactly the same ordered subset of `V x W`.

<1>6. The graph of `rho_V^(-1)` sends `v` to `(v,0)`.
**BY** D1714.

<1>7. The product `1_V+Q` relates `(v,0)` to `(v,(u,w))` exactly when
`(0,(u,w)) in Q`.
**BY** D1702's product.

<1>8. The inverse associator graph sends this tuple to `((v,u),w)`.
**BY** D1714.

<1>9. The product `epsilon_V+1_W` accepts this exactly when `v=u`, and
then gives `(0,w)`.
**BY** D1714's cap order.

<1>10. The left unitor graph sends `(0,w)` to `w`.
**BY** D1714.

<1>11. Thus

    (v,w) in unname(Q) iff (0,(v,w)) in Q.

**BY** `<1>6`--`<1>10` and D1702's existential composition.

<1>12. This also sends the empty state to the empty relation and retains
every nonempty affine translate as the same ordered subset.
**BY** `<1>11`.

<1>13. Applying `<1>3` then `<1>11`, or in the reverse order, is the
identity on the respective Hom-set.
**BY** the two biconditionals.

<1>14. Therefore name and unname are inverse bijections

    L_k^aff(V,W)  <->  L_k^aff(0,bar(V)+W)

including affine, nonfunctional, and empty relations.
**BY** `<1>5`--`<1>13`.

<1>15. **QED** the state/process correspondence.
**BY** `<1>14`.

## 6. Scalars and the closed loop

**PROVE** the exact scalar clauses of registered `SP-COMPACT`.

<1>1. A relation from `0` to `0` is a subset of the singleton `0 x 0`.
**BY** the zero vector space has one element.

<1>2. D1702 permits the empty relation.  Its only nonempty affine
Lagrangian relation is the affine translate of the unique subspace of the
zero ambient space, namely `Delta_0`.
**BY** D1702 and uniqueness of the zero subspace.

<1>3. Hence

    End_(L_k^aff)(0) = { empty, Delta_0 }.

**BY** `<1>1`--`<1>2`.

<1>4. Composition with the empty relation is empty, while
`Delta_0 o Delta_0=Delta_0`.
**BY** D1702's existential relational composition on a singleton.

<1>5. For scalars `s,t`, D1714's fully unital scalar tensor is

    lambda_0 o (s+t) o lambda_0^(-1):0->0.

If either scalar is empty then its Cartesian product is empty and the
transported composite is empty.  If both are `Delta_0`, their Cartesian
product is `Delta_(0+0)` and transport by the unitor graph gives `Delta_0`.
**BY** D1702's Cartesian product and D1714's scalar tensor and
zero unitor.

<1>6. Thus composition and the transported scalar tensor give the two
scalars the Boolean multiplication table, with empty absorbing and
`Delta_0` the identity.
**BY** `<1>3`--`<1>5`.

<1>7. Consider the fully typed closed relation

    0 --eta_V--> bar(V)+V
      --sigma_(bar(V),V)--> V+bar(V)
      --epsilon_V--> 0.

**BY** D1714.

<1>8. The cup supplies `(v,v)` for every `v`; the swap retains the
diagonal; and the cap accepts every such diagonal pair.
**BY** D1714.

<1>9. A witness exists for every `V`, including `V=0`, because every
vector space contains its zero vector.
**BY** the vector-space axioms.

<1>10. Relational composition records only existence of a middle witness,
so the loop is the unique nonempty relation `Delta_0`; it does not record
`|V|` or any amplitude.
**BY** D1702, `<1>3`, and `<1>8`--`<1>9`.

<1>11. Therefore

    epsilon_V o sigma_(bar(V),V) o eta_V = Delta_0.

**BY** `<1>10`.

<1>12. **QED** the scalar and closed-loop clauses.
**BY** `<1>3`, `<1>6`, and `<1>11`.

## 7. Exact proposed conclusion

<1>1. Cups, caps and every displayed coherence graph are D1702 arrows over
every finite field.
**BY** section 1.

<1>2. The two fully typed snake equations hold, and the cup/cap obey the
claimed dagger equation.
**BY** sections 2--4.

<1>3. Name and unname give the claimed inverse Hom-set bijection and retain
the empty relation.
**BY** section 5.

<1>4. The scalar monoid and closed loop have exactly the claimed
witness-forgetting values.
**BY** section 6.

<1>5. Together with the explicit `SP-LREL` dependency, D1714 therefore
equips `L_k^aff` with the proposed dagger compact structure.
**BY** `<1>1`--`<1>4`, `SP-LREL`, and the dagger compact axioms.

<1>6. The proof is classical.  It makes no assignment to Hilbert spaces,
operators or CP maps and introduces no normalization or Choi assertion.
**BY** inspection of sections 1--6 and the D1714 scope.

<1>7. **QED** the exact registered `SP-COMPACT` statement, with `SP-LREL`
retained as its admitted dependency.
**BY** `<1>1`--`<1>6`, the canonical `SP-COMPACT` row in
`claims/CLAIMS.md`, and its `claims/PHANTASM-DAG.md` contract.
