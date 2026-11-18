# TOEIC Score Readiness — Evidence Tracker (v2.93.0)

## Product and learner targets
- Product design target: support a learning pathway toward TOEIC Listening & Reading 850+.
- Initial personal learning milestone: 500+; subsequent milestones may be 600, 700, 750, 800, 850 and 900+.
- These are goals, not predicted outcomes or guaranteed scores.

## What the tracker does
- Reads only the existing device-local Mock history.
- Uses the three most recent completed Full Mock attempts that contain 200 questions and both Listening and Reading accuracy values.
- Before three qualifying attempts, reports `Chưa đủ dữ liệu` and displays the number of qualifying Full Mocks.
- After three qualifying attempts, reports separate Listening and Reading average accuracy plus direction of change from the first to the third attempt in that rolling set.
- The tracker is a progress aid for choosing what to study next, not a psychometric score estimator.

## What it deliberately does not do
- It does not convert raw correct-answer percentages into ETS scaled scores (/495 or /990).
- It does not claim that 75%, 80%, 85% or any raw accuracy guarantees 500+, 850+ or any official score.
- It does not treat Quick Test or Half Mock attempts as full-length readiness evidence.
- It does not send Mock history outside the device and does not create a new storage key.

## Why three Full Mocks
One test can be affected by item familiarity, topic mix, time pressure or chance. Three full attempts provide a small repeated sample for observing direction and variability. Three tests are a minimum display gate, not a statistically validated prediction model.

## Future calibration gate
A future score-prediction feature must not be implemented until the project has:
1. Several independently reviewed, equivalent full-length practice forms covering all seven TOEIC Parts.
2. Evidence that the item pool has appropriate difficulty and distractor quality.
3. A documented equating/calibration method grounded in reliable score data, not an invented linear conversion.
4. Validation against actual official TOEIC results from consenting learners, with uncertainty ranges and a clear sample-size policy.
5. An explicit user-approved decision to display a score estimate.

Until those gates are met, show practice accuracy and trends only.
