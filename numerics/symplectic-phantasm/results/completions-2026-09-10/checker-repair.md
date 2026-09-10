# REPAIR — sole completion-checker repair wave

Date: 2026-09-10. Repair model: `gpt-5.6-sol`, reasoning `xhigh`.
Input: `theory/lanes/phantasm-completions/critic/VERDICT.md`, findings 1--2.

This is a bounded mechanical checker repair. It changes no proof, canonical
record, mathematical scope or status and triggers no fresh review.

## Finding 1 — actual tensor-power growth repaired

F3 no longer constructs the reported `(1,2,4,8,16)` tuple independently of
`tensor_power`. For each sector zero through four it applies the actual tensor
power of `2I` to a normalized symmetric basis vector and checks output
coefficient `2^r`, squared norm `4^r`, and commutation with the actual
symmetrizer. The finite values remain witnesses only; infinite unboundedness
is still a written-proof duty.

New `fock-tensor-collapse` replaces the actual `2I` tensor powers by same-size
identity matrices and first fails F3 at sector one. Disabling only that
acceptance comparison makes the mutation survive with exit `0`; restoration
returns exit `1`.

## Finding 2 — full adjoint divisibility repaired

B1 now compares the actual helper `mu_star(n,k)` directly with the exact
divisibility oracle for every sampled shift and basis index, including
nonmultiples. New `mu-adjoint-divisibility` makes only `mu_star(5,k)` return
floor division on nonmultiples and first fails B1. The existing left-inverse
check on the range and proper range-projection check are unchanged.

Disabling only the new direct comparison makes this mutation survive B1 with
exit `0`; restoration returns exit `1`.

## Verification

Both new reds were observed before repaired green, their disabled controls
survived, and restored affected reds exit `1`. Normal and optimized greens
pass; help exposes fifteen modes. Root performs the final installed all-red
battery. Existing thirteen paths and finite/analytic boundaries are preserved.
