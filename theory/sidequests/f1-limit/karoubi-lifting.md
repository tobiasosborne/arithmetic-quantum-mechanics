# Local completion lifts and the controlled operational limit

Prover: gpt-6-astra, xhigh. Status: PROVED within the stated hypotheses. Admission and repaired scope
are recorded in `../../verdicts/f1-limit-adjudication.md`.
This shard uses D1261–D1266 and KCOM-1–3. It proves a local analytic completion
of the composition lane's generic specialization, with no fusion hypothesis.
Compatibility with the circuit presentation is conditional on D1266's
explicit classical-wiring hypothesis W. No all-CP completeness is claimed.

## Theorem KLIFT-1 (local projection objects and full endpoint evaluation)

**ASSUME** q0>0 and a finite family of self-adjoint projection objects in
`U_q0^dagger`.
**PROVE** they have simultaneous local continuous lifts; evaluation on given
section objects is full; the endpoint germ evaluation is full and essentially
surjective. Endpoint unitaries between given lifts also lift locally.

<1>1. **PROVE** a finite self-adjoint matrix datum has a self-adjoint raw lift.

<2>1. Expand every entry of an endpoint matrix a0 in the normalized Hecke
basis of D1201. Extend those coefficients as constant functions of q on
some compact positive interval containing q0.

<2>2. This gives an ambient matrix section a with a(q0)=a0 by CLIM-1.
For a0 self-adjoint, replace a by `(a+a^*)/2`. Matrix star is continuous
and the replacement still evaluates to a0.

<2>3. This procedure works degree by degree and entry by entry for any
finite number of matrices. A zero component can be lifted as identically
zero. No global algebraic coefficient ring is asserted for later cutoffs.
This proves the raw lifting assertion. **QED**

<1>2. **PROVE** spectral cutoff of a raw lift of p0 is a local projection lift.

<2>1. Let a(q) be the self-adjoint lift of p0 from <1>1 and let 1 denote
the ambient matrix-algebra unit. Put `h(q)=2a(q)-1`. At q0,
`h(q0)^2=1` because `p0^2=p0`.

<2>2. After shrinking, `||h(q)^2-1||<1/2`. The binomial power series for
`(1+z)^(-1/2)` converges absolutely and uniformly in norm for `||z||<=1/2`.
Use it on `z=h^2-1` to obtain the continuous section `c=(h^2)^(-1/2)`.
The series belongs to the matrix section algebra by its norm closedness.

<2>3. Each term commutes with h and is self-adjoint. Multiplying uniformly
convergent power series gives `c^2 h^2=1`. Its scalar branch is positive
on the positive spectrum of h^2. Thus `j=h c` is self-adjoint and `j^2=1`.

<2>4. Consequently `p(q)=(1+j(q))/2` is a continuous self-adjoint
projection with `p(q0)=p0`. In a matrix spectral decomposition, j is +1
on positive eigenvalues of h and -1 on negative ones. Hence this is exactly
the spectral cutoff of a above 1/2, not a discontinuous operation across a
closing spectral gap.

<2>5. The formula uses positive functional calculus locally, not polynomial
base change over D1141's generic coefficient ring. **QED**

<1>3. **PROVE** a finite collection of objects lifts simultaneously.

<2>1. Apply <1>2 to the finitely many nonzero projection matrices in every
object. Intersect their finitely many admissible neighborhoods of q0 and
choose a smaller compact interval therein.

<2>2. Use the same finite degree support and matrix multiplicities as the
endpoint presentations. These are D1261 objects and evaluate to the original
ones on the nose. A nonzero endpoint object stays nonzero by KCOM-2 <1>10.

<2>3. At q0=1 their germs are therefore preimages of all objects of
`U_1^dagger`. Together with the algebraic comparison KCOM-1 <1>6 this also
gives essential surjectivity onto D1224's algebraic U_1, if that convention
is retained. The claimed dagger target is the self-adjoint one. **QED**

<1>4. **PROVE** evaluation is full on any already chosen section objects.

<2>1. For X,Y in U_I^cts and `f0:X(q0)->Y(q0)`, lift the finitely many
rectangular ambient coefficient matrices by <1>1 without imposing star.
Compress to `f(q)=p_Y(q) f_raw(q) p_X(q)` degree by degree.

<2>2. It evaluates to f0 because the source and target projection units
already fix f0. It has the required Hom type and is continuous on I.
Thus evaluation is surjective on every specified Hom space.

<2>3. Identities, matrix multiplication, dagger and the D1262 associators
are pointwise, so evaluation is a full strong monoidal star-functor.
This assertion does not require essential surjectivity for a fixed large I.

<2>4. Restriction commutes with all these operations. D1265 therefore
defines a germ star-category, with full canonical evaluation at one and
essential surjectivity by <1>3. It is not assigned a C*-norm. **QED**

<1>5. **PROVE** an endpoint unitary between chosen object lifts has a local
unitary lift, including when their ambient matrix sizes differ.

<2>1. Let `v0:X(q0)->Y(q0)` satisfy `v0^*v0=p_X(q0)` and
`v0 v0^*=p_Y(q0)`. Lift it to the rectangular corner section a by <1>4.
Set `S=a^*a`. Then `S(q0)=p_X(q0)`.

<2>2. Shrink until `||S-p_X||<1/2`. The binomial series in the source
corner, with constant term p_X, gives a continuous inverse square root
`S^(-1/2)`. Put `v=a S^(-1/2)`. Then `v^*v=p_X` and v(q0)=v0.

<2>3. The endomorphism `vv^*` is a projection in End(Y), dominated by p_Y.
Thus `p_Y-vv^*` is a projection. It is continuous and zero at q0.
After shrinking its norm is less than 1, so it is zero: every nonzero
orthogonal projection has norm 1. Hence `vv^*=p_Y` locally.

<2>4. This also compares two independently chosen lifts of the same endpoint
projection object, by lifting its endpoint identity. It supplies an explicit
unitary between the two local objects, not a declaration that their
projection sections are literally equal. **QED**

<1>6. Steps <1>1–<1>5 prove KLIFT-1. **QED**

## Theorem KLIFT-2 (normalized local data and the dimension-ratio dual)

**ASSUME** a finite family of already lifted nonzero D1261 objects near q0.
**PROVE** finite families of states, POVMs and normalized Kraus instruments
lift locally; their normalized density dual is `w_Y/w_X` times the raw
Kraus transport, with the stated classical-output factor.

<1>7. **PROVE** raw register elements lift on the chosen objects.

<2>1. KLIFT-1 <1>4 gives raw sections for all matrix-corner morphisms,
including endomorphisms. Evaluation is also onto a tensor-register algebra:
a fibre element is a finite sum of elementary tensors of fibre corner
elements, each of which has such a raw lift.

<2>2. Classical factors C^O are constant finite-dimensional algebras, so lift
their components separately. Products and trace pairings are continuous by
KCOM-2 and the balanced tensor construction.

<2>3. When additional local open conditions are needed below, only finitely
many occur. One common smaller compact interval satisfies all of them. **QED**

<1>8. **PROVE** every normalized state density lifts.

<2>1. For `rho0>=0`, `tau_X,q0(rho0)=1`, take its positive square root c0
in the fibre finite C*-algebra. Lift c0 raw by <1>7.

<2>2. Put `H=c^*c` and `z(q)=tau_X,q(H(q))`. It is a continuous positive
scalar with z(q0)=1, hence bounded away from zero on a smaller interval.

<2>3. Then `rho=H/z` is a positive normalized state section evaluating to
rho0. This proof permits rank-deficient states. The normalization uses
D1263's actual corner trace and works on arbitrary finite register words.
The preparation functional is `a |-> tau_X(rho a)`. **QED**

<1>9. **PROVE** finite POVMs and effects lift.

<2>1. Lift each square root of an endpoint POVM element to c_o and put
`A_o=c_o^*c_o`, `S=sum_o A_o`. Then S(q0)=1_X(q0).

<2>2. By the source-corner binomial construction of <1>5, S has a continuous
inverse square root locally. Set `e_o=S^(-1/2) A_o S^(-1/2)`.
Every e_o is positive and their sum is the corner unit. Evaluation gives the
original POVM because S(q0) is the unit.

<2>3. The two-outcome POVM `(e,1-e)` handles an arbitrary effect. A POVM
is only its Heisenberg map from C^O; no postmeasurement quantum state is
inferred without a specified instrument. **QED**

<1>10. **PROVE** any given finite normalized Kraus family lifts.

<2>1. Let `K_(o,i),0:X(q0)->Y(q0)` satisfy total completeness. Choose raw
rectangular corner lifts A_(o,i) by KLIFT-1 <1>4 and set
`S=sum_(o,i) A_(o,i)^* A_(o,i)` in End(X).

<2>2. S(q0)=1_X(q0). On a smaller interval define
`K_(o,i)=A_(o,i) S^(-1/2)`. Then

    sum_(o,i) K_(o,i)^*K_(o,i)=S^(-1/2) S S^(-1/2)=1_X.

The family has its original types, is continuous, and evaluates to the
prescribed family. Zero branches and arbitrary finite graded supports cause
no problem; unsupported Hom components remain zero.

<2>3. A fixed endpoint scalar-unitary mixing of a chosen representative
can be applied to its lift as a constant matrix. We assert existence of a
lift, not a unique germ for its equivalence class or a continuous choice
of mixing matrices for every pair of fibrewise-equivalent sections. **QED**

<1>11. **PROVE** the normalized density factor is w_Y/w_X.

<2>1. For outcome o put

    T_o(rho)=(w_Y/w_X) sum_i K_(o,i) rho K_(o,i)^*.

KCOM-2's cross-object cyclicity gives, for a in End(Y),

    tau_Y(T_o(rho)a)
      =theta_Y(sum_i K_(o,i)rho K_(o,i)^*a)/w_X
      =theta_X(rho sum_i K_(o,i)^*aK_(o,i))/w_X.

This is precisely the Heisenberg/Shrödinger trace-duality identity.

<2>2. Each T_o is positive and its trace is the branch Born weight.
Summing outcomes gives total trace one by Kraus completeness. Relative to
`tau_Y tensor tau_O`, where tau_O is uniform, the full output density has
o-block `|O| T_o(rho)`; evaluating the product trace cancels this factor.

<2>3. For parabolic X_alpha and X_beta, KCOM-3 <1>19 gives
`w_Xalpha=1/P_alpha`, `w_Xbeta=1/P_beta`. Hence
`w_Y/w_X=P_alpha/P_beta`, exactly the normalized parabolic density ratio.
For a unitary v:X->Y, w_X=w_Y by cyclicity, so density transport is simply
`rho |-> v rho v^*`. **QED**

<1>12. **PROVE** retained collective extensions remain normalized.

<2>1. The list `K_(o,i) tensor 1_Z` is in
`Hom(X tensor Z,Y tensor Z)` by KCOM-1. Its sum of adjoint squares is
`1_X tensor 1_Z=1_(X tensor Z)` by interchange.

<2>2. For two lists K,L the direct ordered parallel list consists of
`K_(o,i) tensor L_(p,j)`. Completeness follows in the same way. Associative
nesting and the branch operator products follow from the actual monoidal
functor. The full outcome-wire equations use hypothesis W, not an implicit
swap of classical and quantum wires.

<2>3. The density ratio for right context is unchanged, since
`w_(Y tensor Z)/w_(X tensor Z)=w_Y/w_X` by KCOM-2. Thus retained context
uses the full collective algebra and the same correctly normalized process.
Steps <1>7–<1>12 prove KLIFT-2. **QED**

## Theorem KOP-1 (operational extension of the full composition category)

**ASSUME** hypothesis W of D1266, in addition to KCOM-1–3 and KLIFT-1–2.
**PROVE** the full completion has a controlled UCP operational category,
continuous/germ evaluations, local lifts of individual finite endpoint
circuits, and continuous finite-tree Born probabilities with positive-limit
conditioning. It extends the parabolic operational construction.

<1>13. **PROVE** every D1266 generator has a typed UCP realization.

<2>1. Preparation is the normalized positive functional of <1>8. Discard
is the unit map in Heisenberg orientation. POVMs give a UCP map from C^O:
at matrix level each positive scalar matrix at outcome o tensors with the
positive effect e_o, and their sum is positive. Completeness gives unitality.

<2>2. Each corner-instrument summand is `a |-> K^*aK` inside the faithful
matrix realization, hence CP at every amplification. Total completeness
makes the full map from `End(Y) tensor C^O` unital. Its density dual is
<1>11, including both trace factors.

<2>3. Assembly and split are KCOM-3's UCP maps E and j in the declared
Heisenberg directions. Their separated retract equation is Ej=id, and their
associativity is the expectation/inclusion tower of KCOM-3 <1>18.

<2>4. W supplies correctly typed classical wires and their sound relations.
Stable list mixing cancels within each outcome; typed branch composition and
parallel formulas follow by substitution of the actual matrix lists.
For continuous labels impose the repaired core's pointwise coefficient-Gram
equality, and for germs its eventual version. At each fibre, the finite Gram
lemma supplies scalar mixing, so the same cancellation proves congruence
under products and retained contexts. This is CWIR-3's argument applied to
the finite ambient matrix-Hecke coordinate spaces; no continuous mixing
matrix is needed. Thus the change of equality convention is sound.
Thus all stipulated relations are equality of typed UCP maps. **QED**

<1>14. **PROVE** realization and evaluation descend to the presented categories.

<2>1. Quotient the free typed ordered monoidal circuit category by the
congruence generated by the sound relations in W and <1>13. Composition
and tensor of UCP maps are UCP, so the generator realizations determine a
monoidal functor to D1206's Heisenberg UCP category.

<2>2. On an interval the same formulas act continuously on sections:
Kraus maps use products and adjoints, preparations use continuous traces,
and E is continuous by the explicit Gram proof KCOM-3 <1>17.
W's fixed classical wiring maps introduce no parameter discontinuity.

<2>3. Evaluation of objects and labels preserves each imposed relation.
Pointwise Gram equality evaluates to Gram equality in a fibre, which is
equivalent there to scalar-unitary mixing. The explicit D1218 wiring,
including the one-outcome identity relation, supplies hypothesis W.
Hence there are monoidal evaluation functors from Op^U_I to Op^U_q and
from Op^U_1,germ to Op^U_1. Only the endpoint evaluation is canonical on
arbitrary germs.

<2>4. No claim of faithful realization or of equality of germs from
pointwise-equal isolated CP shadows is made. Eventual coefficient-Gram
equality is the stated label relation, while a continuous scalar-unitary
mixing is a stronger property and is not inferred. **QED**

<1>15. **PROVE** a finite endpoint circuit can be lifted with its chosen
boundary objects, after those objects have been lifted locally.

<2>1. List its finitely many named endpoint quantum objects and lift all
projection presentations by KLIFT-1, choosing one lift for each repeated
object. Lift state, POVM and ordinary Kraus labels by KLIFT-2.

<2>2. A structural box may create a tensor object X tensor Y. The chosen
lift of that endpoint object need not equal the tensor of the independently
chosen lifts of X and Y. Both local objects evaluate to the same endpoint
matrix projection presentation under the fixed D1262 indexing.

<2>3. Apply KLIFT-1 <1>5 to its endpoint identity to get a local unitary
`w: X_tilde tensor Y_tilde -> (X tensor Y)_chosen`. This is a named
connector, whose one-Kraus process evaluates to the identity by W.

<2>4. Lift an assembly box by `U_w o asm_(X_tilde,Y_tilde)` and split by
`spl_(X_tilde,Y_tilde) o U_(w^*)`. Both have the chosen endpoint-object
lifts as their actual boundary types and evaluate to the original boxes.

<2>5. For a retained context or direct collective parallel box, form the
retained lifted list on the structural tensor objects and conjugate its
source/target by the corresponding connectors. The list stays normalized,
and endpoint evaluation is the original retained list.

<2>6. Separated register tensors, POVMs, preparations and classical wiring
already use the chosen wire lifts. A finite classical control, if included
by W as a blockwise family of admitted labels, is lifted by lifting its
finitely many component labels. No extra arbitrary CP data is required.

<2>7. Finitely many raw lifts, normalizations and connectors require only
finitely many neighborhoods. Intersect them and compose the lifted boxes
in the original finite planar graph. Evaluation of every connector is an
identity, so the resulting circuit evaluates to the original morphism.
This proves local fullness of circuit evaluation for its chosen boundary
lifts, without requiring that every box lift remain a single generator.
**QED**

<1>16. **PROVE** the lift does not assert preservation of all endpoint equations.

<2>1. Different projection lifts and connector choices need not agree as
germs. The construction of <1>15 lifts a representative circuit; it is not
a functor assigning one preferred lift to every endpoint morphism.

<2>2. Two representatives of the same endpoint arrow may therefore lift to
different arrows whose evaluations agree. Extra commuting diagram equations,
coincident tensor decompositions and pointwise CP equalities are not imposed
on the chosen lifts. This is consistent with fullness and essential
surjectivity of evaluation, neither of which asserts faithfulness.

<2>3. Equalities that are relations of the presented interval category do
hold there by <1>14. The scope distinction is between these proved relations
and additional equalities that happen only after endpoint evaluation. **QED**

<1>17. **PROVE** branch density transport of every continuous circuit is continuous.

<2>1. Locally choose bases of the input and output endomorphism corners by
KCOM-3 <1>16. For separated registers use their tensor bases and for
classical registers the standard coordinate basis.

<2>2. A generator's Heisenberg coefficients are continuous by <1>14.
In these bases the normalized trace pairing is a continuous invertible
Gram matrix. Solving the finite trace-duality equations therefore gives a
continuous Schrödinger matrix for every generator, even for E and j.

<2>3. Finite composition, tensor and classical outcome extraction use
finite products and sums of these continuous matrices. They preserve
continuous unnormalized branch density sections. Positivity follows from
the CP outcome map; no conditioning division is used at this stage. **QED**

<1>18. **PROVE** the finite protocol probabilities have the asserted limit.

<2>1. Start with a normalized continuous density and a finite tree of typed
circuits, specified instruments and terminal effects. Induction over tree
depth using <1>17 gives continuous positive branch densities.

<2>2. Each leaf weight is the continuous normalized trace pairing with its
effect. It is nonnegative. The child masses sum to the parent mass by
unitality of the full instrument; terminal unit effects give total mass 1.
Event weights are finite sums. Evaluation commutes with all these operations.

<2>3. For a conditioned probability N(q)/D(q), assume D(1)>0. Continuity
then gives `D(q)>D(1)/2` on a smaller interval, and the ratio converges to
N(1)/D(1). No assertion is made at a zero limiting conditioning weight.
Finite germ protocols use one common representative interval. **QED**

<1>19. **PROVE** the construction is the promised glue to the parabolic core.

<2>1. KCOM-1 <1>5 embeds Gamma fully and its additive self-adjoint
completion is all U. KCOM-3 <1>19 identifies its normalized traces, j and
E with the parabolic ones. KLIFT-2 <1>11 identifies the density ratio.

<2>2. Restrict D1266's generator assignments to parabolic atoms and their
words, with the same repaired wiring W. Each matrix list, state/effect,
assembly/split and retained context formula is the original parabolic
formula. The restriction is thus compatible with realization and every
evaluation functor; no claim of full-circuit faithfulness is needed.

<2>3. Every nonzero full finite completion object now has states, effects,
preparations/discards, retained Kraus instruments, traced assembly and finite
protocols by the directly proved construction, although U has no assumed
rigidity, spherical structure or fusion property.

<2>4. This replaces the inapplicable D1121 reference in D1224. Generic
algebraic evaluation retains its former limited coefficient domain; the new
local positive section/germ evaluation reaches every fibre projection by
KLIFT-1. It neither specializes all Weyl observables nor asserts arbitrary
CP-map completeness. Steps <1>13–<1>19 prove KOP-1. **QED**
