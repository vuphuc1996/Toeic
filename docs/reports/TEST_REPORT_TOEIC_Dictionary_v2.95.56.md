# Test report — TOEIC Dictionary v2.95.56

## Change under test
Listening form-diversity gating for the TOEIC Score Readiness panel. See `MOCK_LISTENING_FORM_DIVERSITY_v2.95.56.md`.

## Results

| Check | Result | Evidence |
|---|---|---|
| Mock score readiness | PASS | Same-form gate, distinct-form detection, overlap disclosure, legacy fail-closed, Reading independence |
| Mock exam engine | PASS | Full/half/quick blueprint, reserve exclusion, usage rotation, scoring |
| Mock UI integrity | PASS | 299 unique HTML IDs; existing UI wiring |
| JavaScript runtime regression | PASS | 42/42 `tools/tests/*.mjs` scripts |
| JavaScript syntax | PASS | `app.js`, `mock-score-readiness.js` |
| Data validator | PASS | 1,141 records; 0 errors / 0 warnings; 0 ID additions/removals |
| Version sync | PASS | All 13 registered markers + changelog at 2.95.56 |
| Python full unittest discovery | INCOMPLETE | Attempt exceeded 300-second tool execution limit; not counted as pass |

## Actual form-overlap probe

Using the current Listening/Reading source data and the existing `createMockExam` engine: first Full form = 100 Listening questions; second Full form with first-form usage counts = 100 Listening questions; shared IDs = 98; overlap = 98%; questions exchanged = 2. This validates the need for the warning with the supplied eligible pool.

## Not verified

Remote GitHub Actions, GitHub Pages deployment, installed-PWA cache propagation, physical iOS/iPadOS/Android behavior, and ETS score equivalence.
