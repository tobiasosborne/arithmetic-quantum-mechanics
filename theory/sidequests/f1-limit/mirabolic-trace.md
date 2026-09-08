# Orbital valencies, positive mirabolic fibres, and the trace-supported endpoint

Status: PROVED within the stated hypotheses. Admission and repaired scope
are recorded in `../../verdicts/f1-limit-adjudication.md`.

Definitions D1245--D1248 are recorded in `../../../definitions.md`.  Rosso,
arXiv:1310.3878, Definition 3.2 supplies the common polynomial orbit basis and
polynomial structure constants.  The orbit classification and valency formula
below are local derivations.  The independent finite enumeration required of
the checker is specified in `CHECKER-SPEC.md`.

## 1. MIR-VAL — classify every vector suborbit and count its valency

**ASSUME** `k=F_Q`, `L=k^n`, the standard complete flag `F_0`, its stabilizer
`B`, and a permutation `w in S_n` labelling a relative flag position.

**PROVE** the affine orbital with labels `(w,A)` has valency

`k_(w,A)(Q)=Q^(ell(w)+|down_w(A)|-|A|)(Q-1)^|A|`,

where `A` is an antichain in the poset defined below.

`<1>1.` The stabilizer in `B` of the flag `wF_0` is

`H_w=B intersect wBw^(-1)`.

It contains the diagonal torus and precisely the upper elementary entries
`E_(ij)` for which

`i<j` and `w^(-1)(i)<w^(-1)(j)`.

`<2>1.` Membership in `B` requires the row index not exceed the column index.

`<2>2.` Membership in `wBw^(-1)` imposes the same inequality after applying
`w^(-1)` to both indices.

`<1>2.` Define `i prec_w j` when both strict inequalities in `<1>1` hold,
and take their transitive closure.  The displayed relation is already
transitive, so this is a finite poset on `{1,...,n}`.

`<1>3.` For a vector `v=sum_i v_i e_i`, let `A_w(v)` be the set of maximal
elements of its nonzero support under `prec_w`.  It is an antichain.

`<1>4.` The set `A_w(v)` is invariant under `H_w`.

`<2>1.` Gaussian elimination in the allowed upper-entry pattern factors every
element of `H_w` into the diagonal torus and elementary shears for the pairs
in `<1>1`; closure follows from transitivity of `prec_w`.

`<2>2.` A diagonal element rescales nonzero coordinates and preserves support.

`<2>3.` An allowed elementary shear `I+cE_(ij)`, with `i prec_w j`, changes
only the lower coordinate `v_i` by adding `c v_j`.

`<2>4.` Such a shear cannot remove a maximal nonzero coordinate: a coordinate
strictly above it would have to be nonzero.  It cannot create a new maximal
coordinate either, since new support is created only below existing support.

`<2>5.` The inverse shear has the same form, so the maximal-support antichain
is unchanged in both directions.

`<1>5.` Conversely, every vector with maximal-support antichain `A` lies in
the orbit of

`v_A=sum_(a in A)e_a`.

`<2>1.` Its support is contained in the downset

`down_w(A)={i : i=a or i prec_w a for some a in A}`.

Otherwise a maximal element of its support would not belong to `A`.

`<2>2.` Every coordinate at `a in A` is nonzero.  Independent diagonal
scalings first change those coordinates to one.

`<2>3.` For each `i in down_w(A)\A`, choose one `a(i) in A` with
`i prec_w a(i)`.  The matrix

`I+sum_i c_i E_(i,a(i))`

belongs to `H_w`, is upper triangular unipotent, and sends `v_A` to a vector
with arbitrary prescribed coordinates below `A`.

`<2>4.` Thus the orbit is exactly the set of vectors supported in
`down_w(A)` whose coordinates at every `a in A` are nonzero.

`<1>6.` It follows that

`|H_w v_A|=(Q-1)^|A| Q^(|down_w(A)|-|A|)`.

There are independent nonzero choices on `A` and arbitrary choices on its
strict downset.

`<1>7.` The B-orbit of `wF_0` contains `Q^ell(w)` flags.

`<2>1.` This is the Bruhat-cell cardinality from Iwahori 1964, Lemma 3.1,
pp. 230--231, in the convention already fixed by D1101 and F1-HCK-FLAG.

`<2>2.` For each such flag the residual vector orbit has the size in `<1>6`.

`<1>8.` Therefore the number of points `(F,v)` in the affine suborbit from
the base point `(F_0,0)` is

`k_(w,A)(Q)=Q^ell(w)|H_wv_A|`

and hence is the claimed polynomial.

`<1>9.` The empty antichain labels the zero vector.  Its valency is
`k_(w,empty)(Q)=Q^ell(w)`, exactly the ordinary Hecke valency.

`<1>10.` Every nonempty antichain contributes at least one factor `Q-1`.
This factor, rather than a dimension comparison or an abstract q-rook
isomorphism, controls the reference-trace endpoint.  **QED** (MIR-VAL)

## 2. MIR-POS — the coefficient trace is positive for every real q>1

**ASSUME** Rosso's based polynomial algebra `R_n(q)`, relabelled by the
Q-independent orbit labels `(w,A)` from MIR-VAL, with orbit adjacency basis
`T_(w,A)` and conjugate-linear physical star.

**PROVE** the coefficient functional has an exact positive diagonal Gram form
for every real `q>1` and gives a faithful regular C*-realization.

`<1>11.` Define the coefficient functional by

`tau_q(T_(w,A))=[w=e and A=empty]`.

At a prime power `Q`, this is the normalized operator trace of the affine
commutant realization in `mirabolic.md`.

`<2>1.` A diagonal kernel coefficient evaluates the triple `(F,F,0)`.

`<2>2.` Only the identity orbital contains this triple; transitivity makes the
normalized diagonal average equal to its orbit-basis coefficient.

`<1>12.` At every prime power `Q`, orbit adjacency matrices have

`tau_Q(T_(w,A)^*T_(v,C))`
` = delta_(w,A),(v,C) k_(w,A)(Q)`.

`<2>1.` The left side is their normalized Hilbert--Schmidt inner product.

`<2>2.` Distinct orbitals have disjoint support, giving orthogonality.

`<2>3.` Each row of a transitive orbital adjacency matrix has its orbital
valency many ones, so its squared normalized Hilbert--Schmidt norm is that
valency.

`<1>13.` Both sides of `<1>12` are polynomials in `q`.

`<2>1.` Rosso Definition 3.2 says all orbit-basis structure constants are
polynomials and the star permutes that basis independently of `q`.

`<2>2.` Applying the coefficient functional to a product therefore gives a
polynomial.

`<2>3.` MIR-VAL gives the explicit polynomial on the right.

`<1>14.` Since the equality holds at infinitely many prime powers, polynomial
identity gives, for the generic based algebra,

`tau_q(T_(w,A)^*T_(v,C))`
` = delta_(w,A),(v,C)`
`   q^(ell(w)+|down_w(A)|-|A|)(q-1)^|A|`.

`<1>15.` The same infinite-specialization argument gives
`tau_q(xy)=tau_q(yx)` and `tau_q(x^*)=conjugate(tau_q(x))` identically in
`q`: both hold for normalized matrix trace at every prime power.

`<1>16.` For every real `q>1`, all diagonal values in `<1>14` are strictly
positive.  Thus `tau_q(x^*x)>0` for every nonzero `x`.

`<1>17.` Left multiplication on the Hilbert completion of
`(R_n(q),<x,y>=tau_q(x^*y))` is faithful and satisfies
`L_x^*=L_(x^*)`.

`<2>1.` Traciality gives
`<L_xu,v>=tau(u^*x^*v)=<u,L_(x^*)v>`.

`<2>2.` If `L_x=0`, then `x=L_x1=0`.

`<1>18.` Its image is a finite-dimensional operator star algebra and hence a
finite C*-algebra.  This proves positive non-arithmetic fibres for `q>1` from
the valency formula plus polynomial identities.  The presentation alone would
not have proved this.

`<1>19.` For `0<q<1`, the displayed Gram entries with odd `|A|` are negative.
No positive physical fibre with this star and trace is claimed in that range.
**QED** (MIR-POS)

## 3. MIR-EXPECT — Hecke inclusion and vector coarse graining

**ASSUME** real `q>1`, the Hecke subalgebra from Rosso Remark 3.3, and D1247.

**PROVE** coefficient deletion is the trace-preserving UCP conditional
expectation onto the positive Hecke context algebra.

`<1>20.` The basis elements `T_(w,empty)` are precisely the embedded Hecke
basis `T_w`, and the restriction of `tau_q` is D1101's coefficient trace.

`<1>21.` Define

`E_q(T_(w,A))=[A=empty]T_w`.

By `<1>14`, this is the orthogonal projection from `L2(R_n,tau_q)` onto the
unital star subalgebra `H_n(q)`.

`<1>22.` The orthogonal projection onto a unital star subalgebra of a finite
tracial C*-algebra is its trace-preserving conditional expectation.

`<2>1.` For `b,c in H_n(q)`, orthogonality of `x-E_qx` to `H_n(q)` and
traciality show `E_q(bxc)=bE_q(x)c`.

`<2>2.` Positivity follows by testing, for `b in H_n(q)`,
`tau_q(b^*E_q(x)b)=tau_q((b^*b)x)>=0` when `x>=0`; faithfulness of the trace
on the subalgebra implies `E_q(x)>=0`.

`<2>3.` Applying the same proof in every matrix amplification gives complete
positivity.  The unit is fixed and the trace is preserved by construction.

`<1>23.` The inclusion `i_q:H_n(q)->R_n(q)` is a unital trace-preserving
star monomorphism and `E_q i_q=id`.

`<1>24.` Consequently every normalized Hecke density, effect and Kraus list
from D1106 embeds unchanged in the mirabolic fibre.

`<2>1.` Positivity is preserved by a star monomorphism between finite
C*-algebras and the trace normalization is unchanged.

`<2>2.` A relation `sum_j K_j^*K_j=1` remains the same relation after
inclusion, so the retained list gives the same UCP process.

`<2>3.` Restriction by `E_q` recovers its Hecke Born probabilities and process
action exactly on the included subalgebra.

`<1>25.` This is a genuine positive operational extension and retraction for
each `q>1`.  No cross-rank mirabolic tensor map is needed for this fixed-rank
claim.  **QED** (MIR-EXPECT)

## 4. MIR-END — literal trace specialization and GNS quotient

**ASSUME** algebraic evaluation of the based algebra and coefficient trace at
`q=1`, as in D1248.

**PROVE** the trace radical is exactly the vector-orbit sector and the
trace-supported quotient is `H_n(1)=C[S_n]`.

`<1>26.` Evaluating `<1>14` at one gives

`tau_1(T_(w,A)^*T_(v,C))=delta_(w,A),(v,C)[A=empty]`.

The form is positive semidefinite.

`<1>27.` Its nullspace is exactly

`N_n=span{T_(w,A):A nonempty}`.

`<1>28.` The nullspace of a positive tracial form is a two-sided star ideal.

`<2>1.` Cauchy--Schwarz holds for every positive semidefinite functional.  If
`x in N_n`, apply it to `x` and `a^*a x` to obtain
`tau_1(x^*a^*a x)=0`; hence `ax in N_n`.

`<2>2.` The nullspace is star-stable by traciality, so left stability implies
right stability.  It is therefore a two-sided star ideal.

`<1>29.` The quotient has the `n!` orthonormal classes
`[T_(w,empty)]`, and their multiplication is the embedded Hecke multiplication
at `q=1`.

`<1>30.` Therefore

`R_n(1)/N_n ~= H_n(1)=C[S_n]`

as a traced star algebra, and `tau_1` descends to the faithful group
coefficient trace.

`<1>31.` The coefficient deletion `E_1` from MIR-EXPECT is now multiplicative:
it is exactly the star quotient map, followed by the fixed Hecke-basis
identification.  Thus vector coarse graining becomes exact at the endpoint.

`<1>32.` Rosso's idempotent `e=q^(-1)(T_0+1)` satisfies at one
`1-e=-T_0 in N_n`.  His presentation gives the same quotient by imposing
`e=1`; relations (23)--(26) then leave precisely the symmetric-group
relations.

`<1>33.` The algebraic endpoint itself still contains `N_n`.  Only the GNS
representation of the specialized reference trace kills it.

`<1>34.` Endpoint Hecke states, effects and normalized Kraus processes lift
through the inclusion `i_1`.  Their values survive the quotient because
`E_1i_1=id`.

`<1>35.` Rank one displays what does not automatically survive.  With
`A=T_0=qe-1`,

`A^2=(q-2)A+(q-1)1`,

and the two projection weights are

`tau_q(e)=1/q`, `tau_q(1-e)=(q-1)/q`.

`<1>36.` At `q=1`, the algebraic algebra still has both summands
`C e direct-sum C(1-e)`, while the trace weights become `(1,0)` and the GNS
quotient is `C=H_1(1)`.

`<1>37.` For every `q>1`,

`h_q=q/(q-1)(1-e)`

is a positive normalized density supported on the vector summand.  Its
coefficient has a pole at one, so it has no regular density specialization.

`<1>38.` The same formula gives a normalized state on the corner
`(1-e)R_n(q)(1-e)` in every rank because MIR-GEN gives the same trace weights.
This proves existence of singular state families, not a classification of
them.

`<1>39.` Operational specialization uses D1249's coefficient-continuous
sections that are positive and normalized for every real q>1 on a one-sided
neighborhood. Positivity only on arithmetic fibres is insufficient. The actual
regular circuit/germ category and its quotient evaluation are proved in
`mirabolic-boundary.md` MIR-REG; that proof tests against lifted Hecke
observables to obtain positive quotient densities. Pole densities remain
outside this regular source category and may occupy a trace-null sector.

`<1>40.` No sequence of prime powers tending to one is invoked.  The endpoint
is algebraic evaluation of polynomial identities followed by the GNS quotient
of the evaluated positive semidefinite form.  **QED** (MIR-END)

## 5. Exact scope

`<1>41.` MIR-VAL is a finite-field orbit theorem, independently enumerable.

`<1>42.` MIR-POS proves faithful positive fibres precisely for real `q>1`.
Arithmetic values `Q` retain the canonical affine permutation realization;
general real fibres use the regular representation of the proved Gram form.

`<1>43.` MIR-EXPECT is a fixed-rank operational retraction.  It supplies
states and CP processes but does not itself define mirabolic assembly.

`<1>44.` MIR-END proves the general trace-supported quotient.  The q-rook
algebra comparison in Rosso Section 5 is neither needed nor promoted to a
star-, trace- or tower-compatible identification.

## 6. Exact rank-two interpolation supporting the endpoint falsifier

**ASSUME** the unscaled rank-two orbit adjacency basis of MIR-AFF and Rosso's
polynomial structure constants from D1246.
**PROVE** four distinct arithmetic values determine every structure constant
at one; this justifies the exact interpolation in the root B4 checker.

`<1>45.` For fixed input orbitals i,j and output orbital k, the coefficient
`c_ij^k(Q)` counts intermediate basis points y for a pair in orbital k.

`<2>1.` This is the matrix-product/kernel-composition identity of MIR-AFF
`<1>5`, with each orbit indicator taking only the values zero and one.

`<2>2.` In rank two, the flag-vector set has
`|Y|=|Fl(F_Q^2)| |F_Q^2|=(Q+1)Q^2` points. Therefore
`0<=c_ij^k(Q)<=Q^2(Q+1)` at every prime power Q.

`<1>46.` Rosso's structure coefficient is a polynomial c_ij^k(q) independent
of the finite field. Its degree is at most three.

`<2>1.` A nonzero polynomial of degree greater than three has absolute
value larger than q^2(q+1) for all sufficiently large positive q, by its
nonzero leading term. This contradicts `<1>45` along unbounded prime powers.
The zero polynomial already has the required bound.

`<1>47.` Evaluation at Q=2,3,5,7 therefore determines that polynomial
uniquely: the difference of two polynomials of degree at most three with
four distinct roots is zero. Exact rational Lagrange interpolation at these
four values gives its exact value at q=1.

`<2>1.` This supports `theory/checks/f1_limit_mirabolic_check.py` B4's
rank-two quotient multiplication and five-dimensional null-Gram sample.
It neither substitutes for the all-rank MIR-END proof nor asserts a cubic
degree bound in higher ranks. **QED** (rank-two interpolation)
