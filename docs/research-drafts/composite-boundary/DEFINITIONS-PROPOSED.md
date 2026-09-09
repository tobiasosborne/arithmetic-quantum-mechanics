# Proposed definitions: composite relative Frobenius boundary

2026-09-09. Proposed D1601--D1607; no admission yet. Existing definitions
retain their numbering and conventions, in particular D8's Weyl sign and
D1306's negative Fourier kernel.

## D1601 (completed concrete arithmetic source)

For a finite named field diagram I in characteristic p, let A_I^mat be
the image of the D1324 arithmetic amplitude interpretation, with equality
of typed actual matrices and scalars in R_p=Q(zeta_p,sqrt(p)). Its finite
additive completion has finite lists of objects and rectangular matrices
of its arrows. Its self-adjoint projection completion has objects (X,e)
with e=e^*=e^2 an actual endomorphism in that completion, and arrows
f:(X,e)->(Y,g) given by actual matrices f=gfe. Hilbert realization is ran e.
Independent tensor is the actual tensor of words, projections and arrows.

Use finite retained Kraus lists of these arrows whose actual squared
amplitudes sum to at most the source identity; normalized lists have sum
equal to that identity. Classical tags use block output algebras and sum
of ordinary traces. States include the D1501 and D1503 additional reference
preparations and the prescribed fixed zero preparations. Coherent sums
retain source Hom blocks; they are not classical tags. No surjectivity
onto all complex CP maps is stipulated. Collective assembly is specified
by actual isometries, arithmetic circuits and projections in this source.

## D1602 (relative multiplication-graph register)

Fix a named extension E/K with |K|=q=p^s, |E|=q^n=p^r, r=sn and n>=1.
Let sigma(x)=x^q and let U|x>=|sigma(x)> on the D1301 field register.
For each sigma-orbit O of length d|n and k in Z/d, put

    v_(O,k)=d^(-1/2) sum_(x in O)|x,sigma^k(x),x sigma^k(x)>.

Let G_(d,k) be the diagonal projector on precisely the computational
tuples appearing in this sum as O varies over length-d orbits. Put
G=sum_(d|n)sum_(k=0)^(d-1)G_(d,k), Delta=U tensor U tensor U, and
T=(1/n)sum_(j=0)^(n-1)Delta^j. Define P=TG and
P_d=T sum_k G_(d,k), Q_(d,k)=T G_(d,k). That these are self-adjoint
projections and have the advertised ranges is a claim. The Hilbert
register H_(E/K)^rel is ran P, with its inherited inner product.
No origin in an orbit is chosen. The square roots in the displayed
normalized vectors are positive real normalizations for analysis, not
additional coefficients required of their ambient projector matrices.

## D1603 (relative Frobenius and common observables)

For D1602 use the actual multiplication M=M_E^(2) of D1308 and set

    R=M (I tensor U tensor I) M^*,
    E_(d;a,b)=Q_(d,a) R^(a-b) Q_(d,b).

Let B_(E/K)^rel be the complex star algebra generated on ran P by R|ran P
and all Q_(d,k). Let B_n=direct-sum_(d|n)M_d(C), with matrix units e_(d;a,b),
and let S_n=direct-sum_(d|n)S_d, S_d|k>=|k+1 mod d>.
The proposed comparison sends e_(d;a,b) to E_(d;a,b).
For n>1 the primitive relative component means the d=n component;
its abstract algebra is M_n(C). These common observables do not include
arbitrary operations on or between different orbit multiplicities.

## D1604 (copied reference preparation and retained histories)

For D1602 with n>1, let Pi_n project in H_E onto labels of sigma-period n.
Let C:H_E->H_E^tensor3 be C|x>=|x,x,x^2>, realized by two zero ancillas,
controlled addition into the second slot, and M_E^(2) into the third.
For one input rho_E(h) of D1501, or lambda_E(h) of D1503, use the
three preparation Kraus amplitudes

    K_cut=I-Pi_n : H_E -> H_E,
    K_fail=(I-T)C Pi_n : H_E -> H_E^tensor3,
    K_ok=T C Pi_n : H_E -> H_E^tensor3.

Their output tags are primitive-cut failure, averaging failure, and success.
On success apply R, then measure the projection Q_(n,1), retaining its
complement. The other histories stop at their stated objects. In the
dephased comparison, the computational dephasing channel on all three
slots is inserted immediately before R. In the identity comparison R is
replaced by I. All comparisons use the same final projection, including T.
The two zero ancillas are fixed states, not additional POS references.

## D1605 (primitive relative quantum boundary)

For D1604 retain the D1506 order, leading probability coefficient and
conditional state on the common M_n observable algebra. The candidate
boundary realization has algebra M_n(C), state |0><0|, projections |k><k|,
the matrix units generated in D1603, and the channel Ad(S_n) on that block
(here S_n denotes the single n-cycle when only that block is under discussion).
Use the full graded physical preparation before any later continuation;
this definition does not identify physical multiplicity states across p.

The quantum boundary's arithmetic processes are those induced by the
displayed common matrices and specified instruments. A larger category of
all CP maps is an explicitly optional envelope. No tensor or sum operation
between boundary objects, and no conventional C_1, is stipulated.

## D1606 (fixed-base relational transfers and Fourier return)

For a named K-embedding i:E->F between finite extensions of the same
named K, let J_i be the D1304 label inclusion. Its candidate relational
isometry is J_i^rel=(J_i tensor J_i tensor J_i)|ran P_(E/K).
Its retained decoder has successful amplitude (J_i^rel)^* and failure
amplitude I-J_i^rel(J_i^rel)^*, with distinct target tags. Towers retain
every stopped history. Comparisons use all period components, with a
length-d component remaining length d in the larger ambient extension.

For D1602 with n>1 let F_first=F_E tensor I tensor I and retain, on the
primitive code, the return amplitude P_n F_first|ran P_n and the ambient
failure amplitude (I-P_n)F_first|ran P_n. Both outcomes are retained.
No invariance under Fourier on other slots is stipulated.

## D1607 (finite relational spectral data)

For D1602--D1603 use ordinary Hilbert trace on H_(E/K)^rel and the
characteristic polynomial det(I-zR|H_(E/K)^rel), including actual orbit
multiplicities. Also keep the separate normalized trace tr_d on a common
M_d block and the linear-map trace on its channel Ad(S_d).
For n>=1 let c_d(q) be D1331's exact-period polynomial evaluated at q.
The copied-reference spectral mixture is formed by applying C and T with
the success outcome retained, then uniformly randomizing over R^j,
0<=j<n, and explicitly discarding that classical randomization label.
It is a different preparation from the unrandomized witness of D1604.
