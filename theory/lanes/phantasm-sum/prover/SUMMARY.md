# SP-SUM prover summary

Lane model: `gpt-5.6-sol`, reasoning `xhigh`.

`sum.md` is a bounded Lamport prover pass for the exact canonical SP-SUM
statement. Actual computational preparations, translations and adjoints give
every rectangular matrix unit, while arbitrary addition enters only in
D1707's complex span. F1-REAL square spanning is reused without reopening
finite SvN.

Admitted SP-STAB-REL proves this enlargement is strict: actual amplitudes
give finitely many projective rays in each finite-field relation Hom-set,
whereas a complex Hom-space of dimension greater than one has infinitely
many rays.

The block realization is proved bijective onto all maps between coherent
finite sums and compatible with composition and adjoint. It handles empty
source/target lists as typed zero maps, distinguishes the empty list from the
rank-zero object `C`, and preserves repeated tags.

For nonempty lists, the proof derives the coherent and tagged dimensions and
identifies the tagged algebra with the diagonal blocks. D1707's summand
projections give an ordinary-trace-preserving SP-CP channel that deletes
off-diagonal blocks and has tagged range. No zero-space channel is claimed.

Supporting artifacts are `LABBOOK-FRAGMENTS.tex`, `SOURCE-REUSE.md`, and
`PATCH.md`. The independent `EXPECTATIONS.md` is frozen; its content and
checker code were not read.
SP-SUM remains `SKETCH`, with no trunk/status/Git action or stronger
categorical/source claim.
