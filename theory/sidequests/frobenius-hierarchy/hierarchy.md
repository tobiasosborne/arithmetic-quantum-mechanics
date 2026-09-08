# Multiplication gates at exact prime-field hierarchy levels

Prover: native inherited agent model/settings; no independently exposed
model name. Status: PROVED within the stated hypotheses after capped review.
Definitions are D1301, D1306--D1309. Dependencies: FRB-TRACE,
FRB-FROB, FRB-CODE and FRB-TRANSFER.

Source convention comparison: Cui--Gottesman--Krishna,
`refs/frobenius-hierarchy/1608.06596/paper.txt`, p. 2, equations (3)--(6),
includes all global phases in its first hierarchy level, as does D1307.
Its multiqudit classification, Theorem 3 on p. 6, is not needed here.
Anderson, `refs/frobenius-hierarchy/2212.05398/paper.txt`, p. 2,
equation (1.1) and the paragraph beginning “We will briefly consider”,
records failure of general higher-level composition closure. We make no
such closure assertion. Every positive result below is proved internally.

Admission and repair record: `../../verdicts/frobenius-hierarchy-adjudication.md`.

## 1. Elementary hierarchy calculus

**ASSUME** D1307 on a fixed ordered register list A.
**PROVE** the hierarchy is nested, is invariant under scalar phases and
Clifford conjugation, and every level is closed under multiplication on
either side by a Pauli. Here a Clifford means an element of `C_2(A)`.

<1>1. **ASSUME** D1301's Weyl operators and D1307's Pauli definition.
**PROVE** `P_A` is a group and its projective quotient is a finite set.
  <2>1. From D8's explicit basis action, one obtains
  `W_E(a,b) W_E(c,e)=psi_E(ae) W_E(a+c,b+e)`.
  Inverses are `psi_E(ab) W_E(-a,-b)`.
  Tensor these identities and include D1307's scalar phases.
  **BY** D8 and substitution on each `|x>`.
  <2>2. Distinct translation labels give distinct basis permutations;
  with the same translation label, a scalar ratio of phase operators
  forces their momentum labels equal by FRB-TRACE nondegeneracy.
  Hence modulo `U(1)` the Pauli labels form the finite set
  `product_j S_(E_j)`. **BY** D1301, D1307 and FRB-TRACE.
  <2>3. Conjugation by a Pauli fixes each projective Pauli label, with
  a scalar factor, by <2>1 and its reversed product.
  In particular `P_A subset C_2(A)`.
  **BY** D1307 and <2>1.
  <2>4. **QED** <1>1 by <2>1--<2>3.

<1>2. **ASSUME** `C in C_2(A)`.
**PROVE** `C P_A C^*=P_A` and `C^* in C_2(A)`.
  <2>1. D1307 says conjugation maps Paulis into Paulis. It induces
  an injection of their finite projective label set: if two images differ
  by a scalar, conjugating back gives the same relation before imaging.
  Thus the injection is onto. **BY** <1>1.<2>2 and invertibility of C.
  <2>2. Conjugation fixes all scalars, so onto projective labels means
  onto the full scalar Pauli group. Conjugating this equality back shows
  `C^* P_A C=P_A`, the membership condition for `C^*`.
  **BY** D1307 and <2>1.
  <2>3. **QED** <1>2 by <2>1--<2>2.

<1>3. **ASSUME** D1307's recursion.
**PROVE** scalar invariance, nesting, Clifford conjugation invariance,
and Pauli absorption at every positive level.
  <2>1. Scalar multiplication does not change any conjugation, so
  levels at least two are scalar-invariant; level one is by definition.
  **BY** D1307.
  <2>2. Nesting starts with <1>1.<2>3. If `C_(k-1) subset C_k`
  and `U in C_k`, then all `UPU^*` lie in `C_(k-1) subset C_k`;
  hence `U in C_(k+1)`. **BY** D1307 and induction.
  <2>3. Clifford conjugation preserves level one by <1>2. Inductively,
  if it preserves level k and `U in C_(k+1)`, then
  `(C U C^*) P (C U C^*)^*=C[U(C^*PC)U^*]C^* in C_k`.
  The bracket lies in C_k because `C^*PC` is Pauli; the outer
  conjugation preserves C_k by induction. Apply also `C^*` for equality.
  **BY** D1307, <1>2 and induction on k.
  <2>4. For k=1 absorption is the group law. For k>=2 and Pauli R,
  `(UR)P(UR)^*=U(RPR^*)U^* in C_(k-1)` by the Pauli group law.
  Also `(RU)P(RU)^*=R(UPU^*)R^* in C_(k-1)` by <2>3, since
  R is Clifford by <1>1.<2>3. This proves both absorptions.
  **BY** D1307, <1>1, <2>3 and the displayed conjugations.
  <2>5. **QED** <1>3 and the hierarchy calculus by <2>1--<2>4.

## 2. Phase-polynomial upper bound and difference lower obstruction

**ASSUME** D1309 and D1307 for the same configuration space A.
**PROVE** if f has a coordinate polynomial expression of total degree
at most m, where `m>=1`, then `D_f in C_m(A)`.
Conversely, if `D_f in C_k(A)`, then every k-fold additive difference
of f is a constant function. Only this necessary condition is asserted.

<1>1. **ASSUME** `f(t)=c+ell(t)` with ell `F_p`-linear.
**PROVE** `D_f` is Pauli, and every first difference of f is constant.
  <2>1. On each field factor, every linear functional is
  `x -> Tr_E(bx)` for a unique b: FRB-TRACE makes the trace-pairing
  map injective between vector spaces of the same dimension, hence
  bijective by elimination. Decompose ell over the independent factors.
  **BY** FRB-TRACE and the coordinate direct product in D1309.
  <2>2. Thus `D_f=zeta_p^c tensor_j Z_(E_j)(b_j)` belongs to P_A.
  Also `delta_h f(t)=ell(h)` is independent of t.
  **BY** D1301, D1307, D1309 and <2>1.
  <2>3. Conversely a diagonal Pauli has zero position labels: a
  nonzero translation moves every computational basis point.
  Its phases are a constant times a trace-linear character. If the
  phases are `zeta_p^f`, their ratio at t and zero gives
  `f(t)-f(0)=ell(t)` in F_p, since zeta_p is primitive.
  Hence a diagonal D_f in C_1 has constant first differences.
  **BY** D1301, D1307 and primitivity in D1301.
  <2>4. **QED** <1>1 by <2>2--<2>3.

<1>2. **ASSUME** `X(h)|t>=|t+h>` and D1309's f.
**PROVE** the exact difference identity
`D_f X(h) D_f^* X(h)^*=D_(delta_h f)`.
  <2>1. Apply the left side right-to-left to `|t>`; the accumulated
  phase is `zeta_p^(f(t)-f(t-h))` and the final basis vector is `|t>`.
  **BY** D1301 and D1309.
  <2>2. Consequently, for every Pauli `P=lambda X(h) Z(b)`,
  `D_f P D_f^*=D_(delta_h f) P`, since all diagonal operators commute.
  The notation Z(b) here means the tensor product on the named list.
  **BY** <2>1 and D1301's diagonal phases.
  <2>3. **QED** <1>2 by <2>1--<2>2.

<1>3. **ASSUME** f has total coordinate degree at most m, `m>=2`.
**PROVE** the claimed upper bound by induction on m.
  <2>1. For a monomial `t_1^a1 ... t_N^aN`, expand its translate
  `product_j (t_j-h_j)^aj`. Its leading monomial is the original
  monomial; all remaining terms have strictly lower total degree.
  Subtraction cancels that leading monomial in any characteristic.
  Thus `delta_h f` has a polynomial expression of degree at most m-1.
  **BY** D1309 and the displayed finite binomial expansion.
  <2>2. Induction (with base <1>1) gives
  `D_(delta_h f) in C_(m-1)` for every h. Multiplication by P retains
  this level by Section 1's Pauli absorption. The conjugation identity
  of <1>2 therefore places `D_f P D_f^*` in `C_(m-1)` for every P.
  **BY** <2>1, <1>1, <1>2 and Section 1 <1>3.<2>4.
  <2>3. D1307's recursion now gives `D_f in C_m`.
  **QED** <1>3 by <2>1--<2>2 and D1307.

<1>4. **ASSUME** `D_f in C_k(A)`.
**PROVE** every k-fold difference of f is constant by induction on k.
  <2>1. The case k=1 is <1>1.<2>3.
  **BY** the diagonal-Pauli characterization there.
  <2>2. For k>=2, `D_f X(h) D_f^* in C_(k-1)` by D1307.
  Absorb the right Pauli `X(h)^*` using Section 1; <1>2 then gives
  `D_(delta_h f) in C_(k-1)` for every h.
  **BY** D1307, Section 1 <1>3.<2>4 and <1>2.
  <2>3. Apply induction to the function delta_h f. Every further
  k-1 differences is constant, which is the assertion for f.
  **BY** <2>2 and induction; differences are functions as in D1309.
  <2>4. **QED** <1>4 and Section 2 by <1>3--<1>4.

No converse degree classification is needed: different polynomial
expressions can define the same function in characteristic p. Strictness
below is witnessed by actual differences of the function itself.

## 3. FRB-HIERARCHY: multiplication has exact level d+1

**ASSUME** any D1301 field E, any `d>=1`, distinct control registers
`x_1,...,x_d`, one separate target register z, and D1308's gate.
**PROVE** it is unitary and lies in `C_(d+1)(E,...,E)` but not in C_d.
The statement holds for every p without a restriction relating p and d.

<1>1. **ASSUME** the controls are fixed.
**PROVE** M is a permutation unitary and its target Fourier conjugate
is `D_f` with `f(x_1,...,x_d,y)=-Tr_E(y product_j x_j)`.
  <2>1. The inverse sends z to `z-product_j x_j`, with controls
  unchanged. Thus M bijects the computational basis and is unitary.
  **BY** D1308 and D1301's orthonormal basis.
  <2>2. On fixed controls, M is `X_E(product_j x_j)` on the target.
  FRB-TRANSFER's Fourier covariance sends it to `Z_E(-product_j x_j)`.
  Therefore `F_target M F_target^*=D_f` with the displayed f.
  **BY** D1306, D1308, D1309 and FRB-TRANSFER <1>2.
  <2>3. Fourier is Clifford on the list: the two covariance formulas
  in FRB-TRANSFER send every target Pauli to a Pauli, and all other
  factors are unchanged. **BY** D1307 and FRB-TRANSFER <1>2.
  <2>4. **QED** <1>1 by <2>1--<2>3.

<1>2. **ASSUME** named prime-field bases on the d+1 registers.
**PROVE** `D_f in C_(d+1)`.
  <2>1. Multiplication and trace make f multilinear over F_p in
  the d+1 separate register arguments. Expand each argument in its
  named basis. Every monomial selects one coordinate from each
  register, so has degree d+1 (some coefficients may vanish).
  **BY** field distributivity, FRB-TRACE linearity and <1>1's f.
  <2>2. Section 2's upper bound gives the asserted membership.
  **BY** D1309, <2>1 and Section 2 <1>3.
  <2>3. **QED** <1>2 by <2>1--<2>2.

<1>3. **ASSUME** h_j translates control register j by `1_E` and
is zero on all other registers, for `1<=j<=d`.
**PROVE** `D_f notin C_d` using the actual d-fold difference.
  <2>1. With other variables fixed, subtraction in control j gives
  `x_j-(x_j-1)=1`. Applying these d differences successively yields
  `delta_(h_d)...delta_(h_1) f=-Tr_E(y)`.
  **BY** D1309 and the explicit multilinear expression in <1>1.
  <2>2. This function is nonconstant: it is zero at y=0 and equals
  -1 at a y with trace one, supplied by FRB-TRACE surjectivity.
  This remains nonzero in F_2. **BY** FRB-TRACE <1>3 and <2>1.
  <2>3. Membership in C_d would make every d-fold difference constant
  by Section 2 <1>4, contradicting <2>2. Hence D_f is not in C_d.
  **BY** Section 2 and <2>1--<2>2.
  <2>4. Fourier conjugation preserves every hierarchy level by Section 1.
  Thus M has the same membership and exclusion as D_f. Nesting means
  excluding C_d excludes every lower positive level as well.
  **BY** <1>1.<2>3, Section 1 <1>3, <1>2 and <2>3.
  <2>5. **QED** FRB-HIERARCHY by <1>1--<1>3.

The distinct registers matter: no derivative introduces a factorial.
Repeated arguments such as `x^p` in one register have a different
function degree and are outside D1308's statement.

## 4. FRB-NATURAL: Frobenius, embeddings and encoded multiplication

**ASSUME** D1308 with `d>=1` and a D1303 embedding `i:K->E`.
**PROVE** M commutes with simultaneous Frobenius, and
`M_E^(d) J_i^(tensor(d+1))=J_i^(tensor(d+1)) M_K^(d)`.
It consequently preserves the tensor support code and its encoded
logical action is M_K^(d), of exact logical level d+1 for FRB-CODE's
logical prime-field Pauli frame. The same intertwining holds for inverses.

<1>1. **ASSUME** an input basis point `(x_1,...,x_d,z)`.
**PROVE** simultaneous Frobenius commutes with M_E^(d).
  <2>1. Either order gives control labels `x_j^p` and target label
  `z^p+product_j x_j^p`, because `(z+product x_j)^p` equals this.
  **BY** D1302, D1308 and FRB-FROB's field-automorphism property.
  <2>2. Equality on the computational basis gives operator equality.
  **QED** <1>1 by <2>1 and linearity.

<1>2. **ASSUME** an input basis point over K.
**PROVE** embedding intertwining and exact encoded logical action.
  <2>1. Applying either side of the intertwining gives controls
  `i(x_j)` and target `i(z)+product_j i(x_j)=i(z+product_j x_j)`.
  **BY** D1304, D1308 and the embedding's field homomorphism laws.
  <2>2. The tensor encoding is an isometry by FRB-TRANSFER: tensor
  products of its orthonormal columns remain orthonormal.
  Its range is the tensor support code by D1305.
  Left-compress <2>1 by its adjoint to obtain logical M_K^(d).
  **BY** FRB-TRANSFER, D1305 and <2>1.
  <2>3. FRB-CODE identifies the logical Pauli frame with P_(K,...,K),
  factorwise using the trace quotient. FRB-HIERARCHY for K gives
  exact logical level d+1. Replacing product by its negative in
  <2>1 also proves inverse intertwining.
  **BY** FRB-CODE, FRB-HIERARCHY and D1308's inverse in Section 3.
  <2>4. **QED** FRB-NATURAL by <1>1--<1>2.

## 5. A coherent return-probability witness

**ASSUME** `Q=|E|`, `d=2`, and the normalized vector
`|+_E>=Q^(-1/2)sum_(x in E)|x>` on each of three registers.
**PROVE** the squared return amplitude for
`F_target M_E^(2) F_target^*` is `(2Q-1)^2/Q^4`.
<1>1. By Section 3 the return amplitude is
`Q^(-3)sum_(x,y,t in E) psi_E(-txy)`.
**BY** Section 3 <1>1 and D1301's orthonormal basis.
<1>2. For fixed x,y the t-sum is Q if xy=0 and zero otherwise.
This follows by the character-sum cancellation proved in FRB-CODE,
using FRB-TRACE nondegeneracy when xy is nonzero.
**BY** FRB-CODE <1>2.<2>3 and FRB-TRACE.
<1>3. A field has xy=0 iff x=0 or y=0. There are `2Q-1` such pairs,
counting `(0,0)` once. The amplitude is `(2Q-1)/Q^2`, a positive real,
so its squared modulus is the asserted probability.
**BY** the field axioms, <1>1--<1>2 and finite counting.
<1>4. **QED** by <1>1--<1>3. For Q=2 the probability is 9/16;
identity evolution has probability one on this normalized input.
The rational function tends to one at Q=1; this arithmetic observation
does not construct a specialization functor or an endpoint trace.
