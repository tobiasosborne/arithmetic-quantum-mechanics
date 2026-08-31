# data/ - placeholder

Generated CSVs should not be written here. They live under
`runs/<YYYY-MM-DD>-<slug>/data/`.

This directory holds `SCHEMA.md`, the per-column reference for generated CSVs.
Every CSV-producing script must update `data/SCHEMA.md` and `INDEX.md` in the
same change that adds or changes its output.
