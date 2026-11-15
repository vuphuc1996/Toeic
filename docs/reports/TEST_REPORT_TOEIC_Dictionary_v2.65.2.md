# Test Report — TOEIC Dictionary v2.65.2

**Scope:** add a Part 1 lead-in and explicit A–D spoken labels, keep the Practice and Mock Exam audio sequence identical, and make the pause after the lead-in configurable.
**Environment:** local source workspace; Node.js and Python. No physical browser/device audio capture was available.

## Behavior implemented

1. The shared TTS readiness pipeline prepares the voice catalog and startup buffer.
2. Part 1 speaks: “Now, listen to the four statements.”
3. A configurable pause follows the lead-in (default 1,000 ms; 800–1,800 ms).
4. The app then speaks four separate utterances: “A. [description]”, “B. [description]”, “C. [description]”, “D. [description]”.
5. The existing 1,300 ms default pause separates each adjacent option; the value remains configurable.
6. Practice and Mock Exam buttons both invoke `playListeningAudio()` for the same content item, so they share the same lead-in, option labels, voice choice and timing.
7. The transcript shows the lead-in and letter labels. The source data remains clean and runtime formatting avoids duplicate labels if one is already present.
8. Incomplete Part 1 content with other than four segments is stopped with a clear message.

## Verification

| Check | Result |
|---|---|
| `test_tts_readiness.py` | **13/13 PASS** |
| Selected Python modules (TTS, version sync, listening expansion, CI coverage, PWA readiness) | **35/35 PASS** |
| All JavaScript regression suites | **19/19 PASS** |
| `listening-tts-regression.mjs` | **PASS** — lead-in, exact user example `A. Passengers are boarding an aircraft by stairs.`, A–D labels, lead-in gap, 1.3s option gaps, cancellation during lead-in, same Practice/Mock path |
| Part 1 library integrity | **9/9 units have exactly four segments** |
| `sync-version.py --check` | PASS after changelog update |
| `node --check` on app JS and service worker | PASS |
| `validate-data.py` | 992 records; 0 errors; 0 warnings |

## Compatibility and data safety

- `part1LeadInPauseMs` is an additive `appSettings.tts` setting with a default of 1,000 ms. Existing configurations receive the default through the existing merge-with-defaults path.
- `part1OptionPauseMs` remains 1,300 ms by default.
- No listening question text, answer keys, explanations, stable IDs, transcript source text, IndexedDB schema/stores or learner progress were changed.
- The same `playListeningAudio()` method is called from the Listening Practice event and Mock Exam audio event.

## Limitations

- Speech Synthesis output, pronunciation of the letter names A–D and actual pause durations depend on the browser/OS voice engine. They are verified at the application queue/timer level only; physical iPhone/iPad/Android/desktop listening remains outstanding.
- The inherited strict Part 1 media validator remains blocked by eight missing original JPG binaries in the archive (1/9 present). Preserve existing repository photo assets when applying the source update; do not weaken the validator or use fabricated binaries.
- No remote GitHub Actions or GitHub Pages deployment is claimed.
