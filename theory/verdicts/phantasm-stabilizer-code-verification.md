# Frozen SP-STAB-REL checker verification

Date: 2026-09-10. Model: `gpt-5.6-sol`, reasoning `xhigh`.

This is mechanical verification of the frozen quantum checker and its
pre-registration only. The attempted mathematical critic pass in this
directory is invalidated as recorded in `INVALIDATED.md`; nothing here is a
proof verdict or promotion argument.

## Artifact and dependency identity

| artifact | observed SHA-256 |
|---|---|
| frozen quantum checker | `c9ddc1a9a287437f26ee6c179f8f40fe63d0797893114fe6d98d75dc11bfec43` |
| quantum `EXPECTATIONS.md` | `d6ec7e433f5b9cc7635b84213f89cd41574c3ce635d0cf2e1c84917630fb173e` |
| imported `theory/checks/wh_kappa_check.py` | `4cad037cd7d82e8101af72def4a4abf748f671f68fda93806b24a74ed83892fa` |
| imported installed classical checker | `bdfa9952f1b0ea496a8eb07e6c72794d173cf7aa5cd795038d6e3b800ee6cfe2` |
| classical lane checker | `bdfa9952f1b0ea496a8eb07e6c72794d173cf7aa5cd795038d6e3b800ee6cfe2` |

The frozen quantum hash matches the value supplied by root. Its behavior is
not determined by that hash alone: imports resolve first from
`theory/checks/`, then from the classical checker lane. The two classical
copies were byte-identical during this verification. A frozen record should
retain the dependency hashes above, or vendor/freeze the imported API.

## Green and advertised-red result

The help text exposes exactly thirteen named mutations and no bare `--red`.
Green exited `0` with S1--S5 passing. Every named mutation exited `1` at its
declared target gate:

| gate | modes |
|---|---|
| S1 | `weyl-sign`, `fourier-sign`, `drop-shear` |
| S2 | `phase-only`, `zero-collapse` |
| S3 | `average-sign`, `origin-dependent`, `fixed-seed`, `empty-nonzero` |
| S4 | `product-order`, `dagger-transpose` |
| S5 | `tensor-order`, `cup-singleton` |

The exact outputs and timings are in `RUNS.md`.

## Exact-code audit by gate

### S1

S1 constructs Weyl matrices directly in cyclotomic integers and compares
their products with the separately computed symplectic exponent and label.
Fourier conjugation uses dense exact multiplication and the integer factor
`p`; shear uses the fixed quadratic diagonal. The generated Clifford closure
and state orbits are independent of the relation catalog. The three mutations
have distinct exit paths: Weyl multiplication, Fourier covariance, and the
216-class qutrit census.

Reachability limit: both sign mutations fail in the first F3 case, so no red
mode reaches their corresponding F5 comparisons; no mutation targets the F5
30-ray orbit. The green F5 checks remain exact but lack a late-path mutation.

### S2

The general projective comparison is substantive: it treats zero separately
and uses all cyclotomic-entry cross-products after locating a nonzero anchor.
It does not divide in the coefficient ring. `phase-only` and `zero-collapse`
fail at distinct assertions. The independently generated qutrit family census
and full-rank/rank-one disjointness have no late-path mutation, but are not
textually self-comparisons.

### S3

The group average and the D1715 equation checker are independent
implementations: the former uses monomial Weyl actions on projector columns,
while the latter uses dense Weyl matrices and all origins/directions. The
unnormalized identities `P^2=|L|P` and `trace(P)=|L|`, projective collision
counts, independently generated amplitude families, graph/Clifford split, and
F5 state orbit are substantive.

Acceptance reachability is weak. All four S3 mutations are applied only in
the opening preflight and are not propagated into the 389-relation/F5 bulk:

- `average-sign` and `fixed-seed` are bit-identical in observed effect, both
  failing `translated computational state failed D1715 equations/nonzero
  line` at the first S3 assertion;
- `origin-dependent` fails the small three-origin comparison;
- `empty-nonzero` fails the small empty-scalar comparison.

No advertised mutation reaches the exhaustive all-origin equations,
projector square/trace, projective bijection, generated-family equality, graph
split or F5 checks. An independent copy changing only the projector-trace
ground truth reached and failed the S3 trace assertion. A second copy disabling
the fixed-seed preflight made `--red-fixed-seed` survive the entire target gate
and exit `0`, exactly demonstrating that the mutation has no independent bulk
backstop.

Recommended mechanical repair: add late-path mutations for projector trace or
rank, one all-origin bulk relation, the actual-family bijection and the F5
orbit; propagate at least one averaging/seed mutation into the catalog loop.
Keep distinct modes for the average sign and zero-column seed so they fail at
different named acceptance checks.

### S4

The exhaustive loop compares a relation-composite image with an actual matrix
product, so it is not tautological. Dagger compares a separately reconstructed
relation image with cyclotomic conjugate transpose. The two named mutations
fail at distinct graph/complex-state preflights and are not propagated into
the 140,101-composition or 389-dagger loops.

An independent copy reversing product order only for square `1->1->1` cases
passed S1--S3 and failed inside the exhaustive S4 loop at
`functoriality failed in typed composition 1->1->1`. This proves that the bulk
acceptance path is live. A first unrestricted reversal was intentionally
discarded as an invalid mutation because rectangular products became
ill-typed and produced exit `2` rather than a gate failure.

Recommended mechanical repair: add a same-typed bulk product-order mutation
and a bulk conjugation mutation which pass the preflights and fail within the
exhaustive loops.

### S5

The tensor comparison reconstructs the direct-sum relation image and compares
it with an independently formed Kronecker product. The Bell comparison obtains
one side by vectorizing the independently reconstructed identity-relation
operator. The retained closed scalar is computed by exact Bell cap/cup matrix
multiplication.

`tensor-order` fails at the first graph pair and does not reach the exhaustive
state/effect or selected mixed tensors. `cup-singleton` passes all tensor cases
and fails at Bell vectorization, so those two modes are distinct. No mutation
targets the final retained scalar `p` assertion.

The preliminary check `cup(plane).pts == identity(plane).pts` is definitional:
the imported `cup` and `identity` functions both construct the same `x+x`
point set and the comparison discards their different types. It should not be
counted as independent evidence; the following vectorization/Bell equality is
the substantive cup check.

Recommended mechanical repair: add a tensor mutation that reaches the bulk
state/effect loop and a closed-scalar mutation that reaches the final exact
value. Retain the current Bell/vectorization comparison.

## Duplicate and tautological comparison register

- No whole S1--S4 gate simplifies to a same-function comparison.
- S5's point-set-only `cup == named identity` check is definitional as noted
  above; its independent vectorization check prevents the gate from being a
  no-op.
- The most material issue is mutation placement rather than green
  tautology: S3's large acceptance block, S4's exhaustive blocks, and S5's
  tensor bulk/final scalar are reached by no advertised mutation.

## Independent copy mutations

All temporary copies lived under `/tmp`; no checker or trunk file changed.

1. Expected qutrit Clifford count changed `216 -> 215`: S1 exited `1` at its
   census.
2. Expected unnormalized projector trace changed `|L| -> |L|+1`: S1/S2 passed,
   then S3 exited `1` at the projector-trace assertion in Hom `(0,0)`.
3. Exhaustive S4 product order reversed only for square `1->1->1` cases:
   S1--S3 passed, then S4 exited `1` inside the bulk composition loop.
4. The first fixed-seed preflight assertion was disabled and the actual
   `--red-fixed-seed` mutation retained: S3 completed and the process printed
   `RED SURVIVED ...` with exit `0`.

These checks support only code reachability conclusions. They do not establish
the arbitrary-prime theorem, D1704 membership, fullness, or any proof claim.
