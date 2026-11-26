# Node Regression Report — TOEIC Dictionary v2.95.70

- Result: **45/45 scripts PASS**.
- Source: FullSource v2.95.69 verified predecessor, working candidate manifest `2.95.70`.
- Execution log is retained outside the source package at `/mnt/data/v2970_node_tests/NODE_TESTS_v2.95.70.log` in this run environment.
- The CI workflow's complete Node test block (45 scripts) was executed, beginning at the first listed test and ending with learner-data backup integration.

## Main coverage

- Runtime render and migration smoke: deferred answer drafts, stable choice IDs and idempotent migration.
- Listening/TTS and Reading Parts 5–7 regression.
- Mock quick/half/full blueprint, reserve-question exclusions and scoring.
- Learning Focus workspace, modal dismissal and assessment deferred workflow.
- Single-action assessment confirmation: exactly one explicit result action, no post-completion return/recheck route, and Foundation persist-before-reveal behavior.
- Foundation A2, listening, reading and evidence; Learning Outcome progress.
- Data validation, release shell, Service Worker update and cache coherence.
- Robot Buddy layout, learning insights, progress dashboard and local data boundary.
- Learner backup envelope, integrity and exact restore round-trip.

## Specific v2.95.70 regression

`tools/tests/assessment-one-way-confirmation.mjs` confirms that the completed result surface contains only `Xác nhận & xem đáp án`; the previous `Quay lại kiểm tra` action, delegated route and legacy toast are absent. Foundation confirmation tests verify that storage failure keeps prior committed progress and staged selections, and successful storage occurs before progress state is committed and answer review is revealed.

## Scope limits

These are local Node regression results. They do not establish hosted GitHub Actions, live GitHub Pages deployment, installed-PWA cache/offline propagation, or physical-device acceptance.
