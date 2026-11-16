# v2.82.0 — Restore legacy Google AI from v2.79.0

## Why this corrective release exists

The v2.81.0 implementation removed every runtime Google AI integration. That exceeded the requested scope. The actual request was to remove the new Google AI functionality added with the v2.80.0 floating assistant, while preserving the feature-level Google AI actions that had already existed before v2.80.0.

This release restores those pre-v2.80 controls from the exact v2.79.0 Full Source, while retaining the local Quick Help functions and A2 writing portfolio developed later.

## Legacy functions restored

| Existing application area | Restored action | Data included in prompt |
|---|---|---|
| Vocabulary detail | “Tra cứu Google AI” button | Existing headword, IPA, topics, senses, word family, verb forms, collocations and examples |
| Unknown lookup term | Google AI explanation fallback | User-entered English term and a structured TOEIC explanation request |
| Practice question/review | “Tra cứu Google AI” / “Phân tích thêm bằng Google AI” | Current question, choices, accepted answer, explanation, user answer and dictionary references |
| Grammar lesson | Google AI analysis button | Existing lesson formula, explanation, examples, tips, exercises and answers |
| Reading | Google AI passage analysis button | Passage, translation, vocabulary, questions, answer keys and explanations |
| Listening | Google AI analysis button | Existing transcript/segments, questions, answers, explanations and vocabulary |

The existing one-way prompt preview/modal is restored with its title, context summary, read-only prompt field, explicit run button and close control. The Google URL retains the pre-existing observed parameters `udm=50` and `hl=vi`.

## What remains removed

The following are specifically the newer v2.80 floating-assistant additions, not the older feature-level Google AI actions:

- The assistant-specific contextual prompt builder for arbitrary currently open pages/details.
- The new “ask Google AI about this context” follow-up action from the shared floating assistant.
- New copy/transfer controls used by that v2.80 contextual handoff, including its long-prompt copy-and-manual-paste path.
- Any Google AI action inside the Quick Help panel itself.

The Quick Help panel remains local-only. It retains the welcome greeting, in-app navigation guide, existing Placement Diagnostic entry point, and masked completion based on actual canonical vocabulary records. It does not call Google or another external service.

## Privacy and operational boundary

- No Google model is embedded in the PWA.
- No Google API key, backend, proxy or separate AI service is introduced.
- No prompt is submitted on page load, navigation, typing or background activity.
- A prompt is prepared locally from the selected feature's existing content and shown in the existing modal. It is sent outside the app only after the learner explicitly presses the run button.
- The handoff opens an external Google Search URL. Google controls the destination interface and may change or discontinue its observed query parameters. The app does not control or guarantee Google's response.
- The pre-existing 12,000-character URL guard remains: an oversized prompt is not silently truncated or sent through a new background service.

## Preserved product scope

- v2.81 A2 writing portfolio remains in the existing Foundation dashboard.
- `::apply1` and `::produce1` evidence remain separate.
- `toeic:foundation-progress:v1` and IndexedDB v1 remain unchanged.
- No vocabulary record, Foundation lesson/question ID, Reading/Listening question bank or TOEIC Mock pool is changed by this restoration.
- Quick Help remains offline-cached via the existing Service Worker.

## Regression boundary

`tools/tests/legacy-google-ai.mjs` verifies the legacy controls, prompt builders, event routing, explicit external URL construction, and CSS panel. `tools/tests/quick-help.mjs` separately verifies that the local helper stays offline-only. The newer assistant-specific AI hooks are asserted absent.
