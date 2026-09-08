# Trace geometry, Frobenius and subfield stabilizers

Prover: native inherited agent model/settings (model name not independently
exposed). Status: PROVED within the stated hypotheses after capped review.
All characteristics are included. Definitions are D1301--D1305 and D8.
This shard derives the finite-field facts it uses; source corroboration is
Stacks, local `refs/frobenius-hierarchy/stacks-0BIE/source.html`, Lemmas
9.20.5 (tag 0BIJ) and 9.20.7 (tag 0BIL), and D3's trace-power formula.
No existence or functoriality of a full Weil representation is used.

Admission and repair record: `../../verdicts/frobenius-hierarchy-adjudication.md`.

## 1. FRB-TRACE: relative trace and prime-field symplectic geometry

**ASSUME** D1301 and a D1303 embedding `i:K->E`, with
`|K|=q=p^s`, `|E|=q^d=p^r`.
**PROVE** the trace formula takes values in `i(K)`, `T_i` is surjective
and `K`-linear, `kappa_i=|E|/|K|`, the trace pairing on `E/F_p` is
nondegenerate, and `Omega_E` is alternating and nondegenerate.
For a tower `j:L->K`, prove `T_(i j)=T_j T_i`; prove also
`Tr_(E/F_p)(i(a)x)=Tr_(K/F_p)(aT_i(x))`.

<1>1. **ASSUME** a finite field `B` with `Q` elements.
**PROVE** `x^Q=x` for all `x in B`; a nonzero polynomial over a field
of degree `n` has at most `n` roots.
  <2>1. If `x != 0`, multiplication by `x` permutes `B^times`.
  Multiplying its elements gives `x^(Q-1) product B^times=product B^times`.
  Cancel the nonzero product to get `x^(Q-1)=1`; `x=0` is direct.
  **BY** field multiplication and the finite cardinality in D1301.
  <2>2. For a root `a`, division by the monic polynomial `t-a` gives
  `f(t)=(t-a)g(t)` with `deg g=deg f-1`; any other root is a root of `g`.
  Division follows by successively cancelling the leading monomial.
  Induction starting with a nonzero constant proves the root bound.
  **BY** the field axioms and this displayed cancellation algorithm.
  <2>3. **QED** <1>1 by <2>1--<2>2.

<1>2. **ASSUME** `S(x)=sum_(j=0)^(d-1) x^(q^j)` in `E`.
**PROVE** `S(x) in i(K)` and `S` is `i(K)`-linear and nonzero.
  <2>1. In characteristic `p`, `(x+y)^p=x^p+y^p`: the intermediate
  binomial coefficients are divisible by `p`, since `p` divides `p!`
  but not `k!(p-k)!` for `0<k<p`. Iteration gives the same assertion
  for every `p`-power. **BY** D1301 and the binomial expansion.
  <2>2. `S(x)^q-S(x)=x^(q^d)-x=0` by <1>1.
  Every element of `i(K)` is a root of `t^q-t` by <1>1, and there are
  already `q` such elements; the root bound allows no others.
  Thus `S(x) in i(K)`. **BY** <1>1 and <2>1.
  <2>3. Additivity follows termwise from <2>1. If `c in i(K)`, then
  `c^(q^j)=c`, hence `S(cx)=cS(x)`. **BY** <1>1 and the formula for S.
  <2>4. The polynomial `sum_j t^(q^j)` has nonzero highest coefficient
  and degree `q^(d-1)<q^d`. It cannot vanish on every point of `E`.
  Thus `S` is nonzero even if `p` divides `d`. **BY** <1>1's root bound.
  <2>5. **QED** <1>2 by <2>2--<2>4.

<1>3. **ASSUME** D1303.
**PROVE** `T_i` is well defined, `T_i(i(a)x)=aT_i(x)`, is surjective,
and has kernel cardinality `|E|/|K|`.
  <2>1. Apply the inverse embedding to <1>2. A nonzero linear map to
  the one-dimensional `K`-space `K` is onto: if `T_i(x)=c != 0`, then
  `T_i(i(a/c)x)=a` for each `a`. **BY** D1303 and <1>2.
  <2>2. For each `a`, choose one preimage `x_a`. Its fibre is
  `x_a+ker T_i`, as follows by subtracting two preimages.
  There are `|K|` disjoint fibres, each with `kappa_i` points.
  Therefore `|E|=|K|kappa_i`. **BY** D1303 and <2>1.
  <2>3. **QED** <1>3 by <2>1--<2>2.

<1>4. **ASSUME** a D1303 tower `L --j--> K --i--> E`, with
`|L|=p^t`, `s=et`, `r=ds`.
**PROVE** `T_(i j)=T_j T_i`, absolute trace transitivity and the pairing
identity in the claim.
  <2>1. Transport the composite trace into `E`. It is
  `sum_(a=0)^(e-1) sum_(b=0)^(d-1) x^(p^(ta+sb))`.
  The indices `a+eb` run once through `0,...,ed-1`, giving precisely
  D1303's formula for `T_(i j)`. **BY** D1303 and <1>2.<2>1.
  <2>2. Specialize `L=F_p` with its unique unital embedding.
  Then D1303's formula is D3's absolute trace formula.
  Consequently `Tr_E=Tr_K T_i`. **BY** <2>1 and D3.
  <2>3. `Tr_E(i(a)x)=Tr_K(T_i(i(a)x))=Tr_K(aT_i(x))`.
  **BY** <2>2 and <1>3.<2>1.
  <2>4. **QED** <1>4 by <2>1--<2>3.

<1>5. **ASSUME** `c in E` is nonzero.
**PROVE** some `x in E` satisfies `Tr_E(cx) != 0`.
  <2>1. Apply <1>3 to `F_p->E` to obtain `u` with `Tr_E(u)=1`.
  Take `x=c^(-1)u`. Then `Tr_E(cx)=1`. **BY** <1>3 and field inverses.
  <2>2. The trace pairing is therefore nondegenerate; it is bilinear
  by <1>2 and multiplication distributivity. **BY** <2>1 and D1301.
  <2>3. **QED** <1>5 by <2>1--<2>2.

<1>6. **ASSUME** `v=(a,b) in S_E`.
**PROVE** `Omega_E` is alternating and nondegenerate over `F_p`.
  <2>1. `Omega_E(v,v)=Tr_E(ab-ab)=0` in every characteristic.
  Bilinearity follows from <1>5's bilinearity. **BY** D1301.
  <2>2. If `Omega_E(v,w)=0` for every `w`, first take `w=(0,c)`;
  <1>5 implies `a=0`. Then take `w=(c,0)`; <1>5 implies `b=0`.
  Thus the radical is zero. **BY** D1301 and <1>5.
  <2>3. **QED** <1>6 and FRB-TRACE by <1>3--<1>6.

## 2. FRB-FROB: exact covariance and atomic factorization

**ASSUME** D1301--D1302, with `|E|=p^r`.
**PROVE** `sigma_E` is an automorphism, `U_E` is unitary, both have
order r, and
`Omega_E(sigma_E v,sigma_E w)=Omega_E(v,w)` and
`U_E W_E(a,b) U_E^*=W_E(a^p,b^p)` hold exactly.
Given a named `F_p`-basis `(e_j)` and its trace-dual `(e^j)`, prove that
the associated coordinate unitary identifies `W_E(a,b)` with the tensor
product of prime-field Weyl operators, using position coordinates in
`(e_j)` and momentum coordinates in `(e^j)`.

<1>1. **ASSUME** `sigma_E(x)=x^p`.
**PROVE** it is a field automorphism and `Tr_E(x^p)=Tr_E(x)`.
  <2>1. Multiplication and the unit are preserved by field powers;
  addition is preserved by FRB-TRACE <1>2.<2>1. If `x^p=y^p`, then
  `(x-y)^p=0`, whence `x=y` in a field. An injection of the finite
  set `E` into itself is bijective. **BY** D1302 and FRB-TRACE.
  <2>2. The trace sum after taking a `p`-th power is shifted cyclically,
  since `x^(p^r)=x`. This gives trace invariance.
  **BY** D3 and FRB-TRACE <1>1.
  <2>3. `sigma_E^r=id` by FRB-TRACE <1>1. If `0<k<r` and
  `sigma_E^k=id`, all `p^r` elements would be roots of the nonzero
  polynomial `t^(p^k)-t` of smaller degree, contrary to its root bound.
  Thus sigma_E has exact order r; its faithful basis permutation U_E
  has the same order. **BY** D1302 and FRB-TRACE <1>1.
  <2>4. **QED** <1>1 by <2>1--<2>3.

<1>2. **ASSUME** `v=(a,b),w=(a',b')`.
**PROVE** the phase-space and operator covariance assertions.
  <2>1. `Omega_E(sigma v,sigma w)=Tr_E((ab'-a'b)^p)=Omega_E(v,w)`.
  **BY** D1301 and <1>1.
  <2>2. `U_E` permutes an orthonormal basis and hence is unitary.
  On that basis `U_E X_E(a) U_E^*|x>=|x+a^p>`.
  **BY** D1301--D1302 and <1>1's bijectivity.
  <2>3. If `y=sigma_E^(-1)(x)`, then
  `psi_E(by)=psi_E((by)^p)=psi_E(b^p x)`.
  Hence `U_E Z_E(b) U_E^*=Z_E(b^p)`.
  **BY** D1301 and <1>1.<2>2.
  <2>4. Multiply <2>2 and <2>3 in D8's order. This gives
  `U_E W_E(a,b) U_E^*=W_E(a^p,b^p)` without a phase correction.
  **BY** D1301 and <2>2--<2>3.
  <2>5. **QED** <1>2 by <2>1--<2>4.

<1>3. **ASSUME** a named `F_p`-basis `(e_1,...,e_r)` of `E`.
**PROVE** a unique trace-dual basis exists and gives the asserted
tensor factorization.
  <2>1. The matrix `B_ij=Tr_E(e_i e_j)` has zero kernel by
  FRB-TRACE <1>5: a kernel column represents a vector orthogonal to all
  of `E`. Gaussian elimination supplies an inverse matrix and a unique
  basis `(e^j)` with `Tr_E(e_i e^j)=delta_ij`.
  **BY** FRB-TRACE and finite-dimensional elimination.
  <2>2. Write `x=sum x_j e_j`, `a=sum a_j e_j`, `b=sum b_j e^j`.
  The coordinate unitary sends `|x>` to `tensor_j |x_j>`.
  It sends translation by `a` to independent translations by `a_j`.
  **BY** D1301 and uniqueness of basis coordinates.
  <2>3. `Tr_E(b(x+a))=sum_j b_j(x_j+a_j)` by <2>1.
  Substitution into D8 yields exactly `tensor_j W_(F_p)(a_j,b_j)`.
  **BY** D8, <2>1 and <2>2.
  <2>4. **QED** <1>3 and FRB-FROB by <1>2--<1>3.

The factorization depends on the position basis. No self-dual basis and no
characteristic-two splitting theorem for all symplectic maps is assumed.

## 3. FRB-CODE: support stabilizers and logical quotient

**ASSUME** D1301--D1305 and a named embedding `i:K->E`.
**PROVE** `C_i` is exactly the common `+1` eigenspace of `G_i`,
`dim C_i=|K|`, and `P_i=kappa_i^(-1)sum_(b in ker T_i) Z_E(b)`.
Moreover `N_i^perp=i(K) direct-sum E`, and D1305's quotient map is a
symplectic isomorphism onto `S_K`. Exactly the Weyl operators with
position label in `i(K)` preserve the code; their restrictions satisfy
`J_i^* W_E(i(a),b) J_i=W_K(a,T_i(b))`.

<1>1. **ASSUME** the absolute trace pairing from FRB-TRACE.
**PROVE** the annihilator of `i(K)` is `ker T_i`, and the annihilator
of `ker T_i` is `i(K)`.
  <2>1. `Tr_E(bi(a))=Tr_K(aT_i(b))` for all `a,b`.
  Thus it vanishes for all `a` iff `T_i(b)=0` by nondegeneracy on `K`.
  **BY** FRB-TRACE <1>4 and <1>5.
  <2>2. For completeness, if `B` is a nondegenerate pairing on a
  finite-dimensional space `V`, the annihilator of an `m`-dimensional
  subspace `L` has dimension `dim V-m`: extend a basis of `L` to one
  of `V`; the restriction of linear functionals to `L` is onto, and
  `v -> B(v,.)` is invertible by nondegeneracy and elimination.
  Its composite with restriction has a kernel of that dimension.
  **BY** FRB-TRACE's nondegeneracy and basis extension/elimination.
  <2>3. The inclusion `i(K) subset (ker T_i)^perp` follows from <2>1.
  By <2>2 both spaces have prime-field dimension `s`, so they coincide.
  **BY** <2>1--<2>2 and FRB-TRACE's kernel cardinality.
  <2>4. **QED** <1>1 by <2>1 and <2>3.

<1>2. **ASSUME** `v=sum_x c_x|x>`.
**PROVE** the code, dimension and projector assertions.
  <2>1. Since all `Z_E(b)` are diagonal, they fix `v` iff for every
  nonzero `c_x` one has `zeta_p^(Tr_E(bx))=1` for all `b in ker T_i`.
  A primitive root has this value iff its exponent is zero in `F_p`.
  By <1>1 this means `x in i(K)`. **BY** D1301 and D1305.
  <2>2. The vectors `|i(a)>` form an orthonormal family of cardinality
  `|K|`; their coordinate projection is `J_i J_i^*`.
  **BY** D1304--D1305 and injectivity of `i`.
  <2>3. On `|x>`, the stabilizer average has eigenvalue
  `kappa_i^(-1)sum_b psi_E(bx)`. If this character is trivial the
  value is one. Otherwise choose `b_0` with `psi_E(b_0x)!=1`;
  translation of the sum by `b_0` multiplies it by that value, so the
  sum is zero. By <1>1 these cases mean `x in i(K)` and its complement.
  **BY** D1301, <1>1 and the displayed finite-sum argument.
  <2>4. **QED** <1>2 by <2>1--<2>3.

<1>3. **ASSUME** D1305's `N_i`.
**PROVE** the quotient and Weyl restriction assertions.
  <2>1. `Omega_E((a,b),(0,c))=Tr_E(ac)`. By <1>1 it vanishes for
  all `c in ker T_i` iff `a in i(K)`. Also `Omega_E(N_i,N_i)=0`.
  Hence `N_i^perp=i(K) direct-sum E` and `N_i` is isotropic.
  **BY** D1301, D1305 and <1>1.
  <2>2. The map `(i(a),b) -> (a,T_i(b))` is surjective, has kernel
  `N_i`, and preserves the alternating forms by FRB-TRACE <1>4.
  It thus induces the asserted symplectic isomorphism.
  **BY** D1305, FRB-TRACE and <2>1.
  <2>3. D8 gives
  `W_E(i(a),b)|i(x)>=psi_K(-T_i(b)(x+a))|i(x+a)>`.
  This is exactly `J_i W_K(a,T_i(b))|x>`.
  **BY** D8 and FRB-TRACE <1>4.
  <2>4. A Weyl operator with translation label `c` sends the support
  set `i(K)` to `c+i(K)`. This equals `i(K)` iff `c in i(K)`;
  phase factors never vanish. **BY** D8 and additive cosets.
  <2>5. **QED** <1>3 and FRB-CODE by <1>2--<1>3.

## 4. Constructive boundary recorded with the positive package

**ASSUME** D1303 with extension degree `d`.
**PROVE** `psi_E(i(a))=psi_K(a)^d`; the logical momentum coordinate of
`i(b)` is `db`, so momentum inclusion can collapse when `p` divides `d`.
<1>1. Every term in the relative trace of `i(a)` is `i(a)`, whence
`T_i(i(a))=da`. **BY** D1303 and FRB-TRACE <1>1.
<1>2. Trace transitivity gives `psi_E(i(a))=zeta_p^(Tr_K(da))`;
FRB-CODE identifies the momentum coordinate with `T_i(i(b))=db`.
**BY** D1301, FRB-TRACE <1>4 and FRB-CODE.
<1>3. **QED** by <1>1--<1>2.
The positive replacement is the trace quotient, requiring no division by
the extension degree and no trace-one choice in a field.
