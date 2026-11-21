# Test report — TOEIC Dictionary v2.95.22

## Scope
- Baseline v2.95.21; added deterministic frequency-ranked related-term backlog reporting.
- No learning UI/runtime, vocabulary content, learner state, storage schema or relationship data changed.
## Checks
- Related glossary backlog: 2/2 PASS.
- Batch 027 regression: 5/5 PASS.
- CI coverage: 3/3 PASS.
- JavaScript suites: 38/38 PASS.
- Python syntax compile for new generator/test: PASS.
- Vocabulary validator: 1,141 records; 0 errors, 0 warnings.
- Learning content validator: 0 errors, 0 warnings.
- Repository integrity: 395 references/data files; 0 errors, 0 optional warnings.
- Version synchronization: PASS.
## Generated backlog
- Glossary: 423 entries.
- Unglossed terms: 392 unique.
- Unglossed occurrences: 393.
- Report JSON and Markdown are generated under `docs/reports/` from canonical vocabulary letter files only.
## Limitations
- Full Python test discovery not run.
- Remote GitHub Actions, Pages deployment, browser/device acceptance and owner manual acceptance not claimed.
- New tooling only; no new glossary entries were added and independent review remains necessary.
