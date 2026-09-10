# SUMMARY — SP-STAB-REL source audit

Date: 2026-09-10. Model: `gpt-5.6-sol`, reasoning setting `xhigh`.

The local primary bodies support the odd-prime, modulo-invertible-scalars
**symmetric monoidal** equivalence underlying SP-STAB-REL. They do not directly
supply its canonical dagger clause. SP-CK21's theorem says symmetric monoidal
equivalence; SP-BC24's explicit dagger is time-reversed converse, while D1702
uses bare converse.

This is a comparison obligation rather than a refutation. CK21's row/right
generator matrices convert to the D1703 column action by
`g=(M^(-1))^T`; this recovers the D1703 positive Fourier, negative lower
shear and controlled-add actions exactly. Bare converse then gives inverse
graphs, matching the adjoints of the displayed quantum generators. The proof
must verify the affine phase sign and extend this calculation across a
dagger-closed presentation.

The audit also isolates the target comparison. CK21 generates its quotient
from all Clifford unitaries and `|0>,<0|`; D1704 uses all D1307 `C_2(A)`
unitaries, `delta_0`, adjoints and actual complex scalars before D1705 quotients
by `C^times`. Gross supports the projective Clifford/affine-symplectic part.
Equality of the two Pauli normalizers and the harmlessness of freely adjoining
nonzero scalars still require short explicit lemmas; zero remains a separate
class on both sides.

`AUDIT.md` gives the exact dictionary, locators, dagger/shear witness and six
remaining comparison lemmas. `PATCH.md` contains string-anchored ledger
locator/scope replacements. No trunk, prior lane, proof or checker artifact
was edited or read.
