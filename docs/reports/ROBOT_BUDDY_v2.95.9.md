# Robot Buddy — v2.95.9 progressive replies and local composition

## User-visible changes

- A submitted message first shows the three-dot “đang chuẩn bị câu trả lời” indicator.
- The reply then appears progressively by grapheme-sized chunks, with a blinking caret. The caret and typing animation respect `prefers-reduced-motion`.
- The user can send another message while a reply is streaming; the previous partial response is safely completed before the new turn is appended.
- Reply action buttons appear only after the streamed text completes.
- The feature/help flow retains its shortcuts, and current-page/current-item content remains available to the response composer.

## Less rigid local responses

- Feature guidance combines a varied opener, an authored feature explanation and a varied action prompt.
- FAQ answers use phrase-scored matching and varied framing/closing text.
- Current-item help uses the active page, item title and available snippet, with varied transitions and study steps.
- Identity, encouragement and clarification messages are assembled from independent local phrase groups.
- Repeated supported prompts can receive different phrasing even when the underlying factual guidance is unchanged.
- Unknown prompts are handled honestly: the Buddy asks what topic or task the learner means and may refer to the current item; it does not invent a factual answer.

## Technical and privacy boundary

- This is not ChatGPT and does not use a generative model. The streaming effect animates locally composed text; it does not stream from an AI service.
- Content sources are the bundled dialogue/FAQ library, light rule-based intent classification, varied response fragments and the current in-memory app context.
- No external API, backend, WebSocket, remote model, new permission or analytics service was added.
- The Buddy itself still does not open IndexedDB/localStorage. Learning Insights remain opt-in and read-only through the app-supplied in-memory snapshot. No progress is written, reset, migrated or transmitted.
- Existing Learning Insights dashboard, shortcut actions, Placement consent/skip, idle reminders and head-only mascot are preserved.

## Acceptance checks

1. Send “Mở Từ vựng”: see the thinking dots, then progressive text and a blinking caret; the route shortcut appears after completion.
2. Open a vocabulary word and ask “Giải thích từ này giúp tôi”: reply must include the current word/available meaning and context-specific study guidance.
3. Repeat the same supported request: phrasing should vary while preserving the same supported guidance.
4. Ask an unsupported question: Buddy should request clarification, not fabricate an answer.
5. Start a second message mid-stream: the first reply must complete cleanly; no overlapping cursor or stale timer remains.
6. Enable OS reduced-motion: Buddy should render the complete response without the typing animation.
7. Toggle Learning Insights off/on: normal local conversation continues; the insight dashboard remains opt-in and read-only.
8. Test offline: conversation/composition works without external network calls.

Browser visual acceptance, deployed Pages behavior, offline installation and physical-device performance remain pending until checked after deployment.
