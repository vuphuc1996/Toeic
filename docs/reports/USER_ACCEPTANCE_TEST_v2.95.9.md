# User Acceptance Test — TOEIC Dictionary v2.95.9

## A. Release and deployment

1. Upload the complete v2.95.9 source to the intended GitHub branch.
2. Confirm the remote Actions run passes; confirm GitHub Pages displays v2.95.9.
3. On a device with the previous PWA installed, refresh/update the app shell and confirm no stale v2.95.8 Robot Buddy code remains.

Expected: remote workflow passes, Pages serves v2.95.9, and the app shell loads all required files.

## B. Robot Buddy progressive response

1. Open Robot Buddy and send “Mở Từ vựng”.
2. Observe the three-dot preparation state, then a message appearing progressively with a blinking caret.
3. Wait for completion and confirm the “Mở Từ vựng” action appears only after the text completes.
4. Click the action and confirm it opens the exact page.

Expected: no instant whole-message reveal in the standard chat path; no HTML injection, cut-off text or duplicate message.

## C. Dynamic local composition and context

1. Send “Mở Từ vựng” several times; phrasing should vary while the action still routes to `dictionary`.
2. Open an actual word in Dictionary; ask “Giải thích từ này giúp tôi”.
3. Confirm the response includes the open word and the available meaning/snippet, then gives the Dictionary-specific study step.
4. Repeat the contextual request and confirm the wording/transition can vary.
5. Ask an unsupported question; confirm Buddy asks for clarification and does not invent an answer.

Expected: response composition uses live in-memory app context and local content; no unrestricted AI claim.

## D. Interruption and accessibility

1. Send a long request and submit another message while the first is streaming.
2. Confirm the prior answer completes once and the next user turn/reply appears in order.
3. Enable OS “Reduce motion” and repeat a request.

Expected: no overlapping timers/carets, duplicate actions or cut-off strings; reduced-motion users receive a non-animated response.

## E. Existing learning and privacy safeguards

1. Toggle Learning Insights off; normal feature guidance must still work.
2. Toggle it on and request progress; confirm one visual dashboard only.
3. Confirm Buddy behavior remains available offline and does not depend on external AI/API connectivity.
4. Confirm no learner data, IndexedDB record, localStorage key or progress history is reset or migrated.

Expected: existing Learning Insights, dashboard, navigation, Placement consent/skip, idle reminders and learning progress are preserved.

## F. Cross-device

Check desktop/laptop, Android and iPhone/iPad if available. Confirm the chat log scrolls to the streaming cursor without horizontal overflow, input remains usable and the response animation does not block navigation.

Expected: no layout overflow; actual device performance and screen-reader behavior should be recorded separately.
