# User Acceptance Test — TOEIC Dictionary v2.94.0

**Test approach:** one consolidated pass after deploying the full source. Record `PASS`, `FAIL` or `NOT TESTED` for each line. Do not delete local app data or clear browser storage as part of this test.

## 1. Update and PWA startup

- [ ] Publish the complete v2.94.0 source to the intended GitHub repository.
- [ ] Confirm the GitHub Actions workflow completes successfully, including `Repository integrity preflight`, `question_evidence`, `TTS readiness`, `Grammar example quality` and the existing validation suites.
- [ ] Open the published site, confirm the displayed version is v2.94.0, reload once and confirm the new build is active.
- [ ] Test one offline page open and reconnect; note any stale cache or missing resource.

Expected: all assets load, no missing-file console errors, version/cache changes are visible and existing learning data remains present.

## 2. Mobile/tablet zoom and Robot Buddy layout

- [ ] On a phone and tablet, open Robot Buddy and tap the chat input.
- [ ] Type and send several messages; tap quick prompts and the progress-analysis button.
- [ ] Confirm focusing the input does not automatically enlarge the whole page.
- [ ] Confirm manual pinch-to-zoom remains available for accessibility.
- [ ] Confirm the message list scrolls independently; quick prompts, input, send button and privacy note remain usable.

Expected: no focus-triggered zoom, no clipped composer/footer, and normal user pinch zoom is preserved.

## 3. Robot Buddy progress dashboard

- [ ] Start a new Buddy session and press **Phân tích tiến độ của tôi** in the welcome message.
- [ ] Confirm three status totals appear: Cần học / Cần luyện / Cần ôn.
- [ ] Inspect the colored per-module meters and their studied-item denominator.
- [ ] Confirm sparse evidence is reported as insufficient rather than labeling a skill weak.
- [ ] Turn progress analysis off and verify ordinary help/chat still works.

Expected: all information reflects local progress only. A module's meter is study exposure/coverage, not course completion, official TOEIC score or CEFR mastery. No single aggregate percentage is invented.

## 4. Voice — highest priority

Test on desktop and at least one mobile/tablet browser. Use both Listening and Reading.

- [ ] Open **Cấu hình → Giọng đọc**. Record the English voice catalogue status and selected voice.
- [ ] Press the male and female preview buttons. Confirm audible output.
- [ ] Open Listening Part 2 or Part 3 and press **Nghe toàn bộ**. Confirm audio starts, each turn is spoken, inter-speaker pauses are natural and status changes while playing.
- [ ] Open a Part 1 item. Confirm topic title, lead-in and A/B/C/D labels/descriptions are spoken in sequence.
- [ ] Open a Reading passage (preferably a longer or double-passage item) and press **Nghe đọc bài**.
- [ ] Press Dừng while audio is active; then press Nghe again.
- [ ] Return to Cấu hình, select another available voice and repeat one sample.
- [ ] If a selected voice fails, confirm the browser-default fallback is attempted once. If the browser cannot start speech, confirm a clear error appears instead of silent indefinite waiting.

Expected: first utterance is queued immediately from the tap/click; there is no mandatory fixed two-second pre-play wait. If the browser supplies no voice list, the app attempts system-default SpeechSynthesis using the English locale. A start failure should be reported after the 10-second watchdog. Local automated tests verify the fallback path, but actual audible output must be confirmed on your devices.

For any voice failure, record: OS, browser/version, device, selected voice name/language, type of content, status text, whether any sound was heard and whether Dừng works.

## 5. Grammar examples

- [ ] Open several of the latest 17 expanded Grammar lessons (Batch 024/025).
- [ ] Inspect English example, Vietnamese translation and sentence breakdown.
- [ ] Confirm formula, explanation and exercises still align; submit one answer and confirm explanation appears only after confirmation.
- [ ] Open an older lesson and report examples that still lack full translation/analysis.

Expected: the 42 enriched examples are complete and readable. Earlier lessons may still need progressive editorial enrichment; report missing examples rather than treating them as a runtime defect.

## 6. Listening and Reading content / Mock boundary

- [ ] Confirm Listening and Reading libraries open and questions can be answered.
- [ ] Check new Batch 024/025 content appears for practice.
- [ ] Confirm pending-review items do not enter Mock.
- [ ] Open Quick, Half and Full Mock modes; confirm blueprint, timer, scoring and previous result history work.

Expected: user-facing practice content remains separate from Mock-approved questions; no pending reserve item is silently promoted.

## 7. Score Readiness and local-data preservation

- [ ] Open Score Readiness with fewer than three Full Mocks (where applicable); confirm it reports insufficient evidence.
- [ ] With three qualifying Full Mocks, confirm L/R accuracy trends only; no false ETS scaled-score estimate.
- [ ] Verify vocabulary, flashcard, Grammar, Listening, Reading, Foundation and Mock progress survive reload.
- [ ] Verify Robot Buddy analysis does not write, reset or upload learning records.

Expected: IndexedDB schema v1 and existing local progress keys remain intact. No new backend/API or external transfer is introduced.

## 8. Product/responsive sweep

- [ ] Desktop 15.6-inch at 100% zoom: sidebar/footer and main content visible without clipping.
- [ ] Phone portrait and landscape; tablet portrait and landscape: no horizontal overflow or inaccessible controls.
- [ ] Review ordinary learning screens to ensure no developer test/audit panel is exposed to learners.

## Result record

For each failed/not-tested item, record the number, browser/device, exact steps, expected behavior, actual behavior and screenshot if available. The release is not considered user-accepted until the voice checks, data-preservation check and Mock boundary checks pass.
