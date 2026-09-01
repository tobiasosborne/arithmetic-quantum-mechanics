<!-- ROLE: live state. UPDATE POLICY: every session end and every phase
     boundary. Not an authoritative source for mathematics — that is
     definitions.md, claims/CLAIMS.md, and theory/. -->

# HANDOFF — live state

Updated: 2026-08-31, session 1 (the reboot session).

Read order gate: `CLAUDE.md` -> **`PRD.md` (the constitution; where it conflicts
with anything recorded here, PRD wins)** -> this file.

## Where the campaign is

Session 1 rebooted the repository and completed the first increment end to end.
The previous lab book is frozen under `v0.1/` and is a source of hints only
(L12): nothing in the trunk was copied from it.

North star: a general definition and workflow assigning canonical quantum
systems -- Hilbert space, observable algebra, and where possible dynamics as
automorphisms or projective unitary representations of symmetry groups, with
fusion categories as the expected general endpoint -- to arbitrary arithmetic
schemes. Guiding path: `F_p` and its canonical symplectic space `F_p x F_p`.
Product: `labbook/main.pdf`.

## The first increment, closed

`Spec κ` for a finite field `κ`. One full capped loop ran: prove -> one hostile
round -> one repair wave -> mechanical adjudication
(`theory/verdicts/wh-kappa-adjudication.md`). The extra round that a FATAL on a
headline claim would have bought was deliberately not spent.

**The result.** The quantum system attached to a finite field is determined by
three data, not two: the field, a choice of additive character `ψ`, and a choice
of polarizing cocycle `β ∈ Adm(ω)`. The third was hidden inside what the work
order called a convention. It is vacuous at odd `p`, where `ω/2` is the unique
antisymmetric admissible cocycle and hence canonical. It is real at `p = 2`,
where the admissible cocycles fall into two isomorphism types -- at `q = 2`, six
give `D_4` and two give `Q_8` -- separated by `Arf(Q_β)` for the quadratic form
`Q_β(v) = β(v,v)`. Three independent computations agree on this.

Two further canonicity findings: the trace character admits **no** sections along
field embeddings (`WH-FUNCT-b-SEC`, REFUTED; it fails first at `F_2 ⊂ F_4`), so
there is no functor on finite fields with embeddings, only on pairs `(κ,ψ)`;
and `κ`-linearity is imposed data the algebra does not carry, its intrinsic
symmetry group being the larger `Sp_{2m}(F_p)` (`WH-SYMM`).

**State:** 28 rows -- 22 PROVED, 4 SKETCH, 1 CONJECTURE, 1 REFUTED. D1-D11 in
`definitions.md`, 35 symbols in `notation.md`, a 37-page labbook in lockstep,
ten sources registered in `refs/LEDGER.md` with zero gaps.

**The four SKETCH rows are procedural, not evidential.** They are the statements
written in the repair wave (the Arf classification, the Gauss-sign identity, the
level statement, `β`-independence of the projective model space). Each has a
complete proof and exhaustive finite verification; none has faced a hostile
round. One hostile round on `theory/wh-kappa-choice.md` would settle them.

## Next useful steps

1. One hostile round on `theory/wh-kappa-choice.md` to move the four procedural
   SKETCH rows, if they are wanted at PROVED. This is a round, not research.
2. The next increment of the definition: an arbitrary affine scheme of finite
   type over `F_q`, by closed points, tested against the seed case first. The
   open question the seed case raises is what plays the role of `β` there --
   whether a polarizing cocycle must be chosen point by point, and what glues.
3. `theory/wh-kappa-choice.md` is 503 lines against L2's 500 cap. Trim at the
   next edit.
4. The RED-MATRIX decoration inventory still names sub-checks no mutation
   reaches. Checker work, not claim work.
5. `scripts/setup-env.sh` must be run first in any new container: TeX, latexmk
   and numpy are not preinstalled, and `bd` is unavailable.
