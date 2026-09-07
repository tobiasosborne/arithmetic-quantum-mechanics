# Ordered type-A Hecke tower — prover summary

The bounded candidate is complete in this lane.  Its ground-truth draft is a
386-line Lamport shard with proposed D1101--D1105 and seven claim rows, all
left at `SKETCH` pending the capped review.

For every real `q>0`, the coefficient functional on the type-A Hecke basis is

    tau_n(T_w^* T_v)=delta_(w,v) q^ell(w).

This makes `tau_n` a faithful normalized trace and the left regular
representation a faithful finite C*-representation.  Contiguous blocks give
injective trace-preserving ordered assembly

    iota_(m,n)(T_u tensor T_v)=T_(u x v),

and the trace-preserving expectation is exactly

    E_(m,n)(T_w)=[w in S_m x S_n]T_w.

Umegaki's trace-pairing theorem identifies this orthogonal projection as the
positive faithful conditional expectation; the shard derives its complete
positivity by matrix amplification.  Inclusions and expectations satisfy the
two strict three-block identities.  This supplies state restriction, product
state preparation with density `iota(h tensor k)`, and a coherent sector of
inner unitary processes.  The CP lane owns the broader Kraus-context process
definition at D1121 onward.

For a finite field of prime-power order `Q`, relative-position adjacency
operators on complete flags give a direct trace-preserving isomorphism

    H_n(Q) ~= End_(GL_n(F_Q))(C[complete flags]).

The adjacency-operator convention resolves the usual convolution opposite:
`A_w^*=A_(w^-1)` and normalized operator trace is the coefficient trace.
Iwahori 1964 is the primary source for the commutant, Bruhat basis,
presentation, and index `Q^ell(w)`.

The decisive arithmetic-memory result is intrinsic to the overlapping
subsystem diagram.  Although the abstract algebras

    H_1=C,  H_2=C^2,  H_3=C^2 direct-sum M_2(C)

do not depend on `q`, the two standard `H_2` subalgebras inside `H_3` do.  In
the unique `M_2` summand, their unordered minimal projections have overlap
multiset `{a,a,1-a,1-a}` with

    a=q/(q+1)^2 <= 1/4.

The minimum therefore determines `{q,q^(-1)}` without a generator label or
the coefficient trace, and determines `q` uniquely after imposing `q>=1`.
The marked level-two trace gives the simpler formula
`tau_2(e_triv)=1/(q+1)`.  The reciprocal ambiguity is real:
`T_i -> -q S_i` is a trace-preserving *-isomorphism
`H_n(q) ~= H_n(q^(-1))`.

The overlap is operationally visible.  With `e_i=(T_i+1)/(q+1)`, the central
standard-block projections `P_i=z_std e_i`, and `u_1=2e_1-1`, conjugation by
`u_1` is the identity on the isolated left `H_2` but acts nontrivially on
`H_3`.  Preparing the pure standard-sector state `P_2` and measuring `P_2`
changes the Born probability from

    1  to  (1-2a)^2.

At `q=1` this is `1/4`.  This is an explicit collective qubit process, not an
analogy based only on block dimensions.

The `q=1` specialization is exactly `C[S_n]`.  For `q!=1`, the self-adjoint
Hecke braid generators are not unitaries, and only ordered block assembly has
been proved.  No symmetric assembly is claimed.

The arithmetic bridge is intentionally narrow.  Given a named polarization
`V=L direct-sum L^vee`, this tower is the complete-flag context algebra inside
the chosen Lagrangian `L`.  It omits Weyl translations, phases, symplectic
maps moving `L`, and arbitrary CP-process extensions.  It is not the full
finite-field Weyl--Heisenberg AQM.  The next provable bridge is to embed these
flag contexts and their expectations into a polarized stabilizer/parabolic
process theory and prove how a change of Lagrangian transports the overlap
diagram.

Primary sources are local in `sources/`: Iwahori 1964, Umegaki 1954, and
Stinespring 1955.  `SOURCE-MANIFEST.md` records publisher URLs, exact PDF
hashes, and theorem/page locators; `sources/primary-extracts.tex` is a short
locator sheet.  The weakest proof leaf for hostile recomputation is the
rank-two verification of the standard regular representation at §1 <2>5;
the most important checker target is the basis-projection expectation's
bimodule/CP behavior through level five.
