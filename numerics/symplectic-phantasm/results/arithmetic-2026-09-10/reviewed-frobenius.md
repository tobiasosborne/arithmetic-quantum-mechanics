# Relative Frobenius covariance in the trace-form Weyl model

Lane model: `gpt-5.6-sol`, reasoning `xhigh`.

Prover-pass artifact for the exact canonical SP-FROB row. Status remains
`SKETCH`; SP-TRACE is an explicit unpromoted dependency during drafting.
Canonical definitions are D1301--D1303, D1703, D1706 and D1709. Admitted
FRB-FROB supplies the absolute p-power basis permutation and reference Weyl
covariance; FRB-TRACE supplies trace formulas; SP-CP supplies only
unitary-conjugation channel typing.

Fix an odd-characteristic extension `E/K`, write `q=|K|=p^s` and
`d=[E:K]`, and fix a named nontrivial `chi_K`. Put

    sigma(x)=x^q,
    chi=chi_(E/K)=chi_K o Tr_(E/K).

On `E^n+E^n`, apply `sigma` coordinatewise.

## 1. The relative power is K-linear and trace-form symplectic

**PROVE** `sigma` is a K-linear field automorphism, its `d`th power is
identity, and the coordinatewise phase-space map is symplectic for the
restricted trace form.

<1>1. The q-power map preserves sums, products and one.
**BY** FRB-TRACE foundation.md section 1 `<1>2.<2>1` for p-powers,
iterated `s` times, and ordinary field multiplication.

<1>2. It is injective because `sigma(x)=sigma(y)` implies
`(x-y)^q=0`, hence `x=y`; finiteness makes it bijective.
**BY** the field has no nonzero nilpotents and is finite.

<1>3. Every `a in K` satisfies `a^q=a`, so
`sigma(ax+by)=a sigma(x)+b sigma(y)` for `a,b in K`.
**BY** the finite-field power identity admitted in FRB-TRACE and `<1>1`.

<1>4. Since `|E|=q^d`, every `x in E` satisfies `x^(q^d)=x`. Thus
`sigma^d=1_E`.
**BY** FRB-TRACE section 1 `<1>1`.

<1>5. No exact minimal period is needed; the canonical statement and Scope
allow a smaller period.
**BY** the SP-FROB Scope.

<1>6. The relative trace is the conjugate sum

    Tr_(E/K)(x)=sum_(r=0)^(d-1) sigma^r(x).

Applying `sigma` cyclically permutes the terms, so
`Tr_(E/K)(sigma(x))=Tr_(E/K)(x)`.
**BY** D1303, `<1>4`, and admitted FRB-TRACE.

<1>7. For phase labels `(a,b),(a',b')`,

    omega_E((sigma a,sigma b),(sigma a',sigma b'))
      =sigma(omega_E((a,b),(a',b'))).

**BY** the standard dot-product form and multiplicativity/additivity of
`sigma`, coordinate by coordinate.

<1>8. Taking relative trace and using `<1>6` gives preservation of
`omega_Res`; combined with K-linearity and bijectivity, the phase-space map
is K-linear symplectic.
**BY** `<1>2`--`<1>3`, `<1>6`--`<1>7`, and SP-TRACE's trace form.

<1>9. At `n=0`, the phase space is zero and the map is its identity.
**BY** D1703 and D1709's empty conventions.

<1>10. **QED** the classical relative Frobenius clauses.
**BY** `<1>1`--`<1>9`.

## 2. Invariance of every named relative character

**PROVE** `chi(sigma(x))=chi(x)` for every `x in E`.

<1>1. By definition,

    chi(sigma(x))=chi_K(Tr_(E/K)(sigma(x))).

**BY** D1709.

<1>2. Trace invariance from section 1 turns this into
`chi_K(Tr_(E/K)(x))=chi(x)`.
**BY** section 1 `<1>6` and D1709.

<1>3. This uses no equality with the fixed absolute character `psi_E` and
includes nonstandard choices of `chi_K`.
**BY** D1709's character distinction.

<1>4. It also does not assert that an arbitrary K-character is invariant
under the one-step absolute p-power action on K. The relative q-power fixes K
pointwise and cyclically preserves the relative trace.
**BY** section 1 `<1>3` and `<1>6`.

<1>5. **QED** named relative-character invariance.
**BY** `<1>1`--`<1>4`.

## 3. Exact symmetrized Weyl covariance in every rank

Let `U=U_(E/K,n)=(U_E^s)^tensor n` on `l2(E^n)`, so

    U delta_y=delta_(sigma y).

**PROVE**

    U W^s_(E,n)(a,b) U^*=W^s_(E,n)(sigma a,sigma b)

for the trace-form datum with character `chi`.

<1>1. The map `y |-> sigma y` is a bijection of `E^n`, so `U` is unitary
and `U^*delta_y=delta_(sigma^(-1)y)`.
**BY** section 1 `<1>2` and orthonormality of the computational basis.

<1>2. D1703's symmetrized operator acts on basis vectors by

    W^s(a,b)delta_y
      =chi(-b dot y-a dot b/2)delta_(y+a).

**BY** D1703's wavefunction formula evaluated at the output coordinate,
with its named character replaced by `chi`.

<1>3. Applying the left side to `delta_y` gives output
`delta_(y+sigma a)` with phase

    chi(-b dot sigma^(-1)y-a dot b/2).

**BY** `<1>1`--`<1>2` and coordinatewise action of `sigma`.

<1>4. Character invariance permits applying `sigma` to the phase argument;
because `sigma` preserves sums, products, dot products and `1/2`, the phase
in `<1>3` equals

    chi(-(sigma b) dot y-(sigma a) dot (sigma b)/2).

**BY** section 2, section 1 `<1>1`, and odd characteristic.

<1>5. This is exactly the action of
`W^s(sigma a,sigma b)` on `delta_y`.
**BY** `<1>2` and `<1>4`.

<1>6. Equality on the computational basis proves the covariance identity.
Both phase coordinates are transformed.
**BY** `<1>3`--`<1>5`.

<1>7. D1709's equality `sigma=sigma_E^s` and its tensor prescription make
the displayed `U` exactly `(U_E^s)^tensor n`, reusing the absolute
permutation of FRB-FROB without conflating its character.
**BY** D1302, D1709 and admitted FRB-FROB section 2.

<1>8. At `n=0`, `l2(E^0)=C`, `U=1_C`, and the sole Weyl operator is the
identity, so the formula is literal identity.
**BY** D1703 and D1709.

<1>9. The calculation uses `1/2` and asserts no characteristic-two
half-form covariance.
**BY** `<1>4` and D1709's Scope.

<1>10. **QED** exact arbitrary-rank Weyl covariance.
**BY** `<1>1`--`<1>9`.

## 4. The induced invertible state channel

Define `Ad_U(rho)=U rho U^*`. **PROVE** it is an invertible channel and its
`d`th power is identity.

<1>1. The single Kraus operator `U` obeys `U^*U=1`, so admitted SP-CP makes
`Ad_U` completely positive and ordinary-trace preserving.
**BY** SP-CP's Kraus/channel criterion and section 3 `<1>1`.

<1>2. Thus `Ad_U` is a D1706 channel. This is the sole use of SP-CP.
**BY** D1706 and `<1>1`.

<1>3. Its inverse is `Ad_(U^*)`, since both composites are conjugation by
the identity.
**BY** unitarity and associativity of matrix multiplication.

<1>4. Section 1 `<1>4` gives `U^d=1` on every basis vector, hence

    (Ad_U)^d=Ad_(U^d)=1.

**BY** D1709's tensor action and direct conjugation.

<1>5. At rank zero this channel and its inverse are the identity on `C`.
**BY** section 3 `<1>8`.

<1>6. No partial trace, subsystem projection or non-bijective Frobenius map
appears.
**BY** `<1>1`--`<1>4` and D1709's Scope.

<1>7. **QED** the invertible-channel clauses.
**BY** `<1>1`--`<1>6`.

## 5. Exact canonical conclusion

<1>1. Coordinatewise q-power Frobenius is K-linear symplectic for the
SP-TRACE form and preserves every named relative character.
**BY** sections 1--2 and the explicit SP-TRACE dependency.

<1>2. Its specified tensor permutation implements exact symmetrized Weyl
covariance in every rank, including zero.
**BY** section 3.

<1>3. Its state conjugation is an invertible channel whose `d`th power is
identity.
**BY** section 4 and admitted SP-CP.

<1>4. **QED** the exact canonical SP-FROB statement.
**BY** `<1>1`--`<1>3`, D1301--D1303, D1703, D1706, D1709, FRB-FROB,
FRB-TRACE, SP-WEYL, SP-EGOROV, SP-TRACE and SP-CP at their stated scopes.
