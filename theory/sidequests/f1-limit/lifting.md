# Local endpoint lifting and contextual faithfulness near one

Status: PROVED within the stated hypotheses. Admission and repaired scope
are recorded in `../../verdicts/f1-limit-adjudication.md`.

## Lemma LLIM-1 (raw corner sections and continuous normalization)

**ASSUME** the continuous corner categories of CLIM-2, and fix `q_0>0`.

**PROVE** every finite collection of fibre elements has simultaneous local
continuous corner lifts, and the normalization operations used below are
continuous on a sufficiently small neighborhood.

<1>1. Every fibre corner morphism has a raw continuous lift.

<2>1. Let `a_0 in e_beta(q_0)H_n(q_0)e_alpha(q_0)`.

<2>2. Expand it in the normalized basis as
`a_0=sum_w c_w b_w(q_0)`.

<2>3. On any compact positive interval `I` containing `q_0`, put

    a_raw(q)=e_beta(q)(sum_w c_w b_w(q))e_alpha(q).

<2>4. CLIM-1--2 show this is a continuous corner section.

<2>5. At `q=q_0`, the two corner identities already fix `a_0`, so
`a_raw(q_0)=a_0`.

<1>2. A finite collection can be lifted on one common interval.

<2>1. Apply <1>1 to each element.

<2>2. Intersect the finitely many positive neighborhoods on which any later
open conditions are satisfied.

<2>3. The intersection contains a compact interval about `q_0`.

<1>3. Invertibility is an open condition for continuous corner sections.

<2>1. Let `S(q)` be self-adjoint in `A_alpha(q)` and suppose
`S(q_0)=e_alpha(q_0)`.

<2>2. Continuity in the fixed regular matrix representation gives, after
shrinking the interval,

    ||S(q)-e_alpha(q)|| < 1/2.

<2>3. Inside the unital corner with unit `e_alpha(q)`, write
`S=e_alpha-X`, where `||X||<1/2`.

<2>4. The scalar binomial series

    (1-z)^(-1/2)=sum_(r>=0) c_r z^r

has radius of convergence one and converges uniformly for `|z|<=1/2`.

<2>5. Therefore `S(q)^(-1/2)=sum_r c_r X(q)^r` converges uniformly in the
continuous section algebra.

<2>6. It is a continuous self-adjoint corner section and satisfies the usual
inverse-square-root identities by multiplying the uniformly convergent
series, first for scalar polynomials and then by uniform limits.

<1>4. Strict positivity of a continuous scalar at `q_0` also persists after
shrinking the interval.

<2>1. This is the epsilon definition of continuity applied with half its
positive value.

<2>2. In particular, a nonzero positive raw density has positive trace on a
small common interval because every fibre trace is faithful.

<1>5. All statements also hold for tensor-register algebras.

<2>1. Evaluation from the `C(I)`-balanced tensor product of the section
algebras onto the tensor product fibre is surjective on elementary tensors
and hence on their finite linear span.

<2>2. Finite-dimensional tensor products are exactly that span.

<2>3. The fixed matrix representations make multiplication, star, norm, and
the product trace continuous.

<1>6. Steps <1>1--<1>5 prove LLIM-1. **QED**

## Theorem LLIM-2 (states, effects, POVMs, and instruments lift locally)

**ASSUME** a fibre `q_0>0`, and use the controlled generator class of
OPLIM-2.

**PROVE** every endpoint state, effect, POVM, and normalized corner-Kraus
instrument has a continuous local lift of the same operational type.

<1>7. Let `h_0>=0` be a normalized density on a fibre register `X`.

<2>1. In the finite C*-algebra take its positive square root `c_0=h_0^(1/2)`.

<2>2. Use LLIM-1 to choose a raw section `c(q)` with `c(q_0)=c_0`.

<2>3. Put `H(q)=c(q)^*c(q)` and

    z(q)=tau_X,q(H(q)).

<2>4. Then `H(q)>=0`, `z` is continuous, and `z(q_0)=1`.

<2>5. After shrinking, `z(q)>0`; set `h(q)=H(q)/z(q)`.

<2>6. This is a continuous positive density, has trace one in every fibre,
and evaluates to `h_0`.

<1>8. Let `(e_(o,0))_(o in O)` be any endpoint POVM on `X`.

<2>1. Lift each positive square root `e_(o,0)^(1/2)` to a raw section
`c_o(q)` and put `A_o(q)=c_o(q)^*c_o(q)`.

<2>2. The positive section `S(q)=sum_o A_o(q)` satisfies
`S(q_0)=1_X(q_0)`.

<2>3. By LLIM-1 it has a continuous inverse square root locally.

<2>4. Define

    e_o(q)=S(q)^(-1/2) A_o(q) S(q)^(-1/2).

<2>5. Every `e_o(q)` is positive and their sum is the unit.

<2>6. At `q_0`, `S=1`, so the lifted POVM evaluates to the given one.

<2>7. Applying this to `(e_0,1-e_0)` lifts every individual effect while
preserving `0<=e(q)<=1`.

<1>9. Let `K_(o,i,0) in e_beta(q_0)H_n(q_0)e_alpha(q_0)` be a normalized
endpoint corner-Kraus instrument.

<2>1. Choose simultaneous raw corner lifts `Khat_(o,i)(q)` by LLIM-1.

<2>2. Put

    S(q)=sum_(o,i) Khat_(o,i)(q)^*Khat_(o,i)(q).

<2>3. This is a positive section of `A_alpha(q)` and
`S(q_0)=e_alpha(q_0)`.

<2>4. On a smaller interval, LLIM-1 supplies `S(q)^(-1/2)` in that corner.

<2>5. Define the normalized lift

    Ktilde_(o,i)(q)=Khat_(o,i)(q)S(q)^(-1/2).

<2>6. It has the same corner type and satisfies

    sum_(o,i) Ktilde_(o,i)^*Ktilde_(o,i)
      =S^(-1/2)SS^(-1/2)=e_alpha.

<2>7. Since `S(q_0)^(-1/2)=e_alpha(q_0)`, it evaluates to the original
instrument.

<1>10. The construction preserves the coefficient-Gram process equality.

<2>1. Choose one endpoint representative, lift and normalize it as in <1>9.

<2>2. Any other endpoint representative obtained by a fixed scalar unitary
has the corresponding unitary mixture of the lifted list and hence the same
pointwise coefficient Gram.

<2>3. More generally, D1210 declares two continuous labels equal when their
coefficient Grams agree pointwise, and two germ labels equal when this holds
on a smaller common interval.  This definition does not require a continuous
choice of scalar mixing unitaries.

<2>4. Thus one normalized lift represents the endpoint process label.  The
claim is local existence of a representative, not a continuous-unitary lift
of every possible equivalent endpoint list.

<1>11. Retained context and collective parallel lifts require no further
normalization.

<2>1. Apply D1209's Hecke inclusion pointwise to the lifted list.

<2>2. OPLIM-2 shows its normalization, composition, and ordered parallel
identities are exact on the entire neighborhood.

<2>3. Canonical refinement isometries `e_beta` for `alpha<=beta`, as in
D1141, are themselves global continuous sections.

<1>12. Preparation and discard lift across arbitrary ranks.

<2>1. Preparations use the lifted density in <1>7.

<2>2. Discard is the parameter-independent unit map in each fibre.

<2>3. Contextual preparation and discard are then the circuits of OPLIM-3,
whose assembly and split boxes exist on the whole positive interval.

<1>13. Steps <1>7--<1>12 prove LLIM-2. **QED**

## Theorem LLIM-3 (locally uniform contextual Gram faithfulness)

**ASSUME** a fixed `n>=1`, the complete composition `x^n=(1,...,1)`, and
the normalized basis `b_h(q)`, `h in S_n`, of CLIM-1.

**PROVE** on some interval about one, equality of one retained
`(2n-1)`-constituent context action is equivalent to Kraus-Gram equality and
fibrewise stable scalar-unitary equality.

<1>14. Choose a set `S` of size `n` inside a set `T` of size `2n-1`.

<2>1. Fix `s_0 in S` and let `d in S_T` fix `s_0` while swapping the other
`n-1` points of `S` with the `n-1` points of `T\S` in named pairs.

<2>2. Then `d=d^(-1)` and
`S_n intersect dS_nd^(-1)={1}` by F1-OP-KCF.

<2>3. Hence the `(n!)^2` permutations

    h^(-1) d k,        h,k in S_n,

are pairwise distinct.

<2>4. Use the left contiguous-block inclusion and write explicitly

    Btilde_h(q)=iota_(n,n-1)(B_h(q) tensor 1)
      in H_(2n-1)(q).

At `q=1` this is the permutation of `S` extended by the identity on `T\S`.

<1>15. For a local list `K_i(q)=sum_h a_i(h,q)b_h(q)`, define its normalized
basis Gram

    J_K(q)(k,h)=sum_i a_i(k,q) conjugate(a_i(h,q)).

<2>1. For the retained inclusion into rank `2n-1`, expansion gives

    Phi_(K,q)(B_d(q))
      =sum_(h,k) J_K(q)(k,h)
         Btilde_h(q)^* B_d(q) Btilde_k(q).

<2>2. This formula is linear in the Gram matrix and uses the retained Kraus
coefficients before taking the CP shadow.

<1>16. Let `C_n(q)` be the matrix of the linear map

    J |->sum_(h,k)J(k,h)Btilde_h(q)^*B_d(q)Btilde_k(q)

from `M_(S_n)(C)` to `H_(2n-1)(q)`, in normalized standard bases.

<2>1. Every entry of `C_n(q)` is continuous by CLIM-1.

<2>2. At `q=1`, its column `(k,h)` is the coordinate vector of the group
element `h^(-1)dk`.

<2>3. By <1>14, the square submatrix using exactly those distinct output
rows is a permutation matrix.

<2>4. Its determinant is therefore `+1` or `-1` at one.

<2>5. Determinants are polynomials in matrix entries, so this selected minor
remains nonzero on some interval `I_n` about one.

<2>6. Consequently `C_n(q)` is injective for every `q in I_n`.

<1>17. On `I_n`, equality of the two retained context channels on the single
observable `B_d(q)` forces `J_K(q)=J_L(q)`.

<2>1. Subtract the two expansions in <1>15.

<2>2. Injectivity in <1>16 makes the Gram difference zero.

<1>18. Conversely, Gram equality makes every retained context channel equal.

<2>1. For any ambient rank, any ambient basis element `B_g(q)`, and any
inclusion of the local contiguous block, expansion of
`sum_i K_i^*B_gK_i` is linear in the same Gram coefficients.

<2>2. Equal Grams therefore give equal outputs on a basis and hence on the
whole ambient algebra.

<1>19. At each fixed fibre, Gram equality is equivalent to stable
scalar-unitary mixing.

<2>1. Regard the coefficient columns `(a_i(h))_i` as vectors indexed by
`h in S_n`.

<2>2. Equal Grams say that the correspondence between the two finite sets of
coefficient columns preserves all inner products.

<2>3. It extends to an isometry of their spans; after zero padding, extend
that isometry orthogonally to a unitary of the Kraus-index space.

<2>4. The resulting unitary maps one list coefficientwise to the other at
that fixed `q`.  No continuity of this unitary as `q` varies follows or is
needed.

<2>5. The reverse implication is the unitary cancellation identity.

<1>20. Distinct Grams have an operational Born separator throughout `I_n`.

<2>1. `B_d(q)` is self-adjoint because `d=d^(-1)`.

<2>2. Shrink to a compact interval and choose
`M>=sup_(q in I_n)||B_d(q)||`.

<2>3. Then `a_q=(1+B_d(q)/M)/2` is an effect.

<2>4. The channels are unital, so a difference on `B_d(q)` is equivalent to
a difference on `a_q`.

<2>5. A nonzero self-adjoint output difference in a finite C*-algebra has a
nonzero spectral subspace; a unit vector in that subspace defines a positive
state separating the two Born probabilities.

<1>21. The interval `I_n` depends on `n` and on the selected determinant
minor.

<2>1. This proves only the locally uniform positive-`q` statement needed for
endpoint germs.

<2>2. It neither proves the proposed sharp `2n-1` bound for every `q>0` nor
promotes the existing F1-OP-KCF-Q sketch.

<1>22. Steps <1>14--<1>21 prove LLIM-3. **QED**

## Theorem LLIM-4 (local lifting of every finite endpoint circuit)

**ASSUME** a morphism of the controlled endpoint category `Op_1` represented
by a finite typed circuit.

**PROVE** it lies in the image of endpoint evaluation
`Ev_1:Op_1^germ->Op_1`.

<1>23. The circuit contains finitely many generator labels.

<2>1. Lift every state label by LLIM-2 <1>7.

<2>2. Lift every POVM/effect label by LLIM-2 <1>8.

<2>3. Lift every normalized Kraus-instrument label by LLIM-2 <1>9.

<2>4. Use the global canonical sections for assembly, split, refinement,
discard, and retained context extension.

<1>24. Intersect the finitely many lift neighborhoods.

<2>1. The intersection contains an endpoint interval because the circuit is
finite.

<2>2. If the same endpoint label occurs repeatedly in the circuit, choose one
lift and reuse it at every occurrence.

<2>3. On that interval the same typed planar graph, with the lifted labels,
is a morphism of `Op_I^cts`.

<2>4. Its endpoint evaluation is exactly the original representative.

<1>25. Passing to its germ proves surjectivity on represented Hom sets.

<2>1. Different choices of raw lifts can give different germs.

<2>2. Therefore the result is local existence, not a canonical section of
the evaluation functor and not a global lifting theorem.

<2>3. The bounded process class is essential: no assertion is made that an
arbitrary CP map without retained corner-Kraus data lifts in this manner.

<2>4. Nor is an arbitrary finite commuting diagram lifted with all of its
extra endpoint equations preserved.  Symmetry enhancement at `q=1` can add
relations, such as exchange relations, which have no positive-neighborhood
lift.

<1>26. For a finite family of circuits whose local Kraus equality must be
checked operationally, take the intersection also with the finitely many
intervals `I_n` from LLIM-3.

<2>1. On that neighborhood, pointwise coefficient-Gram equality, equivalently
fibrewise stable-unitary mixing, is equivalent to equality in the displayed
finite collective contexts.

<2>2. This supplies honest contextual equality locally without assuming the
unproved all-positive-parameter Hecke context theorem.

<1>27. Steps <1>23--<1>26 prove LLIM-4. **QED**
