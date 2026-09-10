# Independent recomputation — SP-STAB-REL

Date: 2026-09-10. Critic model: `gpt-5.6-sol`, reasoning `xhigh`.

This is the sole valid blind hostile review lane.  Prover and critic use the
same model family.  I read only the canonical D1701--D1715 material, the exact
SP-STAB-REL claim/DAG, admitted stage-one proofs/adjudication, the registered
primary-source passages, and the four expressly named target files.  I did
not read or list any prover notes, proposal, patch, summary, source-locator
file, invalidated review, or invalidated-review notes, and did not contact the
prover.

I independently authored the finite checker before taking this critic role.
That is a limitation, not validation: the proof recomputation below does not
infer correctness from the checker, and the checker implementation is assigned
to a separate verification actor.

## General reconstruction

Let `X=bar(V_m)+V_n`, with `Omega=-omega_m+omega_n`, and let

    rho(v,w)(T)=W_n(w) T W_m(v)^*.

Direct multiplication gives

    rho(x)rho(y)=psi(Omega(x,y)/2)rho(x+y).

The right-factor order is essential: the two input adjoints multiply as
`W(v')^*W(v)^*`, producing `-omega_m(v,v')/2`.  On the Hilbert--Schmidt
space, `rho(x)^*=rho(-x)`.  The matrix-unit trace of `T |-> ATB` is
`Tr(A)Tr(B)`, so admitted Weyl trace orthogonality yields
`Tr_Hom rho(x)=p^(m+n)[x=0]`.

For `R=r+L`, isotropy removes the multiplier on `L`.  The normalized
character average

    P_R=|L|^(-1) sum_(l in L) psi(Omega(r,l))rho(l)

is self-adjoint, fixes precisely the D1715 simultaneous eigenspace, and has
trace `p^(m+n)/|L|=1`.  Thus it is an orthogonal rank-one projector.  If
`r'=r+l_0`, then `Omega(r',l)=Omega(r,l)` for all `l in L`; this proves the
all-origins definition equals any one-origin computation without retaining a
choice.

For a nonzero line element `T`, define its projective Weyl stabilizer
`D(T)={x:rho(x)T in C T}`.  Two such labels have scalar actions on `T`, so
the Weyl commutator and faithfulness of the prime-field character force their
symplectic pairing to vanish.  Closure under addition and repeated addition
gives an Fp-subspace.  Since `L subset D(T)`, `L` is Lagrangian, and an
isotropic subspace has dimension at most `m+n`, one gets `D(T)=L`.  Equality
of eigencharacters then determines `r` modulo `L`.  This recovers the affine
relation and proves faithfulness, with zero reserved for the empty relation.

## Supports and composition

For `A_R={a:(0,a) in L_R}`, the output equations put the range of `T` in
the eigenspace with character `psi(-omega_n(r_n,a))`.  Lagrangianity gives
`pr_n L_R=A_R^perp`.  Weyl operators from `A_R^perp/A_R` restrict to an
orthogonal basis of the full endomorphism algebra of this eigenspace.  Hence
`TT^*` commutes with the full endomorphism algebra on the support and is a
positive nonzero scalar times its projector.  Repeating the calculation for
`B_R={b:(b,0) in L_R}` gives
`T^*T=d_R P_R^in` with input character
`psi(-omega_m(r_m,b))`; this sign follows by taking the adjoint of
`T W_m(b)^*=psi(+omega_m(r_m,b))T`.

For composable nonempty `R,S`, the two middle affine projections meet iff
`s_n-r_n in A^perp+B^perp`, equivalently their support characters agree on
`A cap B`.  Expanding the two character projectors gives

    Tr(P_B P_A)=p^n |A cap B|/(|A||B|)

in the matching case and zero otherwise.  Since this trace is also
`||P_B P_A||_HS^2`, support overlap is equivalent to a nonempty relational
composite.  Surjectivity of `T` onto its final support and injectivity of `U`
on its initial support then prove `UT` is nonzero exactly in that case.
Choosing a common middle origin cancels the two middle symplectic terms, so a
nonzero `UT` lies in the composite D1715 line.  One-dimensionality completes
the composition equality, including empty factors and nonempty factors with
empty composite.

## Dagger, tensor, and vectorization

For bare converse, `Omega_dagger((r_n,r_m),(w,v))=-Omega(r,(v,w))`.
Taking the Hilbert adjoint conjugates the character and gives exactly the
converse D1715 equation; no time-reversal involution is inserted.

Direct sums add the two D1715 exponents.  The admitted grouped Weyl
comparison identifies the source and target standard-coordinate reorders
with Hilbert tensor factors, proving line-tensor compatibility.  Identity
lines are scalar identity operators by the full Weyl commutant.  The explicit
basis swap, associator and unit maps satisfy the corresponding line equations,
and the admitted SP-TENSOR coherence fixes their grouped order projectively.

For target membership, `c_m(a,b)=(a,-b)` is symplectic from `bar(V_m)` to
`V_m`, because `omega(cu,cv)=-omega(u,v)`.  With
`vec(T)=sum_x delta_x tensor T delta_x`, direct matrix-unit expansion gives

    vec(A T B^*)=(bar(B) tensor A)vec(T),
    bar(W(a,b))=W(a,-b).

Therefore the D1715 line becomes the ordinary Weyl stabilizer-state line of
the standard affine Lagrangian state `(c_m+1)(name(R))`.  Any Lagrangian
direction is the image of the vertical standard Lagrangian under a symplectic
map: the basis-completion correction
`c_i=d_i-(1/2)sum_h omega(d_i,d_h)b_h` has zero mutual pairing in odd
characteristic.  An admitted affine Egorov implementer is a D1307
second-level unitary and sends the computational preparation into the desired
state line.  Contracting the resulting state with the Bell effect
`sum_x <x|tensor<x|` unvectorizes it, so the line consists of actual D1704
amplitudes.

## Every D1307 second-level unitary and fullness

For arbitrary `U in C_2(A)`, uniqueness of Weyl labels gives
`UW(v)U^*=gamma(v)W(g(v))`.  Product labels make `g` additive and therefore
Fp-linear; the commutator and faithful prime-field character make it
symplectic.  Equality of the half-form multipliers makes `gamma` an additive
character.  Nondegeneracy supplies unique `t` with
`gamma(v)=psi(omega(t,gv))`, and rearrangement puts `U` in the D1715 line of
the affine graph `(t,g)`.  This argument treats every D1307 unitary rather
than a selected generating list.

The computational preparation, its adjoint, all nonzero scalar classes, and
zero also have source relations.  Closure already proved for composition,
tensor and dagger gives an induction on every D1704 generating expression.
This proves fullness.  Recovery proves faithfulness, and the standard rank
objects are exactly the target objects.

## Exact independent computation

`RECOMPUTE.py` imports no repository checker or prover code.  It implements
`Z[zeta_3]` independently as pairs with `zeta_3^2+zeta_3+1=0`.  Its run was:

```text
R1 PASS: 729 exact opposite-space vectorization cases
R2 PASS: identity projector Q^2=9Q, trace 9, first column 3I
R3 PASS: supports, zero/nonzero overlaps, and bare-converse adjoint
R4 PASS: missing conjugation detected at ((0, 1), 0, 1); reversed affine character detected
```

The explicit examples include orthogonal computational state/effect lines,
a nonfunctional rank-one relation with both support projectors, a genuinely
complex affine state for which transpose fails but adjoint succeeds, and the
identity-graph group average.

## Frozen checker evidence and copied-data mutation

Frozen checker SHA-256:
`c9ddc1a9a287437f26ee6c179f8f40fe63d0797893114fe6d98d75dc11bfec43`.
Green exited `0`.  All thirteen help-advertised actual-data reds exited `1`
at their named S1--S5 gates.  S1 has three reachable modes, S2 two, S3 four,
S4 two, and S5 two.  `average-sign` and `fixed-seed` reach the same first S3
translated-state acceptance check but mutate different actual data; the
other failure paths are distinct.

As an independent copy mutation, I changed only the relation form used by the
copied checker from `rel.src.dual()+rel.tgt` to
`rel.src+rel.tgt`, leaving every expected equation canonical.  The copy
passed S1--S2 and then exited `1` at:

```text
S3 FAIL: F3 relation image failed an all-origin D1715 equation in Hom(1, 1)
```

The finite checks corroborate conventions and examples.  They do not prove
the arbitrary-rank, every-odd-prime fullness or equivalence statement.
