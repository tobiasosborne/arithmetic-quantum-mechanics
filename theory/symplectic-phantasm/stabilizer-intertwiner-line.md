# The affine Lagrangian intertwiner line

Lane model: `gpt-5.6-sol`, reasoning `xhigh`.

Admitted proof component for `SP-STAB-REL`; see
`theory/verdicts/phantasm-relations-adjudication.md`. This shard uses D1715 and admitted SP-WEYL/SP-TENSOR.  SP-CK21,
`lagrel.tex` 3647--3744, is the source-level odd-prime projective stabilizer
comparison; its theorem states a symmetric monoidal equivalence.  The proof
below independently constructs the line needed in the repository's D1702
sign and D1703 Weyl conventions.

Fix an odd prime `p`.  As proof-local abbreviations for the existing
canonical names, write `psi=psi_(F_p)`, `H_n=H_(F_p,n)`,
`W_n=W^s_(F_p,n)`, and

    Omega((v,w),(v',w'))=-omega_m(v,v')+omega_n(w,w')

on `bar(V_m)+V_n`.  For a nonempty relation `R=r+L`, write
`chi_r(l)=psi(-Omega(r,l))`.  These are proof-local abbreviations for
D1715.

## 1. The Weyl action on an operator space

**ASSUME** ranks `m,n`.  On `Hom_C(H_m,H_n)` define

    rho_(m,n)(v,w)(T)=W_n(w) T W_m(v)^*.

**PROVE** this is the D1703 Weyl representation for the symplectic form
`Omega` and has zero trace away from the zero label.

<1>1. For labels `l=(v,w)` and `l'=(v',w')`,

    rho(l)rho(l')(T)
      =W_n(w)W_n(w') T W_m(v')^*W_m(v)^*.

**BY** the displayed definition.

<1>2. D1703's product gives

    W_n(w)W_n(w')
      =psi(omega_n(w,w')/2)W_n(w+w')

and

    W_m(v')^*W_m(v)^*
      =psi(-omega_m(v,v')/2)W_m(v+v')^*.

**BY** D1703 and `(AB)^*=B^*A^*`.

<1>3. Consequently

    rho(l)rho(l')=psi(Omega(l,l')/2)rho(l+l').

**BY** `<1>1`--`<1>2` and the definition of `Omega`.

<1>4. Also `rho(l)^*=rho(-l)` for the Hilbert--Schmidt inner product
`<S,T>=Tr(S^*T)`.
**BY** cyclicity of the finite matrix trace and D1703's unitary Weyl
operators.

<1>5. The linear map `T |-> A T B` on a matrix Hom-space has trace
`Tr(A)Tr(B)`.
**BY** evaluate it on the matrix-unit basis `E_(ij)` and sum the diagonal
coefficients.

<1>6. SP-WEYL identifies D1703's coefficient trace with normalized matrix
trace.  Hence

    Tr_(H_j)(W_j(x))=p^j if x=0, and 0 otherwise.

**BY** admitted SP-WEYL.

<1>7. Applying `<1>5`--`<1>6` to `rho(v,w)` gives

    Tr_Hom(rho(v,w))=p^(m+n) if (v,w)=0, and 0 otherwise.

**BY** `<1>5`--`<1>6`; taking an adjoint does not change whether a Weyl
label is zero.

<1>8. **QED** the operator-space Weyl and trace formulas.
**BY** `<1>3`--`<1>7`.

## 2. Origin independence

**ASSUME** a nonempty affine Lagrangian relation `R=r+L` and another point
`r' in R`.  **PROVE** D1715's equations do not depend on which point is
chosen.

<1>1. There is `l_0 in L` with `r'=r+l_0`.
**BY** the definition of the affine translate `r+L`.

<1>2. For every `l in L`, `Omega(l_0,l)=0`.
**BY** D1702 says `L` is Lagrangian, hence isotropic, in the displayed
ambient form.

<1>3. Thus

    psi(-Omega(r',l))
      =psi(-Omega(r,l)-Omega(l_0,l))
      =psi(-Omega(r,l)).

**BY** bilinearity, `<1>2`, and the character law.

<1>4. D1715's difference set is `R-R=L`, and the direction computed from
either single origin is also `R-r=R-r'=L`.
**BY** differences in `r+L` form `L-L=L`, while
`R-r'=(r+L)-(r+l_0)=L-l_0=L`.

<1>5. Hence both choices give the same simultaneous eigenspace
`E_p(R)`.
**BY** D1715 and `<1>3`--`<1>4`.

<1>6. **QED** origin independence; no origin becomes retained data.
**BY** `<1>5`.

## 3. The rank-one group-average projector

**ASSUME** the same `R=r+L`.  **PROVE** `E_p(R)` is one-dimensional and
nonzero.

<1>1. Since `L` is isotropic, `<1>3` of section 1 restricts to

    rho(l)rho(l')=rho(l+l')  for l,l' in L.

Thus `rho|_L` is an ordinary unitary representation of the additive group
`L`.
**BY** D1702 and section 1.

<1>2. The function `chi_r(l)=psi(-Omega(r,l))` is a character of `L`.
**BY** bilinearity of `Omega` and additivity of `psi`.

<1>3. Define the operator on the Hilbert--Schmidt space

    P_R=(1/|L|) sum_(l in L) chi_r(l)^(-1) rho(l).

**BY** finite dimensionality over the finite field.

<1>4. **PROVE** `P_R` is the orthogonal projector onto `E_p(R)`.

  <2>1. For `x in L`, reindexing `l |-> l+x` gives

      rho(x)P_R=chi_r(x)P_R.

  **BY** `<1>1`--`<1>3` and the character law.

  <2>2. Hence `im P_R subset E_p(R)`.
  **BY** D1715's eigen-equations and `<2>1`.

  <2>3. If `T in E_p(R)`, then every summand in `<1>3` sends `T` to `T`,
  so `P_R T=T`.
  **BY** D1715.

  <2>4. Therefore `im P_R=E_p(R)` and `P_R^2=P_R`.
  **BY** `<2>2`--`<2>3`.

  <2>5. Replacing `l` by `-l` in the adjoint of `<1>3` gives
  `P_R^*=P_R`.
  **BY** section 1 `<1>4` and
  `chi_r(-l)=chi_r(l)^(-1)`.

  <2>6. **QED** `<1>4`.

<1>5. Since `L` is Lagrangian in a space of dimension `2(m+n)`,
`dim_Fp L=m+n` and `|L|=p^(m+n)`.
**BY** D1701--D1702 and the half-dimension characterization of a
Lagrangian subspace.

<1>6. Only the `l=0` term contributes to the trace of `P_R`, so

    Tr(P_R)=p^(m+n)/|L|=1.

**BY** section 1 `<1>7`, `<1>3`, and `<1>5`.

<1>7. The rank of a finite-dimensional orthogonal projector equals its
trace.  Hence `rank P_R=1`.
**BY** diagonalize the self-adjoint idempotent, whose eigenvalues are zero
and one.

<1>8. Therefore `E_p(R)=im P_R` is a nonzero line.
**BY** `<1>4`, `<1>6`, and `<1>7`.

<1>9. By prescription `E_p(empty)={0}`.  Thus the candidate space contains
a nonzero map exactly when the relation is nonempty.
**BY** D1715 and `<1>8`.

<1>10. **QED** the dimension and nonzero/empty clauses.
**BY** `<1>8`--`<1>9`.

## 4. Recovery of the affine relation from its line

**ASSUME** `R=r+L` is nonempty and `0 != T in E_p(R)`.  Put

    D(T)={x in bar(V_m)+V_n : rho(x)T is in C T}.

**PROVE** `D(T)=L`, and the eigenvalues recover the affine coset `r+L`.

<1>1. D1715 gives `L subset D(T)`.
**BY** the defining eigen-equations.

<1>2. **PROVE** `D(T)` is isotropic.

  <2>1. Suppose `x,y in D(T)`, with
  `rho(x)T=aT` and `rho(y)T=bT`, where `a,b` are nonzero because each
  `rho` is unitary.
  **BY** the definition of `D(T)` and section 1 `<1>4`.

  <2>2. The Weyl multiplication formula gives

      rho(x)rho(y)=psi(Omega(x,y))rho(y)rho(x).

  **BY** section 1 `<1>3` and alternation of `Omega`.

  <2>3. Applying this equality to `T` gives
  `abT=psi(Omega(x,y))abT`, hence `psi(Omega(x,y))=1`.
  **BY** `<2>1`--`<2>2` and `T != 0`.

  <2>4. The character `psi(x)=zeta_p^x` on `F_p` has zero kernel, so
  `Omega(x,y)=0`.
  **BY** primitivity of `zeta_p` and `p` prime.

  <2>5. **QED** `<1>2`.

<1>3. An isotropic subspace of a `2(m+n)`-dimensional symplectic space has
dimension at most `m+n`.
**BY** `D subset D^perp` and
`dim D+dim D^perp=2(m+n)`.

<1>4. Although `D(T)` was defined as a set, it is closed under addition
and `F_p`-scaling: the Weyl product and powers send scalar eigenvectors to
scalar eigenvectors.
**BY** section 1 `<1>3`, and the additive group of `V_m+V_n` has exponent
`p`.

<1>5. Thus `D(T)` is an isotropic subspace containing the Lagrangian
subspace `L`; the dimension bound forces `D(T)=L`.
**BY** `<1>1`--`<1>4` and `dim L=m+n`.

<1>6. Suppose a second nonempty relation `S=s+M` has the same projective
line.  Choose the same nonzero `T` in both lines.  Then `M=D(T)=L`.
**BY** `<1>5`, noting that rescaling `T` does not change `D(T)`.

<1>7. On each `l in L`, the two defining eigenvalues agree, so

    psi(-Omega(r,l))=psi(-Omega(s,l)).

**BY** D1715 and `T != 0`.

<1>8. Faithfulness of `psi` yields `Omega(r-s,L)=0`; since `L=L^perp`,
`r-s in L`.
**BY** `<1>7` and D1702's Lagrangian condition.

<1>9. Hence `r+L=s+L`, so `R=S`.
**BY** `<1>8`.

<1>10. The zero line recovers the empty relation by D1715, while every
nonempty relation has a nonzero line by section 3.
**BY** D1715 and section 3.

<1>11. **QED** the recovery and prospective faithfulness clauses.
**BY** `<1>5`--`<1>10`.

## 5. Shard conclusion

<1>1. D1715 is independent of the bound origin.
**BY** section 2.

<1>2. It assigns a unique nonzero projective line to each nonempty affine
Lagrangian relation and the zero space exactly to the empty relation.
**BY** section 3.

<1>3. Distinct relations have distinct projective lines.
**BY** section 4.

<1>4. **QED** the line, origin, nonzero, and recovery portions of the
refined SP-STAB-REL statement.
**BY** `<1>1`--`<1>3`.
