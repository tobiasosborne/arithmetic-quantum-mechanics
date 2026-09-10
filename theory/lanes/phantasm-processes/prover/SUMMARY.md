# Process prover summary

Lane model: `gpt-5.6-sol`, reasoning `xhigh`.

The prover pass supplies the exact SP-SCALAR and SP-CP arguments in three
bounded Lamport shards.

`scalar.md` proves amplified one-Kraus positivity, the rectangular trace
identity, trace nonincrease iff `T^*T<=1`, and
`Phi_(cT)=|c|^2Phi_T`, including `T=0` and `c=0`.  It distinguishes phases
from non-unit-modulus rescalings and states only that D1705 prescribes no
branch, probability or normalization rule. It proves positively that
`T rho T^*/||T||^2` is a representative-independent TNI branch on every
nonzero class, with zero handled separately. Compatibility of an added rule
with composition is outside the claim.

`kraus-blocks.md` proves both directions of the finite direct-sum Kraus/CP
criterion.  SP-WAT18 Theorem 2.22 is invoked only for nonzero component maps;
zero components receive empty lists.  The shard proves the per-input block
TNI and channel iff-conditions using ordinary trace and keeps actual CP-map
equality distinct from D1325 source equality.

`instruments.md` first constructs the unique ordinary-trace adjoint of every
complex-linear block map by conjugate-transposing its matrix-unit coefficient
matrix. It then proves composition and tensor closure with exact hidden and
block indices, including entangled tensor inputs.  It proves retained,
sequential and independent instrument normalization with outcome-first pairs
and no outcome-count factor.  The Kraus formula for `Phi^(tr*)` is CP and
unital for channels; ordinary discard shows it need not be a reverse TNI
branch.

Supporting artifacts are `LABBOOK-FRAGMENTS.tex`, `SOURCE-REUSE.md`,
`PATCH.md`, and the sole-wave `REPAIR.md`. All proof shards remain within the
required 200--500 range. The independent checker remains separately owned.

Both claims remain `SKETCH`.  No normalized relation lift, automatic CP
assignment from the projective quotient, arbitrary source exhaustion,
automatic CP dagger, field/global construction, spectral conclusion, trunk
edit, or Git action is asserted.
