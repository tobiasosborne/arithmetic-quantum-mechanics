# Symmetric Fock functor and normalized exponential law

Lane model: `gpt-5.6-sol`, reasoning `xhigh`.

SP-FOCK is `PROVED` through
`theory/verdicts/phantasm-completions-adjudication.md`. Canonical definitions are D1010 and D1708. SP-DER06
`derezinski.tex` 1814--2090 is the registered primary comparison. The proof
supplies the boundedness and completion arguments rather than assigning them
to finite probes.

## 1. Symmetric sectors and bounded second quantization

**ASSUME** a complex Hilbert space `H` and `r>=0`. **PROVE** D1708's `P_r`
is the orthogonal projection onto symmetric tensors.

<1>1. The permutation operators satisfy

    U_pi U_sigma=U_(pi sigma),  U_pi^*=U_(pi^(-1)).

**BY** D1708's inverse-index action evaluated on pure tensors, which span
the Hilbert tensor product.

<1>2. Taking adjoints in the finite average and reindexing inverses gives
`P_r^*=P_r`.
**BY** `<1>1` and bijectivity of inversion in `S_r`.

<1>3. Multiplying two averages gives

    P_r^2=(r!)^(-2)sum_(pi,sigma)U_(pi sigma)=P_r,

because each product permutation occurs exactly `r!` times.
**BY** `<1>1` and finite group counting.

<1>4. Thus `P_r` is an orthogonal projection. Its range is exactly the
vectors fixed by all permutations.
**BY** a self-adjoint idempotent is an orthogonal projection; averages are
fixed, and if every `U_pi xi=xi`, then `P_r xi=xi`.

<1>5. At `r=0`, the group and tensor are trivial and `P_0=1_C`.
**BY** D1708's zero-sector convention.

<1>6. **QED** the sector projection.
**BY** `<1>1`--`<1>5`.

**ASSUME** a contraction `T:H->K`. **PROVE** D1708's `Gamma_s(T)` is a
bounded functorial map of norm one.

<1>7. On pure tensors,

    T^tensor-r U_pi=U_pi T^tensor-r,

so `T^tensor-r P_r^H=P_r^K T^tensor-r` and symmetric sectors map to
symmetric sectors.
**BY** each route applies `T` to every permuted factor.

<1>8. The tensor norm satisfies `||T^tensor-r||<=||T||^r<=1`.
**BY** first on pure tensors and finite sums by the Hilbert tensor norm;
iterate the standard bound `||A tensor B||<=||A||||B||`.

<1>9. For `xi=(xi_r)_r` in the Hilbert direct sum,

    ||Gamma_s(T)xi||^2
      =sum_r||T^tensor-r xi_r||^2<=sum_r||xi_r||^2.

**BY** `<1>8` and monotone convergence of nonnegative partial sums.

<1>10. Hence the sectorwise algebraic prescription extends to a bounded
operator of norm at most one. The vacuum sector is identity, so its norm is
exactly one.
**BY** `<1>9` and D1708's `T^tensor-0=1_C` convention.

<1>11. Sectorwise,

    Gamma_s(1_H)=1,  Gamma_s(S)Gamma_s(T)=Gamma_s(ST)

for composable contractions; equality extends to the Hilbert sums.
**BY** tensor powers preserve identities/composition and bounded operators
agree when they agree on the dense finite-particle subspace.

<1>12. Thus `Gamma_s` is a functor from complex Hilbert spaces and
contractions to bounded Hilbert-space maps.
**BY** `<1>7`--`<1>11`.

<1>13. The contraction boundary is sharp for the prescribed direct sum. If
`||T||>1`, choose unit vectors `h` with `||Th||` arbitrarily close to
`||T||`; the symmetric unit tensor `h^tensor-r` has image norm
`||Th||^r`, so the sector norms are unbounded in `r`.
**BY** the definition of operator norm and multiplicativity of pure-tensor
norms.

<1>14. **QED** bounded functorial second quantization, with no expansive-map
extension.
**BY** `<1>7`--`<1>13`.

## 2. Shuffle norm for the homogeneous exponential map

**ASSUME** Hilbert spaces `H,K`, integers `n,m>=0`, `r=n+m`, and homogeneous
vectors `xi in Sym^n H`, `eta in Sym^m K`. Let

    x=(jmath_H^tensor-n xi) tensor (jmath_K^tensor-m eta)

in `(H+K)^tensor-r`. **PROVE**

    ||P_r^(H+K)x||^2=(n!m!/r!)||xi||^2||eta||^2.

<1>1. Let `Sh(n,m)` be the permutations preserving the relative order of
the first `n` and last `m` slots. It has `r!/(n!m!)` elements and supplies
one representative for each coset of `S_n times S_m` in `S_r`.
**BY** choose the `n` positions occupied by H; the remaining positions are
K positions.

<1>2. Since `xi,eta` are symmetric, every permutation in one such coset has
the same action on `x`. Therefore

    P_r x=(n!m!/r!)sum_(sigma in Sh(n,m))U_sigma x.

**BY** D1708's group average and `<1>1`.

<1>3. Distinct shuffle tensors in `<1>2` lie in orthogonal tensor-product
summands: at some slot one has an H vector and the other a K vector inside
the orthogonal sum `H+K`.
**BY** the tensor inner product is the product of slot inner products.

<1>4. Each shuffle is unitary and
`||x||=||xi||||eta||`.
**BY** D1708 and Hilbert tensor norms.

<1>5. Taking the squared norm in `<1>2` and using `<1>3`--`<1>4` gives

    (n!m!/r!)^2 (r!/(n!m!))||xi||^2||eta||^2,

which simplifies to the claimed formula.
**BY** finite orthogonal Pythagoras and arithmetic.

<1>6. Multiplication by D1708's positive factor
`sqrt(r!/(n!m!))` therefore preserves the homogeneous tensor norm.
**BY** `<1>5`.

<1>7. The cases `n=0` or `m=0` have one shuffle and factor one, agreeing
with the prescribed unit identification; `n=m=0` maps vacuum to vacuum.
**BY** D1708 and `<1>1`--`<1>6`.

<1>8. **QED** the exact factorial normalization.
**BY** `<1>1`--`<1>7`.

## 3. Unitary extension and exhaustion of every sector

**PROVE** `Exp^(alg)_(H,K)` is a well-defined isometry with dense range and
extends uniquely to a unitary

    Exp_(H,K):Gamma_s(H) tensor Gamma_s(K)->Gamma_s(H+K).

<1>1. The algebraic tensor domain is the algebraic direct sum of mutually
orthogonal bidegree spaces `Sym^n H tensor Sym^m K`.
**BY** distributivity of algebraic tensor over finite-support direct sums
and orthogonality of Fock sectors.

<1>2. Images of different bidegrees are orthogonal: different total degrees
lie in different Fock sectors, and for fixed total degree different H-slot
occupations lie in orthogonal summands before symmetrization and remain
orthogonal after the occupation-number projection.
**BY** the orthogonal decomposition by the number of H factors, as in
section 2 `<1>3`.

<1>3. Section 2 shows the map preserves norms on each bidegree, so `<1>1`
and `<1>2` make the complex-linear algebraic map an isometry.
**BY** section 2 `<1>6`.

<1>4. **PROVE** its range exhausts `Sym^r(H+K)` for every `r`.

  <2>1. Symmetrized pure tensors
  `P_r(v_1 tensor ... tensor v_r)`, `v_i in H+K`, span a dense subspace of
  `Sym^r(H+K)`.
  **BY** pure tensors span the Hilbert tensor product and `P_r` is a bounded
  projection by section 1.

  <2>2. Write each `v_i=jmath_H h_i+jmath_K k_i` and expand. Group terms by
  the subset of H choices; symmetrization turns every group with `n` H
  choices into the image of a tensor from `Sym^n H tensor Sym^(r-n)K`, up to
  D1708's nonzero normalization.
  **BY** finite multilinear expansion, internal symmetrization, and the
  shuffle formula of section 2.

  <2>3. The homogeneous isometry of section 2 first defined on
  `Sym^n H odot Sym^m K` extends to the completed Hilbert tensor
  `Sym^n H tensor Sym^m K`. Its image is closed. The finitely many completed
  bidegree images at total degree `r` are orthogonal, so their sum is closed.
  **BY** preservation of Cauchy distances, completeness of the Hilbert
  tensor product, and sections 2--3 `<1>3`.

  <2>4. The expansion in `<2>2` makes the symmetrized pure tensors dense in
  this closed sum, so the completed bidegree images exhaust the whole sector.
  **BY** `<2>1`--`<2>3`.

  <2>5. **QED** `<1>4`.

<1>5. The original algebraic range is dense in each completed bidegree
image, and finite sector sums are dense in Fock space. It is therefore dense
in `Gamma_s(H+K)`.
**BY** `<1>4`, density of algebraic tensor products in Hilbert tensor
products, and the definition of Hilbert direct sum.

<1>6. An isometry on a dense subspace extends uniquely by Cauchy limits to
an isometry on the Hilbert completion.
**BY** if `x_n` is Cauchy, its images are Cauchy with the same distances;
independence of approximating sequence follows similarly.

<1>7. The extended range is closed, while `<1>5` makes it dense; hence it
is onto and the extension `Exp_(H,K)` is unitary.
**BY** an isometry has closed range and a closed dense subspace is whole.

<1>8. Its adjoint is the unitary comparison in the canonical claim's
direction `Gamma_s(H+K)->Gamma_s(H) tensor Gamma_s(K)`.
**BY** D1708 and `<1>7`.

<1>9. **QED** unitary extension and vacuum/zero-unit clauses.
**BY** `<1>3`--`<1>8` and section 2 `<1>7`.

## 4. Naturality for contractions

**ASSUME** contractions `S:H->H'`, `T:K->K'`. **PROVE**

    Exp_(H',K') (Gamma_s(S) tensor Gamma_s(T))
      =Gamma_s(S+T) Exp_(H,K).

<1>1. On bidegree `(n,m)`, `(S+T)^tensor-(n+m)` commutes with the
permutation average and satisfies

    (S+T)jmath_H=jmath_(H')S,
    (S+T)jmath_K=jmath_(K')T.

**BY** direct evaluation on vectors and section 1 `<1>7`.

<1>2. Applying `<1>1` to D1708's homogeneous formula shows the two routes
agree, including the identical positive factorial scalar.
**BY** D1708 and `<1>1`.

<1>3. By linearity they agree on the algebraic tensor of finite-particle
spaces.
**BY** finite bidegree decomposition.

<1>4. All maps are bounded: the exponential maps are unitary and second
quantizations of contractions have norm one.
**BY** sections 1 and 3.

<1>5. Equality on the dense algebraic domain extends to the completions.
**BY** continuity and `<1>3`--`<1>4`.

<1>6. Multiplying `<1>5` on the left by `Exp_(H',K')^*` and on the right
by `Exp_(H,K)^*` gives the covariant naturality square in the claim's
opposite comparison direction:

    (Gamma_s(S) tensor Gamma_s(T)) Exp_(H,K)^*
      =Exp_(H',K')^* Gamma_s(S+T).

**BY** section 3 unitarity and `<1>5`.

<1>7. No associativity, symmetry coherence, or strong-monoidal theorem is
asserted beyond this two-variable natural square.
**BY** the exact SP-FOCK statement and D1708 Scope.

<1>8. **QED** naturality.
**BY** `<1>1`--`<1>7`.

## 5. Zero and one modes

**PROVE** `Gamma_s(0)=C` and identify the one-mode completion and particle
number exactly as claimed.

<1>1. For the zero Hilbert space, `Sym^0(0)=C` and
`Sym^r(0)=0` for every `r>0`; hence its Hilbert direct sum is `C` with vacuum
one.
**BY** D1708 and the zero tensor powers.

<1>2. Let `e=1` be the standard unit vector of `C`. Each
`Sym^r(C)` is one-dimensional with unit vector `e^tensor-r`.
**BY** every permutation fixes the pure tensor and `C^tensor-r` is
one-dimensional.

<1>3. D1010 gives

    <x^m,x^n>=[m=n]n!,

so `f_r=x^r/sqrt(r!)` is an orthonormal basis of `F_alg`.
**BY** D1010 and the positive square root.

<1>4. The map `f_r |-> e^tensor-r` is an isometry from `F_alg` onto the
one-mode finite-particle space and extends uniquely to a unitary
`F_bos->Gamma_s(C)`.
**BY** `<1>2`--`<1>3` and completion of an orthonormal-basis map.

<1>5. Sending `e^tensor-r` to the standard basis vector `delta_r` gives
`Gamma_s(C) ~= l2(N_0)`.
**BY** the Hilbert direct sum of the one-dimensional sectors.

<1>6. D1708's `N_C` sends `e^tensor-r` to `r e^tensor-r` and has domain

    {sum_r c_r e^tensor-r : sum_r r^2|c_r|^2<infinity}.

**BY** the prescribed particle-number formula.

<1>7. Under `<1>4`--`<1>5`, particle number is diagonal with eigenvalue `r`
on `f_r` and `delta_r`, with the same domain.
**BY** `<1>6`.

<1>8. No Hall multiplication, creation/annihilation claim, or older
F1-HALL sketch is promoted.
**BY** D1010 and the exact SP-FOCK scope.

<1>9. **QED** zero/one-mode and number-operator clauses.
**BY** `<1>1`--`<1>8`.

## 6. Exact canonical conclusion

<1>1. Symmetric second quantization is a bounded functor on contractions.
**BY** section 1.

<1>2. The normalized exponential map extends unitarily and is natural; its
adjoint has the claim's displayed direction.
**BY** sections 2--4.

<1>3. The zero and one-mode identifications and particle-number action hold.
**BY** section 5.

<1>4. **QED** the exact canonical SP-FOCK statement.
**BY** `<1>1`--`<1>3`, D1010, D1708 and SP-DER06 at its registered scope.
