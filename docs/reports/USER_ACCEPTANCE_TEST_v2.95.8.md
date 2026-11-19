# User Acceptance Test — TOEIC Dictionary v2.95.8

Run after deploying the complete source to GitHub Pages. Record each item as PASS / FAIL / NOT TESTED. Do not clear browser data or IndexedDB during these tests.

## A. Release and CI
1. Push the complete v2.95.8 source to the intended GitHub branch.
2. Confirm GitHub Actions completes, including `editorial_review`, `CI coverage`, `release_rotation`, repository integrity, version sync and all JavaScript suites.
3. Open GitHub Pages and confirm the visible version is v2.95.8; if stale, update the PWA/Service Worker and reload.

Expected: remote workflow passes and the deployed site serves v2.95.8 with no missing app-shell resource.

## B. Robot Buddy navigation
1. Ask Robot Buddy to open Từ vựng, Nghe hiểu and Đọc hiểu.
2. Click each generated shortcut, including a page-only shortcut after a reply and a shortcut inside the progress dashboard.
3. Confirm the Buddy panel closes and the exact destination opens.

Expected: all valid shortcuts navigate correctly; no dead buttons.

## C. Editorial review and CI
1. Open the GitHub Actions `Unit tests — editorial_review` step.
2. Confirm blank/duplicate Part 7 answer options and invalid `answerIndex` types are rejected by the tests.
3. Confirm `CI coverage` checks the dedicated editorial test invocation and every Python/JavaScript suite.

Expected: editorial review and CI coverage pass; no stale fixed inventory assertion fails.

## D. Listening / Reading narration sequence
1. Play one standalone Listening item from each Part 1–4.
2. Play Reading Parts 5–7.
3. Enter Guided Mock Listening Parts 2–4 and verify the Mock transition's Part heading/lead-in is not repeated by the shared player.

Expected: Part title → instruction/lead-in → content → questions → answer options, with no missing or duplicated introduction. Part 2 audio itself remains the question.

## E. TTS cadence
1. Play Listening Parts 2–4 and Reading Parts 5–7 on a device with audible English TTS.
2. Confirm approximately 1 second after each A/B/C/D label before the option text and approximately 1 second between option text and the next label.
3. In Listening Part 1, confirm 1.5 seconds after each label and 1.3 seconds between descriptions.
4. Repeat on iPhone/iPad, Android and desktop where available; record OS, browser and selected voice.

Expected: cadence is audible and natural. Voice quality and actual acoustic timing are judged on the device, not inferred from automated tests.

## F. Robot Buddy Learning Insights
1. Open Robot Buddy and use the explicit progress-analysis action.
2. Ask “Phân tích tiến độ học tập của tôi.”
3. Confirm one visual dashboard appears per request, with one set of Cần học / Cần luyện / Cần ôn totals and no repeated prose statistics.
4. Turn Learning Insights off; confirm ordinary chat, help, quick prompts and page shortcuts still work. Turn it back on and repeat.
5. Use a dashboard navigation action and confirm the exact module opens.
6. Open a vocabulary detail and ask “Giải thích từ này giúp tôi”; confirm the reply refers to the current word and its visible meaning. Open a Listening item and ask “Hướng dẫn bài này”; confirm the reply gives Listening-specific guidance for that current item.
7. Wait through a safe idle interval while a learning item is open; confirm the reminder offers a brief suggestion related to that current item.

Expected: context-aware help uses the current in-session item; opt-in local read-only analysis works; the visual dashboard is preserved; no duplicate text summary or external transmission is introduced.

## G. Existing learning data and core flows
1. Open a vocabulary entry, Flashcard, Grammar lesson, Listening item, Reading item and Review mode.
2. Confirm existing personal vocabulary, saved progress and Mock history remain visible.
3. Complete one practice question and reload the app.
4. Complete a 5-word or 10-word Flashcard quiz and confirm its result modal is visible above the learning-focus surface.
5. Test Part 5 recall when a linked headword is hidden from the personal dictionary; confirm a valid fallback question opens.

Expected: no learner data reset, no empty Review start caused by a hidden linked word, and Flashcard completion confirmation remains actionable.

## H. Responsive / offline / reminders
1. On a 15.6-inch laptop at 100% zoom, confirm the sidebar bottom status is visible and Robot Buddy fits without clipping.
2. On mobile, confirm the Robot input does not trigger automatic focus zoom; pinch zoom remains available.
3. Test quick prompts, reminder mute, idle prompt dismissal/snooze and safe suppression during Mock/modal activity.
4. Test one cached page offline, reconnect and reload.

Expected: no horizontal overflow or clipped Robot controls; offline/reconnect recovers normally.

## Result log

| Item | Result | Device / browser | Notes |
|---|---|---|---|
| A. Release and CI | NOT TESTED | | |
| B. Robot Buddy navigation | NOT TESTED | | |
| C. Editorial review and CI | NOT TESTED | | |
| D. Listening / Reading sequence | NOT TESTED | | |
| E. TTS cadence | NOT TESTED | | |
| F. Robot Buddy Learning Insights | NOT TESTED | | |
| G. Existing learning data and core flows | NOT TESTED | | |
| H. Responsive / offline / reminders | NOT TESTED | | |
