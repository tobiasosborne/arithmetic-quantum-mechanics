# SP-EGOROV / SP-TENSOR prover summary

Actual lane model: `gpt-5.6-sol`; reasoning: `xhigh`.

The lane produced two Lamport proof shards, confined to this directory:

- `sp-egorov.md` proves the affine generator formula is a unital
  star-isomorphism, verifies the exact D1701 semidirect-product composition and
  inverse, identifies translation as conjugation by the target Weyl operator,
  and derives unique projective unitary implementation and model transport from
  the admitted `F1-REAL` uniqueness theorem.
- `sp-tensor.md` proves the generator comparison is a trace-preserving
  star-isomorphism, imports only the configuration/Hilbert tensor and half-form
  phase comparison already supplied by `F1-FUNCT` and `reuse.md`, proves the
  exact naturality square for arbitrary affine arrows, and proves exact algebra
  coherence plus projective model coherence for association, units, symmetry,
  and affine naturality.

Both drafts carry `SP-WEYL` as an explicit `SKETCH` dependency.  SP-TENSOR also
carries SP-EGOROV explicitly.  No finite Stone--von Neumann theorem,
configuration-product tensor theorem, or rank-one foundation was reproved.
No chosen genuine Weil lift, coherent representative phases, additive
completion, characteristic-two extension, or model-independent Hilbert space
was asserted.

Primary scope was checked locally against:

- SP-GH07 section 1.1 and Proposition `functor_prop`: odd-characteristic
  Heisenberg/SvN and the oriented, contravariant canonical quantization model;
- SP-GH09 Proposition `Cartesian_prop`: monoidal compatibility for that
  canonical model;
- SP-GROSS06 Theorem `thCliffordStructure` and Lemma `cliffordAffine`:
  projective symplectic and affine implementation in its odd-dimensional phase
  convention;
- SP-PRASAD09's registered finite Stone--von Neumann scope, used through the
  already admitted self-contained `F1-REAL` proof rather than rederived here.

No new numbered definition or notation row is needed for the two exact current
claims.  `PATCH.md` gives string-anchored integration instructions and keeps
both statuses unpromoted.  This prover lane did not read or design the
independent checker lane and ran no checker as mathematical evidence.
