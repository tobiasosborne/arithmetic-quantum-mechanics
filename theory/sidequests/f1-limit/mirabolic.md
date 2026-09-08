# The affine-vector commutant is the Fourier-dual controlled-Weyl sector

Status: PROVED within the stated hypotheses. Admission and repaired scope
are recorded in `../../verdicts/f1-limit-adjudication.md`.

Primary source: Rosso, arXiv:1310.3878, Section 3, especially equation (6),
Remarks 3.3--3.4, Section 3.1, Theorem 3.6 and Remark 3.7; local source and
exact locators are recorded in `../../../refs/LEDGER.md`.  All Hilbert-space, Fourier and
trace identifications below are derived explicitly.

## 1. MIR-AFF — invariant kernels and the affine group

**ASSUME** a finite field `k=F_Q`, an `n`-dimensional `k`-vector space `L`,
`G=GL(L)`, `X=Fl(L)`, and D1241.

**PROVE** Rosso's arithmetic mirabolic convolution algebra is canonically the
finite C*-algebra

`R_X(L)=End_(G semidirect L)(C[X times L])`,

with physical adjoint and normalized operator trace as stated in D1241.

`<1>1.` Give `A=G semidirect L` multiplication

`(g,a)(h,b)=(gh,a+gb)`

and action `(g,a)(F,x)=(gF,a+gx)` on `Y=X times L`.

`<1>2.` Embed the Borel `B<=G` as `(B,0)<=A`.  The map

`A/B -> Y`, `(g,a)B |-> (gB,a)`,

is well defined, bijective and A-equivariant.

`<2>1.` Right multiplication by `(b,0)` changes `g` to `gb` and leaves `a`
fixed, so the map is well defined.

`<2>2.` Every `(F,a)` has a representative `(g,a)B`, and two representatives
have the same right B-coset.  This proves bijectivity.

`<2>3.` Left multiplication gives `(h,c)(g,a)B=(hg,c+ha)B`, exactly the stated
action on `(gB,a)`.

`<1>3.` Write a matrix kernel in the orthonormal basis of `C[Y]` as

`K((F,x),(F',x'))=<e_(F,x),T e_(F',x')>`.

The operator `T` commutes with A exactly when `K` is constant on diagonal
A-orbits in `Y times Y`.

`<2>1.` The matrix coefficients of `U_a T U_a^*` are the simultaneous
translate of both kernel arguments.

`<2>2.` Thus `U_aT=TU_a` for every `a` is equivalent to diagonal invariance.
This is a direct matrix calculation and uses no double-commutant theorem.

`<1>4.` Translation invariance makes such a kernel uniquely of the form

`K_f((F,x),(F',x'))=f(F,F',x'-x)`

for a diagonally G-invariant function `f:X times X times L -> C`.

`<2>1.` Translate the pair by `-x` to obtain `(F,0),(F',x'-x)`.

`<2>2.` A linear element `g` sends this normalized pair to
`(gF,0),(gF',g(x'-x))`; hence precisely diagonal G-invariance remains.

`<2>3.` Conversely the displayed formula is invariant under translations and
under G, so every such `f` gives an affine-equivariant kernel.

`<1>5.` Matrix multiplication transports through `<1>4` to

`(f*g)(F,F',v)=sum_(H in X,u in L) f(F,H,u)g(H,F',v-u)`.

`<2>1.` In the intermediate point `(H,y)`, put `u=y-x` and
`v=x'-x`; then `x'-y=v-u`.

`<2>2.` The map `y |-> u` is a bijection of `L`, so the matrix-kernel sum is
exactly the displayed convolution.

`<1>6.` This is Rosso's equation (6), not merely an isomorphic abstract
presentation.  Rosso Section 3.1 separately identifies the same algebra with
the double-coset corner `e_B C[A]e_B`.

`<1>7.` Hilbert adjoint becomes

`f^dagger(F,F',v)=conjugate(f(F',F,-v))`.

On G-orbit indicators this is Rosso's anti-involution with conjugate-linear
extension.

`<2>1.` Kernel transpose-conjugation gives the displayed formula directly.

`<2>2.` The scalar `-1 in G` fixes every subspace in both flags and sends
`v` to `-v`.  G-invariance therefore gives
`f(F',F,-v)=f(F',F,v)`.

`<2>3.` Rosso Remark 3.4 swaps the flags and his orbit-basis formula is
`T_(w,beta)^star=T_(w^-1,w(beta))`; this agrees with `<2>1`--`<2>2` on the
real orbit basis.

`<1>8.` Restricting normalized matrix trace from `End(C[Y])` defines

`tau_Q(T)=Tr(T)/(|X||L|)`.

It is a faithful normalized positive trace on `R_X(L)`.

`<2>1.` Normalized matrix trace has these properties on the full matrix
algebra.

`<2>2.` If `T>=0` and its restricted trace is zero, every eigenvalue of the
positive matrix `T` is zero, hence `T=0`.  Restriction is faithful.

`<1>9.` Thus the arithmetic mirabolic realization supplies its star,
positivity and physical trace from an actual finite Hilbert space.  Rosso's
polynomial presentation alone is not used to claim the same for arbitrary
positive real parameters.  **QED** (MIR-AFF)

## 2. MIR-GEN — the vector generator is a controlled Weyl projection

**ASSUME** D1142 and D1241--D1242 in addition to the hypotheses above.

**PROVE** the Hecke context algebra and the controlled translation constraints
generate exactly `R_X(L)`.

`<1>10.` Embed the complete-flag Hecke algebra into invariant kernels by

`h(F,F') |-> h(F,F') delta_(v,0)`.

Under `<1>4`, its operator on `C[X] tensor C[L]` is `A_h tensor I_L`.

`<2>1.` The delta condition forces input and output vector coordinates to
coincide.

`<2>2.` Convolution reduces to flag-kernel multiplication, so the map is a
unital star homomorphism.

`<2>3.` This is Rosso Remark 3.3, now with its concrete joint-register action
specified.

`<1>11.` Let `F=(U_1(F)<...<U_n(F)=L)` and let `T_0` denote the orbit kernel

`T_0(F,F',v)=[F=F'][v in U_1(F)\{0}]`.

This is Rosso Theorem 3.6's vector generator.

`<1>12.` Put `e=Q^(-1)(T_0+I)`.  Its joint-register action is

`e=sum_(F in X) |F><F| tensor P^X_(U_1(F))`.

`<2>1.` The kernel of `T_0+I` is one when `F=F'` and
`x'-x in U_1(F)`, and zero otherwise.

`<2>2.` Dividing by `Q=|U_1(F)|` averages translations by the line
`U_1(F)`.

`<2>3.` This is D1142's `P_U^X=|U|^(-1)sum_(u in U)X(u)`, with the context
flag controlling `U`.

`<1>13.` Directly, `e=e^dagger=e^2`: it is blockwise a finite-group averaging
projection.  Its physical trace is

`tau_Q(e)=1/Q`, `tau_Q(1-e)=(Q-1)/Q`.

`<2>1.` Each flag block `P^X_(U_1)` has rank `|L|/Q` on `C[L]`.

`<2>2.` Divide the total rank `|X||L|/Q` by `|X||L|`.

`<1>14.` Equivalently `T_0=Qe-I` and

`T_0^2=(Q-2)T_0+(Q-1)I`.

This recovers Rosso's relation (8) from the physical projection.

`<1>15.` Rosso Theorem 3.6 proves that `T_0,T_1,...,T_(n-1)` generate the
whole mirabolic convolution algebra; the `T_i`, `i>=1`, are the simple Hecke
flag kernels.

`<1>16.` Therefore

`R_X(L)=C^*( A_(s_i) tensor I, C_i^X : 0<=i<=n )`

and in fact `C_1^X` together with the simple flag kernels already generates.

`<2>1.` The inclusion from right to left holds because every `C_i^X` commutes
with affine translations and is invariant under the simultaneous G-action.

`<2>2.` The reverse inclusion follows from `<1>12` and Rosso's generation
theorem: `C_1^X=e` and the simple kernels generate all of `R_X(L)`.

`<2>3.` The extra `C_i^X` are useful typed tests but are redundant as algebra
generators.  No unquoted formula expressing them as words is needed.

`<1>17.` This identifies the vector extension on the nose.  It is stronger
than an abstract isomorphism with a q-rook algebra: it fixes the Hilbert
module, orbit basis, star, trace and Hecke inclusion.  Rosso Proposition 5.2
does not fix those data and is not used here.  **QED** (MIR-GEN)

## 3. MIR-FOURIER — exact identification with controlled Z constraints

**ASSUME** a named nontrivial additive character `psi:k->U(1)` and D1243.

**PROVE** Fourier transform plus dual-flag reversal identifies `R_X(L)` with
the algebra generated by the existing Hecke transitions and controlled
`P^Z` constraints on the dual register.

`<1>18.` Define the unitary finite Fourier transform

`F_(L,psi)e_x=|L|^(-1/2) sum_(lambda in L^vee) psi(-lambda(x))e_lambda`.

Character orthogonality proves unitarity.

`<2>1.` The inner product of columns `x,y` is
`|L|^(-1)sum_lambda psi(lambda(x-y))`.

`<2>2.` The sum is one when `x=y` and zero otherwise because the dual
characters separate points.

`<1>19.` For `U<=L`, let `U^perp={lambda:lambda(U)=0}`.  Then

`F_(L,psi) P_U^X F_(L,psi)^*=P_(U^perp)^Z`.

`<2>1.` Fourier conjugates `X(u)` to the diagonal multiplier
`e_lambda |-> psi(-lambda(u))e_lambda`.

`<2>2.` Averaging over `u in U` is one exactly for `lambda in U^perp` and
zero otherwise.

`<1>20.` Define dual-flag reversal by

`D_L(F)_j=U_(n-j)(F)^perp`, `0<=j<=n`.

It is a bijection `Fl(L)->Fl(L^vee)`.

`<2>1.` Annihilators reverse inclusions and
`dim U_(n-j)^perp=j`.

`<2>2.` Applying annihilator twice under `L=(L^vee)^vee` recovers the
original flag.

`<1>21.` If a pair `(F,F')` has type-A relative position `w`, then
`(D_LF,D_LF')` has relative position `w_0 w w_0`.

`<2>1.` In the rank-matrix convention,
`r_w(i,j)=dim(U_i intersect U'_j)`.

`<2>2.` The reversed-dual rank matrix is
`i+j-n+r_w(n-i,n-j)` by annihilating `U_(n-i)+U'_(n-j)`.

`<2>3.` Direct counting of the permutation matrix shows this is
`r_(w_0 w w_0)(i,j)`.  Thus simple `s_i` is sent to `s_(n-i)`.

`<1>22.` Let `D` also denote the flag-basis unitary and set

`W_(L,psi)=D tensor F_(L,psi)`.

Then

`W C_i^X W^*=C_(n-i)^Z`,
`W(A_w tensor I)W^*=A_(w_0 w w_0) tensor I`.

`<2>1.` The first identity is `<1>19` with
`U_i(F)^perp=D(F)_(n-i)`.

`<2>2.` The second is `<1>21` applied to the orbit adjacency kernel.

`<1>23.` Consequently

`R_Z(L^vee):=W R_X(L) W^*`

is exactly

`C^*( A_w tensor I, C_i^Z : w in S_n, 0<=i<=n )`

on `C[Fl(L^vee)] tensor C[L^vee]`.

`<2>1.` By `<1>16`, the Fourier image is generated by the displayed Hecke
operators and `C_(n-1)^Z`.

`<2>2.` Every displayed `C_i^Z` is the image of `C_(n-i)^X`, which belongs
to `R_X(L)` by `<1>16`; hence adding all of them does not enlarge the image.

`<2>3.` The endpoint indices matter: `C_n^Z=I`, while
`C_0^Z=I_(flags) tensor |0><0|`.  In rank one the mirabolic generator
`C_1^X` maps to `C_0^Z`; omitting index zero would incorrectly reduce the
rank-one target generators to scalars.

`<1>24.` Equivalently, `R_Z(L^vee)` is the commutant of the simultaneous
dual-Levi action and the phase-multiplier group obtained by Fourier conjugating
the affine translations.  It is a phase-affine commutant, not another claim
that phase multipliers are vector translations.

`<1>25.` A same-register implementation requires a named linear isomorphism
`sigma:L->L^vee`.  Transport along `sigma` sends `<1>23` to the existing
joint Hilbert space `C[Fl(L)] tensor C[L]` and identifies its generated algebra
with the controlled-Z sector in D1142.

`<1>26.` If `sigma'` is another self-duality, the two implementing unitaries
differ by the simultaneous action of a unique `g in GL(L)`.  That action
commutes with every element of the controlled-Z algebra.

`<2>1.` Write `sigma'=sigma g`; transport of vector and flag labels differs
by `g^(-1)` on both registers.

`<2>2.` D1142's covariance says simultaneous Levi conjugation fixes the
generated invariant algebra elementwise.

`<2>3.` Thus the algebra isomorphism is independent of `sigma`, although the
chosen implementing Fourier unitary and the identification of individual
labels retain `sigma`.

`<1>27.` The character `psi` likewise remains part of the Fourier morphism.
Changing it rescales the dual labels by a nonzero field scalar and hence gives
Levi-conjugate implementations, but it does not create a canonical phase
operator after the datum is forgotten.

`<1>28.` The construction is natural for linear isomorphisms:

`F_(L',psi) R(g)=R(g^(-vee)) F_(L,psi)`

with the corresponding dual-flag square. Only the vector Fourier factor
is tensor-preserving under the canonical direct-sum/dual identifications.

`<2>1.` Naturality follows termwise by substituting
`lambda'=lambda o g^(-1)` in the Fourier sum; applying g to subspaces gives
the corresponding dual-flag square.

`<2>2.` On vector registers the character kernel and normalization factor,
so `F_(L direct-sum M)=F_L tensor F_M`. Complete-flag Hilbert spaces do not
have this direct-sum tensor identification.

`<2>3.` For the D1256 decomposable flag-vector isometry J, let Rev send a
shuffle word to its reversed word. Under the named double-dual and vector
factor identifications the actual full-bridge equation is

`W_(L direct-sum M) J_(L,M)`
` = J_(L^vee,M^vee) ((W_L tensor W_M) tensor Rev)`.

Indeed the reversed annihilator of a decomposable step `U_a direct-sum V_b`
is `U_a^perp direct-sum V_b^perp`; reading the steps backwards reverses the
shuffle, while the component flags become their dual reversals. The vector
Fourier part factors by `<2>2`. This proves the displayed equation on a basis.

`<2>4.` Thus the full bridge transports the proper decomposable corner and
its shuffle correspondence to the Fourier-conjugate dual arena. It is not a
tensor identification of the full flag registers. For one-dimensional
`L=M=F_2`, the full composite has three flags and the decomposable shuffle
subspace has two, while the two separate flag registers have dimension one.

`<2>5.` Applying the negative Fourier kernel twice gives

`F_(L^vee,psi)F_(L,psi)e_x`
` = |L|^(-1)sum_(y in L)sum_(lambda in L^vee)psi(-lambda(x+y))e_y`
` = e_(-x)`.

Here the inner sum uses character orthogonality and the canonical evaluation
identification of L with its double dual. Since `D_(L^vee)D_L(F)=F`,
`W_(L^vee,psi)W_(L,psi)e_(F,x)=e_(F,-x)`, exactly D1243/D1259. In
characteristic two this is the identity on vector labels.

`<1>29.` This proves the comparison groupoid D1244.  It retains `psi` and,
when a same-register unitary is requested, `sigma`; the forgetful functor to
finite C*-algebras retains only the canonical conjugacy class of the bridge.

`<1>30.` The full Weyl matrix algebra does not interpolate inside this
commutant.  For example a nonzero translation fails to commute with all phase
multipliers in `R_Z`, and a nonconstant phase multiplier fails to commute with
all affine translations in `R_X`.

`<1>31.` What has been recovered is exact and positive: all context Hecke
transitions and all controlled commuting Weyl constraints.  The central
Heisenberg character, cocycle and individual noncommuting Weyl displacements
remain separate phase data; no equivalence with the full Weyl observable
algebra is asserted.  **QED** (MIR-FOURIER)

## 4. Scope carried to admission

`<1>32.` MIR-AFF and MIR-GEN are arithmetic finite-C*-algebra statements for
prime powers `Q`; their positivity is an operator theorem.

`<1>33.` MIR-FOURIER is a unitary comparison at each arithmetic fibre and is
natural for isomorphisms.  Its phase and dual-label data must travel with the
comparison even when the underlying algebra map is independent up to Levi
conjugacy.

`<1>34.` The continuous positive trace and its GNS endpoint are proved from
explicit orbital valencies in `mirabolic-trace.md`; they are not consequences
of Rosso's presentation alone.

`<1>35.` No generic mirabolic ordered assembly map has been proved here.
Type-C direct-sum composition is handled instead by the finite-field positive
correspondence in `type-c.md`.
