# Positive arithmetic counting boundary — preregistered falsifiers

2026-09-09, native inherited Codex verifier. Written from
`briefs/positive-arithmetic-goal.md` and the proposed interface messages before
new prover artifacts or verifier calculations. Only stdlib and numpy;
integer, Fraction, and exact cyclotomic arithmetic. Finite samples falsify
but do not prove all-field, all-degree, all-CP, or varying-characteristic claims.

## Independent data and finite bounds

Build polynomial quotient fields directly; verify the displayed moduli and
derive prime Frobenius, periods, embeddings, relative traces, and multiplication
from their field operations. Do not import old checker tables or the prover's
construction. Census/state samples: p=2,3,5 and degrees r=1..4 (maximum Q=625).
Dense Fourier/CP samples use p=2,3 and Q<=27; the degree-four binary inclusion
is included. Rational interpolation t in {1,6/5,3/2,2,3,p}. Taylor coefficients
are compared through order six, exceeding the largest tested reference word
length m<=3. General formulas remain written-proof obligations.

## Gates P1--P7

- **P1 — density, coefficients, arithmetic comparison and moments.** Count
  the nonzero exact-period labels independently. Form diagonal D_E(t) and
  rho_E(t)=t^-r D_E(t). Verify positivity, normalization, rho_E(p)=I/Q,
  rho_E(1)=P0, every Frobenius power modulo r, nonzero/moving masses, and
  recovery of conditional FRL block weights. Derive Taylor coefficients
  independently by expanding each exponential monomial; compare with Jordan
  products divided by k!b_d(p), including d=1. Check coefficient positivity,
  trace r^k/k!, and exact normalized coefficient-state/Poisson identities.
- **P2 — named embeddings, towers and Fourier contexts.** Construct actual
  F2->F4->F16 and F3->F9 plus F3->F27 maps, and a Frobenius-twisted
  F4->F16 embedding. Check J*D_E J=D_K, J*L_E J=L_K, composite embeddings
  and code success t^(s-r), including degrees divisible by p. Build negative
  Fourier kernels from absolute traces, verify transported J/V reference
  identities and both retained branches. Exhibit failure of naive Fourier
  invariance away from the arithmetic comparison point.
- **P3 — positive state versus invalid tracial continuation.** Construct an
  actual generic two-code joint-support projection from independent J,V
  matrices. Its complement must have nonnegative new-state expectation,
  although the old rank-based continuation 1-2/kappa is negative at a
  specified near-one parameter. Check nontraciality directly; do not impose
  the old tracial rule on this new state.
- **P4 — genuine mixed full circuits and quantum coherence.** Specify
  circuits containing actual multiplication, Fourier, relative Frobenius
  and a transfer/retained decoder. Include a coherent input, actual complex
  phases, and a path leaving and returning to a sector. Compare full
  evolution, measured success/failure histories and forbidden intermediate
  compression separately. A Born witness must detect noncommuting state/
  effects and a corrupted multiplication entry.
- **P5 — positive CP coefficients and finite leading profiles.** Apply
  concrete fixed CP branches to independently computed D-word Taylor
  coefficients, under sequential composition and tensor Cauchy products.
  Compare the first nonzero *matrix*, order, and normalized state with
  Phi(L_word), where L_E=P0+h B_E and B_E=A_E1. Include order-zero, one,
  two and three branches, an entangling CP output, and branches killing all
  grades below m. Verify the tested nonzero branches have order <=m.
  Explicitly test sequential rare postselection for which retaining only
  the leading conditional state loses a later branch, while retaining the
  full finite polynomial profile preserves the composed endpoint. A wrong
  total-degree-one truncation must fail on a two-register active event.
- **P6 — arithmetic activity and arity.** For d=1,2,3, compute multiplication
  active mass, weighted gate trace and squared difference from actual label
  permutations, compare leading order d and conditional value two. Do not
  infer a general Clifford-level classification from this diagnostic.
  Detect relative Frobenius on a vector outside the old joint J/V code
  support, and mutate an actual multiplication-table entry observably.
- **P7 — retained-characteristic dependence.** Compare degree r=2 at p=2
  and p=3. Record the common scalar period moments and shared zero endpoint,
  together with different register dimensions, leading nonzero coefficient
  weights and any specified Born observables which depend on p. No
  characteristic-free endpoint is assumed or inferred from a fixed algebra.

## Red-first and mutation contract

Implement `--red-<name>` modes, advertised in `--help`, changing mathematical
data or an operation rather than the expected answer. Run a substantive red
before the first green. Each final red must exit nonzero at a named assertion;
record the exact path, not merely its exit code. Planned independent defects:
period mass/normalization, Jordan coefficient, reference Fourier invariance,
embedding label, wrong tracial complement, intermediate compression,
coherence erasure, multiplication entry, CP leading profile, degree-one
truncation, discarded later rare branch, and erased characteristic dependence.

Record final green and every actual red CLI with hash and bounded sample
inventory. Every P1--P7 group must have a reachable specific mutation.
Do not fit outputs to themselves or infer operator positivity from trace alone.
The finite-profile theorem remains a candidate until its written proof and
hostile pass; these tests must be able to reject it.

## Interface supplement before implementation

Root/prover supplied the following all-extension mixed protocol as a claim
to test independently. Choose a,b with T(ab)=0 and T(a^q b)=1. Postselect
E,E,K reference labels a,b,0, use target V_i, relative Frobenius on the first
control, M_E^(2), target F_E, retained J_i decoder, and F_K* on success.
Predicted output is base label 1 with success one. Omitting Frobenius or M
gives label zero; omitting F_E gives success 1/kappa when p does not divide
the extension degree and zero otherwise. Dephasing the trace-fibre target
before these operations gives success 1/kappa and the same successful label.
The rare-preparation leading coefficient is independently B_E(a)B_E(b).
Extend exact cyclotomic phase tests to p=5,Q<=25 for this protocol; no
floating phase approximation will be used.

The prover's later formal interface adds D1504 positive-series normalizers.
After the initial P1--P7 implementation, supplement P5 with a multiple-Kraus
branch, independently binomial coefficient-state tensor weights, two actual
qubit CP channel series with normalizers (1+h),(1+2h), their product
normalizer, and cross-multiplied equality after multiplying both numerator
and denominator by (1+3h). The dedicated normalizer mutation changes that
scalar data. Also retain root's independent-versus-copied nonzero diagonal
event: orders two and one respectively, using the actual copy isometry.
P2's coefficient restriction tests cover every grade zero through six.
The multiplication-entry mutation alters one entry of the separately
materialized multiplication-gate table; Fourier/trace data remain computed
from the validated original field, so the mutant fails an observable gate
rather than crashing while constructing a malformed Fourier character.
