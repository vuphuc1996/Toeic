# Test Report — TOEIC Dictionary v2.95.70

Date: 2026-11-26
Status: **Local source candidate — test suites PASS WITH ONE ACCEPTED SKIP**

## Source of truth

- Sole predecessor: `TOEIC_Dictionary_v2.95.69_FullSource.zip`
- Predecessor SHA-256: `4ec559a2117a1b1b38ef95d4a0d6955431b46e701cf208bd939bd38db232e853`
- Predecessor ZIP: 847 entries; CRC verified before extraction.
- Working source: manifest `2.95.70`. No older FullSource, alternate branch, Patch or extracted stale directory was used as input.

## Implemented behavior under test

1. Assessment completion now exposes one explicit action only: **Xác nhận & xem đáp án**. The post-completion **Quay lại kiểm tra** action, event route, Practice/Foundation return helpers and obsolete draft-saved toast have been removed.
2. Selection-only drafts remain persisted while a learner is answering. Opening the result summary does not delete or migrate draft data. Confirming is the only commit point for progress/evidence and answer reveal.
3. Foundation progress is calculated into a separate `nextProgress`, persisted to the matching localStorage key, then assigned to in-memory committed state. If persistence throws, committed progress remains unchanged and the pending result and staged selections are retained for retry.
4. UI layout, IndexedDB schema, local learner data schema, canonical vocabulary data, question/choice IDs and answer keys were not redesigned or migrated.

## Test results

| Suite | Result |
|---|---:|
| Python inventory | 105/105 modules terminal; 789 cases: 788 PASS, 0 FAIL, 1 accepted SKIP |
| Node CI scripts | 45/45 PASS |
| Focused one-way confirmation Python test | 4/4 PASS |
| Focused distractor quality Python test | 6/6 PASS |
| Focused choice-history Python test | 5/5 PASS |
| Focused practice fallback Python test | 6/6 PASS |
| Single-overlay contract | 3/3 PASS |
| JavaScript syntax (`assets/js/*.js`) | PASS |
| Service Worker syntax | PASS |
| Data validator | 1,141 records; IDs +0/-0; 0 errors, 0 warnings |
| Learning-content validator | 0 errors, 0 warnings |
| Repository integrity preflight | 409 local references/data files; 0 errors, 0 optional warnings |
| Part 1 photo assets | 9/9 valid; 0 missing-photo warnings |
| Design-token audit | 0 new violations; 2,773 known legacy findings remain warnings |
| Version synchronization | 18 release markers, 17 app imports and 42 Service Worker URLs aligned to 2.95.70 |
| Design profile synchronization | 54 tokens and 406 legacy font-floor selector groups synchronized |

### Python skip detail

`tools/tests/test_patch_data.py::PatchDataTests::test_repository_gitignore_excludes_audit_logs` is skipped because a FullSource ZIP does not include `.git` metadata and the assertion requires a Git clone. The other 19 tests in that module passed. This skip is recorded as accepted, not silently converted to PASS.

The complete module-level inventory is in `PYTHON_TEST_SHARDS_v2.95.70.md` and `.json`. It records 105/105 modules, 0 failed, 0 errored, 0 timed out and 0 not run. The heavy `test_validator.py` module completed 44/44 in 67.339 seconds.

## Data preservation

Compared byte-for-byte against a clean extraction of the exact `.69` predecessor:

- `data/`: 68/68 files remain at the same paths. Only `data/manifest.json` differs, and only its `version` value changes from `2.95.69` to `2.95.70`; parsed manifests are identical after normalizing that field.
- 1,141 canonical vocabulary IDs: no additions or removals.
- No vocabulary headword, definition, IPA, relation, or learner-data bank changes.
- No question ID, choice ID, correct-answer key, Mock eligibility or reserve-question changes.
- No IndexedDB schema or learner record migration.

See `DATA_DIFF_v2.95.70.md` for the detailed comparison scope.

## Release acceptance boundary

**Completed:** local source edits, regression suites, validators, data comparison, release documentation, FullSource/Patch construction and exact patch replay.

**Not verified:** hosted GitHub Actions, live GitHub Pages deployment, installed-PWA update/offline propagation, reconnect behavior and physical iPad/iPhone/Android/browser testing. No Git push or production deployment is claimed. This is a locally verified source candidate, not production deployment acceptance.
