# Test Report — TOEIC Dictionary v2.95.23

## Scope

Backlog reporting improvement only. Missing related-term glossary entries now carry source-headword traceability, headword breadth, and synonym/antonym counts for editorial prioritization. No new glossary meanings were created.

## Checks

- Related glossary backlog tests: **3/3 PASS**.
- Batch 027 provenance regression: **5/5 PASS**.
- Version synchronization tests: **12/12 PASS**.
- Repository integrity test: **1/1 PASS**.
- Total focused Python tests: **21/21 PASS**.
- Robot Buddy Node regression: **PASS** (library/routing/insights/privacy and safeguards).
- Generated backlog totals: **423 glosses; 392 distinct unglossed terms; 393 missing reference occurrences** (unchanged).
- Queue now includes source headword anchors and reference-type breakdown. Example: `disorganize` has 2 antonym references from `arrange` and `organize`.

## Not run / not claimed

Full Python and JavaScript suites, full validator sweep, remote GitHub Actions, Pages deployment, browser/device QA, acoustic testing and independent lexical review were not run in this focused pass.

## Manual smoke test

1. Open `docs/reports/RELATED_GLOSSARY_BACKLOG.md` and confirm the table now includes Headwords, Synonym, Antonym and Source headwords.
2. Check `disorganize`: 2 references, 2 source headwords, 0 synonym and 2 antonym references (`arrange`, `organize`).
3. Open JSON and confirm schemaVersion 2 with `sourceHeadwords` and counts.
4. Confirm vocabulary terms, definitions and application UI remain unchanged.

## Master update

`docs/MASTER_STATUS.md`, `docs/CHANGELOG.md`, `docs/versions/CURRENT_VERSION.md`, `docs/versions/PREVIOUS_VERSION.md`, and `docs/README.md` updated for v2.95.23.
