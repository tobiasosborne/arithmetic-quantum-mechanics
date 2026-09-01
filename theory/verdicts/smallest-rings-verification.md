# Verification of `CLAIMS-TO-VERIFY.md`

Lane model: gpt-5.6-sol, reasoning xhigh, codex exec.

Blind-lane constraint observed: the orchestrator's scratch script was neither
read nor requested.  Evidence is the independently written
`small_rings_catalogue_check.py`, whose green run exits 0 and whose eight
distinct red modes exit 1 at their pre-registered gates.

## Discrepancies found

1. **REFUTED:** §5 says “the two top-stratum representations per ring are
   inequivalent.”  At `F4` there are **three**, one for each nonzero (hence
   generating) additive character.  This also contradicts the report's own
   earlier data and sum-of-squares tables.  The corrected sentence is: two for
   each non-field order-4 ring, three for `F4`.
2. **REFUTED as a numerical-catalogue claim:** §5 says the three order-4 rings
   give “three different catalogues.”  The explicit dimension/multiplicity
   catalogue in §3 is identical for `Z4` and `F2[e]/e2`:
   `16 x dim 1`, `4 x dim 2`, `2 x dim 4`.  There are only two distinct
   numerical catalogues among the three rings.  A richer catalogue retaining
   the central-character group could distinguish the two, but the report does
   not define that stronger meaning there.
3. **OVERSTATED / NOT-CHECKED:** “complete invariant of the collapse geometry”
   is not established by five examples or by the class/square closure.  The
   census confirms the displayed annihilator strata, not a completeness
   theorem for an undefined class of collapse geometries.

The phrase “8 distinct scaled Weyl images” is potentially ambiguous.  Both
thickened rings have 8 distinct Weyl matrices and 8 projective Weyl classes;
the full Heisenberg group image, after central scalars are included, has 16
matrices.  Thus the stated 8 is confirmed for the 16 Weyl labels, not for the
full group image.

## Per-claim verdicts

Rows group only statements supported by the same exhaustive calculation.
Together they cover every numerical table, formula, count, dimension,
multiplicity, and finite identification in the report.

| id | report claim | verdict | independent result / gate |
|---|---|---|---|
| V01 | The listed objects are exactly all local rings at the three smallest orders, with a three-way tie at order 4. | **NOT-CHECKED** | A0 validates all five listed local-ring tables, but does not enumerate isomorphism classes of all rings of order at most 4. |
| V02 | The §1 table: maximal ideals, residue fields, socles, units, `|Gen|=(1,2,3,2,2)`, `|Adm|=(8,27,64,64,64)`, and only F3 has `omega/2`. | **CONFIRMED** | C1: `|soc|=(2,3,4,2,2)`, `|R^x|=|Gen|=(1,2,3,2,2)`; all characters and all admissible coefficient triples exhausted. |
| V03 | All five are Frobenius; `Gen` is the free unit orbit; the five displayed reference characters generate. | **CONFIRMED** | C1 computes every `I_psi`, compares the unit orbit as a set with `Gen`, and checks each reference character has `I_psi=0`. |
| V04 | `H_beta0(R) ~= UT_3(R)` and the cocycle is associative with central term `t+t'+ab'`. | **CONFIRMED** | C2 checks the cocycle on every triple and the coordinate product on every ordered group pair. |
| V05 | The complete §2 group table: orders 8/27/64/64/64, displayed centres, exponents 4/3/4/8/4, and all five order profiles/identifications. | **CONFIRMED** | C3 brute-force powers every element and exhausts the centre.  It supplies a D4 presentation at F2 and the exponent-3 extraspecial invariants at F3. |
| V06 | The three order-64 groups are pairwise non-isomorphic by cyclic centre/order 8 and 27 versus 31 involutions. | **CONFIRMED** | C3 compares `(centre profile, exponent, full order profile)` and obtains three distinct signatures. |
| V07 | In `H(Z4)`, order 8 occurs exactly when `ab` is odd, giving 16 elements; equal-characteristic doubling prevents order 8 for the dual numbers. | **CONFIRMED** | C3 checks the iff element by element: 4 eligible vectors times 4 values of `t`; it also checks `2v=0` for the dual ring. |
| V08 | Beta dependence: F3 has 27 transported presentations; F2 splits 6:2 into D4/Q8 profiles; F4 has two profile types. | **CONFIRMED** | C2 checks all 27 F3 coboundaries.  C3 discovers F2 frequencies 6/2 and F4 frequencies 40/24 with two distinct profiles. |
| V09 | `[H,H]=R x 0`, `H^ab ~= V`, and the class counts `(5,11,19,22,22)` equal `n^2+sum_{u!=0}|Ann(u)|^2`. | **CONFIRMED** | C4 checks every commutator, constructs every conjugacy orbit, and evaluates the annihilator identity independently. |
| V10 | For each `u`, there are `|Ann(u)|^2` irreps of dimension `n/|Ann(u)|`; the number of rows equals the class count and their squares sum to `|H|`. | **CONFIRMED** | C6 evaluates every `u`; class closure is `(5,11,19,22,22)` and square closure is `(8,27,64,64,64)`. |
| V11 | Bottom stratum: `n^2` one-dimensional characters, centre trivial. | **CONFIRMED** | C6 exhausts all pairs of additive characters of `R`, checks their homomorphism law on `V`, and gets 4/9/16/16/16. |
| V12 | Top stratum: one irreducible of dimension `n` for every unit-scaled generating character; exact trace-Gram orthogonality makes the `n^2` Weyl operators span `M_n(C)`. | **CONFIRMED** | C5 checks every generating character, not only one reference: Gram=`n I_(n^2)` in exact cyclotomic arithmetic and commutant dimension 1. |
| V13 | The named qubit/qutrit/F4 two-qubit/ququart/dual-number clock-shift fingerprints and top multiplicities `1,2,3,2,2`. | **CONFIRMED** | C5 checks the Pauli image order 8, `ZX=psi(1)XZ`, two independent F4 shifts, and the Z4 phase row `(0,1,2,3)`; C6 supplies the multiplicities. |
| V14 | Middle stratum at `u=2,e`: `I=Ann(u)=m`, radical `I+I`, four inequivalent 2-dimensional irreps in total, and 8 Weyl images. | **CONFIRMED** | C7 exhausts the radical and obtains 8 exact/8 projective Weyl images; C6/C7 construct and exhaust four radical-character classes. |
| V15 | Requested extension: decomposition of the 4-dimensional middle model. | **CONFIRMED** | At both rings C7 finds `2+2`: two inequivalent 2-dimensional blocks, multiplicity one each, with radical signs `(+,+)` and `(-,+)`.  Thus the model contains 2 of the 4 total classes. |
| V16 | Fields have no middle stratum; among these five, being thickened is equivalent to having dimensions strictly between 1 and `n`. | **CONFIRMED** | C6 has no intermediate dimensions for F2/F3/F4 and has four dimension-2 classes for each non-field ring. |
| V17 | The five sum-of-squares rows in §3. | **CONFIRMED** | C6 obtains `4+4=8`, `9+18=27`, `16+48=64`, and twice `16+16+32=64`. |
| V18 | Lagrangian totals/free/non-free are `3/3/0,4/4/0,5/5/0,7/6/1,7/6/1`; the non-free witnesses are `(2)+(2)` and `(e)+(e)`. | **CONFIRMED** | C8 discovers every submodule by closure, recomputes every perpendicular, and identifies each unique witness. |
| V19 | Model-label counts are `6,12,20,28,28`, with `n` characters for every `A_L`. | **CONFIRMED** | C8 exhausts all algebra-character phase assignments in roots allowed by the group exponent; each Lagrangian has exactly `n`. |
| V20 | All 28 labels at each thickened ring are induced presentations of one isomorphism class. | **NOT-CHECKED** | The checker counts all labels and proves the reference Weyl image is `M_4(C)`, but does not explicitly construct and compare all 28 induced modules. |
| V21 | §5: “two top-stratum representations per ring.” | **REFUTED** | C1/C6 give 3 at F4; the corrected order-4 counts are `3,2,2`. |
| V22 | §5: the three order-4 rings have three different representation catalogues. | **REFUTED** | In the report's displayed dimension/multiplicity sense, Z4 and the dual numbers have the same catalogue; only their group/ring labels distinguish them. |
| V23 | The catalogue is a complete invariant of collapse geometry. | **NOT-CHECKED** | No definition or comparison class for “collapse geometry” is supplied; the finite census establishes only the five displayed cases. |
| V24 | Numerical physics fingerprints: F4 is 4-dimensional with exponent 4 and no middle stratum; Z4 is 4-dimensional with a fourth-root clock and 16 order-8 elements; the dual ring is 4-dimensional, exponent 4, with a middle stratum. | **CONFIRMED** | C3, C5, C6, and C7 give exactly these finite invariants. |

Verdict count: **19 CONFIRMED / 2 REFUTED / 3 NOT-CHECKED** (24 rows).
