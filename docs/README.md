# TOEIC Dictionary v2.28.0 — Documentation Center

## Active release window

- **Current candidate — v2.28.0:** [Master status & roadmap](MASTER_STATUS.md), [test report](reports/TEST_REPORT_TOEIC_Dictionary_v2.28.0.md), [coverage](reports/TOEIC_CONTENT_COVERAGE_v2.28.0.md), [Vocabulary Batch 018](batches/TOEIC_VOCABULARY_BATCH_018_v2.28.0.md), [update notes](../V2.28.0_UPDATE_NOTES.txt).
- **Previous baseline — v2.27.0:** [test report](reports/TEST_REPORT_TOEIC_Dictionary_v2.27.0.md), [coverage](reports/TOEIC_CONTENT_COVERAGE_v2.27.0.md), [Batch 017 / Focus Workspace](batches/TOEIC_FOCUSED_LEARNING_AND_VOCAB_BATCH_017_v2.27.0.md), [previous update notes](../V2.27.0_UPDATE_NOTES.txt).

## Central references

- [Compatibility & retirement register](COMPATIBILITY.md) — only current compatibility/deprecation register.
- [Content operations](CONTENT_OPERATIONS.md) — guarded content and release workflow.
- [Design system](DESIGN_SYSTEM.md) — UI implementation rules.
- [Platform benchmark](reference/TOEIC_APP_BENCHMARK_2026.md).
- [Project History](archive/PROJECT_HISTORY.md) — consolidated historical evidence; not current instructions.

## File governance

Keep only the previous and current release generations in `docs/batches/`, `docs/reports/` and root update notes. Before retiring older release-specific files, preview and run `python tools/rotate-release-files.py` / `python tools/rotate-release-files.py --apply`. Update `MASTER_STATUS.md` and `CHANGELOG.md`; do not create another version-specific Master or duplicate roadmap.
