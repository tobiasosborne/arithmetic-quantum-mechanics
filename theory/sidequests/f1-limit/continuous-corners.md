# Continuous positive Hecke algebras and their corner germs

Status: PROVED within the stated hypotheses. Admission and repaired scope
are recorded in `../../verdicts/f1-limit-adjudication.md`.

This shard constructs the actual continuous family used by the operational
limit.  It does not take a limit through prime powers.  A positive real
parameter is evaluated at an arithmetic value `q=Q` or at the endpoint
`q=1`.

## Theorem CLIM-1 (continuous regular Hecke C*-algebras)

**ASSUME** `I` is a compact interval contained in `(0,infinity)`, and use the
positive type-A Hecke algebra and coefficient trace of D1101.

**PROVE** D1201--D1202 give a unital C*-subalgebra
`H_n^cts(I) <= C(I,M_(n!)(C))`, every fibre evaluation is a surjective
star-homomorphism onto the faithful regular copy of `H_n(q)`, and the
coefficient traces form a continuous faithful tracial field.

<1>1. Fix `n>=0`, write `ell` for Coxeter length, and put

    b_w(q)=q^(-ell(w)/2) T_w(q),       w in S_n.

<2>1. F1-HCK-POS gives

    tau_(n,q)(b_u(q)^* b_v(q))=delta_(u,v).

<2>2. Thus the maps `b_w(q) |-> delta_w` identify every GNS Hilbert space
with the one fixed Hilbert space `K_n=ell^2(S_n)`.

<2>3. Let `B_w(q)` be left multiplication by `b_w(q)` after this
identification.

<1>2. The matrices `B_w(q)` depend continuously on `q`.

<2>1. For a simple reflection `s=s_i`, the standard multiplication rule in
F1-HCK-POS gives, when `ell(sw)=ell(w)+1`,

    T_s T_w=T_(sw),
    T_s T_(sw)=q T_w+(q-1)T_(sw).

<2>2. In the ordered orthonormal pair `(b_w,b_(sw))`, left multiplication by
`T_s` therefore has matrix

    [[0,sqrt(q)],[sqrt(q),q-1]].

<2>3. This matrix is self-adjoint and its entries are continuous on
`(0,infinity)`.

<2>4. A reduced product expresses every `B_w(q)` as a finite product of a
scalar power of `q^(-1/2)` and such generator matrices.

<2>5. Hence every matrix entry of every `B_w(q)` is continuous.

<1>3. Define

    H_n^cts(I)
      ={ q |-> sum_(w in S_n) f_w(q) B_w(q) : f_w in C(I) }.

<2>1. The Hecke multiplication rule and the normalization in <1>1 express
`B_u(q)B_v(q)` as a finite linear combination of the `B_w(q)` with
continuous coefficients.

<2>2. Inversion preserves length, so `B_w(q)^*=B_(w^(-1))(q)`.

<2>3. The constant section `B_e` is the identity.

<2>4. Therefore the displayed space is a unital star-subalgebra of
`C(I,M_(n!)(C))`.

<1>4. This star-subalgebra is norm closed.

<2>1. For `x(q)=sum_w f_w(q)B_w(q)`, apply `x(q)` to `delta_e`.

<2>2. Since `B_w(q)delta_e=delta_w`, its coordinate at `delta_w` is exactly
`f_w(q)`.

<2>3. If `x_r` converges uniformly in operator norm, every coefficient
function `f_(r,w)` converges uniformly to the corresponding coordinate of
`x(q)delta_e`.

<2>4. The limit is consequently `sum_w f_w B_w` with every `f_w` continuous.

<2>5. Thus `H_n^cts(I)` is closed and is a C*-algebra with the inherited
supremum norm.

<1>5. Evaluation at `q_0 in I` is a surjective star-homomorphism

    ev_(q_0):H_n^cts(I) -> H_n(q_0).

<2>1. Pointwise evaluation preserves multiplication, star, and the unit.

<2>2. A fibre element has a unique expansion `sum_w c_w b_w(q_0)`.

<2>3. Choosing the constant coefficient functions `f_w(q)=c_w` gives a
section evaluating to it.

<2>4. The regular representation is faithful by F1-HCK-POS, so this is the
claimed fibre algebra rather than a quotient.

<1>6. Define the continuous coefficient trace by

    tau_n^cts(x)(q)=tau_(n,q)(x(q)).

<2>1. In the expansion of <1>3 this is `f_e(q)`, hence belongs to `C(I)`.

<2>2. Each fibre functional is normalized, tracial, positive, and faithful
by F1-HCK-POS.

<2>3. If the positive section `x^*x` has trace function identically zero,
then every fibre `x(q)` is zero by fibre faithfulness.

<2>4. Hence `x=0`, so the `C(I)`-valued trace is faithful in the required
sense.

<1>7. Positivity holds at every rank and every `q in I`.

<2>1. If `x=sum_w c_wT_w(q)`, F1-HCK-POS gives directly

    tau_(n,q)(x^*x)=sum_w |c_w|^2 q^ell(w).

<2>2. Every summand is nonnegative and all weights are strictly positive.

<2>3. The form is therefore positive definite for every `n` and every
positive real parameter, including `q=1` and every prime power `Q`.

<1>8. Steps <1>1--<1>7 prove CLIM-1. **QED**

## Theorem CLIM-2 (continuous parabolic corner category)

**ASSUME** CLIM-1, D1102, and the parabolic idempotents of D1141.

**PROVE** D1203 defines an ordered monoidal C*-category
`Gamma_I^cts`; its evaluations are full ordered star-functors to
`Gamma_q`; and its normalized corner traces, inclusions, and expectations
are continuous and coherent.

<1>9. For a composition `alpha` of `n`, the section

    e_alpha(q)=P_alpha(q)^(-1) sum_(w in W_alpha) T_w(q)

belongs to `H_n^cts(I)`.

<2>1. In the normalized basis its coefficient at `b_w(q)` is
`q^(ell(w)/2)/P_alpha(q)` for `w in W_alpha`, and zero otherwise.

<2>2. The polynomial `P_alpha(q)=sum_(w in W_alpha)q^ell(w)` is strictly
positive on `I`.

<2>3. All coefficients in <2>1 are therefore continuous.

<2>4. Put `x_alpha=sum_(w in W_alpha)T_w`.  For a simple reflection `s` in
`W_alpha`, pair each `w` with `sw`, ordered so the second has greater length.
The two Hecke multiplication cases give
`T_s(T_w+T_(sw))=q(T_w+T_(sw))`.

<2>5. Summing pairs gives `T_sx_alpha=qx_alpha`; reversal and star give the
same equation on the right.

<2>6. Hence `T_wx_alpha=q^ell(w)x_alpha` for `w in W_alpha`, so
`x_alpha^2=P_alpha(q)x_alpha`.  Inversion preserves the parabolic and length,
so `x_alpha^*=x_alpha`.

<2>7. Therefore `e_alpha^*=e_alpha=e_alpha^2` in every fibre.

<2>8. Pointwise equality of continuous sections gives the same projection
identities in `H_n^cts(I)`.

<2>9. If `alpha` refines `beta`, then `W_alpha<=W_beta`; the preceding
eigenvector calculation gives
`e_alpha e_beta=e_beta=e_beta e_alpha`.

<1>10. Define objects to be compositions, and define

    Hom_(Gamma_I^cts)(alpha,beta)
      = e_beta H_n^cts(I)e_alpha

when `|alpha|=|beta|=n`, and the zero Banach space otherwise.

<2>1. If `x:alpha->beta` and `y:beta->gamma`, pointwise multiplication gives
`yx=e_gamma(yx)e_alpha`.

<2>2. The identity of `alpha` is `e_alpha`.

<2>3. Star maps `e_beta x e_alpha` to `e_alpha x^*e_beta` and reverses
composition.

<2>4. Every Hom space is a closed corner of the C*-algebra in CLIM-1.

<2>5. The C*-identity and positivity of `x^*x` follow in the containing
C*-algebra, so this is a C*-category.

<1>11. Ordered concatenation defines its monoidal product.

<2>1. On section algebras the source is the `C(I)`-balanced tensor product

    H_m^cts(I) tensor_(C(I)) H_n^cts(I),

where `f x tensor y=x tensor f y` for `f in C(I)`.  Equivalently, it is the
C*-algebra of continuous sections of the pointwise fibre tensor products.

<2>2. This balancing is necessary: the ordinary spatial tensor over `C`
contains `f tensor 1-1 tensor f` for nonconstant `f`, and diagonal fibrewise
assembly kills that nonzero element.

<2>3. Coxeter length is additive on contiguous block permutations, hence

    iota_(m,n)(b_u(q) tensor b_v(q))=b_(u times v)(q).

<2>4. The balanced domain is a free finite-rank `C(I)`-module with basis
`B_u tensor B_v`.  Their images are the distinct normalized block-basis
sections `B_(u times v)`, so coefficient recovery at `delta_e` proves
injectivity.  D1102 therefore gives a continuous unital star-monomorphism
of the balanced section algebras.

<2>5. D1141 gives

    iota_(m,n)(e_alpha tensor e_beta)=e_(alpha concat beta).

<2>6. Therefore `iota` sends typed corner morphisms to typed corner
morphisms and obeys interchange.

<2>7. F1-HCK-TOWER proves the two three-block maps agree on every standard
basis element, hence their continuous versions agree pointwise.

<2>8. The empty composition is the unit.  No block exchange has been added.

<1>12. The normalized corner trace is

    tau_alpha,q(a)=P_alpha(q) tau_(n,q)(a).

<2>1. D1141 gives `tau_(n,q)(e_alpha)=P_alpha(q)^(-1)`, so
`tau_alpha,q(e_alpha)=1`.

<2>2. Faithfulness and traciality are inherited from the ambient coefficient
trace.

<2>3. If `a` is a continuous corner section, its normalized trace is a
continuous scalar function by CLIM-1 and continuity of `P_alpha`.

<2>4. Since `P_(alpha concat beta)=P_alpha P_beta`, the normalized trace of
an assembled elementary tensor is the product trace.

<1>13. The parabolic expectation restricts to the corners.

<2>1. Write `j_(alpha,beta)` for the restriction of `iota_(m,n)` from
`A_alpha tensor A_beta` to `A_(alpha concat beta)`.

<2>2. Its image identity is `e_(alpha concat beta)` by <1>11.

<2>3. The coefficient expectation `E_(m,n)` is bimodular over the parabolic
subalgebra by F1-HCK-TOWER.

<2>4. For `a in A_(alpha concat beta)`, bimodularity gives

    E_(m,n)(a)
      =(e_alpha tensor e_beta) E_(m,n)(a)(e_alpha tensor e_beta).

<2>5. Hence it lands in `A_alpha tensor A_beta`; call this restriction
`E_(alpha,beta)`.

<2>6. It is UCP, preserves the product normalized trace, and satisfies

    E_(alpha,beta) j_(alpha,beta)=id.

<2>7. The reverse composite `jE` is the conditional expectation onto the
proper product subalgebra and is generally not the identity.

<2>8. Three-block coherence is the restriction of F1-HCK-TOWER's inclusion
and expectation tower identities.

<1>14. Fibre evaluation defines a full ordered star-functor

    ev_q:Gamma_I^cts -> Gamma_q.

<2>1. It preserves identities, composition, star, and concatenation because
all are defined pointwise.

<2>2. To lift `x in e_beta(q)H_n(q)e_alpha(q)`, choose a constant-coefficient
ambient section `a` evaluating to `x`, using CLIM-1.

<2>3. The section `e_beta a e_alpha` evaluates to `x` and has the required
type.

<2>4. Thus evaluation is surjective on every Hom space, which is fullness.

<1>15. At a prime power `Q`, F1-HCK-FLAG realizes the evaluated complete-flag
object and D1141 realizes every parabolic corner on partial flags.

<2>1. This is an evaluation at the real number `Q`, followed by the
finite-field representation.

<2>2. It is not a limit of primes and does not change the chosen Lagrangian
or supply missing Weyl observables.

<1>16. Steps <1>9--<1>15 prove CLIM-2. **QED**

## Theorem CLIM-3 (the local germ and endpoint evaluation)

**ASSUME** `I_epsilon=[1-epsilon,1+epsilon]` with `0<epsilon<1`.

**PROVE** D1204 defines an ordered monoidal star-category of germs at one,
with a full endpoint evaluation to `Gamma_1` and local positive
representatives.

<1>17. A morphism germ is represented by `x in Gamma_(I_epsilon)^cts` for
some `epsilon`, with two representatives equal when their restrictions agree
on a smaller such interval.

<2>1. Equality on a smaller interval is an equivalence relation because a
finite intersection of endpoint neighborhoods contains another endpoint
neighborhood.

<2>2. Composition, star, addition, and ordered tensor commute with
restriction.

<2>3. They therefore descend to germ classes; identities are the germs of
the sections `e_alpha`.

<1>18. Endpoint evaluation is well defined and full.

<2>1. Equal germs have representatives equal at one, so evaluation does not
depend on the representative.

<2>2. CLIM-2 lifts every endpoint corner morphism on every chosen interval;
its germ is a preimage.

<2>3. Pointwise definitions make evaluation an ordered star-functor.

<1>19. Every representative interval is a genuine C*-category with faithful
positive normalized corner traces.

<2>1. Thus every germ can be evaluated on some whole positive neighborhood,
and every such fibre has honest finite C*-operational order.

<2>2. The germ category itself is not called a C*-category: a nonzero germ
may vanish at one, so endpoint norm would only be a seminorm.

<2>3. "Positive germ" means a germ admitting a positive section
representative on one neighborhood, a condition preserved by further
restriction and by evaluation.

<1>20. At `q=1`, D1101 gives `H_n(1)=C[S_n]`; D1141 makes every parabolic
idempotent a subgroup average.

<2>1. Hence the distinguished complete-flag powers have endomorphism
algebras `C[S_n]`, while the other objects are the specified permutation
module retracts.

<2>2. This is the actual endpoint category reached by evaluation.

<1>21. Steps <1>17--<1>20 prove CLIM-3. **QED**

## Theorem CLIM-4 (arithmetic partial-flag corner realization)

**ASSUME** `Q` is a prime power, `L=F_Q^n`, D1104, and the maps `J_alpha`
of D1141.

**PROVE** every evaluated corner is the full `GL(L)` intertwiner space on
partial flags, and its normalized corner trace is the normalized physical
operator trace.

<1>22. Every partial flag of type `alpha` has exactly `P_alpha(Q)` complete
refinements.

<2>1. Refining one successive quotient of dimension `alpha_i` amounts to
choosing a complete flag in that quotient.

<2>2. F1-HCK-FLAG's Bruhat cells index those flags by `S_(alpha_i)`, with
cell sizes `Q^ell(w)`.

<2>3. Independent choices in the successive quotients multiply, giving

    product_i sum_(w in S_(alpha_i))Q^ell(w)=P_alpha(Q).

<1>23. The normalized fibre-sum map

    J_alpha:C[Fl_alpha(L)]->C[Fl(L)]

is an isometric `GL(L)` intertwiner.

<2>1. Distinct partial flags have disjoint refinement fibres.

<2>2. Each column of `J_alpha` has `P_alpha(Q)` entries of modulus
`P_alpha(Q)^(-1/2)`, so the columns are orthonormal.

<2>3. Forgetting flag steps commutes with `GL(L)`, proving equivariance.

<1>24. Under F1-HCK-FLAG, the projection `J_alpha J_alpha^*` is
`e_alpha(Q)`.

<2>1. Its matrix entry is `P_alpha(Q)^(-1)` exactly when two complete flags
have the same `alpha`-partial flag, and zero otherwise.

<2>2. Such a pair has relative position in `W_alpha`; hence the adjacency
kernel sum is `x_alpha=sum_(w in W_alpha)T_w`.

<2>3. Division by `P_alpha(Q)` is precisely D1141's `e_alpha(Q)`.

<1>25. The map

    F |->J_beta F J_alpha^*

is a star-compatible linear bijection

    Hom_(GL(L))(C[Fl_alpha(L)],C[Fl_beta(L)])
      -> e_beta H_n(Q)e_alpha.

<2>1. Equivariance and F1-HCK-FLAG put the displayed extension in the
complete-flag commutant, and <1>24 puts it in the required corner.

<2>2. Conversely a corner element `x` restricts as `J_beta^*xJ_alpha`.

<2>3. The two constructions are inverse because the relevant `JJ^*` are
the corner identities acting on `x`.

<2>4. Inserting `J_beta^*J_beta=1` shows compatibility with composition;
taking adjoints shows star compatibility.

<1>26. The normalized traces agree.

<2>1. For `x in e_alpha H_n(Q)e_alpha`, ordinary trace of `x` on the full
flag space equals ordinary trace of `J_alpha^*xJ_alpha` on the partial-flag
space because `x` vanishes off `ran(J_alpha)`.

<2>2. The full flag count is
`|Fl(L)|=P_alpha(Q)|Fl_alpha(L)|` by <1>22.

<2>3. F1-HCK-FLAG identifies normalized full operator trace with `tau_n`.

<2>4. Therefore normalized partial-flag operator trace is
`P_alpha(Q)tau_n=tau_alpha,Q`.

<1>27. Concatenation and refinement maps are the evaluated algebraic maps
already proved in CLIM-2; the realization above preserves their typed
composition and star.

<2>1. It does not turn different total degrees into amplitude morphisms and
does not supply an exchange.

<1>28. Steps <1>22--<1>27 prove CLIM-4. **QED**

## Scope boundary

<1>29. The construction above evaluates continuous sections.  The apartment
map `Omega_Q:H_n(Q)->C[S_n]` of D1144 instead compresses one fixed arithmetic
fibre to a coordinate apartment.

<2>1. Evaluation is multiplicative because it substitutes the parameter in
the defining multiplication law.

<2>2. D1144's `J_ap` is an isometry, so compression by it is UCP.  On
coordinate flags, the adjacency operator `T_s(Q)` has exactly one coordinate
neighbor and compresses to the regular permutation `s`.

<2>3. Consequently

    Omega_Q(T_s(Q)^2)=(Q-1)s+Q1,
    Omega_Q(T_s(Q))^2=1,

so the compression is not multiplicative when `Q>1`.

<2>4. These maps have different domains and different structural claims;
neither is used as a substitute for the other. **QED**
