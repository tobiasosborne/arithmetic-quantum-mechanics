# Continuous self-adjoint completion and its traced assembly

Prover: gpt-6-astra, xhigh. Status: PROVED within the stated hypotheses. Admission and repaired scope
are recorded in `../../verdicts/f1-limit-adjudication.md`.
Definitions are D1261–D1264 in definitions.md. The input is the continuous regular
Hecke algebra of D1201–D1202/CLIM-1 and the PROVED F1-HCK-POS/TOWER.
This proof does not invoke D1121: the category need not be rigid or fusion.

## Theorem KCOM-1 (the full finite graded continuous completion)

**ASSUME** I is a nonempty compact positive interval and use D1261–D1262.
**PROVE** `U_I^cts` is an additive ordered monoidal C*-category with all
self-adjoint idempotents split, and its fibre category is the self-adjoint
model of the full composition category U_q, not merely the parabolic part.

<1>1. **PROVE** the displayed matrix corners form a C*-category.

<2>1. For each degree n, the CLIM-1 algebra `A_n(I)` is a C*-algebra.
Its rectangular matrices sit as corners in square matrix C*-algebras.

<2>2. The map `a |-> p_Y a p_X` is a bounded idempotent on each such
rectangular Banach space; its range is therefore closed. D1261 has only
finitely many nonzero component spaces in each Hom.

<2>3. Matrix multiplication sends `p_Z b p_Y` and `p_Y a p_X` to
`p_Z ba p_X`. Identity, associativity and dagger follow by multiplication.

<2>4. The C*-identity `||a^*a||=||a||^2` and positivity of `a^*a` hold in
the containing finite matrix C*-algebras, hence with the maximum norm over
the finitely many degrees. This proves the C*-category axioms. **QED**

<1>2. **PROVE** the direct sum and projection splitting are the full ones.

<2>1. In degree n, `X direct-sum Y` has projection `diag(p_X,p_Y)`.
Multiplication by the two block inclusions/projections proves the biproduct
identities; its endomorphisms include `p_X M_(r,s)(A_n)p_Y` and its adjoint.

<2>2. If a self-adjoint idempotent `e` lies in End(X), then `e=p_X e p_X`
and `e^2=e=e^*`. The same finite matrix presentation with projection e is
an object. The rectangular map e has `e^*e=e` and `ee^*=e` as an
endomorphism of X, so it splits this idempotent.

<2>3. Conversely every D1261 object is such a retract of the finite direct
sum of r_n copies of the regular degree-n objects. Thus D1261 is precisely
`Kar_dagger(Add(C[A_*]))`. No equal-degree off-diagonal Hom is lost. **QED**

<1>3. **PROVE** the balanced tensor domain in D1262 is explicit and injects.

<2>1. CLIM-1 identifies `A_m(I)` as the free C(I)-module with basis B_u.
The balanced section tensor has basis `B_u tensor B_v`, with continuous
coefficients in the single parameter q. Its pointwise finite-dimensional
C*-norm, maximized over I, is the norm intended in D1262.

<2>2. This space is closed: in the tensor regular representation, applying
a section to `delta_e tensor delta_e` recovers all coefficient functions.
The uniform-limit argument of CLIM-1 therefore applies verbatim.

<2>3. D1102 and block length additivity send `B_u tensor B_v` to
`B_(u times v)`. Distinct pairs give distinct permutations. The resulting
C(I)-linear map is injective, multiplicative, unital and star preserving.
It is continuous in the regular frame. Matrix amplifications share these
properties by the matrix-unit multiplication rule. **QED**

<1>4. **PROVE** object and morphism tensor are well defined.

<2>1. Every block `iota^(r,s)(p_X tensor p_Y)` is a self-adjoint projection
by <1>3. Their degreewise block diagonal is the projection of D1262.
There are only finitely many degrees and finitely many index pairs.

<2>2. If `a=p_X' a p_X` and `b=p_Y' b p_Y`, multiplicativity puts the
amplified `a tensor b` in the required tensor-object corner.

<2>3. The matrix-unit multiplication rule and the homomorphism property of
iota give `(a' tensor b')(a tensor b)=(a'a) tensor (b'b)`.
Dagger and identities are preserved by the same computation.

<2>4. For three factors both parenthesizations have indices named by
`(l,m,n;i,j,k)`. The D1262 permutation matrices give the associator between
the two chosen orders. Both maps on an entry are the same ordered
three-block Hecke inclusion, by F1-HCK-TOWER.

<2>5. Each pentagon path sends every index to the same tuple of four degrees
and four matrix indices and acts identically on its Hecke coefficient.
This verifies the pentagon, rather than assuming strict equality of the
matrix presentations. The degree-zero unit and triangle are checked by
deleting the unique unit index. **QED**

<1>5. **PROVE** the parabolic category has exactly this completion.

<2>1. Send alpha to its rank-one matrix presentation e_alpha in degree
`|alpha|`, and a corner morphism to the identical matrix entry. D1141 and
CLIM-2 give equality of its Hom spaces, composition and dagger.

<2>2. `iota(e_alpha tensor e_beta)=e_(alpha concat beta)` gives the
monoidal comparison, with the same ordered associators as <1>4.

<2>3. In every degree n, the complete composition `1^n` has projection 1,
including the empty composition in degree zero. Its finite sums and
self-adjoint retracts therefore contain all D1261 objects by <1>2.

<2>4. Extending the inclusion to additive self-adjoint completions is fully
faithful on the identical rectangular corners and essentially surjective
by <2>3. It is a unitary strong monoidal equivalence. This proves the
interval version as well as its fibre version. **QED**

<1>6. **PROVE** the fibre comparison also covers algebraic U_q if that
notation retains arbitrary idempotents as in D1223.

<2>1. In a finite-dimensional matrix C*-algebra, let e be an algebraic
idempotent. The support projection p of `ee^*` is a polynomial in `ee^*`
by interpolation on its finite spectrum, hence belongs to that algebra.
In a faithful matrix representation, `ran(p)=ran(e)`.

<2>2. It follows that `pe=e` and `ep=p`: e acts as identity on its range.
The matrices e and p are inverse morphisms between the two algebraic
idempotent objects, since their composites are e and p, respectively.

<2>3. Apply this in every nonzero degree. Thus every algebraic U_q object
is isomorphic to a self-adjoint one. On self-adjoint objects the rectangular
Hom formula is unchanged. This is an equivalence of underlying algebraic
categories; the dagger assertion is made only for the self-adjoint model.
No arbitrary algebraic similarity is called a unitary identification. **QED**

<1>7. Steps <1>1–<1>6 prove KCOM-1. **QED**

## Theorem KCOM-2 (faithful cyclic traces and tensor multiplicativity)

**ASSUME** D1263 and KCOM-1.
**PROVE** theta is positive, faithful, continuous and cyclic across typed
rectangular morphisms; d is positive on every nonzero connected-interval
object; `w_(X tensor Y)=w_X w_Y` and normalized traces multiply under j.

<1>8. **PROVE** the component matrix coefficient traces are faithful.

<2>1. For a rectangular matrix a, direct expansion gives

    (Tr_r tensor tau_n)(a^*a)=sum_(i,j) tau_n(a_(i,j)^* a_(i,j)).

Each term is nonnegative and vanishes only when its entry vanishes, by
F1-HCK-POS. Summing over degrees proves faithfulness for the Hom norm square.

<2>2. For a positive endomorphism h, its square root belongs to its corner
C*-algebra. Apply <2>1 to this square root to get `theta_X(h)>=0`, with
strict inequality in a fibre whenever h is nonzero there.

<2>3. In the normalized regular frame the trace is the sum of diagonal
identity coefficients, so it is continuous on sections. Restriction to a
corner and finite degree sums preserve these assertions. **QED**

<1>9. **PROVE** cyclicity holds between different objects.

<2>1. For `a:X->Y` and `b:Y->X`, expand a degree-n contribution as
`sum_(i,j) tau_n(b_(i,j)a_(j,i))`.

<2>2. Traciality of tau_n changes this to
`sum_(j,i) tau_n(a_(j,i)b_(i,j))`, the corresponding term for ab.
Hence `theta_X(ba)=theta_Y(ab)` after summing degrees.

<2>3. A unitary isomorphism v gives
`theta_Y(v h v^*)=theta_X(h)` and `w_Y=w_X`, by taking `v^*v=1_X`.
Thus the traces do not depend on the named presentation up to the declared
unitary identifications. No rigid categorical trace is being invoked. **QED**

<1>10. **PROVE** a nonzero object cannot acquire a zero fibre on connected I.

<2>1. Each `p_(X,n)(q)` is a continuous orthogonal projection in the fixed
regular finite matrix representation. Its ordinary representation rank is
the ordinary matrix trace of that projection, a continuous integer-valued
function, hence constant on connected I.

<2>2. If X is nonzero as a section object, one component projection is
nonzero at some q; that component consequently has positive rank throughout I.
By <1>8, `w_X(q)=theta_X,q(p_X(q))>0` throughout I.

<2>3. The continuous positive function w_X has a positive minimum on the
compact interval. Division by it gives a continuous faithful normalized trace
tau_X. Zero objects remain in the amplitude category but are excluded from
normalized systems, exactly as in D1263. **QED**

<1>11. **PROVE** the unnormalized traces multiply under ordered tensor.

<2>1. In an `(m,n)` block of `a tensor b`, matrix trace and the coefficient
trace product law of F1-HCK-TOWER give

    (Tr_(r_m s_n) tensor tau_(m+n))(iota(a_m tensor b_n))
      =(Tr_(r_m) tensor tau_m)(a_m)
       (Tr_(s_n) tensor tau_n)(b_n).

<2>2. Trace of the degree-k block diagonal is the sum over `m+n=k`.
Summing all degrees therefore gives

    theta_(X tensor Y)(a tensor b)=theta_X(a) theta_Y(b).

This uses the full degree-k matrix trace. Additional off-diagonal
endomorphisms exist but have zero matrix trace individually.

<2>3. Taking a,b to be identities gives `w_(X tensor Y)=w_X w_Y`.
Dividing <2>2 by this identity proves
`tau_(X tensor Y)(j(a tensor b))=tau_X(a)tau_Y(b)`. **QED**

<1>12. **PROVE** j is an injective unital star-map on system algebras.

<2>1. `End(X)` is the finite direct sum of its degree corners. Thus the
fibre tensor `End(X) tensor End(Y)` is the direct sum over pairs `(m,n)`.
For each pair, <1>3's amplified injective map remains injective on its corner.

<2>2. Distinct pairs occupy distinct diagonal matrix blocks, even when their
total degree agrees. A sum of their images can vanish only when each does.
This proves injectivity without assuming a fusion-category theorem.

<2>3. Tensor identities give the identity projection of X tensor Y.
Star and multiplication are preserved by <1>4. Trace preservation is <1>11.
The same pointwise argument proves injectivity of the balanced section map.

<2>4. KCOM-2 follows from <1>8–<1>12. **QED**

## Theorem KCOM-3 (unique continuous traced UCP expectations)

**ASSUME** nonzero D1261 objects X,Y on connected I and write Z=X tensor Y.
**PROVE** D1264 defines a unique traced UCP expectation in every fibre,
these maps act continuously on sections, and their ordered tower is coherent.

<1>13. **PROVE** trace orthogonal projection onto a finite unital subalgebra
is a trace-preserving conditional expectation.

<2>1. Work in one fibre `A=End(Z)` with faithful normalized trace tau_Z
and subalgebra `B=j(End(X) tensor End(Y))`. On A use
`<a,c>=tau_Z(a^*c)`. Finite-dimensional orthogonal projection F onto B exists
uniquely by the positive definite Gram matrix of any basis of B.

<2>2. Its defining identity is
`tau_Z(b^*F(a))=tau_Z(b^*a)` for b in B. It fixes B and hence the unit.
Taking b=1 proves trace preservation.

<2>3. The trace identity and conjugation show `F(a^*)=F(a)^*`.
For c,d,b in B, cyclically move d to compare `tau_Z(b^*cad)` and
`tau_Z(b^*cF(a)d)`. Their equality by <2>2, with test `c^* b d^*`,
proves `F(cad)=cF(a)d`. Nondegeneracy on B justifies the conclusion.

<2>4. If a is positive and F(a) has a negative spectral projection r in B,
then `tau_Z(rF(a))<0` by faithfulness, whereas <2>2 gives
`tau_Z(rF(a))=tau_Z(ra)=tau_Z(a^(1/2)r a^(1/2))>=0`.
Contradiction. Therefore F is positive.

<2>5. Entrywise F is the trace-orthogonal projection from M_l(A) to M_l(B)
for `Tr_l tensor tau_Z`: test on matrix units times b to verify the
orthogonality identity. Repeat <2>3–4 in this finite algebra. All matrix
amplifications are positive, so F is completely positive. **QED**

<1>14. **PROVE** uniqueness includes any traced UCP retraction onto B.

<2>1. Let G:A->B be UCP, fix B and preserve tau_Z. In a faithful matrix
representation of B, Stinespring 1955, Theorem 1 (pp. 211–213), writes
`G(a)=V^*pi(a)V`; unitality makes V an isometry.

<2>2. For b in B, expand the square norm of `pi(b)V-Vb`.
Its square is `G(b^*b)-G(b)^*b-b^*G(b)+b^*b=0`, because G fixes B.
Thus `pi(b)V=Vb`, and its adjoint gives bimodularity of G.

<2>3. Consequently `tau_Z(b^*G(a))=tau_Z(G(b^*a))=tau_Z(b^*a)`.
By uniqueness of trace orthogonal projection, G=F. This is exactly the
finite tracial expectation characterized in Umegaki 1954, pp. 177–179,
equation (1); <1>13 independently supplies existence and complete positivity.

<2>4. Define `E=j^(-1)F`. The inclusion is a unital star-isomorphism onto
B, so E is UCP, trace preserving for the product trace, and `Ej=id`.
The reverse map jE is F, which need not be identity. **QED**

<1>15. **PROVE** corner Hom dimensions are locally constant.

<2>1. Identify every ambient `M_(s_n,r_n)(A_n(q))` with its fixed
normalized-basis coefficient vector space. The linear operator
`Q(q):a |-> p_Y(q)a p_X(q)` has continuous coefficients and is idempotent.

<2>2. The rank of an idempotent equals its ordinary vector-space trace:
its minimal polynomial divides t(t-1), so its eigenvalues are 0 and 1.
Therefore the continuous scalar `Tr(Q(q))` is an integer and locally constant.
This argument concerns the full matrix corner, not merely the rank of p_X.

<2>3. Finite degree sums show that Hom dimensions, and in particular the
endomorphism corner dimensions, are locally constant. **QED**

<1>16. **PROVE** local continuous bases exist for each corner bundle.

<2>1. At q0 choose a vector-space basis of `End(X(q0))`. Lift each element
by constant normalized Hecke coefficients in its finite matrix entries and
compress by the already given p_X(q) on both sides.

<2>2. These raw corner sections evaluate to the chosen basis. Their Gram
matrix for the faithful continuous trace is positive definite at q0, so its
determinant stays nonzero on a smaller interval.

<2>3. They are linearly independent there. By <1>15, their number is the
constant dimension, so they are a basis throughout that interval.
Repeat for Y, Z and any other finitely many needed corners. **QED**

<1>17. **PROVE** the expectation on sections is continuous.

<2>1. On an interval from <1>16, choose bases x_i,y_j for End(X),End(Y).
The sections `b_(i,j)=j(x_i tensor y_j)` form a basis of B in every fibre
by <1>12. Enumerate them as b_1,...,b_N.

<2>2. Define

    G_ab(q)=tau_Z,q(b_a(q)^* b_b(q)),
    t_a(q)=tau_Z,q(b_a(q)^* z(q))

for a continuous z in End(Z). G is continuous positive definite and t is
continuous by KCOM-2. Hence `c(q)=G(q)^(-1)t(q)` is continuous.

<2>3. The section `F(z)(q)=sum_b b_b(q)c_b(q)` satisfies precisely the
trace orthogonality equations in <1>13. It is therefore the unique fibre
expectation. Its preimage `E(z)=sum_(i,j)c_(i,j) x_i tensor y_j` is a
continuous balanced tensor section.

<2>4. Different local bases produce the same map on overlaps by fibrewise
uniqueness. They consequently glue over I. The map is C(I)-linear, and
fibrewise UCP implies supremum-norm contraction and complete positivity
on section matrix algebras. This proves actual section continuity. **QED**

<1>18. **PROVE** the ordered inclusion/expectation tower is coherent.

<2>1. The two inclusions of `End(X) tensor End(Y) tensor End(W)` into the
collective three-object endomorphism algebra agree under the D1262 associator,
by <1>4. Traces are preserved by KCOM-2.

<2>2. Each iterated E is a UCP retraction to the same three-factor algebra,
preserves its normalized product trace, and fixes that subalgebra.
By <1>14 uniqueness the two composites agree. This also proves the usual
tower equation for any of these nested included algebras.

<2>3. These are equalities of continuous maps, since they hold in every
fibre and <1>17 realizes the maps on sections. Thus the assembly and split
relations in D1264 are coherent without a rigidity assumption. **QED**

<1>19. **PROVE** the parabolic assembly is recovered on the nose.

<2>1. For X_alpha given by e_alpha, D1263 has
`theta_Xalpha=tau_n` on the corner, `w_Xalpha=1/P_alpha`, and hence
`tau_Xalpha=P_alpha tau_n`, exactly D1141/D1203.

<2>2. The inclusion j is the same restricted Hecke block inclusion.
CLIM-2's corner expectation is traced UCP and fixes this subalgebra.
It equals D1264's E by <1>14. No alternative trace has been substituted.

<2>3. Steps <1>13–<1>19 prove KCOM-3. **QED**

## Worked check KCOM-4 (colliding degrees retain collective observables)

**ASSUME** X=Y=[0] direct-sum [1], with identity projections in both degrees.
**PROVE** the full completion has a seven-dimensional collective algebra,
a four-dimensional separated algebra, and an explicit proper expectation.

<1>20. **PROVE** the algebras and traces have the following forms.

<2>1. `End(X)=C direct-sum C`, with `w_X=2` and normalized trace averaging
the two components. In X tensor X the degrees 0,1,2 have multiplicities
1,2,1 respectively, by the pair-index rule of D1262.

<2>2. Therefore

    End(X tensor X)=C direct-sum M_2(C) direct-sum H_2(q),
    w_(X tensor X)=1+2+1=4,
    tau(a,B,c)=(a+Tr_2(B)+tau_2(c))/4.

The dimension is `1+4+2=7`, while `End(X) tensor End(X)=C^4`.

<2>3. In the order (00,01,10,11), j sends four scalars to the scalar
in degree zero, the two diagonal matrix entries in degree one, and the
scalar multiple of the identity in H_2(q). Its expectation is

    E(a,B,c)=(a,B_11,B_22,tau_2(c)).

Direct trace pairing verifies D1264, so uniqueness identifies this formula.
The degree-one matrix unit E_12 is a nonzero retained collective observable
annihilated by jE. Treating the two degree-one summands as separate degrees
would incorrectly delete it from the category itself. **QED**
