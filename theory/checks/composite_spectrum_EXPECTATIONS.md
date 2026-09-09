# Exact finite spectrum/completion falsifiers

`composite_spectrum_check.py` is an independent standard-library-only
checker. The original preregistration and frozen evidence are preserved in
`theory/lanes/composite-spectrum/check/` and
`numerics/composite-spectrum/results/` respectively.

Green executes 41,216 exact comparisons over seven gates: divisor corners
and arithmetic embeddings (S1), actual copied-reference degree weights
(S2), finite Frobenius actions (S3), positive cutoff densities (S4),
Dirichlet coefficients (S5), implementing moments (S6), and tensor-cycle
distinctions (S7). Every gate has an actual data mutation.

There are thirteen distinct data changes, fourteen named --red-* flags,
and fifteen advertised flags including plain --red. `central-dynamics`
is an explicit alias of the identity-action mutation; plain --red aliases
drop-divisor-weight. These aliases are not counted as independent
mathematical mutation scenarios. Every invocation must return exit one
with JSON status FAIL at the registered S1--S7 mathematical gate.

The main samples include binary fields through F4096, a nonprime-base
F16/F4 comparison, all twenty-two polynomial embeddings and thirty-eight
strict tower paths. Integer cutoffs D=2,4,8,16,32 and beta=2,3,4 use exact
positive state normalization, not decimal zeta values. Dirichlet coefficients
are checked through 120 and finite tail fragments through 128.

The infinite norm completion, outerness, trace domains and all-beta
convergence rely on the structured proofs. Finite norm-one displacement
tests are evidence for the actual cyclic action, not a proof of infinite
outerness. The tail estimate's cutoff is an integer. No analytic
continuation, Riemann-zero spectrum or endpoint tensor closure is checked
or asserted.
