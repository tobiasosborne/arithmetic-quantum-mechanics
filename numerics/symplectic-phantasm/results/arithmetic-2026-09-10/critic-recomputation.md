# Independent recomputation — arithmetic interfaces

Date: 2026-09-10. Model: `gpt-5.6-sol`, reasoning `xhigh`.

## Restriction of scalars

For nonzero `v`, the E-linear functional `w -> omega_E(v,w)` is nonzero and
therefore onto E. Since the trace of a finite separable extension is a nonzero
K-linear functional, it is onto K. Choose `w` whose E-pairing with `v` has
trace one. This proves directly that `Tr_(E/K) omega_E` has zero radical.
Alternation and K-bilinearity commute with trace.

For the degree-three extension F27/F3, independent table calculations gave

    |Tr^-1(0)|=|Tr^-1(1)|=|Tr^-1(2)|=9,
    Tr(1)=0,  Tr(element 6)=1.

Restricted symplectic Gram matrices in E-ranks 0, 1, 2 have sizes and ranks
`(0,0),(6,6),(12,12)`. Thus the degree-equals-characteristic case explicitly
rejects `Tr(x)=3x`.

Surjectivity also gives a preimage of any `a` on which the named nontrivial
`chi_K` is nonunit, proving `chi_K o Tr` nontrivial. In odd characteristic,
K-linearity gives

    Tr(omega_E(v,w)/2)=Tr(omega_E(v,w))/2.

The two half-form multipliers are therefore identical on the common label
set. Negation, zero, and the coefficient-at-zero trace are also identical, so
the label identity is the exact star-isomorphism.

For `L subset K subset E`, the comparison is composable precisely when the
K-character is `chi_L o Tr_(K/L)`. Then
`Tr_(E/L)=Tr_(K/L)Tr_(E/K)` identifies forms, characters, multipliers, and the
underlying identity map. An unrelated K-character gives differently typed
intermediate Weyl data and is not covered.

As the characteristic-two boundary, F4/F2 has trace values `[0,0,1,1]` in the
audited encoding and `Tr(1)=0`; the trace is still onto. The classical trace
form argument survives, but `1/2` does not exist, exactly as the Scope says.

## Relative Frobenius

Put `q=|K|`, `d=[E:K]`, `sigma(x)=x^q`. The freshman's-dream identity and
`a^q=a` for `a in K` give K-linearity. Finiteness makes sigma bijective and
`x^(q^d)=x` gives `sigma^d=1`. The conjugate sum for the field trace is
cyclically permuted by sigma, so both trace and `chi_K o Tr` are invariant.

For the standard form,

    omega(sigma(a,b),sigma(c,d))=sigma(ad-cb),

and trace invariance makes sigma symplectic after restriction. On basis state
`delta_y`, conjugating the canonical signed half-form action gives

    delta_(y+sigma a),
    chi(-b sigma^-1(y)-ab/2).

Applying sigma inside the invariant character changes the phase to
`chi(-(sigma b)y-(sigma a)(sigma b)/2)`, exactly the target Weyl action.

Independent F81/F9 enumeration found a nine-element fixed field, nine trace
values, zero tower-trace mismatches, zero q-power K-linearity mismatches, and
zero trace-invariance mismatches. A non-F3 parameter (encoding 36 in this
presentation) gives a named F9 character differing from the restricted fixed
absolute character. These encoding numbers are not compared across the two
imported GF implementations.

The permutation unitary has inverse sigma inverse and dth power identity.
Consequently conjugation is a CP ordinary-trace channel, its inverse is
conjugation by the adjoint, and its dth power is identity. At rank zero all
maps are the identity on C.

## Symplectic subsystem geometry and models

For `A=j(U)`, nondegeneracy of U implies `A cap A^perp=0`. The kernel of
`V -> A^*`, `v -> omega(v,-)|A`, is `A^perp`, and restriction from `V^*` to
`A^*` is onto. Rank-nullity gives `dim A+dim A^perp=dim V`, hence the direct
sum. Double perpendiculars prove the complement nondegenerate.

In the F3 checker fixture,

    j(a,b)=(a,a;b,0),       k(u,v)=(0,u;-v,v).

Direct expansion gives `omega(jx,jy)=omega(x,y)`, the same for k, and zero
cross-pairing. For target `(x1,x2;y1,y2)`, the unique inverse decomposition is

    (a,b)=(x1,y1+y2),       (u,v)=(x2-x1,y2).

Independent enumeration found zero symplectic/orthogonality mismatches and
81 distinct sums.

The symplectic sum map pulls the chosen V model back to the same full matrix
Weyl algebra represented irreducibly on `H_U tensor H_W`. Admitted model
uniqueness therefore supplies a unitary intertwiner, and Schur uniqueness
makes its ambiguity one U(1) phase. For a tower, the complement map
`(w,z)->ell(w)+z` is an orthogonal symplectic bijection. Both staged and direct
unitaries then carry `(u,w,z)` to the label `ell(ju)+ell(w)+z`, so the full
D1710 compatibility phase exists.

## Decoder and tower

For an orthonormal complement basis, let
`K_r=(1 tensor <e_r|)J^*`. Matrix units give

    D_J(rho)=sum_r K_r rho K_r^*=Tr_W(J^*rho J),
    sum_r K_r^*K_r=1.

Thus D_J is CP and trace-preserving with the ordinary trace. Cyclicity of the
finite matrix trace gives

    Tr(D_J(rho)a)=Tr(rho J(a tensor 1)J^*).

Setting the complement Weyl label to zero yields
`iota_J(W_U(u))=W_V(ju)` and therefore restriction of the characteristic
function. Multiplying J by a phase cancels in both quadratic formulas.

For the registered tower, partial trace first over `H_(W_ell)` and then over
`H_(W_j)` has Kraus rows indexed by `(r,s)`. Replacing the staged J by its
phase multiple of the direct route cancels the phase, while `J^perp` sends the
tensor basis `(e_r tensor f_s)` to a basis of the combined complement. The
Kraus sums are therefore identical. The exact F3 maps

    (x1,x2,x3) -> (x1,x1+x2,x1+x2+x3)

agree by direct and staged routes on all 27 basis labels. No equation survives
if the retained factor is changed without changing the registered data.
