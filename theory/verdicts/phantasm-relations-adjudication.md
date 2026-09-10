# Mechanical adjudication — relations, compact data, and stabilizer comparison

Date: 2026-09-10. Adjudicator: `gpt-5.6-sol`, reasoning `xhigh`.

This is a mechanical disposition of preserved reviews and their sole repair
waves. It is not a fresh proof review. The mathematical calculations fenced as
verified by the valid critics were not reopened.

## Record used

- Classical blind verdict: `theory/verdicts/phantasm-relations-r1.md`.
- Classical prover repair: `classical-prover-repair.md` in the result directory below.
- Classical checker repair: `classical-checker-repair.md` in that directory.
- Invalidated quantum attempt: `theory/verdicts/phantasm-stabilizer-invalidated.md`.
- Sole valid quantum blind verdict: `theory/verdicts/phantasm-stabilizer-r1.md`.
- Quantum prover repair: `stabilizer-prover-repair.md` in that directory.
- Separate checker-only audit:
  `theory/verdicts/phantasm-stabilizer-code-verification.md`.
- Quantum checker repair: `stabilizer-checker-repair.md` in that directory.
- Final targeted records under
  `numerics/symplectic-phantasm/results/relations-2026-09-10/`.

The first quantum attempt is not counted as a proof review. It crossed its
literal blind-file boundary and was invalidated before verdict. Its later code
audit was mechanical only.

The sole valid SP-STAB-REL critic was also the independent checker author.
That same-family overlap limits checker independence. The critic explicitly
did not use the checker as self-validation: it supplied a separate exact
recomputation, and another actor audited the checker and drove its repair. The independent
recomputation and probe are frozen as `stabilizer-independent-recomputation.md`
and `stabilizer-independent-recompute.py` in the same result directory.

## Decision order

The dependencies force the following order:

1. SP-LREL, with no mathematical dependency.
2. SP-COMPACT, depending on SP-LREL.
3. SP-STAB-REL, depending on both classical claims and the already admitted
   SP-WEYL, SP-EGOROV and SP-TENSOR results.

## SP-LREL disposition

The classical critic returned
`FAIL(OBJ-1, OBJ-2, OBJ-3, OBJ-4)` and also recorded OBJ-5 and OBJ-6 as MINOR.
Its verified-correct fence accepted the general finite-field reduction,
affine empty/nontransverse cases, category/dagger/tensor laws and faithful
graph calculations. The one repair wave closes every objection:

- OBJ-1: D1701 now owns affine-arrow direct sum, zero unit and the
  zero-translation associator, unitors and symmetry. The repaired canonical
  `lrel-laws.md` proves those source data coherent before calling the graph
  functor symmetric monoidal.
- OBJ-2: D1714 and its labbook restatement bind the finite-dimensional
  symplectic spaces `U,V,W` before use.
- OBJ-3: the unsupported generic `--red NAME` interface was removed. Help now
  exposes exactly fourteen concrete classical mutation flags.
- OBJ-4: G6 was split into G6a--G6f. `dagger-swap` reaches G6c and
  `snake-wire` reaches G6d after the earlier cup checks.
- OBJ-5: the duplicated tensor comparison was replaced by an independent
  Boolean relation-matrix Kronecker oracle.
- OBJ-6: `compact.md` now points to the actual `lrel-reduction.md` and
  `lrel-laws.md` shards and to the canonical SP-COMPACT row/DAG.

Root's strict targeted classical run passed green and all fourteen advertised
mutations at their named gates. With only G6c disabled on a temporary copy,
`dagger-swap` survived with exit `0`; restoration returned it to exit `1`.

No classical FATAL or MAJOR remains after the sole repair wave. The admitted
scope is every finite field, including characteristic two, zero objects,
empty relations and nontransverse affine composites.

Admitted: SP-LREL

## SP-COMPACT disposition

SP-COMPACT used the same valid classical review. The critic accepted the
opposite-form diagonal cup/cap typing, both fully typed snakes, bare-converse
dagger equation, name/unname bijection, empty cases, Boolean unit scalars and
the witness-forgetting closed loop. Its relevant objections were the missing
labbook quantifiers, proof locators and compact mutation reachability, all
closed above.

The dependency SP-LREL is admitted immediately before this decision. No
compact objection survives the repair, and the targeted G6 control confirms
that the dagger acceptance path is effective.

The admitted scope is the classical affine Lagrangian category over every
finite field. Its closed loop is the nonempty relational scalar, without
witness multiplicity, amplitude or quantum normalization.

Admitted: SP-COMPACT

## SP-STAB-REL disposition

The sole valid blind quantum verdict is `PASS` with one MINOR. Its verified
fence accepted origin independence, the rank-one character projector,
support/overlap and zero-composite criteria, recovery, bare-converse adjoint,
grouped tensor/coherence, opposite-space vectorization, D1704 membership,
all-`C_2(A)` fullness, faithfulness and object surjectivity.

The MINOR concerned the typed zero amplitude. Equality conventions alone did
not construct a zero in every D1704 Hom-set. The sole prover repair now gives,
for every `m,n`,

    e_n o (0:C->C) o e_m^*:H_(F_p,m)->H_(F_p,n),

where `e_j` is the tensor of computational zero preparations and `e_0=1_C`.
The repaired canonical `stabilizer-equivalence.md` and labbook proof both
contain this typed construction. The objection is closed without changing
the statement or scope.

The separate code-only audit found bulk acceptance paths that the original
thirteen mutations did not reach. The sole checker repair propagated the S3
construction mutations into the actual catalog and added projector,
actual-family and F5-orbit controls; moved product, zero-product and dagger
mutations into S4's exhaustive loops; moved tensor order into S5's bulk; and
added a final F5 cap-weight scalar mutation.

Root's final targeted quantum verification completed successfully:

- all eighteen help-advertised mutations exited `1` at their exact intended
  S1--S5 subchecks;
- green covered all 389 small F3 relation lines, all 140,101 typed F3
  compositions, all 389 daggers, 338 state/effect tensors, 144 selected mixed
  tensors, and the registered F5 controls;
- disabling only S5e made `f5-cap-weight` survive with exit `0`, and restoring
  S5e returned it to its intended failure.

The two classical dependencies are admitted above, and the stage-one quantum
dependencies were already admitted. The valid proof review has no open FATAL
or MAJOR, its sole MINOR is repaired, and the checker objections are closed.

The admitted quantum scope is odd prime fields on the standard objects
`V_n`, all ranks including zero, with the fixed trace-framed character and
quotient by every element of `C^times`, retaining zero separately.

Admitted: SP-STAB-REL

## Coordinator interface verification

The contract checker now resolves and validates every file in a multi-shard
Proof field, rather than treating a comma-separated list as one filename.
Its new `proof-shard` mutation appends an existing unstructured document and
fails at G4. All twenty-two advertised contract modes failed at their exact
intended gates after the three promotions, and the green contract verifies
the exact canonical/labbook definitions, statements and scopes.

A help-token audit found two unsupported `--red-` wildcard prefixes in the
contract and older limit checker docstrings. Both produced argparse usage
errors, not failed mathematical checks. The descriptions were corrected;
no older mathematical checker code changed. The historical stage-1 total
of 279 advertised runs included these two usage errors. The final token
audit rejects unsupported flags and required-argument bare modes while
retaining valid optional-argument aliases. The new classical and quantum
strict verifiers require exit 1 and the named gate; exit 2 does not pass.

## Boundaries retained

These admissions do not choose actual representative norms, successful-branch
normalizations or probabilities. They do not define CP maps, instruments or a
Choi correspondence; D1706 remains separate. They do not assert arithmetic
source exhaustion, Gaussian-channel exhaustion, extension-field scope,
characteristic-two quantum scope, or a genuine scalar-retaining lift.

The final targeted checker runs above are complete. Repository-wide
validation passed all 30 green suites and 310 advertised red runs in
aggregate. The canonical session-close process terminated with SIGTERM
(exit 143) after 15 greens and 164 reds without a reported mathematical
failure; the frozen resume script completed every unfinished command and
verified unchanged checker hashes. The partial and resumed transcripts and
complete coverage record are preserved in the result directory. This is not
a claim that the interrupted process itself reached its success banner.

The final labbook builds at 182 pages. The new compact/intertwiner data and
relation/stabilizer statements and proofs were visually inspected on
pp.172--173 and 176--180; final provenance was rebuilt and inspected. The
lockstep and contract checks passed against the final sources. Computations
remain finite corroboration, while the all-field/arbitrary-rank mathematics
rests on the valid reviews and their bounded repairs.

PASS
