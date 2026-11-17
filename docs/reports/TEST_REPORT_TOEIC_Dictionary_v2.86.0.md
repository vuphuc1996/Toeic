# Test Report — TOEIC Dictionary v2.86.0

## Scope

- Prevent long conversations from compressing Robot Buddy quick prompts.
- Keep the quick-prompt choices visible and reusable throughout the chat session.
- Give the conversation log its own bounded scroll area.
- Keep the composer, typing indicator and privacy footer from flex-shrinking.
- Reduce the privacy footer to 6.5px without changing its privacy meaning.

## Local checks

| Check | Result | Scope |
|---|---|---|
| `node --check assets/js/app.js` | PASS | Application module syntax |
| `node --check sw.js` | PASS | Service Worker syntax |
| `node --check tools/tests/robot-buddy-layout.mjs` | PASS | New layout test syntax |
| `node tools/tests/robot-buddy-layout.mjs` | PASS | Reserved menu height, independent chat scroll, persistent prompts and compact footer contract |
| `node tools/tests/robot-buddy.mjs` | PASS | Robot dialogue, routing, UI and privacy regression |
| `node tools/tests/robot-learning-insights.mjs` | PASS | Evidence thresholds and read-only insight behavior |
| `node tools/tests/runtime-render-smoke.mjs` | PASS | Runtime rendering and migration smoke |
| `node tools/tests/quick-help.mjs` | PASS | Legacy compatibility paths |
| `node tools/tests/learning-assistant.mjs` | PASS | Compatibility/no-op contract |
| `node tools/tests/legacy-google-ai.mjs` | PASS | Existing feature-level Google AI entry points |
| All `tools/tests/*.mjs` suites | PASS 30/30 | Every JavaScript regression suite, including the new layout suite |
| `tinycss2` stylesheet parse | PASS | 1,789 top-level CSS nodes; 0 parse errors after repairing the inherited reduced-motion rule |
| `python -m unittest discover -s tools/tests -p 'test_responsive_layout.py' -v` | PASS | Responsive layout regression tests |
| `python -m unittest discover -s tools/tests -p 'test_design_system.py' -v` | PASS | Design system tests |
| `python -m unittest discover -s tools/tests -p 'test_sync_version.py' -v` | PASS | Version marker test suite |
| `python -m unittest discover -s tools/tests -p 'test_project_progress.py' -v` | PASS | Project progress contract |
| `python -m unittest discover -s tools/tests -p 'test_pwa_readiness.py' -v` | PASS | PWA shell readiness |
| `python -m unittest discover -s tools/tests -p 'test_ci_coverage.py' -v` | PASS | Every Python/JS test suite is wired into CI |
| `python tools/validate-data.py` | PASS | 1,137 vocabulary records; no new structural errors/warnings |
| `python tools/validate-learning-content.py` | PASS | No learning-content errors/warnings |
| `python tools/sync-version.py --check` | PASS | All registered version markers and changelog agree |

Summary: all 30/30 JavaScript regression suites passed; 45/45 selected Python tests passed; CSS parsing, vocabulary/content validation and version sync passed. This was a full JavaScript suite run but not a full Python test-suite run.

## Browser/device verification status

A Chromium/Playwright layout run was attempted, but navigation to both the local HTTP and file URL is blocked by the execution environment (`ERR_BLOCKED_BY_ADMINISTRATOR`). Therefore computed visual sizes and screenshots could not be captured here. Desktop 15.6-inch 100% zoom, mobile browser/PWA, iOS/Android, GitHub Actions and GitHub Pages still require user/deployment validation.

## Preservation

- No IndexedDB schema/store changes or migrations.
- No changes to vocabulary/question-bank records, stable IDs or learning content.
- No changes to learner progress keys, onboarding or reminder settings.
- Robot continues to use bundled dialogue and the existing in-memory local read-only progress snapshot. No network/API/server transfer is added.
