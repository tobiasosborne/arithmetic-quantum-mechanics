# The marked right-module category and its regular operational endpoint

Prover: gpt-6-astra, xhigh. Status: SKETCH, candidate for separate review.
Use D1273–D1276 and MMOD-1–2. The positive parameter range is q>1.
The categorical completion below needs finite C*-algebras and the proved
block action, not fusion, rigidity or a spherical structure. Operational
statements are conditional on the repaired D1257 classical-wiring hypothesis W.

## Theorem MCAT-1 (the raw and full completed right Hecke-module categories)

**ASSUME** the block homomorphisms rho and their MMOD-2 coherence.
**PROVE** C_R(q) is a right module category over C_H(q); its finite additive
self-adjoint completion M_q is a right module C*-category over U_q^dagger.
The stated finite traces multiply under this action.

<1>1. **PROVE** the raw action is an actual bifunctor.

<2>1. On objects it sends (m,n) to m+n. On nonzero homogeneous Hom spaces
it is rho_(m,n); a zero cross-degree morphism is sent to zero.

<2>2. For a,b in R_m and c,d in H_n, MMOD-1 gives
`rho(a tensor c)rho(b tensor d)=rho(ab tensor cd)`. This is the action's
composition/interchange identity, with the stated multiplication convention.
The unit element maps to the unit and star is preserved.

<2>3. MMOD-2 <1>11 gives equality of the two three-block morphism maps.
Thus the raw right module associator can be the identity on object m+n+k.
Its pentagon holds because every parenthesization sends a tensor of basis
arrows to the same ordered block label. The right unit is H_0=C. **QED**

<1>2. **PROVE** finite sums and self-adjoint corners extend the action.

<2>1. In each degree, rectangular matrices over R_m(q) form a C*-category;
compressing by source and target projections gives its closed corner Hom
spaces. Products, adjoints and the C*-identity are inherited from the ambient
finite matrix algebras. Finite graded sums use the maximum norm.

<2>2. The amplified map rho sends `p_m tensor e_n` to a self-adjoint
projection. Its block diagonal over m+n=k is therefore the D1273 object
projection in a single matrix algebra over R_k.

<2>3. Amplified rho sends typed rectangular corner morphisms to the required
corner, preserves adjoints and obeys matrix interchange. This defines the
right action on M_q times U_q^dagger.

<2>4. Two different pairs (m,n) with the same total k are matrix summands
in that one degree. Their full endomorphism corner includes off-diagonal
morphisms. The action map itself is block diagonal on the pair indices;
this does not remove the other morphisms from M_q. **QED**

<1>3. **PROVE** the completed module associator is coherent and unitary.

<2>1. Name the matrix indices of a triple by `(m,n,k;i,j,l)`. The two
iterated action objects use the same amplified triple inclusion by MMOD-2,
with different groupings of these finite indices.

<2>2. The canonical permutation matrix of these groupings is a unitary
between the two projection presentations. It is natural in every rectangular
corner map, since those maps have the identical triple-entry formula.

<2>3. In a quadruple, either pentagon path takes each grouped index to the
same ordered four-tuple and applies the same four-block inclusion to its
coefficient. This proves the module pentagon. Removing the unique degree-zero
unit index proves the triangle. No exchange of ordered blocks is included.
**QED**

<1>4. **PROVE** the finite graded traces give positive action-compatible weights.

<2>1. For any rectangular marked matrix a,
`sum_m(Tr tensor tau_R,m)(a_m^*a_m)` is the sum of positive faithful
entrywise Gram norms. Thus theta_X is faithful and positive on End(X).
Matrix trace cyclicity and tau_R cyclicity also give
`theta_X(ba)=theta_Y(ab)` for typed marked rectangular a:X->Y,b:Y->X.

<2>2. In an (m,n) action block, the ordinary matrix trace and MMOD-1's
coefficient-trace product give

    theta_(X triangleleft Y)(a triangleleft b)=theta_X(a)theta_Y(b)

after summing all pairs. The trace includes all same-degree matrix blocks;
off-diagonal entries have zero matrix trace but remain valid observables.

<2>3. Taking identities yields `d_(X triangleleft Y)=d_X d_Y`.
Each nonzero fibre projection has positive d by faithfulness, so the normalized
traces satisfy the corresponding product formula under assembly.

<2>4. The induced map End(X) tensor End(Y)->End(X triangleleft Y) is
injective: each pair's corner restriction of the amplified rho is injective,
and different pairs occupy distinct diagonal blocks. Thus there is a unique
traced UCP expectation onto this included algebra by MMOD-2's finite tracial
projection argument. This supplies traced fibre systems on the completed
module category without using D1121's fusion hypothesis. **QED**

<1>5. Steps <1>1–<1>4 prove MCAT-1. **QED**

## Theorem MCAT-2 (fully typed right-module induction realization)

**ASSUME** q>1 and the right-module conventions in D1274.
**PROVE** the completed action is algebraically equivalent to induction of
finite-dimensional graded right modules, with the explicitly induced Hecke
product and coherent balancing. The dagger convention remains explicit.

<1>6. **PROVE** the matrix-corner description has the correct right variance.

<2>1. The object (r,p) in degree m represents the right module p R_m^r,
using column vectors and right scalar multiplication. A right-linear map to
(s,f) is left multiplication by `a in f M_(s,r)(R_m)p`.

<2>2. Indeed its values on the projected standard columns determine it,
and source/target projection identities force exactly this corner equation.
Matrix multiplication is its composition, in the raw category's convention.

<2>3. Every finite-dimensional module over the finite C*-algebra R_m is
projective: decompose that algebra into finite full matrix summands and each
module into their simple right modules. Equivalently every module
is a summand of a finite free right module.

<2>4. The same holds for H_n. Algebraic idempotents can be replaced by
self-adjoint ones: the support p of ee^* belongs to the finite matrix algebra
by polynomial interpolation on its spectrum, and `pe=e`, `ep=p` exhibit
inverse morphisms between e and p presentations. Thus the self-adjoint corner
categories have the full underlying finite right-module categories. **QED**

<1>7. **PROVE** induction matches the amplified block action on free modules.

<2>1. Let A=R_m tensor H_n and B=R_(m+n), with left A-action on B through
rho. Define

    (R_m^r tensor H_n^s) tensor_A B -> B^(rs),
    (a tensor b) tensor c |-> (rho(a_i tensor b_j)c)_(i,j).

It is balanced because multiplying the two source right coefficients acts
on B by the same homomorphism rho. It is right B-linear.

<2>2. If xi_i and eta_j are the two standard unit columns, its inverse
sends a column z in B^(rs) to
`sum_(i,j)(xi_i tensor eta_j) tensor z_(i,j)`.
Balancing reduces both composites to the identity on elementary tensors and
standard columns. This proves a genuine isomorphism, not a dimension count.

<2>3. The source idempotent p tensor e corresponds under this map to the
amplified projection `rho^(r,s)(p tensor e)` on B^(rs). Restricting the free
isomorphism to these images therefore yields

    (pR_m^r tensor eH_n^s) tensor_A B
       ~= rho^(r,s)(p tensor e) B^(rs).

On corner morphisms it sends the induced tensor map to the amplified rho,
by the same entrywise formula. This is exactly D1273's action. **QED**

<1>8. **PROVE** the induced action has the required right associator.

<2>1. Let M,N,P be right modules over R_m,H_n,H_k. Both bracketings of
the action identify with

    (M tensor N tensor P)
       tensor_(R_m tensor H_n tensor H_k) R_(m+n+k),

where the left action is the common map of MMOD-2 <1>11.

<2>2. From `(M triangleleft N) triangleleft P`, the map on generators is

    [((x tensor y) tensor b) tensor z] tensor c
      |-> (x tensor y tensor z) tensor rho_(m+n,k)(b tensor 1)c.

Balancing in R_m tensor H_n, then in R_(m+n) tensor H_k, respects this
formula by the homomorphism and action identities. Its inverse inserts the
unit b=1. Each composite reduces to the identity by balancing.

<2>3. For `M triangleleft (N star P)`, the corresponding map is

    [x tensor ((y tensor z) tensor h)] tensor c
      |-> (x tensor y tensor z) tensor rho_(m,n+k)(1 tensor h)c.

Here h is in H_(n+k). It is balanced by the ordinary Hecke block inclusion
and the same action identity. Again the inverse inserts h=1.

<2>4. These are natural right-linear isomorphisms. For four factors every
associator path reduces to the same elementary tensor with all intermediate
algebra elements multiplied through the common ordered inclusion. Thus they
satisfy the module pentagon; H_0=C supplies the unit isomorphism. **QED**

<1>9. **PROVE** the algebraic and dagger assertions are correctly separated.

<2>1. Steps <1>6–8 give an equivalence of algebraic right module categories
and their induced actions. Bare vector-space modules have not been assigned
a canonical adjoint operation.

<2>2. On the projection module pR_m^r use the standard R_m-valued inner
product `<a,b>=sum_i a_i^*b_i`. Corner-matrix maps have adjoints given by
their matrix stars. The same applies on Hecke projection modules.

<2>3. Under induction, the corresponding B-valued form is

    <(a tensor b) tensor c,(a' tensor b') tensor d>
       =c^*rho(<a,a'> tensor <b,b'>)d.

The free isomorphism of <1>7 carries it to the standard positive form on
B^(rs), and its corner restriction does likewise. Thus the completed action
also has the stated dagger realization in these explicit projection Hilbert
modules. This is not an implicit metric on every bare module.
Steps <1>6–<1>9 prove MCAT-2. **QED**

## Theorem MEND-1 (the reference quotient is the ordinary Hecke right module)

**ASSUME** q=1 in the based algebras, D1275 and MIR-END.
**PROVE** the raw reference quotient is C_H(1) with its ordinary right
monoidal action, its additive self-adjoint completion is U_1^dagger, and the
quotient is compatible with the induced right-module construction.

<1>10. **PROVE** the reference null ideal respects the marked action.

<2>1. N_m is the span of nonempty-antichain orbitals. Rho retains A, so
`rho_(m,n)(N_m tensor H_n(1)) subset N_(m+n)` directly from its basis formula.

<2>2. The induced map on quotient bases is
`T_u tensor T_v |-> T_(u block v)`, exactly the ordinary Hecke inclusion at
one. Thus

    Pi_(m+n) rho_(m,n),1=iota_(m,n),1(Pi_m tensor id).

<2>3. Pi is a unital star-homomorphism only at this reference boundary;
it is the nonmultiplicative vector expectation at generic q. At one its
identity-on-objects map is a genuine functor C_R(1)->C_H(1) respecting the
right action. Quotienting its Hom ideal N gives exactly the raw Hecke
category and its ordinary right action. **QED**

<1>11. **PROVE** the quotient extends to the full finite amplitude completions.

<2>1. Apply Pi to every matrix entry of every finite self-adjoint idempotent
presentation. Multiplicativity and star show that the image is a self-adjoint
projection; rectangular corner equations are preserved.

<2>2. For chosen source projections p,f and an arrow a between their
quotient images, a lift in the algebraic endpoint corner is
`f i(a) p`, using entrywise Hecke inclusion in each degree. Applying Pi
returns a because its endpoint source/target units already fix it.
Thus this functor is full on those Hom spaces.

<2>3. Every Hecke projection e has the lift i(e), so the functor is
essentially surjective. Its kernel ideal is the corresponding matrix-corner
part of N. Its reference quotient has the additive self-adjoint completion
U_1^dagger, compatibly with <1>10's right action.

<2>4. Some nonzero algebraic endpoint projections have zero quotient image.
Zero objects are allowed here; no normalized state or positive nonzero
operational system is assigned to such an image. No norm-continuous boundary
C*-field for these full algebraic presentations is asserted. **QED**

<1>12. **PROVE** the endpoint right-module functor has the correct balancing.

<2>1. On right modules the quotient functor is extension of scalars
`M |-> M tensor_(R_m(1)) H_m(1)`, where R_m acts on H_m through Pi_m.

<2>2. For any right Hecke module N, associativity of the balanced tensor and
<1>10.<2>2 identify both

    (M triangleleft N) tensor_(R_(m+n)(1)) H_(m+n)(1),
    (M tensor_(R_m(1)) H_m(1)) star N

with `(M tensor N) tensor_(R_m(1) tensor H_n(1)) H_(m+n)(1)`.
The identifications send elementary tensors to the same products and their
inverses insert unit elements, as in MCAT-2 <1>8.

<2>3. Consequently the quotient respects induced right action. It can kill
modules supported on the null ideal; it is not an equivalence between all
modules of the unquotiented R_*(1) and all Hecke modules.
Steps <1>10–<1>12 prove MEND-1. **QED**

## Theorem MREG-1 (regular operational evaluation respects marked assembly)

**ASSUME** the repaired bridge MIR-REG and its hypothesis W, together with
D1276 and MMOD-1–2. All regular labels have continuous coefficients on
[1,1+epsilon] and positivity/normalization for every nearby real q>1.
**PROVE** the mixed assembly, split and retained processes extend that
regular operational category, and its quotient endpoint functor sends them
to the ordinary Hecke ordered assembly, split and retained processes.

<1>13. **PROVE** the mixed assembly generators are typed continuous UCP maps.

<2>1. MMOD-1–2 give UCP maps F and rho in exactly the Heisenberg directions
specified in D1276. Their formulas insert or delete finite orbit coefficients,
so they act continuously on regular coefficient sections including at one.

<2>2. Their trace-duals are respectively rho and F by MMOD-2's trace-pairing
identity. Thus assembly of separated normalized densities h,k has collective
density `rho(h tensor k)`, and splitting a collective density uses F.
Both retain positivity and trace in every real punctured fibre.

<2>3. The separated retract relation `spl^R o asm^R=id` has realization
F rho=id. Its reverse has realization rho F and is not imposed as an
identity. MMOD-2 <1>12 proves the typed module associativity relating two
successive mixed assemblies to one mixed assembly after Hecke assembly.
The reverse splits obey the inclusion associativity. **QED**

<1>14. **PROVE** mixed retained instruments and their label relations extend.

<2>1. For normalized lists K in R_m and L in H_n, define the output list
`rho(K_(o,i) tensor L_(p,j))`. Its sum of adjoint squares is
`rho(1 tensor 1)=1` by the star-homomorphism property. Its coefficients
are continuous, and its action is defined on the full collective R_(m+n).

<2>2. Pointwise within-outcome Gram equality gives a scalar-unitary mixing
at each q, as in MIR-REG <1>9. Tensoring and applying rho carries that
mixing to the resulting list. Thus the retained construction respects the
regular label congruence without an isolated-CP quotient.

<2>3. Multiplicativity and MMOD-2 associativity prove the list composition,
context nesting and right-action parallel identities. All outcome product
and routing maps in those equations are the explicit W maps. They are not
implicit changes between separated and collective register words. **QED**

<1>15. **PROVE** both new structure maps intertwine the endpoint quotient.

<2>1. MEND-1 proves the inclusion square. MMOD-2 <1>13 at one proves the
expectation square. Explicitly,

    Pi_(m+n) rho_(m,n),1=iota_(m,n),1(Pi_m tensor id),
    (Pi_m tensor id) F_(m,n),1=E^H_(m,n),1 Pi_(m+n).

<2>2. In Heisenberg orientation these are exactly the two equations for
sending mixed assembly to ordinary Hecke assembly and mixed split to ordinary
Hecke split. When m=0 they reduce to the existing up/down endpoint identities.

<2>3. Applying the inclusion square to each retained Kraus entry sends the
mixed list to `iota(Kbar tensor L_1)`. Completeness and its endpoint CP map
are consequently the ordinary Hecke retained process, including the same
classical outcome labels and uniform-trace factors. **QED**

<1>16. **PROVE** a well-defined enlarged circuit functor and finite Born limit result.

<2>1. Adjoin the D1276 boxes to the regular source and the usual Hecke
assembly boxes to its endpoint target. Impose the old sound congruence and
the additional typed relations proved in <1>13–14. The free-category
quotient therefore has a UCP realization at every q>1.

<2>2. The new relations evaluate to true Hecke relations by <1>15 and
MMOD-2. The old ones do by MIR-REG. Hence coefficient evaluation followed by
Pi descends to a monoidal functor on the enlarged circuit category and its
one-sided germs.

<2>3. The new Schrödinger maps rho,F preserve regular coefficients by
<1>13. Their retained Kraus maps do by finite multiplication. Thus the
MIR-REG induction on finite protocol trees still applies: branch and event
Born weights converge to the evaluated Hecke protocol, with conditioning
only when its limiting event probability is positive.

<2>4. Endpoint labels lift locally through the Hecke inclusion by MIR-REG,
while the new assembly/split boxes themselves are defined on the entire
punctured interval. Finite endpoint circuits using these boxes consequently
have regular local lifts after choosing one common interval. This is
existence for individual circuits, not an equation-preserving global lift
functor. **QED**

<1>17. **PROVE** the distinction between one and two retained marked systems
is preserved by this result.

<2>1. Every new faithful algebra assembly has source R_m tensor H_n.
The second block's updates leave its vector coordinate unchanged in the
geometric proof; its operator algebra is Hecke, not another R_n.

<2>2. A circuit may first apply down_n to a second marked register and then
assemble it as an unmarked one. Its Schrödinger map first applies
`id tensor E_n` to the separated densities before mixed assembly. Its
Heisenberg map is `(id tensor i_n) F_(m,n)`, which is UCP; this process does
not provide a star-embedding of the full two-marked tensor algebra into
R_(m+n).

<2>3. Retained two-marked composition therefore remains the separate
arithmetic shuffle correspondence D1256. The new generic law is precisely
the positive right Hecke-module action. It supplies no full-Weyl extension,
mirabolic monoidal product, or arbitrary CP completeness theorem.
Steps <1>13–<1>17 prove MREG-1. **QED**
