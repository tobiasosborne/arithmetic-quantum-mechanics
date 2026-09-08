# Blind critic verdict: full traced Karoubi glue

Date: 2026-09-08. Prover: `gpt-6-astra`, `xhigh`. Critic:
`gpt-5.6-sol`, `xhigh`. This is an independent blind cross-model review. I
read the frozen six-file Karoubi artifact, the current definition/claim
proposals on which it depends, the permitted verified scope in
`core-critic/VERDICT.md`, the relevant executable checkers, and the registered
Umegaki and Stinespring source bodies. I did not read a Karoubi summary or
prover reasoning/messages.

Frozen hashes used for this review:

* `01-continuous-traced-completion.md`:
  `c310ada437a0bd0a783d830ef904d0ba693e0342a0b243c0135ca4ba2990d6cd`
* `02-local-lifting-and-operational-glue.md`:
  `5efc42a7f10af360152a7c430096d4af0942ab39d5b10bb44e70a3bf262d22d4`
* `DEFINITIONS-PROPOSED.md`:
  `d0ba474cff4a08b518ab53090d60d8dc41922481d108588a2a813991d2a1c79d`
* `CLAIMS-PROPOSED.md`:
  `2f1ffe55fae015bc872693c76d72412fbba2dac907703dec5fa8f3deee01753a`
* `check_karoubi.py`:
  `af5f7b4c2e1dcce18c6e660462306acf8ec606795022316363d48649cf8a7d3e`
* `CHECKS.md`:
  `f787e6888a243cbdde622c4aa0f7c7a104a74735ffdf919f3b8a9590bd22e454`

## Objections and scope notes

### K1 — MINOR: `d_X` collides with the current single-source notation

**(a) Exact location.** `DEFINITIONS-PROPOSED.md`, D1263 lines 52--66;
`01-continuous-traced-completion.md` KCOM-2 `<1>10`--`<1>11` and KCOM-3
`<1>19`; current `definitions.md` D1121 and the `notation.md` row for
`A_X,Tr_X,tau_X,d_X,j_X,Y,E_X,Y`.

**(b) Independent comparison.** The current register fixes `d_X` as the
positive categorical dimension in the unitary-fusion datum D1121. D1263 uses
the same symbol for the new trace weight `theta_X(1_X)` and expressly says
that no duality or spherical trace is assumed. These meanings need not be the
same: for the parabolic retract `X_alpha`, KCOM-3 `<1>19` gives
`d_Xalpha=1/P_alpha(q)`, a parameter-dependent corner weight. The collision
does not alter any calculation, but copying the proposal verbatim would
violate L4 and obscure the ratio in KLIFT-2.

**FIX DEMAND.** Give the completion trace weight a distinct registered symbol
(or explicitly replace the old notation row by a scoped general trace-weight
definition) and update `d_Y/d_X` consistently on admission.

**SURVIVING WEAKER STATEMENT.** With `d_X` read locally as
`theta_X(1_X)`, every positivity, multiplicativity, expectation and density-
transport formula in the artifact is correct.

### K2 — NOTE: W is a sufficient conditional interface, not an instantiated theorem

**(a) Exact location.** `DEFINITIONS-PROPOSED.md`, D1266 lines 116--136;
`02-local-lifting-and-operational-glue.md` KOP-1 `<1>13.<2>4`,
`<1>14.<2>1`--`<2>3`, `<1>15.<2>6`, and `<1>19.<2>2`;
`CLAIMS-PROPOSED.md`, `F1-LIM-KOP` line 15.

**(b) Independent type check.** W requires the missing classical
product/unit/relabeling maps, routing past quantum outputs, outcome-history
bijections, and sound typed relations. With those data, sequential composition
has the legal intermediate target `Y C^O`, routing changes
`Z C^P C^O` to `Z C^(O times P)`, and parallel composition routes the first
classical wire past the second quantum output before fusing outcomes. The
current root D1218 formulas and the W1--W5 checker give a concrete model of
such data. W therefore repairs the type defect conditionally. The Karoubi
artifact itself does not choose that model, and its proof correctly assumes W
rather than declaring the earlier CC1 issue unconditionally solved.

**FIX DEMAND.** Preserve “conditional on W” in every admitted statement; if an
unconditional operational category is later wanted, instantiate W explicitly
(for example by the repaired D1218 presentation) and register that dependency.

**SURVIVING WEAKER STATEMENT.** For every explicitly supplied W satisfying
D1266, KOP-1 constructs the claimed typed operational category and UCP
realization. Without W, KCOM-1--3 and KLIFT-1--2 still stand, but `Op^U` is not
asserted.

## VERIFIED CORRECT — do not churn in repair

```text
1. KCOM-1 <1>1--<1>7:
   The finite-support matrix corners form a C*-category. Additive sums use
   one same-degree block projection, so both rectangular off-diagonal Hom
   corners are present. Every projection object is a retract of finitely many
   regular degree objects, and every self-adjoint idempotent splits.

2. KCOM-1 <1>3--<1>5:
   The section tensor has the necessary C(I)-balanced domain. In normalized
   Hecke bases, B_u tensor B_v maps to the distinct B_(u times v), proving
   injectivity. Pair-indexed block projections give a well-typed ordered
   tensor; the permutation associators preserve the ordered Hecke blocks and
   satisfy the pentagon entrywise. The complete composition 1^n has unit
   projection in each degree, so additive dagger-Karoubi completion of the
   parabolic category is the full displayed category.

3. KCOM-1 <1>6:
   At a fibre, an algebraic idempotent e is isomorphic to the support
   projection p of ee*. In a faithful finite matrix representation,
   ran(p)=ran(e), whence pe=e and ep=p; the elements e and p are inverse
   corner morphisms. This proves algebraic equivalence while making no false
   dagger claim for a non-self-adjoint presentation.

4. KCOM-2 <1>8--<1>12:
   theta is the ordinary unnormalized matrix trace composed with the faithful
   coefficient trace in each degree. Rectangular cyclicity follows entrywise.
   Continuous projection rank is constant on a connected interval, so a
   nonzero object has d_X(q)>0 everywhere and a uniformly defined normalized
   trace. Matrix trace and Hecke trace multiplicativity give
   d_(X tensor Y)=d_X d_Y. Images belonging to distinct degree pairs occupy
   distinct diagonal blocks even when their total degree collides; therefore
   j is injective on fibres and balanced sections.

5. KCOM-3 <1>13--<1>19:
   The trace-orthogonal projection onto the included unital star subalgebra is
   positive, bimodular and completely positive by the displayed amplified
   argument. A traced UCP retraction fixes the subalgebra in its multiplicative
   domain, so the Stinespring argument proves uniqueness. Constant-coefficient
   raw lifts compressed by p_X(q),p_Y(q) give local corner bases; Gram inversion
   therefore proves genuine continuity for arbitrary projection sections.
   Uniqueness yields the ordered three-factor tower. On parabolic projections,
   theta=tau_n, d=1/P_alpha and tau_X=P_alpha tau_n, so the old normalization
   is recovered exactly.

6. KCOM-4 <1>20:
   For X=[0] direct-sum [1], End(X tensor X) is
   C direct-sum M_2(C) direct-sum H_2(q), of dimension 7 and trace dimension 4.
   The separated image is C^4. Its traced expectation takes the two diagonal
   entries in M_2 and tau_2 on H_2; E_12 is a nonzero collective observable
   killed by jE. Thus the construction neither erases the collective corner
   nor identifies a proper retraction with an isomorphism.

7. KLIFT-1 <1>1--<1>6:
   Constant normalized-basis coefficients give raw matrix lifts. The sign
   construction for h=2a-1 uses a uniform local spectral gap and produces a
   continuous projection with the prescribed endpoint. Finite families share
   a common smaller interval. Compression proves fullness on Homs. Polar
   normalization of a rectangular lift gives a local isometry; the continuous
   complementary projection is zero locally because it is zero at the
   endpoint and every nonzero projection has norm one. Hence endpoint
   unitaries, including between different ambient matrix sizes, lift locally.

8. KLIFT-2 <1>7--<1>12:
   Square-root lifting followed by trace normalization handles arbitrary
   states, including rank-deficient ones. Simultaneous S^(-1/2)
   normalization lifts every finite POVM and every specified finite Kraus
   instrument, including zero branches. Cross-object cyclicity gives exactly
   T_o(rho)=(d_Y/d_X) sum_i K_(o,i)rho K_(o,i)^*. With the uniform classical
   trace the full output block is |O|T_o; both factors are necessary. The
   ratio becomes P_alpha/P_beta for parabolic corners and is unchanged after
   tensoring a retained right context.

9. KOP-1 <1>13--<1>14, conditional on W:
   Preparations, discards, POVMs, Kraus instruments, assembly E and split j
   have the stated typed UCP realizations. W supplies exactly the classical
   maps needed to type multi-outcome sequential and parallel relations. The
   quotient is by sound typed relations, so realization and evaluation descend.
   Continuous scalar-unitary mixing is required as section data; pointwise
   Gram equality is not silently promoted to germ equality.

10. KOP-1 <1>15--<1>16:
    A finite endpoint circuit, after choosing its finitely many object lifts,
    can use locally lifted unitaries as explicit connectors between a tensor
    of chosen lifts and the independently chosen lift of its tensor object.
    Conjugating assembly, split and retained lists by those connectors
    preserves normalization and endpoint evaluation. This lifts a chosen
    circuit representative. The proof explicitly does not lift arbitrary
    extra diagram equations, choose a functorial section, or identify
    pointwise-equal CP shadows.

11. KOP-1 <1>17--<1>19:
    Local corner bases and their trace Grams give continuous density duals for
    every generator, including E and j. Finite circuit trees therefore have
    continuous positive branch densities and continuous Born weights. A
    conditioning denominator with D(1)>0 stays bounded away from zero locally.
    The conclusion is limited to finite specified trees and does not infer a
    value for zero-probability endpoint conditioning.
```

The functional-calculus and UCP arguments are uniform proofs, not conclusions
drawn from the finite samples. Umegaki 1954, pp. 177--179, supports the finite
tracial expectation characterization, and Stinespring 1955, Theorem 1,
supports the dilation used in the uniqueness proof; complete positivity and
section continuity are rederived in KCOM-3.

## Independent non-parabolic and mixed-degree recomputation

In spectral coordinates for `H_2(q)`, let `e_+,e_-` be the trivial and sign
projections, with trace weights `1/(q+1),q/(q+1)`. In `M_2(H_2(q))` I used

`p=e_+ [[1/2,1/2],[1/2,1/2]] + e_- [[1,0],[0,0]]`.

This is a self-adjoint projection not coming from a rank-one parabolic corner,
and `(Tr_2 tensor tau_2)(p)=1` for every `q>0`. Put X equal to the direct sum
of the degree-zero unit and this degree-two object, and Y equal to the direct
sum of the degree-zero unit and `e_+` in degree two. Then

`d_X=2`, `d_Y=1+1/(q+1)`,

while the tensor contributions in degrees 0,2,4 are

`1`, `1+1/(q+1)`, `1/(q+1)`.

Their sum is `d_X d_Y`. At `q=1,3/2,2,3` the common values were respectively
`3,14/5,8/3,5/2`. The colliding degree-two full corner is `M_2(C) direct-sum C`
of dimension 5; its separated diagonal subalgebra has dimension 3. This
independently confirms both the same-degree off-diagonal Homs and the need for
a proper expectation. Mutating the `e_+` block by replacing its off-diagonal
`1/2` with `1/3` makes `p^2-p` nonzero, so projection validity is a reachable
condition rather than a fitted trace identity.

For the density ratio, a rectangular isometry from a trace-dimension-two
source to a trace-dimension-three target sends the normalized source density
to raw target trace `2/3`; multiplication by `d_Y/d_X=3/2` restores trace one.
This calculation is independent of K2's rank-one source example.

## Statement/proposal register check

All six proposed rows remain `SKETCH`, and D1261--D1266 remain lane proposals;
no root promotion is claimed. Their statements agree with the proof scopes:

* `F1-LIM-KAR`, `F1-LIM-KTRACE`, and `F1-LIM-KEXPECT` include full
  same-degree matrix corners, the balanced section tensor, normalized trace,
  injective assembly and continuous arbitrary-corner expectations.
* `F1-LIM-KLIFT` distinguishes fullness on already chosen interval objects,
  local essential surjectivity through germs, and the absence of fixed-large-
  interval essential surjectivity.
* `F1-LIM-KPROC` states the correct `d_Y/d_X` and `|O|` factors and does not
  replace continuous mixing data by fibrewise Gram equivalence.
* `F1-LIM-KOP` carries W in the claim itself and limits lifting to individual
  finite circuits rather than arbitrary endpoint diagrams.

No proposed row depends on a REFUTED claim. The core CLIM-1/2 normalization,
balanced-domain and germ facts were used only at the verified scope recorded
in `core-critic/VERDICT.md`; the prior operational CC1 was not treated as
resolved except under W. The six rows match the honest strength of nearby
SKETCH proposals. K1 is the only single-source integration correction needed.

## Checker and mutation reachability

`python3 theory/lanes/f1-limit/karoubi/check_karoubi.py` exited `0` with
K1--K6 counts `4,3,10,3,3,3`. Each advertised mutation ran independently,
continued through every other gate, and exited `1` only through its intended
gate:

| mutation | reached failure |
|---|---|
| `--red-grading` | K1, full same-total matrix corner dimension |
| `--red-density-ratio` | K2, normalization and rectangular trace duality |
| `--red-cutoff` | K3, spectral band and endpoint projection |
| `--red-normalization` | K4, Kraus completeness in the source corner |
| `--red-gram` | K5, traced expectation and trace preservation |
| `--red-classical` | K6, uniform classical trace factor |

The relevant repaired-wiring checker also passed: W1--W5 recorded
`8,9,3,3,14` exact probes. Its five red modes respectively reached only W1
sequential routing, W2 parallel routing, W3 classical trace, W4 instrument
backaction, and W5 history associativity. These samples establish mutation
reachability for the primitive formulas; they do not prove W for an
unspecified presentation.

K1's principal dimension comparison, K2's two trace calculations, K3's
projection/spectral equations, K4's normalization, K5's independently rotated
diagonal expectation, and K6's product-trace total are genuine data
comparisons. The auxiliary K1 pair-count identity is elementary bookkeeping,
but the gate as a whole is not a syntactic identity. All target mutations are
specific and every target gate is reachable.

PASS
