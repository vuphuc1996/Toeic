# Test Report — TOEIC Dictionary v2.95.10

**Code base:** v2.95.9 plus separately committed P0 fixes.  
**Date:** 2026-11-19.  
**Git branch:** `work-v2.95.10` (local only; no remote push).

## Changes

1. Removed the 5-card Flashcard option and all runtime branches for five-card sessions. Học tổng hợp, topics, continue/next batch and wrong-answer review now share a maximum of 10 cards.
2. Expanded vocabulary ID baseline from 928 to 1,141 only after proving 213 additions and zero deletions.
3. Hardened patch operations with immutable protected paths, explicit exact `allowedPaths`, whole-batch rejection on whitelist violation and operation-level JSONL logs. If the final audit record fails after data replacement, original file bytes are restored before returning an error.
4. Added user-approved Service Worker update activation after first install, including an update banner and `SKIP_WAITING` message. Updated typography uses shared tokens.

## Automated results

| Verification | Result |
|---|---:|
| JavaScript `.mjs` suites | **37/37 PASS** |
| `test_baseline_ids.py` | **13/13 PASS** |
| `test_patch_data.py` | **17/17 PASS** |
| `test_practice_mode_fallback.py` | **6/6 PASS** |
| `test_pwa_readiness.py` | **3/3 PASS** |
| `test_ci_coverage.py` | **3/3 PASS** |
| `test_design_profile.py` | **6/6 PASS** after using shared typography tokens in the PWA banner |
| `test_sync_version.py` | **12/12 PASS** |
| `test_release_rotation.py` | **6/6 PASS** |
| `test_repository_integrity.py` | **1/1 PASS** |
| Vocabulary validator | **PASS** — 1,141 records, 0 added IDs, 0 missing IDs, 0 errors, 0 warnings |
| Learning-content validator | **PASS** — 0 errors, 0 warnings |
| Repository integrity | **PASS** — 366 references/data files, 0 errors, 0 optional warnings |
| Service Worker simulator | **PASS** — first install, user-approved update, failed install, optional assets, cache cleanup and 404 fallback |
| `node --check assets/js/app.js`, `node --check sw.js` | **PASS** |
| `git diff --check` | **PASS** |
| Workflow `continue-on-error` scan | **0 occurrences** |

The listed complete Python modules total **67 passing test cases**. This is a focused set, not the full Python test inventory.

## Explicitly incomplete / not claimed

- `test_validator.py` did not finish within the available execution window. A current full-module run was interrupted while executing; no complete module result is claimed. The actual full-data `python tools/validate-data.py -v` command did pass with 0 errors and 0 warnings.
- A broad Python module sweep was interrupted by the execution limit; do not interpret it as a complete 54/54 Python module run.
- The full aggregate Python discovery command did not complete.
- Remote GitHub Actions and deployed GitHub Pages were not run from this environment.
- Browser-level animation/layout, real two-tab update consent, PWA install/offline/reconnect, iOS Safari and Android Chrome TTS, audible cadence and physical-device behavior remain unverified.

## Data and storage safety

- Canonical vocabulary JSON files A–Z were not changed. No `id`, `word`, or `topics` field was patched.
- No TOEIC Listening/Reading/Grammar question, answer key or editorial status was changed. No pending item was promoted to Mock eligibility.
- Existing patch operation payload values were not changed; only their exact `allowedPaths` metadata was added.
- IndexedDB remains `toeic-vocabulary-phase1`, schema version 1, store `workspace`. Learner records and localStorage keys were not reset, migrated or deleted.
- No external AI/API, backend or learner-data transfer was added.

## Commit separation

| Commit | Scope |
|---|---|
| `d51798a` | Remove the 5-card Flashcard setting; fixed maximum 10 across flows |
| `9818888` | Expand baseline to all 1,141 vocabulary IDs |
| `d19a836` | Protect patch paths, require `allowedPaths`, write per-operation logs |
| `4879bb1` | Restore source files if final patch audit logging fails |
| `d1627bb` | Require user approval for subsequent Service Worker updates |
| `5bc5d6c` | Use shared typography tokens in the update banner; restore design-profile check |

Release-version synchronization and docs are captured in the final release metadata commit; no GitHub push was performed.

## Command logs

The companion `TOEIC_v2.95.10_Test_Logs.zip` contains the exact command outputs, exit codes where captured, the 37-suite JavaScript log, focused Python logs, final post-fix verification (`25-final-verification.log`), validator outputs and explicitly incomplete sweep logs. `COMMAND_LOG_INDEX_v2.95.10.md` explains which attempts completed and which were interrupted.
