# Full Repository Audit — TOEIC Dictionary v2.95.6

## 1. Scope

Full audit of the supplied `TOEIC_Dictionary_v2.95.5_FullSource.zip`: application/runtime modules, imports, Service Worker shell, HTML/CSS references, canonical JSON, aggregate counts, stable IDs, test/CI wiring, release metadata, current documentation and retained historical artifacts.

## 2. Findings and disposition

### Corrected in v2.95.6

- Reconciled `MASTER_STATUS.md`, `README.md`, `COMPATIBILITY.md`, `CHANGELOG.md`, `CURRENT_VERSION.md` and `PREVIOUS_VERSION.md` around one current/previous release ledger.
- Removed contradictory descriptions that treated the retired `learning-assistant.js` progress reader as active. The current Robot Buddy runtime is `robot-buddy.js` + `robot-learning-insights.js` + `data/robot/robot-library.json`; the old `learning-assistant.js` and `quick-help.js` are inert compatibility tombstones, not active modules.
- Consolidated the Master file to current state/backlog and retained chronological release history in `CHANGELOG.md` and retired-document summaries in `archive/PROJECT_HISTORY.md`.
- Rebuilt the current progress snapshot from canonical JSON rather than carrying forward stale v2.95.0 inventory values.
- Updated repository-integrity count in release documentation from the earlier 362 to the current 363 inspected references/data files.
- Retired old version-specific report Markdown through a reference-aware two-generation rotation tool. It preserves historical documents still referenced by tests, tools or current documentation; the v2.92.0 content review checklist and B1 blueprint remain active at their original paths. Canonical data, assets, patch payloads, vocabulary batch provenance and learner storage contracts were not removed.

### No runtime defects found by this audit

- All 17 JavaScript files under `assets/js/` and `sw.js` pass Node syntax checks.
- No duplicate JavaScript function declarations were found in shipped modules.
- All 293 static HTML IDs are unique.
- Every required Service Worker resource exists; every REQUIRED item is in APP_SHELL; optional assets resolve or remain explicitly optional.
- All canonical JSON files parse; objective-resource references resolve 339/339.
- All current runtime modules are either imported by `app.js`/another runtime module or explicitly documented compatibility tombstones. No active imported module was removed.

## 3. Regression and validation results

| Check | Result |
|---|---:|
| JavaScript regression suites | 34/34 PASS |
| Python test modules | 54/54 PASS individually |
| Python test cases | 426 PASS |
| Python `py_compile` | PASS — all tools/tests |
| Node syntax | PASS — 17 app JS modules + `sw.js` |
| Repository integrity | 363 inspected; 0 errors; 0 optional warnings |
| Version synchronization | PASS |
| Canonical design profile | PASS — 54 tokens / 406 selector groups |
| Vocabulary validator | 1,141 records; 0 errors / 0 new warnings against legacy baseline |
| Learning-content validator | 0 errors / 0 warnings |
| Objective-resource audit | 339/339 links; 11 objectives |
| Question-evidence audit | 502 TOEIC questions indexed |
| Distractor structural audit | PASS — 240 questions in audit scope |
| Foundation A2 assessment audit | PASS — Reading 13/13, Listening 13/13; 39 questions each |
| Listening readiness | 102 eligible; 137 pending independent review; 239 total |
| Part 1 image audit | 9/9 JPG assets valid |

All 54 Python modules completed successfully when run individually. A single aggregate `unittest discover` invocation exceeded the available execution window; it is not reported as a completed aggregate run. The CI coverage guard confirms every Python module and JavaScript suite is declared in the GitHub Actions workflow.

## 4. Data consistency and known editorial debt

- Vocabulary manifest total, A–Z file counts and canonical records agree at 1,141. The immutable 928-ID baseline has 213 additive IDs and zero missing IDs.
- Current TOEIC inventory: Grammar 50 lessons / 137 exercises; Listening 121 units / 239 questions; Reading 65 resources / 263 questions; separate Part 5 practice 80 questions.
- Foundation inventory remains separate: 23 lessons; 23 core Reading passages / 59 questions; 23 core Listening clips / 59 questions; 13 supplementary A2 Reading passages / 39 questions and 13 supplementary A2 Listening clips / 39 questions.
- Objective-resource links are complete (339/339), but the separate outcome registry has 33 criteria and only 6 instrumented evidence paths. The remaining 27 are an explicit integration backlog, not a broken resource link.
- Vocabulary validator informational findings: 93 records lack US IPA; 338 of 809 synonym/antonym terms lack explicit glosses; four English definition pairs are identical across related headwords; one word-level/sense-level CEFR difference is present for `package` (word-level B1, senses A2/B1). These are editorial-review items, not silently auto-corrected data.
- The 137 TOEIC Listening reserve questions, Part 7 second-review items, 80 separate Part 5 practice questions and supplementary Foundation A2 content retain their existing review/eligibility boundaries.

## 5. Listening / Reading TTS sequence verification

- Standalone Listening Parts 1–4: Part title → lead-in → audio/dialogue or Part 1 A–D descriptions → questions → answer options. Part 2's spoken segment is the question itself; the generic stored UI prompt is not repeated as a second question.
- Reading Parts 5–7: Part title → instruction → sentence/text/documents → questions → A/B/C/D labels and option text.
- Guided Mock Listening Parts 2–4 honors `skipLeadIn` after the transition has already spoken the Part introduction; it proceeds directly to the audio content.
- Listening Parts 2–4 and Reading Parts 5–7 use the tested 1,000 ms option cadence. Part 1 preserves 1,500 ms after each A–D label and 1,300 ms between descriptions.
- Tests validate queued utterance order and delay calls. Actual audible quality and acoustic timing still require physical-device testing.

## 6. Cleanup decisions

- Retained `data/vocabulary/batch-*.json` as editorial provenance; canonical runtime vocabulary remains A–Z only.
- Retained `patches/` payloads as reproducible, guarded historical changes; they are not runtime imports.
- Retained `learning-assistant.js` and `quick-help.js` as inert compatibility tombstones because GitHub overlay updates may need to overwrite old paths. They are not active modules and remain covered by tests.
- Did not mechanically delete repeated CSS selectors. The app stylesheet uses responsive and component override layers; selector repetition alone does not prove dead CSS. Design profile and responsive tests pass. A future CSS consolidation must preserve cascade order and be browser-verified.
- No duplicate static HTML IDs or duplicate JavaScript function declarations were found.

## 7. Preservation / non-changes

- No vocabulary/question/answer content, stable IDs, learner progress, IndexedDB schema, localStorage keys, Robot library or media assets changed.
- No user-facing layout, menu, visual theme or learning flow changed.
- No migration, learner-data reset, backend/API or external learner-data transfer was introduced.

## 8. External acceptance still required

- Remote GitHub Actions execution and deployed GitHub Pages version/cache are not verifiable from this local archive.
- iPhone/iPad, Android and desktop visual/audio behavior, offline/reconnect and actual TTS voice clarity require user device acceptance.
- Use `USER_ACCEPTANCE_TEST_v2.95.6.md`; record PASS/FAIL/NOT TESTED with device/browser details.
