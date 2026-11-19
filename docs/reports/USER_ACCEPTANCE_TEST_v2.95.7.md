# User Acceptance Test — TOEIC Dictionary v2.95.7

Run after deployment to GitHub Pages. Record PASS / FAIL / NOT TESTED; for failures include device, OS, browser, steps and screenshot/log where relevant.

## A. Release / GitHub
1. Confirm GitHub Actions completes the full workflow successfully.
2. Open GitHub Pages and confirm the visible release is v2.95.7.
3. If the PWA shows an older release, reload/update the Service Worker and verify the new cache namespace.

Expected: remote workflow PASS, Pages serves v2.95.7, no missing app-shell resources.

## B. Robot Buddy privacy boundary
1. Open Robot Buddy on a first-use profile. Confirm it asks whether to run the optional Placement diagnostic.
2. Choose “Không cần, bỏ qua”. Confirm the app continues normally and Robot Buddy remains available.
3. Ask “Bạn là ai?”, “Phân tích tiến độ học của tôi” and “Hôm nay tôi cần ôn những gì?”.
4. Confirm Robot Buddy explains that it does not read progress, answers or learner profile data; it may offer only general navigation to Trang chủ / Ôn tập.
5. Inspect the Buddy UI: there must be no progress-analysis toggle or personalized progress dashboard.
6. Wait through the idle prompt interval while on a safe page. Confirm prompts are generic encouragement/caring messages, not counts or suggestions derived from stored progress.
7. Use feature shortcuts such as Từ vựng, Listening, Reading and Cấu hình. Confirm the Buddy closes and navigates to the exact selected page.

Expected: Buddy dialogue is static/library-based; no learner progress or profile is read, summarized or used for proactive nudges. The Placement diagnostic runs only after explicit consent.

## C. Core learning regression
1. Open one vocabulary entry, one flashcard set, one grammar lesson, one Listening item and one Reading item.
2. Confirm content loads and existing learner progress remains available.
3. Complete one practice question and verify normal app progress saving still works outside Robot Buddy.
4. Reload the app and confirm existing data remains intact. Do not clear browser storage as part of this test.

Expected: core learning and app-owned progress functions remain unchanged; Robot Buddy is isolated from them.

## D. Listening / Reading narration and TTS
1. Test Listening Parts 1–4 and Reading Parts 5–7 using the existing v2.95.6 sequence checklist.
2. Confirm content/lead-in/question/option order and the established A/B/C/D cadence on the actual device.

Expected: no missing or repeated narration. Automated tests validate queued order and delays; actual voice quality requires device testing.

## E. PWA / responsive / offline
1. Test Windows desktop at 100% zoom and a narrow mobile viewport.
2. Confirm Robot Buddy panel, quick prompts, composer and reminder toggle fit without horizontal overflow.
3. Test one previously cached page offline, then reconnect and reload.

Expected: no new layout regressions, cached resources load, reconnect returns the app to normal operation.
