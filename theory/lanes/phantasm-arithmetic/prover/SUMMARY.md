# Arithmetic prover summary

Lane model: `gpt-5.6-sol`, reasoning `xhigh`.

The prover pass supplies four bounded Lamport shards for the exact canonical
SP-TRACE, SP-FROB and SP-SUBSYS statements.

`trace.md` proves arbitrary-rank nondegeneracy of the relative trace form,
nontriviality of a named possibly nonstandard relative character, exact
identity of the two odd-characteristic half-form Weyl algebras, rank zero,
degree divisible by the characteristic and compatible tower composition.

`frobenius.md` proves K-linearity and trace-form symplecticity of the
`#K`-power, invariance of every named relative character, exact
arbitrary-rank symmetrized Weyl covariance, the rank-zero identity, and the
invertible unitary-conjugation channel with `[E:K]`th power identity.

`subsystem-models.md` proves the actual nondegenerate orthogonal complement,
constructs the model unitary from admitted SP-TENSOR/SP-WEYL, proves the
combined iterated complement comparison symplectic, and constructs all four
registered iterated unitaries with the exact pure-tensor compatibility up to
the allowed phase.

`subsystem-decoder.md` proves the observable inclusion is a unital
star-homomorphism, constructs the ordinary partial-trace Kraus channel,
derives Weyl-characteristic restriction and phase independence, and proves
the full compatible inclusion/decoder tower by basis expansion. It keeps this
TP tensor decoder distinct from D1327's TNI support-code success branch.

Supporting artifacts are `LABBOOK-FRAGMENTS.tex`, `SOURCE-REUSE.md`, and
`PATCH.md`. The independent arithmetic expectations file is frozen; its
contents and checker code were not read in this prover pass. All claims remain
`SKETCH`, with no trunk/status/checker/Git change or characteristic-two,
global, modular or spectral expansion.
