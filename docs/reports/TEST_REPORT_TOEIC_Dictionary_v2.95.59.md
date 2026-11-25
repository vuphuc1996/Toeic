# Test Report — TOEIC Dictionary v2.95.59

## Release scope

- Sole predecessor: `TOEIC_Dictionary_v2.95.58_FullSource.zip`.
- SHA-256: `67dd7d59a8f63bdb1307780dd95dd52e75f1b25af143ac0cef2a42e938b3d5cc`.
- Added a deterministic, read-only complexity review queue for all Listening/Reading questions. Signals are structural prompts only; no calibrated difficulty or CEFR/ETS claim is made.
- Question libraries were byte-identical to the predecessor: `data/listening/listening-library.json` SHA-256 `32fa347f500e3dbb241c183f48892572cbb529be6aa5a26c76d831bae7cf8111`; `data/readings/reading-library.json` SHA-256 `f7165c37af11e97333714b5b8c80ccd83332f5df22c7afef82555ba1f0372eba`.

## Executed checks

| Check | Result |
|---|---|
| Node regression scripts | 42/42 PASS |
| Focused Python: item complexity | 5/5 PASS |
| Focused Python: answer position balance | 4/4 PASS |
| Focused Python: learning outcome progress | 3/3 PASS |
| Focused Python: learning outcomes | 3/3 PASS |
| Focused Python: question evidence | 7/7 PASS |
| Focused Python: answer leakage | 7/7 PASS |
| Focused Python: distractor quality | 6/6 PASS |
| Focused Python total | 35/35 PASS |
| `tools/audit-item-complexity.py` | PASS; 582 questions, 280 reserve across both libraries, 106 with one or more signals, 0 structural errors |
| `tools/audit-question-evidence.py` | PASS; 582 questions indexed; Listening reserve 193 |
| `tools/audit-answer-leakage.py` | PASS; 177 eligible-scope questions, 6 diagnostic flags |
| `tools/audit-distractors.py` | PASS; 264 reviewed-scope questions, 156 reserve structural checks, 12 historical revisions verified |
| `tools/validate-data.py` | PASS; 1,141 records, 0 ERROR / 0 WARNING |
| `tools/validate-learning-content.py` | PASS; Listening 295, Reading 287, Grammar 169 exercises, Part 5 practice 80; 0 errors / 0 warnings |
| `tools/sync-version.py --check` | PASS; 13/13 registered version markers synchronized |
| Python compilation | PASS for new audit and test modules |
| `node --check sw.js` | PASS |
| Every `assets/js/*.js` syntax check | PASS |

## Complexity review output

- Total: 582 questions (Listening 295 + Reading 287).
- Listening reserve-pending: 193; Reading reserve-pending: 87; combined reserve: 280. All remain excluded from Mock pending independent approval.
- Structural signals: source text >=250 words: 40; inference/purpose wording: 10; option word-count spread >=8: 1; multi-document language cue: 98; long question prompt >=18 words: 0.
- The 98 multi-document counts are language cues, not proof that all 98 are multiple-passage items. No difficulty ranking is generated.

## Incomplete / unverified

- Full Python `unittest discover` was not run in this release; no full-suite completion claim is made.
- Hosted GitHub Actions, GitHub Pages deployment, cache propagation, offline/reconnect and physical iOS/iPadOS/Android/browser acceptance are UNVERIFIED.
- Independent editorial second review and psychometric calibration are not performed by this static audit.
