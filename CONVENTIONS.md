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

For the finite-spectrum quasi-local algebra, use the directed system of finite
supports:

```text
A_finqloc(X) = colim_{S finite subset X} A(S).
```

When `X` is finite this directed system has terminal object `X`, so
`A_finqloc(X) = A(X)`. This is the finite-region finite-spectrum analogue, not
a general infinite affine locality construction.

Do not define the general affine quasi-local algebra by the colimit over
quasi-compact opens. For affine `X = Spec(R)`, the global open `X` is itself
quasi-compact and terminal in that poset, so such a colimit collapses to the
global algebra whenever that algebra is defined. Quasi-compact opens may be
used as topology/control data, but they are not the nonterminal finite-region
indexing convention for infinite affine spectra.

The closed-complement construction may also be made directed, but only after
reindexing by finite closed supports `Z` ordered by inclusion:

```text
Z |-> A(Z).
```

That is a separate closed-support or defect algebra, not a replacement for the
open-local net. For affine schemes of finite type over `F_q`, use convention
`(y)`: finite closed supports inside `U cap |X|_cl`.

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
global phased Lagrangian stabilizer
  -> full global stabilizer state at the label level;

fixed global phased Lagrangian with zero descent defect
  = stabilizer labels generated by the chosen local pieces,
    with phases inherited from the fixed global phase character.
```

The second condition is the local-to-global condition.  It is not automatic
from being Lagrangian; entangled stabilizer states can have nonzero descent
defect even for a disjoint two-site cover.  The converse direction from an
arbitrary full stabilizer state to a phased Lagrangian label space requires a
separate stabilizer classification theorem before it is used as a report
claim.  If local phased stabilizers are chosen independently on an overlapping
cover, their eigencharacters must also satisfy overlap compatibility with the
chosen Weyl multiplier; AQM-38--AQM-39 prove the fixed-global-phase label
generation statement, not a general phase-descent theorem.  Mixed-residue
finite rings and finite Frobenius modules need separate module-language
versions before rank or dimension statements are imported.

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
`c_(s,r,x) = (c_y)_y`.  This preserves the non-half Weyl multiplier, and hence
the character-valued Weyl commutator, so it induces a unital `*`-monomorphism

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
`product_l F_l`. The corresponding `hat{Z}` action is only the action obtained
after coordinatewise reduction modulo each prime, so it factors through the
squarefree residue quotient `product_l F_l` and is not faithful on all of
`hat{Z}`. For `n != 0`, the automorphism is not implemented by the naive
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

## (ao) Derivative/Cotangent Dynamics Proposal Convention

For a finite commutative `k`-algebra `A`, the intrinsic first derivative
object is the module of Kahler differentials

```text
Omega^1_(A/k)
```

with universal `k`-derivation `d : A -> Omega^1_(A/k)`. At a point
`x in Spec(A)` the cotangent fibre is

```text
T^*_(Spec A/k,x) = Omega^1_(A/k) tensor_A kappa(x),
```

and the tangent space is its `kappa(x)`-dual, equivalently the local
derivations into `kappa(x)` under the Stacks tangent-space convention. This
cotangent object is geometric data, not by itself the Weyl-Heisenberg momentum
label group.

This project now separates three layers which earlier exploratory prose may
have kept too close together.

```text
residue-Weyl prequantisation:
  E_x^res = kappa(x)_q direct_sum kappa(x)_p,
  H_x^res = l2(kappa(x)).

geometric tangent-cotangent phase space:
  V_x = T_(Spec A/k,x),
  V_x^* = T^*_(Spec A/k,x),
  E_x^geom = V_x direct_sum V_x^*,
  omega((v,alpha),(w,beta)) = beta(v) - alpha(w).

finite de Rham CSS test:
  C^0=A -> C^1=Omega^1_(A/k) -> C^2=Omega^2_(A/k),
  R_X=im(d0), R_Z=im(transpose(d1)).
```

The residue-Weyl layer is the finite local Heisenberg system attached to the
residue field. The geometric tangent-cotangent layer is the infinitesimal
phase-space object attached to the scheme. They agree only after additional
choices in special cases; for example, at a smooth curve point
`dim_kappa(x) T_x = 1`, choosing a tangent basis identifies
`T_x direct_sum T_x^*` with `kappa(x)^2`. For higher-dimensional, singular, or
nonreduced points, the geometric phase space has dimension
`2 dim_kappa(x) T_x`, and can differ from the residue-Weyl space
`kappa(x)^2`.

The subspaces `T_x direct_sum 0` and `0 direct_sum T_x^*` are isotropic
subspaces of `E_x^geom`; if maximal, they are Lagrangian. They are not an
extra step in the named kinematical recipe. In this programme, an isotropic or
Lagrangian label set becomes physically operative only when a stabilizer
selection principle chooses the corresponding mutually commuting Weyl
operators. A dynamical principle must therefore be additional data, such as a
global isotropic relation, a Hamiltonian/action, a connection, or a checked
finite chain-complex rule.

The named kinematical recipe `tangent_cotangent_weyl_kinematics` is:

```text
Input: a finite-residue point x in Spec(A), K=kappa(x),
       finite-dimensional K-vector space V_x=T_(Spec A/k,x).

Symplectic label space:
  E_x^geom = V_x direct_sum V_x^*.

Heisenberg/projective representation:
  construct the finite Weyl-Heisenberg projective unitary
  representation rho_x^geom: E_x^geom -> PU(H_x^geom)
  using psi_K. The Hilbert space H_x^geom is the carrier of
  this representation.
```

For a finite set of finite-residue points `S`, use the direct sum of phase
labels and the tensor product of projective representations:

```text
E_S^geom = direct_sum_(x in S) E_x^geom,
rho_S^geom = tensor_product_(x in S) rho_x^geom.
```

For `K=F_(p^r)`, `psi_K(a)=exp(2*pi*i*Tr_(K/F_p)(a)/p)`. If
`dim_K V_x=m`, then the finite Weyl-Heisenberg projective representation with
central character `psi_K` has Hilbert carrier dimension `|K|^m`; after choosing
a `K`-basis of `V_x`, the carrier has the size of `m` qudits of local dimension
`|K|`. This dimension statement belongs to the representation theory of
`E_x^geom`; it is not a direct assignment of a Hilbert space to the tangent
space alone.

The compatible de Rham selection test for this kinematics is called
`evaluated_de_rham_momentum_constraints`. For a finite support `S` of
finite-residue points, evaluate exact one-forms fibrewise:

```text
ev_S^1 : Omega^1_(A/k) -> direct_sum_(x in S) T_x^*,
L_Z^dR(S) = ev_S^1(dA).
```

The labels `L_Z^dR(S)` are cotangent/momentum labels, hence define commuting
Weyl operators in the projective representation of `E_S^geom`. Choosing a
compatible phased-stabilizer character on this label subgroup, in the sense of
convention `(ac)`, gives a stabilizer family and hence a joint eigenspace in
the Hilbert carrier of `rho_S^geom`. An arbitrary assignment of eigenvalue
phases is not enough. This is compatible with
`tangent_cotangent_weyl_kinematics`. It is not by itself a full CSS rule:
`X`-type tangent labels require extra data, for example a chosen isotropic
subspace commuting with `L_Z^dR(S)`, a metric/Hodge identification, or a
separately justified dynamical principle.

The first derivative-stabilizer test is a proposal, not a settled dynamical
principle. For finite-dimensional `k`-vector spaces obtained from the
algebraic de Rham complex

```text
C^0 = A  --d0-->  C^1 = Omega^1_(A/k)  --d1-->  C^2 = Omega^2_(A/k),
```

one may choose finite `k`-bases and the corresponding dot pairing, put qudits
on `C^1`, and form the CSS support spaces

```text
R_X = im(d0),          R_Z = im(transpose(d1)).
```

The equation `d1*d0 = 0` gives CSS orthogonality by convention `(b)` and
AQM-08, so this produces an isotropic stabilizer after the basis/pairing and
phase choices are fixed. This construction is called the `de_rham_css_test`.
It is separate from the even Artin-Weyl layer of convention `(ab)` and from the
fermion parity-shift catalogue of convention `(am)`. A report shard may use it
only as a checked finite example or as an explicitly labelled proposal.

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
It may query a locally installed GAP for `NumberSmallRings(s)` and
`SmallRing(s,i)` for orders `1..15`, the range documented by the registered
GAP small-ring manual snapshot. Its scoped status count is computed by an
exact element-level two-sided identity detector: enumerate `Elements(R)`, test
each candidate `e` by GAP equality after both products `e*x` and `x*e` for
all enumerated elements `x`, reject multiple identities, and then combine the
result with `IsCommutative(R)`. This deliberately does not use
`IsRingWithOne(SmallRing(s,i))` as the scoped-count filter. `SmallRing(1,1)`
is counted by the same identity law under the local zero-ring policy, and the
helper must fail loudly if that order-1 check is inconsistent.

The helper invokes GAP as an argv command with `--bare -q` for this status
metadata query, because the status helper needs only core GAP ring operations
and this avoids package autoload/startup failures observed with the local Nix
GAP build. Its status rows carry `certifies_completeness=false`; the helper
writes no SQLite rows, emits no structure constants, imports no presentations,
creates no certificates, creates no run artifacts, and makes no database
completeness claim. Missing GAP is represented by the explicit
`gap_not_available` skip reason. Source scope is pinned to
`references/finite_ring_database/SOURCES.md` lines 103-160,
`references/finite_ring_database/gap_rings_chapter_56.html` lines 472-477,
1041-1071, and 1115-1131, and the registered GAP collection/domain/magma
manual snapshots covering `Elements(R)`, element equality, element
multiplication, ring/magma closure, and the two-sided identity law.

The first quotient-constructor helper is exact in-memory local-core status only.
It emits only the three PRD MVP quotient examples `F_2[x]/(x^2+x)`,
`F_3[e]/(e^2)`, and `Z/6Z` through the manual structure-constant constructors
above, reports Sage/OSCAR/Nemo availability or `tool_not_available` skips, and
certifies no backend completeness; this helper is not a general quotient-ring
engine and performs no SQLite writes, quotient-basis extraction, Groebner-basis
extraction, generated certificate creation, or run-artifact creation.

## (ap) Quantum-System Association Vocabulary

For the meta-plan in `docs/quantum_system_associations/PLAN.md` and report
shard `AQM-64-QUANTUM-SYSTEM-ASSOCIATION-META-PLAN`, the preferred general
term is `quantum-system association`, not a canonical functorial
`quantisation`. A quantum-system association is a recorded workflow that starts
from specified structure on an object `X`, adds explicitly named choices, and
returns kinematical quantum data such as a Hilbert carrier, observable algebra,
Weyl-Heisenberg projective representation, Fock sector, or stabilizer subspace.

The local shorthand names `Quant1`, `Quant2`, `field association`,
`single-particle sector`, `review shard`, `gap shard`, `association
equivalence`, `agreement`, `inequivalence`, and `degenerate case` are
programme labels, not established mathematical classifications. A report shard
may use them only after stating the specific local workflow and the evidence
status of any comparison.

Dynamics is not part of a quantum-system association unless a later convention
records a separate dynamics-selection principle. Therefore Hamiltonians,
actions, time evolutions, and Witten-index-style statements remain out of scope
for this meta-plan except as explicitly labelled future questions.

## (aq) Structureless Finite-Set First Carrier

For QSA Step 03 and report shard
`AQM-67-QSA-FINITE-SET-FIRST-ASSOCIATION`, a bare finite set `X` supplies only
labels. The first structureless finite-set association writes

```text
C<X> = direct_sum_{x in X} C e_x,
```

also denoted `C^X` in the Step 03 shorthand because `X` is finite. The
workflow output is the complex vector-space carrier together with its
`X`-indexed formal basis labels `e_x`. It does not include an inner product,
norm, adjoint, observable algebra, Hamiltonian, tensor-factor interpretation,
direct-sum particle interpretation, or Weyl-Heisenberg data.

Any inner product or Gram matrix on this carrier is extra data. In the formal
basis, a Gram array `G = (G_xy)_{x,y in X}` is a separately supplied choice;
neither the identity Gram matrix nor any other array is determined by the bare
set in this workflow.

The empty set gives the zero formal carrier with no basis labels. A one-point
set gives one formal generator. An `n`-point set gives `n` formal generators
after choosing labels for display. Comparisons with tensor-site workflows,
direct-sum particle workflows, or special one-dimensional internal-space
choices are planned for later QSA shards and are not proved by this convention.

## (ar) Structureless Finite-Set Tensor-Site Data

For QSA Step 04 and report shard
`AQM-68-QSA-FINITE-SET-TENSOR-SITES`, a bare finite set `X` still supplies
only labels. A tensor-site association starts only after adding one
finite-dimensional complex Hilbert space `H_x` for each `x in X`, or directly
adding one finite-dimensional unital `*`-algebra `A_x` for each site.

In the Hilbert-space version, set

```text
A_x = End_C(H_x),
H(S) = tensor_product_{x in S} H_x,
A(S) = tensor_product_{x in S} A_x
```

for each finite subset `S <= X`, with empty tensor product `C`. An ordering of
`S` may be chosen only to write the finite tensor product; it is display data,
not structure supplied by the bare set. If `S <= T`, the local observable
inclusion is

```text
A(S) -> A(T),        a |-> a tensor 1_(T \ S).
```

This convention supplies independent coexisting site factors. It is not the
formal carrier `C<X>` of convention `(aq)`: the latter is a direct sum of
formal labels with no inner product or observable algebra, while the
tensor-site workflow has explicitly chosen Hilbert or algebra factors and uses
tensor products.

## (as) Structureless Finite-Set Direct-Sum Particle Data

For QSA Step 05 and report shard
`AQM-69-QSA-FINITE-SET-DIRECT-SUM-PARTICLE`, a bare finite set `X` supplies
only labels for alternatives. A direct-sum particle association starts only
after adding one finite-dimensional complex carrier `K_x` for each `x in X`;
in the Hilbert version each `K_x` is a finite-dimensional complex Hilbert
space `H_x`.

The carrier is

```text
K_oplus(X) = direct_sum_{x in X} K_x,
H_oplus(X) = direct_sum_{x in X} H_x
```

with empty direct sum `0`. In the Hilbert version the inner product is the
finite direct-sum inner product

```text
<psi,phi> = sum_{x in X} <psi_x,phi_x>_{H_x}.
```

This is an alternatives/one-particle-at-one-of-many-sites carrier. It is not
the tensor-site coexistence carrier of convention `(ar)`, whose Hilbert space
is a tensor product and whose empty tensor product is `C`.

If every internal carrier is one-dimensional, then a chosen nonzero vector
`u_x in K_x` for each site gives a vector-space identification
`C<X> -> direct_sum_x K_x` by `e_x |-> u_x` in the `x` summand. Without those
chosen vectors, the bare finite set does not supply the identification. If the
`K_x` are Hilbert lines, unit choices `u_x` make this identification compatible
with the identity Gram convention, but the Hilbert inner products and the unit
or orthonormal choices are still extra data and are not inherited from the
bare set or from convention `(aq)`.

## (at) Finite AND/OR Carrier Grammar

For QSA Step 06 and report shard
`AQM-70-QSA-AND-OR-MANY-PARTICLE-GRAMMAR`, a finite grammar expression is
built from finite-dimensional complex carriers already supplied by conventions
`(ar)` and `(as)`, the tensor unit `C`, the zero carrier `0`, and the two
operations:

```text
AND(E,F)  = E tensor_C F       independent coexistence,
OR(E,F)   = E direct_sum F     alternatives.
```

Only finite parse trees are in scope. The grammar therefore produces a
finite-dimensional complex carrier by ordinary finite tensor products and
ordinary finite direct sums. No Hilbert-space completion, C*-completion,
infinite direct sum over particle number, or infinite tensor product is part
of this convention.

When the atoms are declared to be one-particle carriers and `C` is declared to
be the zero-particle vacuum carrier, the same finite expression carries a
particle-count grading. For an atom `K`, put `K` in degree `1`; for `C`, put
`C` in degree `0`; for `0`, put no sectors. The operations are:

```text
OR:   (E OR F)_n  = E_n direct_sum F_n,
AND:  (E AND F)_n = direct_sum_{i+j=n} E_i tensor_C F_j.
```

This grading is grammar bookkeeping. It is not a bosonic, fermionic, para,
Fock, or fusion-category construction. Symmetric or antisymmetric quotients,
permutation-sector rules, CAR/CCR fields, para-statistics data, Fock
completions, fusion rules, associators, braidings, and pivotal or spherical
data are separate enhancements and must be introduced by later conventions
before being used.

## (au) QSA Table Status Tokens

For QSA Steps 21--22 and later report comparison tables, status tokens are
lowercase report-planning labels, not generated CSV sentinel values. They do
not change `data/SCHEMA.md`, `#`-prefixed CSV sentinel comment rows, or any
schema-local finite-ring status vocabulary.

Use `available` when the row has a named local workflow/output anchor;
`agreement` when two workflows are locally compared by a recorded map or
invariant; `inequivalence` when a local obstruction records that the selected
workflows do not agree; `degenerate` when a concrete row collapses, forgets
structure, or reduces to an earlier case; `zero` when the mathematical output
is the zero carrier/object; `empty` when the input set, support, or indexing
family is empty; `blocked` when required evidence, conventions, or tooling are
missing; `unknown` when the row has not yet been determined; and
`not_applicable` when the workflow is outside the row's stated semantics.

Do not introduce compound status tokens such as `blocked/database`,
`available locally`, or `proposal/blocked`.  Put the sanctioned token first
and record qualifiers such as "database helper", "local anchor only",
"generic-sector proposal", or "completion proposal" in the prose, witness, or
gap column.  Boundary categories from AQM-84 are classifiers for what kind of
choice is missing; they are not additional table status tokens unless this
convention is explicitly amended.

The tokens `agreement` and `inequivalence` require the evidence contract of
convention `(ap)`: a specific object, specified workflows and choices, and a
local source, derivation, test, run artifact, map, invariant, or obstruction.
The token `blocked` is an evidence-state label, not a mathematical result.

## (av) Intrinsic Versus Relative Cotangent Data

For QSA Step 13 and report shard
`AQM-77-QSA-INTRINSIC-RELATIVE-COTANGENT`, cotangent comparisons for
`X=Spec(A)` must keep two objects separate.

At a selected point `x`, with local ring `A_x`, maximal ideal `m_x`, and
residue field `K=kappa(x)`, the intrinsic/local cotangent object is

```text
C_x^loc = m_x / m_x^2.
```

It records the first local neighbourhood of the point in the local ring. It is
not relative to a base ring.

For a named base ring map `B -> A`, the relative Kahler cotangent object is

```text
C_x^rel(B) = Omega^1_(A/B) tensor_A K.
```

It records first-order directions of the morphism `Spec(A) -> Spec(B)`.
Changing `B` can change this object. When the usual local comparison applies,
base directions from the maximal ideal of the image point are quotiented out,
so relative cotangent data can be smaller than `m_x/m_x^2`.

The associated tangent-cotangent phase-label spaces are formed separately:

```text
V_x^loc = Hom_K(C_x^loc, K),
E_x^loc = V_x^loc direct_sum C_x^loc,

V_x^rel(B) = Hom_K(C_x^rel(B), K),
E_x^rel(B) = V_x^rel(B) direct_sum C_x^rel(B).
```

If `K` is finite and the chosen cotangent dimension is `m`, the finite
Weyl-Heisenberg carrier dimension is `|K|^m`, as in convention `(ao)`. A shard
must state which cotangent object it uses before quoting a phase-label
dimension, Weyl carrier size, or agreement/inequivalence comparison. No
finite-ring-wide cotangent table, database-backed cotangent row, or helper
coverage claim follows from this convention.

## (aw) Derivative Constraints on Residue Weyl-Heisenberg Elements

For the residue-site field layer, derivative data are allowed to select or
reject Weyl-Heisenberg elements only through their residue phase labels.

Input data are:

```text
B -> A                    finite commutative algebra with named base,
S <= Spec(A)              finite selected finite-residue support,
K_x = kappa(x)            locally anchored residue field for each x in S,
E_S = direct_sum_x K_x^2  residue-site phase-label group,
WH(E_S) -> E_S            Weyl-Heisenberg central extension label map pi.
```

The arithmetic quantum field at this layer is the projective unitary
representation of `WH(E_S)` fixed by the local finite-field Weyl conventions
and by tensoring the local projective representations over the direct sum
`E_S`. This convention tracks the represented Weyl elements by their labels in
`E_S`; central phases are not selection data unless separately declared.

An admissible map family is not an arbitrary set-map family. It is a named
finite additive subgroup, or named finite `B`-submodule when available,
`F <= Gamma(Spec(A), O) = A`. Coordinate-pair maps are elements of `F^2`.
The residue label map is

```text
lambda_(S,F) : F^2 -> E_S,
lambda_(S,F)(q,p) = ((q mod x, p mod x))_(x in S).
```

Let `d : A -> Omega^1_(A/B)` be the universal `B`-derivation. A derivative
predicate is a specified subset `P <= Omega^1_(A/B) x Omega^1_(A/B)`; in the
linear cases used in the report it is an additive subgroup, for example
`dq=0`, `dp=0`, or `dp=lambda*dq` after the scalar/action has been named.
The derivative-selected residue labels are

```text
C_P(S,F) =
  lambda_(S,F)({(q,p) in F^2 : (dq,dp) in P}) <= E_S.
```

The selected Weyl-Heisenberg elements are `pi^(-1)(C_P(S,F))`. The rejected
Weyl-Heisenberg elements are `pi^(-1)(E_S \ C_P(S,F))`. Equivalently, at the
projective level, the selected Weyl operators are exactly the labels
`W(e)` with `e in C_P(S,F)`.

A derivative predicate has an internal bite at `(S,F)` when

```text
C_P(S,F) proper_subset lambda_(S,F)(F^2),
```

so the derivative rejects labels that the same map family otherwise
represents. It has an ambient bite when `C_P(S,F)` is a proper subset of
`E_S`. If `P` is an additive subgroup, then `C_P(S,F)` is an additive subgroup
of `E_S`; otherwise it is only a subset. Any claim that a derivative predicate
is intrinsic to residue labels, independent of representatives in `F`, must
state the required fibre-saturation condition separately. Without such a
condition, the convention uses the displayed image definition and makes no
representative-independent stronger claim.

## (ax) Scheme-Incidence Code-Source Convention

For code-source conjectures after `AQM-88`, a finite scheme is not allowed to
silently mean a chain complex.  A bare finite residue-site scheme supplies
finite Weyl-Heisenberg sites.  A CSS chain complex requires extra incidence
data.

The finite incidence input is:

```text
k = F_2 unless another finite field is named,
S_i finite sets for i = 0,1,2,
X_i = Spec(k^(S_i)) the corresponding finite reduced schemes,
I_10 <= S_1 x S_0 and I_21 <= S_2 x S_1 incidence relations.
```

The incidence relations define F_2-linear boundary maps by parity:

```text
partial_1(e) = sum_{v : (e,v) in I_10} v,
partial_2(f) = sum_{e : (f,e) in I_21} e.
```

The datum is a CSS source only after the chain condition
`partial_1 partial_2 = 0` is checked.  With qubit Weyl labels on `S_1`, put

```text
E = F_2^(S_1)_q direct_sum F_2^(S_1)_p,
R_X = im(delta^0) = im(partial_1^T),
R_Z = im(partial_2),
L = (R_X direct_sum 0) + (0 direct_sum R_Z) <= E.
```

The selected Weyl-Heisenberg elements are the central preimage of `L` under the
label map `WH(E) -> E`.  This is the same CSS-isotropy convention as AQM-08,
rewritten for finite schemes whose point sets carry explicitly named
incidence relations.

A constant finite group scheme in this convention is only the following
explicit finite affine case.  For a finite abstract group `G`,

```text
G_k = Spec(k^G)
```

with multiplication, unit, and inverse maps induced contravariantly by the
corresponding maps of finite sets.  The underlying scheme `Spec(k^G)` is just
the product-field spectrum from AQM-40; the group law and any chosen generators
are additional structure.  Therefore a toric-code construction from a constant
group scheme must name the group law and the chosen commuting generators before
using them to define edge and face incidences.

## (ay) Split Algebraic Torus Quant2 Test Convention

For the split two-dimensional algebraic torus over `k = F_q`, use

```text
T = G_m^2 = Spec(k[x, x^(-1), y, y^(-1)])
          = D(xy) <= Spec(k[x,y]).
```

The raw arithmetic-field `Quant2` layer is the closed-point finite-residue
layer of convention `(y)`: for an open `U <= T`,

```text
E_T(U) = direct_sum_{z in U cap |T|_cl} kappa(z)^2
```

with finite support, Weyl-Heisenberg group `WH(E_T(U))`, and projective
unitary representation fixed by the finite-field Weyl convention.  Regular
Laurent-function profiles are not automatically quasi-local Weyl elements;
they become Weyl operators only after restriction to a named finite support or
after a later completion convention is fixed.

The rational support is

```text
T(k) = (k^*)^2.
```

It is a finite support inside the closed-point layer, not the full closed-point
scheme when `T` has infinitely many closed points.  A chosen pair of units
`alpha, beta in k^*` defines the finite subgroup

```text
G_(alpha,beta) = <alpha> x <beta> <= T(k).
```

If `alpha` and `beta` have orders `N_x` and `N_y`, this support has
`N_x N_y` vertices.  The statement that all of `k^*` is generated by one
primitive unit is not used unless such a unit is explicitly named or sourced.

The toric-code-like edge layer is separate from the raw residue-site Quant2
layer.  After choosing `alpha,beta`, put

```text
S_0 = G_(alpha,beta),
S_1 = G_(alpha,beta) x {x,y},
S_2 = G_(alpha,beta),
```

with qubit labels on `S_1`.  The boundary maps are the Cayley-square maps
displayed in `AQM-90`.  The resulting selected Weyl-Heisenberg elements are
the central preimage of the CSS subgroup

```text
L_square = (im(partial_1^T) direct_sum 0)
           + (0 direct_sum im(partial_2))
         <= F_2^(S_1) direct_sum F_2^(S_1).
```

Thus the algebraic torus supplies a natural source of two multiplicative
directions and commuting squares, but the finite step units and the decision
to put qubit Weyl labels on the edge set are named extra structure.

## (az) Haah-Laurent Versus Algebraic-Torus Convention

When comparing Haah's translation-invariant Laurent-polynomial code formalism
with the algebraic-torus `Quant2` test case, keep two Laurent rings distinct.

The algebraic-torus coordinate ring is

```text
A_T = k[x, x^(-1), y, y^(-1)]
```

where `x` and `y` are regular invertible coordinate functions on
`T = Spec(A_T)`.  The Haah translation ring is

```text
R_tr = F_p[X, X^(-1), Y, Y^(-1)] = F_p[Z^2]
```

where `X` and `Y` are lattice translation operators.  The same abstract
Laurent algebra appears in both places, but its role is different: `A_T` is a
coordinate algebra, while `R_tr` is a group algebra acting on finite-support
Pauli/Weyl labels.  Do not identify them without naming the bridge.

The bridge used in `AQM-91` is finite and periodic.  After choosing
`alpha,beta in k^*` of orders `N_x,N_y`, let

```text
G = <alpha> x <beta> <= T(k).
```

For labels over `F_p`, set

```text
R_(G,p) = F_p[X, X^(-1), Y, Y^(-1)] / (X^(N_x)-1, Y^(N_y)-1)
        = F_p[C_(N_x) x C_(N_y)].
```

As a vector space, `R_(G,p)` is the finite periodic configuration module with
basis the sites of `G`; multiplication by `X` and `Y` shifts by the chosen
torus steps.  This is not automatically the coordinate ring of the finite set
`G`; it is the finite quotient of the translation group algebra.

For the qubit toric-square comparison, first specialize the label field to
`p=2`.  In the following display, `R_G = R_(G,2)` means this `F_2`
specialization.  Order the edge label module as

```text
P_G = R_G^4 = (q_x, q_y, p_x, p_y)
    ~= F_2^(G x {x,y})_q direct_sum F_2^(G x {x,y})_p.
```

With the AQM-90 edge orientation, the Haah toric generator matrix is used in
the orientation-equivalent form

```text
sigma_square =
  [ 1 + X^(-1)   0
    1 + Y^(-1)   0
    0            1 + Y
    0            1 + X ].
```

Its selected Weyl-Heisenberg labels are `im(sigma_square) <= P_G`; the
selected Weyl-Heisenberg elements are the central preimage of that submodule.
The excitation map is

```text
epsilon_square = sigma_square^dagger lambda_2 : P_G -> R_G^2.
```

The generator-isotropy/commutation condition is instead

```text
epsilon_square sigma_square = sigma_square^dagger lambda_2 sigma_square = 0.
```

This Haah excitation map is not the Kähler derivation
`d: A_T -> Omega^1_(A_T/k)` from `AQM-90`.  The derivation is an infinitesimal
coordinate-ring operation; the Haah map is a finite-difference/symplectic
constraint on translation labels.  Any proposed relationship between them must
be stated as an additional construction and checked on finite supports.

## (ba) Scheme Haah-Datum Layer Convention

When extracting general lessons from Haah's module formalism for an arbitrary
affine scheme `X = Spec(A)`, use the following layer names.

A `pre-Haah datum` over `A` is only an algebraic control package

```text
(G, P, lambda, sigma)
```

where `G` and `P` are specified `A`-modules, `lambda` is a specified
alternating or symplectic form when such a form has been chosen, and
`sigma : G -> P` is a specified generator map.  This layer is allowed for any
commutative ring `A`, but it does not by itself define Pauli operators,
Hilbert spaces, locality, a Hamiltonian, or a code.  If `lambda` gives a
usable adjoint convention, the formal excitation map is

```text
epsilon = sigma^dagger lambda : P -> G^vee.
```

The expression `ker(epsilon) / im(sigma)` is only a logical-defect module at
this layer; it is not automatically a physical logical-operator group.

A `scheme Haah datum` is a pre-Haah datum interpreted on `Spec(A)` through
quasi-coherent or finite locally free sheaves.  This layer may discuss support,
restriction, base change, localization, residue fibres, and nilpotent
thickenings.  It still does not identify the points of `Spec(A)` with lattice
translation sites unless an additional bridge has been named.

A `finite Weyl-Haah datum` adds enough finite self-duality data to turn the
module labels into Weyl-Heisenberg labels: for example finite field residue
labels, or a finite Frobenius-ring/generating-character convention already
recorded in the Weyl-Heisenberg source manifest and the finite-ring QSA
shards.  Arbitrary finite commutative rings are not promoted to this layer
without a named nondegenerate pairing or a cited Frobenius-ring mechanism.

A `translation Haah datum` adds a group algebra, an involution or antipode,
and the identity-coefficient trace convention, as in the Haah sources used in
`AQM-91`.  This is the layer where Laurent-polynomial stabilizer matrices,
finite-difference locality, and the toric-code matrix comparison live.  The
translation basis is group data, not the same thing as the Zariski point set
of `Spec(A)` unless a separate finite-support bridge identifies them.
