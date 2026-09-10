# SP-WEYL corollary draft — blind hostile verdict

- **Target:** `theory/symplectic-phantasm/reuse.md`, sections 1–2, against
  D1701/D1703, the canonical `SP-WEYL` row, the `SP-WEYL` DAG contract, and
  admitted F1-DUAL/F1-WEYL/F1-REAL.
- **Critic model:** `gpt-5.6-sol`, reasoning `xhigh`.
- **Blindness and family limitation:** this was a blind lane. I read no prover
  lane, prover summary, or root-chat reasoning. The campaign has no available
  cross-family prover/critic split. The pre-existing reuse draft does not
  record its author's model, so an exact target-author family match cannot be
  verified; this verdict must not be described as cross-family review.
- **Prior verdicts on this target:** none found. The F1 adjudication was read
  only to fix the inherited PROVED scope, not to reopen that proof.
- **Decision:** **PASS with two MINOR repairs and one NOTE.** I found no FATAL
  or MAJOR objection to the SP-WEYL statement. The coordinate reduction,
  character-dual sign, half-form rephasing, raw-center quotient, trace, unit,
  and unitary irreducible scope survive independent recomputation.

## Numbered objections

### OBJ-1 — MINOR — the fixed-central-character representation sentence omits the unitary qualifier

**(a) Exact location.** `claims/CLAIMS.md`, canonical `SP-WEYL` row, the
sentence “fixed-central-character irreducibles are unique up to unitary
equivalence”; its labbook restatement in
`labbook/sections/symplectic_phantasm_contracts.tex`, proposition `SP-WEYL`;
and `theory/symplectic-phantasm/reuse.md` §2 `<1>4.<2>3`–`<2>4`.

**(b) Independent computation.** Let

    G_V = k x V,
    (t,v)(t',w) = (t+t'+omega(v,w)/2,v+w).

After a chosen symplectic coordinate map, the homomorphism

    Phi(t,a,b) = (psi(t+a.b/2),a,chi_b),
    chi_b(x)=psi(-b.x),

is onto `H_p(A)` and has kernel
`{(t,0,0):psi(t)=1}`. A representation of `G_V` with central action
`rho(t,0)=psi(t)I` therefore factors through `H_p(A)`, and conversely. F1-REAL
gives algebraic uniqueness of irreducibles and, **when both models carry the
stipulated unitary structures**, polar decomposition gives a unitary
intertwiner unique up to `U(1)`. Without saying “unitary representation” in
the first sentence, “unitary equivalence” has no specified Hilbert structures.
The next sentence uses the correct phrase “irreducible unitary models,” so
this is a closure/wording defect rather than a mathematical counterexample.

**FIX DEMAND.** Replace “fixed-central-character irreducibles” by
“fixed-central-character irreducible unitary representations of the raw
group (equivalently, of its `H_p(A)` quotient).”

**SURVIVING WEAKER STATEMENT.** In the category of unitary representations
with raw central character `psi` (equivalently quotient central character
`iota`), the irreducible is unique up to unitary equivalence, has dimension
`q^n`, and its unitary intertwiners form a `U(1)`-torsor.

### OBJ-2 — MINOR — two advertised R4 subchecks are constructed identities rather than independent acceptance tests

**(a) Exact location.** `theory/checks/phantasm_reuse_check.py`, function
`finite_model`, the R4 statements `len(family) == dim**2` and
`Fraction(dim, denominator) == 1`; compare
`claims/PHANTASM-DAG.md`, `SP-WEYL` **Required mutations**, “wrong trace
normalization and missing vacuum.”

**(b) Independent computation.** In green mode, `m.ops` receives one entry for
every pair in `A x A`, so `len(list(m.ops.values()))=|A|^2=dim^2` by loop
construction before R4 examines an operator. The vacuum mutation kills the
test only by replacing that constructed list with `[]` at rank zero. Likewise
green mode sets `denominator=dim`, so the normalization assertion simplifies
symbolically to

    Fraction(dim,dim) == 1.

The trace-normalization mutation kills it only by changing the right-hand
denominator to `dim^2`. Neither subcheck independently evaluates the matrix
trace of the `(0,0)` operator and compares it with the coefficient trace.
The adjacent exact Gram test is substantive: it computes Hilbert–Schmidt
inner products from the monomial matrices and detects all distinct labels.
The proof's trace calculation is also correct, so this does not undermine the
theorem; it means the two named R4 red paths overstate their independent
checker evidence.

**FIX DEMAND.** Make R4 derive the actual `(0,0)` operator, verify it is the
identity including at rank zero, evaluate its matrix trace from its entries,
and compare `q^{-n}Tr` with the coefficient functional; make the red modes
mutate that operator/expected data rather than a preselected denominator or
list.

**SURVIVING WEAKER STATEMENT.** R4's exact operator Gram computation remains
a meaningful finite test of orthogonality and independence, while the proof
in §2 `<1>3.<2>3`–`<2>4` independently establishes the normalized faithful
trace for every rank.

### OBJ-3 — NOTE — the executable gates do not bind the proof text itself

**(a) Exact location.** `theory/symplectic-phantasm/reuse.md` §1
`<1>4.<2>1` and §2 `<1>1.<2>2`; `theory/checks/phantasm_reuse_check.py` R1–R3;
and `theory/checks/phantasm_contract_check.py` G6–G7.

**(b) Independent computation.** On separate temporary repository copies I
changed only the target proof to (i) `chi_b(x)=psi(b.x)` and (ii)
`W^s(v)=c(v)^(-1)W_ref(v)`. Both the reuse checker and contract checker still
exited zero, because neither parses the proof body. Changing D1703's
wavefunction sign instead made the contract checker exit at G6, while the
reuse checker stayed green. Changing the independently imported Abelian
operator on another checker copy from `chi(y+a)` to `chi(y)` made the reuse
checker exit at R2. Thus the implementation comparison is real, but proof-text
correctness is supplied only by hostile review. This matches the checkers'
express disclaimer that passing does not prove the mathematics.

**FIX DEMAND.** In adjudication, continue to treat this hostile recomputation
as the proof-text gate and describe R1–R4 only as implementation-level finite
interface evidence.

**SURVIVING WEAKER STATEMENT.** The checkers meaningfully test their hard-coded
finite interfaces and the contract data they actually read; they do not
validate the Lamport proof text.

## Independent recomputation

1. **Symplectic coordinates.** For `e != 0`, choose `f` with
   `omega(e,f)=1`. With

       v_perp = v-omega(v,f)e+omega(v,e)f,

   alternation gives `omega(v_perp,e)=omega(v,e)-omega(v,e)=0` and
   `omega(v_perp,f)=omega(v,f)-omega(v,f)=0`. Pairing `ae+bf` with `e,f`
   gives `-b,a`, so the plane is nondegenerate and meets its perpendicular
   trivially. Induction gives an ordered symplectic basis and a chosen map
   `k^n+k^n -> V` with form `a.b'-a'.b`. No preferred basis is produced.

2. **Character dual and its sign.** A nontrivial additive `psi:k->U(1)` has
   image of order `p`, since every image element has `p`-th power one. If
   `b != 0`, the map `x |-> b.x` is onto `k`; hence
   `chi_b(x)=psi(-b.x)` is nontrivial. The map `b |-> chi_b` is injective and
   therefore bijective because F1-DUAL gives `|Hom((k^n,+),mu_p)|=q^n`.
   Under this identification the reference multiplier is
   `chi_b'(a)^(-1)=psi(a.b')` and its commutator is
   `psi(a.b'-a'.b)`.

3. **Half-form conversion.** For `c(a,b)=psi(a.b/2)`, direct expansion gives

       a.b' + a.b/2 + a'.b'/2 -(a+a').(b+b')/2
       = (a.b'-a'.b)/2.

   Therefore `W^s(v)=c(v)W_ref(v)` has multiplier
   `psi(omega(v,w)/2)`. Since the multiplier at `(v,-v)` is one and each
   reference operator is unitary, `W^s(v)^*=W^s(-v)`.

4. **Wavefunction sign.** Acting on a basis vector gives

       W^s(a,b)delta_y = psi(-b.y-a.b/2) delta_(y+a).

   Setting `x=y+a` yields
   `(W^s(a,b)f)(x)=psi(-b.x+a.b/2)f(x-a)`, exactly D1703. At `p=3`, with
   `psi(r)=zeta_3^r` and `1/2=2`, independent enumeration gave

       W^s(1,1): delta_0 -> zeta delta_1,
                   delta_1 -> delta_2,
                   delta_2 -> zeta^2 delta_0.

   All 81 products of the nine rank-one operators had multiplier
   `zeta_3^{2(ad-cb)}` for labels `(a,b),(c,d)`.

5. **Matrix and trace clauses.** Rephasing preserves the span and linear
   independence of the `q^(2n)` F1-REAL operators. Since
   `dim End(C[A])=(q^n)^2`, the representation is a bijective unital
   star-homomorphism. For a nonzero translation the matrix trace is zero; for
   `a=0,b!=0`, character orthogonality gives zero; and the zero label gives
   trace `q^n`. Hence `tau_V=q^{-n}Tr` on every basis element and therefore on
   the algebra. Matrix positivity and faithfulness transfer through the
   isomorphism.

6. **Raw center, including extension fields and rank zero.** The quotient map
   `Phi` displayed in OBJ-1 is a homomorphism because its image product has
   phase exponent

       t+t' + a.b/2 + a'.b'/2 + a.b',

   while applying `Phi` after the raw product gives the same exponent after
   expanding `(a+a').(b+b')/2`. It is onto, and its kernel is exactly
   `ker(psi) x {0} x {0}`, of size `q/p`; no faithfulness of `psi` over
   extension fields is assumed. At rank zero, `A=0`, the raw group is `(k,+)`,
   the quotient is `mu_p`, the model is `C`, and the same kernel statement
   holds.

7. **Characteristic audit.** Nothing in the dual or quotient argument assumes
   `k=F_p`; it works for every `q=p^f`. The half-form uses `2^{-1}` and is
   therefore correctly restricted to odd characteristic. At `p=2`, `2=0`, so
   no field element can satisfy `2h=1`; the target makes no characteristic-two
   claim and delegates that design to DG-CHAR2.

## Checker and mutation audit

### Reuse checker

Green exited `0` with the recorded counts:

| gate | exact comparisons | substantive acceptance condition |
|---|---:|---|
| R1 | 1002 | nontrivial character image, signed dual evaluation, and bijection |
| R2 | 942 | imported Abelian action versus direct wavefunction action and position labels |
| R3 | 69258 | independently composed monomial operators versus the half-symplectic multiplier; raw kernel/image checks |
| R4 | 68346 | exact operator Gram; see OBJ-2 for the constructed normalization/vacuum subchecks |
| R5 | 99 | whole-register operator versus explicit tensor of factor operators |
| R6 | 1380 | relative character and relative-Frobenius covariance over `F9` inside `F81` |

Every shipped bridge mutation exited `1` at its registered first gate:

| mutation | actual exit gate and first witness |
|---|---|
| `dual-sign` | R1, `q=3`, rank 1, `b=x=(1,)` |
| `trivial-character` | R1, character-image check at rank zero |
| `rephase` | R2, `q=3`, rank 1, `a=b=(1,)` |
| `position-labels` | R2, `q=3`, rank 1, `a=(1,), b=(0,)` |
| `cocycle` | R3, first nontrivial rank-one product over `F3` |
| `central-injective` | R3, `F9`: actual kernel size 3 versus expected 1 |
| `trace-normalization` | R4, constructed normalized-trace assertion (OBJ-2) |
| `vacuum` | R4, constructed family-size assertion at rank zero (OBJ-2) |
| `tensor-phase` | R5, ranks `0+1` |
| `character-conflation` | R6, relative-character comparison |
| `relative-frobenius` | R6, relative-Frobenius covariance comparison |

No top-level R1–R6 gate is unreachable. Symbolic inspection found that R2
shares the cochain helper on its two sides, so R3 supplies the independent
test of the half-form value; R3's surjectivity subcheck is redundant after
R1's character-image check. R4's Gram is nontrivial, while its other two
subchecks have the defect in OBJ-2. R5 and R6 form their compared sides by
different operations.

On temporary copies, the independent imported-ground-truth order mutation
exited `1` at R2. The three source-text mutations and their paths are recorded
in OBJ-3. No trunk file was changed for these probes.

### Contract checker

The contract run used repository checkpoint `853c564`, checker blob
`5c2c94ce442e2fbee44759597612b4340bf64990`. The reuse checker at that
checkpoint was blob `409f8e38fcf6e0395858a98bbd2922e9e9ad20d6`. A later uncommitted root
edit began after these runs to adjust future-promotion mutation plumbing; it
was not the contract-checker version reported below and did not change the
mathematical target or reuse checker.

Green exited `0`: G1 parsed 14 unique contracts; G2 resolved contracts,
definitions, dependencies and sources; G3 found a DAG with 14 lemmas and 7
decision gates; G4 found no refuted reliance or unsupported promotion; G5
verified 25 pinned local sources and 5 unused GAP leads; G6 matched 13
definitions and 14 claim restatements; G7 checked selected notation and sign
ownership; G8 checked inherited status/path and definition reuse.

All shipped contract mutations exited `1` at their registered gate:

| actual gate | mutations reaching it |
|---|---|
| G1 | `duplicate-node`, `empty-scope` |
| G2 | `missing-node`, `missing-definition`, `status`, `orphan-claim`, `decision-input` |
| G3 | `cycle`, `decision-cycle` |
| G4 | `refuted` (first seen from SP-EGOROV's dependency), `promote` (missing admitted review/evidence) |
| G5 | `source-hash`, `source-gap` |
| G6 | `labbook`, `definition-drift` |
| G7 | `notation-alias`, `notation-owner` |
| G8 | `inherited-status`, `untracked-reuse`, `definition-reuse`, `definition-cycle` |

The contract checker is a structural/lockstep gate, not a truth checker. Its
mutations are specific and all G1–G8 gates are reachable.

## Independently VERIFIED CORRECT — do not churn during repair

<!-- BEGIN VERIFIED CORRECT -->

1. Section 1's symplectic-plane split and induction prove the coordinate
   reduction in every finite dimension, including the unique zero-space map.
2. The negative signed dual `chi_b(x)=psi(-b.x)` is forced by D8/D1003 and
   produces the positive reference cocycle `psi(a.b')`.
3. The positive half-dot cochain produces exactly the D1703 multiplier
   `psi(omega/2)` and the stated star.
4. The D1703 wavefunction has the correct `x-a` shift and phase
   `-b.x+a.b/2`; the basis-vector and function formulas agree.
5. F1-REAL applies to the additive group `A=(k^n,+)` at level `p` for all
   finite fields `k`, not only prime fields or rank one.
6. The full matrix image, irreducibility, dimension, and unitary-intertwiner
   conclusions are used at exactly their admitted finite-abelian scope.
7. The coefficient trace equals normalized matrix trace and is unital,
   positive, faithful, and cyclic. OBJ-2 concerns only the redundant finite
   checker subassertions, not this derivation.
8. The raw `k`-center is correctly quotiented by `ker(psi)`; it is never
   falsely identified with the faithful `mu_p` center. The result includes
   `q=p^f`, kernel size `q/p`, and rank zero.
9. The abstract Weyl algebra depends only on the named `(k,V,omega,psi)` and
   half-form. A standard matrix formula additionally names a symplectic
   coordinate map; no preferred polarization, basis, or genuine Weil lift is
   claimed.
10. Rank one specializes to D4 at `beta=omega/2` and to the positive
    half-dot rephasing of D8 without relabelling positions.
11. The target relies only on admitted F1-DUAL/F1-WEYL/F1-REAL and current
    numbered definitions. It uses no REFUTED row, unregistered source, or
    `v0.1/` import.
12. The canonical row, DAG, proof preamble, and labbook all retain SKETCH and
    the same odd-characteristic/no-preferred-basis scope.

<!-- END VERIFIED CORRECT -->

## Status-register check

The artifact is currently honest at SKETCH and is in exact status/scope
lockstep with the canonical row and labbook. Its mathematical content is in
the same proof register as the nearest admitted F1-DUAL/F1-WEYL/F1-REAL rows:
the new bridge is a finite-dimensional corollary whose missing coordinate,
phase, center, trace, and endpoint calculations are supplied. OBJ-1 is a
wording closure repair. OBJ-2 narrows the advertised strength of two checker
subassertions and should be repaired mechanically, but it does not leave a
FATAL or MAJOR mathematical gap. Promotion remains the coordinator's
adjudication action.

PASS
