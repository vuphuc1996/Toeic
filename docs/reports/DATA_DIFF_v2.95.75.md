# Data Difference Report — v2.95.75 vs v2.95.74

## Baseline

- Sole predecessor: verified local workspace snapshot `v2.95.74` (preserved ahead of older GitHub `candidate` `cfae6ce`, which was at `v2.95.73`).
- Baseline counts preserved: `1,181` canonical vocabulary headwords (`A`–`Z`), `567` Related Glossary entries, `145` Listening units / `295` questions, `73` Reading units / `287` questions, `58` Grammar lessons / `169` exercises, and `80` Separate Part 5 questions.

## `data/` comparison

- Files in target: **70**
- Added / removed data files: **0 / 0**
- Modified data files:
  - `data/manifest.json`: `version` `2.95.74` → `2.95.75`; canonical headword count (`1,181`), letter counts, CEFR counts, and `releaseRepairProfiles` are unchanged.
  - `data/learning-path/objective-outcomes.json`: updated `policy.scopeWarning` and added documentation/wiring metadata (`runtimeWiring`, `measurementRule`, `runtimeStatusNote`) across the `11` objectives and `33` criteria while preserving all objective/criterion IDs, `status` values (`6/33` Foundation `instrumented_*`, `27/33` `criteria_defined_not_yet_instrumented`), thresholds, and `minimumUniqueItems`.
- All remaining `68` data files (including `data/vocabulary/A.json`–`Z.json`, `data/related-terms.json`, `data/categories.json`, `data/listening/listening-library.json`, `data/readings/reading-library.json`, `data/grammar/lessons.json`, `data/practice/part5-sentence-completion.json`, Foundation banks, and `data/learning-path/objective-resource-map.json`) are byte-identical.

## Protected identities and learning data

- Canonical vocabulary: `1,181` headwords; IDs `+0/−0` (`sha256` ID set `b5dde212c7de6fe6…`).
- Related Glossary: `567` term identities and `meaning_vi` preserved verbatim (`2` low-priority `short-definition-review` flags remain).
- Question banks & reserve gates: no question IDs, passage IDs, choice IDs, answer keys, Mock eligibility flags, or reserve gates (`193` Listening, `87` Reading Part 7, `80` Separate Part 5) changed.
- Learner storage: no IndexedDB v1 store/schema or localStorage key migrations changed.

## Validation

- `tools/validate-data.py`: **PASS** (`1,181` records, `+0/−0` IDs, `0` errors, `0` legacy warnings).
- `tools/validate-learning-content.py`: **PASS** (`0` errors, `0` warnings).
- `tools/audit-learning-outcomes.py`: **PASS** (`11/11` objectives, `33` criteria, `6/33` criterion-level instrumented, `11/11` group-level wired).
