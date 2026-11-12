# Test report — TOEIC Dictionary v2.9.11

Date: 2026-11-09  
Base: v2.9.10  
Target: v2.9.11

## Release gates

| Check | Result |
|---|---|
| `tools/validate-data.py` | PASS — 928 records, 0 ERROR, 12 preserved legacy WARNING |
| `tools/sync-version.py --check` | PASS — manifest, Service Worker, index, README, Master and CHANGELOG markers all 2.9.11 |
| `py_compile` | PASS — validator, sync-version and patch tool |
| JavaScript syntax | PASS — `sw.js` and all `assets/js/*.js` checked with `node --check` |
| APP_SHELL integrity | PASS — 65 entries, 0 missing files |
| Workflow YAML | PASS — parsed successfully; `validate` job found |
| Word-family targets | PASS — all added family targets that are dictionary headwords resolve to current records |
| ID integrity | PASS — 928 IDs unchanged; SHA-256 `dd1705e64c8df4ad7ebca188a6ad856fff1d180d99730d2d77d2ba6fbdc12656` |

## Unit tests

| Test module | Result |
|---|---:|
| `test_baseline_ids` | 13/13 PASS |
| `test_patch_data` | 11/11 PASS |
| `test_sync_version` | 12/12 PASS |
| `test_validator` | 26/33 confirmed PASS (25 completed in grouped run; `test_unknown_topic` also passed when isolated) |

**Overall:** 62/69 test cases confirmed PASS. Seven validator test cases remain unverified in this run because the Python 3.13.5 sandbox process intermittently stalled during repeated subprocess-based tests. This is not reported as a full-suite PASS. The production validator itself completed successfully with 0 new ERROR and 12 legacy WARNING.

## Remaining legacy warnings

- DF005: 3 violations across 3 records.
- EX006: 1 violation across 1 record.
- FD001: 8 violations across 7 records.
- IP001/IP004: 0; all 7 IPA-related legacy entries were corrected and removed from the baseline through `--tighten-baseline`.

## Not tested / not claimed

- GitHub Actions on the remote repository was not run (no push performed).
- GitHub Pages deployment was not performed or verified.
- iPhone Safari, Android Chrome, tablet and other physical-device QA were not performed.
- v2.10.0 UX, Listening TTS and personal IndexedDB `baseSig` migration were not modified or tested in this release.
