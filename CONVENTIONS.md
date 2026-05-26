# CONVENTIONS - arithmetic-quantum-mechanics

<!--
ROLE: Notational, sign, grading, gauge, modelling, tolerance, and data-layout
      choices specific to this repository.
UPDATE POLICY: New conventions are appended with explicit reasoning. Changing
      an existing convention requires a sweep of every file that follows it.
TRIGGER: Any new representational choice; any imported content that uses a
      non-canonical convention.
-->

## Status

Initial scaffold declared on 2026-05-24. The project has not yet fixed
substantive zeta-function, supersymmetric-QM, or lattice-model conventions.
Until an entry below fixes a convention, report text must state the convention
as unknown or source-dependent.

## (a) Claim Status Labels

Every substantive statement in the report should be readable as one of:

| Label | Meaning |
|---|---|
| `Question` | A research question with no asserted truth value. |
| `Proposal` | A working construction or analogy awaiting evidence. |
| `Source-local` | A claim copied or paraphrased from a registered local source. |
| `Checked` | A claim verified by a local derivation, test, or run artifact. |
| `Rejected` | A proposal ruled out by a local source, derivation, or run. |

Reasoning: the project deliberately spans arithmetic geometry, quantum
mechanics, and topological lattice models; status labels prevent analogies from
being mistaken for results.

## (b) Report Master And Shard IDs

`report.tex` is the only LaTeX master. It should contain the preamble, global
macros, include order, bibliography hook, and `\end{document}`. Body prose
belongs in `report/sections/*.tex`.

Shard IDs have the form `AQM-NN-SHORT-LABEL`, where `NN` matches the two-digit
filename prefix. The stable source maps are `report/README.md` and
`report/SHARD_CATALOG.md`.

## (c) Source Manifests

Every source topic under `references/<topic>/` should contain a `SOURCES.md`
manifest. Each acquired source entry should record:

| Field | Required content |
|---|---|
| Citation key | Stable local key used in notes. |
| Bibliographic data | Author, title, venue/version, year. |
| Locator | DOI, arXiv ID, URL, ISBN, or other access route. |
| Retrieved | Date acquired in `YYYY-MM-DD` format. |
| Local file | Relative path under `references/`. |
| SHA256 | Hash of the stored source file or snapshot. |
| Notes | Relevant theorem/equation/section locators. |

Fetched source files are append-only. Corrections go in the manifest or a new
snapshot, not by editing the fetched file.

## (d) Run Bundles

Generated artifacts live under:

```text
runs/<YYYY-MM-DD>-<slug>/
  README.md
  data/
  figures/
```

The slug is lowercase kebab case and names the question being probed. Top-level
`data/` and `figures/` are documentation placeholders, not output targets.

## (e) CSV Sentinel Comment Lines

A CSV row whose first column begins with `#` is a sentinel comment line, not
data. It carries caveats such as supersession status, negative-control status,
or missing-tool status. Parsers must skip such rows and schema entries must
document them.

## (f) Tool Dispatch

`scripts/run_all.jl` is the canonical local driver. Registered entries declare
their tool explicitly when the extension is ambiguous. Supported initial tools:

| Tool | Executable | Use |
|---|---|---|
| Julia | `julia` | Numerical linear algebra, package tests, plotting helpers. |
| Sage | `sage` | Exact arithmetic, finite fields, zeta examples, algebraic geometry probes. |
| GAP | `gap` | Finite groups, fusion/category-adjacent algebra, exact combinatorics. |
| Shell | `bash` | Small orchestration checks only. |

If a tool is optional and missing, the producer must either skip explicitly
with a clear note or fail before writing partial artifacts.

## (g) Exact And Floating Columns

When a generated CSV needs both exact and numerical values, use separate
columns:

| Suffix | Meaning |
|---|---|
| `_exact` | String representation of the exact value in the producing tool. |
| `_float` | Floating approximation. |
| `_residual` | Declared normed error, with denominator documented in schema. |

Floating diagnostics must state the tolerance, norm, denominator, precision,
and whether the result is a positive test or a negative control.

## (h) Unfixed Core Conventions

The following are intentionally not fixed yet:

- Frobenius direction and zeta-function variable normalization.
- Cohomology type and trace sign convention.
- Hilbert-space completion and Hamiltonian sign for arithmetic-QM models.
- Supersymmetric grading, adjoint, and boundary-domain conventions.
- Toric-code/star-plaquette orientation and boundary convention.
- Levin-Wen fusion-category gauge, pivotal/spherical structure, and F/R data.

Do not silently choose any of these. Add a new convention entry before using
one in a derivation or script.

## (i) Toric-Code Stabilizer Convention

For the first toric-code run, use the square `k x k` lattice with periodic
boundary conditions and one qubit on each oriented edge. There are `2k^2`
qubits: horizontal edges and vertical edges.

For a vertex `s`, the star operator `A_s` is the product of Pauli `X` over the
four incident edges. For a plaquette `p`, the plaquette operator `B_p` is the
product of Pauli `Z` over the four boundary edges. The code space is the common
`+1` eigenspace of all `A_s` and `B_p`.

Source: `references/toric_code/kitaev_quant_ph_9707021_source/anyons.tex`,
lines 189-222.

The positive Hamiltonian used in this repo is the shifted penalty

```text
H_TC = sum_s (I - A_s)/2 + sum_p (I - B_p)/2.
```

It has the same ground space as Kitaev's `H_0 = -sum_s A_s - sum_p B_p`
from equation (4), lines 328-337 of the same source.

## (j) Finite Supercharge Convention

For a finite-dimensional Hilbert space, a supercharge is a matrix `Q` with
`Q^2 = 0`. Its adjoint is written `Q^*`. The associated positive Hamiltonian
is `{Q,Q^*} = Q Q^* + Q^* Q`.

For the first toric-code run, `Q` is a local-check ghost/Koszul supercharge on
the enlarged Hilbert space `ghost Fock space tensor physical qubits`:

```text
Q = sum_i c_i^* P_i,
```

where `i` runs over all vertex and plaquette checks, `P_i=(I-S_i)/2` is the
projector onto the violated-check eigenspace, and `c_i^*` creates the auxiliary
fermion associated to check `i`. The abstract fermion modes satisfy
`c_i c_j^* + c_j^* c_i = delta_ij` and anticommute otherwise.

With this convention, `{Q,Q^*}=H_TC tensor I_ghost`. Restricted to the ghost
vacuum sector this is the physical shifted toric-code Hamiltonian. This proves
a local-check ghost formulation, not a purely physical-qubit supercharge.

The elementary meaning of cohomology for this `Q` is defined in report shard
`AQM-05-TORIC-SUPERCHARGE` before the term is used substantively. The explicit
chain-to-ghost proof is in `AQM-06-TORIC-CHAIN-GHOST-PROOF`.
The operator-level comparison of `Q_cell` and `Q_gh`, including why the former
is not a low-ghost restriction of the latter, is in
`AQM-07-TORIC-OPERATOR-RELATION`.

## (k) Toric Chain-Complex/CSS Convention

The homological toric-code layer uses the `F_2` chain complex

```text
C_2 --partial_2--> C_1 --partial_1--> C_0,
```

where `C_2` is spanned by plaquettes, `C_1` by edges/qubits, and `C_0` by
vertices. Over `F_2`, signs and orientations drop out.

The CSS check matrices are:

```text
H_X = partial_1
H_Z = transpose(partial_2)
```

so the CSS commutation condition is exactly

```text
H_X * transpose(H_Z) = partial_1 * partial_2 = 0.
```

There is a finite-cell cochain supercharge already at this level:

```text
Q_cell = delta^0 + delta^1,  delta^0 = transpose(partial_1),
delta^1 = transpose(partial_2).
```

Its square is zero because `partial_1 * partial_2 = 0`, and its middle
cohomology is `ker(delta^1) / im(delta^0)`.

This boundary-map layer is not itself the quantum stabilizer supercharge from
convention (j). It is the cellular skeleton. It determines the supports of the
local checks used in the ghost/Koszul supercharge:

```text
Q = sum_v c_v^* (I - A_v)/2 + sum_f b_f^* (I - B_f)/2,
```

where the `A_v` supports are rows of `partial_1` and the `B_f` supports are
columns of `partial_2`.

Source: `references/toric_code/bombin_martin_delgado_0605094_source/HomologicalErrorCorrection6.tex`,
lines 2050-2140, and `references/toric_code/error_correction_zoo_toric.yml`,
lines 20-39.

## (l) Symplectic Stabilizer/CSS Convention

For prime qudit dimension `p`, Pauli labels live in

```text
V = F_p^n x F_p^n.
```

The first component is the `X` exponent vector and the second component is the
`Z` exponent vector. The symplectic form is

```text
omega((x,z),(x',z')) = z*x' - x*z'
```

with dot products over `F_p`. Stabilizer generators labelled by a subspace
`L <= V` commute exactly when `L` is isotropic: `omega(L,L)=0`.

For a CSS code from a chain complex

```text
C_2 --partial_2--> C_1 --partial_1--> C_0,
```

qudits live on the basis of `C_1`, and

```text
L = (im delta^0 x 0) + (0 x im partial_2),
delta^0 = transpose(partial_1).
```

The identity `partial_1 * partial_2 = 0` is exactly the isotropy condition for
this `L`. The logical Pauli module is the symplectic reduction

```text
L^perp / L = (H^1) x (H_1).
```

For prime powers `q=p^m`, the same formulas hold over `F_q` with the Pauli
phase character composed with `Tr_{F_q/F_p}`. For composite non-field qudit
dimension, module torsion can enter, so rank/dimension statements are not
silently imported from the field case.

## (m) Symplectic Supercharge Convention

For a CSS stabilizer subspace `L <= F_p^n x F_p^n`, a generator-based
supercharge requires an ordered independent generator list
`G = (ell_1, ..., ell_r)` for `L`. For each generator, define the invariant
projector

```text
Pi_i = (1/p) * sum_{a in F_p} W(a * ell_i)
P_i = I - Pi_i
```

and the ghost/Koszul supercharge

```text
Q_G = sum_i epsilon_i * P_i.
```

This `Q_G` depends on the generator basis, but its degree-zero cohomology is
the `L`-stabilizer code and is basis-independent. The logical Pauli action on
that cohomology is `L^perp / L`. A basis-free but redundant variant attaches
one ghost to each projective line in `L`.

## (n) Steane Code Molecular Convention

For the detailed Steane calculation, use Gottesman's seven-qubit CSS table
with qubits ordered `1,...,7` and binary check rows

```text
g1 = 1111000
g2 = 1100110
g3 = 1010101
```

The rowspace is `D = <g1,g2,g3> <= F_2^7`, the classical Hamming code is
`C = D^perp`, and the odd coset representative is

```text
u = 0000111.
```

The CSS stabilizer subspace is

```text
L = (D x 0) + (0 x D) <= F_2^7 x F_2^7.
```

The logical representatives are `Xbar = (u,0)` and `Zbar = (0,u)`, with
binary symplectic pairing `omega(Xbar,Zbar)=1`. The six-generator Steane
supercharge uses one ghost for each ordered stabilizer label
`(g1,0),(g2,0),(g3,0),(0,g1),(0,g2),(0,g3)`.

For this generator-based Koszul supercharge, the full cohomology is
`Code x Lambda^* E`. Higher ghost-degree classes are interpreted as
presentation-dependent derived constraint/conormal data for the chosen
stabilizer equations, not as additional logical code states. The physical QECC
space is the no-ghost sector `H^0(Q)`.

## (o) Clifford/Koszul Morphism Convention

In the Steane Clifford calculation, a "symplectic morphism" means the
Pauli-label action induced by an actual Clifford unitary `U`. If `F_U` sends a
chosen stabilizer generator list `G=(ell_i)` to `G'=(F_U ell_i)`, then the
Clifford lift of the Koszul complex is

```text
Phi_U = U tensor Lambda(T),  T(epsilon_i) = epsilon'_i.
```

It is a chain isomorphism from `Q_G` to `Q_G'`. If `G'` is a permutation of
`G`, this is an automorphism of the same written supercharge after the same
ghost permutation. If `G'` is a different independent basis of the same
stabilizer subspace `L`, compare back to the original presentation by the
common deformation retract that contracts every nonzero syndrome sector and
keeps the zero-syndrome sector `Code x Lambda^* E`.

## (p) Clifford Group Ghost-Gaussian Convention

For arbitrary Clifford statements, Pauli labels are signed. The Hermitian
representative is

```text
W(x,z) = i^(x dot z) product_j X_j^x_j Z_j^z_j,
S = sign * W(x,z), sign in {+1,-1}.
```

The violated-check projector is `P_S=(I-S)/2`. Therefore a Clifford image with
negative sign is not silently identified with the unsigned binary label; it is
the opposite syndrome projector for that unsigned label.

For an ordered signed stabilizer presentation `G=(S_i)`, the Koszul
supercharge is `Q_G=sum_i c_i^dagger P_{S_i}`. Any Clifford `U` gives the
transported signed presentation `U(G)=(U S_i U^dagger)` and the strict chain
isomorphism

```text
U tensor Lambda(T),  T(epsilon_i)=epsilon_i^U.
```

Presentation changes inside the same signed stabilizer group are generated by
row swaps and row shears. A row shear `S_a -> S_a S_b` uses

```text
P(S_a S_b) = P(S_a) + S_a P(S_b)
```

and lifts to the number-preserving fermionic Gaussian
`exp(S_a c_a^dagger c_b)` on ghosts. This is not Bogoliubov mixing: ghost
degree is preserved. It is not a scalar `GL_r(F_2)` operation on the full
physical Hilbert space, because the coefficient `S_a` is an operator. On the
zero-syndrome code sector all `S_i=+1`, so the same shear reduces to the
ordinary exterior linear map `c_b^dagger -> c_b^dagger + c_a^dagger`.

## (q) Arithmetic Quantum Field Convention

For the finite-field arithmetic quantum field construction, `X` is a finite
physical point set and `V` is a finite symplectic vector space over
`F_q`. Without extra structure on `X`, the ambient field space is written
`Map(X,V)`, not `Hom(X,V)`. The notation `Hom(X,V)` is reserved for a
specified structure-preserving class of maps.

An arithmetic field label space is a chosen `F_q`-linear subspace
`E <= Map(X,V)`. The pointwise symplectic form uses weights `w_x`; the current
run fixes all weights to `1`:

```text
Omega(phi,psi) = sum_{x in X} w_x * omega_V(phi(x), psi(x)).
```

The construction is symplectic only after checking the radical

```text
rad(E) = {phi in E : Omega(phi,psi)=0 for all psi in E}.
```

If `rad(E)=0`, use `E` as the Weyl label space. If `rad(E) != 0`, the honest
Weyl label space is the reduced symplectic quotient `E_red = E/rad(E)`.

In the exact `F_3` examples, the internal space is `V=F_3^2` with
`omega((q,p),(q',p')) = p*q' - q*p'`. A scalar function space
`U <= Map(X,F_3)` gives `E = U q + U p`; the scalar pairing is
`B(f,g)=sum_x f(x)g(x)`, and the field form is
`Omega((q,p),(q',p'))=B(p,q')-B(q,p')`.

## (r) Projective Sheaf Field Convention

For projective arithmetic spaces, the default finite field-label space is not
the set of regular maps from a projective variety to an affine symplectic
vector space. The source-backed reason is that proper geometrically integral
varieties have only constant global regular functions in the Stacks convention
(`references/algebraic_geometry/stacks_project_varieties.tex`, lines
4875-4886).

The projective replacement used in this repo is:

```text
E(X,L,V) = H^0(X,L) tensor_Fq V
```

where `L` is an explicitly chosen sheaf, usually a line bundle or twist, and
`V` is the finite symplectic target. For `X = P^1_F3` the first run uses
`L = O(d)` for `d=0..4`. Stacks computes
`H^0(P^n_R,O(d)) = R[T_0,...,T_n]_d` for `d >= 0`
(`references/algebraic_geometry/stacks_project_coherent.tex`, lines
1557-1622), so `H^0(P^1_F3,O(d))` is represented by homogeneous polynomials
of degree `d` in `X,Y`.

For the finite rational-point algebra, evaluations are recorded in the fixed
point order

```text
[1:0], [0:1], [1:1], [2:1].
```

The monomial `X^(d-i)Y^i` is evaluated on these chosen representatives. This
is a chart-coordinate evaluation convention for the finite point calculation,
not a claim that sections of `O(d)` are global scalar functions. The scalar
pairing is

```text
B(s,t) = sum_{P in P^1(F3)} s(P) t(P)
```

with all weights equal to `1`; the `V=F_3^2` symplectic extension is as in
convention (q). The radical must be checked after this finite-point pairing.

Stalk computations use the standard frames `e_X^(d)` on `D_+(X)` and
`e_Y^(d)` on `D_+(Y)`. With `u=Y/X` and `v=X/Y`, the monomial
`X^(d-i)Y^i` has germ `u^i e_X^(d)` at `[1:0]` and germ
`v^(d-i) e_Y^(d)` at `[t:1]`. Evaluation is residue modulo `(u)` or
`(v-t)`, respectively.

Terminology: in the arithmetic-field language, a stalk is the local field germ
at a point. The sampled field value is the fiber/residue value, obtained from
the stalk by tensoring with the residue field. For rational points of
`P^1_F3`, the residue field is `F_3`, so the fiber of
`O(d) tensor F_3^2` is canonically represented as the target space `F_3^2`
after the chosen local frame is reduced modulo the maximal ideal.

## (s) Finite Canonical Boson/Fermion Field Comparison

For comparison with the finite arithmetic quantum field construction, a
standard finite bosonic field uses a finite site set `X` and the real
symplectic target

```text
V_B = R_q x R_p,
omega_B((q,p),(q',p')) = p*q' - p'*q.
```

The field phase space is `E_B = Map(X,V_B)` with summed form

```text
Omega_B(phi,psi) = sum_{x in X} omega_B(phi(x),psi(x)).
```

If `|X|=N`, this is the finite-dimensional real symplectic space `R^{2N}`.
The Weyl convention used for the comparison is

```text
W(y) W(z) = exp(-i Omega_B(y,z)/2) W(y+z),
```

matching the Derezinski CCR source after identifying its covector coordinate
`eta` with the momentum coordinate `p`. The resulting irreducible regular
representation is the Schrodinger/Stone-von-Neumann representation on
`L^2(R^N)` and is also equivalent to the finite-mode bosonic Fock
representation.

A standard finite fermionic field is not obtained by replacing `V_B` with a
Grassmann algebra inside the same ordinary symplectic-vector-space recipe.
Instead, fix a finite-dimensional complex one-particle Hilbert space
`Z = Map(X,K)`. The CAR label space is the real Hilbert space

```text
Y_F = Re(Z x conjugate(Z))
```

with scalar product `alpha((z,bar z),(w,bar w)) = Re <z,w>`. On the
antisymmetric Fock space `Gamma_a(Z)`, the field operator is

```text
phi(z,bar z) = a^*(z) + a(z),
```

and it satisfies

```text
{phi(y), phi(z)} = 2 alpha(y,z).
```

Grassmann variables are therefore recorded as a fermionic phase-space calculus
inside the Grassmann-extended CAR algebra, not as a drop-in target producing
ordinary Hilbert-space projective phases by the same Stone-von-Neumann
argument. For finite modes the Cahill-Glauber displacement convention is

```text
D(gamma) = exp(sum_i (a_i^* gamma_i - gamma_i^* a_i)),
D(alpha)D(beta)
  = D(alpha + beta)
    exp(1/2 sum_i (beta_i^* alpha_i - alpha_i^* beta_i)).
```

Here the Grassmann variables anticommute with the odd CAR generators, and
adjunction reverses the order of all fermionic quantities. The displacement
operators are unitary in the Grassmann-extended CAR algebra and displace
`a_i` to `a_i + gamma_i`. The multiplier is Grassmann-valued, not generally a
complex `U(1)` phase, so the ordinary scalar projective-unitary Weyl
construction does not directly apply. Shard
`AQM-20-GRASSMANN-WEYL-FERMION-DISPLACEMENTS` records the definitions and
positive representation theorem; `AQM-21-GRASSMANN-WEYL-FERMION-DERIVATIONS`
records the derivations and the ordinary-Hilbert-space caveat.

## (t) Prime-Field Arithmetic Field / Qudit Pauli Convention

When comparing the arithmetic field construction with qudit stabilizer
formalism, this repo distinguishes two point sets attached to a prime field
`F_p`:

```text
Spec(F_p) = {(0)}        one point, hence one qudit;
underlying set F_p       p points, hence p qudits.
```

For the underlying set comparison, use all maps, not linear `Hom`:

```text
X = F_p as a finite set
V = Frac(F_p)^2 = F_p_X x F_p_Z
E = Map(X,V) = F_p^X x F_p^X.
```

The symplectic form and Weyl operators are

```text
Omega((xi,zeta),(xi',zeta'))
  = sum_{u in X} (zeta(u) xi'(u) - xi(u) zeta'(u))
T_xi |s> = |s + xi>
R_zeta |s> = exp(2*pi*i*sum_u zeta(u)s(u)/p) |s>
W(xi,zeta) = T_xi R_zeta.
```

For odd `p`, the group generated by `W(E)` and the character phases is the
standard prime-dimensional qudit Pauli group on `p` qudits, one qudit for each
element of `F_p`. A stabilizer code is not automatic; it requires an
additional isotropic subspace `L <= E` and compatible phases/eigenvalues. For
`p=2`, the projective label space and commutation form are unchanged, but the
conventional Hermitian Pauli group uses fourth roots of unity, e.g. `Y = i X Z`.

## (u) Finite Affine Spectrum / Residue-Qudit Convention

The morally preferred finite arithmetic point space is `Spec(R)`, not the
underlying set of elements of `R`. For a field this gives:

```text
Spec(F_p) = one point with residue field F_p,
local Hilbert space = l2(F_p), one p-level qudit.
```

For a finite reduced ring with several residue fields, attach one local phase
space to each prime:

```text
E_R = direct_sum_{p in Spec(R)} kappa(p)^2
Omega_R = orthogonal direct sum of the standard forms
          z*x' - x*z' over each kappa(p).
```

This direct sum is a label/phase-space direct sum. Weyl quantization represents
it on the tensor product of the local Hilbert spaces:

```text
H_R = tensor_product_{p in Spec(R)} l2(kappa(p)).
```

For `R = Z/6Z`, `Spec(R)` has two points `(2)` and `(3)`, with residue fields
`F_2` and `F_3`. The label group is `F_2^2 direct_sum F_3^2`, but the Hilbert
space is `C^2 tensor C^3`, and the observable algebra is
`M_2(C) tensor M_3(C) ~= M_6(C)`, not `M_2(C) direct_sum M_3(C)`.

## (v) Finite Zariski Open Observable-Net Convention

For a finite affine spectrum `X = Spec(R)` with residue-qudit local factors,
the primary local-observable assignment is open-local:

```text
A(U) = tensor_product_{p in U} End(l2(kappa(p)))
```

for each Zariski open `U <= X`, with empty tensor product `C`. If
`U <= V`, the inclusion is

```text
A(U) -> A(V),  a |-> a tensor I_{V \ U}.
```

This is the convention to use when observable algebras should have natural
inclusions following inclusions of open sets.

The assignment

```text
U |-> A(X \ U)
```

is also meaningful, but it is a closed-complement or vanishing-locus support
assignment. Its inclusions are contravariant in opens: `U <= V` implies
`A(X \ V) <= A(X \ U)`. Therefore it must not be silently substituted for the
open-local net.

For the quasi-local algebra over a general affine spectrum, use the directed
system of quasi-compact Zariski opens:

```text
A_qloc(X) = colim_{U quasi-compact open in X} A(U).
```

This is still concrete: quasi-compact opens may be represented by finite
unions of standard opens at the current level. The closed-complement
construction may also be made directed, but only after reindexing by closed
supports `Z` ordered by inclusion:

```text
Z |-> A(Z).
```

That is a separate closed-support or defect algebra, not the primary
open-local quasi-local algebra.

## (w) Presheaf/Cosheaf Observable-Net Convention

For a topological space `X`, write `Open(X)` for the category of open sets
ordered by inclusion. A presheaf is contravariant,

```text
Open(X)^op -> C,
```

and a precosheaf, also called a copresheaf here, is covariant,

```text
Open(X) -> C.
```

The open-local observable assignment is a precosheaf/local net of unital
`*`-algebras:

```text
U |-> A(U),   U <= V gives A(U) -> A(V).
```

It is not assumed to be an ordinary cosheaf in unital `*`-algebras. For a
disjoint cover, the categorical coproduct is an amalgamated free product, while
the physical/local-net gluing is a commuting tensor-product gluing inside the
ambient algebra. The replacement axioms for the observable layer are:

```text
isotony:       U <= V implies A(U) <= A(V)
locality:      disjoint supports have commuting images
additivity:    A(U union V) = algebra generated by A(U) and A(V)
```

The Weyl label assignment

```text
E(U) = direct_sum_{p in U} E_p
```

is the cosheaf-like layer in abelian groups or vector spaces. Quantization
turns additive label colimits into tensor-local observable algebras; it is not
treated as preserving ordinary algebra coproducts.

## (x) State Presheaf Convention

For a unital local observable algebra `A(U)`, a state is a normalized positive
linear functional:

```text
omega(1) = 1
omega(a^* a) >= 0
```

In the finite-dimensional matrix cases, states are represented by density
matrices `rho >= 0`, `Tr(rho)=1`, via

```text
omega_rho(a) = Tr(rho * a).
```

The local state assignment is contravariant:

```text
S(U) = State(A(U))
U <= V gives S(V) -> S(U),  omega |-> omega restricted to A(U).
```

When `A(V) = A(U) tensor A(W)`, this restriction is represented by partial
trace over `W`. The assignment `S` is a presheaf of convex sets. It is not
assumed to be a sheaf: local marginals do not determine correlations, and
compatible overlapping marginals may fail to have a joint quantum state.

For the algebraic quasi-local algebra

```text
A_qloc(X) = colim_U A(U),
```

states are compatible local families:

```text
State(A_qloc(X)) ~= lim_U State(A(U)).
```

This inverse-limit statement is the working replacement for an ordinary sheaf
gluing axiom on quantum states. A later C*-completion may require adding a
continuity/completion convention.

## (y) Closed-Point Affine Finite-Residue Convention

For an affine scheme `X = Spec(R)` of finite type over `F_q`, the finite
Weyl/qudit observable layer is indexed by the closed points:

```text
|X|_cl = MaxSpec(R).
```

For a closed point `x`, the residue field `kappa(x)` is a finite extension of
`F_q`, so it supports the finite-field Weyl system

```text
E_x = kappa(x)^2,
H_x = ell^2(kappa(x)),
A_x = End_C(H_x).
```

For an open set `U`, the label group is the finite-support direct sum over
closed points in `U`:

```text
E(U) = direct_sum_{x in U cap |X|_cl} kappa(x)^2.
```

The local observable algebra is the algebraic quasi-local algebra over finite
closed supports:

```text
A(U) = colim_{S finite subset U cap |X|_cl} tensor_{x in S} A_x.
```

This extends the finite-spectrum convention when every point is closed and has
finite residue field. Non-closed points, such as the generic point of
`Spec(F_q[t])` or the generic and curve-generic points of `Spec(F_q[x,y])`,
are not finite qudit sites in this convention. They still control the Zariski
topology, closures, and open inclusions.

Regular functions define closed-point field profiles by reduction modulo each
closed point, but these profiles usually have infinite support. Their Weyl
operators are therefore formal infinite-volume fields, not elements of the
algebraic quasi-local algebra, until a separate completion or infinite-product
field-operator convention is fixed.

## (z) Rational-Function Weyl-Heisenberg Convention

For `K = F_q(t)` in characteristic `p`, we separate three related but
non-identical Weyl-Heisenberg layers.

1. The closed-point finite-residue layer of convention `(y)` remains the
   quasi-local arithmetic field on `Spec(F_q[t])`.

2. The algebraic rational-function layer treats `K` as a discrete additive
   group.  Fix an `F_p`-linear functional

```text
lambda_K : K -> F_p
```

and define `chi_K(a) = exp(2*pi*i*lambda_K(a)/p)`.  The default choice is the
coefficient of `t^(-1)` in the Laurent expansion at infinity, followed by
`Tr_{F_q/F_p}`.  This gives a concrete algebraic Heisenberg group

```text
H_K = mu_p x K x K,
(z,q,p)(z',q',p') = (z z' chi_K(p q'), q+q', p+p')
```

and a unitary representation on `ell^2(K)` by translations and modulations.
This representation may be proved irreducible from the nondegeneracy of
`(a,b) |-> chi_K(ab)`.  It is not called a full Stone-von Neumann uniqueness
theorem unless the phase labels are enlarged to the full Pontryagin dual of
the chosen LCA configuration group and the required continuity hypothesis is
included.

3. The locally compact layer replaces `K` by a local completion such as
`F_q((t^(-1)))`, or by an adele ring in later global work.  For an LCA
configuration group `F`, the canonical Weyl system is

```text
G = F x Fhat,
sigma_can((x,gamma),(x',gamma')) = gamma(x')
```

with the Schrödinger representation on `L^2(F)`.  In this layer, standard
Stone-von Neumann-Mackey uniqueness applies under the recorded LCA
hypotheses.  The diagonal field `K` is then a dense or lattice-like arithmetic
subgroup used for arithmetic labels, not itself a substitute for the full dual
phase space.

## (aa) Finite Polynomial-Quotient Residue-Qudit Convention

For a monic nonzero polynomial `p(t) in F_3[t]`, write

```text
R_p = F_3[t]/(p),        X_p = Spec(R_p).
```

Factor

```text
p = product_i pi_i^(e_i)
```

with distinct monic irreducibles `pi_i`.  The closed-point finite-residue
Weyl layer of convention `(y)` uses one site for each distinct factor:

```text
x_i = (pi_i)/(p),       kappa(x_i) = F_3[t]/(pi_i).
```

The Hilbert space and label group are

```text
H_p = tensor_i ell^2(kappa(x_i)),
E_p = direct_sum_i kappa(x_i)^2.
```

The exponents `e_i` are retained as scheme-theoretic nilpotent thickening data
in `R_p`.  Under the present residue-qudit convention they do not add extra
qudit tensor factors.  Equivalently, regular-function profiles factor through
the reduced quotient

```text
R_p,red = F_3[t]/(product_i pi_i) ~= product_i kappa(x_i).
```

Nilpotent classes therefore reduce to zero at every closed-point Weyl site.
The nilpotent-sensitive quantum-field layer is convention `(ab)`, not an
implicit modification of the residue-qudit construction.

## (ab) Nilpotent-Sensitive Polynomial-Quotient Weyl Layer

For `p(t) in F_3[t]` factored as in convention `(aa)`, the
nilpotent-sensitive layer keeps the local Artin factors

```text
A_i = F_3[t]/(pi_i^(e_i)),       m_i = (pi_i)/(pi_i^(e_i)),
K_i = A_i/m_i = F_3[t]/(pi_i).
```

It attaches one thickened quantum site to the same closed point `x_i`, not
`e_i` new points.  The local Hilbert space and Weyl label group are

```text
H_i^thick = ell^2(A_i),          E_i^thick = A_i x A_i.
```

Every element of `A_i` is expanded uniquely as

```text
a = a_0 + a_1*pi_i + ... + a_(e_i-1)*pi_i^(e_i-1),
```

with `a_j` represented in `K_i`.  The default thickening character is

```text
lambda_i(a) = Tr_{K_i/F_3}(a_(e_i-1)),
chi_i(a) = exp(2*pi*i*lambda_i(a)/3).
```

This character detects the socle coefficient.  It is the finite-chain-ring
analogue of the residue-field character used in convention `(y)`.

The local operators are

```text
T_i(q)|s> = |s + q>,
R_i(p)|s> = chi_i(p*s)|s>,
W_i(q,p) = T_i(q) R_i(p).
```

Globally,

```text
H_p^thick = tensor_i H_i^thick,
E_p^thick = direct_sum_i E_i^thick.
```

Equivalently, using Chinese remainders, this is the Weyl system on
`ell^2(R_p)` with label group `R_p x R_p` and character equal to the product
of the local `chi_i`.

The reduced residue-qudit layer is not replaced.  It is the zeroth-order
closed-point layer.  The thickened layer adds jet degrees of freedom at the
same point.  In the associated graded for the `m_i`-adic filtration, position
jets of order `r` pair with momentum jets of order `e_i - 1 - r`; in
particular the reduced position value pairs with the socle momentum layer.

## (ac) Stabilizer Descent Convention

For the vector-space version of the finite residue-qudit label net of
conventions `(v)`--`(y)`, a stabilizer label assignment over an open `U` is a
subspace

```text
L(U) <= E(U)
```

such that the Weyl commutator form vanishes on `L(U)`.  A full stabilizer
state is represented at the label level by a Lagrangian subspace, i.e.

```text
L(U) = L(U)^perp.
```

Phases/eigenvalues are separate data: after choosing a Weyl lift with
multiplier `c(e,f)`, a phased stabilizer over `L` is a map
`alpha : L -> U(1)` satisfying

```text
alpha(e + f) = alpha(e) alpha(f) c(e,f)^(-1).
```

Then `alpha(e)^(-1) W(e)` is multiplicative on `L`.

For a finite cover `U = union_i U_i`, the local part of a global stabilizer
`L <= E(U)` is

```text
Loc_U(L; {U_i}) = sum_i (L cap E(U_i)),
```

where `E(U_i)` is included in `E(U)` by extension by zero.  The stabilizer
descent defect is

```text
D_U(L; {U_i}) = L / Loc_U(L; {U_i}).
```

The defect vanishes exactly when the global stabilizer labels are generated
by labels supported on the chosen cover.  Thus:

```text
global Lagrangian stabilizer
  = full global stabilizer state at the label level;

global Lagrangian with zero descent defect
  = full global stabilizer generated by the chosen local pieces.
```

The second condition is the local-to-global condition.  It is not automatic
from being Lagrangian; entangled stabilizer states can have nonzero descent
defect even for a disjoint two-site cover.  Mixed-residue finite rings and
finite Frobenius modules need separate module-language versions before rank
or dimension statements are imported.  The vector-space proof and the
two-qutrit counterexample are recorded in AQM-38 and AQM-39.

## (ad) Finite Product-Field Spectrum Convention

For a finite field `k = F_q` and

```text
R = k^n = k x ... x k
```

the arithmetic point space is

```text
X = Spec(R),
```

not the underlying set of `R`.  Thus `X` has `n` points, one for each
projection `R -> k`, not `q^n` points.  The point `x_i` is the prime/maximal
ideal `ker(pr_i)`, and its residue field is `kappa(x_i) = k`.

The Zariski topology is discrete: the idempotent `e_i`, with `1` in the
`i`-th factor and `0` elsewhere, satisfies

```text
D(e_i) = {x_i}.
```

Therefore every subset of `{x_1, ..., x_n}` is open.  The residue-qudit
arithmetic field is

```text
E(X) = direct_sum_i k^2 = k^n_X x k^n_Z,
H(X) = tensor_i ell^2(k),
A(X) = tensor_i End(ell^2(k)) ~= M_(q^n)(C).
```

This is the ambient `n` qudit Weyl/Pauli system for `q`-level qudits.  A
stabilizer code is still extra data: an isotropic additive subgroup of the
label group, plus compatible phases.  If one restricts to `k`-linear label
subspaces, this is the usual `k`-linear `q`-ary stabilizer subclass; allowing
`F_p`-additive isotropic subgroups gives the full finite-field additive
stabilizer convention.

## (ae) Cech Descent Convention

Cech data is cover-relative unless a direct limit over refinements is
explicitly declared.  In the current concrete arithmetic-field layer, use
finite ordered Zariski covers

```text
U = union_i U_i
```

and write

```text
U_{i_0 ... i_p} = U_{i_0} cap ... cap U_{i_p}.
```

For an abelian presheaf `F`, the ordered Cech cochains are

```text
C^p(U_i; F) = product_{i_0 < ... < i_p} F(U_{i_0 ... i_p})
```

with differential

```text
(d c)_{i_0 ... i_{p+1}}
  = sum_j (-1)^j c_{i_0 ... hat{i_j} ... i_{p+1}}
      restricted to U_{i_0 ... i_{p+1}}.
```

The cover cohomology is `check H^p({U_i}, F) = ker d^p / im d^{p-1}`.
The global Cech cohomology `check H^p(U,F)` means the colimit of these groups
over refinements and should not be silently substituted for a fixed-cover
defect.

For a covariant vector-space or abelian-group precosheaf `G`, use the dual
Cech chain complex

```text
C_p(U_i; G) = direct_sum_{i_0 < ... < i_p} G(U_{i_0 ... i_p})
```

with the alternating sum of covariant extension maps.  Its homology is the
label-side Cech homology.

The arithmetic quantum-field counterparts are layer-specific:

```text
label cosheaf E:          Cech homology of E;
state presheaf S:         comparison S(U) -> compatible local marginals;
observable net A:         ordinary algebra-colimit to physical net map;
stabilizer sublabels L:   cokernel of local stabilizer generation.
```

Only the first and fourth are abelian-group/vector-space invariants at this
stage.  The state object is convex and nonlinear, and the observable object is
noncommutative; calling their defects "cohomology groups" requires an explicit
linearization or abelianization convention not yet fixed.

## (af) Gaussian/Clifford Dynamics Convention

For finite residue-qudit dynamics in odd characteristic, use the half-Weyl
normalization.  For a finite-dimensional nondegenerate symplectic vector space
`(E, Omega)` over a finite field `k` of odd characteristic and a nontrivial
additive character `chi : k -> U(1)`, the Weyl operators are normalized so
that

```text
W(e) W(f) = chi(1/2 * Omega(e,f)) W(e + f),
W(e)^* = W(-e).
```

This is the normalization in which symplectic maps preserve the full
multiplier, not only the commutator.  A symplectic morphism

```text
S : (E, Omega_E) -> (F, Omega_F)
```

means a `k`-linear map satisfying

```text
Omega_F(S e, S f) = Omega_E(e,f).
```

For nondegenerate `E`, such a morphism is automatically injective.  It induces
a unital `*`-monomorphism of Weyl observable algebras

```text
alpha_S(W_E(e)) = W_F(S e).
```

If `S` is bijective, `alpha_S` is a `*`-automorphism.  A Gaussian or
quasi-free discrete dynamics is a family of symplectic automorphisms
`S_t` with `S_{t+s}=S_t S_s`, acting by `alpha_t = alpha_{S_t}`.

A Clifford implementation is a unitary `U_S`, defined up to phase, satisfying

```text
U_S W(e) U_S^* = W(S e).
```

The resulting map `S |-> [U_S]` is projective.  An affine Clifford dynamics
allows an additional displacement `a in E`:

```text
Ad_{W(a) U_S}(W(e)) = chi(Omega(a, S e)) W(S e).
```

For an open-local net, a global symplectic map is a local net automorphism
only when it preserves the chosen support structure, e.g. `S(E(U)) = E(U)` for
each open in question, or more generally `S(E(U)) = E(phi(U))` for a declared
open-set permutation/homeomorphism `phi`.  Otherwise it is a global
observable-algebra dynamics, not an open-local dynamics.

Pure odd-qudit Gaussian states are identified with stabilizer states in the
finite Hudson sense: nonnegative Gross Wigner function is equivalent to being
a stabilizer state.  For `k = F_(p^r)`, this Gross theorem is imported by
viewing `ell^2(k^m)` as `ell^2(F_p^(rm))` after a chosen `F_p`-basis; the
`k`-linear symplectic dynamics is then a distinguished subclass of the
`F_p`-linear Clifford dynamics.  The algebra-map construction above is
intrinsic, but this finite Hudson/Gaussian-state identification depends on the
chosen odd-prime decomposition.  The statement is not imported for even
characteristic without a separate source and convention.

## (ag) Finite-Field Scale and Continuum-Limit Convention

Fix `k = F_q` and an algebraic closure `bar{k}`.  Write

```text
k_r = F_(q^r) subset bar{k}.
```

Then `k_r subset k_s` is part of the scale system only when `r | s`.  For an
affine `k`-scheme `X_0 = Spec(R)`, the rank-`r` scale is

```text
X_r = X_0 x_Spec(k) Spec(k_r) = Spec(R tensor_k k_r).
```

For `r | s`, the structural map is `pi_(s,r) : X_s -> X_r`, and open-local
nets are compared by pullback of opens, `U |-> pi_(s,r)^(-1)(U)`.

The geometry is canonical; the Weyl embedding is not automatically canonical
with the absolute trace characters of convention `(y)`.  If `x` is a closed
point of `X_r`, put `K = kappa(x)` and

```text
B_(s,r,x) = K tensor_(k_r) k_s ~= product_{y over x} kappa(y).
```

The naive diagonal label map from `K^2` to the direct sum over the fine points
above `x` multiplies the absolute-trace commutator by `n = s/r`.  Hence it is
Weyl-compatible exactly when `n == 1 mod p`.

The trace-normalized replacement is: choose

```text
c_(s,r,x) in B_(s,r,x),       Tr_{B_(s,r,x)/K}(c_(s,r,x)) = 1.
```

Then send

```text
(q,p) |-> ((q_y, c_y p_y))_{y over x},
```

where `q_y,p_y` are the images of `q,p` in `kappa(y)` and
`c_(s,r,x) = (c_y)_y`.  This preserves the character-valued Weyl commutator
and therefore induces a unital `*`-monomorphism

```text
A_r(U) -> A_s(pi_(s,r)^(-1)(U)).
```

If `p` does not divide `n=s/r`, the canonical choice is
`c_(s,r,x) = n^(-1) * 1`.  These choices are coherent under composition.  The
prime-to-`p` scales therefore form a canonical directed subsystem.  If
`p | n`, trace-one elements still exist for finite separable residue
extensions, but no canonical choice is fixed here; the full tower requires
extra trace-one or compatible-character data.  Under the present convention,
the word "continuum limit" means the resulting algebraic filtered colimit of
Weyl observable nets after such coherent embedding data have been fixed.  No
Hilbert-space completion or C*-completion is silently assumed.

## (ah) Trace-Gauge Convention for Full Finite-Field Towers

A full finite-field scale tower may be gauge-fixed by a coherent trace-density
system.  This means a family

```text
a_r in F_(q^r),     Tr_{F_(q^s)/F_(q^r)}(a_s) = a_r for every r | s,
```

with `a_1 != 0`.  The condition forces every `a_r` to be nonzero.  Such
systems always exist by the trace-surjectivity/factorial-tower construction
proved in AQM-44.

Given a coherent trace-density system, set

```text
c_(s,r) = a_s / a_r in F_(q^s),      r | s.
```

Then `Tr_{F_(q^s)/F_(q^r)}(c_(s,r)) = 1` and
`c_(t,r) = c_(t,s)c_(s,r)` for `r | s | t`.  For any closed point
`x in X_r`, use the base-changed element `1 tensor c_(s,r)` in
`kappa(x) tensor_(F_(q^r)) F_(q^s)` to define the trace-normalized Weyl
embedding.  This gives a coherent full-tower system of open-local Weyl-net
monomorphisms.

This choice is called a trace gauge.  It is presentation data for comparing
different scales, not new geometry of `X_0`.  The canonical prime-to-`p`
subtower gauge is recovered by `c_(s,r) = (s/r)^(-1)`.  For `p | s/r`, no
relative-Frobenius-fixed trace-one element can lie in the base field, because
`Tr(1) = s/r = 0` in characteristic `p`.  Thus Frobenius acts naturally on the
space of trace gauges; a strict Frobenius action on a fixed full-tower
presentation requires an additional Frobenius-compatible gauge convention,
which is not fixed here.

## (ai) `Spec(Z)` Closed-Prime Field And Translation Convention

For the first arithmetic base-space model over the integers, write

```text
X = Spec(Z),        eta = (0),        x_l = (l) for rational primes l.
```

The closed points are the `x_l`, with residue fields `kappa(x_l)=F_l`.
The generic point has residue field `kappa(eta)=Q`.

The primary finite-qudit layer is the closed-prime layer:

```text
E_cl(U) = direct_sum_{x_l in U} F_l^2       finite support only,
H_l = ell^2(F_l),
A_cl(U) = colim_{S finite subset U cap {x_l}} tensor_{x_l in S} End(H_l).
```

Thus `Spec(Z)` carries one `l`-level qudit at each rational prime `l`.
For `X` itself this is the algebraic infinite tensor product over all prime
dimensions, i.e. the filtered colimit over finite sets of primes. A Hilbert
space representation of this algebra is not canonical. If a reference vector
`Omega_l=|0>` is chosen at every prime, the reference-vector incomplete tensor
representation has orthonormal basis indexed by finite-support residue
configurations

```text
s = (s_l)_l,      s_l in F_l,      s_l = 0 for all but finitely many l.
```

The generic point is not a finite qudit site. If it is included, it is a
separate rational Weyl sector:

```text
E_eta = Q^2,      H_eta = ell^2(Q),
chi_Q(a) = exp(2*pi*i*a),
T_Q(q)|s> = |s+q>,      R_Q(r)|s> = chi_Q(rs)|s>.
```

Every nonempty open of `Spec(Z)` contains `eta`, so this rational sector is
present in every nonempty local algebra. It is therefore a global generic-fibre
layer, not a prime-local qudit.

There is no scheme-theoretic translation `z |-> z+1` on `Spec(Z)`: affine
self-maps of `Spec(Z)` come from unital ring endomorphisms of `Z`, and the only
such endomorphism is the identity. The expression `z |-> z+1` belongs
scheme-theoretically to `A^1_Z = Spec(Z[z])`, not to `Spec(Z)`.

There is, however, an internal residue-translation action of the additive
group `Z` on the closed-prime qudit algebra. For `n in Z`, at the prime `l`
use the local shift

```text
U_l(n) = T_l(n mod l).
```

On a finite support `S`, set

```text
alpha_n^S = Ad(tensor_{l in S} U_l(n)).
```

These finite-support automorphisms are compatible under tensoring identities,
so they define an automorphism `alpha_n` of the algebraic closed-prime
quasi-local algebra. The action is faithful as a `Z`-action, locally periodic
with period `product_{l in S} l` on a finite support `S`, and extends
continuously through the diagonal residue map to the compact product
`product_l F_l`; equivalently it extends to `hat{Z}` after reduction modulo
each prime. For `n != 0`, the automorphism is not implemented by the naive
infinite product of shifts in the `|0>` reference-vector tensor sector:
it sends the vacuum configuration to one with nonzero residues at all but
finitely many primes.

## (aj) Affine-Line Automorphism Weyl-Net Convention

For `k = F_q`, the affine line is the `k`-scheme

```text
A1_k = Spec(k[x]).
```

The base-preserving symmetry group used in this repo is

```text
Aut_k(A1_k) = Aff_1(k) = {g_(a,b) : x |-> a*x + b,
                          a in k^*, b in k}.
```

Equivalently, the coordinate pullback is the `k`-algebra automorphism

```text
theta_(a,b) : k[x] -> k[x],      theta_(a,b)(x) = a*x + b.
```

This is a base-fixed statement. The affine-line Weyl-net shards do not
classify absolute scheme automorphisms that are allowed to move the
coefficient field.

For a closed point `x_pi = (pi)` with `pi` monic irreducible of degree `d`,
the image under `g_(a,b)` is

```text
g_(a,b)(x_pi) = x_(pi^g),
pi^g(X) = a^d * pi((X - b)/a),
```

where `pi^g` is monic irreducible. The induced residue-field pullback is

```text
tau_(g,pi) : k[x]/(pi^g) -> k[x]/(pi),
tau_(g,pi)([X]) = a*[X] + b.
```

The Weyl label pushforward sends a finite-support label
`e = (q_pi,p_pi)_pi` on an open `U` to the label `S_g e` on `g(U)` defined by

```text
(S_g e)_(g pi) =
  (tau_(g,pi)^(-1)(q_pi), tau_(g,pi)^(-1)(p_pi)).
```

This preserves the finite-residue Weyl multiplier and commutator, hence
defines a covariant net automorphism

```text
alpha_g^U : A(U) -> A(gU),       alpha_g^U(W_U(e)) = W_(gU)(S_g e).
```

For every finite closed support it is implemented by a tensor-factor
permutation together with the residue-field relabelling induced by
`tau_(g,pi)^(-1)`. In odd characteristic this is a finite Clifford/Gaussian
implementation in the sense of convention `(af)`. In even characteristic the
algebra automorphism remains valid, but any half-Weyl or Gross-Hudson
Clifford language requires a separate phase convention.

If the closed-point set is infinite, as for `Spec(F_q[x])`, the full
closed-point algebra is the algebraic infinite tensor product

```text
A(X) = colim_{S finite subset |X|_cl} tensor_{x_pi in S} End(ell^2(K_pi)).
```

Finite rational-point calculations are finite-support approximants, not the
full Zariski-open local algebra. A reference-vector Hilbert representation is
obtained only after choosing `Omega_pi = |0>` at every closed point:

```text
Gamma_fin = direct_sum_{x_pi in |X|_cl} K_pi,
H^0 = ell^2(Gamma_fin).
```

Because every residue relabelling sends `0` to `0`, affine symmetries preserve
this zero-reference sector and are implemented by the basis permutation

```text
(V_g s)_(pi^g) = tau_(g,pi)^(-1)(s_pi),      U_g |s> = |V_g s>.
```

The generic point `eta=(0)` is fixed by every base-preserving affine symmetry
and lies in every nonempty open, but it is not a finite-residue qudit site. A
generic rational-function Weyl sector uses convention `(z)` and requires a
separate additive-character and dual-label convention; the finite-residue
pushforward on both `q` and `p` labels is not automatically symplectic there.

## (ak) Regular-Function Profile and Smearing Convention

For `X = Spec(F_q[x])`, a global regular function is an element of `F_q[x]`.
On a standard open `D(h)`, regular functions are elements of the localization
`F_q[x]_h`. A pair of regular functions on `U` defines a residue profile

```text
ev_U(F,G)_(x_pi) = (F mod pi, G mod pi) in kappa(x_pi)^2,
```

where denominators are inverted at closed points lying in `U`. Except for the
zero pair, this profile has cofinite closed support in every nonempty standard
open. Therefore regular-function profiles are generally formal infinite-volume
fields, not elements of the algebraic finite-support Weyl label group `E(U)`.

A nonzero polynomial `h` has a second role as a support selector:

```text
Z_cl(h) = {x_pi : pi divides h},       rad(h) = product_{pi divides h} pi.
```

The reduced finite smearing over this support uses

```text
E_h^red = direct_sum_{pi divides h} kappa(x_pi)^2,
W_h^red(F,G) = W_(Z_cl(h))((F mod pi, G mod pi)_(pi divides h)).
```

It depends only on `F,G mod rad(h)`. By the Chinese remainder theorem, every
finite closed-support label is represented by some polynomial pair modulo the
squarefree support polynomial, so distinct closed-point qudits have no finite
compatibility condition in the reduced Weyl net.

If `h = product_i pi_i^(e_i)`, the exponents `e_i` are invisible to the
reduced support net. They are visible only in the nilpotent-sensitive layer
where the residue fields `kappa(x_pi_i)` are replaced by local Artin rings
`F_q[x]/(pi_i^(e_i))`.

## (al) Regular-Function Affine Action Convention

For `g = g_(a,b) : x |-> a*x + b` in `Aut_(F_q)(A1)`, write

```text
theta_g(f)(x) = f(a*x + b),        sigma_g = theta_(g^(-1)).
```

Regular functions are pushed forward by the inverse map:

```text
g_# F = sigma_g(F) = F(g^(-1)(x)).
```

For a nonzero support or denominator polynomial `h`,

```text
g_# : F_q[x]_h -> F_q[x]_(g_# h),
g_#(u/h^m) = (g_#u)/(g_#h)^m,
g(D(h)) = D(g_#h).
```

Residue profiles transform by the same residue-field relabelling as Weyl
labels:

```text
ev_(gU)(g_#F,g_#G) = S_g^Pi ev_U(F,G),
(S_g^Pi e)_(pi^g) =
  (tau_(g,pi)^(-1)(q_pi), tau_(g,pi)^(-1)(p_pi)).
```

`S_g^Pi` acts on the full product of residue profiles and restricts to the
finite-support Weyl label map `S_g` of convention `(aj)`. Therefore affine
symmetries preserve the distinction between regular-function profiles and
quasi-local Weyl labels: a nonzero regular-function profile remains infinite
support on every nonempty standard open.

For reduced finite smearing,

```text
alpha_g(W_h^red(F,G)) = W_(g_#h)^red(g_#F,g_#G).
```

For thickenings, `sigma_g` induces

```text
F_q[x]/(pi^e) ~= F_q[x]/((pi^g)^e),
```

so affine symmetries preserve the multiplicity `e` as Artin-ring thickness.
At the thickened Weyl level, one must either transport the chosen generating
character through this ring isomorphism or provide the corresponding dual
momentum-label correction. The reduced residue-field covariance does not by
itself prove that independently chosen top-coefficient Artin characters are
fixed.

## (am) Minimal Fermion Geometry Catalogue Convention

In this catalogue, a standard Hilbert-space fermion mode means the complex CAR
mode

```text
H_1 = C|0> direct_sum C|1>,
c|0>=0, c|1>=|0>, c^*|0>=|1>, c^*|1>=0.
```

An algebraic source over a field `k` supplies such modes only after a separate
mode-count step. If `V` is a finite-dimensional `k`-vector space used as an
odd, parity-shifted, or spinor mode source, the current complex CAR
realization records `r = dim_k(V)` and chooses `C^r` as the one-particle
space. For `k=F_3` this is not scalar extension: there is no unital field map
`F_3 -> C`.

For `char(k) != 2`, a local algebraic superpoint is

```text
Spt_k = (Spec k, k[theta]),      |theta| = odd,      theta^2 = 0.
```

For `k=F_3`, its underlying ungraded ring is isomorphic to the even
dual-number ring `F_3[epsilon]/(epsilon^2)`, but the parity assignment is part
of the data. Even nilpotents alone are not fermions in this convention.

For an ordinary commutative `k`-algebra `A`, the cotangent parity-shift entry is

```text
Pi Omega^1_(A/k).
```

If this vector space is finite-dimensional over `k`, its dimension is the CAR
mode count. Thus `Omega^1_(k/k)=0`, while for `char(k) != 2`

```text
Omega^1_(k[epsilon]/(epsilon^2)/k) ~= k d epsilon.
```

The existing Artin-Weyl layer of convention `(ab)` remains an even
finite-ring Weyl layer. For `A=F_3[epsilon]/(epsilon^2)`, it gives
`ell^2(A)` of dimension `9`; the optional `Pi Omega^1` construction is an
additional one-mode CAR layer, not the same object.

A log-spin datum is

```text
(C, D, S, mu),       mu: S tensor S ~= Omega^1_C(log D),
```

where `C` is a curve, `D` is a divisor with logarithmic one-forms defined, and
`S` is a line bundle. Its algebraic mode source is `Gamma(C,S)`. For
`P^1_k` with `D={0,infty}`, the form `dlog x` trivializes
`Omega^1(log D)`, so `S=O` is a log-spin datum and the mode source is
`Gamma(P^1,O)=k`.

## (an) Finite Commutative Ring Database Convention

For the finite-ring database PRD and its later implementation, the default word
`ring` means:

```text
finite, commutative, associative, unital ring,
```

and isomorphisms are required to preserve `1`. Nonunital rings are excluded
until a separate convention and schema extension are declared. Any imported
source row must record whether the source uses this same ring scope.

```text
finite_ring_db.zero_ring_policy = include
finite_ring_db.zero_ring_characteristic_exact = 1
finite_ring_db.zero_ring_residue_field_sizes_json = []
finite_ring_db.zero_ring_quantization_policy = not_applicable_until_layer_semantics
finite_ring_db.unimplemented_invariant_status = unknown
finite_ring_db.sqlite_commit_policy = local_run_artifact_until_release_policy
finite_ring_db.sqlite_build_rerun_policy = fail_existing_sqlite_unless_force
finite_ring_db.schema_integrity_policy = relational_checks_in_schema_json_and_open_enums_in_audit
finite_ring_db.residue_quantization_helper_scope = mvp_source_backed_only
finite_ring_db.thickened_frobenius_quantization_helper_scope = mvp_source_backed_only
finite_ring_db.prime_field_weyl_matrix_materialization_helper_scope = mvp_exact_in_memory_metadata_only
finite_ring_db.gap_small_ring_import_helper_scope = installed_tool_reconciliation_metadata_only
finite_ring_db.quotient_constructor_helper_scope = mvp_exact_in_memory_local_core_status_only
```

Build CLI reruns follow the marker
`finite_ring_db.sqlite_build_rerun_policy = fail_existing_sqlite_unless_force`:
without `--force`, `finite_ring_db_build.jl` must fail before schema migration
or inserts if `runs/<slug>/data/finite_rings.sqlite` already exists; with
`--force`, it may remove only that SQLite file and must preserve the run README
and sibling run-bundle artifacts. No append mode is part of this MVP policy.

Schema integrity follows the marker
`finite_ring_db.schema_integrity_policy = relational_checks_in_schema_json_and_open_enums_in_audit`.
The schema owns stable relational and row-shape constraints:
`ring_presentation_link.certificate_id` is nullable, but any non-null value
must reference `isomorphism_certificate(certificate_id)`; every `invariant`
row must reference at least one `ring_id` or `presentation_id`; and the stable
SQLite boolean columns `ring.is_commutative` and `ring.has_one` are integer
columns checked to the values `0` or `1`. The later audit gate owns canonical
JSON validity and the open/evolving status-token vocabulary until producers
freeze those vocabularies. No JSON1 `json_valid` schema checks are part of this
MVP schema slice.

Zero-ring edge case: include the one-element zero ring in finite-ring database
scope and in the MVP dataset. Source-local justification: the GAP rings manual
states that zero and identity in a ring-with-one need not be distinct and that
a one-element zero ring can be a ring-with-one
(`references/finite_ring_database/gap_rings_chapter_56.html`, line 477); the
GAP `NumberSmallRings` example beginning at line 1075 records one stored ring
of order `1`; and the Stacks algebra conventions state that rings are
commutative with `1` and that the zero ring is a ring
(`references/algebraic_geometry/stacks_project_algebra.tex`, line 36). This
also fixes the database invariant edge policy for the one-element zero ring.
For database invariant fields, `characteristic_exact` is an operational local
database invariant: the additive order of the stored identity coordinate vector
in the structure-constant model, not an external theorem claim. Since `1=0`
in the one-element zero ring, this convention stores
`characteristic_exact = 1`. Since the Stacks algebra convention states that
the zero ring is the only ring without a prime ideal
(`references/algebraic_geometry/stacks_project_algebra.tex`, lines 36-37),
zero-ring maximal/residue data are empty: no maximal ideals and
`residue_field_sizes_json = []`. Zero-ring quantisation rows remain explicit
`not_applicable_until_layer_semantics` obstruction records until the later
quantisation layer defines layer semantics; this marker makes no Hilbert-space
claim.

Structure-constant presentations use an ordered additive decomposition

```text
Z/d_1 Z direct_sum ... direct_sum Z/d_r Z
```

with ordered generators `e_1,...,e_r`. The table entry
`products[i,j,k]` is the canonical coefficient of `e_k` in `e_i*e_j`,
reduced modulo `d_k`; element coordinates are canonical integers
`0 <= x_i < d_i`; and the identity is stored as a coordinate vector in this
same ordered basis. Source-local justification: Behboodi--Beyranvand--
Hashemi--Khabazian display quasi-basis products
`a_i a_j = sum_k w_ijk a_k` and the induced multiplication formula, then state
well-definedness and associativity conditions
(`references/finite_ring_database/dml_behboodi_finite_rings.pdf`, pages
643-644); GAP `RingByStructureConstants` records the cross-tool shape as
`moduli` plus a structure-constants table
(`references/finite_ring_database/gap_rings_chapter_56.html`, lines
1131-1132).

Manual MVP constructors from PRD section 7 use the following local database
coordinate layouts, matching the structure-constant convention above and the
local examples in AQM-23, AQM-34, AQM-36, and AQM-40. These are data-layout
choices for the database implementation, not new classification claims.
`finite_ring_zero_ring()` is the rank-zero structure-constant model with empty
moduli, empty identity coordinate vector, empty product table, and
order/`characteristic_exact` equal to `1` by the zero-ring policy above.
`finite_ring_zn(n)` uses moduli `[n]`, ordered basis `[1]`, identity `[1]`,
and product table entry `1*1=1`. `finite_ring_dual_numbers(p)` uses ordered
basis `[1,e]`, moduli `[p,p]`, identity `[1,0]`, products `1*1=1`,
`1*e=e`, `e*1=e`, and `e^2=0`. `finite_ring_product` preserves argument
order, concatenates factor coordinate blocks, concatenates factor identity
vectors, copies each factor product table into its coordinate block, and sets
cross-factor products to zero.

Additive invariant factors emitted by the finite-ring database invariant
engine are in invariant-factor form

```text
n_1 | ... | n_s
```

with trivial factors omitted. The zero additive group is encoded as `[]`.
Source-local justification for the decomposition input: Behboodi--Beyranvand--
Hashemi--Khabazian recall the finite abelian-group theorem as a direct sum of
primary cyclic groups (`references/finite_ring_database/dml_behboodi_finite_rings.pdf`,
page 641, also registered in
`references/finite_ring_database/SOURCES.md`). The displayed
`n_1 | ... | n_s` invariant-factor list is this database's local
normalization emitted from that primary cyclic data; this sentence does not
claim that the source uses the same output notation. Unimplemented invariant
statuses use the literal string sentinel `unknown`, not `false`, because an
uncomputed invariant is not a negative mathematical claim. The zero-ring
residue sizes remain `[]` by the existing zero-ring maximal/residue policy
above.

The generated database is a run artifact, not hand-edited top-level data:

```text
runs/<YYYY-MM-DD>-finite-ring-database/data/finite_rings.sqlite
```

The SQLite file is canonical only inside its run bundle and only together with
the run README, source manifest, tool-version record, and audit output.
Generated `finite_rings.sqlite` files are ordinary local run artifacts and
should not be committed in normal development until a release artifact policy
is recorded. Manifests, run READMEs, audit outputs, and review-sized export
summaries remain commit candidates.

A presentation hash or invariant tuple is never an isomorphism proof. The
deduplication convention is:

```text
invariants filter candidates;
certificates prove merges or certified non-isomorphism decisions.
```

The first certificate format records a map on ordered additive generators,
checks that it is bijective as an additive-group map, checks that it sends `1`
to `1`, and checks multiplication preservation. A CAS identifier such as a GAP
small-ring ID may be stored as oracle evidence only with tool name, version,
scope, and source locator.

For the local certificate field `additive_generator_image_matrix`, rows are
source additive generators and columns are target coordinates. Row `i` is the
canonical target coordinate vector for the image of the source additive basis
generator `e_i`; therefore the matrix shape is
`(length(source.moduli), length(target.moduli))`. The verifier must check the
well-defined additive map, additive bijection, identity preservation, and
multiplication preservation independently of any certificate producer flags.
Source-local justification: PRD-FR-006 requires independently checked
certificates for deduplication, and the GAP ring-homomorphism documentation
states that ring homomorphisms respect addition and multiplication
(`references/finite_ring_database/gap_rings_chapter_56.html`, line 997) and
that generator-image data fail when the generators do not generate or do not
define a homomorphism (same file, lines 1014-1019).

The first local deduplication search is a bounded MVP, not a classification
algorithm. It is exhaustive over additive-generator image matrices for finite
rings with `order <= max_order`. Candidate comparisons are filtered first by
the cheap invariant tuple `(order, characteristic, additive invariant
factors)`. A merge is recorded only when
`finite_ring_verify_isomorphism_certificate(...).ok` is true. Representative
choice is deterministic input order for this MVP slice. Failure to find a
certificate in this bounded exhaustive search is only a local checked
non-merge for that bounded comparison, not a global classification theorem.

Quantisation records are layer-labelled. The `residue` layer uses conventions
`(u)` and `(y)`: residue fields at maximal ideals give qudit dimensions and
the Weyl label group is the direct sum of the residue-field phase spaces. The
`thickened_frobenius` layer uses convention `(ab)` or the finite Frobenius-ring
Pauli convention recorded in `AQM-31`; it requires a certified generating
character. If a ring lacks the data required for a layer, the database stores a
`blocked` quantisation row with an explicit obstruction rather than silently
omitting the ring.

The first in-memory residue-quantisation helper is deliberately MVP-scoped:
available residue records are emitted only for source-backed cases already
fixed in this lab book: prime fields from convention `(u)`, `Z/6Z` from
`report/sections/23_spec_z6_residue_qudit_factorisation.tex`, and explicit
finite product fields from convention `(ad)` and
`report/sections/40_product_field_spectrum_qudit_stabilizers.tex`. The zero
ring emits `not_applicable_until_layer_semantics` with no Hilbert-space claim.
Other MVP rings such as `Z/4Z`, `Z/8Z`, `Z/9Z`, and dual-number examples emit
`blocked` until a certified maximal-ideal/residue-field decomposition is added;
this helper is not a general maximal-ideal algorithm.

The first in-memory thickened-Frobenius quantisation helper is likewise
MVP-scoped. In this slice, the only available row is the AQM-36
`F_3[e]/(e^2)` top-coefficient Artin-Weyl example. The zero ring emits
`not_applicable_until_layer_semantics` with no Hilbert-space claim. Other MVP
rings, including `Z/4Z`, `Z/8Z`, `Z/9Z`, `F_2[e]/(e^2)`, fields, and product
fields, emit `blocked` until a certified generating character or a wider
thickened-Frobenius policy is added; this helper is not a general
Frobenius-ring recognizer.

The first prime-field Weyl matrix materialisation helper is deliberately
MVP-scoped. It applies only to the one-qudit prime-field Weyl system of
AQM-22, with basis ordered `[0,1,...,p-1]` and operator order
`W(q,m)=T(q)R(m)`. It emits exact in-memory monomial payloads whose nonzero
entries are encoded as exponents of `zeta_p`, never dense floating complex
matrices. The caller-supplied `matrix_dump_threshold` is mandatory; if
`p > matrix_dump_threshold`, the helper returns a `blocked` record with
obstruction `matrix_dump_threshold_exceeded` and no matrix payload or artifact
path. Any `artifact_path` it reports is deterministic content-addressed
metadata only; this helper performs no filesystem or database writes and is
not a general finite-ring matrix materialiser.

The first GAP small-ring helper is installed-tool reconciliation metadata only.
It is order-1 metadata only: it may query a locally installed GAP for
`NumberSmallRings(1)` and `SmallRing(1,1)`. `SmallRing(1,1)` is counted by
the local zero-ring policy above even on GAP builds whose
`IsRingWithOne(SmallRing(1,1))` returns false. The registered GAP manual
documents a small-ring library through order `15`, but this helper must not
expose scoped counts beyond order `1`; those counts are deferred pending an
exact element-level unit-detection/import path rather than GAP
`IsRingWithOne(SmallRing(s,i))` on the audited small-ring library objects.
The helper invokes GAP as an argv command with `--bare -q` for this status
metadata query, because the status helper needs only core GAP ring operations
and this avoids package autoload/startup failures observed with the local Nix
GAP build. Its status rows carry `certifies_completeness=false`; the helper
writes no SQLite rows, emits no structure constants, imports no presentations,
creates no certificates, and creates no run artifacts. Missing GAP is
represented by the explicit `gap_not_available` skip reason. Source scope is
pinned to
`references/finite_ring_database/SOURCES.md` lines 103-118 and
`references/finite_ring_database/gap_rings_chapter_56.html` lines 472-477,
1041-1071, and 1115-1131.

The first quotient-constructor helper is exact in-memory local-core status only.
It emits only the three PRD MVP quotient examples `F_2[x]/(x^2+x)`,
`F_3[e]/(e^2)`, and `Z/6Z` through the manual structure-constant constructors
above, reports Sage/OSCAR/Nemo availability or `tool_not_available` skips, and
certifies no backend completeness; this helper is not a general quotient-ring
engine and performs no SQLite writes, quotient-basis extraction, Groebner-basis
extraction, generated certificate creation, or run-artifact creation.
