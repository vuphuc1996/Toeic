# Robot Buddy privacy refinement — v2.95.25

## Change
When Learning Insights is toggled OFF, the app now removes all rendered `.robot-progress-dashboard` elements from the Robot Buddy chat panel immediately. It preserves unrelated conversation messages. The opt-in setting and existing analysis boundary remain unchanged.

## Why
A previously rendered local snapshot could remain visible after the user disabled analysis. Although this was not a new data read, clearing the dashboard avoids ambiguity about whether progress insights are still active.

## Validation
- Updated `tools/tests/robot-buddy-data-boundary.mjs` with checks for dashboard cleanup and disable-gate behavior.
- Robot Buddy boundary regression: PASS.
- Full JavaScript suite count: 39 suites (run separately).
- Python full discovery: attempted but did not complete within the execution limit; results are not represented as a full-suite pass.
- Vocabulary and learning-content validators: PASS, 0 errors / 0 warnings.
- Version synchronization: PASS.

## Scope
No UI layout redesign, learner-record deletion, data-store changes, or network access was added. This change is confined to the existing v2.95.25 release.
