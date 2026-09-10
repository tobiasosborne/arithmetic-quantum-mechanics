# Symplectic complements and compatible Weyl subsystem models

Lane model: `gpt-5.6-sol`, reasoning `xhigh`.

First prover shard for canonical SP-SUBSYS. Status remains `SKETCH`.
Canonical definitions are D1701, D1703, D1706 and D1710. Admitted SP-TENSOR
supplies direct-sum Weyl/tensor comparison and admitted SP-WEYL supplies
arbitrary-rank full-matrix realization and unitary model uniqueness. Those
results are reused; finite Stone--von Neumann is not reproved.

Fix an odd-characteristic finite field `k`, one nontrivial character `psi`,
and a symplectic injection `j:U->V`. Put `W=j(U)^perp` as in D1710.

## 1. The actual symplectic complement

**PROVE** `V=j(U)+W` is an orthogonal direct sum of nondegenerate symplectic
spaces.

<1>1. The image `j(U)` is nondegenerate.
**BY** if `ju` pairs to zero with every `ju'`, symplecticity of `j` gives
`omega_U(u,u')=0` for all `u'`; nondegeneracy of `U` gives `u=0`.

<1>2. The intersection `j(U) cap W` is zero.
**BY** an element of the intersection lies in the radical of `j(U)`, which
is zero by `<1>1`.

<1>3. For a subspace `A` of a finite-dimensional nondegenerate bilinear
space,

    dim A+dim A^perp=dim V.

**BY** the map `V->A^*`, `v |-> omega_V(v,-)|_A`, is onto after identifying
`V` with `V^*`; its kernel is `A^perp`, so apply rank-nullity.

<1>4. Applying `<1>3` to `A=j(U)` and using injectivity of `j` gives

    dim j(U)+dim W=dim V.

**BY** D1710 and `<1>3`.

<1>5. The zero intersection and dimension equality prove
`V=j(U) direct-sum W`; it is orthogonal by the definition of `W`.
**BY** `<1>2`--`<1>4`.

<1>6. **PROVE** the restricted form on `W` is nondegenerate.

  <2>1. If `w in W` pairs to zero with every element of `W`, it lies in
  `W cap W^perp`.
  **BY** the definition of a radical.

  <2>2. Double perpendiculars and `<1>1` give `W^perp=j(U)`.
  **BY** `W=j(U)^perp`, finite-dimensional nondegeneracy, and `<1>3`.

  <2>3. Thus `w in W cap j(U)=0` by `<1>2`.
  **BY** `<2>1`--`<2>2`.

  <2>4. **QED** `<1>6`.

<1>7. The sum map

    g_j:U+W->V,  g_j(u,w)=ju+w

is a symplectic linear isomorphism.
**BY** `<1>5` gives bijectivity, and orthogonality plus symplecticity of `j`
gives
`omega_V(ju+w,ju'+w')=omega_U(u,u')+omega_W(w,w')`.

<1>8. If `U=0`, then `W=V` and `g_j` is the left unitor. If `W=0`, `j` is
a symplectic isomorphism and `g_j` is the right-unitor identification.
**BY** the definitions and `<1>5`.

<1>9. **QED** the decomposition and all rank-zero cases.
**BY** `<1>1`--`<1>8`.

## 2. Existence and phase uniqueness of a compatible model unitary

**ASSUME** D1710's specified irreducible unitary Weyl models
`H_U,H_W,H_V`. **PROVE** a unitary `J:H_U tensor H_W->H_V` satisfying the
D1710 Weyl equation exists and is unique up to overall phase.

<1>1. SP-TENSOR makes `H_U tensor H_W` an irreducible unitary model for the
direct-sum Weyl algebra, with

    W_(U+W)^s(u,w) |-> W_U^s(u) tensor W_W^s(w).

**BY** admitted SP-TENSOR and the full-matrix conclusion of SP-WEYL.

<1>2. The symplectic isomorphism `g_j` transports the target model to a
model of the same direct-sum algebra by

    W_(U+W)^s(u,w) |-> W_V^s(ju+w).

**BY** section 1 `<1>7` and D1703: symplecticity of `g_j` makes the two
half-form multipliers equal, while zero and negation labels are preserved.

<1>3. The target model remains irreducible and unitary under this label
transport.
**BY** D1710's irreducibility/unitarity and bijectivity of the algebra map.

<1>4. SP-WEYL's admitted arbitrary-rank unitary model uniqueness supplies a
unitary intertwiner `J` between the models in `<1>1` and `<1>2`.
**BY** SP-WEYL; no new irreducibility or SvN proof is used.

<1>5. Its intertwining equation on each Weyl generator is exactly

    J(W_U^s(u) tensor W_W^s(w))J^*=W_V^s(ju+w).

**BY** `<1>1`--`<1>4`.

<1>6. Any two such unitaries differ by one scalar in `U(1)`.
**BY** admitted SP-WEYL's unitary-intertwiner uniqueness.

<1>7. When a factor has rank zero, SP-TENSOR uses `H_0=C` and the ordinary
Hilbert unitor, so the same existence and phase statement holds.
**BY** D1703, D1710 and SP-TENSOR's unit clauses.

<1>8. **QED** the single-step model existence obligation.
**BY** `<1>1`--`<1>7`.

## 3. Geometry of the registered iterated complements

**ASSUME** composable symplectic injections

    U --j--> V --ell--> X

and D1710's complements `W_j,W_ell,W_(ell j)`. **PROVE**

    c_(j,ell):W_j+W_ell->W_(ell j),
    c_(j,ell)(w,z)=ell(w)+z

is a symplectic linear isomorphism.

<1>1. For `u in U`,

    omega_X(ell(w)+z,ell(j u))
      =omega_V(w,ju)+omega_X(z,ell(ju))=0.

**BY** `w in W_j`, `z in W_ell`, and symplecticity of `ell`.

<1>2. Thus the displayed formula lands in the actual combined complement
`W_(ell j)` and is linear.
**BY** `<1>1` and D1710.

<1>3. Its two summand images are orthogonal: `ell(W_j) subset ell(V)` while
`W_ell=ell(V)^perp`.
**BY** D1710.

<1>4. It is injective. If `ell(w)+z=0`, then `ell(w)=-z` lies in
`ell(V) cap ell(V)^perp`, which is zero because `ell(V)` is nondegenerate;
then `w=z=0`.
**BY** section 1 `<1>1` applied to `ell`, and injectivity of `ell`.

<1>5. Its source dimension is

    (dim V-dim U)+(dim X-dim V)=dim X-dim U,

which is the dimension of `W_(ell j)`.
**BY** section 1 `<1>3`--`<1>4` for `j`, `ell`, and `ell j`.

<1>6. Therefore it is bijective.
**BY** `<1>4`--`<1>5`.

<1>7. For two source pairs, cross terms vanish and

    omega_X(ell w+z,ell w'+z')
      =omega_(W_j)(w,w')+omega_(W_ell)(z,z').

**BY** symplecticity of `ell` and `<1>3`.

<1>8. Hence `c_(j,ell)` is symplectic; in particular the combined
complement is nondegenerate.
**BY** `<1>6`--`<1>7` and section 1 `<1>6` for the source complements.

<1>9. The formula includes any zero complement, where it reduces to the
corresponding symplectic unitor.
**BY** D1710's rank-zero convention.

<1>10. **QED** the iterated complement obligations.
**BY** `<1>1`--`<1>9`.

## 4. Existence and compatibility of the full iterated J-data

**ASSUME** D1710's shared irreducible unitary models for all spaces in
section 3. **PROVE** the four registered unitary types can be chosen with
their Weyl equations and satisfy D1710's compatibility equation for some
overall phase.

<1>1. Section 2 applied to `j`, `ell`, and `ell j` supplies
`J_j,J_ell,J_(ell j)` of the registered types.
**BY** section 2 and the three decompositions from section 1.

<1>2. Section 2 applied to the symplectic comparison `c_(j,ell)` supplies

    J^perp_(j,ell):H_(W_j) tensor H_(W_ell)->H_(W_(ell j))

with D1710's complement Weyl equation.
**BY** section 3 and section 2.

<1>3. Let `A` be the staged unitary

    J_ell o (J_j tensor 1):
      (H_U tensor H_(W_j)) tensor H_(W_ell)->H_X,

and let `B` be the direct unitary

    J_(ell j) o (1 tensor J^perp_(j,ell)) o assoc,

where `assoc` is D1710's explicit pure-tensor reassociation.
**BY** the registered types and ordinary Hilbert tensor composition.

<1>4. On a Weyl tensor labelled `(u,w,z)`, the staged route implements the
label

    ell(ju+w)+z=ell(j u)+ell(w)+z.

**BY** the Weyl equations for `J_j` and `J_ell`.

<1>5. The direct route implements the same label: `J^perp` sends `(w,z)`
to `ell(w)+z`, then `J_(ell j)` sends `(u,ell(w)+z)` to
`ell(ju)+ell(w)+z`.
**BY** the equations for `J^perp` and `J_(ell j)`.

<1>6. Thus `A` and `B` are unitary intertwiners between the same irreducible
domain and target Weyl models.
**BY** `<1>3`--`<1>5`, SP-TENSOR associativity, and SP-WEYL.

<1>7. SP-WEYL's unitary-intertwiner uniqueness gives `A=lambda B` for one
`lambda in U(1)`.
**BY** `<1>6`.

<1>8. Evaluating this equality on every bound pure tensor is exactly
D1710's compatibility condition; the phase is not selected as new data.
**BY** D1710 and `<1>7`.

<1>9. SP-TENSOR's unit coherence supplies the same statement when any
registered factor has rank zero.
**BY** D1710, section 2 `<1>7`, and SP-TENSOR.

<1>10. **QED** existence of full compatible iterated model data.
**BY** `<1>1`--`<1>9`.

## 5. Shard conclusion

<1>1. Every symplectic injection has the claimed actual nondegenerate
orthogonal complement and a compatible irreducible unitary model comparison.
**BY** sections 1--2.

<1>2. The registered combined complement comparison is a symplectic
isomorphism, and all four iterated model unitaries exist and obey the exact
pure-tensor compatibility up to allowed phase.
**BY** sections 3--4.

<1>3. No field restriction, field support code, or characteristic-two
half-form has been introduced.
**BY** D1710's Scope and the fixed hypotheses.

<1>4. **QED** the geometry and model-existence portions of canonical
SP-SUBSYS.
**BY** `<1>1`--`<1>3`, D1701, D1703, D1710, SP-WEYL, SP-TENSOR and
F1-REAL/F1-FUNCT only through their admitted descendants.
