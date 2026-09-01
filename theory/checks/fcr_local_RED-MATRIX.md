# FCR-1 red-mutation reachability matrix

Lane model: gpt-5.6-sol, reasoning xhigh, codex exec.

`F` means the gate actually fails when the mutation is run through every gate
at its targeted seed.  `-` means the mutation does not alter that gate's
inputs or claim.  Green behavior is not counted as mutation reachability.

| gate | nongenerating | transpose | Frobenius-blind | free-only | torsor | dim | half-Weyl drop |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| G1 | - | - | F | - | - | - | - |
| G2 | - | F | - | - | - | - | - |
| G3 | - | - | F | - | - | - | - |
| G4 | - | F | - | - | - | - | - |
| G5 | F | - | - | - | - | F | - |
| G6 | decoration | - | - | - | - | - | - |
| G7 | - | - | - | F | - | - | - |
| G8 | - | - | - | - | F | - | - |
| G9 | - | - | - | - | - | - | F |
| G10 | - | F | - | - | - | - | - |
| G11 | decoration | - | - | - | - | - | - |

## Mutation fingerprints

| mode | only mutated datum/claim | observed failing signature |
|---|---|---|
| `--red-nongenerating` | G4/G5's chosen `Z9` character becomes `psi_3` | G5: rank 27 (claimed 81), matrix commutant 3 |
| `--red-transpose` | active `beta_0` table becomes `beta_0^T` | G2 form sign, G4 Weyl cocycle, and G10 fixed regression beta |
| `--red-frobenius-blind` | least-degenerate non-Frobenius character is claimed generating | G1: `|I|=3`; G3: radical size 9 |
| `--red-free-only` | G7 claims the non-free count is zero | G7 exhibits `(3) x (3)` at `Z9` |
| `--red-torsor` | G8 claims `psi_3` generating for nonunit `3 in Z9` | G8 exhibits `I=(3)` |
| `--red-dim` | G5's claimed `F3` Weyl rank is 10 rather than 9 | G5: rank 9, commutant still 1 |
| `--red-halfweyl-drop` | G9 uses `s(v,v)` instead of `s(v,v)/2` | G9 coboundary fails already for `s=(0,0,1)` |

Thus no two red modes are bit-identical in effect.  In particular, the two G5
modes differ in both mutated state and output: one changes the character and
causes `(rank,commutant)=(27,3)`, while the other changes only the claimed rank
and leaves `(rank,commutant)=(9,1)`.

## Decorations required by E4

- **G6 decoration.** The registered non-generating mutation is valid input to
  G6, so G6 must pass it; it is an error only in G5's generating pipeline.  A
  mutation `--red-g6-arena-confusion` claiming that the *formal* Weyl
  commutant has the matrix-image dimension 3 would reach G6: its exhaustive
  central-label census gives 9.
- **G11 decoration.** The brief declares the profiles to be recorded data and
  permits only internal consistency assertions.  A mutation
  `--red-profile-drop-identity` omitting `(0,0)` from the powering census would
  reach it through both `identity count != 1` and `sum != |R|^3`.

G3, G4, and G10 are secondary firings: their mutations first fire G1 or G2,
but the red driver deliberately continues through the targeted seed so their
reachability is observed rather than inferred.

## Internal sub-check decoration audit (E4)

Reaching a gate does not automatically reach every assertion inside it.  The
following internal branches have no registered mutation and are therefore
decoration, with a concrete mutation that would make each fail.  Sub-checks
not listed here are reached by the gate-level matrix above.

| gate branch not reached by a registered mode | decoration mutation that would reach it |
|---|---|
| G1 additive-character count/distinctness | `--red-character-duplicate`: duplicate one parameter table |
| G1 ideal closure and maximal kernel core | `--red-point-kernel`: use `ker(psi)` itself as `I_psi` |
| G1 unit-orbit set equality | `--red-unit-delete`: omit one unit-scaled character |
| G2 alternation | `--red-form-diagonal`: add `aa'` to `omega` |
| G2 R-bilinearity | `--red-form-nonlinear`: add `a^2 a'` |
| G2 R-nondegeneracy | `--red-form-zero-row`: zero the row and column of `e1` |
| G3 core equality in both directions | `--red-radical-delete`: delete one label from the claimed `I_psi^2` |
| G4 commutation identity (transpose changes only the claimed Weyl cocycle) | `--red-comm-sign`: use `psi(-omega)` |
| G4 fixed Schrödinger sign independent of beta | `--red-model-sign`: use `Z(b)X(a)` |
| G5 disjoint-support premise | `--red-support-collision`: give two shifts the same permutation support |
| G6 formal-vs-matrix arena | `--red-g6-arena-confusion`, described above |
| G7 full submodule enumeration/histogram | `--red-submodule-drop`: omit the socle submodule |
| G7 dual-size identity | `--red-perp-drop`: remove one element from a computed perpendicular |
| G7 common Lagrangian size | `--red-lagrangian-extra`: admit a merely isotropic size-3 module |
| G8 unit characters are generating and distinct | `--red-unit-collapse`: duplicate two unit-scaled tables |
| G9 `2` is a unit | `--red-two-nonunit`: delete its inverse from the table lookup |
| G9 `|Adm|=q^3` and admission | `--red-adm-drop`: omit one symmetric coefficient triple |
| G9 unique antisymmetric member | `--red-half-plus`: claim `omega/2+s` for nonzero antisymmetric `s` |
| G10 count, line, rank, profile fixtures | `--red-regression-count`: alter the fixed `F3` line count |
| G10 literal model fixture | `--red-regression-matrix`: change one fixed phase exponent |
| G11 internal profile consistency | `--red-profile-drop-identity`, described above |
