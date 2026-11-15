# Project Progress Baseline — TOEIC Dictionary v2.65.2

## Release scope

Part 1 playback now includes the spoken lead-in “Now, listen to the four statements.”, a configurable 1,000 ms transition pause, and four separately spoken choices A–D with the retained 1,300 ms inter-option pause. Both Practice and Mock Exam call the same playback function.

## Quantified coverage

- TOEIC vocabulary: 992 / 3,000 minimum = **33.1%**. This is bank size, not learning mastery.
- Listening Part 1: 9 / 9 current units have four descriptions = **100% structural coverage**.
- Part 1 playback sequence: lead-in + A + B + C + D = **5 / 5 playback stages**.
- Current TTS readiness test: **13 / 13 PASS**.
- Selected Python checks: **35 / 35 PASS**; JavaScript regression suites: **19 / 19 PASS**, including ordered speech, exact A-D labels, transition pause, option pauses and cancellation in the lead-in gap.
- Version synchronization: **PASS**.
- Data validation: 992 records; **0 errors, 0 warnings**.

## Not measured / outstanding

- Actual learner pronunciation comprehension or TOEIC performance: not measured by playback interaction.
- Real device TTS quality, letter-name pronunciation and exact audible pauses on iOS/Android/desktop: not measured in this source workspace.
- Strict Part 1 photo validation: inherited blocker, eight original JPG files missing from local archive; 1/9 present.
- GitHub Actions / GitHub Pages deployment: not verified.

## Progress interpretation

Structural feature coverage for current Part 1 playback is **100% (9/9 units have A–D data; the shared runtime supplies lead-in and labels)**. This does not mean the whole Listening curriculum or learner mastery is 100% complete.
