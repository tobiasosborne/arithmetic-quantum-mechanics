# String-anchored integration proposal

The lane made no root-file edits.  Apply only after adjudicating the claim
statuses.  Definition and claim text should be copied from the named proposal
files so one source of wording is reviewed.

## 1. Definitions

Target: `definitions.md`.

Anchor:

`## D1144 (apartment comparison of arithmetic and q=1 context algebras)`

Insert after the complete D1144 block, or after the last definition added by
the other `f1-limit` lanes, all definitions D1241--D1259 from
`DEFINITIONS-PROPOSED.md`.  Preserve the numbers: the user reserved this range
for the vector/polarization bridge.

Admission-sensitive points that must survive consolidation:

* D1242 ranges over `0<=i<=n`; `C_0^Z=I tensor |0><0|` is essential in rank
  one.
* D1246's proved positive domain is `q>1`, with semidefinite boundary `q=1`;
  no claim is made for `0<q<1`.
* D1248 distinguishes algebraic specialization from the GNS quotient.
* D1249 requires coefficient-continuous density sections positive and normalized
  on a real one-sided neighborhood; arithmetic-only positivity is insufficient.
* D1257–D1258 define the regular circuit/germ category and actual quotient
  functor under the repaired core classical-wiring hypothesis W. Singular
  densities remain outside its regular preparation labels.
* D1253 types `pap` with corner unit `p` and includes the factor `r^(-1)` in
  preparation.
* D1255 contains no generic type-C Hecke lift.

## 2. Notation

Target: `notation.md`.

Anchor:

`| J_ap, Omega_Q | coordinate-apartment isometry and its UCP context comparison | D1144 |`

Insert the following rows after the current operational-F1 notation block:

`| Aff(L), Y_L, R_X(L), T_(w,A) | affine group, flag-vector set, mirabolic commutant and orbital basis | D1241,D1245 |`

`| C_i^X, C_i^Z, D_L, F_(L,psi), W_(L,psi), R_Z(L^vee) | controlled constraints, dual-flag reversal, Fourier unitary and dual mirabolic algebra | D1242--D1244 |`

`| prec_w, down_w(A), k_(w,A), tau_q, i_q, E_q, N_(tau_1) | orbit poset, valency, reference trace, Hecke retraction and endpoint radical | D1245--D1249 |`

`| A_C(V), Sh(m,n), J_(V,W), p_(V,W), D_(V,W), r_(V,W), Phi_(V,W), Psi_(V,W) | type-C decomposable composition arena and trace-adjoint channels | D1250--D1255 |`

`| p^aff_(L,M), PMir_(k,psi), RegOp_J, RegOp_(1+), Pi_n, Q_X, Ev_(1+) | affine decomposable projection, phase-polarized bridge groupoid and regular boundary category/maps | D1244,D1256--D1259 |`

## 3. Claims DAG

Target: `claims/CLAIMS.md`.

Anchor:

`## Operational F1 subsystem increment — 2026-09-07`

Append a subsection titled
`## Vector/polarization operational limit — 2026-09-07` after the existing
operational rows.  Copy the thirteen rows from `CLAIMS-PROPOSED.md` with statuses
set by the capped review.  Before review, every row remains `SKETCH`.

Suggested dependency order is:

`F1-MIR-AFF -> F1-MIR-GEN -> F1-MIR-FOURIER`,

`F1-MIR-AFF -> F1-MIR-VAL -> F1-MIR-POS -> F1-MIR-EXPECT -> F1-MIR-END -> F1-MIR-REG`,

`F1-TC-DEC -> F1-TC-CP -> F1-TC-COH`, with `F1-TC-ONE` depending on
`F1-TC-DEC`, and `F1-MIR-DEC` depending on `F1-MIR-AFF`.

## 4. Theory shards

Copy admitted proof shards to an owning root theory location without changing
their statements:

* `vector-mirabolic.md`;
* `reference-trace.md`;
* `type-c-correspondence.md`;
* `operational-boundary.md`.

Each is between 200 and 500 lines and uses Lamport numbering.  If filenames
change, update the `proved in` cells in the claim rows.

## 5. Checker and expectations

The orchestrator's O3 repair supplies these root executables; this bridge
repair does not edit either checker:

* `theory/checks/f1_limit_mirabolic_check.py`: B1, B2, B4, B7, with named
  kernel, line, expectation and affine-decomposable data mutations;
* `theory/checks/f1_limit_bridge_check.py`: B3, B5, B6, including the actual
  dual-reversal, Fourier-square and relative-position checks;
* `theory/checks/f1_limit_check.py`: the existing L10/L12 exact falsifiers.

Use the actual paths in `CLAIMS-PROPOSED.md`. The rank-two interpolation
supporting B4 is proved in `reference-trace.md` §6. The orchestrator records
all green/red exit paths and aligns the original checker specification as
part of O3; this repair makes no new checker-execution claim.

## 6. Labbook lockstep

Target: the section owning the operational F1 limit, selected by the
orchestrator after the other lanes land.

Anchor phrase in the current text:

`The partial-flag category and its coupling to Weyl quantum mechanics`

Add a self-contained subsection with these displayed results:

1. `R_X(L)=End_(GL(L) semidirect L) C[Fl(L) times L]` and its equation-(6)
   kernel composition.
2. `e=(T_0+I)/Q=C_1^X` and the exact Fourier formulas, with indices
   `0<=i<=n`.
3. The antichain valency and trace Gram formula; positive range `q>1`.
4. `R_n(1)/N_(tau_1)=H_n(1)` together with the rank-one singular density,
   explicitly distinguishing the algebraic and GNS endpoints.
5. The type-C product-shuffle corner and the trace-adjoint UCP maps.
6. The nonparabolic block obstruction and exact group-algebra endpoint.
7. The regular one-sided operational category, its quotient evaluation, and
   finite Born limits, with positivity required for every nearby real q>1.
   State only vector-Fourier tensor preservation; retain the full bridge
   through its reversed-shuffle decomposable correspondence.

State q-rook compatibility, generic type-C tensor assembly and the full Weyl
matrix algebra only as excluded stronger claims.  Rebuild the PDF in the same
commit as any definition or claim admission, per L11.

## 7. Sources

The root ledger already contains the title-verified Rosso entry under anchor
`**1310.3878** — Daniele Rosso, *The mirabolic Hecke algebra*.`

No further ledger mutation is required unless a new source is introduced.
Use `SOURCES.md` for exact locators in proof and labbook citations.
