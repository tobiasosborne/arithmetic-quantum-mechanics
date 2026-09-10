# Restriction of scalars and the half-form Weyl datum

Lane model: `gpt-5.6-sol`, reasoning `xhigh`.

Prover-pass artifact for the exact canonical SP-TRACE row. Status remains
`SKETCH`. Canonical definitions are D3, D1301, D1303, D1701, D1703 and
D1709; admitted dependencies are FRB-TRACE and SP-WEYL. The relative trace,
surjectivity, tower transitivity and trace-pairing facts are reused from
`theory/sidequests/frobenius-hierarchy/foundation.md` section 1 rather than
reproved.

Fix a finite extension `E/K` of odd-characteristic finite fields, put
`d=[E:K]`, and let `(V,omega_E)` be a finite-dimensional symplectic
`E`-space. Fix a named nontrivial character `chi_K:K->U(1)` and put
`chi_(E/K)=chi_K o Tr_(E/K)` as in D1709.

## 1. The restricted trace form is symplectic in arbitrary rank

**PROVE**

    omega_Res(v,w)=Tr_(E/K)(omega_E(v,w))

is a nondegenerate alternating K-bilinear form on `Res_(E/K)V`.

<1>1. The form is K-bilinear.
**BY** E-bilinearity of `omega_E` and K-linearity of the relative trace,
admitted in FRB-TRACE section 1 `<1>3`.

<1>2. It is alternating because

    omega_Res(v,v)=Tr_(E/K)(omega_E(v,v))=Tr_(E/K)(0)=0.

**BY** D1701 and linearity of trace.

<1>3. **ASSUME** `v!=0`. **PROVE** some `w` has
`omega_Res(v,w)!=0`.

  <2>1. Nondegeneracy of `omega_E` gives `w_0` with
  `c=omega_E(v,w_0)!=0`.
  **BY** D1701.

  <2>2. FRB-TRACE gives `x in E` with `Tr_(E/K)(x)=1`, even when `p`
  divides `d`.
  **BY** the admitted surjectivity in foundation.md section 1
  `<1>2.<2>4`--`<1>3`.

  <2>3. Put `w=(x/c)w_0`. Then E-bilinearity gives

      omega_E(v,w)=x,

  so `omega_Res(v,w)=1`.
  **BY** `<2>1`--`<2>2` and field inversion.

  <2>4. **QED** `<1>3`.

<1>4. Thus the radical is zero.
**BY** `<1>3` for every nonzero vector.

<1>5. If `dim_E V=2n`, then `dim_K Res_(E/K)V=2nd`, so its symplectic rank
is `nd`; this includes `n=0`.
**BY** scalar-restriction dimension and `<1>1`--`<1>4`.

<1>6. **QED** the arbitrary-rank restricted symplectic space.
**BY** `<1>1`--`<1>5` and D1709.

## 2. The named relative character is nontrivial

**PROVE** `chi_(E/K)` is nontrivial without identifying it with the fixed
absolute-trace character `psi_E`.

<1>1. Since `chi_K` is nontrivial, choose `a in K` with `chi_K(a)!=1`.
**BY** the definition of a nontrivial character.

<1>2. Trace surjectivity gives `x in E` with `Tr_(E/K)(x)=a`.
**BY** admitted FRB-TRACE.

<1>3. Then `chi_(E/K)(x)=chi_K(a)!=1`.
**BY** D1709 and `<1>1`--`<1>2`.

<1>4. This argument uses the named `chi_K`. It does not restrict `psi_E` to
K or assume the two characters agree; a nonstandard base character is fully
included.
**BY** D1709's explicit character distinction.

<1>5. **QED** nontriviality of the relative character.
**BY** `<1>1`--`<1>4`.

## 3. Identity of the two half-form star-algebras

Put

    A_E=A_(chi_(E/K),omega_E/2)(V),
    A_K=A_(chi_K,omega_Res/2)(Res_(E/K)V).

The symbols denote D1703's half-form construction over `E` and `K`; both
have the same underlying finite label set `V`. **PROVE** the identity on
labels extends to an exact unital star-isomorphism `A_E->A_K`.

<1>1. Since the characteristic is odd, `1/2` lies in `K`, and K-linearity
of trace gives

    Tr_(E/K)(omega_E(v,w)/2)=omega_Res(v,w)/2.

**BY** D1709 and FRB-TRACE K-linearity.

<1>2. Hence the E-side product multiplier equals the K-side multiplier:

    chi_(E/K)(omega_E(v,w)/2)
      =chi_K(omega_Res(v,w)/2).

**BY** D1709 and `<1>1`.

<1>3. Therefore the label prescription

    W_(omega_E/2)(v) |-> W_(omega_Res/2)(v)

preserves every product.
**BY** D1703's multiplication law and `<1>2`.

<1>4. Both involutions send label `v` to label `-v`, and both units have
label zero.
**BY** D1703.

<1>5. Both labelled Weyl families are complex bases indexed by the same
set, so the prescription is a complex-linear bijection.
**BY** D1703 and the identity of the underlying additive group.

<1>6. The coefficient traces also agree: each selects the coefficient of
the common zero label.
**BY** D1703.

<1>7. Thus the identity label map is an exact unital trace-preserving
star-isomorphism. SP-WEYL supplies its already admitted full-matrix
realizations; no new SvN or irreducibility proof is needed.
**BY** `<1>3`--`<1>6` and admitted SP-WEYL.

<1>8. At `n=0`, each algebra has the sole label zero and is `C`; the map is
the identity.
**BY** D1703's rank-zero convention and `<1>5`.

<1>9. No step applies in characteristic two: the trace form remains
classically defined there, but this half-form comparison uses `1/2`.
**BY** `<1>1` and D1709's Scope.

<1>10. **QED** the half-form star-algebra comparison.
**BY** `<1>1`--`<1>9`.

## 4. Composition along named towers

**ASSUME** a named tower of finite fields `L->K->E` in odd
characteristic and a named nontrivial `chi_L`. Put

    chi_(K/L)=chi_L o Tr_(K/L),
    chi_(E/L)=chi_L o Tr_(E/L).

**PROVE** the one-step and iterated restrictions and half-form comparisons
agree.

<1>1. Admitted FRB-TRACE gives

    Tr_(E/L)=Tr_(K/L) o Tr_(E/K).

**BY** foundation.md section 1 `<1>4`.

<1>2. Hence the direct L-valued form equals the iterated form:

    Tr_(E/L)(omega_E(v,w))
      =Tr_(K/L)(Tr_(E/K)(omega_E(v,w))).

**BY** `<1>1`.

<1>3. The characters agree on every `x in E`:

    chi_(E/L)(x)=chi_(K/L)(Tr_(E/K)(x)).

**BY** the definitions and `<1>1`.

<1>4. Applying section 3 first from E to K and then K to L therefore gives
the same multiplier, star, unit and coefficient trace as the direct E-to-L
comparison.
**BY** `<1>2`--`<1>3` and section 3.

<1>5. All three label maps are the identity on the underlying additive set,
so the composite is literally the direct identity map after the canonical
scalar-restriction association.
**BY** section 3 `<1>5` and ordinary restriction of scalar actions.

<1>6. This tower statement concerns characters induced compatibly from
`chi_L`; an unrelated named `chi_K` is not silently identified with
`chi_(K/L)`.
**BY** D1709's named-character convention.

<1>7. The proof uses trace surjectivity, not multiplication by the extension
degree, so it includes towers whose degrees are divisible by `p`.
**BY** section 1 `<1>3` and admitted FRB-TRACE.

<1>8. **QED** tower composition.
**BY** `<1>1`--`<1>7`.

## 5. Exact canonical conclusion

<1>1. The restricted trace form is symplectic in every finite rank and the
relative named character is nontrivial.
**BY** sections 1--2.

<1>2. The identity label map gives the exact odd-characteristic half-form
star-algebra comparison, including rank zero.
**BY** section 3.

<1>3. Compatible comparisons compose along named towers.
**BY** section 4.

<1>4. This is restriction of scalars with a trace form, not uncorrected
subfield inclusion or a subsystem decoder.
**BY** D1709's Scope and the constructions above.

<1>5. **QED** the exact canonical SP-TRACE statement.
**BY** `<1>1`--`<1>4`, D3, D1301, D1303, D1701, D1703, D1709,
FRB-TRACE and SP-WEYL at their stated scopes.
