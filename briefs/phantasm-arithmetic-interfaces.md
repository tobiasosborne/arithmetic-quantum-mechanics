# Arithmetic-interface definition candidate

Preparation date: 2026-09-10. Model: `gpt-5.6-sol`, reasoning `xhigh`.

This proposal owns the iterated subsystem types required by SP-SUBSYS and the
narrow process dependency required by SP-FROB. It contains no proof, status
change, or authorization to begin the arithmetic prover pass before the
planned SP-SUM pass lands.

## Proposed complete D1710 body

## D1710 (a specified quantum subsystem decoder)

Fix an odd-characteristic finite field $k$, a nontrivial additive character
$\psi$, and a symplectic linear injection $j:U\to V$ between
finite-dimensional symplectic $k$-spaces. Put $W=j(U)^{\perp_V}$.
A quantum subsystem datum additionally specifies finite-dimensional
Weyl model Hilbert spaces $H_U,H_W,H_V$, with $W^{\mathrm s}_U$,
$W^{\mathrm s}_W$, $W^{\mathrm s}_V$ denoting the symmetrized operators
transported through their named coordinates, and a unitary
$J:H_U\otimes H_W\to H_V$ satisfying
\[
 J(W^{\mathrm s}_U(u)\otimes W^{\mathrm s}_W(w))J^*
 =W^{\mathrm s}_V(ju+w).
\]
Define the observable inclusion $\iota_J(a)=J(a\otimes1)J^*$ and the state
decoder $\mathcal D_J(\rho)=\operatorname{Tr}_{H_W}(J^*\rho J)$, where the
partial trace is specified by
\[
 \operatorname{Tr}(\mathcal D_J(\rho)a)
 =\operatorname{Tr}(\rho\iota_J(a))
 \qquad(a\in\operatorname{End}(H_U)).
\]

For compatible iterated tensor decompositions, take composable symplectic
linear injections
\[
 U\mathrel{\mathop{\longrightarrow}^{j}}V
 \mathrel{\mathop{\longrightarrow}^{\ell}}X
\]
and use the actual orthogonal complements
\[
 W_j=j(U)^{\perp_V},\qquad
 W_\ell=\ell(V)^{\perp_X},\qquad
 W_{\ell j}=(\ell j(U))^{\perp_X}.
\]
The candidate comparison of complements is the linear map
\[
 W_j\oplus W_\ell\longrightarrow W_{\ell j},
 \qquad (w,z)\longmapsto\ell(w)+z.
\]
An iterated quantum subsystem datum consists of single-step and composite
data sharing the model spaces $H_U,H_V,H_X$ and additionally
specifies the complement model spaces and unitaries
\[
\begin{aligned}
 J_j&:H_U\otimes H_{W_j}\longrightarrow H_V,\\
 J_\ell&:H_V\otimes H_{W_\ell}\longrightarrow H_X,\\
 J_{\ell j}&:H_U\otimes H_{W_{\ell j}}\longrightarrow H_X,\\
 J^\perp_{j,\ell}&:H_{W_j}\otimes H_{W_\ell}
   \longrightarrow H_{W_{\ell j}}.
\end{aligned}
\]
The first three unitaries satisfy the preceding Weyl compatibility equation
for $j$, $\ell$, and $\ell j$, respectively. The complement comparison
satisfies
\[
 J^\perp_{j,\ell}
 (W^{\mathrm s}_{W_j}(w)\otimes W^{\mathrm s}_{W_\ell}(z))
 (J^\perp_{j,\ell})^*
 =W^{\mathrm s}_{W_{\ell j}}(\ell(w)+z).
\]
Call the iterated data compatible when there exists
$\lambda\in U(1)$ such that, for every pure tensor
$(\xi\otimes\eta)\otimes\zeta$,
\[
 J_\ell\bigl(J_j(\xi\otimes\eta)\otimes\zeta\bigr)
 =\lambda J_{\ell j}
   \bigl(\xi\otimes J^\perp_{j,\ell}(\eta\otimes\zeta)\bigr).
\]
The right-hand route uses the ordinary Hilbert reassociation
$(\xi\otimes\eta)\otimes\zeta\mapsto
\xi\otimes(\eta\otimes\zeta)$. The phase $\lambda$ is allowed but is not
retained as an additional choice. The associated maps have types
\[
\begin{aligned}
 \iota_{J_j}&:\operatorname{End}(H_U)\to\operatorname{End}(H_V),&
 \mathcal D_{J_j}&:\operatorname{End}(H_V)\to\operatorname{End}(H_U),\\
 \iota_{J_\ell}&:\operatorname{End}(H_V)\to\operatorname{End}(H_X),&
 \mathcal D_{J_\ell}&:\operatorname{End}(H_X)\to\operatorname{End}(H_V),\\
 \iota_{J_{\ell j}}&:\operatorname{End}(H_U)\to\operatorname{End}(H_X),&
 \mathcal D_{J_{\ell j}}&:\operatorname{End}(H_X)\to\operatorname{End}(H_U).
\end{aligned}
\]
For every rank-zero symplectic factor use its existing model
$H_0=\mathbb C$, the identity Weyl operator and the ordinary Hilbert tensor
unitors in the same displayed types and compatibility equation.

**Scope.** The orthogonal direct-sum decomposition, nondegeneracy of every complement, well-definedness into the combined complement and the symplecticity and bijectivity of the displayed complement comparison, existence of the compatible model unitaries, the observable/decoder laws, phase independence and composition of compatible decoders are proof obligations. Compatibility is additional specified data and is not assigned to arbitrary independently chosen model unitaries. This datum is not scalar restriction, a generic field trace, a field support code or a non-bijective interpretation of finite-field Frobenius.

**Sources.** SP-STFIELD,SP-WAT18.

**Obligations.** SP-SUBSYS.

**Reuses.** D1701,D1703,D1706.

**Delta.** A nondegenerate symplectic subsystem and its trace-dual decoder, with the exact direct-versus-iterated model comparison and rank-zero unit types. It is not the support-code decoder of D1327.

## Why the iterated clauses are data rather than conclusions

The three complements are actual subspaces of their displayed ambient
spaces. The formula `(w,z) -> ell(w)+z` is a candidate comparison whose
symplectic isomorphism property remains an SP-SUBSYS obligation. Likewise,
the four unitary types and their Weyl equations specify what a compatible
choice means; the claim must prove such choices exist at its stated model
scope and that the phase cancels from inclusions and decoders. The definition
does not stipulate either decoder composition or inclusion composition.

## Narrow SP-FROB dependency proposal

The SP-FROB statement calls
$\rho\mapsto U_{E/K,n}\rho U_{E/K,n}^*$ an invertible channel. Add D1706 to
its Definitions/depends-on list and add SP-CP to its Dependencies/depends-on
list. Extend Reuse by exactly:

> SP-CP supplies only the ambient unitary-conjugation channel typing; the relative Frobenius covariance, inverse and finite power are separate SP-FROB calculations.

Do not change the SP-FROB statement, Scope, status, or its mathematical
dependencies SP-TRACE/FRB-TRACE/FRB-FROB. No CP fact is used to prove the
field permutation or Weyl covariance.
