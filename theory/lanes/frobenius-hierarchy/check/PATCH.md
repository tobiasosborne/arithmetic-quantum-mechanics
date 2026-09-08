# Checker installation proposal

Only root applies these edits. This lane has not changed trunk or git state.

1. Create `theory/checks/frobenius_hierarchy_check.py` by copying the exact
   bytes of `standalone_frobenius_hierarchy_check.py` from this directory.
   It is fully standalone; do not install the development helper modules or
   builder/freezer scripts under `theory/checks/`. The session-close recursive
   discovery intentionally runs every Python file there as a checker.
2. Preserve `EXPECTATIONS.md`, `RESULTS.md`, and `RESULTS.json` as independent
   campaign evidence, here or at a root-chosen durable checker-results path.
   The JSON pins the checksum of the exact standalone file to install.
3. At the proposed FRB and FRP claim-row anchors, use
   `theory/checks/frobenius_hierarchy_check.py` followed by the actual A-gate
   identifiers as the finite tested-in locator. A1--A6 target the arithmetic
   claims; A7-CP/A7-types/A7-tower/A7-parallel/A7-Fourier target concrete
   operational realizations. A7-boundary is an auxiliary reset counterexample.
   No finite pass upgrades a proof status on its own.
4. No edit to `scripts/session-close.sh` is required: each of the 20
   mutations has an advertised `--red-NAME` alias; plain `--red` also fails.

Reproduce in the lane:

```sh
python3 theory/lanes/frobenius-hierarchy/check/bundle_checker.py
python3 theory/lanes/frobenius-hierarchy/check/freeze_campaign.py
```

The freezer executes every named mutation as an actual subprocess before
the green subprocess, requiring its named mathematical gate and nonzero
exit, and writes `RESULTS.json`. The standalone checker itself supports
`--matrix` for a compact internal red-then-green campaign.

The current file includes root's exit-status repair: a mutated PASS exits 0,
so session-close detects any surviving mutation. The freezer additionally
checks this in a temporary copy with the intended gate disabled, records
the PASS/exit-0 sentinel, and removes the copy. Replace any previously
installed standalone file with the version whose SHA256 is
`946ca4584424329e85b92107664d24c89942f194de42dd0737ddc372d77d8c12`.

This final review repair also removes AC1's redundant A5 indexing comparison
and narrows its description to actual Fourier extraction, all-translation
filtration and strictness. The final count is 263857 exact assertions;
the 20 mathematical mutation failures and exit-status sentinel are preserved.
