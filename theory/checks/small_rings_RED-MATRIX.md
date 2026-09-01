# Small-rings checker red-mutation matrix

Lane model: gpt-5.6-sol, reasoning xhigh, codex exec.

`F` is an observed gate failure at the pre-registered target.  `-` means the
mutation does not alter the gate's datum or expected claim.  All eight red
modes exit 1.  Green exits 0.

| gate | ring soc | transpose cocycle | order profile | class count | Gram | catalogue | middle images | drop non-free |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| A0 | - | - | - | - | - | - | - | - |
| C1 | F | - | - | - | - | - | - | - |
| C2 | - | F | - | - | - | - | - | - |
| C3 | - | - | F | - | - | - | - | - |
| C4 | - | - | - | F | - | - | - | - |
| C5 | - | - | - | - | F | - | - | - |
| C6 | - | - | - | - | - | F | - | - |
| C7 | - | - | - | - | - | - | F | - |
| C8 | - | - | - | - | - | - | - | F |

A0 is explicitly named decoration: it checks the exact cyclotomic quotient
and finite-ring table axioms as preconditions.  It makes no catalogue claim.
Every evidence gate C1--C8 is reached by a distinct registered mutation.

## Mutation fingerprints

| mode | sole mutated datum/claim | observed first failure |
|---|---|---|
| `--red-ring-soc` | claim `|soc(F2)|=1` | C1 computes 2 and lists both elements |
| `--red-transpose-cocycle` | use `beta0^T` with the unchanged `UT3` coordinate map | C2 finds the first product mismatch at `g=1,h=2` |
| `--red-order-profile` | change the claimed F4 involutions from 27 to 26 | C3 returns the exhaustive profile `1:1,2:27,4:36` |
| `--red-class-count` | change the Z4 identity result from 22 to 23 | C4 independently constructs 22 conjugacy orbits |
| `--red-gram` | claim `Gram[0,1]=1` at F3 | C5 obtains exact cyclotomic zero `(0,0)` |
| `--red-catalogue` | claim five middle irreps at `F2[e]/e2` | C6 obtains the `16,4,2` stratum counts |
| `--red-middle-images` | claim seven Z4 middle Weyl images | C7 obtains 8 exact and 8 projective images |
| `--red-drop-nonfree` | replace `7/6/1` by `7/7/0` | C8 exhibits the unique `(e)+(e)` witness |

## Gate scope

- C1: ring data, exhaustive characters, generating orbit, all admissible forms.
- C2: cocycle identity, `UT3` orientation, and all F3 beta transports.
- C3: centre, exponent, profiles, D4/extraspecial witnesses, non-isomorphism.
- C4: commutators, abelianization, conjugacy orbits, annihilator identity.
- C5: exact trace-Gram, commutant, spanning, and named clock/shift fingerprints.
- C6: bottom-character census, every annihilator row, class and square closure.
- C7: middle radical, image count, block decomposition and radical characters.
- C8: full submodule/Lagrangian census and exhaustive `A_L` character counts.
