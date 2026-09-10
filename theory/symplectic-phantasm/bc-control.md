# Represented Bost--Connes control: semigroup, flow, and Gibbs trace

Lane model: `gpt-5.6-sol`, reasoning `xhigh`.

SP-BC-CONTROL is `PROVED` through
`theory/verdicts/phantasm-completions-adjudication.md`. Canonical definitions are D1712--D1713. SP-CM04
`houcheschapter1final7.tex` 1763--1783 and SP-CM08 `paper.txt`
23015--23025, 23106--23114, 23930--23947 are the registered primary
comparisons. The proof concerns the concrete represented algebra only and
does not assert faithfulness of a universal presentation.

Write `H=l2(N_(>0))`, with basis `delta_m`, and use D1712's operators.

## 1. Semigroup isometries and their adjoints

**PROVE** `mu_m mu_n=mu_(mn)` and `mu_n^*mu_n=1`.

<1>1. On a basis vector,

    mu_m mu_n delta_k=mu_m delta_(nk)=delta_(mnk)=mu_(mn)delta_k.

**BY** D1712.

<1>2. Equality on the orthonormal basis gives
`mu_m mu_n=mu_(mn)`; in particular the isometries commute.
**BY** `<1>1` and bounded linearity.

<1>3. The adjoint is

    mu_n^*delta_k = delta_(k/n) if n divides k, and 0 otherwise.

**BY** its coefficient at `delta_j` is
`<mu_n delta_j,delta_k>=[nj=k]`.

<1>4. Hence `mu_n^*mu_n delta_k=delta_k` for every k.
**BY** `<1>3`.

<1>5. Thus `mu_n^*mu_n=1`. For `n>1`, `mu_nmu_n^*delta_1=0`, so `mu_n` is
not unitary.
**BY** `<1>3`--`<1>4`.

<1>6. **QED** the semigroup/isometry clauses.
**BY** `<1>1`--`<1>5`.

## 2. Diagonal arithmetic relations and the root average

**ASSUME** `r in Q/Z`, represented by a real rational modulo one.
**PROVE**

    mu_n^*e(r)mu_n=e(nr),
    mu_n e(r)mu_n^*=(1/n)sum_(ns=r)e(s).

<1>1. On `delta_k`,

    mu_n^*e(r)mu_n delta_k
      =exp(2 pi i nkr)delta_k=e(nr)delta_k.

**BY** D1712 and section 1 `<1>3`.

<1>2. Equality on the basis proves the first identity.
**BY** `<1>1`.

<1>3. The left side of the second identity acts on `delta_k` by zero if
`n` does not divide k and, if `k=nj`, by

    exp(2 pi i jr)delta_k.

**BY** section 1 `<1>3` and D1712's diagonal `e(r)`.

<1>4. The n solutions of `ns=r` in `Q/Z` are

    s_h=(r+h)/n,  h=0,...,n-1.

**BY** multiplication by n on `Q/Z` has kernel represented by `h/n`, and
every displayed element maps to r.

<1>5. The coefficient of the right side on `delta_k` is

    exp(2 pi i kr/n) (1/n)sum_(h=0)^(n-1)exp(2 pi i kh/n).

**BY** D1712 and `<1>4`.

<1>6. The finite root average is one if `n` divides k and zero otherwise.
**BY** if the ratio is one all terms are one; otherwise the geometric sum
has numerator `1-exp(2 pi i k)=0` and nonzero denominator.

<1>7. When `k=nj`, `<1>5` becomes `exp(2 pi i jr)`; otherwise it is zero.
This agrees with `<1>3`.
**BY** `<1>5`--`<1>6`.

<1>8. Equality on the basis proves the corner-average identity, including
the factor `1/n`.
**BY** `<1>3`--`<1>7`.

<1>9. **QED** both arithmetic conjugation formulas.
**BY** `<1>2` and `<1>8`.

## 3. Corner endomorphism and unital CP transfer

Fix n and write proof-locally `q_n=mu_nmu_n^*`. **PROVE** `nu_n` is a
star-isomorphism from `A_BC^rep` onto the corner
`q_n A_BC^rep q_n`, and `L_n` is a unital completely positive self-map of
the represented algebra.

<1>1. Since `mu_n` belongs to the represented C-star algebra, both

    nu_n(a)=mu_n a mu_n^*,  L_n(a)=mu_n^*a mu_n

belong to that algebra for every `a`.
**BY** D1712 and closure under multiplication/star/norm limits.

<1>2. One has `q_n=q_n^*=q_n^2` and
`nu_n(a)=q_n nu_n(a)q_n`.
**BY** section 1 `mu_n^*mu_n=1`.

<1>3. For `a,b` in the algebra,

    nu_n(a)nu_n(b)=mu_n a(mu_n^*mu_n)bmu_n^*=nu_n(ab),
    nu_n(a)^*=nu_n(a^*).

**BY** section 1 and the adjoint law.

<1>4. `nu_n` is injective because `L_n(nu_n(a))=a`.
**BY** `mu_n^*mu_n=1`.

<1>5. If `x=q_n a q_n` lies in the corner, then

    x=nu_n(L_n(a)).

Thus `nu_n` is onto the corner, whose unit is `q_n`.
**BY** expand using `q_n=mu_nmu_n^*` and `mu_n^*mu_n=1`.

<1>6. Hence `nu_n` is the claimed corner star-endomorphism/isomorphism; it
is not unital as a map to the ambient algebra when `n>1`.
**BY** `<1>2`--`<1>5` and section 1 `<1>5`.

<1>7. The map `L_n` is unital because `L_n(1)=mu_n^*mu_n=1`.
**BY** section 1.

<1>8. For every auxiliary finite-dimensional space and positive `R`,

    (1 tensor L_n)(R)=(1 tensor mu_n)^*R(1 tensor mu_n)>=0.

Thus `L_n` is completely positive.
**BY** the quadratic-form positivity of conjugation, at every amplification.

<1>9. Nothing here makes `L_n` multiplicative: the proof used only its
one-Kraus form and unitality.
**BY** `<1>7`--`<1>8` and the exact canonical statement.

<1>10. **QED** the corner and CP-map clauses.
**BY** `<1>1`--`<1>9`.

## 4. Self-adjoint logarithmic energy on its maximal domain

**PROVE** D1712's diagonal operator

    H_log delta_m=(log m)delta_m

is self-adjoint on
`D={xi:sum_m(log m)^2|xi_m|^2<infinity}`.

<1>1. The finite-support sequences lie in D and are dense in H.
**BY** their truncations converge in `l2`.

<1>2. For `xi,eta in D`, absolute Cauchy--Schwarz gives

    <H_log xi,eta>=<xi,H_log eta>,

so the operator is symmetric.
**BY** the multipliers `log m` are real and both weighted sequences lie in
`l2`.

<1>3. If `eta` lies in the adjoint domain, there is `zeta in H` with
`<H_log xi,eta>=<xi,zeta>` for all `xi in D`. Taking `xi=delta_m` gives

    zeta_m=(log m)eta_m.

**BY** the definition of the adjoint and `<1>1`.

<1>4. Since `zeta in l2`, the equality in `<1>3` says exactly that
`eta in D`, and then `H_log^*eta=H_log eta`.
**BY** D1712's weighted-square domain.

<1>5. Conversely symmetry gives `D subset Dom(H_log^*)`; hence the two
domains and actions agree.
**BY** `<1>2`--`<1>4`.

<1>6. **QED** self-adjointness on the stated maximal multiplication domain.
**BY** `<1>1`--`<1>5`.

## 5. Invariant point-norm continuous dynamics

Put `V_u=exp(iuH_log)`. **PROVE** `sigma_u=Ad(V_u)` restricts to a
point-norm continuous automorphism group of `A_BC^rep` and has the stated
generator action.

<1>1. Diagonal functional calculus gives

    V_u delta_m=m^(iu)delta_m,

so every `V_u` is unitary, `V_(u+v)=V_uV_v`, and `V_0=1`.
**BY** section 4 and exponentials of the real eigenvalues `log m`.

<1>2. Direct basis calculation gives

    V_u mu_n V_u^*=n^(iu)mu_n,
    V_u e(r)V_u^*=e(r).

**BY** D1712: the first coefficient is `(nm)^(iu)m^(-iu)=n^(iu)` and the
second pair of diagonal operators commute.

<1>3. Therefore conjugation maps the star-algebra generated algebraically by
the `mu_n,e(r)` into itself. Replacing u by -u gives the inverse.
**BY** `<1>2`, scalar closure, products and adjoints.

<1>4. Since conjugation is isometric, it extends from the generator
star-algebra to an automorphism of its norm closure `A_BC^rep`.
**BY** approximate in norm and use `||V_u a V_u^*||=||a||`.

<1>5. The group law is exact on the represented algebra.
**BY** `<1>1` and uniqueness of the norm-continuous extension.

<1>6. For an algebraic polynomial `b` in finitely many generators,
`u |-> sigma_u(b)` is norm-continuous because it is a finite sum of products
whose scalar coefficients are finite products of functions `n^(iu)`.
**BY** `<1>2` and continuity of the complex exponential.

<1>7. For arbitrary `a` and a polynomial `b`,

    ||sigma_u(a)-sigma_v(a)||
      <=2||a-b||+||sigma_u(b)-sigma_v(b)||.

**BY** add/subtract the two images of b and use isometry.

<1>8. First choose b close to a and then u close to v; `<1>6`--`<1>7`
prove point-norm continuity.
**BY** the epsilon argument in the displayed bound.

<1>9. **QED** invariant point-norm dynamics and the exact formulas
`sigma_u(mu_n)=n^(iu)mu_n`, `sigma_u(e(r))=e(r)`.
**BY** `<1>1`--`<1>8`.

## 6. Trace-class Gibbs operator and zeta partition sum

**ASSUME** real `b>1`. **PROVE** `exp(-bH_log)` is trace class with trace
`zeta(b)` and D1712's `rho_(BC,b)` is a density.

<1>1. Diagonal functional calculus gives

    exp(-bH_log)delta_m=m^(-b)delta_m.

**BY** section 4 and `exp(-b log m)=m^(-b)`.

<1>2. The positive decreasing function `x^(-b)` satisfies

    sum_(m=1)^N m^(-b)
      <=1+integral_1^N x^(-b)dx
      <=1+1/(b-1).

**BY** compare each term for `m>=2` with the integral over `[m-1,m]` and
evaluate the elementary antiderivative.

<1>3. Thus `sum_m m^(-b)` converges. The positive diagonal operator in
`<1>1` is trace class and its trace is this sum.
**BY** a positive diagonal operator is trace class exactly when the sum of
its diagonal eigenvalues is finite; finite-rank truncations increase to it in
trace norm with tail equal to the remaining sum.

<1>4. D1712 names the convergent sum `Z_BC(b)=zeta(b)`, so

    Tr(exp(-bH_log))=zeta(b).

**BY** D1712 and `<1>3`.

<1>5. The operator is positive and nonzero; division by its positive finite
trace gives `rho_(BC,b)>=0` and `Tr(rho_(BC,b))=1`.
**BY** `<1>1`--`<1>4`.

<1>6. The proof does not include `b=1`, where the harmonic partial sums are
unbounded, and makes no statement about zeta zeros.
**BY** the hypothesis `b>1` and the positive real series only.

<1>7. **QED** the Gibbs/partition clauses.
**BY** `<1>1`--`<1>6`.

## 7. Exact canonical conclusion

<1>1. The represented semigroup, adjoint and arithmetic conjugation
identities hold exactly.
**BY** sections 1--2.

<1>2. `nu_n` is the corner star-endomorphism/isomorphism and `L_n` is UCP.
**BY** section 3.

<1>3. `H_log` is self-adjoint on its stated domain and implements the
point-norm continuous invariant flow.
**BY** sections 4--5.

<1>4. For `b>1`, the Gibbs operator is trace class with zeta trace and the
prescribed density has trace one.
**BY** section 6.

<1>5. No universal faithfulness, KMS classification, factor type,
modular-flow equality, Frobenius comparison, global system or zero-spectrum
claim has been made.
**BY** D1712--D1713 Scopes and the proof's hypotheses.

<1>6. **QED** the exact canonical SP-BC-CONTROL statement.
**BY** `<1>1`--`<1>5`, D1712--D1713 and the registered BC sources at the
stated represented scope.

