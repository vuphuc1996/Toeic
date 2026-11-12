# Test Report — TOEIC Dictionary v2.19.0

Date: 2026-11-11  
Status: local release candidate; not pushed/deployed by the assistant.

## Test accounting

| Suite | Methods | Result | Execution note |
|---|---:|---|---|
| Fast and feature/editorial suites from v2.18.0 | 102 | PASS | Executed per suite; includes data baseline, patching, choice identity/history, layout, evidence, distractors, learning content, dashboard and runtime detail scope. |
| Remaining-content review registry | 5 | PASS | Exact 148-item coverage, Part distribution, source fingerprints, key/choice/choice-ID/explanation integrity and conservative review decisions. |
| Version synchronization | 12 | PASS | Full suite completed in one run. |
| Vocabulary validator regression suite | 33 | PASS | Grouped run hit sandbox execution limit; all 33 test methods were run individually in two batches. |
| **Total** | **152** | **152/152 PASS** | No single monolithic test-discovery PASS is claimed. |

## Validators and audits

- `python tools/validate-data.py`: **PASS**, 928 vocabulary records, 0 errors, 12 known legacy warnings (DF005=3, EX006=1, FD001=8); 0 added/missing IDs against baseline. ID-set SHA-256 prefix `dd1705e64c8df4ad`.
- `python tools/validate-learning-content.py`: **PASS**, Listening 56 units/102 questions (P1=8, P2=25, P3=39, P4=30); Reading 35 resources/109 questions (P5=30, P6=16, P7=63); Grammar 25 lessons/54 exercises; 0 errors, 0 warnings.
- Editorial evidence audit: 211 questions indexed and source-mapped across the documented evidence categories.
- Distractor audit: 132 Part 3/4/7 questions; 12 earlier option groups improved; answer-position totals remain P3 A10/B10/C10/D9, P4 A8/B8/C7/D7, P7 A16/B16/C16/D15. Structural key/choice checks PASS.
- New editorial inventory: 148 non-Part-7 question locators (Listening P1–P4=102; Reading P5–P6=46); 5/5 registry regression tests PASS. Source fingerprints tie the review record to the exact two JSON snapshots.
- `python tools/sync-version.py --check`: **PASS**, manifest, Service Worker, HTML title/sidebar/phase/footer, README and Master all 2.19.0; CHANGELOG contains v2.19.0.

## Runtime, syntax and deployment structure

- `node tools/tests/runtime-render-smoke.mjs`: **PASS** for Reading, Listening and Grammar render/migration smoke, archived options, stable choice IDs, stale-index history rendering and idempotency.
- `python -m py_compile tools/*.py tools/tests/*.py`: **PASS**.
- `node --check sw.js` and all `assets/js/*.js`: **PASS**.
- GitHub Actions workflow YAML parse: **PASS**, one validation job and 25 steps; the new `remaining_content_review` test is included.
- Sidebar source regression: independent scroll in `.side-nav`; `.sidebar-bottom` remains non-shrinking and pinned for desktop. Tests cover short laptop heights and status-footer presence. **Real-browser visual confirmation at 100% zoom on a 15.6-inch laptop remains pending.**
- Service Worker app shell: **74/74** listed resources exist in the package root. Sidebar text strings and footer visibility are covered by the desktop layout regression suite.
- Final ZIP: **198 files**, `ZipFile.testzip()` CRC **PASS**, fresh extraction exact comparison **198/198 PASS**. SHA-256 is provided in the `.zip.sha256` sidecar beside the ZIP. Freshly extracted package re-ran vocabulary/learning validators, version sync and runtime render/migration smoke successfully.

## Content and data preservation

- Batch 009 second-pass review covers 148 questions outside Part 7. Together with the 63 Part 7 questions re-reviewed in v2.18.0, internal second-pass coverage totals 211/211 Listening/Reading questions. This is an internal editorial pass, not external teacher/psychometric/ETS certification.
- No answer key, `answerIndex`, question/option text, `choiceIds`, question order or question counts were changed in Batch 009. No vocabulary record or stable ID changed.
- No IndexedDB database version/object-store/schema change or progress reset.
- **Per user request, no personal IndexedDB import/export/migration test was performed.** Development uses the default local profile; no personal profile was read, imported, exported, reset or modified.

## Commands to reproduce key checks

```bash
python tools/validate-data.py
python tools/validate-learning-content.py
python tools/audit-question-evidence.py
python tools/audit-distractors.py
python tools/audit-toeic-coverage.py
python tools/sync-version.py --check
node tools/tests/runtime-render-smoke.mjs
python -m unittest discover -s tools/tests -p 'test_remaining_content_review.py' -v
```

The full unit suite is split by module. `test_validator.py` should be run by individual methods in a constrained sandbox; all 33 methods were confirmed PASS that way in this release.

## Not verified

- No assistant commit/push to `vuphuc1996/Toeic`; user stated v2.17.0 is currently uploaded to GitHub. The v2.19.0 ZIP is a local package for the user's next update.
- No remote GitHub Actions run or GitHub Pages deployment was performed/verified.
- No real browser screenshot/interaction or physical-device test at 100% zoom; CSS tests do not replace visual QA.
- iPhone Safari, Android Chrome, iPadOS Safari, PWA install/offline and physical desktop QA remain pending.
- Personal IndexedDB import/export/migration QA remains explicitly deferred.
