Lane model: gpt-5.6-sol, reasoning xhigh, codex exec

# FCR-2 prove-lane summary

Candidate registers below describe this prover pass; `PROVED` promotion still
requires the capped hostile review and adjudication.

Verification: the promoted green run passed G1--G8 at all eight seeds; all
nine registered red modes exited `1` at their intended gates.  A separate
exact root-of-unity sum gives anisotropic signs `+1,-1,+1` at
`Z/4,Z/8,Z/16`, confirming the even-length correction beyond the census.

| claim | outcome | sharpest clause |
|---|---|---|
| `FCR2-NOANTI` | PROVED | the full torsor proof uses no half; `2 in m` rules out an antisymmetric point |
| `FCR2-Q` | PROVED | `P_beta=2beta-omega`, with unsimplified group and Weyl square laws |
| `FCR2-ALG0` | PROVED | for `beta_0`, central simplicity, the fixed matrix model, and SvN hold in every residue characteristic |
| `FCR2-CLASS` | PROVED at the closed scope | general explicit centre-fixed isomorphisms within residue-Arf fibres and general fibre sizes; exactly two abstract classes at all eight registered seeds |
| `FCR2-EPS` | PROVED | the finite-quadratic-module bridge is constructed; `epsilon` is actually `+/-1`, character-independent, and class-constant |
| `FCR2-LEVEL` | PROVED | `mu_{2N_R}` always suffices; an exact cyclic-factor criterion decides `mu_{N_R}` |
| `FCR2-REG` | PROVED | field clauses are compared at their current registers; agreement with SKETCH rows is labelled only consistency |

Sharpest result: the census guess “separation iff length at least three or a
field” is false.  For every finite chain ring, `epsilon` separates the two
classes exactly when the chain length is odd; at every even length it is `+1`
on both classes.  For an arbitrary local Frobenius ring the exact criterion is
`C_psi(R)=|m|`, where
`C_psi(R)=sum_{a^2=b^2=0}psi(ab)`; non-separation is `C_psi(R)=|R|`.

Weakest step: abstract non-isomorphism outside the eight registered seeds is
not proved.  The general theorem supplies centre-fixed isomorphisms within
each Arf fibre, while seed separation uses hand-derived element-order profiles.

Open questions for the critic:

1. Can residue Arf be recovered group-theoretically for every finite local
   dyadic ring, giving the missing general abstract converse?
2. Does the norm-surjectivity/oriented-normal-form proof need an extra
   hypothesis when the local Frobenius ring is non-chain?
3. Can `C_psi(R)` be expressed by standard ideal invariants beyond chain
   rings, rather than by its exact square-zero-pair sum?
4. Is the `mu_{N_R}` cyclic-factor criterion independent of decomposition in
   a form useful enough to promote as the canonical notion of phase level?
