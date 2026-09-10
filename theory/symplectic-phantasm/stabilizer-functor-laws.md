# Composition, dagger, and tensor for the intertwiner line

Lane model: `gpt-5.6-sol`, reasoning `xhigh`.

Admitted proof component for `SP-STAB-REL`; see
`theory/verdicts/phantasm-relations-adjudication.md`. This shard uses the line and recovery results of
`stabilizer-intertwiner-line.md`, the explicit `SP-LREL` dependency for affine
composition, and admitted SP-WEYL/SP-TENSOR.  It proves functoriality by
finite Weyl projector calculations, including the case in which two
nonempty relations have empty composite.

Keep the abbreviations `psi`, `V_j`, `H_j`, `W_j`, `Omega`, `rho`, and
`chi_r` from the companion shard.

## 1. Stabilizer eigenspace lemma

**ASSUME** an isotropic subspace `A subset V_j` and a character
`lambda:A->U(1)`.  Put

    K(A,lambda)={xi in H_j:W_j(a)xi=lambda(a)xi for every a in A},
    P_(A,lambda)=(1/|A|) sum_(a in A) lambda(a)^(-1)W_j(a).

**PROVE** `P_(A,lambda)` is the orthogonal projector onto `K(A,lambda)`,
`dim K=p^j/|A|`, and the Weyl operators labelled by `A^perp` span the full
endomorphism algebra of `K` after restriction.

<1>1. On the isotropic group `A`, D1703's half-form multiplier is one, so
`a |-> W_j(a)` is an ordinary unitary representation.
**BY** D1703 and `omega_j(A,A)=0`.

<1>2. The character average is an orthogonal projector onto the displayed
simultaneous eigenspace.
**BY** the reindexing and adjoint calculation of `stabilizer-intertwiner-line.md`
section 3 `<1>4`, applied to this restricted Weyl representation.

<1>3. SP-WEYL's trace formula gives

    Tr(P_(A,lambda))=p^j/|A|,

because only `a=0` contributes.
**BY** admitted SP-WEYL and the projector formula.

<1>4. Hence `dim K(A,lambda)=p^j/|A|`.
**BY** `<1>2`--`<1>3`.

<1>5. If `x in A^perp`, then `W_j(x)` commutes with every `W_j(a)`, so it
preserves `K(A,lambda)`.
**BY** D1703's Weyl commutator
`W(a)W(x)=psi(omega(a,x))W(x)W(a)`.

<1>6. Choose one representative from each coset of `A` in `A^perp`.
For distinct representatives `x,y`, the restricted operators are
Hilbert--Schmidt orthogonal:

    Tr_K((W(x)|_K)^* W(y)|_K)=0.

**BY** write the trace as a nonzero scalar times
`Tr(P_(A,lambda)W(y-x))`; expanding `P`, SP-WEYL permits a nonzero term
only if `y-x in A`, excluded by the representatives.

<1>7. Each restricted operator is unitary and hence nonzero.
**BY** `<1>5` and D1703's unitarity.

<1>8. The number of cosets is

    |A^perp/A|=p^(2j)/|A|^2=(dim K(A,lambda))^2.

**BY** nondegeneracy gives `dim A^perp=2j-dim A`, and `<1>4`.

<1>9. Thus the restricted Weyl operators in `<1>6` are an orthogonal
basis of `End_C(K(A,lambda))`.
**BY** `<1>6`--`<1>8` and the dimension of an endomorphism algebra.

<1>10. Any operator on `K(A,lambda)` commuting with all these restrictions
is scalar.
**BY** `<1>9`, since it then commutes with every endomorphism, in particular
the matrix units.

<1>11. **QED** the stabilizer eigenspace lemma.
**BY** `<1>2`, `<1>4`, and `<1>9`--`<1>10`.

## 2. Initial and final supports of an intertwiner

**ASSUME** `R=r+L:V_m->V_n` is nonempty and
`0 != T in E_p(R)`.  Write `r=(r_m,r_n)` and put

    A_R={a in V_n:(0,a) in L},
    B_R={b in V_m:(b,0) in L},
    lambda_R^out(a)=psi(-omega_n(r_n,a)),
    lambda_R^in(b)=psi(-omega_m(r_m,b)).

**PROVE** `TT^*` and `T^*T` are positive nonzero scalar multiples of the
corresponding eigenspace projectors.

<1>1. `A_R` and `B_R` are isotropic.
**BY** restrict the vanishing ambient form on the Lagrangian `L` to pairs
`(0,a)` and to pairs `(b,0)`.

<1>2. D1715's equation at `(0,a)` is

    W_n(a)T=lambda_R^out(a)T.

Hence `P_R^out T=T`, where `P_R^out=P_(A_R,lambda_R^out)`.
**BY** D1715 and section 1.

<1>3. D1715's equation at `(b,0)`, after taking adjoints, is

    W_m(b)T^*=lambda_R^in(b)T^*.

Hence `P_R^in T^*=T^*`, where `P_R^in=P_(B_R,lambda_R^in)`.
**BY** `Omega(r,(b,0))=-omega_m(r_m,b)`, conjugation of the character,
and section 1.

<1>4. **PROVE** `pr_n(L)=A_R^perp`.

  <2>1. If `a in A_R`, isotropy of `L` gives
  `omega_n(a,w)=0` for every `(v,w) in L`.
  **BY** pair `(0,a)` with `(v,w)` in the ambient form.

  <2>2. Conversely, if `a` is perpendicular to every output `w`, then
  `(0,a)` is perpendicular to all of `L`; Lagrangianity gives
  `(0,a) in L`.
  **BY** `L=L^perp`.

  <2>3. Thus `(pr_n L)^perp=A_R`, and taking perpendiculars gives the
  claim.
  **BY** `<2>1`--`<2>2` and finite-dimensional nondegeneracy.

  <2>4. **QED** `<1>4`.

<1>5. For `w in A_R^perp`, choose `v` with `(v,w) in L`.  The line equation
gives `W_n(w)T=cT W_m(v)` for a unit scalar `c`, and therefore

    W_n(w)TT^*W_n(w)^*=TT^*.

**BY** `<1>4`, D1715, and unitarity.

<1>6. By `<1>2`, `TT^*=P_R^out TT^*P_R^out`; by `<1>5` it commutes on the
range of `P_R^out` with every restricted Weyl operator from `A_R^perp`.
**BY** those steps.

<1>7. The eigenspace lemma forces

    TT^*=c_R P_R^out

for a real `c_R>0`.
**BY** section 1 `<1>10`, positivity of `TT^*`, and `T != 0`.

<1>8. Applying the same argument to the adjoint equations in `<1>3` gives

    T^*T=d_R P_R^in

with `d_R>0`.
**BY** interchange input and output and use the converse Lagrangian
direction; the ambient form changes sign, which does not change
perpendiculars.

<1>9. Therefore `T` maps `ran P_R^in` injectively onto `ran P_R^out`, is
zero on the orthogonal complement of `ran P_R^in`, and has full range
`ran P_R^out`.
**BY** `<1>7`--`<1>8`: the two positive equations give the kernel and range,
and the nonzero singular values are positive.

<1>10. **QED** the exact initial/final support lemma.
**BY** `<1>7`--`<1>9`.

## 3. When the middle supports overlap

**ASSUME** nonempty `R=r+L:V_m->V_n` and
`S=s+M:V_n->V_q`.  Let `A=A_R` be the output subgroup of `R` and let
`B=B_S` be the input subgroup of `S`, with projectors `P_A,P_B` from
section 2.  **PROVE** `P_B P_A` is nonzero exactly when `S o R` is
nonempty.

<1>1. The middle projections are

    pr_n(R)=r_n+A^perp,
    pr_n(S)=s_n+B^perp.

**BY** section 2 `<1>4` and its input analogue.

<1>2. These affine subspaces meet exactly when
`s_n-r_n in A^perp+B^perp`.
**BY** solve `r_n+x=s_n+y` with `x in A^perp`, `y in B^perp`.

<1>3. By nondegeneracy, the condition in `<1>2` is equivalent to

    omega_n(h,s_n-r_n)=0 for every h in A cap B.

**BY** `(A^perp+B^perp)^perp=A cap B` and double perpendiculars.

<1>4. Since `psi` is faithful, `<1>3` holds exactly when the characters
`lambda_R^out` and `lambda_S^in` agree on `A cap B`.
**BY** their formulas in section 2 and
`psi(omega_n(s_n-r_n,h))=1` iff the exponent is zero.

<1>5. Expanding both group averages and using SP-WEYL's trace formula gives

    Tr(P_B P_A)
      =p^n |A cap B|/(|A||B|)

when the characters agree on `A cap B`, and zero otherwise.
**BY** only pairs `(b,a)` with `b+a=0` contribute; their character sum is
the sum of one character over `A cap B`, equal to its order for the trivial
character and zero for a nontrivial character.

<1>6. Because `P_A,P_B` are orthogonal projectors,

    Tr(P_B P_A)=Tr((P_B P_A)^*(P_B P_A))=||P_B P_A||_HS^2.

**BY** idempotence and cyclicity of trace.

<1>7. Thus `P_B P_A != 0` exactly when the affine middle projections meet.
**BY** `<1>4`--`<1>6`.

<1>8. The projections meet exactly when `S o R` is nonempty.
**BY** D1702's existential middle-point definition.

<1>9. **QED** the overlap criterion.
**BY** `<1>7`--`<1>8`.

## 4. Composition, including empty composites

**ASSUME** `T in E_p(R)` and `U in E_p(S)`, choosing nonzero maps when the
relations are nonempty.  **PROVE**

    E_p(S) E_p(R)=E_p(S o R)

as one-dimensional product lines, with both sides `{0}` for an empty
composite.

<1>1. If `R` or `S` is empty, then `T=0` or `U=0`, and D1702 makes the
composite empty.
**BY** D1715 and existential relational composition.

<1>2. Suppose both are nonempty.  Section 2 gives

    U T=U P_B P_A T.

**BY** `U=UP_B` from its initial support and `T=P_A T` from its range.

<1>3. If `S o R` is empty, the overlap criterion gives `P_B P_A=0`, hence
`UT=0`.
**BY** sections 2--3 and `<1>2`.

<1>4. If `S o R` is nonempty, then `P_B P_A !=0`.  Since `T` maps onto
`ran P_A` and `U` is injective on `ran P_B`, `<1>2` gives `UT !=0`.
**BY** section 2 `<1>9` and section 3.

<1>5. In the nonempty case choose a middle point `w_0` and origins

    r'=(v_0,w_0) in R,  s'=(w_0,z_0) in S.

Origin independence permits these replacements.
**BY** D1702's nonempty-composite condition and
`stabilizer-intertwiner-line.md` section 2.

<1>6. Let `(v,z)` lie in the direction of `S o R`, and choose `w` with
`(v,w) in L`, `(w,z) in M`.  Applying the two line equations gives

    W_q(z)UTW_m(v)^*
      =psi(-Omega_R(r',(v,w))-Omega_S(s',(w,z)))UT.

**BY** first move `W_q(z)` through `U` using the `S` equation, then move
`W_n(w)` through `T` using the `R` equation.

<1>7. The middle terms cancel:

    Omega_R(r',(v,w))+Omega_S(s',(w,z))
      =-omega_m(v_0,v)+omega_q(z_0,z).

**BY** expand both forms; the terms
`omega_n(w_0,w)` occur with opposite signs.

<1>8. The right side of `<1>7` is the composite ambient form evaluated at
origin `(v_0,z_0)` and direction `(v,z)`.  Thus `UT in E_p(S o R)`.
**BY** D1715, SP-LREL's affine-composition closure, and origin independence
from `stabilizer-intertwiner-line.md` section 2, which makes the equation for this one
composite origin equivalent to the all-origin definition.

<1>9. In the nonempty case both the product and target lines are nonzero
and the target is one-dimensional, so they are equal.  In the empty case
both are `{0}` by `<1>1` or `<1>3`.
**BY** `<1>1`--`<1>4`, `<1>8`, and `stabilizer-intertwiner-line.md` section 3.

<1>10. **QED** exact composition, including nonempty factors with empty
composite.
**BY** `<1>9`.

## 5. Identities and bare-converse dagger

**PROVE** the line assignment preserves identities and D1702's dagger.

<1>1. For `Delta_(V_m)` choose origin zero and direction
`{(v,v):v in V_m}`.  Its line equations are

    W_m(v)T W_m(v)^*=T  for every v.

**BY** D1702 and D1715.

<1>2. SP-WEYL says the Weyl operators span the full matrix algebra, so their
commutant is `C 1`.  Hence `E_p(Delta_(V_m))=C 1_(H_m)`.
**BY** admitted SP-WEYL and `<1>1`.

<1>3. Let `R=r+L` and let `R^dagger=r^dagger+L^dagger`, where endpoint
coordinates are exchanged.  Its ambient form satisfies

    Omega_dagger(r^dagger,(w,v))=-Omega(r,(v,w)).

**BY** D1702's bare converse and its opposite-source forms.

<1>4. Taking adjoints in D1715's equation gives

    W_m(v)T^*W_n(w)^*
      =psi(Omega(r,(v,w)))T^*,

which is exactly the equation for `E_p(R^dagger)` by `<1>3`.
**BY** conjugation of `psi` and reversal of the operator product.

<1>5. Thus `E_p(R^dagger)=E_p(R)^*`; both sides are nonzero lines when
`R` is nonempty and are `{0}` when it is empty.
**BY** `<1>4`, the line theorem, and D1715's empty prescription.

<1>6. This is the required bare-converse/Hilbert-adjoint bridge.  It does
not use SP-BC24's time-reversed dagger.
**BY** `<1>3`--`<1>5` and the source audit.

<1>7. **QED** identity and dagger preservation.
**BY** `<1>2` and `<1>5`.

## 6. Tensor and symmetric coherence

**ASSUME** relations `R:V_m->V_n`, `S:V_a->V_b` and line representatives
`T,U`.  **PROVE** tensor preservation in D1702/D1704's grouped order.

<1>1. If either relation is empty, D1702's Cartesian product is empty and
`T tensor U=0`.
**BY** D1702 and D1715.

<1>2. Otherwise choose product origin `(r,s)` and product direction
`L+M`, using D1702's explicit regrouping to source coordinates
`(v,x)` and target coordinates `(w,y)`.
**BY** D1702.

<1>3. SP-TENSOR identifies the standard grouped Weyl operator exactly as

    W_(n+b)(w,y)=W_n(w) tensor W_b(y)

and likewise on the source.
**BY** admitted SP-TENSOR and D1704's Hilbert identification.

<1>4. Tensoring the two line equations and adding their form exponents
shows `T tensor U in E_p(R+S)`.
**BY** `<1>2`--`<1>3`, D1715, and additivity of `psi`.

<1>5. Both sides are nonzero one-dimensional lines, so

    E_p(R+S)=E_p(R) tensor E_p(S).

**BY** the line theorem and `<1>4`.

<1>6. At rank zero, the identity line is `C->C`; hence the object and arrow
units agree with D1704.
**BY** section 5 `<1>2` at `m=0` and D1704.

<1>7. For the direct-sum swap graph, the Hilbert tensor swap satisfies its
line equations by direct evaluation on pure tensors; uniqueness of the line
makes its projective class the image of the symmetry.
**BY** SP-TENSOR's symmetry diagram and the line theorem.

<1>8. Associators and unitors similarly use D1704's named basis
identifications and obey their diagrams exactly before taking projective
classes.
**BY** SP-TENSOR's associativity/unit diagrams and D1704.

<1>9. **QED** strong symmetric monoidal preservation.
**BY** `<1>1`--`<1>8`.

## 7. Shard conclusion

<1>1. The line assignment respects identities and every composition,
including zero products caused by empty affine fiber intersections.
**BY** sections 3--5.

<1>2. It sends D1702 bare converse to Hilbert adjoint.
**BY** section 5.

<1>3. It preserves the grouped tensor, zero unit, and symmetric coherence.
**BY** section 6.

<1>4. **QED** all functor, dagger, and symmetric monoidal clauses of the
refined SP-STAB-REL statement, subject to the target-membership and fullness
argument in the next shard.
**BY** `<1>1`--`<1>3`.
