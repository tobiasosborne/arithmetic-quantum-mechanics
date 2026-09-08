# Regular one-sided operational specialization of the mirabolic bridge

Repair prover: gpt-6-astra, xhigh. Status: PROVED within the stated hypotheses. Admission and repaired scope
are recorded in `../../verdicts/f1-limit-adjudication.md`.

## Theorem MIR-REG (the regular operational boundary category and functor)

**ASSUME** the based mirabolic algebras of D1246, MIR-POS for every real
q>1, MIR-EXPECT, MIR-END, and the classical-wiring hypothesis W of D1257.
**PROVE** D1257 defines actual one-sided section and germ circuit categories,
and coefficient evaluation followed by the GNS quotient defines D1258's
monoidal UCP-realized endpoint functor. Regular normalized states, effects,
POVMs and retained Kraus instruments descend; all generated finite protocols
have convergent Born weights and positive-limit conditioning. Every finite
endpoint Hecke protocol has a local regular lift.

<1>1. **PROVE** regular sections form a well-defined star algebra.

<2>1. For `J=[1,1+epsilon]`, take the finite free C(J)-module with basis
`T_(w,A)` and multiply coefficients with Rosso's polynomial structure
constants. Evaluating at any q gives the based fibre algebra.

<2>2. Multiplication is a finite sum of products of continuous functions
and polynomial functions of q. It therefore preserves this module.
Associativity and its identity hold by the polynomial algebra identities.

<2>3. D1246's star conjugates coefficients and permutes orbit labels by
flag swap and vector negation, independently of q. In standard-pair
coordinates, swapping `(F_0,wF_0,v_A)` and acting by w^(-1) produces
`(F_0,w^(-1)F_0,-v_(w^(-1)A))`. The map w^(-1) identifies the two posets,
and negation does not change support. This verifies the explicit star formula.

<2>4. The physical orbit involution is antimultiplicative by the kernel
calculation MIR-AFF `<1>7`; its polynomial identities extend to sections.
The coefficient trace is continuous by its defining coordinate functional.

<2>5. These are coefficient-topological algebra statements. MIR-POS makes
every fibre with q>1 a finite C*-algebra, but no C*-norm at the degenerate
boundary or on the whole regular section algebra is asserted. **QED**

<1>2. **PROVE** all separated register words have compatible regular algebras.

<2>1. A Hecke factor uses the CLIM-1 continuous section algebra restricted
to J. Its normalized basis and its T basis differ by continuous nonzero
powers of q, so either gives the same continuous-coefficient sections.

<2>2. For a finite word take the product of the atom bases and any classical
coordinate bases, with continuous coefficients in the same one parameter.
At q>1 this is the ordinary finite-dimensional spatial tensor-product algebra.
It is a C(J)-balanced section tensor, not a tensor with independent parameters.

<2>3. Pointwise multiplication, star and the product normalized trace are
continuous in these product coordinates by <1>1. Classical traces are uniform
on finite nonempty sets; the empty register word has scalar algebra C.

<2>4. Juxtaposition of words and these operations supply ordered separated
tensor. In particular there is no inferred map from `[R_m][R_n]` to
`[R_(m+n)]`. The D1256 arithmetic shuffle correspondences are separate data
and are not generators in this regular category. **QED**

<1>3. **PROVE** the algebraic quotient maps exist on every endpoint word.

<2>1. MIR-END identifies `N_n=span{T_(w,A):A nonempty}` as a two-sided
star ideal and identifies `Pi_n=E_1:R_n(1)->H_n(1)` as its unital star
quotient. It satisfies `Pi_n i_1=id` and `tau_R,1=tau_H,1 Pi_n`.

<2>2. Tensor these quotient maps with the identity on each Hecke and
classical factor to get a surjective unital star-map
`Q_X:B_X,alg(1)->B_bar(X)`.
The product trace satisfies `tau_X,1=tau_bar(X) Q_X`.

<2>3. Its target is a finite C*-algebra with faithful product trace: every
quantum factor is H_n(1)=C[S_n] and every classical factor is C^O.
No assertion of faithfulness is made about the unquotiented source trace.

<2>4. Every x in this target has a continuous raw lift x(q): expand in
Hecke and classical bases, use constant coefficients, and apply i_q in each
mirabolic factor. Then `Q_X(x(1))=x`. These lifts need not be states or
effects; only their algebraic regularity is needed for positivity testing.
**QED**

<1>4. **PROVE** every admitted regular positive density has positive quotient.

<2>1. Let h be coefficient-continuous with `h(q)>=0` for every q>1 in J.
For any target element x use the raw lift from <1>3. Then

    tau_X,q(x(q)^* h(q) x(q)) >= 0                 (q>1).

This holds in each honest positive fibre by MIR-POS and the product trace.

<2>2. Coefficient continuity and polynomial multiplication permit passage to
q=1. By the star quotient and trace identity in <1>3 the limit is

    tau_bar(X)(x^* hbar x) >= 0,     hbar=Q_X(h(1)).

Self-adjointness of h(q) on the punctured interval likewise passes to hbar.

<2>3. If hbar had a negative spectral subspace, its spectral projection r
would satisfy `tau_bar(X)(r hbar r)<0` by faithfulness, contradicting <2>2
with x=r. Thus hbar is positive.

<2>4. If h is a normalized D1249 density, its continuous coefficient trace
has limit 1. Hence `tau_bar(X)(hbar)=1`. This proves a positive normalized
endpoint density without positing positivity at the algebraic boundary.
The proof also applies to unnormalized positive branch density sections.
**QED**

<1>5. **PROVE** regular effects and POVMs descend.

<2>1. For an admitted effect e, both e and `1-e` are positive in every
punctured real fibre. Apply <1>4 to both to obtain
`0<=Q_X(e(1))<=1` in the endpoint algebra.

<2>2. Each member of a finite POVM has a positive quotient. Its sum is the
unit because the defining sum relation holds on the punctured interval and
extends by coefficient continuity and Q_X multiplicativity.

<2>3. The endpoint POVM therefore defines the usual UCP map from its
classical output algebra. Matrix-level positivity follows by summing positive
scalar matrix blocks tensored with these endpoint effects. **QED**

<1>6. **PROVE** regular retained Kraus normalization passes to the endpoint.

<2>1. Let K_(o,i) be a regular finite same-register family in D1257.
The coefficients of `sum K_(o,i)^*K_(o,i)` are continuous on J by <1>1–2.
Since the sum equals 1 throughout q>1, it equals 1 at q=1 algebraically.

<2>2. Applying Q_X gives

    sum_(o,i) Kbar_(o,i)^* Kbar_(o,i)=1,
    Kbar_(o,i)=Q_X(K_(o,i)(1)).

Thus the endpoint list is an honest normalized instrument and defines a
UCP map from `B_bar(X) tensor C^O` to B_bar(X).

<2>3. For any algebraic boundary input `(a_o)_o`, multiplicativity gives

    Q_X(sum_(o,i) K_(o,i)(1)^* a_o K_(o,i)(1))
      =sum_(o,i) Kbar_(o,i)^* Q_X(a_o) Kbar_(o,i).

The branch maps therefore annihilate the appropriate quotient kernel and
descend as maps, not merely as a selected list of scalar probabilities.
**QED**

<1>7. **PROVE** the inclusion/retraction processes descend with their types.

<2>1. The process `up_n:[H_n]->[R_n]` has Heisenberg map E_q, and
`down_n:[R_n]->[H_n]` has map i_q. MIR-EXPECT proves both UCP and traced
for q>1, with `E_q i_q=id`.

<2>2. Both maps are coefficient-continuous: i retains the zero-vector
basis and E deletes the others. At the endpoint

    Pi_n i_1=id_(H_n(1)),       E_1=Pi_n.

These are exactly the two quotient-intertwining equations for sending both
processes to identity on H_n(1).

<2>3. In Heisenberg order, `down o up` realizes `E i=id` on H_n, so
its stated relation is sound. The reverse realizes iE on R_n and is generally
proper away from one; it is not imposed as an interval identity.

<2>4. Tensoring these maps onto separated contexts preserves their UCP,
trace and quotient-intertwining properties. This is actual spatial tensor
of maps, not a cross-rank mirabolic assembly claim. **QED**

<1>8. **PROVE** preparation, discard and all named classical wiring descend.

<2>1. Preparation of h realizes `a |-> tau_X,q(h(q)a)`.
At q=1 its value is
`tau_bar(X)(hbar Q_X(a))` by <1>3–4, so it factors through the quotient.
Discard is the unit map; Q_X preserves the unit.

<2>2. A POVM factors by <1>5, and a Kraus instrument by <1>6. The output
classical factors are unchanged by Q. Their uniform trace density block is
`|O|sum_i K_(o,i)hK_(o,i)^*`, exactly as in D1257.

<2>3. W's classical product, relabeling, unit and routing maps act by fixed
coordinate maps, carrying quantum coefficients along unchanged. Hence they
commute with the factorwise Q maps and have their stated endpoint UCP maps.
A finite classical control is a direct blockwise combination of the already
verified labelled maps, so the same assertion holds block by block. **QED**

<1>9. **PROVE** pointwise Kraus-Gram equality is a legitimate label relation.

<2>1. For a fixed regular product basis `(b_a(q))`, write
`K_i(q)=sum_a k_i(a,q)b_a(q)` within one outcome, and put
`J_K(a,b;q)=sum_i k_i(a,q)conjugate(k_i(b,q))`.
These coefficient Grams are continuous scalar matrices on J.

<2>2. At any fixed q>1, equal Grams mean that the finite coefficient-column
vectors have equal inner products. The induced isometry of their spans
extends after zero padding to a scalar unitary on the Kraus index. Therefore
all branch CP actions agree, including those formed after retained
factorwise inclusion or separated tensor extension.

<2>3. Composition and tensor preserve this relation at each fixed q:
the corresponding mixing matrices are finite tensor or block unitaries.
Thus their resulting coefficient Grams agree pointwise. This argument does
not select a continuous unitary family, and none is required by D1257.

<2>4. Equal Grams on q>1 have equal coefficient limits at one.
If M is the fixed linear coefficient map of Q_X at one, the quotient-list
Grams are `M J_K(1) M^*`; they are therefore equal. The endpoint scalar-unitary
relation is respected, even when the quotient kills some Kraus entries.
**QED**

<1>10. **PROVE** the raw circuit quotient is an actual operational category.

<2>1. Begin with finite typed planar circuits on the D1257 register words.
Vertical composition glues equal wire words; horizontal juxtaposition is
ordered word tensor. The free category/monoidal axioms have their usual
pointwise UCP realization.

<2>2. W supplies the explicit outcome product and classical-wire routing
in every multi-outcome relation. In particular a list-product formula never
silently identifies `X O Y P` with `X Y (O times P)`.

<2>3. Literal state/POVM equality, pointwise within-outcome Gram equality,
typed list identities and the separated retract relation are sound by
<1>5–9. Close the generated equivalence under all typed circuit insertions.
This makes a congruence, and its quotient is RegOp_J.

<2>4. All generator realizations are UCP at every q>1. The sound congruence
therefore gives a monoidal realization in finite-dimensional Heisenberg UCP
maps. Equality is not defined by an arbitrary isolated CP-shadow quotient.
No C*-norm on these circuit Hom sets is claimed. **QED**

<1>11. **PROVE** coefficient evaluation defines the endpoint functor.

<2>1. On objects replace R_n by H_n and retain Hecke/classical factors.
On states, effects and lists use their Q images from <1>4–6; send up/down
to identity by <1>7. Use the same W wiring at the endpoint.

<2>2. Every generator map intertwines the source/target Q maps by <1>6–8.
Every presentation relation evaluates to a valid endpoint relation by
<1>9–10, including stable scalar-unitary equality at a fixed endpoint.

<2>3. The universal property of the free category modulo a congruence gives
`Ev_(1+),J:RegOp_J->Op_H,1^sep`. It preserves composition and ordered tensor,
and realization commutes with coefficient evaluation followed by Q.
This is an actual functor, with an explicit source, target and equality.

<2>4. Restriction to smaller one-sided intervals is also a functor, since
positivity, completeness and all relations persist under restriction.
Germs of labelled circuits consequently form RegOp_(1+); equal germs have
equal endpoint evaluations. This proves D1258's canonical germ functor.
Other q evaluations require a representative interval containing q. **QED**

<1>12. **PROVE** every generated branch density has regular coefficients.

<2>1. For a same-register instrument the unnormalized branch transport is
`h |-> sum_i K_(o,i)hK_(o,i)^*`. Finite products keep its coefficients
continuous. Full classical output and extraction insert only the fixed
factor |O| or its inverse, according to the uniform trace convention.

<2>2. The normalized-trace duals of E_q and i_q are respectively i_q and
E_q by MIR-EXPECT's trace pairing. Both preserve regular coefficients.
Preparation supplies h; discard takes the continuous trace; a POVM produces
classical density coordinates `|O|tau_X,q(h e_o)`.

<2>3. The trace duals of W's fixed classical maps have fixed finite matrices
with the stated uniform-cardinality factors. Thus they also preserve
coefficient regularity. Finite control is treated componentwise.

<2>4. By induction over a finite circuit, every outcome's unnormalized
positive density remains coefficient-continuous. This uses the explicit
allowed generators. It does not invert a trace Gram matrix that degenerates
at one, and it makes no assertion for an arbitrary regular superoperator.
**QED**

<1>13. **PROVE** finite Born probabilities converge operationally.

<2>1. A finite protocol is a finite typed instrument tree with a regular
normalized root density, specified generator/circuit instruments, and regular
terminal effects. A later label may depend on the finite outcome history.

<2>2. Induction on its finite depth using <1>12 gives positive regular
unnormalized branch densities. Their quotient densities are positive by
<1>4, and <1>6–8 identifies their endpoint transport with the evaluated tree.

<2>3. Each Born weight is a coefficient-continuous trace pairing. Its limit
is the pairing of the quotient density and quotient effect, by <1>3.
Finite sums give event weights. Total child mass equals parent mass by
unitality; normalized root mass is one. Hence these are probabilities, not
just convergent formal coefficients.

<2>4. If a conditioning event has weight D(q) with D(1)>0, continuity gives
`D(q)>D(1)/2` after shrinking. For a subevent N the ratio N(q)/D(q) converges
to N(1)/D(1). No zero-limit conditioning assertion is made.
Finite germ protocols are represented on one common one-sided interval.
**QED**

<1>14. **PROVE** endpoint Hecke data and finite protocols have regular lifts.

<2>1. Given an endpoint Hecke density or finite POVM on a register, use the
core CLIM-1/LLIM-2 raw lift of its square roots and normalization:
`c^*c/tau(c^*c)` for a density and `S^(-1/2)c_o^*c_o S^(-1/2)` for a POVM.
These are continuous and positive on a real neighborhood of one.

<2>2. For a normalized endpoint Kraus family, the same core local proof
lifts its entries raw and multiplies on the right by
`(sum_i Khat_i^*Khat_i)^(-1/2)`. It preserves the original endpoint list
and yields exact normalization near one. Restrict all these lifts to q>=1.

<2>3. Embed any desired Hecke factors in mirabolic registers through i_q.
MIR-EXPECT preserves positivity and normalized trace in every real q>1,
and the orbit coefficients stay continuous. Pi_n i_1=id recovers the
original endpoint data.

<2>4. A finite endpoint circuit has finitely many such labels; choose one
common neighborhood and use its fixed W wiring. The lifted labelled circuit
evaluates to it. If its prescribed source/target register words use mirabolic
atoms, attach tensor products of down/up to reach those words; their
endpoint evaluations are identities by <1>7.

<2>5. This is local existence for individual circuits, not a canonical
section of evaluation or preservation of all additional endpoint diagram
equations. Steps <1>1–<1>14 prove MIR-REG. **QED**

## Boundary exclusions required by the source category

<1>15. **PROVE** positivity on arithmetic fibres cannot replace D1249's
real-neighborhood hypothesis.

<2>1. In H_2(q) put `e_+=(T_1+1)/(q+1)` and
`e_-=(q-T_1)/(q+1)`. Their traces are 1/(q+1) and q/(q+1).
The coefficient-regular expression
`h(q)=(q-3/2)e_+ +(5/(2q))e_-` has trace one by direct substitution.

<2>2. It is positive at every prime power Q>=2, but for `1<q<3/2` its
trivial-sector eigenvalue is negative. At one it equals `1-(3/2)T_1`,
with eigenvalues -1/2 and 5/2. It is not a D1249 regular density label.
Thus the repaired domain excludes the exact O1 counterexample. **QED**

<1>16. **PROVE** a coefficient-regular UCP superoperator need not descend.

<2>1. In rank one use MIR-END's projections e and f=1-e, whose trace
weights are 1/q and (q-1)/q. The density `h_s=q/(q-1)f` is positive and
normalized for every q>1 but has a coefficient pole at one.

<2>2. Its state functional has `omega_s(1)=1` and `omega_s(T_0)=-1`,
because `T_0=q e-1` acts as -1 on the f sector. These superoperator
coefficients are constant in the basis `(1,T_0)`.

<2>3. Yet `Pi_1(T_0)=0` by MIR-END, so this functional does not factor
through the boundary quotient. It cannot be a regular preparation of D1257,
whose density coefficients must be continuous. This proves why merely
regular arbitrary UCP matrices cannot be added to the source class.

<2>4. The excluded family remains a valid positive punctured-fibre state
requiring additional boundary data. No classification of such singular
boundary rules, generic mirabolic assembly, or full Weyl specialization is
claimed here. **QED**
