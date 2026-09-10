# RUNS — completion controls

Date: 2026-09-10. Python 3.12.3, x86_64.
Model: `gpt-5.6-sol`, reasoning setting `xhigh`.

`EXPECTATIONS.md` was frozen before implementation and reported to the
coordinator.  The lane read no completion prover artifact or notes and made no
trunk change.

Commands were run from the repository root as

    PYTHONDONTWRITEBYTECODE=1 python3 \
      theory/lanes/phantasm-completions/checker/phantasm_completions_check.py <mode>

## All reds before first green

All thirteen help-advertised actual-data mutations were run before the first
green:

| mode | exit | intended first failure |
|---|---:|---|
| `fock-vacuum` | 1 | F1: sector-zero rank/vacuum at `d=0,r=0` |
| `one-mode-factorial` | 1 | F1: one-mode normalized occupation at `r=2` |
| `fock-binomial` | 1 | F2: exponential normalization at `(n,m)=(1,1)` |
| `fock-expansive` | 1 | F3: accepted contraction datum replaced by actual `2I`, deficit `-3I` |
| `prime-position` | 1 | P1: prime-2 identity inserted after prime 3 |
| `prime-nonunital` | 1 | P1: inserted `diag(1,0)` fails the common unit |
| `density-trace` | 1 | P2: unnormalized rho_2 breaks finite state compatibility |
| `gns-separating` | 1 | P2: faithful separating-test reference replaced by pure rho_3; Gram-action rank loses injectivity |
| `mu-unitary` | 1 | B1: range projection treated as identity at index 1 |
| `root-average` | 1 | B2: missing `1/n` changes the divisible-index coefficient |
| `time-sign` | 1 | B3: valuation-vector time exponent reversed |
| `L-multiplicative` | 1 | B3: actual L compression substituted into the corner-homomorphism product action |
| `b1-trace-class` | 1 | B4: concrete bound 3 exceeded by `H_(2^8)` |

The first green exited `0`.  Self-review then removed a decorative symbolic
tuple equality in F3, replaced P2's copied Gram-rank cyclicity line by an
actual matrix-unit left-action rank, and added symbolic matrix-unit
multiplication/star/corner checks for `nu_n` and `L_n`.  Coordinator steering
then made the three named mutations concrete: actual `2I` replacement with a
PSD deficit check, faithful-to-pure density replacement with Gram-action
injectivity, and actual L-for-nu map substitution in the homomorphism square.
Independent genuine growth, pure nonseparating and L nonmultiplicativity
witnesses remain green checks.  The affected reds were rerun before final
green.

## Disabled-guard survival controls

Only three central finite acceptance comparisons were disabled temporarily,
with their actual mutations still active.  Each red then survived its target
gate with exit `0`:

```text
RED SURVIVED fock-binomial at F2: 15 exact binomial norm-square and homogeneous naturality cases
RED SURVIVED prime-position at P1: 14 inclusions and 30 increasing-prime triangles; exact a*a polynomials
RED SURVIVED root-average at B2: 360 rational phase, divisibility and normalized root-average cases
```

All comparisons were restored immediately.  The final red matrix again gave
exit `1` at every path in the table above.

## Final green and usage records

Final ordinary green exited `0` in 0.11 seconds; optimized green exited `0`
in 0.26 seconds.  Both printed:

```text
F1 PASS: 15 rational symmetrizers; ranks (1,0..),(1^5),(1,2,3,4,5), vacuum/one-mode
F2 PASS: 15 exact binomial norm-square and homogeneous naturality cases
F3 PASS: sector functor through 4; 2I norms 1,2,4,8,16 with symbolic 2^r duty
P1 PASS: 14 inclusions and 30 increasing-prime triangles; exact a*a polynomials
P2 PASS: faithful/pure product states; GNS Gram ranks 576,192,3 and cyclic/nonseparating witness
B1 PASS: symbolic semigroup/adjoint laws on 5 shifts and 30 indices; no truncation
B2 PASS: 360 rational phase, divisibility and normalized root-average cases
B3 PASS: prime-valuation dynamics and concrete L_2(mu_2 mu_2*) != L_2(mu_2)L_2(mu_2*)
B4 PASS: rational b=2,3 tail intervals and eight finite dyadic b=1 lower witnesses
GREEN PASS: exact finite/symbolic controls only; no claim promotion
```

Help exposes exactly thirteen named red flags.  Bare and multiple-red usage
exit `2`.  The norm-two and b=1 checks are finite witnesses attached to
written analytic obligations; the checker makes no finite-to-infinite
inference.

## Sole checker repair wave

The valid blind verdict's two checker MINORs were accepted. Expectations were
updated before implementation.

F3 now applies actual `tensor_power(2I,r)` matrices to the normalized
`e_0^tensor r` symmetric vectors, checks symmetrizer commutation, exact output
coefficient `2^r` and norm square `4^r`. New tensor-collapse changes those
actual matrices to sector identities and exits `1`:

```text
RED CAUGHT fock-tensor-collapse at F3: actual tensor power of 2I failed symmetric growth at sector 1
```

B1 now compares the actual `mu_star(n,k)` helper with `k/n` on divisible
indices and `None` on nonmultiples for every sample. New adjoint-divisibility
makes `mu_star(5,k)` floor-divide nonmultiples and exits `1`:

```text
RED CAUGHT mu-adjoint-divisibility at B1: actual mu_n* disagrees with the divisibility oracle
```

The original left-inverse and proper range-projection controls remain
separate. With only each new acceptance comparison temporarily disabled, its
actual mutation survived with exit `0`:

```text
RED SURVIVED fock-tensor-collapse at F3: sector functor through 4; 2I norms 1,2,4,8,16 with symbolic 2^r duty
RED SURVIVED mu-adjoint-divisibility at B1: symbolic semigroup/adjoint laws on 5 shifts and 30 indices; no truncation
```

Both comparisons were restored. The affected reds again exited `1`; normal
green exited `0` in 0.10 seconds and optimized green in 0.24 seconds. Help
exposes fifteen modes. Root owns the final installed all-mode strict battery;
the existing thirteen lane paths and all finite scopes are unchanged.
