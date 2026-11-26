# Node Regression Report — TOEIC Dictionary v2.95.69

- Result: **44/44 scripts PASS**, 0 failed.
- Runtime: Node.js v22.16.0 on Linux x86_64.
- The complete set of `tools/tests/*.mjs` scripts was run individually against the final v2.95.69 working tree.
- The Robot Buddy layout test was updated to assert the current assessment-result contract: Learning Focus reuses its existing dialog; the duplicate modal is suppressed while the non-Learning-Focus modal fallback remains available. This replaces its stale stacked-modal expectation; no UI/CSS change was made in this batch.
- Detailed captured output: `node-tests-final.log` is maintained in the local verification workspace; the concise release result is recorded here.

Hosted GitHub Actions, GitHub Pages deployment, installed-PWA update/offline propagation and physical-device behavior were not tested by this local Node run.
