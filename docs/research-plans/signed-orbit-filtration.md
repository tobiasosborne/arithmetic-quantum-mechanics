# Signed Frobenius orbits and a two-stage boundary

Date: 2026-09-09. Status: conjectural next target, not an admitted theorem.
The question is forced by the arithmetic Fourier relation F_E^2|x>=|-x>.
Negation commutes with Frobenius, but for odd characteristic it does not
fix 1 and is not a field automorphism. This is arithmetic operator closure,
distinct from taking a normal closure of a field extension.

For every odd p and every r, let C_r times C_2 act on F_(p^r)^times by
Frobenius and negation. On an exact Frobenius-period-d point, negation either
leaves that orbit invariant or pairs it with a different length-d orbit.
The first possibility requires even d, and negation must then be the
half-period shift. Call these internal and external signed orbits.

The precise proposed counts, positivity and orders are registered in D1441
and LIM-SIGNED. The explicit conjecture covers ALL odd primes and all
extension degrees; finite checks below only provide early falsifiers.
The characteristic-two action is different because negation is identity.

For d=2^k m even with m odd, the proposed internal/external point counts are

    A_d(t)=sum_(e|m) mu(m/e)(t^(2^(k-1)e)-1),
    B_d(t)=sum_(e|m) mu(m/e)(t^(2^(k-1)e)-1)^2.

Their sum is c_d(t), using divisor inversion. A_d is expected to vanish
at first order with coefficient phi(d), while B_d vanishes at second order
with coefficient 2^(2k-2)J_2(m). For odd d, every signed orbit is external:
B_1=t-1, and B_d=c_d for d>1. The orbit sizes are d for even internal
orbits and 2d for external orbits. Matrix blocks are associated with the
entire signed orbit; origins or equivalent equivariant comparison data must
be named before any physical representation is claimed.

The first candidate is degree two over every odd prime. The nonzero labels
split into p-1 prime-field labels, p-1 trace-zero nonzero labels, and
(p-1)^2 remaining labels. The first two types have signed orbit size two;
the third has size four. Their matrices would give two first-order qubits
and a second-order four-dimensional sector. On the first qubit Frobenius
is identity and negation flips; on the second both flip. The second-order
sector carries the regular C_2 times C_2 action. Thus the refinement can
retain a distinction that ordinary first-order normalization discards.

This does not construct Fourier itself, multiplication, or their combined
positive process category. Its role is to specify the next exact orbit
filtration that a Fourier-compatible model should understand. The existing
MIX-ALL conjecture still requires a common positive mixed-moment rule and
compatible instruments for every finite extension diagram.

Preregistered S1 falsifiers: enumerate nonzero labels in actual odd-field
quotients, obtain Frobenius periods by iterating the permutation, and test
negation membership by traversing those orbits. Compare the two independently
counted kinds with the formulas. A mutation replacing negation by identity
must fail. Independently differentiate the sparse coefficient polynomials
at one to test the claimed first- versus second-order leading terms.
Samples of degrees 1--4 suffice as a first bounded census; they do not
establish the all-degree conjecture.

The first S1/S2 census is now implemented in
`theory/checks/arithmetic_signed_check.py`: F3,F9,F27,F81,F5,F25 pass, as
do the sparse leading-coefficient checks through degree 48. Both deliberate
mutations fail their intended gates. Frozen outputs are in
`numerics/arithmetic-limits/results/signed-evidence.json`; status remains
CONJECTURE pending the general proof and its later review.
