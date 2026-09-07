# The partial-flag category and its coupling to Weyl quantum mechanics

Status: supporting SKETCH. This explicit construction replaces the
previously proposed but unnamed deformation of a flag algebroid. It was
developed from the Sol bridge lane and rederived below; it is not part of
the promoted Hecke/operational headline. D1141 and D1142 are authoritative.

Sources: Iwahori 1964 and Curtis 1988 for flag/Hecke representations;
Gurevich--Hadani 0705.4556 for the surrounding finite symplectic
quantization; all bodies and locators are in refs/LEDGER.md. Elementary
algebraic steps are displayed rather than attributed to those papers.

## 1. F1-OP-FLAGCAT — positive corners and categorical assembly

**ASSUME** q>0 and D1101, D1102, D1141.
**PROVE** Gamma_q is a graded monoidal C*-category, with the stated
finite-field realization and nonzero normalized corner systems.

`<1>1.` For W_alpha put x_alpha=sum_w T_w. Pair w with s w, where s
is a simple reflection in W_alpha and the latter has greater length.
The Hecke multiplication formula gives
`T_s(T_w+T_(sw))=q(T_w+T_(sw))`. Summing the pairs gives
`T_s x_alpha=q x_alpha`, and the right version follows by star.

`<1>2.` A reduced parabolic word therefore acts on x_alpha by q to
its length. Hence `x_alpha^2=P_alpha(q)x_alpha`.
Inversion preserves W_alpha, so x_alpha is self-adjoint.
Thus e_alpha is a self-adjoint idempotent. The denominator is positive
for q>0 and tau_n(e_alpha)=1/P_alpha(q)>0, so it is nonzero.

`<1>3.` If alpha refines beta, then W_alpha is a subgroup of W_beta.
Every T_w in the smaller parabolic acts on x_beta by q^ell(w), giving
`e_alpha e_beta=e_beta=e_beta e_alpha`. This is the refinement identity.

`<1>4.` For equal total n, the spaces e_beta H_n e_alpha compose by
multiplication: `(e_gamma y e_beta)(e_beta x e_alpha)` belongs to the
required corner. The identity is e_alpha and star reverses its type.
For distinct totals the zero Hom spaces are compatible with composition.

`<1>5.` Represent H_n faithfully on L2(H_n,tau_n), and represent object
alpha by the range of its left-multiplication projection e_alpha.
The corner morphism x acts by left multiplication between those ranges.
It is faithful because x e_alpha=x. The inherited operator norms,
adjoints and finite-dimensional linking algebras make Gamma_q a
C*-category in every degree. This is a realization for proving positivity,
not a stipulated tensor-preserving Hilbert-space fibre.

`<1>6.` Length is additive on block permutations, so
`P_(alpha concat beta)=P_alpha P_beta` and
`iota(e_alpha tensor e_beta)=e_(alpha concat beta)`.
Consequently iota takes the tensor of two typed corner morphisms to the
corner with concatenated source and target. Multiplication, star and
the interchange law are preserved by the Hecke algebra embedding.

`<1>7.` Associativity and the empty-composition unit follow from the
three-block identities F1-HCK-TOWER. This is ordered monoidal coherence;
unitary symmetric coherence at q!=1 is not inferred.

`<1>8.` Finite formal sums are represented by matrices of corner
morphisms, and self-adjoint idempotents split as their Hilbert ranges.
Nonzero completed objects retain finite C*-endomorphism algebras and
faithful positive traces. The zero additive object exists algebraically
but is excluded from the family carrying normalized states.

## 2. An actual specialization of presentations

`<1>9.` The Hecke multiplication coefficients in the T_w basis are
integer polynomials in the parameter. The parabolic maps send basis
symbols to basis symbols and the expectations are coefficient deletion.
Adjoining all P_alpha(t) inverses and t inverse gives exactly D1141's
named coefficient ring; q>0 makes every denominator nonzero.

`<1>10.` Every corner, multiplication, adjoint, identity and concatenation
formula is therefore defined over that ring and specializes at q=1.
No field of characteristic one and no matrix of noninteger size is used.
The positivity theorem concerns the evaluated real q>0 fibres, not a
positivity order on the unevaluated polynomial coefficient ring.

`<1>11.` At q=1, T_i^2=1 and the Coxeter relations give H_n(1)=C[S_n].
The e_alpha become subgroup averages. Tensor powers of x=(1) are the
complete-flag types (1,...,1), for which e=1, so
`End_Gamma1(x^tensor n)=C[S_n]`.

`<1>12.` The category on those tensor powers has endomorphisms the
linearized bijections and zero Hom spaces between different cardinalities.
It is the C-linear finite-bijection skeleton. Other compositions supply
its permutation-module retracts, with their specified averaging maps.
This identifies a concrete F1 category rather than a counting analogy.

## 3. Exact finite-field realization and normalized traces

`<1>13.` For Q a prime power, every partial flag of type alpha has
P_alpha(Q) complete refinements: the refinements are independent complete
flags in its successive quotient spaces, whose counts multiply.
Equivalently, this is the number of flags in the standard parabolic
fibre P_alpha/B, by the Bruhat count in Iwahori's Lemma 3.1.

`<1>14.` The normalized fibre sum J_alpha is an isometry: distinct
partial flags have disjoint sets of refinements, and the squared norm
of each column is P_alpha(Q)/P_alpha(Q)=1.
It is equivariant under GL(L) because forgetting commutes with the action.

`<1>15.` The operator J_alpha J_alpha^* is uniform averaging over the
refinement fibres. The adjacency sum x_alpha has entry one exactly
when two complete flags have the same alpha-partial flag. Dividing by
P_alpha(Q) therefore identifies that projection with e_alpha(Q).
The flag representation F1-HCK-FLAG is being used here.

`<1>16.` An equivariant map F:K_alpha->K_beta extends to the complete
flag space as J_beta F J_alpha^*. It belongs to the corner
e_beta H_n(Q)e_alpha. Conversely x in that corner restricts to
J_beta^* x J_alpha. The two constructions are inverse, preserve star,
and preserve composition because the intermediate corner projections act
as identities. This proves the whole algebroid realization.

`<1>17.` For x in the alpha endomorphism corner, the ordinary traces
on its range and on the complete flag space coincide. Since
`|Fl(L)|=P_alpha(Q)|Fl_alpha(L)|`, normalized physical traces satisfy
`tr_alpha(J_alpha^*xJ_alpha)=P_alpha(Q)tau_n(x)`.
In particular the corner identity has trace one. The ambient faithful
trace alone would assign it 1/P_alpha(Q), which is not its normalized state.

`<1>18.` Under refinement alpha<=beta, the same typed element e_beta
is an isometry beta->alpha, because v^*v=e_beta is the source identity.
Its range projection in the fine corner is e_beta<=e_alpha. Its
Heisenberg compression is UCP. Consecutive refinements compose by the
projection identity `<1>3`; no abstract square root was introduced.

`<1>19.` More generally, a family v_j:alpha->beta gives a UCP map
`a->sum_j v_j^* a v_j` iff `sum_j v_j^*v_j=e_alpha`.
For densities using tau_alpha and tau_beta, the dual map is
`rho -> (P_alpha/P_beta) sum_j v_j rho v_j^*`.
Cyclicity of tau_n checks normalization, including this necessary ratio.
Equivalently one can use positive functionals and precompose with the UCP
map, which avoids any trace-convention ambiguity.

`<1>20.` There is no nonzero amplitude map from degree zero to positive
degree in Gamma_q. Physical states and cross-degree operations belong
to its operational realization, not to a claim that Gamma_q already
has cups, caps, or every state as a morphism from its tensor unit.
**QED** (F1-OP-FLAGCAT, supporting SKETCH)

## 4. F1-OP-COUPLE — actual Weyl constraint chains

**ASSUME** D1142. **PROVE** flags inject equivariantly into Weyl projector
chains, with a controlled quantum coupling to the context register.

`<1>21.` The additive character group of L separates points and has
cardinality |L| by F1-DUAL. Restriction to U is surjective, hence the
annihilator U^ann has cardinality |L|/|U| and separates the nonzero cosets
of L/U. The named psi identifies the k-linear and phase duals.

`<1>22.` The average of Z(chi) over U^ann has coefficient one on e_x
if x is in U and zero otherwise, by character orthogonality. Thus
`P_U^Z=sum_(x in U)|e_x><e_x|`, an orthogonal projection of rank |U|.

`<1>23.` The group average of X(u) over U is a self-adjoint idempotent:
each translation in the product average occurs |U| times. Its range
consists of U-translation-invariant functions, equivalently functions
constant on U-cosets, and has rank |L|/|U|.

`<1>24.` If U<=U', the Z ranges nest covariantly and the X ranges
contravariantly. Hence
`P_U^Z P_U'^Z=P_U^Z`, `P_U^X P_U'^X=P_U'^X`.
Every complete flag gives two commuting chains. The support of each Z
projector recovers U itself, proving injectivity of the flag encoding.

`<1>25.` R(g)e_x=e_(gx) is unitary. Direct action on a basis gives
`R(g)X(u)R(g)^*=X(gu)` and
`R(g)Z(chi)R(g)^*=Z(chi o g^(-1))`.
This is the polarization-preserving symplectic Levi action, and gives
`R(g)P_U^{X,Z}R(g)^*=P_(gU)^{X,Z}`.

`<1>26.` Consequently the flag encoding is GL(L)-equivariant. On the
context register GL(L) permutes the flag basis, and F1-HCK-FLAG identifies
the invariant transition algebra with H_n(Q).

`<1>27.` The controlled operators C_i in D1142 are orthogonal projections:
their flag blocks are P_(U_i(F))^Z. They commute and nest, and the
simultaneous GL(L) action on both registers fixes them by `<1>25`.
Thus their projective measurements are genuine CP instruments on the
joint register, not a merely set-theoretic relation between two models.

`<1>28.` The dimensions are different: `dim C[L]=Q^n`, whereas
`dim K_ctx(L)=[n]_Q!`. No equality or canonical isometric embedding of
those two spaces was asserted. The joint coupling uses their ordinary
tensor product; the context commutant is only one quantum sector.

`<1>29.` Characters, the full Weyl algebra, changes of polarization,
and the full symplectic group are not recovered from the type-A context
algebra alone. At q=1 the corner category specializes, but a specialization
of every Weyl operator and controlled coupling has not been constructed.
**QED** (F1-OP-COUPLE, supporting SKETCH)

## 5. Further controlled comparisons

The analogous full symplectic flag algebra is of type C. Its q=1 Weyl
group is the signed permutation group, whose rank-two group is D8 and
already has an M2 block. However the block subgroup B_m x B_n is not
a standard parabolic of B_(m+n). The type-A assembly proof above cannot
be reused for that candidate without new maps and coherence evidence.

The rank-two Temperley--Lieb quotient has idempotents
`f_i=(q-T_i)/(q+1)` and adjacent coefficient q/(q+1)^2=delta^(-2), with
`delta=sqrt(q)+1/sqrt(q)`. The canonical flag trace is faithful, so it
cannot descend through this nonzero quotient. A Jones/Markov state is
extra input. At q=1 the resulting endomorphism tower is the SU(2)
spin-1/2 tensor-power centralizer tower. Identifying a full rigid tensor
category additionally requires cups/caps and their conventions; it is
not a consequence of the graded corner category alone.

The Fibonacci Jones quotient uses a different root-of-unity parameter
and its appropriate positive star/trace structure. It is not forced by
q=1 along the positive real flag family. Primary comparison sources are
Goodman--Wenzl 1993, Bernstein--Frenkel--Khovanov math/0002087,
Kauffman--Lomonaco 0804.4304 and Iohara--Lehrer--Zhang 1707.01196,
with exact locators in refs/LEDGER.md.

## 6. F1-OP-BELL — two disjoint collective qubits

**ASSUME** D1143 and the q=1 net. **PROVE** it contains an extension of
the ordinary Bell state on two disjoint size-three standard sectors.

`<1>30.` The standard block of C[S3] has s=diag(1,-1) and
`t=[[-1/2,sqrt(3)/2],[sqrt(3)/2,1/2]]`. Its central support is z.
Thus Z_* is Pauli Z on that block, X_num is sqrt(3) times Pauli X,
and Y_anti is i sqrt(3) times Pauli Y. They vanish on the other blocks.

`<1>31.` The expression inside D1143 is consequently the ordinary
Bell projector `(I tensor I+X tensor X-Y tensor Y+Z tensor Z)/4`
in the standard M2 tensor M2 block and zero in the other local blocks.
The block inclusion is a star-monomorphism by F1-HCK-TOWER, so its
image P_Bell is a positive projection in C[S6].

`<1>32.` The standard-block coefficient trace in C[S3] is one third
times ordinary matrix trace. The product trace of the rank-one Bell
projection is therefore 1/9, and tau_6(h_Bell)=1.

`<1>33.` Its two subgroup marginals are `(3/2)z`, representing I/2
in each standard M2 block. Its XX and ZZ correlations are one and its
XZ and ZX correlations zero. Choosing the usual observables
`Z,X` on one side and `(Z+X)/sqrt(2),(Z-X)/sqrt(2)` on the other gives
CHSH value 2 sqrt(2). All have norm at most one in their full local algebras.

`<1>34.` This is a genuine two-region quantum correlation. The extra
observables outside the local product subalgebra do not obstruct it:
the trace-preserving conditional expectation gives exactly the same
extension of the local Bell functional to the full composite algebra.
H14 checks the rational group-algebra projector, full density factor,
marginal and correlations independently. **QED** (supporting SKETCH)

## 7. F1-OP-APART — a direct completely positive arithmetic comparison

**ASSUME** D1144 and Q a prime power. **PROVE** Omega_Q is basis-independent
after the stated permutation labelling, UCP and coefficient-trace preserving,
and maps every T_w(Q) to the corresponding regular group operator at one.

`<1>35.` Coordinate flags are distinct, so J_ap is an isometry.
For each coordinate flag, exactly one other coordinate flag has relative
position w. Thus compression of the relative-position adjacency kernel
A_w is the regular permutation operator labelled w (with inverse in the
right regular action). These span the regular C[S_n] algebra.

`<1>36.` Compression by an isometry is UCP on the full operator algebra
and therefore on the context subalgebra, with its image in C[S_n] by
`<1>35`. Both normalized traces vanish on nonidentity basis elements
and take value one on the identity. Hence the comparison preserves the
coefficient traces. It is a linear bijection, but its inverse is not
asserted positive.

`<1>37.` Any two ordered bases are related by g in GL(L). Their apartment
isometries are related by the permutation unitary of g. Since every
x in Cxt(L) commutes with GL(L), both compressions of x agree after the
same permutation indexing. The comparison is therefore independent of
the basis used to construct it.

`<1>38.` On a contiguous block basis T_(u x v), compression gives the
block permutation u x v. Therefore Omega commutes with the ordered
assembly embeddings. It also commutes with coefficient-projection block
expectations, since both routes discard exactly the nonparabolic basis
elements. This is naturality for those structure maps only.

`<1>39.` For Q>1 and n>=2, this comparison is not multiplicative:
`Omega(T_s^2)=(Q-1)s+Q1`, whereas `Omega(T_s)^2=1`.
In particular `Omega(e_alpha(Q))=(|W_alpha|/P_alpha(Q))e_alpha(1)`.
The q=1 comparison is an operational CP map at a fixed Q; it is distinct
from evaluating a parameter-dependent expression at q=1.

`<1>40.` It is not automatically natural for all corner/refinement
compressions. For the coarse one-block flag object, compression of an
internal parabolic generator before the comparison gives scalar Q,
whereas apartment comparison followed by the q=1 coarse compression
gives scalar 1. This discrepancy names the next problem: compatible
comparison of refinement processes must retain more than these isolated
CP shadows. H9 checks the apartment compression independently over F2^3
and F3^3. **QED** (supporting SKETCH)
