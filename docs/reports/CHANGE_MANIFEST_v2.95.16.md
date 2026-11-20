# Change Manifest — TOEIC Dictionary v2.95.16

- Version: 2.95.16; packaging tooling only.
- Added `tools/package_source.py`: ZIP exports committed Git files only and wraps content in one `Toeic_Dictionary_vX.Y.Z/` root.
- Excludes logs, archives, caches, nested ZIP/bundle/log files, release output folders and `.git` metadata.
- Requires tracked files to be committed before packaging; ignores untracked files by design.
- Added `tools/tests/test_package_source.py` (3 tests) for single-root, tracked-only/exclusion, dirty tracked files and version validation.
- No canonical vocabulary, learner records, application runtime, exam content or data schema changed.
- Prior v2.95.16/17 IPA batch claims from earlier chat could not be recovered as files in this workspace; this candidate is reconstructed from the available v2.95.15 FullSource and does not include those IPA changes.
