# Test Report — TOEIC Dictionary v2.95.8

## 1. Release basis and scope

- Functional base: exact v2.95.5 FullSource archive (`0edab13809c144bed5b2057c6cf05e6eb6d7c9adc237f4ec6bba90daa501d833`).
- Comparison reference: exact v2.95.7 FullSource archive (`be4521b884ecaa166a89e5df01acfdeb46919b5bd08e78a6cd769d1a3eb98282`).
- Release decision: retain all five defect fixes from v2.95.1–v2.95.5 and preserve opt-in local read-only Robot Buddy Learning Insights. Do not carry forward the v2.95.7 change that removed the progress dashboard, analysis toggle and insight aggregator.
- Adopted non-conflicting v2.95.7 maintenance improvements: consolidated Master/Compatibility/README docs, dry-run-first release-report rotation tool and its regression tests.
- Removed generated Python bytecode/cache artifacts from the package. Intentionally inert compatibility tombstones remain because they overwrite stale script paths during GitHub overlay updates; they are not imported as active implementations.

## 2. Five-defect coverage

| Defect group | Implementation / guard | Result |
|---|---|---|
| 1. Robot Buddy page-only navigation | Delegated `data-robot-page` click handling; overlay closes before exact destination navigation; actual handler regression | PASS |
| 2. `editorial_review` and CI | Reject blank/duplicate Part 7 options and invalid `answerIndex` types; dedicated workflow step and coverage guard | PASS |
| 3. Listening/Reading narration sequence | Shared Listening player honors `skipLeadIn` when Guided Mock already announced the Part transition; standalone Listening/Reading retain Part → lead-in → content → questions/options | PASS |
| 4. TTS A/B/C/D cadence | Regression asserts 1,000 ms pauses around labels/options for Listening Parts 2–4, Reading Parts 5–7 and Guided Mock; Part 1 retains 1,500 ms after labels and 1,300 ms between descriptions | PASS |
| 5. Robot Buddy progress dashboard | Explicit and natural-language analysis each render one visual dashboard and one totals row, without duplicate prose statistics | PASS |

## 3. Local automated verification

| Gate | Result |
|---|---|
| JavaScript regression suites | **34/34 PASS** |
| Python test modules | **54/54 PASS**, executed individually (including the full `test_validator.py` module) |
| JavaScript syntax | PASS — all shipped `assets/js/*.js` modules and `sw.js` via `node --check` |
| Python syntax | PASS — `python -m compileall -q tools` |
| Vocabulary validator | 1,141 records; 0 errors; 0 new/legacy warnings; 213 additive IDs vs. 928-ID baseline; 0 baseline IDs missing |
| Learning-content validator | 0 errors / 0 warnings; Listening 121 units / 239 questions; Reading 65 resources / 263 questions; Grammar 50 lessons / 137 exercises; Part 5 practice 80 questions |
| Repository integrity | 363 local references/data files; 0 errors / 0 optional warnings |
| Version synchronization | PASS — all registered markers v2.95.8 |
| Design profile | PASS — 54 tokens / 406 legacy font-floor selector groups |
| Part 1 photo assets | 9/9 valid; 0 missing-photo warnings |
| Objective-resource links | 339/339 across 11 objectives |
| Learning-outcome registry | 33 criteria defined; 6/33 have evidence collection paths; no mastery inferred |
| Question-evidence index | 502 TOEIC questions indexed |
| Distractor structural audit | PASS — 240 questions in scope; 108 reserve structural checks; 12 revisions |
| Foundation A2 audit | PASS — Reading 13/13 resources / 39 questions; Listening 13/13 / 39 questions; supplementary Listening 13/13 / 39 questions |
| Listening readiness | 102 eligible / 137 pending independent review / 239 total |
| Release rotation | PASS — `test_release_rotation.py` 6/6; relative `reports/...` and changelog links protected; CI registration PASS |

## 4. Cleanup and code integrity

- No duplicate top-level function declarations were found in shipped JavaScript modules or `sw.js` during the static declaration scan.
- The existing unified TTS runtime from v2.94.0 is retained; exactly one `speakText` and one `speakUtterance` implementation remain in the shipped app module.
- No learner data, vocabulary/question content, answer keys, stable IDs, IndexedDB schema v1 or existing localStorage learner keys were reset, migrated or rewritten by this release.
- Generated `__pycache__`, `.pyc` and `.pyo` files are excluded from the final archive. The documentation rotation retired 83 superseded report files into the consolidated history index; a post-apply dry-run reports 0 further files to retire.
- `learning-assistant.js` and `quick-help.js` remain inert compatibility tombstones and are not active runtime modules. Their removal would break the deliberate overlay cleanup contract for older GitHub checkouts, so they are not treated as dead active code.

## 5. Known editorial backlog (not release blockers)

- 93 vocabulary entries still lack US IPA.
- 338/809 synonym/antonym terms lack individual glosses.
- Four repeated English definition pairs and one word/sense CEFR discrepancy for `package` remain editorial review items.
- 137 Listening questions remain reserve-pending-independent-review; separate Part 5 practice and supplementary Foundation A2 content remain review-gated as documented.

These are reported as editorial debt, not silently auto-filled or represented as completed quality review.

## 6. External acceptance boundary

- Remote GitHub Actions has not been run or verified from this local workspace.
- GitHub Pages deployment, Service Worker update on the live site, browser acceptance, offline/reconnect behavior and physical-device TTS output are not verified.
- The exact acoustic pause and male/female voice clarity must still be judged on the user's actual iPhone/desktop/browser. Automated tests verify queue order and configured delays, not speaker output.
