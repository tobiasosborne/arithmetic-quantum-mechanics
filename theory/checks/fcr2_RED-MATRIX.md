# FCR-2 red-mutation reachability matrix

Lane model: gpt-5.6-sol, reasoning xhigh, codex exec.

`F` means the gate actually failed in the recorded red run.  `-` means the
mutation does not alter that gate's datum or claimed result.  The driver runs
every gate at the targeted seed; merely reaching a passing gate is not counted
as mutation coverage.

| gate | fake epsilon | collapse | transpose | half-Weyl | wrong profile | field split | square coefficient | model sign | Frobenius-blind |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| G1 | - | - | F | - | - | - | - | - | - |
| G2 | - | - | - | - | - | - | F | - | - |
| G3 | - | F | - | - | F | - | - | - | - |
| G4 | F | - | - | - | - | - | - | - | - |
| G5 | - | - | - | - | - | F | - | - | - |
| G6 | - | - | - | - | - | - | - | F | - |
| G7 | - | - | - | F | - | - | - | - | - |
| G8 | - | - | - | - | - | - | - | - | F |

Every G1--G8 gate has an actually run mutation.  G3 deliberately has two:
one attacks the orbit count and one attacks a profile fixture, so those two
independent parts do not share a bit-identical red fingerprint.

## Observed mutation fingerprints

| mode | sole mutated datum or claim | target | observed first failure |
|---|---|---|---|
| `--red-fake-epsilon` | report `epsilon(beta0)=zeta8`, leaving both exact sums unchanged | `Z4/G4` | direct/histogram mismatch `zeta8^1` versus `zeta8^0` |
| `--red-collapse` | claim one centre-fixed class rather than two | `Z4/G3` | discovered `2`, claimed `1` |
| `--red-transpose` | use `beta0^T` while retaining `beta-beta^T=omega` | `Z4/G1` | first bad pair `(1,4)`; the sign of `omega` reverses |
| `--red-halfweyl` | invent an inverse of doubling and hence `omega/2` | `Z4/G7` | exhaustive table has no inverse of `2` |
| `--red-profile` | install `{1:1,2:1,4:62}` at the dual numbers | `F2[e]/e2/G3` | actual profiles are `{1:1,2:31,4:32}` and `{1:1,2:15,4:48}` |
| `--red-field` | replace the `F4` `40:24` split by one size-64 class | `F4/G5` | actual class sizes `[40,24]` |
| `--red-square` | assert `2Q` instead of `Q` in the square law | `Z8/G2` | first witness `(t,v)=(0,9)` for `beta0` |
| `--red-model-sign` | use `Z(+b)X(a)` in the fixed mixed-characteristic model | `Z4/G6` | Weyl relation fails at operator pair `(4,1)` |
| `--red-frobenius-blind` | claim one generating character at the probe | non-Frobenius `G8` | `Gen=0`; kernel-ideal distribution `{2:6,4:1}` |

All nine modes exited `1`, and each first failure was its pre-registered gate.
In particular:

- transpose is not a field-characteristic-2 mutation: there `-omega=omega`.
  Targeting `Z4` makes the mixed-characteristic sign visible;
- the half-Weyl mode fails because `2` has no inverse, whereas the FCR-1 odd
  mode could form a half and instead failed a wrong coboundary coefficient;
- the plus-sign model mode is likewise invisible over the equal-characteristic
  seeds and therefore targets `Z4`;
- fake epsilon changes only the reported value, while collapse changes only an
  equivalence-class claim, so the two central FCR-2 hypotheses are attacked
  independently.

## Internal decoration audit

The gate-level matrix is complete, but a reached gate contains additional
branches.  Branches not falsified by one of the nine executable modes are
decorations.  The concrete mutation named here is the one that would reach
each decoration; none is presented as current red evidence.

| unreached branch | named decoration mutation |
|---|---|
| A0 cyclotomic order and `x^4+1` reduction | `--red-zeta-order`: identify `zeta8^4` with `+1` |
| A0 ring associativity/distributivity/locality | `--red-ring-entry`: change one multiplication-table entry |
| G1 full torsor distinctness / bilinear coefficient expansion | `--red-adm-duplicate`: duplicate one coefficient triple |
| G1 the `2 beta-omega` correction independent of admission | `--red-field-polarization`: drop `2 beta` at `Z4` |
| G2 quotient component `2v` | `--red-square-field`: claim the field simplification `2v=0` at `Z8` |
| G3 abstract-versus-centre pseudo-isometry equation | `--red-centre-scale`: admit a noncompatible centre map `h` |
| G3 class-size sum `=|Adm|` | `--red-class-drop`: omit one beta from its orbit |
| G3 power-map distribution | `--red-power-bin`: move one lift between central-power bins |
| G3 centre/quotient order profiles | `--red-quotient-order`: call an order-8 quotient element order 4 |
| G4 exact divisibility by `|R|` | `--red-gauss-drop`: omit one phase before normalization |
| G4 all-generating-character coverage | `--red-psi-delete`: omit one unit-scaled character |
| G4 class-constancy report | `--red-epsilon-swap`: attach one computed value to the wrong beta class |
| G5 `#{Q=0}={1,2q-1}` | `--red-zero-count`: alter the anisotropic zero fixture |
| G5 `epsilon={+1,-1}` independently of sizes | `--red-field-sign`: force both field signs positive |
| G6 trace-Gram off-diagonal zeros | `--red-gram-entry`: add one phase to one monomial row |
| G6 every generating character | `--red-model-psi`: substitute a non-generating character at `Z4` |
| G7 direct coefficient antisymmetry census | `--red-anti-fixture`: claim `(0,0,0)` is antisymmetric |
| G8 character additivity and ideal closure | `--red-point-kernel`: use the pointwise kernel instead of its ideal core |

These decorations are explicitly excluded from the `F` matrix.  No two of the
nine implemented red modes mutate the same datum or produce the same observed
failure signature.
