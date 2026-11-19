# User Acceptance Test — TOEIC Dictionary v2.95.10

> Record each result as `Đạt / Không đạt / Chưa kiểm`, with date, device/browser and evidence. Local automated tests do not replace these checks.

## A. Release / GitHub

1. Upload the v2.95.10 source to the intended GitHub branch.
2. Confirm the remote GitHub Actions workflow is green; confirm Pages serves v2.95.10 under the repository path `/Toeic/`.
3. Check browser cache/version markers and open the site in a fresh tab.

Expected: the remote workflow passes; the web app and manifest show v2.95.10; local assets load under `/Toeic/`.

## B. Flashcard — fixed maximum 10

1. Open Flashcard configuration. Confirm there is no `Số từ tiếp theo` control and no 5-card choice.
2. Start `Học tổng hợp`; confirm the session contains at most 10 cards.
3. Start at least two different topics; confirm each session uses the same maximum of 10.
4. Finish a batch and continue; confirm the next batch also uses at most 10.
5. Answer some cards incorrectly and open wrong-answer review; confirm missed words are prioritized and new words fill any remaining slots, with a maximum total of 10.
6. Confirm a short remaining pool shows only available items, not duplicates just to reach 10.

Expected: no route starts a 5-card batch; all Flashcard routes have one consistent 10-card cap. Vocabulary records and saved learning history remain intact.

## C. Robot Buddy streaming and auto-scroll

1. Open Buddy and send a long, supported question.
2. Observe the thinking indicator, progressive text and blinking cursor.
3. Confirm the chat panel scrolls with new text until the final line; the entire page should not be pulled unexpectedly.
4. Confirm action buttons appear after the response completes.
5. Submit a second question during streaming and check message order and no duplicate/cut-off content.

Expected: the conversation pane follows the active answer to its end; no horizontal overflow or overlapping animation.

## D. Service Worker update consent — two tabs

1. Install/open the current deployed PWA and open the same app in two tabs.
2. Deploy v2.95.10 and revisit both tabs.
3. Confirm the new worker waits and the existing app/cache remains active before confirmation.
4. In one tab, select `Có bản mới – Tải lại`.
5. Observe both tabs and verify the new worker becomes active without a partial shell or broken route.
6. Repeat with a failed required asset in a test branch/environment only; verify the old cache remains usable.

Expected: no silent forced takeover on ordinary upgrades; user action is required to apply the new version. Record each tab's behavior.

## E. PWA offline / cache

1. Open the app online once, then switch to airplane mode/offline.
2. Navigate vocabulary, Flashcard, Reading and Listening pages.
3. Restore network, reload and verify normal reconnection and current content.
4. Check that old TOEIC cache cleanup does not remove unrelated origin caches.

Expected: required shell content remains available offline after a successful online install; optional image failure does not block installation.

## F. TTS and responsive checks

1. Listen to Listening Parts 1–4 and Reading Parts 5–7 on the actual device.
2. Compare male/female voices and record browser voice name, clarity and pauses.
3. Check 15.6-inch laptop at 100% zoom, 90% as comparison, Android Chrome and iPhone Safari/iPad Safari where available.
4. Check sidebar, Robot Buddy panel, update banner above mobile navigation, Flashcard cards, image crop, controls and long text wrapping.

Expected: no clipping or overlap; record actual device voice quality and acoustic pacing, which automated tests cannot prove.

## Acceptance record

| Item | Result | Date | Device / browser | Evidence / note |
|---|---|---|---|---|
| A. GitHub Actions / Pages / `/Toeic/` | Chưa kiểm | | | |
| B. Fixed 10-card Flashcard | Chưa kiểm | | | |
| C. Robot Buddy streaming / auto-scroll | Chưa kiểm | | | |
| D. Two-tab update consent | Chưa kiểm | | | |
| E. Offline / reconnect | Chưa kiểm | | | |
| F. TTS / responsive | Chưa kiểm | | | |
