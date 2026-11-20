# Test Report — TOEIC Dictionary v2.95.12

Generated: 2026-11-19 17:55 ICT (local candidate workspace)

## Candidate identity

- Baseline: v2.95.11 at Git commit `daab38d` (`docs(release): publish v2.95.11 acceptance and evidence`).
- Candidate source: v2.95.12, currently local and not deployed.
- Version synchronization: `python tools/sync-version.py --check` — exit 0; all inspected markers match `data/manifest.json`.

## Summary

| Area | Result | Evidence |
|---|---:|---|
| JavaScript regression | **38/38 PASS** | All 38 `.mjs` commands listed in `.github/workflows/validate-data.yml` ran individually; total about 1.84 seconds |
| Focused Python regression | **147/147 PASS** | 13 modules run individually; see Command Log Index |
| Vocabulary validation | **PASS** | 1,141 records; 0 ID additions, 0 missing IDs; 0 errors and 0 legacy warnings |
| Learning-content validation | **PASS** | Listening 239 questions, Reading 263, Grammar 50/137, Part 5 practice 80; 0 errors / 0 warnings |
| Repository integrity | **PASS** | 372 references/data files; 0 errors / 0 optional warnings |
| Design-token ratchet | **PASS** | 2,778 known legacy warning identities; 0 new violations; no ruleset drift |
| Version sync | **PASS** | All release markers synchronized to v2.95.12 |
| Patch replay | **PASS** | Four vocabulary patches plus related-term patch replayed from v2.95.11 baseline into a clean temporary tree; eight A–Z files and `related-terms.json` match candidate byte-for-byte |
| JavaScript / Python syntax | **PASS** | `node --check` for all `assets/js/*.js` and `sw.js`; `python -m compileall -q tools` |
| Git whitespace check | **PASS** | `git diff --check` |

## Python unit modules (13 modules / 147 test cases)

| Module | Tests | Result |
|---|---:|---|
| `test_patch_related_terms.py` | 11 | PASS |
| `test_vocabulary_detail_examples.py` | 15 | PASS |
| `test_vocabulary_family_links.py` | 6 | PASS |
| `test_baseline_ids.py` | 13 | PASS |
| `test_patch_data.py` | 20 | PASS |
| `test_ci_coverage.py` | 3 | PASS |
| `test_audit_design_tokens.py` | 8 | PASS |
| `test_learning_content.py` | 34 | PASS |
| `test_repository_integrity.py` | 1 | PASS |
| `test_design_system.py` | 19 | PASS |
| `test_responsive_layout.py` | 7 | PASS |
| `test_vocabulary_batch_012.py` | 4 | PASS |
| `test_design_profile.py` | 6 | PASS |
| **Total** | **147** | **PASS** |

The modules were run independently with `python -m unittest discover -s tools/tests -p '<module>' -v`. No full Python test-inventory total is claimed. `test_validator.py` was not run as a unit module in this candidate pass; the actual `tools/validate-data.py` command did run successfully.

## Data and content measurements

### Vocabulary

- Canonical headwords: 1,141; stable ID set unchanged (`ID: thêm 0, mất 0`).
- Multi-sense headwords: 30 → 39.
- Examples associated with multi-sense entries: 61 → 81.
- Related-term glossary: 347 → 369 entries.
- Exact-term unmatched synonym/antonym occurrences: 546 → 528 (custom exact-term comparison; not the validator's 333/817 field-level measure).
- Metadata present: US IPA 1,048/1,141 (91.8%); word-family records 276 (24.2%); verb-form records 329 (28.8%); collocation records 971 (85.1%).
- All new definitions, examples and related-term glosses remain provisional and **pending independent lexical review**.

### Learning-content inventory

- Listening: 121 units / 239 questions; 102 Mock-eligible and 137 pending independent review.
- Reading: 65 resources / 263 questions; Part 7 86 single-passage / 85 multiple-passage questions.
- Grammar: 50 lessons / 137 exercises.
- Separate Part 5 Sentence Completion practice: 80 questions, practice-only and review-pending.
- No reserve item was promoted to Mock eligibility.

### Design-token ratchet

- Current metrics from `tools/audit-design-tokens.py`: 979 distinct hex colors / 1,508 occurrences; 128 font-size values / 926 declarations; 9 font-weight values / 169 declarations; 47 border-radius values / 352 declarations; 70 box-shadow values / 80 declarations; 24 breakpoint values / 116 occurrences; 114 `!important`; 34 keyframes.
- Baseline identities: 2,778; current legacy identities: 2,778; resolved: 0; new violations: 0.
- The scanner's metrics may differ from external scans that use different CSS parsing/counting rules. Its identity-level ratchet is the CI gate; no baseline entries were added to hide new warnings.

## Changes exercised by tests

1. Multi-sense vocabulary expansions, sense-linked example indexing, identity/topic preservation, `claimant → claim (n)` and `order → purchase order`.
2. The 22 Cambridge-sourced related-term glosses and a strict patch tool with exact Cambridge host validation, required-field checks, duplicate detection, SHA-256 precondition, dry-run/apply/rollback, permission preservation and byte-exact restoration if audit logging fails.
3. Flashcard fixed maximum 10 remains; removed 5-word setting remains absent. Flashcard back now displays additional meanings and the example matching each extra sense. The helper escapes HTML and produces no empty panel for a single-sense word.
4. The new Flashcard helper is included in both Service Worker `REQUIRED` and `APP_SHELL` precache arrays.
5. Existing Robot Buddy progressive streaming and user-consent Service Worker lifecycle regressions remain green.

## Not verified / not run

- No GitHub push, remote GitHub Actions run or GitHub Pages deployment.
- No real browser visual rendering or owner acceptance; the 18-row manual checklist remains **18/18 Chưa kiểm**.
- No real PWA install, offline first-use, offline-after-online, two-tab update or physical-device test.
- TTS quality on iPhone Safari and Android Chrome remains unverified.
- No independent second-person lexical review of the nine expanded headwords or 22 glossary additions.
- Full Python inventory and `test_validator.py` unit module are not claimed as run; only the 13 listed Python modules and the actual data/content validator CLIs are counted.

## Data safety

- No vocabulary ID, `word` or `topics` value changed.
- No question, answer key, learner progress record, IndexedDB schema, localStorage learner key or storage migration was changed.
- The vocabulary/related-term data patches were replayed from a clean v2.95.11 Git archive in a temporary directory and produced byte-identical results to the candidate files.
