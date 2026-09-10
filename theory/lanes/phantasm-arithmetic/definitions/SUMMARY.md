# Arithmetic definition proposal summary

Preparation model: `gpt-5.6-sol`, reasoning `xhigh`.

`CANDIDATE.md` supplies a complete replacement D1710 that preserves the
existing single-injection subsystem, observable inclusion and ordinary-trace
decoder. It adds the missing ownership for two composable injections:

- actual complements in the intermediate and final spaces plus the combined
  complement;
- typed single-step, composite and complement model unitaries;
- an explicit pure-tensor reassociation comparing staged and direct encoding;
- compatibility up to one unretained overall phase;
- rank-zero model and tensor-unitor cases.

The definition asserts none of the desired theorems. Well-definedness and
symplecticity of the complement comparison, complement nondegeneracy,
existence of compatible models, phase independence, inclusion/decoder laws
and iterated decoder composition remain SP-SUBSYS obligations. A tensor
subsystem is not replaced by scalar restriction or D1327's support-code
success branch.

The proposal also gives the narrow SP-FROB interface repair: add D1706 and
admitted SP-CP solely to type unitary conjugation as a channel. Field
permutation, Weyl covariance, inverse and finite power remain SP-FROB work.

`PATCH.md` gives exact string anchors for the definition, notation, claim,
DAG and labbook changes. This lane contains no proof, checker, review,
canonical edit, status change or Git action and does not begin the arithmetic
cluster before the planned SP-SUM pass.
