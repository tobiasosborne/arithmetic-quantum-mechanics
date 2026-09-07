# Operational subsystem nets from finite C*-tensor data

Status: CPOP-1/2/3/5 are PROVED after the capped operational review;
CPOP-4 (Fibonacci comparison) remains supporting SKETCH. The zero-object
hypothesis was repaired explicitly; definitions are authoritative in definitions.md.
Scope: finite-dimensional C*-algebras only.  The results below do not require
a strong monoidal fibre functor to Hilbert spaces.  They give (i) a general
unitary-fusion-category construction, (ii) a smaller process class for which
context extension is part of the data, and (iii) a concrete symmetric-group
net that can serve as the operational completion of a proposed `q=1` fibre.

Source convention: `Tr_X` is the unnormalised positive categorical trace and
`tau_X=Tr_X/d_X`, where `d_X=Tr_X(1_X)`.  Densities are normalised by
`Tr_X(rho)=1`; this avoids hidden dimension factors in Schrödinger channels.

## Definition restatements (D1121--D1125; authoritative in definitions.md)

**D1121 (finite categorical subsystem net).**  A finite categorical subsystem
datum is a unitary fusion category `C`, with its positive spherical structure,
together with a tensor-closed replete family `S` of **nonzero** objects
containing the unit. Thus every `d_X>0`; zero morphisms remain allowed.  It assigns

    A_X := End_C(X),
    Tr_X(f) := the positive categorical trace of f,
    tau_X := Tr_X/d_X,
    j_X,Y(f tensor g) := f tensor g in A_(X tensor Y).

Associators are retained as comparison maps rather than suppressed as equalities.
For every assembly inclusion `j_X,Y`, `E_X,Y` denotes the `tau_(X tensor Y)`-
preserving conditional expectation onto its image.  The datum includes all
iterated inclusions and expectations, related by associator conjugacy and the
tower law for nested inclusions.

**D1122 (operational realisation of D1121).**  For `X` in D1121's nonzero family, a state is either a
normalised positive functional `omega:A_X -> C`, or its unique density
`rho>=0` satisfying `Tr_X(rho)=1` and `omega(a)=Tr_X(rho a)`.  An effect is
`0<=e<=1`; its Born probability is `omega(e)`.  Restriction from a composite
to an assembly subalgebra sends `rho` to `E_X,Y(rho)`.  Preparation sends a
density `sigma` on `A_X tensor A_Y` to `j_X,Y(sigma)`; equivalently, the
prepared functional is `omega_sigma o E_X,Y`.

**D1123 (context-complete categorical Kraus process).**  For nonzero `X,Y` in the family of D1121, a Kraus process
`K:X->Y` is a finite list of category morphisms `K_i:X->Y` such that
`sum_i K_i^* K_i=1_X`.  Lists are identified only under stable scalar-unitary
mixing: pad two lists by zero morphisms to a common length and apply one
ordinary unitary matrix to the Kraus index.  Its isolated Heisenberg shadow and
Schrodinger action are

    Phi_K(a) = sum_i K_i^* a K_i,       a in A_Y,
    T_K(rho) = sum_i K_i rho K_i^*,     rho in A_X.

Its right-context action is retained as data:

    Phi_K^Z(a) = sum_i (K_i^* tensor 1_Z) a (K_i tensor 1_Z),
                 a in A_(Y tensor Z).

Composition is the list `(L_j K_i)_(j,i)` and tensor product is
`(K_i tensor L_j)_(i,j)`, with the category associators.  This is a sufficient
process class; it is not stipulated to contain every CP map between `A_X` and
`A_Y`.

**D1124 (charge-carrying dilation process).**  A dilation between nonzero objects `X->Y` is a named
nonzero environment `E` and an isometry `v:X->Y tensor E`.  It induces

    Phi_v(a)=v^*(a tensor 1_E)v.

Sequential composition is always defined and retains the ordered environment.
Parallel composition is defined when the environment can be moved past the
other output by named unitary interchange data: in particular in a braided
unitary fusion category, or when the environment has a specified half-braiding.
No parallel product for arbitrary charge-carrying environments is stipulated
in a merely monoidal category.

**D1125 (finite-injection symmetric-group quantum net).**  For a finite set
`S`, put

    G(S)=Sym(S),              A(S)=C[G(S)],
    (sum a_g g)^*=sum conjugate(a_g) g^(-1),
    tau_S(sum a_g g)=a_1.

For an injection `f:S->T`, extend permutations of `S` by the identity off
`f(S)` to obtain `i_f:A(S)->A(T)`.  Let `E_f` delete coefficients outside
`i_f(G(S))` and identify the remaining subgroup algebra with `A(S)`.  Disjoint
union gives `mu_S,T:A(S) tensor A(T)->A(S disjoint-union T)` by block
permutations.  A local process is a stably unitary-equivalent finite list
`K_i in A(S)` with `sum K_i^*K_i=1`; its action in an ambient injection
`f:S->T` uses the retained list `i_f(K_i)`.  This construction is a proposed
operational `q=1` fibre, not a uniqueness claim about quantum mechanics over
`F_1`.

## Proposition CPOP-1: observable algebras, traces, and assembly

**Statement.**  D1121 assigns finite-dimensional C*-algebras with faithful
positive traces.  Each `j_X,Y` is an injective unital star-homomorphism and

    Tr_(X tensor Y)(j_X,Y(f tensor g)) = Tr_X(f) Tr_Y(g).

The inclusion can be proper; no equality with an ordinary tensor product of
observable algebras is asserted.

**Proof.**
<1>1. ASSUME the data of D1121 and choose representatives `a` of the finitely
many simple objects of `C`.
<1>2. Decompose `X` as `direct-sum_a a^(direct-sum m_a)`.
<2>1. Semisimplicity and Schur's lemma identify
`A_X = direct-sum_a M_(m_a)(C)` as a star-algebra.
<2>2. Hence `A_X` is a finite-dimensional C*-algebra.
<1>3. In this decomposition,

    Tr_X(f)=sum_a d_a tr_(m_a)(f_a),

where every `d_a>0` in the positive spherical structure.
<2>1. Positivity follows because each ordinary matrix trace is positive and
each weight is positive.
<2>2. Faithfulness follows because `Tr_X(f^*f)=0` forces every positive
matrix block `f_a^*f_a` to vanish.
<2>3. `Tr_X(1_X)=sum_a d_a m_a=d_X`, so `tau_X` is a faithful tracial state.
<1>4. Tensoring morphisms is bilinear, multiplicative, unital, and dagger
preserving, so `j_X,Y` is a unital star-homomorphism.
<1>5. The spherical trace is multiplicative on tensor products.
<2>1. Equivalently, expand simples and use
`d_a d_b=sum_c N_ab^c d_c`, the dimension character of the fusion ring.
<2>2. This gives the displayed trace identity first on simple matrix units
and hence by linearity on all `f tensor g`.
<1>6. The trace identity extends to the algebraic tensor product:

    (Tr_X tensor Tr_Y)(z^*z)=Tr_(X tensor Y)(j(z)^*j(z)).
<2>1. If `j(z)=0`, faithfulness of `Tr_X tensor Tr_Y` gives `z=0`.
<2>2. Thus `j_X,Y` is injective.
<1>7. Properness is possible: for simple `X,Y`, the source algebra is `C`,
while `End(X tensor Y)` has one central summand for every simple fusion output
and matrix multiplicities when outputs repeat.
<1>8. This proves the statement.  QED.

## Proposition CPOP-2: expectations, states, preparation, and Born rule

**Statement.**  Every assembly inclusion in CPOP-1 has a unique trace-
preserving conditional expectation.  D1122 therefore gives normalised states,
positive restriction and preparation, and Born probabilities in `[0,1]`.
Expectations satisfy the tower law along nested assembly inclusions.

**Proof.**
<1>1. Write `B=j_X,Y(A_X tensor A_Y)` and `A=A_(X tensor Y)`.
<1>2. Equip `A` with the Hilbert-space inner product
`<a,b>=tau_A(a^*b)`.
<2>1. Faithfulness from CPOP-1 makes this nondegenerate.
<2>2. Let `E_B:A->B` be the orthogonal projection.
<1>3. `E_B` is unital, completely positive, `B`-bimodular, and
`tau_A`-preserving.
<2>1. It fixes `B`, hence is unital.  Tracial cyclicity shows that the
orthogonal complement of `B` is stable under left and right multiplication by
`B`, proving bimodularity.
<2>2. If `a>=0` but `E_B(a)` had a negative spectral projection `p in B`,
then `tau_A(pE_B(a))=tau_A(pa)=tau_A(pap)>=0`, a contradiction.  Thus `E_B`
is positive.
<2>3. The entrywise map on `M_n(A)` is the same orthogonal projection onto
`M_n(B)` for the matrix-amplified trace.  Repeating <2>2 for every `n` proves
complete positivity.
<2>4. Taking `b=1` in orthogonality proves trace preservation.  Any other
trace-preserving conditional expectation has `<b,a-E(a)>=0` for every
`b in B`, proving uniqueness.
<1>4. If `B subset C subset A` are nested unital subalgebras with the same
faithful trace, orthogonal projections obey
`E_B^A=E_B^C E_C^A`.
<2>1. This is the tower law and gives coherent repeated restriction.
<1>5. For `rho>=0`, `Tr_A(rho)=1`, and `0<=e<=1`, apply the trace to
`0<=rho^(1/2)e rho^(1/2)<=rho` to get
`0<=Tr_A(rho e)<=Tr_A(rho)=1`.
<2>1. Thus D1122 has the ordinary Born interval and exact normalisation.
<1>6. `E_B(rho)>=0` and
`Tr_B(E_B(rho))=Tr_A(rho)=1`; this is the restricted density.
<1>7. If `sigma>=0` in `A_X tensor A_Y` and its product trace is one, then
`j(sigma)>=0` and CPOP-1 gives `Tr_A(j(sigma))=1`.
<2>1. For every `a in A`, bimodularity and trace preservation give

    Tr_A(j(sigma)a)=Tr_B(sigma E_B(a)).
<2>2. Therefore density embedding and precomposition by `E_B` are the same
canonical preparation.
<1>8. All constructions use the categorical trace and finite C*-algebras;
no Hilbert fibre functor on `C` was used.  QED.

## Proposition CPOP-3: a sufficient coherently composable process class

**Statement.**  D1123 forms a monoidal class of channels
at the level of retained Kraus data.  Every Heisenberg shadow is UCP, every
Schrodinger action is CP and categorical-trace preserving, and every retained
context channel restricts to the ordinary local tensor channel.  D1124 has
coherent sequential composition, with the stated condition for parallel
composition.

**Proof.**
<1>1. For a D1123 list, each map `a -> K_i^*aK_i` is CP, hence so is their
sum, and `Phi_K(1_Y)=sum_i K_i^*K_i=1_X`.
<1>2. Cyclicity of the spherical trace gives

    Tr_Y(T_K(rho))
      =sum_i Tr_Y(K_i rho K_i^*)
      =Tr_X(rho sum_i K_i^*K_i)=Tr_X(rho).
<2>1. Thus positive normalised densities remain positive and normalised.
<1>3. For `K:X->Y` and `L:Y->Z`, the list `(L_jK_i)` is normalised because

    sum_(j,i) K_i^*L_j^*L_jK_i=sum_i K_i^*K_i=1_X.
<2>1. Its Schrödinger action is `T_L o T_K` and its Heisenberg shadow is
`Phi_K o Phi_L`.
<1>4. For `K:X->Y` and `L:X'->Y'`, the list `(K_i tensor L_j)` is normalised
by bilinearity and the interchange law.
<2>1. Associativity and unit coherence are inherited from `C`.
<1>5. Stable scalar-unitary mixing leaves every context channel invariant:
unitarity of the coefficient matrix collapses the two Kraus-index sums.
<2>1. It is preserved by composition and tensoring, so the stated quotient is
a congruence.
<1>6. On `j_Y,Z(a tensor b)`, the right-context formula is

    Phi_K^Z(j(a tensor b))=j(Phi_K(a) tensor b).
<2>1. On collective observables outside this proper subalgebra, the same
formula still specifies an action because the actual `K_i tensor 1_Z` were
retained.
<1>7. For D1124 dilations `(E,v):X->Y` and `(F,w):Y->Z`, set

    u=(w tensor 1_E)v:X->Z tensor (F tensor E)

with displayed associators.
<2>1. `u^*u=1_X`, and diagrammatic substitution gives
`Phi_u=Phi_v o Phi_w`.
<1>8. For parallel dilation, the raw tensor has boundary order
`Y,E,Y',E'`.  A unitary braiding `c_(E,Y')`, or named half-braiding, supplies
the interchange to `Y,Y',E,E'`.
<2>1. Without such data there is no canonical interchange in a general
monoidal category, so no stronger parallel-composition claim is made.
<1>9. Jones--Penneys Definition 4.20 and Theorem 4.28 give the analogous
notions of CP natural transformation and Stinespring dilation for C*-algebra
objects internal to a rigid C*-tensor category.
<2>1. Their theorem supports retaining all categorical fibres/context data.
It is not being invoked to identify the net `X -> End_C(X)` with one of their
internal algebra objects.
<1>10. This proves the bounded sufficient-class statement.  QED.

## Proposition CPOP-4: exact Fibonacci failure of isolated-channel quotient

**Statement.**  In the positive-chirality Fibonacci unitary braided fusion
category, equivalence of unitary morphisms by their isolated conjugation
channel is not a tensor congruence.  The failure has exact Born witnesses.

**Proof.**
<1>1. Name the fusion rule `tau tensor tau = 1 direct-sum tau` and choose the
standard real unitary gauge and positive chirality.
<2>1. The positive dimension solves `d_tau^2=1+d_tau`, hence
`d_tau=phi=(1+sqrt(5))/2`.
<2>2. Put `s=phi^(-1/2)`.  The standard gauge and the named chirality give

    F = [[phi^(-1), s], [s, -phi^(-1)]],
    R = diag(r_1,r_tau),
    r_1=exp(-4 pi i/5),       r_tau=exp(3 pi i/5).
<2>3. Exact coefficient field: with `zeta_20=exp(2 pi i/20)`, both phases lie
in `Q(zeta_20)` (`r_1=zeta_20^12`, `r_tau=zeta_20^6`), while the displayed
real gauge lies in the finite algebraic extension
`Q(zeta_20,s)` with `s^2=phi^(-1)`.
<2>4. The nontrivial pentagon equation in the standard trivalent-vertex gauge
gives the first row `(d_tau^(-1),d_tau^(-1/2))`; orthogonality and the standard
determinant choice give the second.  The two `R` eigenvalues are the hexagon
solution for the named chirality; the mirror category complex-conjugates them.
<1>2. These values are exact: `phi^(-2)+phi^(-1)=1`, so `F^*=F` and `F^2=I`;
`R^*R=I` because its entries are roots of unity.
<1>3. The two-anyon observable algebra is
`A_(tau^2)=End(1 direct-sum tau)=C direct-sum C`.
<2>1. The first braid is `R`, diagonal in the two fusion charges.
<2>2. Therefore `Ad_R` is exactly the identity on `A_(tau^2)`.
<1>4. Left-associate three anyons.  Then

    tau^3 = 1 direct-sum 2 tau,
    A_(tau^3)=C direct-sum M_2(C).
<2>1. On the total-charge-`tau` multiplicity block, ordered by intermediate
charge `(1,tau)`, the extended first braid is exactly `R`.
<2>2. Consequently its Schrödinger conjugation sends
`E_12 -> (r_1/r_tau)E_12=zeta_20^6 E_12`, which is nontrivial.
<1>5. Thus `R` and `1_(tau^2)` have the same isolated channel but
`R tensor 1_tau` and `1_(tau^3)` do not.  Isolated-channel equivalence is not
a tensor congruence.
<1>6. The traces in this example are

    Tr_(tau^2)(lambda_1,lambda_tau)=lambda_1+phi lambda_tau,
    Tr_(tau^3)(z,M)=z+phi tr_2(M).
<2>1. The local assembly inclusion is

    j(lambda_1,lambda_tau)
      =(lambda_tau, diag(lambda_1,lambda_tau)).
<2>2. Its trace-preserving expectation is

    E(z,M)=j(M_11, (z+phi M_22)/phi^2).
<2>3. Direct substitution proves trace preservation; uniqueness follows from
CPOP-2.  The off-diagonal collective observables are exactly what the local
algebra omits.
<1>7. Let `P_+=|+><+|`, `|+>=(1,1)/sqrt(2)`, in the total-`tau` block,
take density `rho_+=(0,P_+/phi)`, and effect `e_+=(0,P_+)`.
<2>1. `Tr_(tau^3)(rho_+)=1`, so this is a normalised state.
<2>2. With no braid the Born probability is one.
<2>3. After the extended first braid it is

    |(r_1+r_tau)/2|^2
      =(1+cos(7 pi/5))/2
      =1/2-1/(4 phi)=(5-sqrt(5))/8.
<2>4. This exact number differs from one and operationally separates the two
context extensions.
<1>8. The second braid in the left-associated basis is `B_2=F R F`.
<2>1. Prepare and measure the intermediate-vacuum projector `P_1`, using the
normalised density `(0,P_1/phi)`.
<2>2. The return probability is

    |phi^(-2)r_1+phi^(-1)r_tau|^2
      =phi^(-2)=(3-sqrt(5))/2.
<2>3. This supplies a second witness using only a fusion-channel preparation,
an `F`-move, a braid, and a fusion-channel effect.
<1>9. Bonderson--Shtengel--Slingerland equations (2.19)--(2.29) justify the
quantum-trace weights and partial-trace warning; Ahmadi--Kissinger equations
(39)--(42) display the same exact `phi`, `F`, `R`, and `FRF` gauge.
<1>10. The conclusion is positive guidance: retain the circuit/Kraus/dilation
data, or a natural family of actions in all contexts, before quotienting.
QED.

## Proposition CPOP-5: bounded `q=1` symmetric-group operational net

**Statement.**  D1125 is a finite C*-algebra net over finite injections with
trace-preserving UCP expectations, proper assembly inclusions, normalised
density/effect/Born semantics, and coherently extensible local Kraus processes.
Its two-to-three-point inclusion has an exact `1 -> 1/4` Born witness showing
again that isolated-channel quotient is invalid.

**Proof.**
<1>1. The left regular representation makes `C[G(S)]` a finite-dimensional
C*-algebra with the involution in D1125.
<2>1. `tau_S(a)` is the normalised regular trace, hence is faithful, positive,
tracial, and satisfies `tau_S(1)=1`.
<1>2. Extension by identity along an injection is an injective group map and
hence a unital star-monomorphism `i_f`.
<2>1. Extension is functorial under composition of injections.
<1>3. For a subgroup `H<=G`, coefficient projection `C[G]->C[H]` is the
orthogonal projection in the `tau_G` inner product.
<2>1. CPOP-2 makes it the unique `tau_G`-preserving conditional expectation;
in particular it is UCP.
<2>2. Subgroup chains give the tower law by deleting coefficients in stages.
<1>4. Disjoint union embeds `G(S)xG(T)` as block permutations.
<2>1. Thus `mu_S,T` is an injective unital star-homomorphism and
`tau_(S disjoint T)(mu(a tensor b))=tau_S(a)tau_T(b)`.
<2>2. It is generally proper: for two singleton sets the source is `C`, while
the target is `C[S_2]=C^2`.
<1>5. For a local Kraus list `K` on `S` and an injection `f:S->T`, define

    Phi_(K,f)(a)=sum_i i_f(K_i)^* a i_f(K_i),
    T_(K,f)(rho)=sum_i i_f(K_i) rho i_f(K_i)^*.
<2>1. These maps are respectively UCP and CP trace preserving by the same
calculation as CPOP-3.
<2>2. Functoriality of `i_f` makes repeated ambient extension unambiguous.
<1>6. Sequential lists are `(L_jK_i)`; on disjoint supports parallel lists
are `mu(K_i tensor L_j)`.
<2>1. The two embedded local algebras commute, so parallel normalisation,
interchange, associativity, and symmetry follow from group multiplication.
<2>2. Stable scalar-unitary Kraus mixing remains a congruence.  Equality only
of the isolated CP shadows is deliberately not imposed.
<1>7. Now take `S={1,2}`, `T={1,2,3}`, `s=(12)`, and the standard inclusion.
<2>1. `A(S)=C[S_2]` is commutative, so `Ad_s=id` on the isolated algebra.
<2>2. In `A(T)`, `Ad_s((23))=(13)`, so the retained ambient action is not the
identity.
<1>8. Let `pi_std` be the two-dimensional standard representation of `S_3`
and let

    e_std=(1/3)(2*1-(123)-(132)),
    q_23=e_std(1+(23))/2,       q_13=e_std(1+(13))/2.
<2>1. `e_std` is the central projection onto the standard block; each `q` is
a rank-one projection there and is zero on the other two simple blocks.
<2>2. The coefficient trace decomposes as

    tau_T=(1/6)(tr_triv+tr_sign+2 tr_std),

so `tau_T(q_23)=1/3`.  Therefore `rho=3q_23` is a normalised full-algebra
density and `e=q_23` is an effect.
<1>9. Initially `tau_T(rho e)=3tau_T(q_23)=1`.
<2>1. Conjugation by `s` sends `q_23` to `q_13`.
<2>2. For two distinct transpositions `u,v`, the standard character values
are `chi_std(1)=2`, `chi_std(u)=chi_std(v)=0`, and
`chi_std(uv)=-1`; hence

    tr_std(((1+u)/2)((1+v)/2))=(2+0+0-1)/4=1/4.
<2>3. It follows exactly that

    tau_T(3 q_13 q_23)=1/4.
<2>4. The conditioned density on the standard `M_2` block is simply the
ordinary rank-one density `Q_23`; the factor `3` is required only when it is
written as a density for the full coefficient-trace algebra.
<1>10. This gives a genuine finite quantum net: noncommutative observable
algebras, normalised densities and positive functionals, UCP/trace-preserving
dynamics, effects and Born probabilities, and coherent assembly/process
extension.
<2>1. It does not assert that every CP map is localisable, that the net is the
unique `F_1` theory, or that a `q>1` Hecke family has already specialised to it.
<1>11. This proves the bounded statement.  QED.

## The finite-`p` to `q=1` acceptance test

The preceding propositions isolate a testable interface for the separate
arithmetic-family work.
<1>1. For every prime `p`, provide a finite arithmetic process category or net
`Q_p` with marked generators and assembly maps.
<1>2. Provide an intrinsic invariant `mem(Q_p)=p`, or prove pairwise
inequivalence of the marked packages.  Merely realising all fibres as abstract
matrix algebras does not remember `p`.
<1>3. Realise each package by finite C*-algebras with faithful normalised
traces, conditional expectations, positive normalised states, effects, Born
pairing, and a context-complete sufficient class of CP processes.
<1>4. State the specialization mechanism to a named `Q_1`; no limit over the
discrete set of primes is inferred.  Specialize composition/dilation data
before taking isolated CP shadows.
<1>5. At `q=1`, D1125 passes the operational part of this test.  A separate
Hecke lane must establish any arithmetic `q>1` family and its specialization;
the present shard neither repeats nor assumes that theorem.
<1>6. If a candidate contains a Fibonacci object, CPOP-4 is a mandatory
stress test.  Fibonacci is an example of collective fusion degrees, not an
axiom or proposed identification of the `F_1` endpoint.

The sharp boundary is therefore: arbitrary isolated UCP maps compose in time,
but do not canonically extend across proper assembly inclusions.  Unitary
circuits, retained category-morphism Kraus lists, suitable charge dilations,
and natural CP families do carry enough information for coherent context.
