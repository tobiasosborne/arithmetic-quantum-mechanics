# Algebraic braid exchange and canonical unitary cactus exchange

Status: PROVED within the stated hypotheses. Admission and repaired scope
are recorded in `../../verdicts/f1-limit-adjudication.md`.
Definitions D1228--D1231 are recorded in `../../../definitions.md`.

Source locators: Davydov--Molev (`DM10`) section 4.1, printed pp. 13--15,
especially Proposition 4.4, Theorem 4.5 and Proposition 4.6, supplies the
algebraic Hecke Yang--Baxter generator and block braiding.  Henriques--
Kamnitzer (`HK06`) arXiv:math/0406478, section 3, printed pp. 10--13,
defines a coboundary category, the interval reversals and cactus group.
Kamnitzer--Tingley (`KT09`) arXiv:0707.2248v2, Definition 4.4 and
Proposition 4.7, printed pp. 5--6, records the symmetry/cactus axioms and
Drinfeld's unitarization.  The longest-Hecke-element polar construction and
its full proof below are internal; no quantum-group representation theorem
is imported to establish it.

## 1. Parameter translation and nonunitary braid exchange

<1>1. **ASSUME** `q>0`, put `v=sqrt(q)`, and use D1101.

<1>2. **PROVE** the generator conversion to DM10 is `T_i=v t_i`.

<2>1. DM10 uses `(t_i-v)(t_i+v^(-1))=0`.

<2>2. Substitution `t_i=v^(-1)T_i` and multiplication by `v^2` gives
`(T_i-v^2)(T_i+1)=0`.

<2>3. Since `v^2=q`, this is D1101's quadratic relation.

<2>4. The braid relation has degree three on both sides and the distant
commutation relation degree two, so uniform rescaling preserves both.

<2>5. Block embeddings preserve the generator conversion, proving the
claim for the whole multiplicative sequence.  **QED**

<1>3. **PROVE** the DM10 braid is generally not a physical unitary for the
coefficient-trace C*-structure.

<2>1. The two spectral projections in `H_2(q)` are nonzero because the
coefficient trace is faithful (`F1-HCK-POS`).

<2>2. On them `T_1` has eigenvalues `q` and `-1`, so `t_1=v^(-1)T_1`
has eigenvalues `v` and `-v^(-1)`.

<2>3. Both eigenvalues have modulus one exactly when `v=1`, equivalently
`q=1`.

<2>4. Thus the algebraic Yang--Baxter automorphism of DM10 is invertible,
but it is not unitary at `q!=1`.  Its categorical braid words remain valid
algebraically.  **QED**

## 2. The adjacent spectral sign and its exact defect

<1>4. **PROVE** D1228's `u_i` is a self-adjoint unitary.

<2>1. The projection onto the `q` eigenspace is
`e_i=(T_i+1)/(q+1)` by the two distinct real roots of D1101's relation.

<2>2. Hence `u_i=2e_i-1` is self-adjoint and satisfies `u_i^2=1`.

<2>3. Explicitly this is
`u_i=(2T_i+1-q)/(q+1)`.  **QED**

<1>5. **PROVE** the exact braid-defect identity

    u_1u_2u_1-u_2u_1u_2
       =-((q-1)^2/(q+1)^2)(u_1-u_2)

in `H_3(q)`.

<2>1. Write `x=T_1`, `y=T_2`, `a=2/(q+1)` and
`b=(1-q)/(q+1)`, so `u_1=ax+b`, `u_2=ay+b`.

<2>2. Direct expansion and cancellation of the braid terms gives

    (ax+b)(ay+b)(ax+b)-(ay+b)(ax+b)(ay+b)
      =a^2 b(x^2-y^2)+a b^2(x-y).

<2>3. The quadratic relations give
`x^2-y^2=(q-1)(x-y)`.

<2>4. Therefore the right side of <2>2 is

    ab(a(q-1)+b)(x-y)
      =-((q-1)^2/(q+1)^2) a(x-y).

<2>5. Since `a(x-y)=u_1-u_2`, the displayed defect follows.

<2>6. The standard basis makes `T_1-T_2` nonzero.  Thus for `q!=1` the
unitaries `u_i` do not satisfy the braid relation.  **QED**

<1>6. **CONCLUDE** spectral normalization solves local unitarity but cannot
turn the algebraic Hecke braiding into a unitary braiding.  A positive
replacement must obey different coherence; the next sections construct a
coboundary/cactus commutor. **QED**

## 3. Polar reversals from longest Hecke elements

<1>7. **ASSUME** `n>=2`, let `w_0=w_0^(n)` and `D_n=T_(w_0)`.

<1>8. **PROVE** `D_n` is self-adjoint, invertible, and its square is
central.

<2>1. The basis star relation of `F1-HCK-POS` is
`T_w^*=T_(w^(-1))`; since `w_0^2=1`, `D_n^*=D_n`.

<2>2. Every generator is invertible, with

    T_i^(-1)=q^(-1)(T_i-q+1),

as follows by multiplying the quadratic relation out.

<2>3. Hence their reduced product `D_n` is invertible.

<2>4. The longest permutation satisfies
`w_0s_i=s_(n-i)w_0`, and both sides have length `ell(w_0)-1`.

<2>5. The descending-length multiplication rule gives

    D_nT_i=qT_(w_0s_i)+(q-1)D_n
           =T_(n-i)D_n.

<2>6. Applying <2>5 twice yields `D_n^2T_i=T_iD_n^2`.

<2>7. The `T_i` generate `H_n(q)`, so `D_n^2` is central.  **QED**

<1>9. **PROVE** `J_n=D_n(D_n^2)^(-1/2)` is a canonical self-adjoint
unitary and implements reversal.

<2>1. Because `D_n` is self-adjoint and invertible, `D_n^2` is positive
and invertible in the finite C*-algebra.

<2>2. Its positive square root and inverse are unique.  Centrality of
`D_n^2` implies centrality of every continuous functional-calculus function,
including `|D_n|=(D_n^2)^(1/2)`.

<2>3. Therefore `J_n=D_n|D_n|^(-1)` is self-adjoint and
`J_n^2=D_n^2|D_n|^(-2)=1`.

<2>4. Since `|D_n|` is central, <2>5 of <1>8 gives

    J_nT_iJ_n=T_(n-i).

<2>5. Uniqueness of the positive square root makes `J_n` choice-free at a
fixed positive fibre.  **QED**

<1>10. **PROVE** the interval reversals `J_[p,r]` satisfy the cactus
interval relations.

<2>1. A shifted interval copy is unitary and involutive by <1>9.

<2>2. Copies on disjoint intervals commute because all their generators
have disjoint indices (D1101).

<2>3. Conjugation by `J_[p,r]` sends the generator at position `i` in that
interval to the generator at reflected position `p+r-i-1`.

<2>4. It consequently sends the shifted longest element of a subinterval
`[k,l] subseteq[p,r]` to the longest element of the reflected interval
`[p+r-l,p+r-k]`.

<2>5. Functional calculus commutes with unitary conjugation, so the same is
true of its polar sign:

    J_[p,r] J_[k,l] J_[p,r]
      =J_[p+r-l,p+r-k].

<2>6. Equivalently,

    J_[p,r]J_[k,l]
      =J_[p+r-l,p+r-k]J_[p,r],

which, together with <2>1--<2>2, is the standard interval presentation of
the cactus relations (HK06 section 3, pp. 11--13).  **QED**

## 4. The block commutor

<1>11. **ASSUME** `m,n>=0`, `N=m+n`, and put

    K_(m,n)=mu_(m,n)(J_m tensor J_n),
    sigma_(m,n)=J_N K_(m,n).

<1>12. **PROVE** `sigma_(m,n)` is a unitary intertwiner which swaps the
two block subalgebras.

<2>1. The two shifted factors of `K_(m,n)` commute and are unitary, so
`K_(m,n)` and `sigma_(m,n)` are unitary.

<2>2. Conjugation by `K_(m,n)` reverses generator order separately inside
the first `m` and last `n` blocks.

<2>3. Conjugation by `J_N` then reverses the total order.  The two internal
reversals cancel, leaving only the block swap.

<2>4. Hence, for all `a in H_m(q)`, `b in H_n(q)`,

    sigma_(m,n) mu_(m,n)(a tensor b) sigma_(m,n)^*
      =mu_(n,m)(b tensor a).

<2>5. Equivalently, the typed naturality equation is

    sigma_(m,n) mu(a tensor b)
      =mu(b tensor a) sigma_(m,n).

<2>6. This proves naturality on tensor powers; linearity gives naturality
on finite sums and compression gives it on retracts.  **QED**

<1>13. **PROVE** symmetry:
`sigma_(n,m)sigma_(m,n)=1` with the second commutor typed after the swap.

<2>1. Total reversal conjugates the internal reversal for blocks `(n,m)`
to the internal reversal for blocks `(m,n)`:

    J_N K_(n,m)J_N=K_(m,n).

<2>2. Therefore

    sigma_(n,m)sigma_(m,n)
      =J_NK_(n,m)J_NK_(m,n)=K_(m,n)^2=1.

<2>3. When one block is empty, `J_NJ_N=1`, proving the unit axioms. **QED**

<1>14. **PROVE** the cactus axiom for blocks of sizes `l,m,n`.

<2>1. Work on the interval `[1,l+m+n]` and abbreviate the reversal of an
interval by its `J`.

<2>2. The path which first swaps the `l,m` blocks and then swaps their
combined block past `n` has product

    [J_(l+m+n) J_[1,l+m] J_[l+m+1,l+m+n]]
    [J_[1,l+m] J_[1,l] J_[l+1,l+m]].

<2>3. Disjoint interval reversals commute and every `J_I^2=1`, so <2>2
reduces to

    J_(l+m+n) J_[1,l] J_[l+1,l+m] J_[l+m+1,l+m+n].

<2>4. The path which first swaps `m,n` and then swaps `l` past their
combined block has product

    [J_(l+m+n) J_[1,l] J_[l+1,l+m+n]]
    [J_[l+1,l+m+n] J_[l+1,l+m] J_[l+m+1,l+m+n]].

<2>5. It reduces to the same expression as <2>3.

<2>6. This is exactly the cactus square in KT09 Definition 4.4, with
strict associators.  Thus `sigma` is a coboundary commutor. **QED**

## 5. Parabolic and arbitrary-corner compatibility

<1>15. **PROVE** the commutor restricts to every D1141 parabolic corner.

<2>1. If `rev(alpha)` reverses the list of parts of `alpha`, conjugation by
`J_n` sends the Young parabolic generators for `alpha` to those for
`rev(alpha)`.

<2>2. It preserves length and the coefficients of
`e_alpha=P_alpha(q)^(-1)sum_(w in W_alpha)T_w`.

<2>3. Thus `J_n e_alpha J_n=e_(rev(alpha))`.

<2>4. Internal reversals send
`e_(alpha concat beta)` to `e_(rev(alpha) concat rev(beta))`, and total
reversal sends this to `e_(beta concat alpha)`.

<2>5. Consequently

    sigma_(m,n)e_(alpha concat beta)sigma_(m,n)^*
       =e_(beta concat alpha).

<2>6. The restriction

    sigma_(alpha,beta)
      =e_(beta concat alpha)sigma_(m,n)e_(alpha concat beta)

is therefore a unitary from `alpha tensor beta` to `beta tensor alpha`,
with inverse `sigma_(beta,alpha)`.

<2>7. For arbitrary projections `p in M_r(H_m)` and
`s in M_t(H_n)`, equation <2>4 of <1>12 similarly carries
`mu(p tensor s)` to `mu(s tensor p)`; the finite matrix-index flip supplies
the direct-sum ordering.  Hence the commutor extends to all of `U_q`. **QED**

## 6. Polar decomposition of block braids

<1>16. **PROVE** `sigma_(m,n)` is the polar unitary of a standard
algebraic block braid.

<2>1. Put `D_(m,n)=mu(D_m tensor D_n)`.

<2>2. Longest-word factorization in `S_(m+n)` gives a length-additive
factorization

    D_(m+n)=B_(m,n)D_(m,n),

where `B_(m,n)` is the Hecke image of the positive minimal braid which
swaps the two ordered blocks.  Equivalently define
`B_(m,n)=D_(m+n)D_(m,n)^(-1)`.

<2>3. Let `K=J_m tensor J_n`.  Since `D=J|D|` in each block,
`D_(m,n)=K|D_(m,n)|`.

<2>4. Using centrality of `|D_(m+n)|` and commutation of the block polar
factors with their moduli,

    sigma_(m,n)^* B_(m,n)
      =K J_(m+n)D_(m+n)D_(m,n)^(-1)
      =|D_(m+n)| |D_(m,n)|^(-1).

<2>5. The last two positive invertible elements commute because the first
is central.  Their product is positive invertible.

<2>6. Hence `B_(m,n)=sigma_(m,n)P_(m,n)` with `P_(m,n)>0`; uniqueness of
polar decomposition identifies `sigma_(m,n)` as its polar unitary. **QED**

## 7. Specialization and exact scope

<1>17. **PROVE** the commutor is continuous for `q>0` and specializes to
the symmetric block permutation at one.

<2>1. Multiplication matrices of `D_n(q)` in the standard basis depend
polynomially on `q`.  Conjugating by the diagonal isometry
`T_w |->q^(ell(w)/2)T_w` places the varying coefficient-trace inner products
on one fixed Euclidean space, with matrices continuous in `q>0`.

<2>2. They remain invertible for `q>0`; inverse square root is continuous
on positive invertible matrices.  Thus `J_n(q)` and `sigma_(m,n)(q)` vary
continuously on the positive real axis.

<2>3. At `q=1`, every `T_i` is a self-adjoint unitary.  Hence `D_n` is the
unitary longest permutation and `J_n=D_n`.

<2>4. The factorization in <1>16 makes `sigma_(m,n)(1)` the ordinary block
shuffle.  The cactus structure then agrees with the symmetry.

<2>5. For `q!=1`, `sigma_(1,1)=J_2=u_1`; <1>5 proves these adjacent
commutors do not braid.  Thus the result is genuinely coboundary.

<2>6. Functional-calculus square roots need not lie in D1141's localized
generic coefficient ring.  The construction is canonical on each positive
C*-fibre and on continuous positive intervals; no algebraic generic
commutor over that ring is claimed.  **QED**

<1>18. **CONCLUDE** `F1-LIM-EXCH`: the standard Hecke exchange is an
algebraic nonunitary braiding away from one, and its adjacent spectral signs
have the registered defect.  **CONCLUDE** `F1-LIM-COB`: polar longest
reversals furnish a canonical natural unitary coboundary/cactus structure on
the entire positive Hecke composition category, including all parabolic and
Karoubi corners. **QED**
