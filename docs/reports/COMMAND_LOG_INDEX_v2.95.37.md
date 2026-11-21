# Command Log Index — v2.95.37


## Content batch
- `tools/content-batch-027-v2.95.37.json`: 16 Listening resources / 32 questions.
- Canonical listening library updated; each question has a transcript evidence pointer and unique choice IDs.
- Added batch tests and CI registration; linked all new resources in `objective-resource-map.json`.

## Validation and audits
- `python tools/validate-data.py` — PASS (1,141 vocabulary records; 0 errors / 0 warnings).
- `python tools/validate-learning-content.py` — PASS (145 Listening units / 295 questions; 0 errors / 0 warnings).
- `python tools/audit-objective-resources.py` — PASS (379/379).
- `python tools/audit-repository-integrity.py` — PASS (407 references; 0 errors / 0 optional warnings).
- `python tools/audit-question-evidence.py` — PASS (582 indexed; 193 pending Listening reserve).
- `python tools/audit-listening-readiness.py` — PASS (102 eligible / 193 pending / 295 total).
- `python tools/audit-distractors.py` — PASS (264 questions in scope; 156 reserve structural checks).
- `python tools/audit-major-release.py` — regenerated version-aware current reports.
- `python tools/report-project-progress.py` — regenerated current project snapshot.
- `python tools/sync-version.py --check` — PASS.

## Tests
- 121 focused Python tests PASS across 15 suites.
- 39/39 JavaScript `.mjs` regression suites PASS.
- Full Python discovery, remote CI, Pages deployment and physical-device QA were not run.
## Package verification — v2.95.37

- FullSource: **556 files**.
- Update Patch: **35 entries** (22 changed + 13 added), **0 deletions**.
- Patch replay on v2.95.36: **556/556 files byte-for-byte identical** to v2.95.37 FullSource.
- ZIP CRC, one-root structure, excluded-path policy and SHA-256 verification: PASS.

