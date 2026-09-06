Lane model: `gpt-5.6-sol`, reasoning `xhigh`, no delegated agents.

# Finite cyclotomic F1 kernel — prover summary

This lane supplies a 434-line Lamport shard and string-anchored proposals for
D1001--D1007 and eight claim rows.  All positive theorem rows remain `SKETCH`
pending the one hostile critic; `F1-CORR` is explicitly `CONJECTURE`.

The bounded positive result is standard finite-abelian Heisenberg mathematics
given a cyclotomic pointed-set interpretation.  For any finite abelian `A` of
exponent dividing `N`, the free pointed `mu_N`-set
`S_A={0} disjoint-union (mu_N x A)` carries the faithful group-with-zero action
with

    W(a,chi)=Z(chi)X(a),
    W(a,chi)W(b,eta)=eta(a)^(-1)W(a+b,chi eta).

After the named base extension `iota:mu_N->C^x`, the `|A|^2` Weyl operators
are an orthogonal basis of `End_C(C^A)`, giving `M_|A|(C)` and finite
Stone--von Neumann.  Isomorphism naturality is exact.  At fixed `N`, the system
is strong symmetric monoidal using balanced smash for phase sets and central
product for Heisenberg groups; using Cartesian product for the latter would
incorrectly leave two centers.

The ring regression is exact and parity-free.  For a local-ring character
`psi:R->mu_N` with `iota o psi in Gen(R)`, use `chi_b(x)=psi(-bx)`.  Then
`W(a,chi_b)=Z(-b)X(a)` and `c=psi(ab')`, matching D8/D16 including `p=2`.
The cyclotomic group is the central pushout `P_psi`, not the raw
`H_beta0(R)`: the raw map has central kernel `ker psi`, which is nonzero for
the trace character of `F4` (order `64` maps to order `32`).

The strict dynamics statement is sharp.  The pointed normalizer is exactly
central phase times the maps
`[u,x]|->[u q(x),f(x)+t]`, where `f` is an automorphism and `q` is a
`mu_N`-valued quadratic phase.  Its phase-space image preserves the chosen
modulation Lagrangian.  Fourier has full support and is not strict monomial,
but its `mu_N`-weighted kernel already gives the canonical exchange
`A <-> A^vee`; a self-Fourier operator requires a named self-duality.

The exact checker independently supports the finite claims: M1 cocycle and
operators, M2 perfect radical, M3 Weyl Gram basis, M4 five D8/D16 ring
regressions, M5 the central kernel, M6 the `C2 x C3` tensor at `N=6`, and M7
Fourier support/orthogonality.  Its registered mutations fail at their intended
gates.  Passing examples are consistency evidence only.

The forward target `F1-CORR` specifies its domain (`LiftHyp_N`, with the phase
lift cochain part of every morphism), target (localized cyclotomic weighted
correspondences), realization (the named `iota`), tensor law, Fourier object,
and possible fixed-level failure.  It additionally requires a realization as
a correspondence sector of a named blueprint/band-style F1 geometry.  This
prevents the target from collapsing to “add `C` by definition.”  It asserts no
canonical self-duality or full Weil splitting and is one candidate among the
sidequest's other developed analogies.

Weakest theorem step for the critic: the converse in `F1-MON` compresses the
argument that normalization of every diagonal character forces the underlying
permutation to be affine.  The shard gives the separation argument, but this
is the first place to recompute.  The main conjectural risk is whether fixed
level `N` is closed under the cyclotomic Gauss composition laws; D1007 makes a
minimal phase enlargement a falsifying outcome rather than hiding it.
