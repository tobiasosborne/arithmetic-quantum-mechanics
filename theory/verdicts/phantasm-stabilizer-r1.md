# Blind hostile verdict — SP-STAB-REL

Date: 2026-09-10. Critic model: `gpt-5.6-sol`, reasoning `xhigh`.
Same-family prover/critic; blind lane.  This is the sole valid blind review:
the earlier reviewer was invalidated before verdict, and I did not read that
review or its notes.  I read no prover proposal, patch, summary,
source-locator file, or reasoning context and did not contact the prover.

I independently authored the frozen finite checker before being assigned this
critic role.  That limits checker independence; it is not used as validation
of its own implementation.  The proof was recomputed separately in
`RECOMPUTATION.md`, and a separate actor is assigned to audit the checker.

Targets reviewed in full:

- `theory/lanes/phantasm-stabilizer/prover/intertwiner-line.md`;
- `theory/lanes/phantasm-stabilizer/prover/functor-laws.md`;
- `theory/lanes/phantasm-stabilizer/prover/equivalence.md`;
- `theory/lanes/phantasm-stabilizer/prover/LABBOOK-FRAGMENTS.tex`.

## Objections

### OBJ-1 — MINOR — empty target membership cites equality rather than constructing the typed zero

**(a) Exact location.** `equivalence.md` section 2 `<1>14`, especially the
justification “D1715 and D1704's equality convention.”

**(b) Independent computation.** D1715 indeed assigns `{0}` to every typed
empty relation, but equality of actual maps does not by itself put the zero
map in every D1704 Hom-set.  The required construction is available: tensor
the one-register preparations to obtain `e_n:C->H_n`, tensor their adjoints to
obtain `e_m^*:H_m->C`, and compose
`e_n o (0:C->C) o e_m^*`.  This is the zero map `H_m->H_n` and uses exactly
D1704's generators.  Thus the theorem is correct, but the cited leaf names
the wrong clause and omits the typed construction.

**FIX DEMAND.** Replace section 2 `<1>14`'s equality-convention justification
by the explicit `e_n o 0 o e_m^*` D1704 generator construction.

**SURVIVING WEAKER STATEMENT.** The empty relation does map to the actual
typed zero stabilizer amplitude for every pair of ranks.

## Independently verified correct — do not churn in repair

<!-- VERIFIED-CORRECT-BEGIN -->

1. The operator-space action has the claimed `-omega_m+omega_n` half-form
   multiplier, Hilbert--Schmidt adjoint and zero-away-from-origin trace.
2. The all-origins D1715 definition is origin independent.  Its character
   average is an orthogonal projector of trace and rank one for every
   nonempty affine Lagrangian; the empty prescription is distinct.
3. The projective Weyl stabilizer recovers the Lagrangian direction, and its
   faithful eigencharacter recovers the affine coset.  No basis or origin is
   retained.
4. The initial/final support characters have the stated signs.  The restricted
   `A^perp/A` Weyl family spans the full support endomorphism algebra, forcing
   `TT^*` and `T^*T` to be positive scalar support projectors.
5. Two middle supports overlap exactly when the affine middle projections
   meet.  Consequently nonempty relation factors compose to zero exactly for
   an empty relational composite, and common-middle origins give the correct
   composite character when nonempty.
6. Bare relational converse maps to Hilbert adjoint.  No SP-BC24
   time-reversal involution is imported.  Tensor uses D1702's grouped reorder,
   the admitted SP-TENSOR comparison, the zero unit and the standard
   associator/unitor/symmetry maps.
7. The opposite-space map `(a,b)->(a,-b)` and computational vectorization have
   the stated factor order.  Every resulting affine Lagrangian state is an
   actual D1704 stabilizer preparation; Bell contraction unvectorizes it.
8. The arbitrary-normalizer calculation treats every D1307 `C_2(A)` unitary:
   its label map is Fp-linear symplectic and its phase is the character of a
   unique affine translation.  It therefore lies in an affine graph line.
9. Generator induction proves fullness; line recovery proves faithfulness;
   the standard object assignment is surjective.  The full `C^times` quotient
   and separate zero are maintained, with no normalized branch or CP/Choi
   claim.
10. The canonical statement, DAG scope, proof headers and labbook fragment all
    retain `SKETCH`, odd-prime standard-object scope and the explicit
    SP-LREL/SP-COMPACT dependencies.  Those two dependencies remain
    unpromoted pending the coordinator's repair verification/adjudication, so
    this verdict does not authorize out-of-order promotion.

<!-- VERIFIED-CORRECT-END -->

## Quantifier, canonicity, reliance, and source checks

The proof delivers all odd primes and all ranks, including rank zero, exactly
as claimed.  It never includes characteristic two or extension fields.
The fixed trace-framed character, standard coordinate ordering, opposite
source form, bare converse and all-invertible-scalar quotient are explicit.
The symplectic-basis and line-representative choices disappear from the
projective assignment; origin independence is proved.

No step relies on a REFUTED claim, `v0.1`, an unregistered source, or the
invalidated review.  SP-CK21 directly states the odd-prime symmetric monoidal
equivalence modulo invertible scalars, but its local discussion relies on
earlier stabilizer references for some generator facts; the target proof does
not outsource its line, fullness or dagger argument to that history.
SP-GROSS06 supports the odd-prime Clifford/phase-space normalizer result.
SP-BC24 uses the global-negative relation form and a time-reversed dagger;
only its explicitly compared convention is used.  My source inspection was
limited to the registered local primary bodies and locators.

## Checker and independent computation register

The frozen checker passed S1--S5.  All thirteen advertised reds exited `1`
at their intended gates; every gate has reachable mutations.  Independent
exact Eisenstein-integer probes passed 729 vectorization cases, projector,
support, overlap and bare-dagger examples, while detecting missing conjugation
and the reversed affine character.  A copied-checker source-form mutation
passed S1--S2 and failed S3's all-origin equation.  These computations are
finite corroboration only, and checker self-authorship is explicitly not an
independence claim.

## Status register check

The artifact's `SKETCH` register is honest and agrees with the canonical row
and labbook fragment.  With no FATAL or MAJOR objection, the proof is suitable
for coordinator repair of OBJ-1 and later adjudication, but SP-STAB-REL cannot
be promoted before SP-LREL and SP-COMPACT are themselves admitted.

PASS
