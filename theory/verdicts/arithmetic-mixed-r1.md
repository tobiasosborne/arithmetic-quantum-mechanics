# Mixed arithmetic charts and towers: hostile verdict

Date: 2026-09-09. **Same-family prover/critic, target-blind lane.**
Runtime: native inherited Codex, no model override or nested CLI.
Context limitation: a fresh thread was unavailable. This context contains
the prior unrelated Galois prover work and the public arithmetic-limits
brief, but no mixed prover reasoning. The critic read only the mixed
artifacts, public brief, single sources, checker and its frozen evidence.
The shared retained-isometry decoder is consequently not an entirely
unfamiliar construction. Its formulas were nevertheless recomputed here.
Root confirmed the full mixed package frozen before this verdict finalized.

**Decision: PASS, with one MINOR wording repair. No FATAL or MAJOR.**
The positive scope is all finite fields for MIX-GRAM, the stated
conditioned strata for MIX-CHART, and every finite length with each degree
invertible for MIX-TOWER. MIX-ALL remains a precise construction conjecture.
No singular-degree tower theorem or mixed multiplication limit is admitted.

## 1. MINOR — specify the Fourier factor at the regular endpoint

**(a) Location.** `mixed/CLAIMS-PROPOSED.md`, MIX-CHART row, the string
`while actual induced Fourier extends to Z` (line 9). Compare
`mixed/gram-and-chart.md`, section 2, `<1>2.<2>2--<2>4`, and section 5,
`<1>2.<2>3`; `mixed/labbook-draft.tex`, tangent proposition, line 234,
already uses the more precise phrase `Actual chart Fourier`.

**(b) Independent computation.** On the regular joint support the actual
operator is `f_c tensor B_i`, where `B_i=(D_n^K)^(-1)F_K` remains present
when c tends to one. Its endpoint is `Z tensor B_i`, rather than
`Z tensor I`. For K=F3,n=2, `B_i|0>=|+>`, so the endpoint sends
`|0> tensor |0>` to `|0> tensor |+>`, not to itself. The three-dimensional
logical factor has not disappeared. The matrix-algebra action on the
chart subalgebra is correctly Ad_Z, and this correctly anticommutes with
the encoded tangent `X tensor I`. The full regular Fourier formula in
the proof and the all-length logical factor in MIX-TOWER are correct;
the isolated claim-row phrase is unnecessarily ambiguous.

**(c) FIX DEMAND.** Replace that phrase by `the chart Fourier factor extends
to Z; with the regular logical factor retained, the full operator extends
to Z tensor B_i`, or an exactly equivalent explicit formulation.

**(d) SURVIVING STATEMENT.** The stated faithful M2 endpoint, actual chart
Fourier conjugation, logical Fourier factor, anticommuting tangent,
continuous CP instruments and all tower formulas survive unchanged.

## Independently VERIFIED CORRECT — preserve this region during repair

The following is a protected list of recomputed assertions, not a request
to rewrite already correct arguments.

1. **Gram and intersection in all degree strata.** At a subfield label
   i(x), trace is nx. The Gram is therefore c times the inverse degree
   permutation when n is nonzero in K, and c times the all-ones column
   at zero when n vanishes. The latter has one squared singular value
   q/kappa=q^(2-n). The isometry intersection corresponds to singular
   value one, which occurs precisely at p=2,n=2. These arguments use
   no restriction to prime base fields or bounded degree.
2. **Projection algebras and physical traces.** On a nonzero angle block,
   products p q (1-p) and its adjoint extract both off-diagonal units.
   In the rank-one Gram case, P Ptilde P/d² isolates the angle rank-one
   projection; its companion and their span isolate the angle plane.
   Subtraction separates the two orthogonal residual scalar sectors.
   In the exceptional case P Ptilde is the common line and all remaining
   projection blocks commute. This independently gives M2⊗I_q, or
   M2⊕C⊕C, or C⊕C⊕C on the joint support, with exactly the listed
   dimension/Q weights and one scalar complementary summand.
3. **Actual Fourier, including odd residual parity.** The negative
   character sum gives F²=R; it does not give I in odd characteristic.
   Combining FJ=VF_K with F² gives FV=JF_K. The regular frame then has
   columns L B and (hJ-cW)B, where B=D_n^-1 F_K. On the singular residual
   space, the second-column image is J R_K, yielding the claimed block
   `[[0,R_K|A],[I_A,0]]`. The independent F3->F27 computation detects
   this reflection. In characteristic two it reduces to X⊗I_A.
4. **Frobenius and its actual support period.** Both J and V intertwine
   Frobenius; prime-field scalar n commutes with it. The zero and uniform
   vectors are fixed and Fourier preserves their relevant complements.
   This gives the two logical copies, with one common invariant line
   removed in the exceptional case, and U_E^s=I on the joint support.
   There is no inference that this is all of the ambient invariant space.
5. **Conditioned positive chart.** Direct matrix multiplication gives
   d²=f²=I, fp f=q, fd=-df and q-p=h d. At one the tangent is X,
   the chart Fourier is Z, and p plus X generate M2. Trace Tr/2 is
   faithful by the entrywise Hilbert--Schmidt norm. The unconditioned
   regular complement really has weight 1-2/kappa, negative at 3/2;
   its rejection does not invalidate the stated prior conditioning.
   The characteristic-two quadratic residual factor correctly uses
   Fourier to enlarge the commuting projection algebra.
6. **All-length corrected transfers and refinement.** Prime-field
   dilation commutes with both J and V; thus corrected L maps multiply
   to V_composite D_product-degree in every permitted named tower.
   Every path isometry has its empty column equal to the composite J
   and its tensor-v column equal to the composite L. Subtracting the
   two columns gives the connector. A consecutive-block refinement
   preserves these two independent vectors; this proves equality for
   arbitrary finite grouping and does not assume literal arithmetic
   equality of unrelated coordinate bases. Scalar propagation leaves
   exactly D_N^-1 F_(K0) as the logical Fourier, not a product of
   unrelated local Fourier operators.
7. **Endpoint and retained CP scope.** A k-excitation coefficient has
   order (t-1)^((k-1)/2), so only the singleton coefficients survive,
   with sqrt(a_r/A). The block identity sqrt(A_b/A)sqrt(a_r/A_b)
   verifies endpoint refinement directly. Tensor Z has sign minus
   on every retained singleton. The connector has rank two, so full
   path reference success is 2/2^l, and conditioning gives I_2/2.
   Standard retained Kraus completeness proves positivity on arbitrary
   ancillas and entangled inputs. Full sequential histories are correctly
   distinguished from the binary composite decoder; only success is
   identified. Higher path excitations are retained in independent tensor.

## Independent finite computations

`independent_probes.py` imports neither target implementation nor repository
checker. Its field trace is the trace of the multiplication matrix on a
found K-basis, independently of the verifier's Frobenius-sum trace. Fourier
coefficients use exact cyclotomic arithmetic, including fifth roots.
The first run with `--red` corrupted a trace datum and exited one at
`independent multiplication-trace Gram`; the next unmodified run exited zero.
Frozen evidence: `probe-red.log` and `probe-results.json`.

| Field embedding | Named twist | Nonzero Gram square | Joint dimension |
|---|---:|---:|---:|
| F2->F4 | 0 | 1 | 3 |
| F2->F8 | 0 | 1/4, multiplicity 2 | 4 |
| F3->F9 | 0 | 1/3, multiplicity 3 | 6 |
| F3->F27 | 0 | 1/3, multiplicity 1 | 6 |
| F4->F16 | 0 and Frobenius twist 1 | 1 | 7 |
| F5->F25 | 0 | 1/5, multiplicity 5 | 10 |

The same independent field matrices verify both Fourier-transfer identities,
regular Gram frames and their full logical Fourier, singular residual
reflection, and Frobenius transfer equivariance. Independent exact rational
path tensors of lengths 1,2,3,4,5 verify both connector-Fourier columns and
every binary consecutive split. These are finite falsifiers; the universal
statements rest on the symbolic derivations reviewed above.

## Checker audit, symbolic simplification and mutation reachability

The frozen lane checker SHA256 is recorded in `checker-audit-results.json`.
Its `--matrix` run passed. More decisively, `checker_audit.py` launched all
22 named red modes as separate actual CLI processes: each exited one at
the mathematical gate below. An ordinary green CLI exited zero with
G1=231, G2=6960, G3=3, F1=61, F2=1212, F3=22, R1=3, R2=131,
R3=16 and M1=5 accepted assertions. No aggregate gate lacks a reachable red.

| Red data mutation | Killing gate | Mathematical exit path |
|---|---|---|
| coset-label | G1 | S3 regular/coset equivariance |
| omit-normalization | G1 | pullback squared norm |
| cyclic-only-image | G1 | normal core and image |
| omit-tensor-outcome | G2 | four typed outcomes |
| erase-orbit-coherence | G2 | cross-orbit Born coherence |
| merge-tower-histories | G2 | merged failures lose cross terms |
| admit-nonuniform | G3 | nonuniform normalized pullbacks fail composition |
| trace-fibre-label | F1 | actual F2->F4 trace-fibre Gram |
| wrong-gram-branch | F1 | squared singular spectrum |
| omit-degree-scaling | F2 | logical D_n correction |
| fourier-sign | F2 | F_E J = V F_K |
| fourier-scaling | F2 | F_E V = J F_K |
| wrong-failure-projector | F2 | retained failure amplitude |
| residual-fourier-reflection | F2 | residual logical reflection |
| physical-support-rank | R1 | negative unconditioned complement |
| compress-mixed-transition | M1 | intermediate compression changes return |
| omit-tangent-normalization | R2 | tangent/Fourier involutions |
| collapse-tangent-algebra | R2 | tangent/Fourier involutions |
| tangent-fourier | R2 | induced Fourier swaps projections |
| incomplete-tangent-instrument | R2 | instrument completeness |
| tower-degree-scaling | F3 | actual corrected-transfer composition |
| tower-connector-coefficient | R3 | squared coefficient normalization |

The two tangent modes killed at the involution check change different
matrices: h*d versus diag(d). They share an early norm failure and are
not evidence that the later span gate was reached. The normal-form proof
of M2 is instead supplied by the independent anticommuting-involution
calculation; no separate theorem is inferred from a late checker label.

Symbolic inspection found no aggregate acceptance test reduced to a
comparison of an expression with itself. One sample-specific degeneracy
must be stated: at c=1 the scaled relation `h D=Q-P` is `0=0`, so that
assertion alone supplies no endpoint evidence. The separate endpoint test
checks D=X and f=Z explicitly, and the involution/anticommutation tests
remain active. The Gram comparison uses independently built field fibres
against the degree permutation; the algebra dimension closes actual
ambient rational P,Q matrices under products; support is computed from
independent columns. The connector normalization simplifies to the
nontrivial multilinear identity
`sum_(nonempty S) product_(r in S)(kappa_r-1)=product_r kappa_r-1`.
Its associativity test uses separately expanded binary refinements.
Endpoint expectations are compared with polynomial coefficients, not
fitted to them. Squared connector coefficients alone cannot certify signs;
the exact Fourier test also checks unsquared amplitudes, as the critic's
sign mutation below confirms. Matrix-unit traces test stated Kraus maps;
their complete positivity is a written amplification argument, not a
conclusion drawn from trace preservation.

Four additional critic mutations were made only on temporary checker
copies under this lane; all copies were removed after their runs:

| Critic data change | Preserved earlier checks | Mathematical exit |
|---|---|---|
| Swap two F27 trace labels outside the embedded F3, preserving fibre counts | F1 Gram, ranks and projection algebra | F2, F_E J = V F_K |
| Change only the tower's logical dilation from degree 4 to 2 | Corrected transfers and all orthogonal paths | F3, actual F81 Fourier path equation |
| Reverse the sign of the connector's second unnormalized column | Connector norm and orthogonality | R3, tensor Fourier intertwining |
| Cyclically permute endpoint singleton weights | Endpoint norm | R3, actual polynomial coefficient limit |

These kill paths rule out merely dying at an unrelated first gate.
`checker-audit-results.json` records exact CLI exits, diagnostics and counts.
No target checker or target data file was modified.

## Quantifier, canonicity, reliance and lockstep audit

- **Quantifiers.** The Gram proof covers all p, every q=p^s, every n>=2
  and every named finite-field embedding. It explicitly keeps p|n and
  p=2,n=2. The positive tower theorem explicitly requires p∤n_r on
  every edge and has no bound on finite length. The positive weights
  are arbitrary named positive reals. No extrapolation from the field
  samples or rational angle samples is used in those proofs.
- **Canonicity.** The source retains fields, named embeddings, common p
  and primitive root, positive square roots, and outer-to-inner factor
  order. The regular frame is specified by Gram subtraction; the singular
  plane by J|+> and V|0>; the residual coordinates use the named Fourier.
  Endpoint weights and their continuation are explicitly chosen. There
  is no unnamed basis, phase, primitive root or universal singular-frame
  comparison hidden in the positive theorem. The process claim supplies
  concrete typed Kraus maps rather than an unspecified canonical category.
- **Reliance.** The arithmetic inputs FRB-TRACE, FRB-TRANSFER and FRB-FROB
  are PROVED in the registry. The local derivations use their admitted
  definitions and explicit finite sums, matrix products and scalar Taylor
  expansion. No REFUTED claim or deprecated snapshot is an input. MIX-ALL
  keeps the separately admitted Galois fragment distinct from cardinality
  registers and does not assert an unsupplied comparison of those spaces.
- **Conjecture scope.** MIX-ALL explicitly demands a common positive
  moment rule, actual objects/arrows, reference weights and comparison
  maps, singular-degree refinements and mixed arithmetic relations.
  It distinguishes measured circuits from unmeasured ones. M1 is called
  a necessary finite-fibre diagnostic, not a verification of existence.
  Those are coherent remaining requirements; they are not proved here.
- **Status register.** Definitions, both proof headers, three positive
  claim rows, labbook propositions and SUMMARY all remain SKETCH.
  MIX-ALL is CONJECTURE throughout. No new claim has been represented
  as an already admitted theorem. The only wording mismatch requiring
  repair is objection 1's endpoint Fourier-factor phrase.
- **Labbook and shard lockstep.** The two shards have 332 and 337 lines.
  The complete final labbook draft has full new definitions, descriptive
  statements, scope and provenance blocks. It independently compiles
  with the actual shared preamble to seven pages, pdflatex exit zero.
  No overfull boxes were reported. Ordinary first-pass label and inherited
  font-shape warnings are not mathematical failures. Final file hashes
  and build evidence are in `artifact-audit.json`. Full trunk integration
  and its lockstep gate remain root responsibilities.

PASS
