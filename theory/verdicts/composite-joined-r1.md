# CMP-JOINT-LIMIT — single capped hostile verdict

2026-09-09. **Same-family prover/critic, target-blind lane.** Native inherited
Codex agent runtime; the exact backend model/reasoning setting is not exposed
to this lane. No separate `codex exec` invocation, `gpt-5.6-sol`/`xhigh` run,
or cross-family independence is claimed. I read the target artifacts, local
single sources and admitted input proofs, the critic protocol, and the
independent checker's source/expectations. I did not read root conversation,
root private reasoning, or `JOINED-LIMIT-SPEC.md`. Same-family correlation
remains a limitation; independent exact recomputation mitigates it.

Target: proposed D1621, proposed CMP-JOINT-LIMIT and
`docs/research-drafts/composite-spectrum/joined-limit.md`, sections 1–4.
This is one attack on this new joined-limit artifact. The admitted finite and
degree-completion claims are inputs, not subjects of another repair review.

**Disposition:** no FATAL or MAJOR. One MINOR definition clarification below.
The stated joined convergence, normalization, and operational scope survive.

## 1. MINOR JN1 — explicitly select the exact reference in D1621

**(a) Location.** `JOINED-DEFINITIONS-PROPOSED.md`, D1621, lines 7–16,
especially “D1604 copied primitive reference instrument”; compare
`joined-limit.md`, section 1 `<1>1.<2>1`, lines 17–20, and D1604 in
`definitions.md`, lines 2476–2481.

**(b) Independent counterexample to the ambiguous reading.** D1604 explicitly
allows either the exact reference `rho_E(h)` or the finite-profile reference
`lambda_E(h)`. Their finite-parameter successes differ. With s=1, d=2,
h=1 and t=e, the exact reference has success `(1-e^(-1))/2`, while the finite
profile has success `1/[2(1+2)]=1/6`. Only the exact preparation has D1621's
displayed function `c_d(t^s)/(d t^(sd))`. The joined proof itself already
selects `rho_(E_d)(log t)`, so there is no proof gap once that selection is
made. Both choices have the same first-grade record at fixed finite D.

**(c) FIX DEMAND.** In D1621 explicitly say that, conditional on degree d,
the preparation is the exact D1501 reference `rho_(E_d)(log t)`, followed by
the three D1604 preparation amplitudes and then the declared twirl.

**(d) SURVIVING WEAKER STATEMENT.** Every displayed exact finite-t formula,
the uniform bound and joined limit are proved for the exact reference used
in section 1. Without making this choice, the first-grade finite-D result
survives for either D1604 reference, but the displayed finite-t formula is
not valid for both.

## 2. NOTE JN2 — finite verification does not prove the infinite quantifiers

**(a) Location.** `joined-limit.md`, section 3 `<1>1.<2>1` through
`<1>3.<2>3`, lines 110–157; section 4 `<1>2`, lines 178–191;
`theory/lanes/composite-joined/check/composite_joined_check.py`,
`scalar_gates`, `cutoff_gates` and its module scope declaration.

**(b) Independent computation.** The verifier samples integer beta=2,3,4,
degrees through 64 and finitely many rational t; its physical fields are
binary. My separate probe adds p=3, s=2 and scalar degrees through 120,
but is still finite. Neither computation exhausts every real beta>1, every
degree, every joined path, or every bounded effect. The written domination,
normalizer floor, and trace-norm argument below establish those quantifiers.
The checker correctly declares this limitation, so this is not an objection
to promotion.

**(c) FIX DEMAND.** None to the mathematics; preserve the distinction between
finite falsification evidence and the written infinite proof in admission.

**(d) SURVIVING WEAKER STATEMENT.** The checker alone certifies only its listed
finite comparisons. In combination with the audited written argument, the
full stated CMP-JOINT-LIMIT survives.

## Independently VERIFIED CORRECT — do not churn during repair

```text
1. Actual copied preparation and its tags.
   I constructed finite fields independently by irreducible-polynomial
   search over p=2 and p=3, enumerated absolute/relative Frobenius orbits,
   built the actual multiplication-graph tuples, and formed the density
   of T C |x> using rational amplitudes 1/d. No target checker was imported.
   Cases: (p,s,d)=(2,1,2),(2,1,3),(3,1,2),(3,1,3),
   (2,2,2),(2,2,3),(3,2,2), all at t=3/2.
   The absolute-period reference normalizes exactly. The actual primitive
   mass and averaging trace give c_d(t^s)/t^(sd) and its 1/d fraction.
   Cut failure, averaging failure and success sum to one. Mixtures retain
   both degree and stopped-history tags; no tensor of independent field
   references has been substituted for a copied reference.

2. State restriction, coherence and twirl are distinct operations.
   The actual common restriction is |0><0|. Actual relative Frobenius
   permutes the multiplication graphs cyclically. The full, identity and
   dephased tests before randomization give 1,0,1/d. Averaging the d shifts
   gives I_d/d, with probability 1/d for Q_1 under either R or I.
   This is a common-block density; the physical orbit-multiplicity mixture
   need not be uniform and has not been identified across characteristics.

3. Exact finite assembled example, independent of characteristic.
   For s=1, beta=2, D=3, t=3/2, the prior is (9/13,4/13),
   degree successes are (1/6,5/27), and total success is 121/702.
   The successful degree probabilities are (81/121,40/121), so the
   ordinary-trace block eigenvalues are 81/242 (twice) and 40/363 (thrice).
   At the retained endpoint the block probabilities are (27/43,16/43),
   and the first-grade total event coefficient is 43/78.

4. All-degree analytic bound.
   The nonnegative divisor partition x^d=sum_(e|d)c_e(x), with c_1(x)=x,
   implies 0<c_d(x)<=x^d-x for d>1, x>1. With x=t^s this bounds
   w_d(t) by (1-t^(-sd))/d. The independent telescope
   1-t^(-sd)=(t-1)sum_(j=1)^(sd)t^(-j)<=sd(t-1)
   gives 0<v_d(t)<=1. The derivative of the finite Mobius sum is
   s sum_(e|d)mu(d/e)e=s phi(d), so v_d(1)=phi(d)/d continuously.
   Exact rational probes verify these formulas through degree 120 for
   s=1,2,3 at t=1,1001/1000,6/5,2,3; these samples are corroboration.

5. Uniform normalizer and integer-cutoff constant.
   v_2(t)=(1/(2s))sum_(j=1)^s t^(-j)>=T^(-s)/2 on [1,T].
   Thus Z_D and Z_infty are >=2^(-beta-1)T^(-s), for integer D>=2.
   The positive unnormalized tail is <=D^(1-beta)/(beta-1).
   Directly summing individual block eigenvalue differences gives
   ||rho_D-rho_infty||_1=2(Z_infty-Z_D)/Z_infty.
   The resulting constant is exactly 2^(beta+2)T^s/(beta-1), as stated.
   The cutoff is integer, beta>1, and s is fixed. No uniformity in varying
   beta down to one or varying s is claimed or needed.

6. Trace-class positivity, both orders and arbitrary joined paths.
   Put g_d(t)=d^(-beta)v_d(t). Its l1 tail is uniformly dominated by
   the summable series d^(-beta). A finite head is continuous at one;
   the two tails of its difference cost at most twice the common tail.
   Therefore ||g(t)-g(1)||_1 tends to zero. Normalization costs at most
   2||g(t)-g(1)||_1/Z_infty(t), whose denominator has the positive floor.
   Each d-block has eigenvalue g_d/(d Z), so positivity and ordinary trace
   one follow from the convergent block masses, not from an infinite
   unnormalized Hilbert trace. The uniform cutoff estimate plus this
   endpoint continuity proves the joint path statement. For fixed D,
   finite continuity gives the other iterated order explicitly.

7. Event rate and t=1 interpretation.
   W_D/h=s[(t-1)/log t]Z_D(beta,t)/L_D(beta).
   Along every joined path, the bracket tends to one, the numerator tends
   to Z_deg(beta), and L_D tends to zeta(beta)-1>0. The claimed coefficient
   s Z_deg(beta)/(zeta(beta)-1) follows. At t=1 the raw success is zero;
   rho_(D,1) describes the retained first grade, not an actual conditioning
   of that zero event. Counting-parameter continuation changes the reference
   on actual fixed-p fields; it does not turn p into a real field cardinality.

8. Effects, choices and admitted scope.
   For fixed a in B_deg, |Tr((rho-rho')a)|<=||rho-rho'||_1||a||.
   Conjugation by the stated common cycle unitary preserves this bound.
   These scalar-block states are stationary, and a separate unrandomized
   preparation witnesses the nonidentity action. The named fields, exact
   reference, explicit degree prior, common observable representation,
   chosen completion and regulator are the data used. No unique prior,
   all-CP physical realization, arbitrary p-dependent probe comparison,
   endpoint tensor/sum closure or Riemann-zero spectrum is inferred.
```

## Checker execution, reachability and independent data mutations

The independently audited frozen checker SHA256 is
`d945e902a081db587ef8cf0f0c5344c5fa42dcdfaf06ba4d97fdeecfbff8c51f`.
Green executed **9,272 exact comparisons**:
J1=3,420; J2=1,585; J3=1,740; J4=1,501; J5=1,026.
Every advertised named mutation was discovered from `--help`, run without
additional arguments, and exited 1 with JSON `FAIL` at the following
mathematical gate. None died at argument parsing or an unrelated exception.

| Mutation | Reached failing gate | Falsified comparison |
|---|---|---|
| `condition-zero` | J1 | Divided polynomial versus zeroed endpoint grade |
| `omit-gap` | J1 | Divided polynomial versus omitted t−1 denominator |
| `drop-divisor` and plain `--red` | J2 | Actual F4 copied success versus missing 1/d |
| `reset-copy` | J2 | Actual copied probability versus independent-reference weights |
| `drop-randomizer` | J2 | Total actual trace after omitting one randomizer outcome |
| `wrong-prior` | J3 | Actual prior ratio versus declared d^(-beta) ratio |
| `wrong-normalizer` | J3 | Ordinary trace one of the success density |
| `lost-history` | J3 | Sum of actual tagged history probabilities |
| `vanishing-bound` | J4 | Nonzero endpoint trace distance versus bound multiplied by t−1 |
| `operator-norm` | J4 | Ordinary trace norm versus twice the normalized tail |
| `drop-grade` | J5 | Actual first coefficient versus positive s Z_D(beta,1)/L_D |

All named gates J1–J5 have reachable mathematical failures. The plain red
alias intentionally duplicates `drop-divisor`; other advertised mutations
change distinct data or formulas. Symbolic inspection finds no gate group
whose evidential comparisons reduce solely to two identical expressions:
J1 uses finite polynomial division against a quotient; J2 actual field
amplitudes against period counts; J3 tagged physical output against scalar
mixture weights; J4 individual eigenvalue sums against normalized tails;
J5 actual POS coefficients against first-grade degree formulas. Internal
normalization identities support these independent comparisons rather than
standing alone as evidence.

On **private copies**, my additional data mutations changed (i) the actual
zero-label reference numerator from 1 to 2, reaching J2's actual reference
normalization failure, and (ii) every coefficient of the fixed rank-one
effect from 1/2 to 3/4, reaching J4's orthogonal-projection failure. The
unmodified checker passed. Copies are generated and removed by
`checker_audit.py`; exact exits, gate counts and source hash are preserved
in `checker-audit.json`.

My independent `independent_probe.py` imports no project code and passes
its three finite gate groups. Its `--red field`, `--red coefficient` and
`--red tail` mutations fail respectively at the retained-history total,
the coefficient bound and the factor-two trace-norm identity. The first
field mutation was executed before the successful green run.

## Status register, lockstep and reliance audit

The target claim is explicitly **SKETCH** pending this distinct capped
review; the definition and proof say UNREVIEWED. At review time there was
no joined-limit row marked PROVED in `claims/CLAIMS.md` and no joined-limit
theorem asserted in the compiled labbook source. This is honest for the
isolated proposal. Promotion must carry D1621's explicit reference choice,
the proved scope, this verdict and the owning labbook statement together.
The parent reports that labbook integration is in preparation; I do not
certify unobserved final integration or a PDF build.

The nearest admitted CMP-COMPLETE/MELLIN and CMP-BOUNDARY/TRACE claims are
used at their displayed scopes. The new proof does not inherit PROVED merely
from those inputs. All input rows checked are PROVED; no REFUTED or CONJECTURE
row is used to obtain the joined theorem. Required period positivity and
divisor facts are admitted local inputs; the additional finite sums,
normalizer, trace-norm and limit arguments were independently recomputed.
No unregistered external source or deprecated v0.1 artifact supplies evidence.

PASS
