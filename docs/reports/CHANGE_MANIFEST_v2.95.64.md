# Change Manifest — v2.95.64

**Base:** `TOEIC_Dictionary_v2.95.63_FullSource.zip`
**Base SHA-256:** `6d43a7f44e1cc84d6ad7f3ee9dae660cceb83c792668d0966ce1060f4aa9ea80`

## Source changes

- `.gitattributes` — added cross-platform LF normalization and binary media rules.
- `.gitignore` — expanded generated/cache/local artifact exclusions.
- `.github/workflows/validate-data.yml` — SHA-pinned official Actions, depth-2 checkout, Git preflight, metadata path filters, full-tree Python compile, duplicate test-step removal.
- `tools/audit-git-commit-readiness.py` — new staged/clean Git commit preflight.
- `tools/audit-repository-integrity.py` — recognizes default unittest discovery pattern and recursively checks test files.
- `tools/tests/test_git_commit_readiness.py` — new real-temporary-repository integration regressions.
- `tools/tests/test_ci_coverage.py` — verifies SHA pins, default test coverage, no duplicate selectors/step names, all Node suites and whole-tree compile.
- `tools/tests/test_repository_integrity.py` — verifies default unittest discovery behavior.
- Version markers in `assets/js/app.js`, `data/manifest.json`, `index.html`, `sw.js` and version documentation: 2.95.63 → 2.95.64.
- `.md` Master, README, changelog, previous-version ledger and test/CI reports updated.

## Generated current-version audit evidence

- `FOUNDATION_A2_ASSESSMENT_QUALITY_v2.95.64.md`
- `TOEIC_ANSWER_LEAKAGE_DIAGNOSTIC_v2.95.64.md`
- `TOEIC_DISTRACTOR_AUDIT_v2.95.64.md`
- `TOEIC_EDITORIAL_EVIDENCE_AUDIT_v2.95.64.md`
- `TOEIC_INDEPENDENT_REVIEW_QUEUE_v2.95.64.md`
- `TOEIC_LISTENING_READINESS_v2.95.64.md`

## Data preservation

`data/manifest.json` is the only changed path beneath `data/`, and its only change is the version marker. All other source data files are unchanged. No UI layout, question content, answer keys, stable identities, learner stores or service-worker cache logic were changed beyond the synchronized release version string.
