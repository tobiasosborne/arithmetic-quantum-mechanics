# SP-SUM critic summary

Date: 2026-09-10. Sole blind same-family critic:
`gpt-5.6-sol`, reasoning `xhigh`.

Verdict: **PASS**, with two minor checker limitations and one scope-register
note. No FATAL or MAJOR mathematical objection survived independent
recomputation.

The canonical proof correctly derives every rectangular matrix unit from
actual preparations, translations, adjoints, and composition; proves the
full rectangular span at all odd primes and ranks including rank zero; and,
conditional on admitted SP-STAB-REL, proves strict enlargement by finite
actual projective rays versus infinitely many rays in `End(H_1)`. Its block
realization handles empty lists and repeated positions, gives the coherent and
tagged dimensions, and proves that the prescribed block projection map is a
CP ordinary-trace-preserving channel exactly for nonempty lists.

Standard and `-O` green runs passed. All nine help-advertised reds exited 1 at
their intended U1--U8 gates. Independent copy mutations exercised basis sign,
block placement, projection support, and trace data; disabled guards produced
the required exit-0 survivors.

The checker should guard the imported 360-ray census before printing that
count, and its projection-loss data should flow through all U7 dephasing
calls. The DAG's stray arithmetic-coefficient-syntax comparison should be
removed or split off because the exact claim and proof deliberately make no
arithmetic-source statement. These points do not reduce the verified SP-SUM
statement.

Status remains SKETCH/draft pending adjudication; this critic pass makes no
promotion.
