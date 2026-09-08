# Coherent arithmetic transfers and the binary quartic example

Prover: native inherited agent model/settings; exact model name unavailable.
Status: PROVED within the stated hypotheses after capped review. Definitions are
D1301--D1306 and D1310. Dependencies: FRB-TRACE, FRB-FROB and FRB-CODE.
All claims are internal matrix or finite-field computations. Stacks
`refs/frobenius-hierarchy/stacks-0BIE/source.html`, tag 0BIJ, independently
corroborates trace transitivity; no source is used to infer normalization.

Admission and repair record: `../../verdicts/frobenius-hierarchy-adjudication.md`.

## 1. FRB-TRANSFER: Fourier-dual isometries, towers and Frobenius

**ASSUME** a named D1303 embedding `i:K->E` over D1301's common
`p,zeta_p`, and D1304's maps `J_i,V_i`.
**PROVE** both maps are isometries, `F_E` is unitary, and
`F_E J_i=V_i F_K`. For `j:L->K`, prove
`J_i J_j=J_(i j)` and `V_i V_j=V_(i j)`; identity embeddings give
identity maps. Prove `U_E J_i=J_i U_K` and `U_E V_i=V_i U_K`.

<1>1. **ASSUME** `a,b in K`.
**PROVE** `J_i^*J_i=V_i^*V_i=I_(H_K)`.
  <2>1. The inner product of `|i(a)>` and `|i(b)>` is `delta_ab`,
  since the embedding is injective. **BY** D1301 and D1304.
  <2>2. Distinct trace fibres are disjoint. Each fibre has `kappa_i`
  elements by FRB-TRACE, so D1304's squared normalization gives norm
  `kappa_i^(-1)kappa_i=1` and distinct columns are orthogonal.
  **BY** D1304 and FRB-TRACE <1>3.
  <2>3. **QED** <1>1 by <2>1--<2>2.

<1>2. **ASSUME** D1306's negative Fourier kernel.
**PROVE** `F_E` is unitary, `F_E X_E(a) F_E^*=Z_E(-a)` and
`F_E Z_E(b) F_E^*=X_E(b)`.
  <2>1. The inner product of columns indexed by `x,x'` is
  `|E|^(-1)sum_y psi_E((x-x')y)`. It is one if `x=x'` and zero
  otherwise: use FRB-TRACE's nondegeneracy and the finite character-sum
  cancellation in FRB-CODE <1>2.<2>3.
  A square matrix with orthonormal columns is unitary, since its inverse
  is its adjoint by elimination. **BY** D1306 and the cited steps.
  <2>2. For every `x`, the coefficients of `F_E X_E(a)|x>` are
  `|E|^(-1/2)psi_E(-(x+a)y)`. These are the coefficients of
  `Z_E(-a)F_E|x>`. **BY** D1301 and D1306.
  <2>3. The coefficient at `y` in `X_E(b)F_E|x>` is
  `|E|^(-1/2)psi_E(-x(y-b))`, equal to that in `F_E Z_E(b)|x>`.
  **BY** D1301 and D1306.
  <2>4. Multiplying the identities by `F_E^*` proves the covariance.
  **QED** <1>2 by <2>1--<2>3.

<1>3. **ASSUME** `a in K`, `x in E`.
**PROVE** the Fourier-transfer identity.
  <2>1. The coefficient of `|x>` in `F_E J_i|a>` is
  `|E|^(-1/2)psi_E(-i(a)x)`.
  **BY** D1304 and D1306.
  <2>2. The coefficient in `V_i F_K|a>` is
  `(|K|kappa_i)^(-1/2)psi_K(-aT_i(x))`.
  **BY** D1304 and D1306; the unique fibre containing x is labelled T_i(x).
  <2>3. The normalizations agree by FRB-TRACE's fibre cardinality;
  the phases agree by its trace-pairing identity.
  Thus `F_E J_i=V_i F_K` coefficientwise.
  **BY** FRB-TRACE <1>3--<1>4 and <2>1--<2>2.
  <2>4. **QED** <1>3 by <2>3.

<1>4. **ASSUME** a named tower `L --j--> K --i--> E`.
**PROVE** both tower identities and the identity-arrow assertion.
  <2>1. `J_i J_j|a>=|i(j(a))>=J_(i j)|a>`.
  **BY** D1304 and composition of named embeddings.
  <2>2. In `V_i V_j|a>`, a basis point `x in E` occurs precisely
  when `T_j(T_i(x))=a`, and it occurs once, from the intermediate
  label `T_i(x)`. Its coefficient is `(kappa_i kappa_j)^(-1/2)`.
  **BY** D1304 and disjointness of the trace fibres.
  <2>3. `T_j T_i=T_(i j)` by FRB-TRACE. Also
  `kappa_i kappa_j=(|E|/|K|)(|K|/|L|)=kappa_(i j)`.
  Substitution in <2>2 gives `V_i V_j=V_(i j)`.
  **BY** FRB-TRACE <1>3--<1>4.
  <2>4. For `i=id_E`, D1303's degree-one sum is the identity and
  `kappa_i=1`. Both D1304 formulas then give `I_(H_E)`.
  **BY** D1303--D1304.
  <2>5. **QED** <1>4 by <2>1--<2>4.

<1>5. **ASSUME** a D1303 embedding `i:K->E`.
**PROVE** Frobenius equivariance of both transfers.
  <2>1. Since an embedding preserves multiplication, `i(a^p)=i(a)^p`.
  Thus `U_E J_i|a>=J_i U_K|a>`.
  **BY** D1302 and D1304.
  <2>2. Take a `p`-th power of the relative-trace sum to obtain
  `T_i(x^p)=T_i(x)^p`. The inverse-embedding transport respects powers.
  **BY** D1303 and FRB-TRACE <1>2.<2>1.
  <2>3. The bijection `x -> x^p` sends the fibre over `a` bijectively
  to the fibre over `a^p`; the coefficient `kappa_i^(-1/2)` is unchanged.
  Hence `U_E V_i|a>=V_i U_K|a>`.
  **BY** <2>2, D1304 and FRB-FROB's bijectivity.
  <2>4. **QED** <1>5 and FRB-TRANSFER by <1>1--<1>5.

## 2. Direct transfer consequences for typed generators

**ASSUME** D1303--D1304.
**PROVE** the reverse Fourier identity
`J_i^* F_E^*=F_K^* V_i^*`, and the compressed logical identities
`J_i^* U_E J_i=U_K` and `V_i^* U_E V_i=U_K`.
<1>1. Taking Hilbert adjoints of FRB-TRANSFER's Fourier equality
reverses multiplication and gives the first formula.
**BY** FRB-TRANSFER and the matrix adjoint rule, entrywise conjugation.
<1>2. Left-multiply the two Frobenius intertwinings by their adjoints.
The isometry identities cancel the adjacent encoding/decoding pairs.
**BY** FRB-TRANSFER <1>1 and <1>5.
<1>3. **QED** by <1>1--<1>2.
These are consequences of FRB-TRANSFER rather than separate claim rows.

The domains in every tower formula are fixed by the named embeddings:
`J_i J_j` and `V_i V_j` run from `H_L` to `H_E`, while their adjoints
run from `H_E` to `H_L`. Normalization uses positive real square roots;
an independent phase choice on each transfer would change the strict
tower equality and is not part of D1304.

## 3. FRB-EXAMPLE: the explicit binary degree-four tower

**ASSUME** D1310's polynomial quotients and constant embeddings.
**PROVE** `K` and `E` are fields of cardinalities four and sixteen,
and the following formulas hold, for `u,v in K`:
`sigma_E(u,v)=(u^2+a v^2,v^2)`,
`sigma_E^2(u,v)=(u+v,v)`, `sigma_E^4=id`, `ord sigma_E=4`,
`T_(K->E)(u,v)=v`, `Tr_(E/F_2)(u,v)=v+v^2`.
The support code has basis `|u,0>`, dimension four, and its transfers are
`J|u>=|u,0>`, `V|v>=(1/2)sum_(u in K)|u,v>`.
For the full tower `F_2->E`, the fibre normalization is `1/sqrt(8)`.
Frobenius-fixed vectors and subfield support differ already for `U_E^2`:
their dimensions are ten and four, respectively.

<1>1. **ASSUME** `f(t)=t^2+t+1` over `F_2`.
**PROVE** `K` is a field with elements `0,1,a,a+1`, and `a^2=a+1`.
  <2>1. `f(0)=f(1)=1`, so a degree-two factorization into nonconstant
  factors cannot exist: both factors would be linear and supply a root.
  Every residue class reduces uniquely to degree below two by monic
  division. **BY** D1310 and polynomial division, as in FRB-TRACE <1>1.
  <2>2. Every nonzero polynomial of degree below two is coprime to f,
  so the Euclidean algorithm expresses one as its multiple plus an
  f-multiple, producing an inverse in the quotient.
  The Euclidean algorithm terminates because successive remainders have
  strictly smaller degree. **BY** <2>1 and polynomial division.
  <2>3. Thus the four residues form a field, with the displayed relation.
  **QED** <1>1 by <2>1--<2>2 and D1310.

<1>2. **ASSUME** `g(t)=t^2+t+a` over K.
**PROVE** `E` is a field with sixteen elements and `b^2=b+a`.
  <2>1. From `a^2=a+1`, the four values `x^2+x`, for
  `x=0,1,a,a+1`, are respectively `0,0,1,1`. None equals `a`.
  Thus g has no root in K and is irreducible by the same degree-two
  argument as <1>1. **BY** <1>1 and direct substitution.
  <2>2. Apply the quotient/inverse argument of <1>1.<2>1--<2>2 with
  coefficient field K. Each element has the unique form `u+vb`, giving
  sixteen elements and D1310's coordinate interpretation.
  **BY** D1310, <2>1 and polynomial division.
  <2>3. **QED** <1>2 by <2>1--<2>2.

<1>3. **ASSUME** `(u,v)=u+vb`.
**PROVE** the Frobenius and trace formulas in the claim.
  <2>1. `(u+vb)^2=u^2+v^2(b+a)` gives
  `sigma_E(u,v)=(u^2+a v^2,v^2)`.
  **BY** <1>2's relation and characteristic two.
  <2>2. Square once more. The constant coordinate is
  `u^4+(a^2+a)v^4=u+v`; the b-coordinate is `v^4=v`.
  Here `a^2+a=1` by <1>1 and `x^4=x` in K by FRB-TRACE.
  **BY** <2>1, <1>1 and FRB-TRACE <1>1.
  <2>3. Applying `(u,v)->(u+v,v)` twice gives the identity, but it
  does not fix `(0,1)`. Consequently sigma_E has order exactly four.
  **BY** <2>2.
  <2>4. The degree-two relative trace is `x+x^4`; <2>2 gives
  `(u,v)+(u+v,v)=(v,0)`, hence its transported value is v.
  Trace transitivity gives `Tr_E(u,v)=Tr_K(v)=v+v^2`.
  **BY** D1303, D3, <2>2 and FRB-TRACE.
  <2>5. **QED** <1>3 by <2>1--<2>4.

<1>4. **ASSUME** the embedding `K->E` of D1310.
**PROVE** the code, logical labels and transfer formulas.
  <2>1. The kernel of the relative trace is `{(u,0):u in K}`.
  D1304 then gives `J|u>=|u,0>` and
  `V|v>=(1/2)sum_u |u,v>`; FRB-CODE gives code dimension four.
  **BY** <1>3.<2>4, D1304 and FRB-CODE.
  <2>2. For `k,m in K`, the position `(k,0)` and momentum `(0,m)`
  restrict to logical labels `(k,m)`. Momentums `(m,0)` restrict to
  zero and are precisely the code's phase-stabilizer labels.
  **BY** <1>3.<2>4 and FRB-CODE's logical trace quotient.
  <2>3. The absolute trace fibre over `e in F_2` is
  `{(u,v):u in K, v+v^2=e}`. There are four choices of u and two
  choices of v, by the four-value computation in <1>2.<2>1.
  Its normalized transfer coefficient is therefore `1/sqrt(8)`.
  **BY** D1304, <1>2.<2>1 and <1>3.<2>4.
  <2>4. **QED** <1>4 by <2>1--<2>3.

<1>5. **ASSUME** `U_E^2|u,v>=|u+v,v>`.
**PROVE** its fixed-vector space has dimension ten.
  <2>1. The fixed basis labels have v=0, giving four singleton orbits.
  The remaining twelve labels have orbits of length two because the
  permutation squares to the identity, giving six further orbits.
  **BY** <1>3.<2>2 and <1>2's field cardinality.
  <2>2. A vector is fixed by a basis permutation iff its coefficients
  are constant on each orbit. The orbit sums have disjoint support
  and form a basis of its fixed-vector space.
  Thus its dimension is `4+6=10`, while <1>4 gives code dimension four.
  **BY** D1301, D1302 and <2>1's orbit partition.
  <2>3. **QED** <1>5 and FRB-EXAMPLE by <1>1--<1>5.

The example retains the field multiplication table; replacing it by
coordinatewise addition changes the higher gate. Code support, relative
trace fibres and Frobenius invariant vectors are three different objects.
