# Change Manifest — TOEIC Dictionary v2.95.81

**Branch:** `candidate`  
**Sole predecessor:** `a16a3e4a51917e687b92e404ab1c785a393dfb0f` (v2.95.80)  
**Target:** Part 7 cross-document evidence guard hardening

## Changes

1. `tools/audit-objective-criterion-map.py`
   - Normalize source labels without coercing invalid types.
   - Require a non-empty documents list, valid unique document labels and distinct valid source labels.
   - Require one non-empty string quote per label and verify it against the matching document.
   - Match each declared source label as a complete phrase in `evidenceBasis`, rather than a loose substring.
2. `tools/tests/test_objective_criterion_map.py`
   - Add regression cases for duplicate/ambiguous document labels, duplicate source labels, non-string labels/quotes and partial-word matches.
3. Release shell only
   - Advance canonical/package/app/HTML/Service Worker/mock-engine version and cache markers to v2.95.81.
   - Add release notes, status and verification documents.

## Unchanged boundaries

- Mapping remains 1,103 links across 638 existing stable question IDs.
- TOEIC instrumentation remains 22/27; Foundation 6/6; total 28/33.
- Five unsupported criteria remain uninstrumented. No Listening reserve item is mapped or promoted.
- No vocabulary/learning bank content, question text, choice/answer keys, stable IDs, Mock eligibility, learner IndexedDB schema/data, UI, navigation, Robot Buddy behavior or hosting architecture changes.
- `main` remains at `256ca21461e78a7685bed773ddd622a64050e33a`.

## Acceptance

New exact-commit Python/Validate/mapping/version-sync/Pages results are pending. Do not treat this manifest as proof of acceptance or package generation.
