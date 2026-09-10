# SUMMARY — arithmetic falsifier plan

Model: `gpt-5.6-sol`, reasoning `xhigh`.

`EXPECTATIONS.md` specifies twelve exact, independently mutable gates for
SP-TRACE, SP-FROB and SP-SUBSYS. New trace/Frobenius coverage includes
F27/F3 with degree equal to characteristic, the nonstandard F9 character in
F81, tower transitivity and sparse rank-0/1/2 Weyl covariance. It explicitly
separates this work from the existing R6 bridge.

The subsystem controls use a non-coordinate F3 cotangent lift with a monomial
permutation implementer, ordinary partial trace, asymmetric/classically
correlated/Bell inputs, Weyl characteristic restriction, phase cancellation
and a compatible three-register decoder tower.

Two interfaces must be owned before promotion: SP-FROB's D1706/SP-CP channel
reuse, already requested by the arithmetic brief, and the currently undefined
compatibility diagram behind SP-SUBSYS's iterated-decoder clause. This lane
does not add them. No SP-SUM lane artifact, proof, checker, status or trunk file
was read or changed.
