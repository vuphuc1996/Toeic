# Robot Buddy Specification — v2.86.0

## Objective

Keep the quick-prompt menu usable throughout a longer conversation and prevent new messages from reducing its available height.

## Layout contract

1. The Robot header remains a fixed, non-shrinking section.
2. The chat shell is constrained by the panel's available height and clips its children to the shell.
3. The message log is the primary flexible region. It has its own vertical scrollbar and a bounded minimum height; message growth must not enlarge the panel indefinitely.
4. The quick-prompt menu remains visible after a user sends a message. It is a non-shrinking sibling of the message log, and the menu itself scrolls if its content exceeds its maximum reserved height.
5. The composer, typing indicator and privacy footer do not flex-shrink.
6. The privacy footer remains explicit about offline, pre-authored dialogue, local-only analysis and no external learning-data transfer; its type size is reduced to 6.5px.
7. Desktop, narrow portrait and short landscape viewports have separate bounded chat/prompt dimensions.

## Conversation behavior

- Quick prompts are reusable at any point during the current in-memory chat session.
- Selecting a prompt sends it through the same existing handler as typed messages.
- No conversation transcript is persisted. Existing memory/session behavior is unchanged.

## Privacy and data compatibility

- Robot Buddy remains a scripted offline companion, not a generative online chatbot.
- Learning Insights remains opt-in, local and read-only over the already-loaded application snapshot.
- No new API, backend, external network call, telemetry, IndexedDB migration or localStorage key is added.

## Regression protection

`tools/tests/robot-buddy-layout.mjs` checks the CSS layout contract, prompt persistence, responsive size bounds and footer type scale; `.github/workflows/validate-data.yml` runs the test.
