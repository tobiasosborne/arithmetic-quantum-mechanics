# Composite degree completion: capped hostile verdict

2026-09-09. **Same-family prover/critic; target-blind lane.**
Runtime: native inherited Codex agent runtime, described by the environment
as GPT-6 based. No separate backend/model-setting attestation was available;
this was not an independently launched, attested `gpt-5.6-sol` CLI run.
No cross-family independence is claimed. No nested agents were launched.

Target: proposed D1611--D1612 and CMP-COMPLETE/CMP-MELLIN in
`docs/research-drafts/composite-spectrum/`. This is the single hostile pass
on this new artifact, not a re-review of the finite CMP repair.

Inputs read: CLAUDE.md, PRD.md, briefs/critic-protocol.md, the relevant
current definition/notation/claim entries, the two admitted finite CMP
shards, FRL-ORBIT's fixed-field derivation, the three target files, and the
new standalone verifier checker with its expectations. The assigned brief
was supplied directly to this agent. No root conversation/reasoning,
SPEC.md, summary file, deprecated snapshot, or prior repair argument was
used. The checker expectations contain a SPEC pathname; that file was not
opened. The current task overrides the generic verdict destination:
all writes are confined to this critic lane; no trunk edits or commits.

**Finding count: 0 FATAL, 0 MAJOR, 2 MINOR.** The proposed mathematics
survives at its expressly selected completion and regulator scope, with
the integer-cutoff precision repair below. Finite passes are falsifiers
only; the infinite assertions were checked by independent derivation.

## Objections

### CS-C1 — MINOR: the tail cutoff needs an integer domain

**(a) Exact location.**
`docs/research-drafts/composite-spectrum/degree-completion.md`, Section 3
`<1>1.<2>1`, lines 151--154; the corresponding CMP-MELLIN statement in
`CLAIMS-PROPOSED.md`, line 9. Neither place binds the otherwise free
cutoff D. The displayed integral comparison is the integer-cutoff one.

**(b) Independent computation.**
For an integer D>=1 and beta>1, each integer d>D satisfies

    phi(d)/d^(beta+1) <= d^(-beta)
      <= integral_(d-1)^d x^(-beta) dx.

Summing gives exactly the stated bound. A real-cutoff interpretation is
false: take D=29/10 and beta=10. The first term of the tail already gives

    sum_(d>D) phi(d)/d^11 >= 2/177147,
    D^(-9)/9 = 1000000000/130564313782821,
    (2/177147)/(D^(-9)/9)
      = 14507145975869/9841500000000 > 1.

The issue is the omitted quantifier, not convergence or the zeta quotient.
The verifier's cutoff samples are all integers and cannot disambiguate it.

**(c) FIX DEMAND.** Write “for every integer cutoff D>=1” in the claim
and at the integral comparison; alternatively use floor(D) in the bound
when defining a real cutoff.

**(d) SURVIVING WEAKER STATEMENT.** For all real beta>1 and all integers
D>=1, the tail after degree D is at most D^(1-beta)/(beta-1). The state,
normalizer and moment formulas are unaffected.

### CS-C2 — MINOR: two named dynamics mutants are bit-identical

**(a) Exact location.**
`theory/lanes/composite-spectrum/check/composite_spectrum_check.py`,
`dynamics_gates`, lines 307--312, and MUTATIONS at line 12; the two
corresponding S3 entries in `check/EXPECTATIONS.md`.

**(b) Independent computation.**
Both `--red-identity` and `--red-central-dynamics` enter the same branch:

    if c.mutation in ('identity', 'central-dynamics'):
        shift = list(range(d))

They produce the same data and both die at the first S3 rank-one
displacement comparison, before reaching the central conjugation test
at lines 323--326. Their substantive execution is identical apart from
the reported mutation name. Thus the 14 named mutation flags represent
13 distinct changes; plain `--red` is already the declared additional
alias for `--red-drop-divisor-weight`.

I separately mutated a COPY's central phase from scalar (-1)^d I_d to
diag((-1)^k). It retained the actual cycle and reached the later S3
central-conjugation comparison, which rejected it. For d=2 and e_01,
conjugation now sends e_01 to -e_01. This demonstrates genuine reachability
of that comparison without pretending the two existing names differ.

**(c) FIX DEMAND.** Mark `central-dynamics` as an intentional alias and
count distinct changes honestly, or give it distinct altered data that
reaches the central-conjugation test.

**(d) SURVIVING WEAKER STATEMENT.** Every named checker flag exits at a
mathematical gate, and every named gate S1--S7 is reached by a failing
mutation. The 14 names do not establish 14 distinct mutation scenarios.
The written distinction between central degree weighting and Frobenius
is correct independently of this duplication.

## Independently VERIFIED CORRECT — do not churn during repair

BEGIN VERIFIED SCOPE

1. **Arithmetic origin of the corner maps.** In F_(q^M), a label's
   relative period d divides N exactly when it is fixed by x->x^(q^N).
   For N|M these fixed labels form the unique q^N-element subfield.
   Every K-embedding of F_(q^N) has exactly this image. Thus it includes
   *every* upper orbit of each period dividing N, not a proper part of a
   multiplicity space. Since J^rel maps v_(O,k) to v_(i(O),k), conjugating
   a lower common matrix unit gives the entire upper common matrix unit
   of the same degree. All other degree blocks vanish. This establishes
   the claimed nonunital corner map with no orbit-origin choice.

2. **First-grade coefficient and completion.** Differentiation of the
   finite exact-period polynomial at t=1 gives phi(d). Substitution
   t=exp(sh) gives s phi(d), and the actual copied orbit average supplies
   1/d. Dividing by fixed s produces eta_d=phi(d)/d multiplying Tr/d.
   These coefficients do not change under a same-base corner inclusion.
   For L_D=lcm(2,...,D), A_(L_D) contains every block up to D. Consequently
   the directed algebraic union is precisely the finitely supported block
   algebra. Its closure in the maximum block norm is precisely c0,
   by truncation in one direction and the uniform-tail estimate in the
   other. No endpoint tensor law is needed by this argument.

3. **C*-algebra and trace domain.** The faithful concrete block
   representation has the stated C* identity. Every element of B_deg has
   unique scalar tail lambda I, and the norm dominates |lambda|, which
   makes the stated unitization closed. On positive elements of A_deg,

       theta(a) = sum_(d>=2) [phi(d)/d^2] Tr(a_d).

   Finite block sums are continuous positive functionals; their supremum
   is lower semicontinuous. Finite central cutoffs increase to a, are
   dominated by a, and converge in norm, while their trace values increase
   to theta(a). This establishes semifiniteness and dense finite-trace
   positive domain in A_deg. Termwise cyclicity and positive coefficients
   establish the trace identity and faithfulness.

4. **The domain warning is essential and is correctly present.** The
   natural cutoff extension to the multiplier identity has infinite mass,
   since sum eta_d dominates the harmonic series. More explicitly, a
   positive element lambda I+a of B_deg with lambda>0 has all sufficiently
   large blocks >=(lambda/2)I_d, hence infinite mass. Therefore a
   finite-trace positive domain cannot be norm dense in B_deg. The
   candidate claims dense definition only on A_deg, exactly as needed.

5. **Dynamics and the precise meaning of outer.** U_deg is unitary by
   preservation of the Hilbert square sum; conjugation preserves c0,
   products, adjoints and positivity at every matrix level. A unitary
   w=lambda I+a in B_deg has |lambda|=1 and asymptotically trivial
   conjugation on norm-one block tests. The actual Frobenius moves e_00
   to the orthogonal projection e_11, with difference norm exactly one
   for every d>=2. This contradicts a scalar tail. In the bounded block
   product, U=(S_d) itself is a unitary multiplier: left/right multiplication
   preserve c0. There is no contradiction between the two assertions.

6. **Both spectra.** The normalized finite Fourier eigenvectors over
   all blocks form an orthonormal basis. A nonzero component of a putative
   eigenvector forces its eigenvalue to be a root of unity, and every root
   occurs at infinitely many multiples of its order. For any point on the
   unit circle, rational-angle eigenvectors give arbitrarily small
   residual norm. Away from the circle, every block inverse is uniformly
   bounded by 1/abs(|lambda|-1), so their direct sum is a bounded inverse.
   Thus point spectrum is exactly the roots of unity and full spectrum
   is exactly the circle. Neither statement concerns Riemann zeros.

7. **Density and regularization.** For beta>1, comparison with the
   convergent positive p-series gives 0<Z<infinity. Counting the d copies
   of each ordinary Hilbert eigenvalue gives Tr(rho_beta)=1, with every
   eigenvalue positive. This proves the trace-class claim. A positive
   bounded a with zero expectation has all diagonal quadratic forms zero;
   its two-plane positive forms force every matrix coefficient to vanish.
   Hence the state is faithful, including on B_deg. Its invariance follows
   because rho_beta is scalar in each Frobenius block.

8. **Connection to the trace, and choice scope.** Direct substitution
   additionally verifies, for bounded positive block observables a,

       omega_beta(a)
         = theta(D_beta^(1/2) a D_beta^(1/2)) / Z_deg(beta).

   The sandwiched operator belongs to A_deg and has finite theta value.
   Thus the displayed density really is the specified degree-regularized
   trace. This statement does not require D_beta itself to be ordinary
   Hilbert trace class: Tr(D_beta)=sum d^(1-beta), which diverges for
   1<beta<=2. No such claim is made. The logarithmic degree flow is central
   and fixes every block observable; it cannot equal Ad(U_deg).

9. **Zeta quotient.** Partitioning {1,...,k} by k/gcd(a,k) independently
   gives sum_(d|k)phi(d)=k. Absolute convergence for beta>1 permits the
   product grouping (sum phi(d)/d^(beta+1))zeta(beta+1)=zeta(beta).
   Positivity permits division, and removing exactly the d=1 term gives
   the asserted minus one. No analytic continuation is required or used.

10. **Moment scope.** The computational-basis diagonal of S_d^j counts
    fixed labels, so it is d for d|j and zero otherwise, also for negative
    j. Weighting with the d-fold scalar density gives the displayed
    finite divisor numerator for j!=0. For j=0 every degree contributes
    and the value is one by density normalization. |U^j|=I has infinite
    unregularized theta mass, so no ordinary theta-integrable trace of
    U^j is thereby defined. These are implementer moments, not traces of
    the conjugation channel.

END VERIFIED SCOPE

## Independent finite recomputation and mutation reachability

The critic-owned `probes/exact_completion_probe.py` imports neither target
nor verifier code. It uses exact integers and Fractions, constructs its
own irreducible polynomial quotients, and was run red first. Its seven
red modes all exit 1 at named mathematical assertions; green exits 0.
`probes/OWN_RESULTS.json` contains outputs and source SHA256
`7790c3e23e73e971c948f6871f19a532b848e12abf822cc2ea6c7ecaacbffa85`.

The arithmetic samples (q,N,M) and directly enumerated upper orbit counts
are:

| (q,N,M) | period -> number of orbits |
|---|---|
| (2,2,4) | 1:2, 2:1, 4:3 |
| (2,2,6), (2,3,6) | 1:2, 2:1, 3:2, 6:9 |
| (3,2,4) | 1:3, 2:3, 4:18 |
| (4,2,4) | 1:4, 2:6, 4:60 |

This includes characteristic two, characteristic three, a nonprime base
field, composite degrees, and two different proper subfield cuts in degree
six. Further exact probes cover d=2..64, s=1,2,3, beta=2,3,4, moments
-12..12, 128 convolution coefficients, and finite tail fragments.

The independent verifier checker was read symbolically and run green and
with every discovered named red flag plus plain `--red`. Its audited
SHA256 is `44b68befc4627f7bbd62e17d75e25837e2dfbc30b16dbe83758e7b2d2a3b926c`.
Green passes 41,216 comparisons. Frozen critic-run results are in
`probes/VERIFIER_RESULTS.json`; no parser/interpreter failure was counted.

| Gate | Mutants that reach and fail a mathematical comparison |
|---|---|
| S1 | corner-unit: nonlinearity at zero |
| S2 | drop-divisor-weight/plain red: actual F4 copied average; reset-corner: conditional mass |
| S3 | identity/central-dynamics: same rank-one displacement, CS-C2 |
| S4 | density-factor: ordinary trace normalization; negative-density: strict positivity; tail-exponent: integral bound |
| S5 | coprimality: literal coefficient count; d1-subtraction: moving coefficient |
| S6 | zero-moment, channel-trace, negative-power: explicit implementer moment |
| S7 | tensor-cycle: actual cycle decomposition |

All seven named gates can fail; no named gate is unreachable. Some
individual algebraic consequences, such as central commutation and
invariance, need data mutations beyond the shipped first-failure modes.
I therefore also mutated three standalone COPIES, preserving originals:

| Additional data mutation | Reached rejection |
|---|---|
| Duplicate one actual embedded field label | S1: whole upper-period label set is no longer the encoder image |
| Replace scalar phase (-1)^d by alternating diagonal (-1)^k | S3: central unitary conjugation no longer fixes e_01 |
| Multiply the two d=2 density entries by 3/2 and 1/2 | S4: positive, normalized density loses cyclic invariance |

The last mutation passes the earlier strict positivity and normalization
tests, so the invariance failure is genuinely reached. Reproducible patches
and `DATA_MUTATIONS.json` are retained in `probes/`; redundant full copies
were removed after execution. No tolerance or numerical fit was used.
Finite checks do not prove any infinite-dimensional assertion above.

## Quantifiers, canonicity, reliance and status register

The same-base embedding condition is explicit and adequate. Nothing
silently specializes to odd characteristic or a prime base field. The
specified Hilbert representation has one common matrix block per degree;
it is not asserted to be the physical Hilbert inductive limit retaining
all arithmetic orbit multiplicities. The relative index k has its actual
graph meaning, so no fresh orbit origin or character is selected.

The c0 completion, minimal unitization, named Hilbert implementation and
central regulator family are explicit choices. Their claim does not
establish a unique regulator, a conventional C1 endpoint, endpoint tensor
or coherent-sum closure, analytic continuation, or a Riemann-zero spectrum.
None of these stronger statements was demanded in this review.

Current CMP-REL, CMP-NATURAL and CMP-TRACE inputs are admitted at the finite
scopes actually used, including CMP-TRACE's n>1 moving-state condition.
No REFUTED claim or unregistered external source is used by the new
argument. The infinite steps above have direct derivations and do not
inherit proof status from a finite checker or from the deprecated tree.

The target definitions and proof identify themselves as UNREVIEWED, and
the candidate claim table states SKETCH pending the capped pass. Those
are honest registers. The new claims are not yet trunk PROVED rows in the
reviewed inputs, and their absence from the current labbook is not a
lockstep defect in an unadmitted draft. Admission must carry these exact
scopes into the live definitions, claim rows and owning labbook section.
No second hostile review of the two minor repairs is requested; the
orchestrator can check them mechanically under the capped protocol.

PASS
