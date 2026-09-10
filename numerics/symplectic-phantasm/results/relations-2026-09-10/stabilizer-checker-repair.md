# REPAIR — one SP-STAB-REL checker repair wave

Date: 2026-09-10. Repair model: `gpt-5.6-sol`, reasoning `xhigh`.
Input: `theory/lanes/phantasm-stabilizer/critic/CODE-VERIFICATION.md`.

This is a checker-only mechanical repair.  The report is not a proof verdict,
and this wave changes no mathematical scope, proof, claim status or trunk
file.  The valid blind proof review remains complete and separate.

## S3 — repaired bulk reachability

The four original mutations now run through actual catalog construction:

- `fixed-seed` changes every nonempty relation's column scan and reaches S3a;
- `average-sign` changes every nonempty catalog projector and reaches S3b's
  independently dense all-origin equations;
- `origin-dependent` changes actual alternate-origin averages and reaches
  S3e;
- `empty-nonzero` changes each catalogued empty relation image and reaches
  S3f.

Their old special preflights were removed.  Added actual-data modes cover the
rank certificate (`projector-entry`, S3c), independent qutrit target family
(`family-state-loss`, S3h), and final F5 Clifford orbit
(`f5-state-loss`, S3k).  The named subchecks S3a--S3l state honestly which
shared gate they exercise; no expected-count literal is mutated.

## S4 — repaired exhaustive paths

The graph and complex-state mutation preflights were removed.
`product-order` now reverses products inside square `1->1->1` cases in the
140,101-pair loop and reaches S4a.  Rectangular cases stay well typed.
`dagger-transpose` changes the actual adjoint in the 389-relation loop and
reaches S4c.  New `zero-product` changes the first actual zero product of two
nonempty factors into a nonzero matrix and reaches S4b on a `0->1->0`
state/effect composite.  The explicit zero and unequal-norm scalar witnesses
remain subsequent green assertions rather than mutation prechecks.

## S5 — repaired tensor and cup paths

`tensor-order` now changes Kronecker order in the exhaustive 169-state loop,
and the same mutation is wired through the effect and mixed loops.  It reaches
S5a without a special graph preflight.  The point-set assertion
`cup.pts==identity.pts` was removed because it erased types and repeated the
same diagonal construction.  S5d retains the independent D1715
operator-vectorization/Bell comparison.

New `f5-cap-weight` changes one coefficient of the actual F5 Bell cap after
all tensor and Bell checks.  It reaches S5e's exact retained scalar.  With only
S5e temporarily disabled, this mutation survived and exited `0`; after
restoration it again exited `1` at S5e.

## Verification

All thirteen changed/new paths were observed before repaired green.  After
the disabled-comparison control and restoration, all eighteen advertised reds
were rerun and exited `1` at their registered S1--S5 gates.  Help advertises
only those supported flags; malformed/multiple usage remains exit `2`.
Ordinary and optimized green runs pass with the same finite counts.  Exact
outputs are in `RUNS.md`.

The checker remains finite, negative-binding evidence only.  It does not prove
general fullness or equivalence, choose normalization, or introduce CP/Choi
semantics.
