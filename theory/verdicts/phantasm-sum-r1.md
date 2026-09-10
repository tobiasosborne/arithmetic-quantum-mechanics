# Blind hostile verdict — SP-SUM

Date: 2026-09-10. Critic model: `gpt-5.6-sol`, reasoning `xhigh`.
This was the sole same-family prover/critic pass and used a literal blind lane.
I did not read the SP-SUM prover lane, checker lane, patch, source-reuse notes,
or hidden reasoning. The reviewed proof was the integrated canonical artifact.

Frozen targets checked:

- `sum.md`: `11ce000439fa096c2264bc9dca3f38953e198d74c940ade7df94c8761f6c1f06`;
- checker: `655af7eadda3991ab2eebabf14d21b0ea255bf35337e5ea12e6507e9a6b742fd`;
- expectations: `ab5d9ed46580e51b5bfbac1f76299964b304f90d463ec7d465b5df22f5dc7a85`.

The mathematical verdict is conditional on the already admitted SP-WEYL,
SP-CP, SP-STAB-REL, and F1-REAL statements at their registered scopes. I did
not re-review those admissions. No REFUTED row is used.

## Numbered objections

### 1. MINOR — U2 does not protect the completeness of the imported census

**(a) Location.** `theory/checks/phantasm_sum_check.py`, U2, lines 371--386,
especially the construction of `actual` at line 377 and the unguarded phrase
“outside 360 pure qutrit classes” at line 386; compare EXPECTATIONS U2.

**(b) Independent computation.** The current imported API really returns 216
Clifford rays, 144 rank-one rays, and 360 distinct endomorphism rays. An
independent cross-multiplication ray test gives zero hits for
`diag(1,1,0)`. However, on a temporary copy I replaced `endos` by
`endos[:1]` at U2. The complete green run still exited 0 and still printed
“outside 360 pure qutrit classes.” U2 checks exclusion from whatever iterable
it receives, but never checks that the iterable is the promised census.

**FIX DEMAND.** Assert the expected imported census cardinalities (and record
or verify the imported dependency hash) before making the 360-class report.

**SURVIVING WEAKER STATEMENT.** At the recorded current dependency hash, the
360-class census is present and the displayed rank-two diagonal has no ray
match; the general strict-enlargement proof does not depend on this finite
witness.

### 2. MINOR — the projection-loss mutant is not propagated through dephasing

**(a) Location.** `theory/checks/phantasm_sum_check.py`, U7, lines 483--505,
especially `used` at line 486 versus `projections` at lines 493--503; compare
the advertised mutation in EXPECTATIONS U7.

**(b) Independent computation.** In projection-loss mode only the completeness
sum uses `used=projections[:-1]`; every subsequent dephasing computation uses
the intact `projections`. Disabling only the completeness `need` on a
temporary copy made `--red-projection-loss` survive with exit 0. Thus the red
does reach and falsify its named first equation, but it does not model one
actual shortened Kraus family consistently through the rest of U7.

**FIX DEMAND.** Pass `used` to the dephasing calls in projection-loss mode, or
rename the red narrowly as a completeness-sum mutation.

**SURVIVING WEAKER STATEMENT.** The unmutated U7 exactly verifies completeness,
unitality, idempotence, and the rank-ten tagged range for the two correct
summand projections; the average mutant independently exercises the output
map.

### 3. NOTE — the DAG outline retains an unproved arithmetic-syntax comparison

**(a) Location.** `claims/PHANTASM-DAG.md`, SP-SUM Remaining and Construction
outline, lines 303 and 314, versus `theory/symplectic-phantasm/sum.md` section
5 `<1>6` and the exact CLAIMS row at `claims/CLAIMS.md:285`.

**(b) Independent computation.** The proof establishes strictness relative to
the pure actual-amplitude fragment by comparing finitely many admitted
projective rays with infinitely many rays in a two-dimensional plane. It does
not define or compare an “arithmetic coefficient syntax,” and section 5
correctly disclaims arithmetic-source exhaustion. The short canonical claim
also contains no such comparison. The two DAG prose lines therefore exceed
the proved target, although the current SKETCH/draft register makes no false
admission.

**FIX DEMAND.** Remove the arithmetic-coefficient comparison from SP-SUM's
Remaining/outline when adjudicating, or move it to a separately defined open
claim.

**SURVIVING WEAKER STATEMENT.** The exact SP-SUM claim proves strict enlargement
over pure stabilizer amplitudes and makes no arithmetic-source claim.

## Independently verified correct

<!-- VERIFIED-CORRECT-BEGIN -->

- In section 1 `<1>1`--`<1>11`, the actual words
  `e_y e_x^*` are all rectangular computational matrix units, including the
  `m=0` and `n=0` cases. Their coefficient-reading proof gives a basis of every
  rectangular Hom-space for every claimed odd prime.
- Section 1 `<1>13.<2>1`--`<2>5` correctly proves category-level strictness:
  admitted SP-STAB-REL supplies finitely many nonzero projective rays at fixed
  ranks, whereas `End(H_1)` contains the pairwise distinct rays of `E+zF`.
- Section 2 `<1>1`--`<1>11` gives a bijective block realization and checks
  composition and adjoint transpose. Empty lists give typed `D x 0`, `0 x D`,
  and `0 x 0` maps, while `(H_0)` remains the one-dimensional space `C`.
  Repeated equal spaces retain their ordered positions.
- Section 3 `<1>1`--`<1>6` gives dimensions `D^2` and `sum_i d_i^2` by an
  actual block decomposition. A cross-block matrix unit proves properness when
  at least two nonzero summands are recorded.
- Section 4 `<1>1`--`<1>10` computes the matrix-unit action of `Delta_X`, its
  exact tagged range, idempotence, unitality, Kraus completeness, complete
  positivity via admitted SP-CP, and preservation of the ordinary trace.
- The nonempty boundary is correctly enforced before applying D1706. No
  channel on the zero Hilbert space is claimed.
- The only construction choices used are the D1003 computational coordinates
  and D1707's recorded ordered block decomposition. No independence from
  either choice is asserted.
- The proof, CLAIMS row, canonical definition, and labbook agree on odd primes,
  standard model spaces, coherent versus tagged algebras, and the exclusion of
  biproduct, fusion, rig, Gaussian, and source-exhaustion conclusions.

<!-- VERIFIED-CORRECT-END -->

## Quantifier, source, and status register

The proof covers all `m,n>=0` and all finite ordered lists at every odd prime,
not only the checker's `p=3`, ranks zero through two. The coordinate argument
also works at `p=2`, but D1704 and the admitted relation comparison do not have
that scope, and neither the statement nor proof promotes characteristic two.
No extension-field claim is made. Watrous's one-coordinate dephasing formula
is used only as a locator; the block result is derived directly. CK21 is not
silently used to infer a larger additive or rig theorem.

The status register is honest: canonical proof header, CLAIMS, DAG, and
labbook all say SKETCH/draft pending review. The nearest dependencies are
registered PROVED. This verdict does not itself promote SP-SUM.

PASS
