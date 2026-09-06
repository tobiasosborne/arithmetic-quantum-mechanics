<!-- ROLE: the single source for symbols (L4). Every symbol used anywhere in
     theory/, checks/ or the labbook appears in this table exactly once. If a
     symbol is not here, it does not exist. -->

# Notation

| symbol | meaning | first fixed in |
|---|---|---|
| `p`, `m`, `q` | prime, degree, `q = p^m` | D1 |
| `κ`, `F_p` | the finite field `F_q` and its prime field; for D12, `κ=R/𝔪` is the residue field | D1, D12 |
| `R`, `𝔪`, `R^×` | a finite commutative local ring; its maximal ideal; its unit group | D12 |
| `soc(R)`, `Ann(I)` | `Ann(𝔪)`; the annihilator of an ideal `I` | D12 |
| `V(κ)`, `V(R)` | `κ⊕κ`; `R⊕R`, the field and local-ring symplectic objects | D1, D14 |
| `v = (a,b)` | a vector of the current `V(κ)` or `V(R)` | D1, D14 |
| `ω` | `ω((a,b),(a',b'))=ab'−a'b` over the current `κ` or `R` | D1, D14 |
| `B_ψ`, `rad(B_ψ)`, `L^{⊥_ψ}` | `ψ∘ω`; its radical; phase-perpendicular of an `R`-submodule | D14 |
| `L_*` | the non-free Lagrangian `soc(R)⊕𝔪` when `R` is not a field | FCR-POL |
| `Adm(ω)` | the admissible polarizing cocycles over the current `κ` or `R` | D2, D15 |
| `Sym(V)`, `Sym_R(V(R))` | symmetric bilinear forms over `κ`; over `R` | D2, D15 |
| `s`, `φ_s` | a symmetric form; `(t,v)↦(t+s(v,v)/2,v)` when `2∈R^×` | FCR-BETA-ODD |
| `β`, `β₀` | a chosen polarizing cocycle; the reference one `ab'`, over the current base | D2, D15 |
| `Q_β` | `Q_β(v) = β(v,v)` | D6 |
| `℘`, `Arf` | `℘(x) = x²+x`; the type `Q_β(e)Q_β(f) ∈ κ/℘(κ)` | D10 |
| `ε` | the sign in `q^{-1}Σ_v W_β(v)² = ε·1` at `p = 2` | D10 |
| `ψ` | a nontrivial additive character of the current `(κ,+)` or `(R,+)` | D3, D13 |
| `X(κ)` | the set of nontrivial additive characters | D3 |
| `R̂`, `X(R)`, `ψ_u` | all additive characters of `R`; the nontrivial ones; `ψ(u·)` | D13 |
| `I_ψ`, `Gen(R)` | largest ideal in `ker ψ`; the generating characters | D13 |
| `κ̂`, `V̂` | `Hom((κ,+),C^×)`, `Hom((V,+),C^×)` | D3 |
| `ζ` | a primitive `p`-th root of unity in `C` | D3 |
| `ψ_ζ`, `Tr_{κ/F_p}` | `ζ^{Tr(·)}`; the absolute trace | D3 |
| `μ_p`, `μ_4`, `U(1)` | `p`-th, 4th roots of unity; unit circle | D3 |
| `W_β(v)` | Weyl operator / basis element of `A_{ψ,β}(V)` over the current base | D4, D16 |
| `A_{ψ,β}(V)` | the twisted Weyl algebra over the current base | D4, D16 |
| `H_β(κ)`, `H_β(R)` | the Heisenberg groups `κ×V(κ)` and `R×V(R)` | D5, D16 |
| `F`, `F^{(p)}` | the Weyl frame; the level-`μ_p` frame | D7, D11 |
| `Aut_F(A)`, `Aut_F^κ(A)` | frame-preserving automorphisms; those with `κ`-linear `g` | D7 |
| `L`, `A_L` | a field line or local-ring submodule; its Weyl subalgebra | D8, D14, D16 |
| `χ`, `C_χ` | a character of `A_L`; its 1-dimensional module | D8, D16 |
| `M_{L,χ}`, `M₀` | Schrödinger model of `(L,χ)`; the field standard model | D8, D16 |
| `ℓ²(R)`, `e_y`, `X(a)`, `Z(b)` | local reference space; standard basis; shift and phase operators | D8, D16 |
| `Mod_{ψ,β}(κ)`, `PMod_{ψ,β}(κ)` | the model groupoid; its projectivization | D9 |
| `P(H_ψ(κ))` | the canonical projective Hilbert space | D9 |
| `P¹(κ)` | the projective line: the `q+1` lines of `V(κ)` | D1 |
| `SL_2(κ)` | `κ`-linear automorphisms of `V(κ)` of determinant 1 | D1 |
| `Sp_{2m}(F_p)` | isometries of the `F_p`-form `ψ∘ω` on `V(κ)` | D7 |
| `O(Q_β)` | `{ g : Q_β ∘ g = Q_β }` | D6 |
| `s_g`, `Q_g` | `s_g(v,v') = β(gv,gv') − β(v,v')`; `Q_g(v) = s_g(v,v)` | D7 |
| `E` | the Weyl average `|V|^{-1}Σ_uW(u)(·)W(u)^{-1}` over the current base | D4, FCR-ALG |
| `FF^±` | pairs `(κ,ψ)` and character-compatible embeddings | D3 |

<!-- F1 sidequest notation. N is phase order, distinct from q, the field cardinality. -->

| symbol | meaning | first fixed in |
|---|---|---|
| `N, mu_N, iota` | cyclotomic level, abstract cyclic phase group, named faithful complex character | D1001 |
| `A, A^vee, V_A, c_A, kappa_A` | finite abelian configuration, phase dual, hyperbolic phase group, cocycle and commutator | D1002 |
| `Free_*^{mu_N}, C_iota, S_A, H_N(A)^0` | pointed phase category, complex realization, standard phase module and group-with-zero | D1001, D1003 |
| `H_N(A), FinAb_N^iso, smash_mu, boxdot` | phase Heisenberg group, configuration groupoid, balanced smash and central product | D1003, D1004 |
| `P_psi, chi_b` | central pushout, signed ring-dual character psi(-b·) | D1005 |
| `theta, B_theta, T_(t,f,theta), F_A, J_A, r_A, ev_a` | quadratic phase and strict normalizer; Fourier map and lifted dual exchange | D1006 |
| `K_N, Mat(K_N), PMat(K_N), LiftHyp_N, Q_N` | cyclotomic coefficient field, framed kernel categories, lifted phase groupoid and projective realization | D1007 |
| `B, N_B, F_1^pm, K, H_crowd, R_H` | band, null ideal, regular partial field, Krasner hyperfield, Heisenberg crowd and colaw | D1008 |
| `F_N, P_N(r)` | cyclotomic scalar monoid and projective Cartesian frame | D1009 |
| `V_r, L(S), B(S), u_r, F_alg, F_bos, a^dagger` | rank-r pointed set, its Hilbert/image-algebra realization, Hall basis, Fock domain/completion and creation | D1010 |
| `C_N(A), C_N(A)_lambda, omega_A, boxtimes_match` | representation category, central sector, forgetful tensor functor and matching external product | D1011 |
| `G_e, sigma_e, nu_2` | order-eight dihedral/quaternion datum, qubit representation and indicator | D1012 |
| `xi, T_xi, T_xi(1,1)` | quantum-torus parameter, algebra and selected central fibre | D1013 |
