# Change Manifest — v2.95.59

## Canonical source
- Base: `TOEIC_Dictionary_v2.95.58_FullSource.zip`
- Base SHA-256: `67dd7d59a8f63bdb1307780dd95dd52e75f1b25af143ac0cef2a42e938b3d5cc`
- Target: v2.95.59

## Changes
- Add `tools/audit-item-complexity.py` and `tools/tests/test_item_complexity_review.py`.
- Add generated `docs/reports/TOEIC_ITEM_COMPLEXITY_REVIEW_v2.95.59.md`.
- Register Python syntax, focused regression and report generation in `.github/workflows/validate-data.yml`.
- Update release version markers, Master Status, Current/Previous Version ledgers, README, Changelog and release reports.
- Regenerate versioned evidence, distractor and answer-leakage reports.

## Protected content
- Listening and Reading question-library files are byte-identical to v2.95.58.
- No question text, IDs, choice IDs/order, answer keys, source evidence, Mock eligibility, reserve status, vocabulary data, learner records, IndexedDB schema or UI layout changed.
- Listening reserve 193 and Reading reserve 87 remain pending independent review and excluded from Mock.

## Scope boundary
The new complexity report is non-calibrated and diagnostic only. It must not be presented as CEFR/ETS difficulty or psychometric validation.
