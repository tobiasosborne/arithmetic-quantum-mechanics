# Observable inclusion and ordinary-trace subsystem decoding

Lane model: `gpt-5.6-sol`, reasoning `xhigh`.

Second prover shard for canonical SP-SUBSYS. Status remains `SKETCH`.
`subsystem-models.md` proves the D1710 complement and compatible model
existence obligations. This shard uses admitted SP-CP for finite Kraus
channel typing and admitted FRP-CP only for the ordinary-discard comparison.
All traces below are ordinary matrix traces.

Fix one D1710 subsystem datum `j:U->V`, `W=j(U)^perp` and
`J:H_U tensor H_W->H_V` obtained at the scope of the companion shard.

## 1. The observable inclusion is a unital star-homomorphism

Recall

    iota_J(a)=J(a tensor 1_(H_W))J^*.

**PROVE** `iota_J:End(H_U)->End(H_V)` is a unital star-homomorphism.

<1>1. It is complex-linear.
**BY** linearity of tensoring with the identity and matrix multiplication by
fixed operators.

<1>2. For `a,b in End(H_U)`,

    iota_J(a)iota_J(b)
      =J(a tensor 1)J^*J(b tensor 1)J^*
      =J(ab tensor 1)J^*=iota_J(ab).

**BY** unitarity `J^*J=1` and tensor multiplication.

<1>3. Also

    iota_J(a)^*=J(a^* tensor 1)J^*=iota_J(a^*).

**BY** `(ABC)^*=C^*B^*A^*` and `1^*=1`.

<1>4. Finally `iota_J(1_(H_U))=J1J^*=1_(H_V)`.
**BY** `JJ^*=1`.

<1>5. **QED** the unital star-homomorphism clause.
**BY** `<1>1`--`<1>4` and D1710.

## 2. The decoder is the ordinary partial-trace channel

Choose an orthonormal basis `(e_r)_(r=1)^d` of `H_W` and put

    K_r=(1_(H_U) tensor <e_r|)J^*:H_V->H_U.

**PROVE**

    D_J(rho)=sum_r K_r rho K_r^*

is D1710's trace-dual decoder and is a D1706 channel.

<1>1. The standard partial trace over `H_W` has matrix-unit formula

    Tr_(H_W)(x)=sum_r(1 tensor <e_r|)x(1 tensor |e_r>).

**BY** evaluate both sides on elementary tensors
`a tensor |e_s><e_t|`, which form a basis; both give `[s=t]a`.

<1>2. Substituting `x=J^*rho J` gives

    Tr_(H_W)(J^*rho J)=sum_rK_r rho K_r^*.

**BY** `<1>1` and the definition of `K_r`.

<1>3. The Kraus completeness sum is

    sum_rK_r^*K_r
      =J(1 tensor sum_r|e_r><e_r|)J^*=1_(H_V).

**BY** completeness of the orthonormal basis and unitarity of `J`.

<1>4. Admitted SP-CP makes the displayed map a completely positive
ordinary-trace-preserving channel.
**BY** SP-CP's finite Kraus/channel criterion and `<1>3`.

<1>5. For `rho in End(H_V)` and `a in End(H_U)`,

    Tr(D_J(rho)a)
      =sum_r Tr(K_r rho K_r^*a)
      =Tr(rho J(a tensor 1)J^*)
      =Tr(rho iota_J(a)).

**BY** rectangular trace reordering, the basis completeness in `<1>3`, and
section 1.

<1>6. Thus the Kraus map is exactly the trace-dual partial trace prescribed
by D1710; its definition is independent of the chosen orthonormal basis.
**BY** `<1>2`, `<1>5`, and nondegeneracy of the ordinary trace pairing.

<1>7. No factor `1/d` occurs. On the identity,
`D_J(1_(H_V))=d 1_(H_U)`, while trace preservation concerns states and
ordinary traces in the opposite direction.
**BY** `<1>2` and `sum_r1=d`; D1706 uses ordinary, not normalized, trace.

<1>8. **QED** the channel and trace-duality clauses.
**BY** `<1>1`--`<1>7`.

## 3. Weyl-characteristic restriction and phase independence

**PROVE** the decoder restricts Weyl characteristic functions to the
embedded subsystem and both maps are independent of an overall phase of
`J`.

<1>1. Put `w=0` in D1710's model equation. Since `W_W^s(0)=1`,

    iota_J(W_U^s(u))=W_V^s(ju).

**BY** D1703 and D1710.

<1>2. Apply trace duality from section 2 with `a=W_U^s(u)`:

    Tr(D_J(rho)W_U^s(u))=Tr(rho W_V^s(ju)).

**BY** section 2 `<1>5` and `<1>1`.

<1>3. Replacing `u` by `-u` gives the corresponding starred convention,
since `W^s(u)^*=W^s(-u)`.
**BY** D1703 and `<1>2`.

<1>4. If `J'=gamma J` with `gamma in U(1)`, then

    J'(a tensor 1)(J')^*=J(a tensor 1)J^*,
    (J')^*rho J'=J^*rho J.

**BY** `gamma conjugate(gamma)=1`.

<1>5. Hence `iota_(J')=iota_J` and `D_(J')=D_J`, and the characteristic
identity is phase-independent.
**BY** `<1>4` and the definitions.

<1>6. This is an equality of ordinary traces and actual maps, not a
coefficient-trace or normalized-trace statement.
**BY** D1706 and D1710.

<1>7. **QED** Weyl restriction and phase independence.
**BY** `<1>1`--`<1>6`.

## 4. Compatible observable and decoder towers

**ASSUME** the full compatible D1710 data for

    U --j--> V --ell--> X

with unitaries `J_j,J_ell,J_(ell j),J^perp_(j,ell)` and phase `lambda`.
**PROVE**

    iota_(J_ell) o iota_(J_j)=iota_(J_(ell j)),
    D_(J_j) o D_(J_ell)=D_(J_(ell j)).

<1>1. Let

    A=J_ell o (J_j tensor 1_(H_(W_ell)))

on `(H_U tensor H_(W_j)) tensor H_(W_ell)`, and let

    B=J_(ell j) o (1_(H_U) tensor J^perp_(j,ell)) o assoc,

where `assoc` is D1710's pure-tensor reassociation. Compatibility says
`A=lambda B`.
**BY** D1710 and `subsystem-models.md` section 4.

<1>2. The staged observable inclusion is

    A(a tensor 1_(W_j) tensor 1_(W_ell))A^*.

**BY** two applications of section 1 with the displayed reassociation.

<1>3. Replace `A` by `lambda B`; the phase cancels. Since
`J^perp` conjugates the complement identity to the combined-complement
identity, `<1>2` becomes

    J_(ell j)(a tensor 1_(W_(ell j)))J_(ell j)^*.

**BY** unitarity of `J^perp` and `|lambda|=1`.

<1>4. This is `iota_(J_(ell j))(a)`, proving inclusion composition.
**BY** D1710 and `<1>2`--`<1>3`.

<1>5. **PROVE** sequential partial trace equals trace over both staged
complements.

  <2>1. Choose orthonormal bases `(e_r)` of `H_(W_j)` and `(f_s)` of
  `H_(W_ell)`. Two uses of section 2 give Kraus rows

      (1_(H_U) tensor <e_r| tensor <f_s|)A^*:H_X->H_U.

  **BY** section 2 `<1>1`--`<1>2` and finite sum reassociation.

  <2>2. Hence `D_(J_j)D_(J_ell)(rho)` is the sum over `(r,s)` of these
  Kraus conjugations.
  **BY** composition of the two finite Kraus sums.

  <2>3. **QED** `<1>5`.

<1>6. Replace `A` by `lambda B` in `<1>5`; the phase again cancels.
**BY** D1710 compatibility.

<1>7. The vectors `J^perp(e_r tensor f_s)` form an orthonormal basis of
`H_(W_(ell j))`.
**BY** unitarity of `J^perp` and the tensor-product basis theorem.

<1>8. Using this basis in section 2's partial-trace formula turns the sum in
`<1>6` into

    Tr_(H_(W_(ell j)))(J_(ell j)^*rho J_(ell j))
      =D_(J_(ell j))(rho).

**BY** `<1>5`--`<1>7` and section 2 `<1>1`.

<1>9. Thus the decoders compose as partial traces under the full registered
compatibility condition. No equality is asserted for independently chosen
incompatible data.
**BY** `<1>8` and D1710's Scope.

<1>10. If either complement has rank zero, its basis is the singleton basis
of `C`, all sums have one index, and the same equations reduce to the
ordinary tensor unitors.
**BY** D1710's rank-zero convention and sections 1--2.

<1>11. **QED** the full iterated inclusion/decoder comparison.
**BY** `<1>1`--`<1>10`.

## 5. Boundary from field support-code decoding

**PROVE** the D1710 decoder is not being identified with D1327's support-code
success map.

<1>1. Here `J:H_U tensor H_W->H_V` is unitary onto the full ambient Hilbert
space, and `D_J` discards a genuine tensor complement with a complete Kraus
sum; it is trace preserving.
**BY** `subsystem-models.md` section 2 and section 2 `<1>3`--`<1>4`.

<1>2. A D1327 success map has one amplitude `s^*` from an isometric code
embedding and effect `ss^*<=1`; it may lose trace and is paired with a
retained failure outcome in the full decoder.
**BY** D1327 and admitted FRP-CP/FRP-DESCENT.

<1>3. A generic field embedding or relative trace does not supply the
nondegenerate symplectic injection and compatible unitary tensor
factorization used here.
**BY** D1709--D1710 Scopes.

<1>4. **QED** the decoder distinction.
**BY** `<1>1`--`<1>3`.

## 6. Exact canonical conclusion

<1>1. The observable inclusion is a unital star-homomorphism and its
ordinary-trace dual decoder is a channel.
**BY** sections 1--2 and admitted SP-CP.

<1>2. The decoder restricts Weyl characteristic functions along `j` and is
independent of an overall model-unitary phase.
**BY** section 3.

<1>3. Under D1710's full compatible iterated data, observable inclusions and
decoders compose by the direct tensor-factor comparison and ordinary partial
trace.
**BY** section 4.

<1>4. The construction is a nondegenerate tensor subsystem, not a field
support-code success branch.
**BY** section 5.

<1>5. **QED** the remaining exact canonical SP-SUBSYS statement.
**BY** `<1>1`--`<1>4`, D1326--D1327, D1701, D1703, D1706, D1710,
SP-WEYL, SP-TENSOR, SP-CP and FRP-CP at their stated scopes.
