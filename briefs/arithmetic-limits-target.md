# General Galois structure and mixed arithmetic limits — 2026-09-09

The user explicitly requests the next round of informed conjectures, provers,
verifiers and the standard capped workflow. They further require results
uniform over arbitrary field extensions and towers, with attention to Galois
closures. Small examples are falsifiers, never the claimed scope.

Effort: about half on general definitions/proofs, a third on exact checks and
the labbook, at most a fifth on review/repair/integration. Four native slots,
including root; inherited models, no nested CLI. Write-isolated lanes under
theory/lanes/arithmetic-limits/. One proof pass, one blind hostile pass, one
repair wave and root mechanical adjudication per positive artifact.

## Research hypotheses and precise targets

### G: general Galois quantization (a conjecture to try to prove now)

For every field K with a named separable closure, write G_K for its absolute
Galois group. Finite separable extensions, and the finite etale algebras
needed to close their tensor products, have a quantum realization on

    H_A = ell^2(Hom_(K-alg)(A,K^sep)).

Use nonzero finite etale algebras and homomorphisms B over A of constant
positive finite locally free rank. Their maps on embedding sets are uniform
surjections; normalized fibre pullback is the candidate covariant isometry.
Conjecture: these maps compose exactly in all towers, respect tensor product
over K through the embedding-set Cartesian comparison, intertwine G_K, and
admit retained CPTP decoders with all independent outcomes.

For a separable field extension A/K, its permutation action factors through
the Galois group of its normal closure (normal core of an embedding
stabilizer). All finite levels jointly recover the profinite G_K action.
Over F_p the cyclic degree-d atom should recover the Frobenius cycle of
length d in the orbit boundary. This is an orbit-type comparison, not an
identification with the cardinality-|A| register or with its physical code
inclusion. Nonabelian Galois groups must be allowed. Inseparable degree is
not detected by embedding sets and must never be silently included in this
claim. General infinite-field Fourier/Haar data are not supplied by it.

### F: uniform two-chart arithmetic (a conjecture to try to prove now)

For every named finite-field embedding i:K->E of degree n>=2, let
q=|K|, Q=q^n, kappa=Q/q, and J,V be the admitted inclusion and normalized
trace-fibre isometries. Study the actual Gram operator J^*V, not only its
trace. The identity Tr_(E/K)(i(x))=n x suggests a complete classification
by whether p divides n. Derive the principal-angle decomposition, projection
algebra, normalized physical trace on its blocks, Frobenius action and
Fourier interchange uniformly in q,n,p.

When n is invertible in K, set D_n|x>=|nx> and L=V D_n. Candidate:
J^*L=kappa^(-1/2)I, so the pair has a two-dimensional angle factor and a
logical H_K factor, with explicit Gram orthonormalization. Verify every
normalization and Fourier scaling/sign. When p divides n, derive the
rank-one Gram case rather than importing the invertible-degree formula.
The quadratic characteristic-two case is essential and is not generic.

### R: conditional Fourier tangent (bounded positive-limit conjecture)

For each nondegenerate two-dimensional angle block, condition on that block
before continuing its angle parameter. As the two code projections coalesce,
adjoin their explicitly normalized difference/off-diagonal direction.
Conjecture: this gives a faithful positive M2 boundary with a retained
Fourier interchange, continuous CP instruments and independent tensor.
Prove exactly which scalar rescaling and which reference trace realize it.
This alone does not establish tower coherence or a full multiplication limit.

### T: coherent tower refinement (added before its prover/checker pass)

For towers with every extension degree invertible in the characteristic,
write L_i=V_i D_(degree i), c_i=kappa_i^(-1/2), s_i=sqrt(1-c_i^2),
and W_i=(L_i-c_i J_i)/s_i. Corrected trace maps are expected to compose.
The direct two-chart frame should embed in the four-path iterated frame by

    C|0>=|00>,
    C|1>=(c_j s_i|01>+s_j c_i|10>+s_j s_i|11>)
          /sqrt(1-c_j^2 c_i^2).

Conjecture: all iterates are coherent through the common path basis; when
kappa_i=t^a_i and t tends to one, the connector has endpoint

    |0> -> |0...0>,
    |1> -> sum_i sqrt(a_i/sum_j a_j) |one excitation at i>.

This supplies an explicit all-length tower target and a positive candidate
for filtered composition. The all-characteristic extension of this law must
be formulated with the singular Gram sectors retained, not assumed from
the invertible-degree formula. Independent tensor keeps higher excitation
sectors; direct tower refinement need not fill that tensor space.

### S: signed-orbit filtration (a precise next conjecture, not this round's proof target)

Fourier squares to negation, so closing the orbit fragment under necessary
Fourier relations requires remembering x->-x as well as x->x^p. For every
odd prime p and every r, consider C_r times C_2 on F_(p^r)^times with these
two commuting actions. If a point has exact Frobenius period d, negation is
either outside its Frobenius orbit (giving a signed orbit of size 2d) or,
for even d, is its half-period shift (signed orbit size d).

Conjecture: for d=2^k m even, m odd, the point counts of these two kinds are

    A_d(t)=sum_(e|m) mu(m/e)(t^(2^(k-1)e)-1),
    B_d(t)=sum_(e|m) mu(m/e)(t^(2^(k-1)e)-1)^2.

For odd d all points are external, with B_1=t-1 and B_d=c_d(t) for d>1.
The internal even counts have a simple zero with coefficient phi(d);
the external even counts have a double zero with coefficient
2^(2k-2) J_2(m), J_2(m)=m^2 product_(ell|m prime)(1-ell^-2).
All these count functions are positive for t>1. Thus closing the arithmetic
symmetries refines some first-order Frobenius sectors into second-order
sectors, suggesting a concrete graded positive boundary. This is a proposed
orbit-count/filtration statement, not yet a full Fourier or multiplication
limit. At p=2 negation is identity and the group action changes; do not
substitute the odd-characteristic formula there.

The verifier may add a bounded preregistered S1 census using its existing
field models. The proof/hostile budget remains on G/F/R/T; S remains a named
conjecture unless separately justified and reviewed in a later round.

An early stress test must check whether the *unconditioned* physical trace
can even continue positively. In the invertible-degree case, two equal-rank
isoclinic projections with angle a=kappa^(-1) have joint-support trace 2/kappa.
A continuation with kappa approaching one appears to give a negative trace
on the complementary projection. Recompute this directly. If confirmed,
record it once as the reason to use the conditional block construction;
do not spend a hostile round on the negative statement alone.

### Remaining mixed arithmetic conjecture

The long-range claim must concern one positive process category retaining
Galois actions, Fourier-related chart changes, multiplication transitions
and their instruments, natural in *all* finite extension diagrams. It must
specialize the orbit fragments with their specified conditional traces and
preserve named arithmetic relation diagrams. Arbitrary constant matrix
envelopes or separate local lifts do not prove it. This round should sharpen
that conjecture using G/F/R and name an explicit next falsifier; do not call
an unspecified category an existence theorem. In particular compare all
finite-characteristic strata and retain the p|n branch information.

## Lanes and reserved interfaces

- orbit-critic: blind review of the existing FRL-ORBIT/POS/COMP/ACTIVE
  package only, including its existing checker and labbook.
- galois: G and its precise finite-field orbit comparison. Reserve
  D1401--D1409 and claim prefix GAL. Write proposed definitions/notation/
  claims, 1--2 structured shards, a self-contained labbook draft, checker
  specifications, PATCH.md and SUMMARY.md. No trunk edits.
- check: independent G/F/R falsifiers, preregistered before proofs land.
  Reserve a new standalone checker arithmetic_limits_check.py in the lane,
  EXPECTATIONS.md, results and summaries. Run red first, then green, then
  all named mutations. Do not silently validate a formula against itself.
- root (then a freed prover slot if useful): F/R constructions, primary
  sources, conjecture formulation and integration. New mixed definitions
  reserve D1421--D1429 and prefix MIX.
- critics launched after each final artifact: fresh contexts, read only
  brief/artifacts/registries/sources, recompute; one repair wave follows.

## Early falsifiers

G1. Nonabelian S3 action on cosets of an order-two subgroup and its regular
six-point cover; normalized pullback, G-equivariance, normal core, exact
decoder success 1/2. Also all small cyclic quotient towers and products.
G2. Verify ternary tensor/tower matrices and all four retained outcomes on
matrix units, including coherent cross-orbit tests. Reject the false
identification of set orbit decomposition with classical quantum sectors.
G3. Exhibit failure of unqualified normalized pullback for nonuniform finite
maps; constant-rank scope must be tested or replaced by an honest category.
F1. Compute J^*V and singular-value squares from actual finite-field trace
fibres, including n invertible and p|n. At least F2->F4, F2->F8,
F3->F9, F4->F16, and a degree-three characteristic-three example if feasible.
F2. Full Fourier intertwining including logical scaling; compare support
dimensions and both branches of each retained decoder.
R1. Exact symbolic/rational trace of the complementary central projection
in the proposed physical continuation; a negative value rejects positivity.
R2. Positive 2x2 tangent matrices, normalized difference, noncommutativity,
Born witness, instrument completeness and independent tensor. Rational
Pythagorean parametrizations can avoid floating square roots.
M1. Retain the known multiplication sector leakage. Test whether compressing
each intermediate gate changes a mixed circuit, versus retaining all chart
outcomes; a new conjecture must say which of those processes it preserves.

## Sources and admission

Use local registered sources or internal derivations. Root is fetching
Stacks 04JI (finite etale/Galois sets), 0BMI (infinite Galois theory), and
Milne's Fields and Galois Theory as needed. Existing FRB-TRACE/TRANSFER are
the arithmetic inputs; no v0.1 evidence. The source results are not newly
claimed discoveries. New positive conclusions require the capped review;
unsettled conjectures stay CONJECTURE/SKETCH with precise scopes. Integrate
the labbook and registries in lockstep, run the session-close suite, and
commit/push the concrete continuation after verification.

## Outcome of this round

GAL-FUNCTOR/DESCENT/IMAGE and MIX-GRAM/CHART/TOWER passed their respective
target-blind capped reviews and were admitted at the stated scopes. The
earlier four FRL claims were reviewed and admitted after the one checker
and phase repair. MIX-ALL and LIM-SIGNED remain explicit CONJECTURE rows.
The final register and next experiment are in HANDOFF.md; proof/status
decisions are in the three new adjudications under theory/verdicts/.
