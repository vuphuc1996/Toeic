# Learner-local Objective Progress Integrity Audit

## Purpose

`auditObjectiveProgress(progress, resourceMap)` is a read-only integrity diagnostic for the learner-local Learning Outcome Evidence ledger. It is intentionally separate from content inventory, score calculation, editorial approval and mastery decisions.

## Safety contract

- The function never writes to IndexedDB and never mutates the supplied progress object.
- It never repairs, deletes, migrates, merges or replaces learner records.
- It reports issue codes and ledger paths only; it does not include answer text or question content.
- Unknown objective IDs are reported as `orphan_objective` warnings. They are retained; an old objective may still be needed to interpret historical evidence.
- Structural evidence errors are marked `error`; recoverable metadata problems such as invalid optional duration or recall deadline are warnings.
- `valid` means no structural errors were found. It does not mean evidence is pedagogically sufficient, independently reviewed, or proof of mastery.

## API

```js
import { auditObjectiveProgress } from './assets/js/learning-outcome-progress.js';
const report = auditObjectiveProgress(progress, resourceMap);
```

The report includes `valid`, `issueCount`, `errorCount`, `warningCount`, `objectiveCount`, `itemCount`, `attemptCount` and `issues[]`. Each issue has a stable `code`, a local ledger `path`, and a `severity`.

## Current checks

- Ledger and objective container shape; supported positive integer schema version when present.
- Objective identity against the current resource map, without deleting unknown history.
- Item shape, latest correctness and answer timestamp.
- Attempt array shape, correctness, answer timestamp and optional non-negative duration.
- Optional recall deadline and recall-check record shape.
- Explanation rubric latest ratings and historical attempt shape.
- Latest summary fields are compared with the final stored attempt; disagreement is a warning and never triggers automatic repair.
- Resource maps and optional nested ledger branches are read defensively; malformed records are ignored by summaries and reported by the audit rather than causing a dashboard exception.
- Write operations reject non-finite or negative timestamps and deduplicate objective IDs before appending evidence.

## Explicit non-goals

This diagnostic does not infer learner ability, calculate CEFR/ETS scores, determine mastery, judge content quality, promote reserve questions, access external services, or expose learner progress to Robot Buddy. It does not change the IndexedDB schema or PWA UI.

## Verification

Runtime regression coverage is in `tools/tests/learning-outcome-progress.mjs`; Python CI wrapper is `tools/tests/test_learning_outcome_progress.py`. Tests include clean data, malformed structural data, recoverable warnings, orphan retention, read-only non-mutation, malformed nested branches, invalid timestamp rejection, duplicate objective IDs and latest-attempt mismatch reporting.
