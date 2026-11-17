# Robot Buddy v2.85.0 — UI refinement and action-oriented insights

## Visual structure

- Header row 1 contains only the head avatar, **Robot Buddy**, the “Bạn đồng hành TOEIC · Offline” status and the close (×) control.
- Header row 2 contains two independent controls: `Phân tích tiến độ: Bật/Tắt` and `Lời nhắc: Bật/Tắt`.
- The two controls use a shared two-column grid on desktop and mobile. Their accessible `aria-pressed` value represents the enabled state (true = Bật, false = Tắt).
- The quick-prompt area has a larger scrollable height and larger touch targets. The footer is compact but still states that dialogue is pre-authored/offline, local progress is read only when analysis is enabled, data is not sent externally, and Robot is not an online AI chatbot.

## Response typography

Bot replies visually emphasize these exact terms: **Robot Buddy**, **TOEIC Dictionary** and **Vũ Nguyễn Hoàng Phúc**. The renderer splits text into DOM text nodes and `<strong>` nodes. It does not assign user or library text to `innerHTML`; line breaks and plain text remain intact.

## One-tap actions after Learning Insights

- After the analysis is computed from the already-loaded local snapshot, up to four distinct page actions may be attached to the bot reply.
- Routes are selected from concrete item `area` values in the `learn`, `practice` or `review` lists: Vocabulary, Flashcard, Grammar, Reading, Listening, Foundation, Mock or Objective recall/Practice.
- Actions open existing pages only. They do not claim an individual item was opened, alter review schedules, add quiz attempts or write progress.
- If there is no sufficient evidence, no navigation action is fabricated. The response keeps the existing “chưa đủ dữ liệu” language.

## Preservation

- The 500-message offline dialogue library, 59 help messages, six FAQ entries and 16 quick prompts are unchanged.
- `toeic:robot-buddy-settings:v1` remains the only Robot preference key. No migration or new preference field is introduced.
- IndexedDB schema v1, all progress keys, stable content IDs, local-only data handling, insight thresholds and Service Worker resource inventory remain unchanged.
