# Test Report — TOEIC Dictionary v2.17.0

Date: 2026-11-11  
Release state: local release candidate; no commit/push/deployment is claimed.

## Scope delivered

- Rebalanced the keyed answer position across the 132 reviewed Part 3/4/7 questions. The 27 explicit position changes are recorded in `tools/answer-position-balance-v2.17.0.json`.
- New distributions: Part 3 A10/B10/C10/D9; Part 4 A8/B8/C7/D7; Part 7 A16/B16/C16/D15.
- Each changed item retains its exact v2.16 option and ID order in `previousChoices` / `previousChoiceIds`, plus `previousAnswerIndex` and `choiceOrderRevision`.
- Startup migration maps saved `choiceId` to its current option index; legacy progress without an ID is recovered from v2.16 snapshots. Previous numeric index is preserved as `previousChoiceIndex` when the option moved.
- Historical options from the 12 v2.15.0 distractor revisions remain represented by separate `legacyChoiceIds`. Ambiguous saved text and invalid indices are not guessed. A second migration pass does not write progress again.
- No question/passage/transcript/explanation content, stable question ID, question sequence, vocabulary ID, or question-pool size changed. No IndexedDB database/store/version change and no progress reset.

## Unit-test accounting

| Suite | Result | Execution note |
|---|---:|---|
| Baseline ID integrity | 13/13 PASS | Module run |
| Guarded patch data | 11/11 PASS | Module run |
| Version sync | 12/12 PASS | Each method run separately because grouped discovery timed out in this sandbox |
| Vocabulary validator | 33/33 PASS | Each method accounted for; grouped discovery stalled in this sandbox, isolated methods passed |
| Learning content | 24/24 PASS | Module run |
| Dashboard layout | 6/6 PASS | Module run |
| Design system | 13/13 PASS | Module run |
| Question evidence | 4/4 PASS | Module run |
| Distractor quality | 5/5 PASS | Module run |
| Choice history | 5/5 PASS | Module run |
| Learning detail scope | 3/3 PASS | Module run |
| Choice identity | 9/9 PASS | Module run |
| Answer position balance | 3/3 PASS | Module run |

**Total: 141/141 test methods PASS.** Two slower subprocess-based suites (`sync_version`, `validator`) were accounted for using isolated test-method runs after sandbox module discovery timed out. This is not evidence that the remote GitHub Actions runner has passed.

## Validators and audits

- `python tools/validate-data.py`: 928 vocabulary records; 0 errors; 12 known legacy warnings (DF005=3, EX006=1, FD001=8); 0 added/missing stable IDs.
- `python tools/validate-learning-content.py`: 0 errors, 0 warnings; Listening 102, Reading 109, Grammar 25 lessons / 54 exercises.
- Coverage audit: PASS; 928 vocabulary records, Listening 56 units / 102 questions, Reading 35 resources / 109 questions, Part 7 split 38 single / 25 multiple.
- Answer-to-source evidence audit: all 211 questions indexed; category counts unchanged.
- Distractor/answer audit: 132 questions; 12 option sets previously revised; all four options structurally unique and answer indices valid; new Part 3/4/7 distributions match the target.
- `python tools/sync-version.py --check`: PASS at 2.17.0.
- Python compilation, Service Worker JavaScript syntax, all `assets/js/*.js` syntax and runtime-render/migration smoke: PASS.

- Evidence audit now writes a versioned `TOEIC_EDITORIAL_EVIDENCE_AUDIT_v{manifest version}.md` report instead of overwriting a file named v2.15.0. The current v2.17.0 report maps all 211 answer keys.

## Runtime migration smoke

Node VM smoke exercises Reading, Listening and Grammar progress for: a v2.15-era record without `choiceId`, a v2.16-era record with `choiceId`, an archived distractor from the 12 legacy sets, a moved Listening option, stale-index wrong-answer highlighting, an unknown saved text that must remain untouched, preservation of `correct` / `answeredAt` / `choiceText`, and idempotent second startup.

This is a deterministic runtime simulation, not a real browser IndexedDB migration on the user's existing GitHub Pages origin. Real profile verification remains a release follow-up.

## Package integrity

- Release ZIP: 182 files; CRC check passed; clean extraction compared byte-for-byte with the release working tree: 182/182 exact. SHA-256 is supplied in the `.zip.sha256` sidecar outside the archive.

## Data preservation and release boundary

- Vocabulary: 928/928 stable IDs and 26 A–Z files preserved.
- Listening / Reading / Grammar: 102 / 109 / 25 lessons with 54 exercises unchanged in count.
- Question IDs, source text, explanations and question order unchanged; 27 answer positions updated only through stable option identity mappings.
- IndexedDB remains `toeic-vocabulary-phase1`, version 1, object store `workspace`; no reset or schema bump.
- Remote GitHub Actions after push, GitHub Pages deployment, service-worker update/offline QA in production, real profile migration, and physical iOS/Android/iPad/PC browser QA are **not verified**.
