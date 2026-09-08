# Independent finite checker result

2026-09-08: **PASS**, 263857 exact assertions in the final green run.
All **20 named mutations** ran in actual subprocesses before that green run;
each exited 1 at its preregistered mathematical gate. The green exited 0.
The default `--red` aliases `frob-one-label`; every mutation also has a
`--red-NAME` option advertised to `scripts/session-close.sh`.

Frozen standalone SHA256:
`946ca4584424329e85b92107664d24c89942f194de42dd0737ddc372d77d8c12`.
`RESULTS.json` contains the actual exit codes, first-failure diagnostics,
assertion counts, and all finite example data. No tolerance or floating point
was used. The only third-party dependency is numpy, used with int64 values
reduced modulo 2 or 3. The arithmetic helper is original to this lane and is
bundled into the installation file.

Root inspection caught an exit-status defect in the initial checker:
`main()` forced exit 1 whenever a mutation flag was present, even if the
mathematical result were PASS. This is repaired: exit status now depends
only on the reported mathematical result. All then-existing 19 mutations were
rerun and still fail at their intended gates. A temporary copy with only
the A1-symplectic rejection disabled reports **PASS and exit 0** under
`--red-frob-one-label`, demonstrating that a surviving mutation is exposed.
The temporary copy was removed; no disabling option ships in the checker.
The sentinel result and copy checksum are frozen in `RESULTS.json`.

The final bounded D1327 addition supplies 478 A7-PREP assertions: all 42
computational-basis preparations in the six fields are normalized, the six
hidden basis-bra discard effect sums are identities, and all 430 matrix
units return their ordinary trace. Removing one bra fails A7-PREP. The
exit-status sentinel was rerun successfully with this final checker.

The single formal review repair AC1 removes 756 redundant indexing
comparisons previously described as direct Pauli conjugation. They compared
two notations for the same table entries and supplied no independent
evidence. The surviving A5 computation extracts actual target-Fourier matrix
blocks, applies the all-translation difference filtration, and tests the
separate nonconstant strictness witnesses. Its numerical table below is
unchanged; there is no additional claimed conjugation comparison. All 20
intended mutation subprocesses ran before the final green, and the temporary
disabled-gate sentinel still reports mutated PASS and exit 0.

Model convention: native Codex checker subagent, inherited parent model and
reasoning, no override and no separate CLI invocation. The tool interface
does not expose a more precise inherited model identifier. No prover proof
drafts were read; shared formulas and typed statements arrived by messages.

## Finite coverage

| gates | exact finite scope |
|---|---|
| A1 | F2,F3,F4,F8,F9,F16; all trace-symplectic label quadruples, nondegeneracy, all Frobenius Weyl basis actions; all reference-cocycle label pairs at basis inputs 0 and 1 |
| A2 | F2->F4,F8,F16; F3->F9; F4->F16; all annihilator labels, support vectors, exact projector, compressed Weyl labels and momentum quotient fibres |
| A3 | Same embeddings; all trace pairings and Fourier entries, character restriction degree, Frobenius covariance, exact fibre norms; F2->F4->F16 inclusion and trace-fibre tower |
| A4 | Full basis permutation and covariance: d=1..4 for F2,F3; d=1..3 for F4; d=1,2 for F8,F9,F16. Every named embedding intertwines d=1..3 on the full smaller-field basis |
| A5 | Exact target-Fourier matrix blocks and recursive hierarchy certificate: d=1..4 for F2,F3; d=1..3 for F4; coherent d=2 return experiment in all three fields |
| A6 | Every element of F16=F4[b]/(b²+b+a), its Frobenius image, squared Frobenius shear, order-four check and all squared-Frobenius orbits |
| A7 | Basis preparation and ordinary-trace discard in all six fields; J and V for F2->F4; full typed decoder and explicit positive Choi Gram; F2->F4->F16 three-history tower on all 256 matrix units; two independent decoders on all product matrix units, product and entangled states; both Fourier-conjugated branches |

## Hierarchy certificate data

The algorithm first sums the actual Fourier-conjugated permutation blocks
in the exact cyclotomic basis and extracts their diagonal root exponents.
It repeatedly computes the F_p span of **all** translation differences of
the current span. Each layer is an exact linear-algebra calculation on value
tables. A constant final nonzero layer followed by zero is the recursive
diagonal-Pauli quotient certificate. No input polynomial degree, coefficient
fit, or assumed hierarchy label enters that calculation.

| field | d | dimensions of successive difference spaces | observed d-control difference | next trace-dual scalar exponent |
|---|---:|---|---|---:|
| F2 | 1 | 3,1,0 | nonconstant: 0,1 | 1 |
| F2 | 2 | 7,4,1,0 | nonconstant: 0,1 | 1 |
| F2 | 3 | 15,11,5,1,0 | nonconstant: 0,1 | 1 |
| F2 | 4 | 31,26,16,6,1,0 | nonconstant: 0,1 | 1 |
| F3 | 1 | 3,1,0 | nonconstant: 0,1,2 | 2 |
| F3 | 2 | 7,4,1,0 | nonconstant: 0,1,2 | 2 |
| F3 | 3 | 15,11,5,1,0 | nonconstant: 0,1,2 | 2 |
| F3 | 4 | 31,26,16,6,1,0 | nonconstant: 0,1,2 | 2 |
| F4 | 1 | 5,1,0 | nonconstant: 0,1 | 1 |
| F4 | 2 | 13,7,1,0 | nonconstant: 0,1 | 1 |
| F4 | 3 | 29,21,9,1,0 | nonconstant: 0,1 | 1 |

The nonconstant observed d-fold quotient excludes C_d in these samples;
the filtration certifies C_(d+1). The final scalar uses step 1 in F2/F3
and step a in F4, avoiding the vanishing absolute trace of 1 in F4.

## Concrete arithmetic and operational outputs

F16 elements are numbered `a0+4*b0`, with F4 entries `0,1,a,a+1` numbered
`0,1,2,3`. Squaring is the permutation
`[0,1,3,2,6,7,5,4,13,12,14,15,11,10,8,9]`; its square is
`[0,1,2,3,5,4,7,6,10,11,8,9,15,14,13,12]`. The latter has four singleton
orbits and six two-cycles. Thus its ten-dimensional fixed-vector space and
the four-dimensional F4-supported code are distinct computed objects.

For d=2 the coherent return amplitudes are `3/4,5/9,7/16` for F2,F3,F4,
and the probabilities are `9/16,25/81,49/256`.

Both J and V decode instruments have success probabilities `1/2,1,0,1/2`
on the named maximally mixed, code, complement, and coherent states. The
tower retains quantum output dimensions `16,4,2` for first failure, later
failure, and total success. Independent parallel decoding retains the four
ordered tags `ss,sf,fs,ff` with dimensions `4,8,8,16`.

The auxiliary reset example has local output diagonal `[1/2,0,1/2,0]` and
global-reset diagonal `[1/4,1/4,1/4,1/4]`; these are intentionally unequal.
No equality of those reset maps is admitted as independent tensor coherence.

## Limits of this evidence

These finite computations do not prove the all-field/all-d theorem, the
general category presentation, syntactic faithfulness, generic q
specialization, or closure of higher hierarchy levels under composition.
The category equality is supplied by its typed presentation; matrix equality
here is only the independently checked CP realization of concrete examples.
The full scalar Pauli frame is used for hierarchy membership, not a claim
about strict normalization of the finite mu_p phase centre in characteristic
two. Root adjudicates claim admission using the separate proofs and review.
