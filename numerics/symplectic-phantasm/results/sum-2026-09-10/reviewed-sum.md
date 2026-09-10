# Coherent lists, tagged blocks, and block dephasing

Lane model: `gpt-5.6-sol`, reasoning `xhigh`.

Prover-pass artifact for the exact canonical SP-SUM row.  Status remains
`SKETCH` pending its one blind review and adjudication.  Canonical definitions
are D1003 and D1704--D1707; admitted dependencies are F1-REAL, SP-WEYL,
SP-STAB-REL and SP-CP.  F1-REAL already proves the full square matrix span, so no finite
Stone--von Neumann argument is repeated here.  The new work is the explicit
rectangular span, D1707 block realization, empty-list behavior, dimensions,
and ordinary-trace block dephasing.

Fix an odd prime `p`.  Write `H_n=H_(F_p,n)=l2(F_p^n)` only as proof-local
shorthand.  In particular `H_0=C`; D1707's empty-list realization is instead
the zero Hilbert space.

## 1. Actual rectangular matrix units

**ASSUME** ranks `m,n>=0`.  **PROVE** the complex span inside actual maps of

    Stab_p^amp(H_n,H_m)

is the full `Hom_C(H_n,H_m)`.

<1>1. For `n>=1`, tensor `n` copies of D1704's computational preparation to
obtain

    e_0:C->H_n,  e_0(1)=delta_(0,...,0).

For `n=0`, put `e_empty=1_C:C->H_0`.
**BY** D1704's tensor closure, rank-zero object, and named coordinate
identification.

<1>2. For `x=(x_1,...,x_n) in F_p^n`, the translation

    X(x)=tensor_(r=1)^n X(x_r)

is an actual D1704 unitary and `e_x=X(x)e_0` sends `1` to `delta_x`.
**BY** D1003's Schrödinger translations, D1704's inclusion of every
second-level unitary and closure under tensor/composition.  A Weyl
translation normalizes the full-scalar Pauli group by its commutator, so it
is in the second level.

<1>3. At `n=0`, the same statement uses the unique empty tuple, empty tensor
and `e_empty=1_C`.
**BY** D1704.

<1>4. D1704's adjoint closure supplies

    e_x^*:H_n->C,  e_x^*(delta_z)=[x=z].

**BY** `<1>1`--`<1>3` and orthonormality of the computational basis.

<1>5. For `y in F_p^m`, define the actual composite

    E_(y,x)=e_y e_x^*:H_n->H_m.

Then

    E_(y,x)(delta_z)=[x=z]delta_y.

**BY** D1704's composition and `<1>4`.

<1>6. Every `E_(y,x)` is an actual stabilizer amplitude before taking any
linear span.
**BY** `<1>2`, `<1>4`, `<1>5`, and D1704.

<1>7. The family has `p^(m+n)=dim H_m dim H_n` members and is linearly
independent.
**BY** in a relation `sum_(y,x)c_(y,x)E_(y,x)=0`, apply to `delta_x` and
read the coefficient of each `delta_y`.

<1>8. Hence these rectangular matrix units form a basis of
`Hom_C(H_n,H_m)`.
**BY** `<1>7` and the dimension of a rectangular matrix space.

<1>9. Thus every linear map is a finite complex sum

    T=sum_(y,x)c_(y,x)E_(y,x)

and belongs to D1707's complex span of the actual D1704 Hom-set.
**BY** `<1>6`--`<1>8` and D1707.

<1>10. At `m=n`, this conclusion agrees with the already admitted
F1-REAL square spanning theorem; no irreducibility or uniqueness theorem has
been reproved.
**BY** F1-REAL section 2 and SP-WEYL.

<1>11. At `m=0`, `n=0`, or both, the same basis calculation uses row
functionals, column preparations, or the single scalar matrix unit
respectively.
**BY** `<1>3`--`<1>8`.

<1>12. Addition occurs only in D1707's complex span.  An arbitrary sum in
`<1>9` need not be one morphism of the uncompleted actual-amplitude category.
The D1705 `C^times` quotient supplies neither this addition nor its equality.
**BY** D1704--D1707 and their Scopes.

<1>13. **PROVE** this complex span strictly enlarges the pure actual-amplitude
fragment at the claimed odd-prime scope.

  <2>1. For fixed ranks, there are only finitely many affine Lagrangian
  relations over `F_p`: each is a subset of the finite set `V_n times V_m`.
  **BY** finiteness of the standard phase spaces; restricting to affine
  Lagrangian subsets preserves finiteness.

  <2>2. Admitted SP-STAB-REL identifies those relations with all D1705
  projective stabilizer classes.  Hence the nonzero actual D1704 maps occupy
  only finitely many complex rays in each Hom-space.
  **BY** SP-STAB-REL's full and faithful equivalence and D1705's quotient by
  every nonzero scalar.

  <2>3. But `End_C(H_1)` has dimension `p^2>1` and infinitely many rays: for
  two independent matrix units `E,F`, the rays of `E+zF`, `z in C`, are
  pairwise distinct.
  **BY** if `E+zF=c(E+z'F)`, independence gives `c=1` and `z=z'`.

  <2>4. Thus some linear maps in the full span are not actual stabilizer
  amplitudes, even up to nonzero scalar.  The enlargement is strict.
  **BY** `<2>2`--`<2>3` and section 1 `<1>9`.

  <2>5. **QED** `<1>13`.

<1>14. **QED** the exact rectangular spanning and Scope-enlargement clauses.
**BY** `<1>1`--`<1>13`.

## 2. Block-matrix realization on coherent sums

**ASSUME** finite ordered lists

    X=(H_i)_(i=1)^s,  Y=(K_j)_(j=1)^t,

with `s,t>=0`, and a D1707 arrow matrix `T=(T_(j i))`.
**PROVE** D1707's block action identifies its matrix Hom-space with every
linear map `H_X->H_Y`, including empty lists.

<1>1. If `s,t>0`, every entry `T_(j i)` is an arbitrary linear map
`H_i->K_j` by section 1.
**BY** D1707 and section 1 `<1>9`.

<1>2. D1707 realizes this matrix by

    R_(X,Y)(T)(xi_i)_i=(sum_i T_(j i)xi_i)_j.

**BY** D1707's prescribed block action.

<1>3. **PROVE** this realization is injective.

  <2>1. If `R(T)=0`, take an input supported only at position `i` and
  project the output to position `j`; the result is `T_(j i)xi=0` for every
  `xi in H_i`.
  **BY** `<1>2` and the direct-sum injections/projections.

  <2>2. Thus every block entry is zero and `T=0`.
  **BY** extensional equality of linear maps.

  <2>3. **QED** `<1>3`.

<1>4. **PROVE** this realization is surjective.

  <2>1. Given `L:H_X->H_Y`, let

      T_(j i)=pi_j L iota_i:H_i->K_j.

  Each block belongs to the D1707 span by section 1.
  **BY** canonical direct-sum injection `iota_i`, projection `pi_j`, and
  section 1.

  <2>2. For every `(xi_i)_i`, linearity gives

      L((xi_i)_i)=(sum_i T_(j i)xi_i)_j.

  **BY** `(xi_i)_i=sum_i iota_i xi_i` and the definitions of the blocks.

  <2>3. Hence `R(T)=L`.
  **BY** `<2>1`--`<2>2`.

  <2>4. **QED** `<1>4`.

<1>5. For composable arrow matrices `S,T`,

    R(S T)(xi)_k=sum_j S_(k j)(sum_i T_(j i)xi_i)
      =(R(S)R(T))(xi)_k.

**BY** D1707 matrix multiplication and finite distributivity.

<1>6. For the adjoint transpose,

    <eta,R(T)xi>=sum_(j,i)<T_(j i)^*eta_j,xi_i>
      =<R(T^*)eta,xi>.

Thus `R(T^*)=R(T)^*`.
**BY** the orthogonal direct-sum inner product and D1707.

<1>7. If `s=0`, then `H_X=0`; if `t=0`, then `H_Y=0`.  In either case the
unique empty block matrix realizes the unique zero linear map of the stated
type.
**BY** D1707's explicit empty-list prescription and uniqueness of a linear
map to or from the zero vector space.

<1>8. In particular `End(0)` is the zero vector space/algebra attached to
the empty list.  It is not the scalar algebra `End(H_0)=C` attached to the
one-entry list `(H_0)`.
**BY** D1707 and `H_0=C` from D1704.

<1>9. D1706 does not apply to the empty-list realization because its systems
are finite nonempty families of nonzero Hilbert spaces; no zero-space channel
has been asserted.
**BY** D1706's object hypothesis and D1707's Scope.

<1>10. Repeated equal Hilbert spaces at distinct positions remain distinct
summands: the block extraction `pi_j L iota_i` retains their list indices.
**BY** the ordered-list datum in D1707 and `<1>4`.

<1>11. **QED** full coherent block realization, composition, dagger, empty
lists and repeated tags.
**BY** `<1>1`--`<1>10`.

## 3. Coherent and tagged algebra dimensions

**ASSUME** a nonempty list `X=(H_i)_(i=1)^s`, put

    H=direct-sum_i H_i,  d_i=dim H_i,  D=sum_i d_i.

**PROVE** the coherent and tagged algebra clauses.

<1>1. The coherent algebra decomposes as a vector space into all blocks:

    End(H)=direct-sum_(i,j) Hom_C(H_j,H_i).

**BY** section 2's block extraction and realization with `X=Y`.

<1>2. Therefore

    dim_C End(H)=sum_(i,j)d_i d_j=(sum_i d_i)^2=D^2.

**BY** `dim Hom(H_j,H_i)=d_i d_j` and finite distributivity.

<1>3. The tagged algebra is the diagonal block sum

    A_tag(X)=direct-sum_i End(H_i) subset End(H).

It is closed under multiplication, adjoint, and contains the coherent
identity.
**BY** D1707's embedded block-diagonal prescription and block multiplication.

<1>4. Its dimension is

    dim_C A_tag(X)=sum_i d_i^2.

**BY** direct-sum dimension and `dim End(H_i)=d_i^2`.

<1>5. If `s>=2`, choose nonzero basis vectors in two distinct recorded
positions.  Their rank-one cross-block matrix unit lies in `End(H)` and not
in `A_tag(X)`, even when the two Hilbert spaces are equal as untagged spaces.
**BY** all D1707 blocks exist by sections 1--2, while tagged elements have
zero off-diagonal blocks.

<1>6. **QED** the coherent/tagged subalgebra and dimension clauses.
**BY** `<1>1`--`<1>5`.

## 4. Ordinary-trace block dephasing

**ASSUME** the same nonempty list and D1707 projections `P_i=P_i^X`.
**PROVE**

    Delta_X(a)=sum_i P_i a P_i

is the ordinary-trace-preserving block-dephasing channel onto the tagged
subalgebra.

<1>1. The projections satisfy

    P_i^*=P_i,  P_iP_j=[i=j]P_i,  sum_i P_i=1_H.

**BY** D1707's coordinate action on the ordered summands.

<1>2. For the `(r,s)` block `a_(r s)=pi_r a iota_s`,

    (Delta_X(a))_(r s)=[r=s]a_(r r).

**BY** insert `<1>1` into D1707's displayed sum and use
`pi_rP_i=[r=i]pi_r`, `P_i iota_s=[i=s]iota_s`.

<1>3. Thus `Delta_X` fixes every tagged block-diagonal operator, kills every
off-diagonal block, and has range exactly `A_tag(X)`.
**BY** `<1>2` and section 3 `<1>3`.

<1>4. It is idempotent and unital.
**BY** applying `<1>2` twice changes nothing, and
`Delta_X(1_H)=sum_iP_i=1_H` by `<1>1`.

<1>5. The list `(P_i)_i` is a Kraus presentation and

    sum_i P_i^*P_i=sum_iP_i=1_H.

**BY** `<1>1` and D1707's formula.

<1>6. Regard `H` as the singleton nonzero D1706 system `(H)`.  Admitted
SP-CP applied to `<1>5` makes `Delta_X` a completely positive
trace-preserving channel.
**BY** SP-CP's Kraus/channel criterion; nonemptiness of `X` and nonzero
summands imply `H!=0`.

<1>7. Independently, ordinary matrix trace is the sum of diagonal-block
traces, so

    Tr_H(Delta_X(a))=sum_i Tr_(H_i)(a_(i i))=Tr_H(a).

**BY** choose concatenated orthonormal bases adapted to the summands and use
`<1>2`.

<1>8. No division by the number or dimensions of the blocks occurs.
**BY** `<1>5`--`<1>7` and D1706's ordinary-trace convention.

<1>9. No dephasing map is prescribed for the empty list, and `<1>6` is not
applied there.
**BY** D1707's Scope and section 2 `<1>9`.

<1>10. Idempotence and the exact range support the phrase “block
dephasing”; the canonical claim uses only the block-diagonal target and
trace-preserving channel conclusions.
**BY** `<1>3`--`<1>6`.

<1>11. **QED** block dephasing.
**BY** `<1>1`--`<1>10`.

## 5. Exact canonical conclusion

<1>1. Actual preparations, translations and adjoints supply every
rectangular matrix unit; their complex span is every linear map between
standard model spaces.
**BY** section 1.

<1>2. D1707 arrow matrices realize every map between coherent finite sums,
including unique typed zero maps for empty lists and separate repeated tags.
**BY** section 2.

<1>3. For nonempty lists, coherent and tagged algebra dimensions are
`(sum_i dim H_i)^2` and `sum_i(dim H_i)^2`, with the tagged algebra exactly
the block-diagonal subalgebra.
**BY** section 3.

<1>4. D1707's `Delta_X` is the corresponding ordinary-trace-preserving
block-dephasing channel.
**BY** section 4 and admitted SP-CP.

<1>5. The complex completion strictly enlarges the pure stabilizer fragment.
**BY** section 1 `<1>13` and admitted SP-STAB-REL.

<1>6. None of these calculations promotes a biproduct, fusion, rig,
Gaussian, pure-stabilizer-sum, or arithmetic-source-exhaustion statement.
**BY** D1707's Scope and the exact boundaries in sections 1--4.

<1>7. **QED** the exact canonical SP-SUM statement and its exact Scope.
**BY** `<1>1`--`<1>6`, D1003, D1704--D1707, F1-REAL, SP-WEYL, SP-STAB-REL and SP-CP at
their stated scopes.
