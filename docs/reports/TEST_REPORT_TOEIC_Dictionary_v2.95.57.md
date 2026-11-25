# Test Report — TOEIC Dictionary v2.95.57

## Release scope

- Focus: Stage 2 item 7 — answer leakage / distractor overlap diagnostics.
- Change is developer tooling and reporting only. No question text, answer keys, choice order/IDs, source evidence, Mock eligibility, learner data/schema, UI or Robot Buddy scope changed.
- Scope: 177 Mock-eligible questions — Listening Part 3 (39), Part 4 (30), Reading Part 7 (108). Reading reserve (87 questions) and Listening reserve (193 questions) are excluded.

## Results

| Check | Result | Evidence |
|---|---|---|
| Node regression | PASS — 42/42 scripts | `Node_Regression.log` |
| Focused Python regressions | PASS — 36 tests across 6 modules | `Python_Focused.log` |
| Answer leakage diagnostic | PASS — deterministic report; 6 review signals | `TOEIC_ANSWER_LEAKAGE_DIAGNOSTIC_v2.95.57.md` |
| Existing distractor structural audit | PASS — 264 structural scope questions; valid keys and distinct options | `Source_Preflight.log` |
| CI coverage | PASS — every Python and JS regression suite is invoked | `Python_Focused.log` |
| Repository integrity preflight | PASS — 436 local references/data files inspected; 0 errors / 0 warnings | `Source_Preflight.log` |
| Data validator | PASS — 1,141 records; 0 ID additions/removals; 0 errors / 0 warnings | `Source_Preflight.log` |
| Version synchronization | PASS — all 13 registered markers + changelog at 2.95.57 | `Source_Preflight.log` |
| JavaScript syntax | PASS — `assets/js/app.js` | `Source_Preflight.log` |
| Protected content comparison | PASS — Listening library, Reading library and sampled vocabulary files byte-identical to v2.95.56 | `PACKAGE_VERIFICATION_v2.95.57.md` |

## Diagnostic result

- 6/177 questions flagged for editorial triage: Part 3 = 2, Part 4 = 1, Part 7 = 3.
- All six flags are answer-length outliers. No question-stem lexical-cue flag or key/distractor lexical-overlap flag remains in the Mock-eligible scope.
- A long correct answer may be required by legitimate content; this signal is not a defect verdict. The diagnostic cannot prove semantic uniqueness, detect paraphrase equivalence, or establish ETS/psychometric calibration.
- No question content was auto-corrected. Human review must inspect the full source, evidence and all options before any future edit.

## Not run / unverified

- Full Python `unittest discover` was not run for v2.95.57; only the 36 focused Python tests above are claimed PASS.
- Hosted GitHub Actions, GitHub Pages deployment, installed-PWA cache propagation, browser storage behavior and physical iOS/iPadOS/Android acceptance are UNVERIFIED.
- No official ETS comparison, psychometric calibration or external independent reviewer sign-off is claimed.
