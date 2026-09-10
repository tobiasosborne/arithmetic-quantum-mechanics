# Completion ownership candidates

Preparation date: 2026-09-10. Model: `gpt-5.6-sol`, reasoning `xhigh`.

This file proposes complete D1708 and D1711 replacements before the bounded
completion prover pass. It states data and extension obligations only. It
does not assert unitarity, naturality, strong monoidality, coherence,
inductive-limit existence, state extension, arithmetic coupling or modular
properties.

## Proposed complete D1708

## D1708 (bosonic Fock space and bounded second quantization)

For a complex Hilbert space $H$, let
$P_r=(r!)^{-1}\sum_{\pi\in S_r}U_\pi$, where
\[
 U_\pi(h_1\otimes\cdots\otimes h_r)
 =h_{\pi^{-1}(1)}\otimes\cdots\otimes h_{\pi^{-1}(r)},
\]
and set $\operatorname{Sym}^rH=\operatorname{ran}P_r$, with
$\operatorname{Sym}^0H=\mathbb C$. Define
\[
 \Gamma_s(H)=\widehat{\bigoplus}_{r\geq0}\operatorname{Sym}^rH,
 \qquad\Omega=1\in\operatorname{Sym}^0H.
\]
The hat means Hilbert direct sum. The algebraic finite-particle space is
$\bigoplus_{r\geq0}^{\mathrm{alg}}\operatorname{Sym}^rH$.
For a contraction $T:H\to K$, prescribe
\[
 \Gamma_s(T)=\bigoplus_{r\geq0}
 T^{\otimes r}|_{\operatorname{Sym}^rH}.
\]
Particle number is the operator $N_H\xi=(r\xi_r)_r$ on the domain
$\{\xi:\sum_r r^2\|\xi_r\|^2<\infty\}$.

For Hilbert spaces $H,K$, prescribe the coordinate inclusions
\[
 \jmath_H:H\longrightarrow H\oplus K,\quad h\longmapsto(h,0),
 \qquad
 \jmath_K:K\longrightarrow H\oplus K,\quad k\longmapsto(0,k).
\]
On the algebraic tensor product of the two algebraic finite-particle spaces,
prescribe the complex-linear homogeneous map
\[
 \mathsf{Exp}^{\mathrm{alg}}_{H,K}:
 \left(\bigoplus_{n\geq0}^{\mathrm{alg}}\operatorname{Sym}^nH\right)
 \odot
 \left(\bigoplus_{m\geq0}^{\mathrm{alg}}\operatorname{Sym}^mK\right)
 \longrightarrow
 \bigoplus_{r\geq0}^{\mathrm{alg}}\operatorname{Sym}^r(H\oplus K)
\]
by, for $\xi_n\in\operatorname{Sym}^nH$ and
$\eta_m\in\operatorname{Sym}^mK$,
\[
 \mathsf{Exp}^{\mathrm{alg}}_{H,K}(\xi_n\otimes\eta_m)
 =\sqrt{\frac{(n+m)!}{n!m!}}\,
 P^{H\oplus K}_{n+m}
 \left((\jmath_H^{\otimes n}\xi_n)
 \otimes(\jmath_K^{\otimes m}\eta_m)\right).
\]
The square root is the positive real one, and the tensor inside the
projection has all $H$ slots before all $K$ slots. Prescribe
\[
 \mathsf{Exp}^{\mathrm{alg}}_{H,K}(\Omega\otimes\Omega)=\Omega,
\]
When $K=0$, use $\operatorname{Sym}^0(0)=\mathbb C$ and prescribe the formula
on $\xi_n\otimes\Omega$ to agree with the standard identification
$\operatorname{Sym}^nH\cong\operatorname{Sym}^n(H\oplus0)$; use the
analogous left-unit identification when $H=0$.
If the algebraic map extends boundedly to the Hilbert completions, denote
that extension by
\[
 \mathsf{Exp}_{H,K}:\Gamma_s(H)\otimes\Gamma_s(K)
 \longrightarrow\Gamma_s(H\oplus K).
\]
The comparison in the direction
$\Gamma_s(H\oplus K)\to\Gamma_s(H)\otimes\Gamma_s(K)$ is
$\mathsf{Exp}_{H,K}^*$ whenever the extension is unitary.

**Scope.** Boundedness and functor laws for $\Gamma_s(T)$ are obligations. Well-definedness on symmetric sectors, isometry and unitary extension of $\mathsf{Exp}^{\mathrm{alg}}_{H,K}$, and naturality of the completed map are obligations; neither unitarity nor naturality is stipulated. No bounded second quantization of an arbitrary expansive map, strong-monoidal/coherence structure, or unspecified categorical free-monoid property is imposed.

**Sources.** SP-DER06.

**Obligations.** SP-FOCK,DG-RIG.

**Reuses.** D1010.

**Delta.** General Hilbert-space symmetric Fock functor and its contraction domain, together with the directed normalized homogeneous exponential-law candidate and its vacuum/zero-unit conventions. D1010 already names the one-mode polynomial domain and its completion.

### Checked source locators outside the canonical body

SP-DER06 `derezinski.tex` lines 1814--1829 own
the completed tensor Fock space and vacuum; 1843--1851 give second
quantization and its boundedness boundary; 1911--1964 define symmetric Fock
sectors; 2019--2038 restrict second quantization to them; and 2051--2090 give
the same tensor-to-direct-sum exponential direction, positive factorial
normalization, vacuum, unitary extension and natural operator square. The
last two properties remain obligations here rather than stipulations.

## Proposed complete D1711

## D1711 (finite-prime tensor assembly with a chosen reference)

For every prime $p$, choose an integer $d_p\geq1$, a Hilbert space
$H_p=\mathbb C^{d_p}$ and a positive operator $\rho_p$ of trace one.
For a finite set of primes $P$, put
\[
 A_P=\bigotimes_{p\in P}^{\nearrow}\operatorname{End}(H_p),
 \qquad A_\varnothing=\mathbb C,
\]
where $\nearrow$ means increasing prime order. For $P\subseteq Q$ and an
increasing-prime simple tensor, prescribe
\[
 \iota_{QP}\!\left(\bigotimes_{p\in P}^{\nearrow}a_p\right)
 =\bigotimes_{q\in Q}^{\nearrow}b_q,
 \qquad
 b_q=\begin{cases}
 a_q,&q\in P,\\
 1_{H_q},&q\in Q\setminus P.
 \end{cases}
\]
Extend $\iota_{QP}:A_P\to A_Q$ complex-linearly from simple tensors. For the
empty stage prescribe
\[
 \iota_{Q\varnothing}(c)
 =c\bigotimes_{q\in Q}^{\nearrow}1_{H_q},
 \qquad c\in\mathbb C,
\]
including $\iota_{\varnothing\varnothing}=1_{\mathbb C}$.
Define the candidate norm completion
$A_{\mathrm{pr}}=\overline{\varinjlim_P A_P}^{\|\cdot\|}$ using the finite
matrix norms. On finite tensors prescribe
\[
 \varphi_{\mathrm{pr}}\!\left(
 \bigotimes_{p\in P}^{\nearrow}a_p\right)
 =\prod_{p\in P}\operatorname{Tr}(\rho_pa_p).
\]

**Scope.** The homomorphism, injectivity, isometry, inductive-limit and state-extension properties are obligations. The matrices and increasing-order identity insertions are specified data, not yet an all-prime Weyl assignment or arithmetic coupling. Neither inter-prime arithmetic maps, a factor type, separating cyclicity nor modular data are supplied.

**Sources.** SP-CM08,SP-WAT18.

**Obligations.** SP-PRIME,DG-GLOBAL.

**Reuses.** D1706.

**Delta.** A specified unital finite-prime tensor system and reference with an explicit increasing-order identity-insertion formula, linear extension and empty stage; it is not the nonunital degree-block completion of D1611 and adds no arithmetic coupling.
