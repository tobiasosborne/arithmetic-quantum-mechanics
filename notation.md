<!-- ROLE: the single source for symbols (L4). Every symbol used anywhere in
     theory/, checks/ or the labbook appears in this table exactly once. If a
     symbol is not here, it does not exist. -->

# Notation

| symbol | meaning | first fixed in |
|---|---|---|
| `p`, `m`, `q` | prime, degree, `q = p^m` for a finite field; in D1101, `q>0` is a real Hecke parameter with field specializations `q=Q` | D1, D1101 |
| `κ`, `F_p`, `k` | the finite field `F_q`, its prime field, and k as a bound field name; for D12, κ=R/𝔪 is the residue field | D1,D12; k used in D1104,D1701 |
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
| `W_β(v)` | Weyl basis element for the chosen cocycle; D1703 uses the same notation in arbitrary rank at β=ω/2; its concrete symmetrized model is W^s | D4,D16; extended in D1703 |
| `A_{ψ,β}(V)` | the twisted Weyl algebra; D1703 extends the field construction to arbitrary symplectic rank at β=ω/2 | D4,D16; extended in D1703 |
| `H_β(κ)`, `H_β(R)` | the Heisenberg groups `κ×V(κ)` and `R×V(R)` | D5, D16 |
| `F`, `F^{(p)}` | the Weyl frame; the level-`μ_p` frame | D7, D11 |
| `Aut_F(A)`, `Aut_F^κ(A)` | frame-preserving automorphisms; those with `κ`-linear `g` | D7 |
| `L`, `A_L` | a field line or local-ring submodule; its Weyl subalgebra | D8, D14, D16 |
| `χ`, `C_χ` | a character of `A_L`; its 1-dimensional module | D8, D16 |
| `M_{L,χ}`, `M₀` | Schrödinger model of `(L,χ)`; the field standard model | D8, D16 |
| `ℓ²(R)`, `e_y`, `X(a)`, `Z(b)` | local reference space; standard basis; shift and phase operators | D8, D16 |
| `Mod_{ψ,β}(κ)`, `PMod_{ψ,β}(κ)`; `Mod_{ψ,β_V}(V)`, `PMod_{ψ,β_V}(V)` | the rank-one model groupoid and its projectivization; their arbitrary-rank half-form extension | D9,D1703 |
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

<!-- Operational F1 subsystem notation. Trace normalization is explicit in each datum. -->

| symbol | meaning | first fixed in |
|---|---|---|
| `H_n(q), T_i, T_w, ell(w), tau_n` | type-A Hecke algebra, generators, permutation basis, Coxeter length, coefficient trace | D1101 |
| `iota_(m,n), E_(m,n)` | ordered block assembly and parabolic coefficient expectation | D1102 |
| `a(C;B_1,B_2), Tr_2` | intrinsic minimum rank-one overlap; ordinary M2 trace | D1103 |
| `Q, Fl(L), Cxt(L), A_w, tr_Fl` | finite-field cardinality, flags, context commutant, adjacency operators and normalized flag trace | D1104 |
| `e_triv, r_2` | marked trivial spectral projection and its reference probability | D1105 |
| `A_X, Tr_X, tau_X, d_X, j_X,Y, E_X,Y` | categorical endomorphism algebra, positive trace, normalized trace, dimension, assembly and expectation | D1121 |
| `omega, rho, h, Phi_K, T_K` | normalized functional, categorical/coefficient-trace density, Heisenberg channel and density channel (context determines the stated trace) | D1106,D1122,D1123 |
| `G(S), A(S), i_f, E_f, mu_S,T` | symmetric-group net and injection/expectation/assembly maps | D1125 |
| `J_K, FinPInj, R(f)` | Kraus Gram, partial-injection category and CP realization | D1126,D1127 |
| `alpha, W_alpha, P_alpha, e_alpha, Gamma_q, J_alpha` | partial-flag type, Young subgroup, Poincare polynomial, projection, corner category and incidence isometry | D1141 |
| `U^ann, P_U^X, P_U^Z, K_ctx(L), C_i, R(g)` | Weyl annihilator, constraint projections, context register, controlled tests and Levi action | D1142 |
| `z, Z_*, X_num, Y_anti, P_Bell, h_Bell` | standard S3 block and collective two-qubit operators/density | D1143 |
| `J_ap, Omega_Q` | coordinate-apartment isometry and its UCP context comparison | D1144 |

<!-- Operational categorical limit. Existing Hecke and Weyl symbols retain their definitions above. -->

| symbol | meaning | first fixed in |
|---|---|---|
| `b_w(q), B_w(q), K_n` | normalized Hecke basis, its regular matrix, and fixed regular Hilbert space | D1201 |
| `H_n^cts(I), tau_n^cts` | continuous positive section algebra and C(I)-valued trace | D1202 |
| `Gamma_I^cts, A_alpha(I), A_alpha(q)` | continuous parabolic category and its section/fibre endomorphism corners | D1203 |
| `Gamma_1^germ, I_epsilon` | endpoint corner germ category and a representative interval | D1204 |
| `[alpha], underline(O), tau_O` | quantum atom, nonempty classical outcome wire, uniform classical trace | D1205 |
| `HCPU_fd, Phi_*` | category of quantum processes in Heisenberg orientation and normalized-trace density dual | D1206 |
| `K_(o,i), prep_h, disc_X, M_e` | retained instrument list, preparation, discard and POVM maps | D1207 |
| `asm, spl` | typed collective assembly and split, realized by expectation and inclusion | D1208 |
| `triangleleft, boxtimes_c` | retained right context and ordered collective parallel process | D1209 |
| `Op_q, Op_I^cts, Op_1^germ, Real_q, Ev_q` | presented circuit categories, operational realization and evaluation | D1210,D1211 |
| `N(q), D(q)` | event numerator and conditioning-event probability in a specified finite protocol | D1212 |
| `Khat, S, Ktilde, Btilde_h` | raw lift, completeness operator, normalized lift and explicitly embedded recovery basis | D1213–D1215 |
| `P_2, gamma(q), u_1` | named level-three Lüders effect, standard-block trace coefficient and retained local unitary | D1217 |
| `rel_r, mul_(O,P), unit_cl, route_(O,X), Seq, Par, chi` | explicit classical relabeling/product/unit/routing, routed instruments and history interchange | D1218 |
| `C[A_*], SW_fin(A_*), Proj_*(A_*)` | multiplicative-sequence skeleton, finite right-module Day category and positive projection completion | D1221–D1223 |
| `U_R, U_q, Y_q, DM_fin(v)` | generic self-adjoint envelope, positive Hecke completion, parabolic embedding and algebraic DM comparison | D1224–D1227 |
| `v, t_i, u_i` | positive square-root parameter, DM generator and physical spectral-sign exchange | D1226,D1228 |
| `D_n, J_n, sigma_(m,n)` | longest Hecke element, its polar reversal and the unitary coboundary commutor | D1229,D1230 |
| `rho_(d,n), P_sigma, nu_(m,n), tr_(d,n), E_(d,K)` | Schur–Weyl map, tensor permutation, quotient assembly, physical trace and expectation | D1232–D1235 |
| `i:U_q->R, R_d, I, Neg, tr_J` | named rigid comparison, concrete target, tensor/negligible ideals and Jones trace | D1236,D1237 |
| `f_i, delta, q_H, q_ILZ, U_i^(ILZ)` | TL idempotent, loop parameter and explicitly translated Hecke/ILZ root conventions | D1238,D1239 |
| `Aff(L), Y_L, R_X(L), R_n(q)` | affine group, flag-vector set, arithmetic commutant and based mirabolic algebra | D1241,D1246 |
| `C_i^X, C_i^Z, Ctx_X(L), T_0` | controlled X/Z constraints, their generated algebra and mirabolic boundary generator | D1242 |
| `F_(L,psi), D_L, W_(L,psi), PMir_(k,psi)` | vector Fourier map, dual-flag reversal, joint unitary and named comparison groupoid | D1243,D1244 |
| `prec_w, down_w(A), T_(w,A)` | permutation poset, antichain downset and mirabolic orbital basis | D1245 |
| `i_q, E_q, Pi_n, N_(tau_1)` | Hecke inclusion, vector expectation, endpoint quotient and trace-null ideal | D1247,D1248 |
| `J_epsilon, RegOp_J, RegOp_(1+), Q_X, Ev_(1+)` | one-sided regular interval, operational categories, product quotient and boundary functor | D1249,D1257,D1258 |
| `X_C(V), A_C(V), Sh, J_(V,W), p_(V,W)` | isotropic flags, type-C commutant, shuffles, decomposable isometry and projection | D1250,D1251 |
| `H_(V,W), D_(V,W), r_(V,W), Phi_(V,W), Psi_(V,W)` | local symmetry, its composition arena, corner fraction and trace-adjoint UCP correspondence | D1252,D1253 |
| `p^aff_(L,M)` | projection onto decomposable flags with every vector label retained | D1256 |
| `U_I^cts, U_q^dagger, p_(X,n), r_n, U_1^germ` | full finite graded continuous/fibre/germ projection completions and their presentations | D1261,D1262,D1265 |
| `theta_X, w_X` | full graded trace and its positive weight on the identity; w_X is distinct from fusion dimension d_X | D1263 |
| `B_X, j_(X,Y), E_(X,Y), Op^U_q, Op^U_I, Op^U_1,germ` | completed endomorphism systems, traced assembly/retraction and their operational categories | D1264,D1266 |

| symbol | meaning | first fixed in |
|---|---|---|
| `H_E, psi_E, S_E, Omega_E` | trace-framed field register and its prime-field symplectic space | D1301 |
| `X_E(a), Z_E(b), W_E(a,b)` | reference translations, phases and D8 Weyl operators on the named register | D1301 |
| `sigma_E, U_E` | field Frobenius and its computational-basis permutation | D1302 |
| `T_i, kappa_i` | transported relative trace of a named embedding and its kernel cardinality | D1303 |
| `J_i, V_i` | inclusion and normalized trace-fibre transfers | D1304 |
| `C_i, P_i, N_i, G_i` | subfield support code, projector, isotropic phase labels and phase stabilizers; embedding subscript distinguishes these from flag indices | D1305 |
| `F_E` | negative-kernel Fourier transform on the named field register | D1306 |
| `P_A, C_k(A)` | full-scalar Pauli group and hierarchy on an ordered arithmetic word; D1704 uses this same C_2(A) on repeated prime-field atoms | D1307; reused in D1704 |
| `M_E^(d)` | multiplication into a separate target register, with d separate controls | D1308 |
| `D_f, delta_h f` | diagonal phase and backward additive difference | D1309 |
| `(u,v)=u+vb` | coordinates in the named binary degree-four tower | D1310 |

| symbol | meaning | first fixed in |
|---|---|---|
| `I, F, R_p` (arithmetic-process context) | finite named field diagram, its field set, scalar field Q(zeta_p,sqrt(p)) | D1321 |
| `Q_E, C_i, X` (arithmetic register context) | field atom, ambient-labeled code atom, ordered quantum word | D1321 |
| `A_I; w_E,f_E,u_E,m_(E,d),j_i,v_i,e_E,t_i,c_i` | amplitude presentation and its typed generators | D1322,D1323 |
| `H` (arithmetic interpretation) | amplitude interpretation in finite Hilbert spaces | D1324 |
| `Proc_I, k_(b,a,j), h_(a,l)` | source-certified process category, Kraus amplitudes, residual certificate amplitudes | D1325 |
| `B_X, Tr_X, R` (arithmetic process context) | block matrix algebra, sum of ordinary traces and CP interpretation; D1706 extends B_X and Tr_X to arbitrary Hilbert block families, while R remains the arithmetic interpretation | D1326; target extended in D1706 |
| `p_s,q_s,D_s,d_s,a^[i],a_B` | range/complement projections, retained decoder, success arrow, code lift, named coordinate circuit | D1327 |

| symbol | meaning | first fixed in |
|---|---|---|
| `t, mu, phi, c_d(t)` (orbit context) | real continued characteristic parameter; integer Moebius and Euler functions; exact-period point-count polynomial | D1331 |
| `O_r, S_d, u_r, R_(p,r), b_O` (orbit context) | common matrix blocks by orbit length; cyclic shift; Frobenius; marked physical representation; chosen orbit origin | D1331 |
| `e_r, O_r^+, u_r^+, theta_(r,t), w_r(t), omega_(r,t)` | nonfixed-label corner, its algebra and unitary, ambient reference functional, weight and conditional functional | D1332 |
| `lambda_(r,d), sigma_(r,t), P_r^mov` | conditional block weight, ordinary-trace reference density, physical nonfixed-label projection | D1332 |
| `O_R^+, omega_(R,t), W_R, e_(r,s), j_(r,s), h_(r,s), B_(d,e)` | word algebra/reference/ambient weight; inclusion cut/encoding/success weight; coherent cycle-pair reblocking | D1333 |
| `P_(E,d)^nz, tau_(E,d), v_(E,d), tau_(E,d)^nz, P_A^nz, P_r^dual` | nonzero-control cut, whole-word trace, restricted multiplication, corner trace, subset cut, Fourier-dual moving-label cut | D1334 |

| symbol | meaning | first fixed in |
|---|---|---|
| `Gamma_r^sgn, A_d^sgn, B_d^sgn, J_2(m)` | Frobenius/negation action on nonzero labels; candidate internal/external point counts; second Jordan totient | D1441 |


| symbol | meaning | first fixed in |
|---|---|---|
| `Omega=K^sep, G_K, Et_K^+, r_f` | named separable closure, absolute Galois group, constant-positive-rank finite etale category, arrow rank | D1401 |
| `X_A,n_A,H_A^emb,B_A^emb,U_A^emb,rho_A^mix` | embedding set, K-dimension, counting Hilbert space, full observable algebra, Galois unitary, maximally mixed density | D1401 |
| `R_f,s_f,mu_(A,C),W_(eta,A),c_eta` | restriction of embeddings, normalized fibre isometry, tensor comparison, closure-change unitary and conjugation | D1402 |
| `P_f,Q_f,E_f,d_f,D_f` (embedding context) | range/complement projections, encoding, success map, retained embedding decoder | D1403 |
| `H_(A,tau_0),C_A,N_A` | embedding stabilizer, its normal core, compositum normal closure | D1404 |
| `Frob_p,O_b,T_a,L_(tau_0)` | arithmetic Frobenius on the closure, primitive orbit, evaluation comparison, named cyclic coordinates | D1405 |


| Symbol | Meaning | Owner |
|---|---|---|
| `Gamma_i`, `Ptilde_i`, `S_i`, `E_i` | Gram map, trace-code projection, joint range, joint-support projection | D1421 |
| `tau_E` (joint-code context) | Normalized physical matrix trace; q,Q keep their field-cardinality meanings | D1421 |
| `\|+_K>`, `R_K` | Uniform vector, additive reflection | D1421 |
| `D_a^K`, `L_i`, `c_i,h_i`, `W_i`, `mathcal T_i`, `B_i` | Scalar dilation, corrected trace map, angle data, orthogonal second column, frame, logical Fourier factor | D1422 |
| `alpha_i,beta_i,d_i,e_i`, `A_K`, `mathcal T_i^ang,mathcal T_i^res` | Singular-degree sectors and frames | D1423 |
| `p_c,q_c,f_c,d_c`, `tr_2` | Conditioned chart projections, Fourier, tangent and trace | D1424 |
| `mathcal T_path`, `C_(c_l,...,c_1)`, `c_*,h_*`, `v_r` | Iterated frame and direct-to-path connector | D1425 |
| `K_b(t)`, `D_S` | Continuous Kraus amplitudes and retained decoder | D1426 |
| `C_a(t)`, `a_r,A`, `\|one_r>` | Weighted endpoint connector, weights and excitation basis | D1427 |


| symbol | meaning | definition |
|---|---|---|
| `h,t=exp(h), b_d(t), P_(E,0), P_(E,d)^times` | interpolation variable, nonzero period count, zero and period projections | D1501 |
| `D_E,rho_E,D_word,rho_word,R` | unnormalized density, reference state and ordered products, total absolute degree | D1501 |
| `J_k(d),A_(E,k),B_E,sigma_(E,k),A_(word,k),sigma_(word,k)` | positive Jordan coefficient, reference coefficient, first coefficient and normalized coefficient states | D1502 |
| `L_E,L_word,lambda_word,P_S,B_S` | finite reference profile, normalized preparation and nonzero support masks | D1503 |
| `(Phi,Z),z_k,Phi_k` | positive-series process representative, normalizer and CP coefficients | D1504 |
| `Phi_*A,(X,A)` | coefficientwise arithmetic action and profile experiment | D1505 |
| `v(A),M(A),w(A),eta(A)` | leading order, matrix, probability coefficient and conditional state | D1506 |
| `w_x` (positive mixed protocol) | diagonal weight of B_E at a nonzero label x, equal to phi(period(x))/b_(period(x))(p) | POS-MIXED |

| symbol | meaning | definition |
|---|---|---|
| `A_I^mat`, `(X,e)` | concrete arithmetic matrix image and its finite additive/self-adjoint projection completion | D1601 |
| `sigma`, `U`, `O`, `v_(O,k)` (relational context) | relative q-Frobenius, its field permutation, an orbit, and its normalized multiplication-graph vector | D1602 |
| `G_(d,k)`, `G`, `Delta`, `T` (relational context) | diagonal orbit-graph tests, their sum, simultaneous Frobenius and its complex invariant average | D1602 |
| `P`, `P_d`, `Q_(d,k)`, `H_(E/K)^rel` (relational context) | full relational projection, period and relative-index projections, and their Hilbert register | D1602 |
| `C` (copied graph context) | arithmetic isometry mapping x to the tuple (x,x,x^2), defined for every relative degree n>=1 | D1602 |
| `R`, `E_(d;a,b)`, `B_(E/K)^rel`, `B_n`, `u_n^rel` | multiplication-conjugated relative Frobenius, common matrix units, generated/common algebras and all-period cycle implementer | D1603 |
| `Pi_n`, `K_cut`, `K_fail`, `K_ok` (relational context) | primitive relative-period test and the three retained preparation amplitudes | D1604 |
| `w_(s,n)(h)` | copied-reference primitive success c_n(exp(s h))/(n exp(sn h)) for n>1 | CMP-BOUNDARY |
| `J_i^rel`, `F_first`, `D_phase` | fixed-base relational inclusion, actual first-register Fourier and its compressed orbit phase | D1606, CMP-FOURIER |

| symbol | meaning | definition |
|---|---|---|
| `A_N`, `j_(N,M)`, `eta_d`, `theta_N` (degree completion) | finite moving divisor-block algebra, zero-extension corner, weight phi(d)/d and its trace | D1611 |
| `H_deg`, `A_deg`, `B_deg`, `theta` | Hilbert sum of primitive degree registers, c0 block algebra, minimal unitization and extended positive trace on A_deg | D1611 |
| `U_deg`, `alpha` (degree completion) | direct sum of actual relative cycles and its quantum automorphism | D1612 |
| `beta`, `Z_deg(beta)`, `D_beta`, `rho_beta`, `omega_beta`, `M_beta(j)` (degree regularization) | real exponent >1, moving-degree normalizer, central regulator, trace-class density, state and implementing-operator moment | D1612 |

| symbol | meaning | definition |
|---|---|---|
| `L_D(beta)`, `L_infty(beta)`, `pi_d` | finite/infinite degree-prior normalizers and the finite classical degree probabilities | D1621 |
| `w_d(t)`, `v_d(t)`, `Z_D(beta,t)`, `Z_infty(beta,t)` | exact primitive success, its rescaling by s(t-1), and common successful mixture normalizers | D1621 |
| `rho_(D,t)`, `rho_(infty,t)`, `W_D(beta,t)` | finite/completed common conditional densities and total physical mixture success | D1621, CMP-JOINT-LIMIT |

## Symplectic Phantasm — shared notation, revised 2026-09-10

Existing Weyl algebras/generators, Pauli groups, hierarchy levels and
ordinary block traces retain their owning rows above. No second definition
is created by their use in the quest. Bound variables may be reused in
separate typed formulas; the fixed character psi_E is not a freely chosen
base character. The following rows own only the additional names.

| symbol | meaning | first fixed in |
|---|---|---|
| `omega_V`, `overline V`, `n` (symplectic rank) | form on an arbitrary-rank space, its sign reversal and half the phase-space dimension | D1701 |
| `S_k`, `S_k^aff`, `(t,g)` | linear and affine symplectic groupoids; v maps to gv+t; the direct sum of affine arrows is prescribed in D1701 | D1701 |
| `L_k^aff`, `Delta_V`, `R dagger` | affine Lagrangian relation candidate, including empty relations; diagonal and converse | D1702 |
| `tau_V`, `beta_V` | coefficient trace and half-form cocycle in the existing Weyl algebra notation | D1703 |
| `H_(k,n)`, `W^s_(k,n)(a,b)` | coordinate Hilbert tensor of n existing k-registers; symmetrized operator with the same position labels as D8, related by the positive half-dot phase; W^s_V denotes its coordinate transport | D1703; D1710 for abstract-space models |
| `Stab_p^amp` | category generated by the existing C_2(A), computational preparations and actual complex scalars; equality of actual maps | D1704 |
| `Stab_p^proj`, `[T]` | quotient by invertible complex scalars with a distinct zero class | D1705 |
| `K_(b a,j)`, `Phi_o`, `Phi^(tr*)` (ambient CP target) | actual Hilbert Kraus maps, outcome maps and the ambient ordinary-trace adjoint; B_X and Tr_X reuse the D1326 row; distinct from D1206's normalized-trace density dual | D1706 |
| `Mat(span_C Stab_p^amp)` | the specified coherent matrix completion; not the arithmetic R_p syntax or graded Hecke completion | D1707 |
| `P_i^X`, `Delta_X` (coherent list) | ordered-summand projection and block-dephasing endomorphism; distinct from D1305 support-code projectors and D1713 modular operators | D1707 |
| `P_r`, `U_pi`, `Sym^r H`, `Gamma_s(H)`, `Omega`, `N_H` (Fock) | symmetrizer, permutation action, symmetric sector, Hilbert Fock sum, vacuum and particle number; the one-mode polynomial completion is already F_bos in D1010 | D1708 |
| `Res_(E/K)V`, `omega_Res`, `chi_K`, `chi_(E/K)` | scalar restriction, trace form, named general base character and its relative-trace composite; neither character symbol replaces the fixed psi_E family | D1709 |
| `sigma_(E/K)`, `varphi_V`, `U_(E/K,n)` | relative field power, named abstract semilinear datum and tensor of powers of the existing U_E | D1709 |
| `j`, `J`, `iota_J`, `D_J` (nondegenerate subsystem) | symplectic injection, compatible model unitary, observable inclusion and trace-dual decoder; distinct from a field support-code success map | D1710 |
| `P`, `A_P`, `iota_QP`, `A_pr`, `varphi_pr`, `d_p`, `rho_p` (prime tensor assembly) | finite prime set, finite tensor algebra, unital embedding, norm completion, product reference and chosen local dimensions/densities | D1711 |
| `H_BC`, `A_BC^rep`, `e(r)`, `mu_n`, `H_log`, `nu_n`, `L_n`, `Z_BC(b)`, `rho_(BC,b)` | represented BC benchmark, phase and semigroup operators, logarithmic energy, corner and adjoint maps, partition sum and density | D1712 |
| `b`, `u`, `sigma_u` (real dynamics) | inverse temperature, time and physical automorphism flow; these are bound real variables, not Weyl labels or field Frobenius | D1712,D1713 |
| `N_varphi`, `H_varphi`, `pi_varphi`, `Omega_varphi`, `M_varphi`, `S_varphi`, `J_varphi`, `Delta_varphi` | GNS and modular data under the stated cyclic/separating hypothesis | D1713 |
| `alpha_(t,g)` | affine Egorov star-isomorphism on the existing Weyl generators | SP-EGOROV |
| `a_(U,V,W)`, `lambda_V`, `rho_V`, `sigma_(V,W)` (relation coherence) | zero-translation affine tuple coherence maps and their graph associator, left/right unitors and swap | D1701,D1714 |
| `eta_V`, `epsilon_V`, `ulcorner R urcorner`, `llcorner Q lrcorner` (compact relations) | opposite-form diagonal cup/cap and fully typed name/unname prescriptions | D1714 |
| `V_n`, `omega_n`, `Omega_(m,n)` (stabilizer relation coordinates) | bound names for the existing standard prime-field symplectic spaces/forms and signed source-target form | D1703,D1715 |
| `E_p(R)` (stabilizer intertwiners) | origin-free complex space cut out by the Weyl intertwining equations; its line and functor properties belong to SP-STAB-REL | D1715 |
