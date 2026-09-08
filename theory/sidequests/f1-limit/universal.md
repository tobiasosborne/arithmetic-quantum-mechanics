# Universal type-A composition and the multiplicative-sequence category

Status: PROVED within the stated hypotheses. Admission and repaired scope
are recorded in `../../verdicts/f1-limit-adjudication.md`.
Definitions D1221--D1227 are recorded in `../../../definitions.md`.
Existing inputs are D1101, D1102, D1141 and claims `F1-HCK-POS`,
`F1-HCK-TOWER`. The required partial-flag projection and tensor properties
are derived below, without relying on the old F1-OP-FLAGCAT sketch.

Source `DM10` means Davydov--Molev, *A categorical approach to classical
and quantum Schur--Weyl duality*, arXiv:1008.3739v2.  Section 2.1,
printed pp. 6--8, is the source for multiplicative sequences, the opposite
functor category, right modules and formula (2.1).  Section 4.1, printed
pp. 13--15, Proposition 4.4 and Theorem 4.5, is the source for the Hecke
sequence and its free Hecke Yang--Baxter category.  The equivalence with the
finite additive Karoubi category and all variance checks below are local.

## 1. The skeleton and right-module variance

<1>1. **ASSUME** a multiplicative sequence `A_*` as in D1221.

<1>2. **PROVE** `C[A_*]` is a strict complex-linear monoidal category.

<2>1. Its objects, Homs and composition are given in D1221.

<2>2. The tensor of `a in A_m` and `b in A_n` is
`mu_(m,n)(a tensor b)` in `A_(m+n)`.

<2>3. Because `mu_(m,n)` is an algebra homomorphism,

    mu(a' tensor b') mu(a tensor b)
      =mu(a'a tensor b'b),

so tensor satisfies the interchange law with the declared convention
`a' after a=a'a`.

<2>4. The multiplicative-sequence square is precisely strict associativity
of tensor on morphisms; `A_0=C` and unitality give the strict unit.

<2>5. There are no mixed-degree composites to check.  **QED**

<1>3. **PROVE** a linear presheaf on `C[A_*]` is the same thing as a
graded family of right `A_n`-modules.

<2>1. Let `F:C[A_*]^op->Vect` and `m in F([n])`.

<2>2. Put `m dot a=F(a)(m)` for `a in A_n`.

<2>3. Contravariance says `F(ab)=F(b)F(a)` when `ab` is `a after b` in
the original category.

<2>4. Therefore

    (m dot a) dot b=F(b)F(a)m=F(ab)m=m dot (ab),

and the identity acts as the identity.  This is a right action.

<2>5. Conversely, right actions define the value of the contravariant
functor on each endomorphism; zero cross-degree Homs impose no further data.

<2>6. A natural transformation is exactly a family of right-module maps.

<2>7. Hence the presheaf category is `product_n Mod-A_n`; its finite-support
subsystem is D1222's algebraic direct sum.  **QED**

<1>4. **PROVE** the Yoneda embedding sends `[n]` to the right regular
module and is covariant on the source category.

<2>1. The representable is `h_[n]=Hom(-,[n])`.

<2>2. At `[n]` it is `A_n`.  Precomposition by `a` sends `x` to `x a`,
which is the right regular action.

<2>3. If `z:[n]->[n]`, postcomposition defines a natural endomorphism
`h_z(x)=z x`, hence left multiplication `L_z:A_n->A_n`.

<2>4. The assignment is covariant because `L_(zy)=L_z L_y`, and it is
fully faithful since every right-linear map `A_n->A_n` is left
multiplication by its value at `1`.

<2>5. This explains both occurrences of multiplication: the module action
is on the right, while categorical arrows act between representables on the
left.  No opposite algebra is missing.  **QED**

## 2. Day tensor is induction

<1>5. **ASSUME** every `A_j` is finite-dimensional over `C`,
`M in mod_fd-A_m` and `N in mod_fd-A_n`.

<1>6. **PROVE** D1222's balanced tensor is the Day convolution and is
associative with unit `A_0=C`.

<2>1. DM10 equation (2.1), printed p. 7, gives exactly

    (M tensor N) tensor_(A_m tensor A_n) A_(m+n).

<2>2. The balancing relation is

    ((m dot a) tensor (n dot b)) tensor c
       =(m tensor n) tensor mu(a tensor b)c.

<2>3. This relation makes the formula a right `A_(m+n)`-module through
multiplication on the final factor. It is a quotient of the finite-dimensional
vector space `(M tensor N) tensor_C A_(m+n)`, hence remains an object of
`mod_fd-A_(m+n)`. Finite degree support remains finite under tensor.

<2>4. Both bracketings of three factors canonically reduce to

    (L tensor M tensor N)
      tensor_(A_l tensor A_m tensor A_n) A_(l+m+n).

<2>5. The reduction is well-defined because the two structural maps into
`A_(l+m+n)` agree by D1221.

<2>6. These canonical reassociations obey the pentagon because every route
is the same universal balanced map from the fourfold tensor product.

<2>7. The identifications `M star C ~=M~=C star M` obey the triangle for
the same reason.  **QED**

<1>7. **PROVE** representables multiply as expected, and record why this is
not an objectwise tensor of representations.

<2>1. For right regular modules define

    Phi_(m,n):(A_m tensor A_n)
       tensor_(A_m tensor A_n) A_(m+n) -> A_(m+n),
    (a tensor b) tensor c |-> mu(a tensor b)c.

<2>2. Its inverse is `c |-> (1 tensor 1) tensor c`; balancing proves the
two composites are identities.

<2>3. Thus `h_[m] star h_[n] ~=h_[m+n]`, as Day convolution requires.

<2>4. A right `A_m`-module and a right `A_n`-module have actions of
different algebras.  Their vector-space tensor carries only a right
`A_m tensor A_n` action.

<2>5. Extension of scalars along `mu_(m,n)` is the operation that produces
an `A_(m+n)`-module.  Calling `M tensor_C N` alone the tensor product in the
Schur--Weyl category would be ill-typed.  **QED**

## 3. Additive Karoubi completion

<1>8. **PROVE** D1223 is equivalent to the category of finite generated
projective graded right modules.

<2>1. The additive completion of the degree-`n` representable has objects
`A_n^r`; a matrix `z in M_(s,r)(A_n)` acts by left multiplication.

<2>2. Splitting an idempotent `e in M_r(A_n)` replaces `A_n^r` by its
image `eA_n^r`, a finitely generated projective right module.

<2>3. Its typed morphisms to `fA_n^s` are precisely the right-linear maps
`v |-> z v` with `z=fze`, namely `fM_(s,r)(A_n)e`.

<2>4. Every finitely generated projective is a direct summand of some
`A_n^r`, hence is isomorphic to `eA_n^r` for an idempotent `e`.

<2>5. The construction is fully faithful by <2>3 and essentially
surjective by <2>4.  **QED**

<1>9. **PROVE** the equivalence in <1>8 is strong monoidal.

<2>1. For idempotents `e in M_r(A_m)` and `f in M_s(A_n)`, put
`p=mu(e tensor f) in M_(rs)(A_(m+n))`.

<2>2. Define the typed map

    Psi:(eA_m^r tensor fA_n^s)
          tensor_(A_m tensor A_n) A_(m+n) -> pA_(m+n)^(rs)

by

    (ea tensor fb) tensor c |-> mu(ea tensor fb)c,

with matrix indices ordered lexicographically.

<2>3. It is balanced by multiplicativity of `mu` and lands in the range of
`p` because left multiplication by `p` fixes its value.

<2>4. Write `c=(c_(ij))` as a column of length `rs`. Its inverse sends
`pc` to `sum_(i,j)(e delta_i tensor f delta_j) tensor c_(ij)`.
Balancing and `e^2=e,f^2=f` show that replacing `c` by `pc` leaves this
sum unchanged. It therefore depends only on `pc`; direct substitution
proves both composites are identities.

<2>5. For corner morphisms `z=f'ze` and `w=g'wf`, the induced module map
corresponds under `Psi` to left multiplication by `mu(z tensor w)`.

<2>6. Therefore the module equivalence respects tensor, including its
associator and unit constraints.  **QED**

<1>10. **ASSUME** every `A_n` is a finite-dimensional complex C*-algebra
and every structural map `mu` is a star-homomorphism.

<1>11. **PROVE** every finite-dimensional right module lies in D1223.

<2>1. A finite-dimensional C*-algebra is a finite direct sum of matrix
algebras by finite-dimensional C*-algebra structure theory, already used in
the operational shards following `F1-HCK-POS`.

<2>2. Every module over a matrix algebra is a direct sum of its unique
simple module and is projective; the same holds for a finite direct sum.

<2>3. Hence every finite-dimensional `A_n`-module is finitely generated
projective.

<2>4. An algebraic idempotent defining it is similar, as a module
projection, to an orthogonal projection onto the same invariant summand.
Thus the algebraic and self-adjoint-projection models are algebraically
equivalent. The projection model has matrix star as dagger; a bare right
module carries no chosen Hilbert form or dagger.

<2>5. Combining <1>8--<1>9 gives

    Proj(A_*) ~= direct-sum_n mod_fd-A_n

as algebraic strong monoidal categories, after forgetting the projection
model's dagger on the left. **QED**

## 4. The Hecke and partial-flag categories

<1>12. **ASSUME** `q>0`, `A_n=H_n(q)` and D1101--D1102.

<1>13. **PROVE** the positive Hecke category `U_q` is the finite part of
the Davydov--Molev Schur--Weyl category after exact parameter translation.

<2>1. Put `v=sqrt(q)>0` and `t_i=v^(-1)T_i`.

<2>2. Multiplying the DM10 relation
`(t_i-v)(t_i+v^(-1))=0` by `v^2` gives

    (T_i-v^2)(T_i+1)=0,

which is D1101's relation because `q=v^2`.

<2>3. Braid and far-commutativity relations are homogeneous and unchanged
by this simultaneous rescaling.

<2>4. The block maps send `t_i` to the corresponding unshifted or shifted
generator.  Scaling commutes with those maps, so this is an isomorphism of
multiplicative sequences, not merely degreewise algebra isomorphisms.

<2>5. DM10 Proposition 4.4 and Theorem 4.5, pp. 14--15, identify its
presheaf category as the abelian monoidal category freely generated by a
Hecke Yang--Baxter object.

<2>6. By `F1-HCK-POS`, every `H_n(q)` is a finite-dimensional C*-algebra.
Apply <1>11 to identify its finite-dimensional right-module part with
`U_q=Proj_*(H_*(q))`, with the bare-module equivalence understood algebraically.

<2>7. This proves the equivalence in D1227.  It also fixes the scope:
DM10 allow the full module category, while `U_q` keeps finite support and
finite-dimensional modules required for finite operational systems. **QED**

<1>14. **PROVE** D1141's partial-flag category embeds fully faithfully in
`U_q` and has the same additive Karoubi completion.

<2>1. Put `x_alpha=sum_(w in W_alpha)T_w`. Pair `w,sw` for each simple
reflection in the parabolic. The Hecke multiplication rule gives
`T_s x_alpha=q x_alpha`; star gives the right version. Consequently
`x_alpha^2=P_alpha x_alpha`, and inversion of the parabolic gives
`x_alpha^*=x_alpha`. Thus `e_alpha=x_alpha/P_alpha` is a nonzero
self-adjoint projection, since `P_alpha>0` and `tau(e_alpha)=1/P_alpha`.

<2>2. Send `alpha` to the projection-model object `(1,e_alpha)`, whose
underlying right module is `e_alpha H_n(q)`, and
`z in e_beta H_n e_alpha` to `L_z`.

<2>3. The typed module-Hom calculation <2>3 of <1>8 gives

    Hom_(H_n)(e_alpha H_n,e_beta H_n)
       ~=e_beta H_n e_alpha,

so the functor is fully faithful with the same arrow direction as D1141.

<2>4. Coxeter length is additive on ordered block permutations, so
`P_(alpha concat beta)=P_alpha P_beta`. Expanding the two normalized sums
therefore gives `mu(e_alpha tensor e_beta)=e_(alpha concat beta)`.

<2>5. For corner arrows `a=e_alpha' a e_alpha`, `b=e_beta' b e_beta`,
multiplicativity and star preservation of `mu` put `mu(a tensor b)` in the
required concatenated corner. The same properties give arrow composition
and interchange. Three-block coherence is F1-HCK-TOWER, and the empty
composition is the unit. Thus this is an actual monoidal star-category.

<2>6. The explicit isomorphism `Psi` of <1>9 therefore identifies
the induced tensor of the two right ideals with
`e_(alpha concat beta)H_(m+n)` and carries `z tensor w` to
`mu(z tensor w)`.  Thus the functor is strong monoidal and star preserving.

<2>7. In every degree `n`, the complete-flag composition
`1^n=(1,...,1)` has trivial Young subgroup and `e_(1^n)=1`.

<2>8. Hence the image contains the regular module `H_n`; finite sums and
retracts of these produce every object of `U_q` by <1>8.

<2>9. The extended projection-model functor
`Kar_*(Add(Gamma_q))->U_q` is fully faithful and essentially surjective,
hence an equivalence.  **QED**

## 5. Generic specialization and operational scope

<1>15. **PROVE** the comparison respects the named `q=1` specialization
without asserting that every fibre projection has a global lift.

<2>1. Let `R` be D1141's localization of the Laurent polynomial ring and
form `C[H_*(R)]`, its finite additive category, and its self-adjoint
idempotent envelope `Kar_*` for the stated coefficient-ring involution.

<2>2. Evaluation `R->C`, `t|->q>0`, carries multiplication, identities,
block assembly and every self-adjoint idempotent whose entries lie in `R` to the
corresponding evaluated data.

<2>3. At `q=1`, it sends `T_i` to the simple transposition and gives
`H_n(1)=C[S_n]`; it sends every named `e_alpha(t)` to the subgroup average
`|W_alpha|^(-1)sum_(w in W_alpha)w`.

<2>4. Thus all objects and arrows presented over `R`, including the whole
named partial-flag category, have coherent evaluation functors.

<2>5. An arbitrary projection constructed separately by C*-functional
calculus in a single fibre need not have entries in `R`.  Essential
surjectivity of a global evaluation functor on all fibrewise Karoubi objects
is therefore not asserted.

<2>6. At every positive fibre, normalized states live on nonzero
endomorphism corners and CP processes live in the operational envelope.
There are still zero amplitude Homs between distinct degrees, exactly as in
D1141.

<2>7. The universal category supplies composition and ordered induction;
preparations, discards and cross-degree stochastic operations remain the
typed CP data of the operational core.  **QED**

<1>16. **CONCLUDE** `F1-LIM-UNIV` and `F1-LIM-DM`: the universal finite
positive Hecke composition category is simultaneously the finite
additive-idempotent completion of the multiplicative-sequence skeleton, the
finite right-module/Day category, and the completion of the partial-flag
corner category, with all opposites and tensor maps fixed above. **QED**
