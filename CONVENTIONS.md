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
