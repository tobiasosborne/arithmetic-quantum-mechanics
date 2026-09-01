Lane model: gpt-5.6-sol, reasoning xhigh, codex exec

# Smallest-rings verifier summary

Verdicts: 19 CONFIRMED / 2 REFUTED / 3 NOT-CHECKED (24 rows).

REFUTED: F4 has 3 top-stratum irreps, not “two ... per ring.”

REFUTED as numerical: Z4 and F2[e]/e2 have the same displayed irrep catalogue,
so the three order-4 rings yield only 2 dimension/multiplicity catalogues.

Middle result at both thickened rings: the 4-d model is 2+2, with two
inequivalent 2-d blocks of multiplicity 1; it contains 2 of 4 total classes.

Green observed: `python3 small_rings_catalogue_check.py` -> exit 0.

Observed red exits (all pre-registered gate kills):
`--red-ring-soc` 1; `--red-transpose-cocycle` 1;
`--red-order-profile` 1; `--red-class-count` 1; `--red-gram` 1;
`--red-catalogue` 1; `--red-middle-images` 1; `--red-drop-nonfree` 1.

A0 is named decoration/precondition; every evidence gate C1--C8 is mutation-reached.
