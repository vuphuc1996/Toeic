# Test Report — TOEIC Dictionary v2.95.11

## 1. Scope and release boundary

This report covers the three remaining items from the independent v2.95.10 review:

1. Patch-data audit-log hygiene (`logs/` ignored; every operation records `dry-run`, `apply` or `rollback`).
2. CSS design-token governance: formal specification, identity-based ratchet, RULE-DRIFT guard, CI registration and a token migration limited to the PWA update banner.
3. Owner-run manual acceptance checklist with all results initially marked `Chưa kiểm`.

The user-requested Robot Buddy progressive local response and Flashcard fixed maximum of 10 are retained. No vocabulary IDs, headwords, topics, learning questions, answer keys, learner records, IndexedDB schema or learner localStorage keys were changed. No broad CSS conversion was performed.

## 2. Changed files by item

### Item 1 — patch-data log hygiene

- `.gitignore` — ignores `logs/`.
- `tools/patch-data.py` — adds explicit `mode` to operation-level and batch-level log records; dry-run is not represented as apply.
- `tools/tests/test_patch_data.py` — tests dry-run/apply/rollback mode records and Git ignore behavior.

Commit: `b4fd07b fix(data): classify audit log modes and ignore logs`.

### Item 2 — design-token governance

- `docs/DESIGN_SYSTEM.md` — normative section covering one font stack, nine named text roles with line-height, five allowed font weights, radius/shadow/spacing scales, semantic color roles, four responsive bands, shared component recipes and token-change governance.
- `tools/design-token-rules.json` — canonical rule parameters.
- `tools/audit-design-tokens.py` — CSS scanner, identity-based warning/error ratchet and rules-file hash check.
- `tools/design-token-baseline.json` — legacy identity baseline; baseline is never auto-updated by normal audit.
- `tools/tests/test_audit_design_tokens.py` — valid, invalid, legacy, new violation, resolved issue, immutable baseline and RULE-DRIFT cases.
- `.github/workflows/validate-data.yml` — runs token-audit tests and audit in CI.
- `assets/css/app.css` — moves PWA update banner typography, color, spacing, radius and shadow to existing shared tokens.
- `docs/reports/DESIGN_TOKEN_AUDIT_BASELINE_v2.95.11.md` — baseline and measurement notes.

Commit: `32c7da2 feat(ui): add CSS design-token ratchet audit`.

### Item 3 — owner-run manual acceptance and release synchronization

- `docs/reports/MANUAL_ACCEPTANCE_CHECKLIST.md` — 14 manual checks; all 14 start at `Chưa kiểm`.
- `tools/sync-version.py` and `tools/tests/test_sync_version.py` — synchronize current version references in README/current-version documentation as well as app markers.
- `docs/MASTER_STATUS.md`, `docs/CHANGELOG.md`, `docs/README.md`, `docs/versions/CURRENT_VERSION.md`, `docs/versions/PREVIOUS_VERSION.md` — update the release ledger and link acceptance/test artifacts.
- `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.95.11.md` and `docs/reports/COMMAND_LOG_INDEX_v2.95.11.md` — this report and command index.

Release version was changed only using `python tools/sync-version.py --set 2.95.11 --apply`.

## 3. Automated tests and exact outcomes

### 3.1 Focused Python suites

| Command / module | Tests | Result | Elapsed (test runner) | Process exit |
|---|---:|---|---:|---:|
| `test_patch_data.py` | 20 | PASS | 16.904 s | 0 |
| `test_audit_design_tokens.py` | 8 | PASS | 0.016 s | 0 |
| `test_ci_coverage.py` | 3 | PASS | 0.003 s | 0 |
| `test_sync_version.py` | 12 | PASS | 10.892 s | 0 |
| `test_design_profile.py` | 6 | PASS | 0.734 s | 0 |
| `test_design_system.py` | 19 | PASS | 0.002 s | 0 |
| `test_responsive_layout.py` | 7 | PASS | 0.006 s | 0 |
| `test_visual_composition.py` | 8 | PASS | 0.001 s | 0 |
| `test_learning_surface_consistency.py` | 5 | PASS | 0.004 s | 0 |
| `test_alphabet_sound_lab.py` | 7 | PASS | 0.001 s | 0 |
| **Total focused Python coverage** | **95** | **95/95 PASS** | **28.563 s summed test-runner time** | **0 for each process** |

These are ten specifically executed modules. This count is not the total repository Python suite.

### 3.2 JavaScript regression suites

- Registered `.mjs` suites: **37/37 PASS**.
- Aggregate runner exit code: **0**.
- Log: `30-javascript-regressions.log`.

### 3.3 Validators, audits and synchronization

| Command | Result | Exit |
|---|---|---:|
| `python tools/validate-data.py` | 1,141 canonical records; ID additions 0 / missing 0; hash matches; 0 errors / 0 warnings | 0 |
| `python tools/validate-learning-content.py` | Listening 121 units / 239 questions; Reading 65 / 263; Grammar 50 / 137; Part 5 practice 80; 0 errors / 0 warnings | 0 |
| `python tools/audit-repository-integrity.py` | 367 references/data files; 0 errors / 0 optional warnings | 0 |
| `python tools/validate-part1-photo-assets.py` | 9/9 Part 1 photo assets valid | 0 |
| `python tools/audit-design-tokens.py` | 2,778 legacy identities; 0 new violations; no RULE-DRIFT | 0 |
| `python tools/sync-design-profile.py --check` | 54 tokens and 406 legacy typography floor selector groups synchronized | 0 |
| `python tools/sync-version.py --check` | All app, SW, HTML and release-document version markers aligned at 2.95.11 | 0 |
| `git diff --check` | No whitespace errors | 0 |

The baseline vocabulary set hash is `adccbdb4c98872207d2bede7bdc530e1c079bbd8b3679e7e4f6288054c7e404b`.

## 4. CSS measurement: tool definition and comparison

Claude's supplied v2.95.10 scan reported: 979 unique hex strings / 1,508 uses; 128 font-size values / 918 declarations; 70 non-standard font-weight declarations; 47 radius values; 69 box-shadow values; 114 `!important`; 25 breakpoint values; 34 keyframes.

The new scanner's current v2.95.11 report is:

- Hex strings: 979 unique / 1,508 occurrences.
- `font-size`: 128 unique / 921 declarations.
- `font-weight`: 9 unique / 167 declarations across all CSS; the five allowed numeric values are 400/500/600/700/800.
- `border-radius`: 47 unique / 351 declarations.
- `box-shadow`: 70 unique / 80 declarations.
- Media breakpoint values: 24 unique / 116 occurrences.
- `!important`: 114 occurrences.
- `@keyframes`: 34.

The `font-size` declaration count (921 vs Claude's 918) and breakpoint count (24 vs 25) do not match. They are explicitly reported rather than silently normalized; parser/tokenization definitions differ and need a shared measurement definition before treating the count delta as a source regression. Raw hex count agrees. The box-shadow unique-value metric is 70 in the current scan because the PWA banner now references a shared token; raw value cardinality is not the legacy-warning count.

Ratchet outcome:

- Baseline before banner migration: 2,781 legacy identities / 3,000 occurrences.
- Three exact update-banner violations were resolved and removed from baseline; no new baseline identities were added.
- Current legacy baseline: 2,778 identities / 2,997 occurrences.
- Current new violations: 0.
- Rule hash matches baseline; `RULE-DRIFT` is not present.
- All remaining legacy findings are WARNING, not CI failure. New identities/values, increased occurrences and rule drift fail CI.

## 5. Baseline / data safety

- Canonical vocabulary ID baseline remains 1,141 unique IDs.
- Validator reports zero additions and zero missing IDs.
- No vocabulary A–Z data record, `id`, `word` or `topics` field was modified in this release work.
- No learning question, answer key, learner record, IndexedDB schema or learner localStorage key was changed.
- `logs/` is ignored by Git; dry-run still records a log row for traceability and labels it `mode: dry-run`.
- Existing patch file contents were preserved; log and allowlist governance remain intact.

## 6. Incomplete / not verified

- The full Python `unittest discover` sweep did not finish in this execution environment: the orchestration process hit its execution time limit before a complete result was produced. It is **not** reported as PASS. The ten focused suites listed above are the complete targeted Python results counted here.
- Claude previously reported 433 Python tests passing on the supplied v2.95.10 package in its own Python 3.12.3 / Node 22 environment. That result is a user-provided independent v2.95.10 finding, not a claim that all 433 were rerun on v2.95.11 here.
- GitHub Actions on the remote repository, GitHub Pages deployment and actual `/Toeic/` browser routing have not been run from this workspace.
- PWA installation, first-time offline, cached offline, cache replacement, two-tab update, iPhone Safari TTS, Android Chrome TTS, Flashcard behavior with an old real browser profile and visual Part 1 cropping have not been tested on physical browsers/devices.
- All 14 rows in `MANUAL_ACCEPTANCE_CHECKLIST.md` remain `Chưa kiểm` until the owner performs them and records date/device/result.
- `calm-study-blue` remains a conditional development/audit default. `design/design-profile.json` remains `proposed-default-awaiting-user-preferences`; no owner approval is inferred.
- No GitHub push or deployment was made.

## 7. Evidence files

See `COMMAND_LOG_INDEX_v2.95.11.md` and the separately supplied `TOEIC_v2.95.11_Test_Logs.zip`. The test archive includes the full output for every focused test/validator command and a record of the interrupted full-suite attempt.
