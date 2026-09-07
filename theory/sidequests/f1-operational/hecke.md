# The ordered type-A Hecke tower as a finite operational quantum sector

Status: F1-HCK-POS/FLAG/TOWER/OPS/LOW/Q are PROVED after one Sol critic
round and coordinator repair; the extraction scope in section 7 is SKETCH.
Definitions D1101–D1105 are in definitions.md. Source tags H1/H2/H3
mean Iwahori 1964, Umegaki 1954 and Stinespring 1955, registered in
refs/LEDGER.md and local under refs/f1/. See the operational adjudication.

Scope: the positive result is the ordered tower of finite traced C*-algebras,
its parabolic inclusions and conditional expectations, its finite-field flag
model, and its intrinsic level-three parameter.  The final section states the
exact bridge still missing to full arithmetic Weyl--Heisenberg quantum
mechanics.

## 1. Faithful positivity of the coefficient trace (`F1-HCK-POS`)
<1>1. **ASSUME** `q>0`, `n>=0`, and D1101.
<1>2. **PROVE** the reduced elements `T_w`, `w in S_n`, form a basis and
`T_w^*=T_(w^-1)`.
<2>1. For `n<=1` this is D1101, so suppose `n>=2`.
<2>2. Put `s_i=(i,i+1)` and let `ell` be Coxeter length on `S_n`.
<2>3. On the vector space `V_n` with basis `(b_w)_(w in S_n)`, define

    L_i b_w = b_(s_i w)                         if ell(s_i w)=ell(w)+1,
              q b_(s_i w)+(q-1)b_w             if ell(s_i w)=ell(w)-1.
<2>4. On every two-element string `{w,s_iw}`, the matrix of `L_i`, ordered
from shorter to longer, is `[[0,q],[1,q-1]]`; hence
`(L_i-q)(L_i+1)=0`.
<2>5. If `|i-j|>1`, the four-element rank-two strings give
`L_iL_j=L_jL_i`; if `|i-j|=1`, the six-element rank-two strings give
`L_iL_jL_i=L_jL_iL_j`.
<3>1. The length comparisons on such a string are exactly those in the
Coxeter groups `S_2 x S_2` and `S_3`.
<3>2. Substitution of the two cases in <2>3 on their four or six basis
vectors gives the asserted identities.
<3>3. This is the standard rank-two verification of the relations; H1,
Theorem 3.2, pp. 231--232, records the same relations in the finite-field
model.
<2>6. Thus `T_i -> L_i` defines a representation of the presented algebra.
<2>7. Coxeter braid moves connect any two reduced expressions (H1, Theorem
2.6, pp. 224--228), so the reduced product `T_w` is well-defined.
<2>8. Repeatedly replacing a nonreduced adjacent square by
`T_i^2=q+(q-1)T_i`, and applying braid moves, expresses every word as a
linear combination of the `T_w`.
<2>9. For a reduced expression of `w`, every prefix raises length, so
`L_w b_e=b_w`.
<2>10. If `sum_w c_w T_w=0`, applying its regular-model image to `b_e`
gives `sum_w c_w b_w=0`; hence every `c_w=0`.
<2>11. The defining relations are stable under conjugation and reversal;
therefore `T_i^*=T_i` defines an anti-involution and
`T_w^*=T_(w^-1)`.
<2>12. Steps <2>8 and <2>10 prove the basis assertion, and <2>11 proves the
star assertion. **QED**
<1>3. **PROVE**
`tau_n(T_u^*T_v)=delta_(u,v)q^ell(u)`.
<2>1. Give `V_n` the Hermitian form, linear in the second argument,

    <b_u,b_v> = delta_(u,v) q^ell(u).
<2>2. Each `L_i` is self-adjoint for this form.
<3>1. It is enough to inspect a string `{u,s_i u}` with
`ell(s_i u)=ell(u)+1`.
<3>2. The off-diagonal pairings are

    <L_i b_u,b_(s_i u)> = q^(ell(u)+1),
    <b_u,L_i b_(s_i u)> = q q^ell(u).
<3>3. The diagonal pairings agree from the same two-by-two matrix, so the
claim follows because `q^(ell(u)+1)=q q^ell(u)`.
<2>3. Under the vector-space identification `T_w <-> b_w`, the coefficient
of `T_e` in `x` is `<b_e,L_x b_e>`.
<2>4. Therefore

    tau_n(T_u^*T_v)
      = <b_e,L_(T_u^*T_v)b_e>
      = <L_(T_u)b_e,L_(T_v)b_e>
      = <b_u,b_v>
      = delta_(u,v)q^ell(u).
<2>5. This proves the displayed identity. **QED**
<1>4. **PROVE** `tau_n` is a faithful normalized trace.
<2>1. Normalization is `tau_n(1)=tau_n(T_e)=1` by D1101.
<2>2. If `x=sum_w c_wT_w`, <1>3 gives

    tau_n(x^*x)=sum_w |c_w|^2 q^ell(w).
<2>3. Because `q>0`, this is nonnegative and vanishes only for `x=0`.
<2>4. For basis elements, apply <1>3 with `u=x^(-1)` to obtain

    tau_n(T_xT_y)=delta_(x^(-1),y)q^ell(x).
<2>5. The right side is unchanged by swapping `x,y`, because
`y=x^(-1)` implies `ell(y)=ell(x)`; linearity gives `tau_n(ab)=tau_n(ba)`.
<2>6. Hence `tau_n` is positive, faithful, normalized, and tracial. **QED**
<1>5. **PROVE** `H_n(q)` is canonically a finite-dimensional C*-algebra.
<2>1. On `L^2(H_n,tau_n)`, left multiplication satisfies

    <ax,y>=tau_n(x^*a^*y)=<x,a^*y>.
<2>2. Thus the left regular representation is a *-representation.
<2>3. It is faithful because `a1=0` implies `a=0`.
<2>4. Its image is finite-dimensional and therefore operator-norm closed;
with the inherited norm it is a C*-algebra.
<2>5. This proves `F1-HCK-POS`. **QED**

## 2. The complete-flag commutant (`F1-HCK-FLAG`)
<1>6. **ASSUME** `Q` is a prime power, `L` is `n`-dimensional over `F_Q`,
and D1104.
<1>7. **PROVE** `T_w -> A_w` is a trace-preserving *-isomorphism
`H_n(Q) -> Cxt(L)` with no unresolved opposite convention.
<2>1. `GL(L)` acts transitively on `Fl(L)`, and its orbits on ordered pairs
of flags are indexed by relative positions `w in S_n` (Bruhat decomposition;
H1, Lemma 3.1, pp. 230--231).
<2>2. An equivariant operator has a kernel constant on those orbits, so the
`A_w` form a vector-space basis of `Cxt(L)`.
<2>3. Fixing every subspace of a flag except its `i`-dimensional member
amounts to choosing a line in a two-dimensional quotient.
<2>4. There are `Q+1` such lines, hence exactly `Q` other flags in the same
`i`-panel.
<2>5. Two steps in that panel give

    A_(s_i)^2 = Q I + (Q-1) A_(s_i).
<2>6. Minimal galleries give the far-commutation and braid relations, and a
reduced gallery of type `w` gives `A_w`; these are H1, Theorem 3.2,
pp. 231--232.
<2>7. H1, Theorem 4.1, pp. 233--234, says these relations present the Hecke
ring, so D1101 gives a homomorphism `T_w -> A_w`.
<2>8. It is bijective because both displayed families are bases indexed by
`S_n`.
<2>9. Transposing the real orbit kernel reverses relative position, so
`A_w^*=A_(w^-1)`.
<2>10. Only `A_e` has diagonal entries, all equal to one; hence

    tr_Fl(A_w)=delta_(w,e)=tau_n(T_w).
<2>11. We defined multiplication by composition of the adjacency operators.
Thus the map in <2>7 is direct.  H1, Proposition 1.4, pp. 220--221, instead
first obtains an anti-isomorphism from right convolution and then composes
with inversion; the two conventions agree with <2>9.
<2>12. This proves `F1-HCK-FLAG`. **QED**

## 3. Ordered assembly and conditional expectations (`F1-HCK-TOWER`)
<1>8. **ASSUME** D1101--D1102 and `m,n>=0`.
<1>9. **PROVE** `iota_(m,n)` is an injective unital trace-preserving
*-homomorphism.
<2>1. The generators `T_1,...,T_(m-1)` and
`T_(m+1),...,T_(m+n-1)` satisfy the two smaller Hecke presentations and
commute across the omitted bridge generator `T_m`.
<2>2. Therefore their product gives a unital homomorphism with the basis
formula in D1102.
<2>3. Distinct pairs `(u,v)` give distinct standard basis elements
`T_(u x v)`; hence the homomorphism is injective.
<2>4. The block inverse is `u^(-1) x v^(-1)`, so <1>2 proves star
preservation.
<2>5. D1101 gives

    tau_(m+n)(T_(u x v))
      = delta_(u,e)delta_(v,e)
      = (tau_m tensor tau_n)(T_u tensor T_v).
<2>6. This proves all assertions. **QED**
<1>10. **PROVE** the basis projection `E_(m,n)` is the unique
trace-preserving faithful UCP conditional expectation onto the image of
`iota_(m,n)`.
<2>1. By <1>3, the standard basis is orthogonal and the parabolic image is
the span of the basis elements indexed by `S_m x S_n`.
<2>2. Thus the D1102 formula is exactly orthogonal projection in
`L^2(H_(m+n),tau_(m+n))` onto the parabolic subalgebra.
<2>3. Umegaki's theorem H2, pp. 177--179, constructs the trace-preserving
positive conditional expectation as precisely the map characterized by

    tau_(m+n)(x iota(b))
       = (tau_m tensor tau_n)(E_(m,n)(x)b).
<2>4. The characterization and <2>2 identify Umegaki's map with the basis
projection in D1102.
<2>5. It is unital, fixes the subalgebra, is positive and faithful, preserves
the trace, and obeys `E(b_1xb_2)=b_1E(x)b_2` by H2's theorem.
<2>6. It is completely positive.
<3>1. For `x_1,...,x_r in H_(m+n)` and `b_1,...,b_r` in the parabolic
algebra, bimodularity and positivity give

    sum_(i,j) b_i^* E(x_i^*x_j)b_j
      = E((sum_i x_i b_i)^*(sum_j x_j b_j)) >= 0.
<3>2. Hence every Gram matrix `[E(x_i^*x_j)]` is positive over the
subalgebra.
<3>3. If `[a_ij]>=0` in a matrix algebra over `H_(m+n)`, write it `Y^*Y`;
its amplified image is a sum of the positive Gram matrices from <3>2.
<3>4. Therefore every matrix amplification is positive, which is complete
positivity in H3, p. 211.
<2>7. If another trace-preserving conditional expectation existed, the
trace-pairing identity in <2>3 and faithfulness of the restricted trace would
make its difference from `E_(m,n)` zero.
<2>8. This proves the claimed expectation properties. **QED**
<1>11. **PROVE** strict ordered three-block coherence.
<2>1. For `l,m,n>=0`, both composites

    iota_(l+m,n) o (iota_(l,m) tensor id),
    iota_(l,m+n) o (id tensor iota_(m,n))

send `T_u tensor T_v tensor T_w` to `T_(u x v x w)`.
<2>2. Both reverse composites

    (E_(l,m) tensor id) o E_(l+m,n),
    (id tensor E_(m,n)) o E_(l,m+n)

retain `T_x` exactly when `x in S_l x S_m x S_n`, and otherwise send it to
zero.
<2>3. Thus the inclusion and expectation identities hold on bases, hence as
maps.  They are ordered identities: no block swap has been supplied.
<2>4. Steps <1>9--<1>11 prove `F1-HCK-TOWER`. **QED**

## 4. Finite operational semantics (`F1-HCK-OPS`)
<1>12. **ASSUME** the density, effect, Born-probability and UCP conventions of D1106,
and the traced algebras proved in §1.
<1>13. **PROVE** the Hecke levels have normalized densities, Born
probabilities, and CP restriction/coarse graining.
<2>1. In a finite-dimensional C*-algebra with faithful trace, blockwise
matrix duality gives every positive functional uniquely as
`phi_h(x)=tau(hx)` with `h>=0`.
<2>2. The functional is normalized exactly when `tau(h)=1`.
<2>3. If `0<=a<=1`, positivity and normalization give
`0<=phi_h(a)<=phi_h(1)=1`; this is the Born probability.
<2>4. The inclusion `iota` is a unital *-homomorphism and hence UCP; pulling
a state back along it is normalized and positive.
<2>5. The coarse graining `E` is UCP by <1>10.  H3, Theorem 1,
pp. 212--213, supplies its standard dilation interpretation.
<2>6. This proves the first operational assertions. **QED**
<1>14. **PROVE** the ordered product state
`(phi_h tensor phi_k) o E_(m,n)` has density
`iota_(m,n)(h tensor k)` and is associative.
<2>1. If `h,k` are local densities, then `h tensor k>=0` and has product
trace one.
<2>2. For `x in H_(m+n)`, the trace-pairing identity in <1>10 gives

    (phi_h tensor phi_k)(E_(m,n)(x))
      = tau_(m+n)(iota_(m,n)(h tensor k)x).
<2>3. Therefore `iota(h tensor k)` is the density of the ordered product
preparation; it is positive and normalized by <1>9.
<2>4. The expectation coherence in <1>11 makes the two three-state
preparations equal under the standard tensor associator.
<2>5. Thus product preparation is ordered-associative. **QED**
<1>15. **PROVE** local inner unitary dynamics has a coherent extension to
collective observables.
<2>1. If `u,v` are local unitaries, `iota(u tensor v)` is unitary because
`iota` is a unital *-homomorphism.
<2>2. Its conjugation is a UCP *-automorphism of the full composite algebra.
<2>3. On the local product subalgebra,

    Ad_(iota(u tensor v))(iota(x tensor y))
       = iota(Ad_u(x) tensor Ad_v(y)).
<2>4. Inclusion coherence in <1>11 makes these extensions independent of
ordered parenthesization, and multiplication of embedded unitaries makes them
respect identity and composition.
<2>5. This is a genuine process-assembly sector.  This lane deliberately does
not identify different Kraus presentations or prescribe an extension of every
pair of abstract CP maps.
<2>6. Steps <1>13--<1>15 prove `F1-HCK-OPS`. **QED**

## 5. Low levels, intrinsic arithmetic, and a collective qubit (`F1-HCK-LOW`)
<1>16. **ASSUME** `q>0` and put `d=1+q+q^2`.
<1>17. **PROVE**
`H_1=C`, `H_2=C^2`, and `H_3=C^2 direct-sum M_2(C)`.
<2>1. The first equality is D1101.
<2>2. In `H_2`, the self-adjoint generator has distinct eigenvalues `q,-1`,
so functional calculus gives `H_2=C e_triv direct-sum C(1-e_triv)=C^2`.
<2>3. For `H_3`, define two one-dimensional representations
`chi_+(T_i)=q`, `chi_-(T_i)=-1`, and a two-dimensional representation by

    R(T_1) = [[q,0],[0,-1]],
    R(T_2) = [[-1/(q+1), sqrt(qd)/(q+1)],
              [sqrt(qd)/(q+1), q^2/(q+1)]].
<2>4. Direct multiplication verifies the quadratic and braid relations; the
two matrices are self-adjoint.
<2>5. In the ordered basis
`1,T_1,T_2,T_1T_2,T_2T_1,T_1T_2T_1`, the determinant of the six coordinate
vectors under `chi_+ direct-sum chi_- direct-sum R` is

    -q(q+1)d^3,

which is nonzero for `q>0`.
<2>6. Since §1 gives dimension six, this representation is a
*-isomorphism onto `C direct-sum C direct-sum M_2(C)`. **QED**
<1>18. **PROVE** the coefficient trace in this decomposition is

    tau_3 = alpha chi_+ + beta chi_- + gamma Tr_2,
    alpha=1/((q+1)d), beta=q^3/((q+1)d), gamma=q/d.
<2>1. The ordinary matrix traces of `R` on the six basis elements from
<1>17 are

    2, q-1, q-1, -q, -q, 0.
<2>2. Substitution of the displayed `alpha,beta,gamma` gives value one on
the identity and zero on the other five basis elements.
<2>3. This is D1101's coefficient trace by linearity; all three weights are
positive for `q>0`. **QED**
<1>19. **PROVE** the two unlabelled embedded `H_2` algebras remember
`{q,q^(-1)}`.
<2>1. Put `e_i=(T_i+1)/(q+1)`.  In the `M_2` block of <1>17,

    P_1=R(e_1)=[[1,0],[0,0]],
    P_2=R(e_2)
       = [[a,c],[c,1-a]],
    a=q/(q+1)^2, c=sqrt(qd)/(q+1)^2.
<2>2. Since `c^2=a(1-a)`, `P_2` is a rank-one projection; so are `P_1`
and their complements.
<2>3. The four ordinary matrix-trace overlaps are

    Tr_2(P_1P_2)=Tr_2((1-P_1)(1-P_2))=a,
    Tr_2(P_1(1-P_2))=Tr_2((1-P_1)P_2)=1-a.
<2>4. The arithmetic-geometric mean inequality gives
`a=q/(q+1)^2<=1/4`, with equality exactly at `q=1`.
<2>5. Hence the unlabelled minimum in D1103 equals `a`.
<2>6. The equation `a=q/(q+1)^2` has the two positive reciprocal roots

    q = (1-2a +- sqrt(1-4a))/(2a).
<2>7. Thus the overlap diagram determines `{q,q^(-1)}`, and its `q>=1`
member is the root with the plus sign. **QED**
<1>20. **PROVE** this overlap controls a collective qubit experiment.
<2>1. Let `z_std` be the canonical central support of the unique `M_2`
summand and regard `P_i=z_std e_i` as its rank-one effects.
<2>2. Put `u_1=2e_1-1`; it is a self-adjoint unitary, and `Ad_(u_1)` is the
identity on the commutative left parabolic `C[e_1]`.
<2>3. It is nontrivial on `H_3`, since in the standard block it changes the
sign of the nonzero off-diagonal entry `c` of `P_2`.
<2>4. Prepare the normalized standard-block state
`phi_2(x)=Tr_2(P_2 x_std)` and measure the effect `P_2`.
<2>5. Before the process, `phi_2(P_2)=Tr_2(P_2)=1`.
<2>6. In the standard block `u_1=2P_1-1`; for a rank-one `P_2`,

    phi_2(u_1P_2u_1)
       = |Tr_2(P_2u_1)|^2
       = |2 Tr_2(P_1P_2)-1|^2
       = (1-2a)^2.
<2>7. Thus a locally invisible inner automorphism is detected on the
collective matrix block, with an exactly `q`-dependent Born probability.
<2>8. Steps <1>17--<1>20 prove `F1-HCK-LOW`. **QED**

## 6. Marked trace recovery, reciprocal duality, and `q=1` (`F1-HCK-Q`)
<1>21. **PROVE** the D1105 marked level-two trace recovers `q`.
<2>1. Since `e_triv=(T_1+1)/(q+1)` and `tau_2(T_1)=0`,

    r_2=tau_2(e_triv)=1/(q+1).
<2>2. Therefore `q=r_2^(-1)-1`.
<2>3. The complementary minimal projection has trace `q/(q+1)`; forgetting
which projection is trivial leaves exactly the reciprocal ambiguity. **QED**
<1>22. **PROVE** the reciprocal *-isomorphism and the `q=1` specialization.
<2>1. Let `S_i` generate `H_n(q^(-1))`.  The assignment
`T_i -> -q S_i` preserves the braid and far-commutation relations.
<2>2. Its two eigenvalues are `q,-1`, so it preserves the quadratic
relation and the involution.
<2>3. The inverse is `S_i -> -q^(-1)T_i`; hence it is a *-isomorphism.
<2>4. It sends `T_w` to `(-q)^ell(w)S_w`, so the coefficient traces agree.
<2>5. At `q=1`, the quadratic relation is `T_i^2=1`; with the Coxeter
relations and §1's basis, this is exactly `C[S_n]`.
<2>6. In the faithful C*-representation, `T_i` has spectrum `{q,-1}`.
For `q!=1`, its square has spectrum `{q^2,1}` and is not the identity, so
the self-adjoint braid generator is not unitary.
<2>7. D1102 provides ordered block maps only.  None of <2>1--<2>6 supplies
a coherent block swap, so no symmetric assembly is asserted.
<2>8. Steps <1>21--<1>22 prove `F1-HCK-Q`. **QED**

## 7. Exact arithmetic bridge and remaining scope (`F1-HCK-CONTEXT`)
<1>23. **ASSUME** `Q=p^r`, a split finite symplectic space
`V=L direct-sum L^vee`, and the named Lagrangian polarization `L`.
<1>24. **PROVE** the construction gives a positive operational context
sector attached to `L`.
<2>1. The chosen `L` supplies the complete-flag space `Fl(L)` and D1104's
finite-dimensional Hilbert space `ell^2(Fl(L))`.
<2>2. Section 2 identifies its `GL(L)`-commutant, normalized operator trace,
and relative-position observables exactly with `H_n(Q)`.
<2>3. Sections 3--4 give ordered inclusions, UCP expectations, states,
effects, Born probabilities, product preparations, and coherently assembled
inner dynamics.
<2>4. Section 5 shows proper collective degrees already in
`H_1 tensor H_2 -> H_3`, including a unique `M_2` block and a measurable
parameter-dependent process.
<2>5. Therefore this is a concrete finite C*-operational subsystem sector
that remembers the finite-field cardinality through flag geometry. **QED**
<1>25. **PROVE** the sharp boundary of the result.
<2>1. The Weyl--Heisenberg algebra for the full phase space uses translations,
characters, a polarizing cocycle, and observables that move between or across
Lagrangian contexts (D1--D9, and D12--D16 over local rings).
<2>2. `Cxt(L)` instead uses only complete flags inside the named `L` and the
commutant of `GL(L)` on those flags.
<2>3. No step constructs a comparison functor from the full Weyl--Heisenberg
process theory, proves independence of `L`, extends every pair of CP maps to
the collective blocks, or identifies a `q -> 1` geometric base object.
<2>4. The next bounded bridge is therefore: place the flag-context tower
inside the stabilizer/parabolic process theory of a polarized finite
Weyl--Heisenberg system and test how changing `L` transports the two overlap
subalgebras and their conditional expectations.
<2>5. This boundary is part of `F1-HCK-CONTEXT`; the claim is not a full
finite-field Weyl--Heisenberg AQM theorem. **QED**
<1>26. The candidate theorem cluster `F1-HCK-POS`, `F1-HCK-FLAG`,
`F1-HCK-TOWER`, `F1-HCK-OPS`, `F1-HCK-LOW`, `F1-HCK-Q`, and
`F1-HCK-CONTEXT` follows from §§1--7. **QED**
