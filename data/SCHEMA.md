# data/SCHEMA.md - CSV Column Reference

Generated CSVs live under `runs/<YYYY-MM-DD>-<slug>/data/`; this file records
their schemas.

No CSV outputs exist yet.

## Common Rules

- A row whose first column begins with `#` is a sentinel comment line and must
  be skipped by parsers.
- Exact values should be represented as strings in `_exact` columns.
- Floating approximations should be represented in `_float` columns.
- Residual columns must document norm, denominator, precision, and tolerance.

## CSV Schemas

| CSV path | Producing script | Status |
|---|---|---|
| _none yet_ | _none_ | Initial scaffold only. |
