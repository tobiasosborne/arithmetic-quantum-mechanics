# Exact primitives for the full continuous Karoubi completion

The six-gate checker was written with the Astra prover submission, then
independently run and data-mutated by the Sol Karoubi critic. It is now
`theory/checks/f1_limit_karoubi_check.py`; its mathematics is unchanged.

| Gate | Finite example | Mutation |
|---|---|---|
| K1 | Full same-total matrix corners when graded tensor contributions collide | --red-grading |
| K2 | Rectangular Kraus transport and the normalized trace-weight ratio | --red-density-ratio |
| K3 | A continuous projection and its spectral cutoff | --red-cutoff |
| K4 | Local normalized Kraus correction | --red-normalization |
| K5 | Independently rotated diagonal conditional expectation and trace pairing | --red-gram |
| K6 | Uniform classical trace and output-cardinality factor | --red-classical |

Green probe counts are K1–K6: 4,3,10,3,3,3. Every advertised red mode was
observed failing at its own mathematical gate while all other gates ran;
none relies on a parsing failure or interpreter exception. The independent
critic additionally perturbed a non-parabolic projection and recomputed a
mixed-degree tensor trace at q=1,3/2,2,3. Its record is in the Karoubi verdict.

All arithmetic is rational/integer. Passing these examples does not prove
the general projection-lifting theorem, norm continuity, all-rank trace
multiplicativity, Gram-basis continuity or categorical presentation. Those
statements rest on the structured proofs. The new trace weight is denoted
w_X after integration, to distinguish it from the fusion dimension d_X.
