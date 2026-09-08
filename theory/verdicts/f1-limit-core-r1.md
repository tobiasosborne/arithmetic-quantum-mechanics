# Blind verdict: operational categorical limit core

Reviewer: **gpt-6-astra, xhigh**. Prover: **gpt-5.6-sol, xhigh**.
Date: 2026-09-07. Independent blind lane; different models from the same
provider. Only the six frozen core artifacts, the instructed single sources,
review briefs, root checkers, and registered primary source bodies were read.
No prover SUMMARY, scratch reasoning, prior conversation, or other proof lane
was used. This is the one authorized hostile review, without repair.

**Decision: FAIL(CC1, CC2).** No FATAL found. The continuous Hecke family,
corner and germ constructions, local analytic lifting, and local fibrewise
Gram recovery survive. The proposed operational category has untyped
multi-outcome relations, and its headline worked protocol uses a POVM as
though a particular quantum instrument had been specified. Those are MAJOR
objections to the submitted operational claims, not evidence against the
underlying continuous construction.

Locations below use paths relative to `theory/lanes/f1-limit/core/` unless
another path is given. Step addresses are part of the location.

## CC1 — MAJOR: multi-outcome list identities are not typed circuit relations

**Location.** `02-operational-envelope.md`, OPLIM-2
`<1>9.<2>1`, `<1>11.<2>3–4`, `<1>13.<2>4`; OPLIM-4
`<1>21.<2>2–5`, `<1>22.<2>1–3`; `DEFINITIONS-PROPOSED.md`,
D1207, D1209, D1210. In particular the sequential-list assertion is at
lines 195–199, and the collective interchange equation at lines 248–249.

**Independent type computation.** Let K have outcomes O and L have outcomes
P, with quantum types alpha -> beta and beta -> gamma. Their stated
Heisenberg formulas force these actual process types:

    K : [alpha] -> [beta] underline(O),
    L : [beta]  -> [gamma] underline(P).

Thus `L o K` is not a composite in the free circuit category. The legal
circuit `(L tensor id_O) o K` has target
`[gamma] underline(P) underline(O)`. The advertised fused list
`(L_(p,j) K_(o,i))` is an instrument with target
`[gamma] underline(O x P)`, with the chosen outcome order. These targets are
different words. Planar graph isomorphism, associativity and scalar-unitary
mixing inside a fixed outcome do not identify them.

Likewise `K tensor L` has target
`[beta] underline(O) [beta'] underline(P)`. A paired-outcome instrument
written on the separated quantum outputs has target
`[beta][beta'] underline(O x P)`. Moving the classical O wire through the
second quantum output is not a planar monoidal axiom. For collective
interchange, sequential outcome histories also require a specified bijection
between `((o,p),(o',p'))` and `((o,o'),(p,p'))`. Kraus-index reordering does
not supply a classical-outcome retyping: D1207 expressly forbids mixing
outcomes. Even singleton outcomes need a stated identification with the
monoidal unit if a one-outcome instrument is to be an arrow `[alpha]->[beta]`.

The displayed operator products are valid branch CP formulas. Their validity
does not prove the claimed equalities of typed arrows. The free category on
the declared generator boxes exists, but quotienting it by these unspecified
multi-outcome relations is not the typed presentation asserted in OPLIM-4.

**FIX DEMAND.** Give the classical product/unit/relabeling and required
classical-wire routing maps explicit types and coherent relations, then write
the instrument identities using them; alternatively restrict the current
list-composition/interchange relations to genuinely one-outcome channel boxes
and leave multi-outcome trees as explicitly external typed protocol data.
This requires no quantum block exchange at generic q.

**SURVIVING WEAKER STATEMENT.** Every individual generator has a UCP
realization; deterministic retained Kraus lists compose and assemble; the free
ordered circuit category with only the already typed sound relations has a
UCP realization. Assembly/split alone remains correctly typed. The current
proof does not establish F1-LIM-OP with all its advertised instrument
relations, and F1-LIM-LIFT/BORN cannot inherit that uncorrected presentation.

## CC2 — MAJOR: D1217 specifies effects, not its postmeasurement state

**Location.** `DEFINITIONS-PROPOSED.md`, D1207's POVM clause and D1217;
`04-protocol-continuity-and-example.md`, PLIM-2
`<1>14.<2>3–5` (lines 198–204), `<1>16.<2>2`, `<1>17.<2>3`;
`CLAIMS-PROPOSED.md`, F1-LIM-H3.

**Independent counterexample.** The explicitly invoked POVM generator is
`[x^3] -> underline({s,f})`; its Heisenberg domain is `C^{s,f}`. It has no
quantum output to which the later u_1 can be applied. Even interpreting
"measure the POVM" as some unspecified quantum instrument does not determine
the successful density used in the proof.

Write P=P_2, u=u_1 and h=(q+1)e_2. Both of the following legitimate
corner-Kraus instruments have exactly the asserted POVM `(P,1-P)`:

    I:   K_s=P,    K_f=1-P;
    II:  K_s=uP,   K_f=1-P.

For II, `(uP)^*(uP)=P`, so completeness and the first success probability
are unchanged. Under I the successful density is `P/gamma`. Under II it is
`uPu/gamma`. The protocol next applies u, and `u^2=1`, so II returns to
`P/gamma` and the final P measurement succeeds with probability **1**.
At q=1 the two joint probabilities are therefore respectively **1/6** and
**2/3**, although the stated initial density, refinement, POVM, retained
subsequent u, and final effect are identical. This was independently
recomputed in the six-element group algebra, with exact rational arithmetic.

**FIX DEMAND.** Specify the first measurement in D1217 and PLIM-2 as the
Lüders corner instrument with successful Kraus operator P_2 and unsuccessful
operator `1-P_2`, retain its quantum output, and refer to its successful
branch in the typed tree. Update the claim statement to include that choice.

**SURVIVING WEAKER STATEMENT.** Every displayed numerical formula in PLIM-2
is correct for this specified Lüders instrument. A POVM alone determines the
first outcome probability, not the subsequent return probability or the
successful density. The analytic Born-continuity theorem for specified CP
instrument trees is unaffected.

## CC3 — MINOR: the section-level tensor map needs its balanced domain

**Location.** `01-continuous-hecke-corners.md`, CLIM-2
`<1>11.<2>1–2` (lines 197–202); D1202–D1203.

**Independent counterexample to an ordinary tensor reading.** At m=n=1 and
nondegenerate I, both section algebras are C(I). The proposed fibrewise map
on an ordinary spatial tensor product is restriction from C(I x I) to the
diagonal. For any nonconstant f,

    f tensor 1 - 1 tensor f != 0,
    iota(f tensor 1 - 1 tensor f)=0.

It is not a monomorphism on that domain. The correct injective domain is the
C(I)-balanced tensor product, equivalently the section algebra of the
pointwise fibre tensor products. The existing pointwise monoidal bifunctor
itself has no defect.

**FIX DEMAND.** State the section-algebra domain explicitly as the balanced
C(I)-tensor product and justify injectivity in its standard block basis; do
not call the ordinary spatial tensor map injective.

**SURVIVING WEAKER STATEMENT.** CLIM-2's ordered monoidal C*-category and its
full evaluations are correct with the pointwise/balanced interpretation
already used by the construction.

## CC4 — MINOR: proposed checker references are not the executable gate names

**Location.** `CLAIMS-PROPOSED.md`, all ten `tested in` cells;
`04-protocol-continuity-and-example.md`, exact falsifier contract
`<1>26.<2>1–13`; actual `theory/checks/f1_limit_check.py`, `main` and
`need` calls.

**Independent comparison.** The frozen proof advertises proposed C1–C13
probes. The executable has L1–L14, covering a broader programme, and the
existing operational checker has H1–H14. For example, regular Gram and
parabolic identities are actually H1/H2/H13, the refinement density ratio is
L4, the protocol numbers are L5, and assembly is L14/H3. No executable gate
checks the proposed classical wire tags or a general continuous normalization
algorithm. These proofs must not be represented as verified by nonexistent
C-gate execution. This is a reference/scope mismatch, not a failed analytic
proof and not a request for additional meta-audits.

**FIX DEMAND.** Replace proposed tested-in placeholders by the actual file
and L/H gate identifiers, and identify which assertions have only the written
proof rather than an executable probe.

**SURVIVING WEAKER STATEMENT.** The actual 14 limit gates and 14 operational
gates all pass, with the mutation reachability recorded below. They are
finite falsifiers of their implemented data, not categorical typecheckers or
proofs of general continuity.

## CC5 — MINOR: distinguish fibrewise mixing from continuous/germ equality

**Location.** `03-local-lifting-and-context.md`, LLIM-2
`<1>10.<2>3`; LLIM-3 `<1>19.<2>2–4`; LLIM-4
`<1>26.<2>1–2`; D1210; F1-LIM-CTX.

**Independent boundary example.** LLIM-3 correctly obtains a scalar unitary
separately in each fibre. It does not obtain a continuous choice. Put
`t=q-1`, `u(q)=2e_1(q)-1` in H_2(q), and on a small endpoint interval use

    K(q)=(sqrt(1-t^2)1, t u(q)),
    L(q)=(sqrt(1-t^2)1, t exp(i/t)u(q))  for t!=0,
    L(1)=K(1)=(1,0).

Both lists are continuous and normalized. Their Grams and every retained
context channel agree at every q. For t!=0, the linear independence of 1
and u(q) forces any Kraus mixing U to fix the first index vector and send
the second to `exp(i/t)` times itself. Thus no continuous U exists at t=0,
even after finite zero padding. A constant U certainly does not suffice.

**FIX DEMAND.** Say explicitly that LLIM-3 and LLIM-4's contextual recovery
conclusion is fibrewise. Specify whether interval-presentation mixing means
constant matrices, continuous matrices, or pointwise equivalence. If it means
continuous mixing, do not infer equality of section/germ labels solely from
pointwise Gram equality.

**SURVIVING WEAKER STATEMENT.** The uniform neighborhood with fibrewise Gram
recovery is proved for every fixed n. Local lifting of a chosen normalized
Kraus representative remains valid; neither needs a continuous choice of
unitaries relating every possible pair of equivalent sections.

## VERIFIED CORRECT — do not churn these arguments in repair

```text
1. CLIM-1, all ranks and every compact positive interval:
   T_s acts by [[0,sqrt(q)],[sqrt(q),q-1]] on each length pair.
   B_w delta_e=delta_w recovers coefficients uniformly, proving closedness.
   The fibre trace has strictly positive Gram diagonal q^ell(w); evaluation
   is onto by constant normalized-basis coefficients. All are uniform proofs.

2. CLIM-2, with the balanced tensor clarification in CC3:
   T_s x_alpha=q x_alpha proves x_alpha^2=P_alpha x_alpha; star reverses
   the parabolic. tau(e_alpha)=1/P_alpha is nonzero at every positive q.
   Corners are closed Banach spaces with the inherited C*-identity.
   Ordered block length additivity proves concatenation and interchange.
   P_(alpha concat beta)=P_alpha P_beta gives the product normalized trace.
   Bimodularity restricts the expectation to the corners; Ej=id, while
   jE is generally proper. No collective/product algebra is identified.

3. CLIM-3:
   Finite common neighborhood restriction defines the star-category of germs.
   Evaluation at one is full. A nonzero germ can vanish at one, so the text
   correctly does not impose the endpoint seminorm as a C*-norm. Evaluation
   away from one requires a representative. Positivity is local positivity.

4. Primitive operational semantics and OPLIM-3:
   Preparations, discards, POVMs and individual corner instruments are UCP.
   For K:alpha->beta, cyclicity gives T_o(rho)=(P_alpha/P_beta)sum K rho K*.
   With the uniform classical trace, the full output block is |O| T_o(rho),
   not T_o(rho). At q=1 and two outcomes I independently obtained total
   output trace 1 with this factor and 1/2 without it.
   Assembly has Heisenberg map E, split has map j; spl after asm has Ej=id.
   Product preparation has density j(h tensor k). Contextual preparation
   and discard formulas have the stated direction and normalization.

5. LLIM-1/2:
   Compression of a constant-coefficient raw lift has the desired fibre.
   If S(q0)=e_alpha(q0), ||S-e_alpha||<1/2 ensures a continuous inverse
   square root in the moving corner (the series constant term is its unit).
   Khat S^(-1/2), c*c/tau(c*c), and S^(-1/2) A_o S^(-1/2) give exact local
   Kraus, density and POVM normalization. Zero Kraus branches and rank-
   deficient densities cause no difficulty. Finite common neighborhoods
   suffice; no arbitrary commuting endpoint diagram is claimed to lift.

6. LLIM-3, fibrewise scope:
   H intersect dHd^-1 is trivial because S intersect dS has one point.
   Thus h^-1 d k are distinct, so the selected minor is a permutation matrix
   at one. Continuity keeps it nonzero on an interval depending on n.
   Expansion recovers the coefficient Gram. Gram equality gives unitary
   mixing in each fibre and equality in every retained ordered context.
   Independent endpoint row counts for n=1,2,3,4 were 1,4,36,576.
   No all-q sharpness or rank-independent neighborhood is proved or needed.

7. PLIM-1 for correctly specified typed finite UCP instrument trees:
   Finite products, tensors, sums and continuous trace pairings give
   continuous nonnegative branch/event weights; unitality conserves total
   branch mass. Evaluation commutes with these finite operations.
   D(1)>0 bounds D away from zero locally and gives convergence of N/D.
   PLIM-3's damped oscillatory Kraus branch is continuous, normalized and
   has conditional subsequential limits 1 and 1/4 when success vanishes.

8. PLIM-2 with the Lüders instrument specified in CC2:
   Independently use P1=diag(1,0), P2=[[a,1],[a(1-a),1-a]] in a similar
   (nonorthonormal) two-dimensional representation. The braid defect forces
   a=q/(q+1)^2. Solving tau(1)=1, tau(T1)=tau(T1T2)=0 gives trace weights
   A=1/((q+1)d), B=q^3/((q+1)d), gamma=q/d, d=1+q+q^2.
   Thus success=q(q+1)/d, conditioned density=P2/gamma and return
   (q^2+1)^2/(q+1)^4=(1-2q/(q+1)^2)^2. At one these give 2/3,3P2,1/4,1/6.
   The calculation is uniform for q>0; separate exact group convolution
   at q=1 confirmed it and the alternative-instrument counterexample.

9. CLIM-4 and F1-LIM-ARITH:
   The refinement fibres have P_alpha(Q) elements. J_alpha is isometric,
   equivariant, and J_alpha J_alpha*=e_alpha. Extension J_beta F J_alpha*
   and restriction J_beta* x J_alpha are inverse on the full intertwiner
   spaces and preserve composition/star. Dividing physical traces by the
   respective flag counts gives P_alpha(Q)tau_n. This is valid for every
   prime power, including characteristic 2 and extension fields.
   Arithmetic evaluation, real endpoint evaluation and apartment compression
   have distinct domains. The displayed T_s^2 calculation correctly shows
   the apartment map is not multiplicative at Q>1.
```

The independent matrix calculation used exact symbolic algebra; the endpoint
calculation used a separate rational permutation-convolution implementation,
not either checker's Hecke multiplication routine. The representation in
item 8 is similar to the orthogonal projection model because `0<a<1`.

## Status and proposal lockstep

All ten proposed rows honestly remain SKETCH and the four shards consistently
say prover-lane candidate. No root promotion is asserted. No dependence on a
REFUTED root row was found. The existing PROVED F1-HCK-POS/FLAG/TOWER/LOW and
F1-OP-KCF scopes suffice for the uses made here; this review does not silently
promote F1-OP-KCF-Q or the older F1-OP-FLAGCAT sketch.

| Proposed row | Review scope |
|---|---|
| F1-LIM-CTS | Verified uniformly |
| F1-LIM-CORNER | Verified with CC3 domain clarification |
| F1-LIM-GERM | Verified as a star-category, with canonical evaluation only at one |
| F1-LIM-OP | Blocked by CC1 |
| F1-LIM-ASM | Verified on the correctly typed generator subpresentation |
| F1-LIM-CTX | Verified fibrewise, with CC5 explicit scope |
| F1-LIM-LIFT | Primitive/local analytic proof verified; full circuit formulation depends on CC1 |
| F1-LIM-BORN | Finite CP-tree theorem verified; reference to the whole submitted category depends on CC1 |
| F1-LIM-H3 | Numerical theorem verified only after the instrument choice required by CC2 |
| F1-LIM-ARITH | Corner/flag realization verified; operational circuit layer inherits CC1 |

The frozen lane does not modify the root definitions, claim register or
labbook. Labbook integration is not among the permitted frozen artifacts and
has not been certified. CC4 is the actual proposal/evidence mismatch to fix
before integration. No stronger claim about all CP maps, arbitrary Weyl
polarizations, global canonical lifting, generic symmetric exchange, or a
prime-power sequence tending to one was smuggled into the surviving scope.

Primary bodies checked: Iwahori 1964, pp. 220–221 Proposition 1.4 and
pp. 231–233 Theorem 3.2 (local OCR, since `paper.txt` is essentially empty);
Umegaki 1954, pp. 177–179 theorem and displayed trace-pairing equation (1);
Stinespring 1955, pp. 211–213, definition of CP and Theorem 1. All three are
registered in `refs/LEDGER.md`. Their roles agree with the source claims:
commutant/Hecke identification, tracial expectation, and CP dilation. General
analytic assertions above were checked from the written arguments, not
inferred from the finite test samples.

## Checker execution and mutation reachability

`python3 theory/checks/f1_limit_check.py` exited 0. All 14 advertised red
modes exited 1. `need` accumulates failures and `main` runs every test family
before the final `if FAILED: SystemExit(1)`: later gates are not hidden by an
early failure. The table records the first failing mathematical gate and all
failing gates, rather than treating every nonzero exit as interchangeable.

| Limit mutation | First failure | All failed gates |
|---|---|---|
| descent | L1 product evaluation | L1 |
| density | L2 square-density normalization | L2,L3 |
| outcome | L3 sequential instrument completeness | L3 |
| corner-ratio | L4 corner density/trace duality | L4,L5 |
| context | L5 retained-context return | L5 |
| ancilla | L6 Gram recovery minor | L6 |
| braid | L7 unitarized exchange defect | L7 |
| cycle | L8 fixed-point cycle trace | L8 |
| reference-trace | L9 physical-trace expectation | L9 |
| null-weight | L10 limiting reference null sector | L10 |
| postselection | L11 conditional branch normalization | L11 |
| valency | L12 vector-orbit valency | L12 |
| polar | L13 unitary interval reversal | L13 |
| collective-identity | L14 proper collective coarse graining | L14 |

Every L gate is reached by its own distinct data mutation. In the green run,
L1–L14 respectively recorded 160,6,12,42,19,6,6,164,15,49,22,190,175,39
probes. L1 compares polynomial evaluation with rational multiplication using
shared multiplication logic, so it is a consistency falsifier, not an
independent derivation. L2's fitted density trace is a normalization check,
not a positivity theorem. L6 compares independently indexed output supports
with the required distinct coefficient count. The other gates compare
actual matrix/permutation products, branch weights or orbit counts with
separate relations/formulas; none of the 14 acceptance conjunctions is
wholly a syntactic no-op. Some gates test other programme lanes and are not
evidence for new core theorems.

`python3 theory/checks/f1_operational_check.py` exited 0 with all H1–H14
passing, including independent F_2^3 and F_3^3 flag constructions. All 25
advertised red modes were also run and exited 1 through named failed gates:

| Operational mutation(s) | Failed gate(s) |
|---|---|
| product | H1,H2 |
| trace; positive-domain | H2 |
| expectation; amplified | H3 |
| overlap | H4 |
| local-collapse; density-norm | H5 |
| unitary-braid | H6 |
| injection | H7 |
| kraus; kraus-mix | H8 |
| flag; incidence; apartment | H9 |
| tl-trace | H10 |
| context-size; context-lower | H11 |
| partial-zero; partial-dagger; partial-comp; partial-lax | H12 |
| corner-trace; refinement | H13 |
| bell-sign | H14 |

These runs likewise accumulate failures and continue through the remaining
families before exiting. The `flag` mutation first breaks the F_2 adjacency
quadratic; `context-size` first breaks Gram-coefficient separation;
`corner-trace` first breaks the corner-unit trace; `refinement` first breaks
the containment identity. The additional diagnostics in a family are actual
downstream failures, not unreachable advertised checks.

Two independent mathematical-data mutations were performed on copies in
this critic lane, without changing any target:

1. Replaced the prepared outcome projection P_2 in L5 by P_2/2. Green-mode
   execution exited 1 at L5, including projection idempotence, success and
   endpoint probability failures. This mutates the tested datum itself.
2. Replaced the successful quantum state P_2/gamma by u_1 P_2 u_1/gamma,
   corresponding exactly to instrument II in CC2. It remained normalized,
   but green-mode execution exited 1 at L5's retained-context return and
   endpoint joint probability. The original L5 hard-codes P_2/gamma; it
   does not derive that state from the first measurement's Kraus label.

The classical density factor was independently checked against the uniform
classical trace, and the noncommuting successful-instrument counterexample
was independently recomputed outside both checkers. No new meta-audit or
additional hostile review is requested. One bounded repair of the exact
objections, followed by the orchestrator's specified adjudication, suffices.

FAIL(CC1, CC2)
