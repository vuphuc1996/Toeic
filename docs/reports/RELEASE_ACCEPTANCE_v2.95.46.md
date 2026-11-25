# Release Acceptance Run — v2.95.46

- Timestamp (UTC): 2026-11-24T04:55:06Z
- Overall status: **PASS**

| Check | Status | Exit | Duration (s) |
|---|---|---:|---:|
| repository_integrity | PASS | 0 | 0.856 |
| data_validator | PASS | 0 | 1.242 |
| learning_content_validator | PASS | 0 | 0.659 |
| version_sync | PASS | 0 | 0.664 |
| listening_readiness | PASS | 0 | 0.662 |
| question_evidence | PASS | 0 | 0.699 |
| distractor_audit | PASS | 0 | 0.709 |
| learning_outcomes | PASS | 0 | 0.716 |
| major_release_audit | PASS | 0 | 0.660 |
| related_glossary_backlog | PASS | 0 | 0.700 |
| editorial_review_queue | PASS | 0 | 0.731 |
| full_python_suite | PASS | 0 | 196.076 |

## Commands

### repository_integrity

`/opt/pyvenv/bin/python tools/audit-repository-integrity.py`

Status: **PASS**

```text
Repository integrity preflight: 420 local references/data files inspected
Errors: 0 | Optional warnings: 0
```

### data_validator

`/opt/pyvenv/bin/python tools/validate-data.py`

Status: **PASS**

```text
TOEIC data validation — 1141 bản ghi, version 2.95.46, baseline có
ID: thêm 0, mất 0; sha256 tập ID adccbdb4c9887220…
Baseline: legacy (WARNING) 0, mới (ERROR từ luật DEBT) 0, đã sửa (resolved) 0
Coverage: ipa=1062 (93%), word_family=276 (24%), verb_forms=329 (29%), collocations=971 (85%), synonyms=405 (35%), antonyms=210 (18%), multi_sense=49 (4%)
INFO: ví dụ <5 từ=0, định nghĩa trùng giữa các từ=4, IPA thiếu=79, syn/ant chưa có nghĩa=248/804, CEFR từ≠sense=9, C1=122, tham chiếu asset đã kiểm=28
RESULT: PASS — 0 ERROR, 0 WARNING (legacy)
```

### learning_content_validator

`/opt/pyvenv/bin/python tools/validate-learning-content.py`

Status: **PASS**

```text
TOEIC learning content validation
Listening: 145 units / 295 questions
  Part 1: 9 units / 9 questions
  Part 2: 61 units / 61 questions
  Part 3: 41 units / 123 questions
  Part 4: 34 units / 102 questions
Reading: 73 units / 287 questions
  Part 5: 13 units / 60 questions
  Part 6: 8 units / 32 questions
  Part 7: 52 units / 195 questions
Part 7 passage mix: 110 single-passage / 85 multiple-passage questions
Grammar: 58 lessons / 169 exercises
TOEIC Part 5 Sentence Completion: 80 curated questions (practice only; pending independent review)
  Part 5 tagged: 31 lessons / 108 exercises
  Part 6 tagged: 16 lessons / 51 exercises
Errors: 0 | Warnings: 0
```

### version_sync

`/opt/pyvenv/bin/python tools/sync-version.py --check`

Status: **PASS**

```text
Phiên bản chuẩn (data/manifest.json): 2.95.46
  [OK  ] app.js release version: 2.95.46
  [OK  ] sw.js version: 2.95.46
  [OK  ] index.html <title>: 2.95.46
  [OK  ] index.html sidebar: 2.95.46
  [OK  ] index.html phase-note: 2.95.46
  [OK  ] index.html footer: 2.95.46
  [OK  ] docs/README.md title: 2.95.46
  [OK  ] docs/README.md current test report: 2.95.46
  [OK  ] docs/README.md current command log: 2.95.46
  [OK  ] docs/versions/CURRENT_VERSION.md source: 2.95.46
  [OK  ] docs/versions/CURRENT_VERSION.md release package: 2.95.46
  [OK  ] docs/versions/CURRENT_VERSION.md test report: 2.95.46
  [OK  ] docs/MASTER_STATUS.md version line: 2.95.46
  [OK  ] docs/CHANGELOG.md: có mục cho 2.95.46
RESULT: PASS — mọi vị trí đồng bộ
```

### listening_readiness

`/opt/pyvenv/bin/python tools/audit-listening-readiness.py`

Status: **PASS**

```text
docs/reports/TOEIC_LISTENING_READINESS_v2.95.46.md
eligible=102; pending=193; total=295
```

### question_evidence

`/opt/pyvenv/bin/python tools/audit-question-evidence.py`

Status: **PASS**

```text
Wrote docs/reports/TOEIC_EDITORIAL_EVIDENCE_AUDIT_v2.95.46.md
Total indexed questions: 582
Listening: reserve-pending-independent-review=193, response-fit-checked=25, lexical-evidence=34, direct-text-match=32, manual-paraphrase-verified=3, photo-source-reviewed=8
Reading: direct-text-match=34, lexical-evidence=26, explicit-source-evidence=132, manual-paraphrase-verified=3, grammar-checked=60, context-fit-checked=32
```

### distractor_audit

`/opt/pyvenv/bin/python tools/audit-distractors.py`

Status: **PASS**

```text
Wrote docs/reports/TOEIC_DISTRACTOR_AUDIT_v2.95.46.md
Questions in audit scope: 264; reserve structural checks: 156; revisions: 12
Part 3: A=10, B=10, C=10, D=9
Part 4: A=8, B=8, C=7, D=7
Part 7: A=49, B=49, C=49, D=48
Structural audit: PASS — unique choices and valid answer keys across review scope
```

### learning_outcomes

`/opt/pyvenv/bin/python tools/audit-learning-outcomes.py`

Status: **PASS**

```text
PASS: 11/11 objectives; 33 measurable outcome criteria; 6/33 outcomes have an evidence-collection path.
Foundation instrumentation: 6/6 outcomes wired; learner records and mastery are not inferred from wiring.
NOTE: production ratings are learner self-reports; practice thresholds and delayed recall do not certify CEFR/ETS mastery.
```

### major_release_audit

`/opt/pyvenv/bin/python tools/audit-major-release.py`

Status: **PASS**

```text
{
  "version": "2.95.46",
  "vocabulary": {
    "headwords": 1141,
    "ipa_us": 1062,
    "word_family": 276,
    "verb_forms": 329,
    "collocations": 971,
    "synonyms": 405,
    "antonyms": 210
  },
  "vocabularyFieldCoverage": {
    "ipa_us": {
      "count": 1062,
      "percent": 93.1
    },
    "word_family": {
      "count": 276,
      "percent": 24.2
    },
    "verb_forms": {
      "count": 329,
      "percent": 28.8
    },
    "collocations": {
      "count": 971,
      "percent": 85.1
    },
    "synonyms": {
      "count": 405,
      "percent": 35.5
    },
    "antonyms": {
      "count": 210,
      "percent": 18.4
    }
  },
  "relatedGlossary": {
    "entries": 567,
    "uniqueEntries": 567,
    "duplicateEntries": 0,
    "referencedUniqueTerms": 804,
    "coveredUniqueTerms": 556,
    "coveragePercent": 69.2,
    "unglossedUniqueTerms": 248,
    "unglossedReferenceOccurrences": 249,
    "placeholderEnglishDefinitions": 73,
    "canonicalVocabularySourceEntries": 205
  },
  "contentInventory": {
    "grammarLessons": 58,
    "listeningResources": 145,
    "readingResources": 73,
    "part5PracticeQuestions": 80
  },
  "learningOutcomes": {
    "objectives": 11,
    "criteria": 33,
    "instrumentedCriteria": 6,
    "instrumentedPercent": 18.2,
    "statusCounts": {
      "instrumented_practice_evidence": 2,
      "instrumented_learner_self_report": 2,
      "instrumented_delayed_recall": 2,
      "criteria_defined_not_yet_instrumented": 27
    },
    "criteriaDetail": [
      {
        "objectiveId": "foundation-pre-a1-a1",
        "outcomeId": "foundation-pre-a1-a1-recognition",
        "title": "Nhận biết từ/cấu trúc nền tảng trong ngữ cảnh quen thuộc",
        "status": "instrumented_practice_evidence",
        "evidenceMetric": "correct_rate",
        "masteryThreshold": 0.8,
        "minimumUniqueItems": 10
      },
      {
        "objectiveId": "foundation-pre-a1-a1",
        "outcomeId": "foundation-pre-a1-a1-production",
        "title": "Tạo câu ngắn đúng mẫu đã học",
        "status": "instrumented_learner_self_report",
        "evidenceMetric": "rubric_score",
        "masteryThreshold": 0.8,
        "minimumUniqueItems": 10
      },
      {
        "objectiveId": "foundation-pre-a1-a1",
        "outcomeId": "foundation-pre-a1-a1-retention",
        "title": "Nhớ lại nội dung ở lần ôn cách quãng",
        "status": "instrumented_delayed_recall",
        "evidenceMetric": "delayed_correct_rate",
        "masteryThreshold": 0.8,
        "minimumUniqueItems": 10
      },
      {
        "objectiveId": "foundation-a2",
        "outcomeId": "foundation-a2-recognition",
        "title": "Nhận biết và hiểu cấu trúc A2 trong ngữ cảnh công việc quen thuộc",
        "status": "instrumented_practice_evidence",
        "evidenceMetric": "correct_rate",
        "masteryThreshold": 0.8,
        "minimumUniqueItems": 10
      },
      {
        "objectiveId": "foundation-a2",
        "outcomeId": "foundation-a2-application",
        "title": "Vận dụng cấu trúc A2 vào tình huống giao tiếp ngắn",
        "status": "instrumented_learner_self_report",
        "evidenceMetric": "rubric_score",
        "masteryThreshold": 0.8,
        "minimumUniqueItems": 10
      },
      {
        "objectiveId": "foundation-a2",
        "outcomeId": "foundation-a2-retention",
        "title": "Nhớ lại nội dung A2 qua ôn tập cách quãng",
        "status": "instrumented_delayed_recall",
        "evidenceMetric": "delayed_correct_rate",
        "masteryThreshold": 0.8,
        "minimumUniqueItems": 10
      },
      {
        "objectiveId": "grammar-core",
        "outcomeId": "grammar-core-form-recognition",
        "title": "Nhận diện cấu trúc ngữ pháp phù hợp trong câu",
        "status": "criteria_defined_not_yet_instrumented",
        "evidenceMetric": "correct_rate",
        "masteryThreshold": 0.8,
        "minimumUniqueItems": 10
      },
      {
        "objectiveId": "grammar-core",
        "outcomeId": "grammar-core-contextual-choice",
        "title": "Chọn đáp án đúng theo cấu trúc và ngữ cảnh TOEIC",
        "status": "criteria_defined_not_yet_instrumented",
        "evidenceMetric": "correct_rate",
        "masteryThreshold": 0.8,
        "minimumUniqueItems": 10
      },
      {
        "objectiveId": "grammar-core",
        "outcomeId": "grammar-core-error-explanation",
        "title": "Giải thích được lý do chọn đáp án và loại phương án nhiễu",
        "status": "criteria_defined_not_yet_instrumented",
        "evidenceMetric": "explanation_rubric",
        "masteryThreshold": 0.8,
        "minimumUniqueItems": 10
      },
      {
        "objectiveId": "listening-part-1",
        "outcomeId": "listening-part-1-visual-audio-match",
        "title": "Ghép mô tả nghe được với hành động/vị trí trong ảnh",
        "status": "criteria_defined_not_yet_instrumented",
        "evidenceMetric": "correct_rate",
        "masteryThreshold": 0.8,
        "minimumUniqueItems": 10
      },
      {
        "objectiveId": "listening-part-1",
        "outcomeId": "listening-part-1-paraphrase-recognition",
        "title": "Nhận diện cách diễn đạt tương đương trong audio",
        "status": "criteria_defined_not_yet_instrumented",
        "evidenceMetric": "correct_rate",
        "masteryThreshold": 0.8,
        "minimumUniqueItems": 10
      },
      {
        "objectiveId": "listening-part-1",
        "outcomeId": "listening-part-1-detail-retention",
        "title": "Nhớ chi tiết chính sau khi nghe một lần",
        "status": "criteria_defined_not_yet_instrumented",
        "evidenceMetric": "delayed_correct_rate",
        "masteryThreshold": 0.8,
        "minimumUniqueItems": 10
      },
      {
        "objectiveId": "listening-part-2",
        "outcomeId": "listening-part-2-response-intent",
        "title": "Nhận diện loại câu hỏi và ý định giao tiếp",
        "status": "criteria_defined_not_yet_instrumented",
        "evidenceMetric": "correct_rate",
        "masteryThreshold": 0.8,
        "minimumUniqueItems": 10
      },
      {
        "objectiveId": "listening-part-2",
        "outcomeId": "listening-part-2-natural-response",
        "title": "Chọn phản hồi tự nhiên, đúng ngữ cảnh",
        "status": "criteria_defined_not_yet_instrumented",
        "evidenceMetric": "correct_rate",
        "masteryThreshold": 0.8,
        "minimumUniqueItems": 10
      },
      {
        "objectiveId": "listening-part-2",
        "outcomeId": "listening-part-2-distractor-resistance",
        "title": "Tránh bẫy lặp từ và đáp án nghe có vẻ liên quan",
        "status": "criteria_defined_not_yet_instrumented",
        "evidenceMetric": "correct_rate",
        "masteryThreshold": 0.8,
        "minimumUniqueItems": 10
      },
      {
        "objectiveId": "listening-part-3",
        "outcomeId": "listening-part-3-conversation-purpose",
        "title": "Xác định mục đích cuộc hội thoại",
        "status": "criteria_defined_not_yet_instrumented",
        "evidenceMetric": "correct_rate",
        "masteryThreshold": 0.8,
        "minimumUniqueItems": 10
      },
      {
        "objectiveId": "listening-part-3",
        "outcomeId": "listening-part-3-detail-inference",
        "title": "Tìm chi tiết và suy luận từ hội thoại",
        "status": "criteria_defined_not_yet_instrumented",
        "evidenceMetric": "correct_rate",
        "masteryThreshold": 0.8,
        "minimumUniqueItems": 10
      },
      {
        "objectiveId": "listening-part-3",
        "outcomeId": "listening-part-3-speaker-linking",
        "title": "Liên kết người nói, vai trò và hành động",
        "status": "criteria_defined_not_yet_instrumented",
        "evidenceMetric": "correct_rate",
        "masteryThreshold": 0.8,
        "minimumUniqueItems": 10
      },
      {
        "objectiveId": "listening-part-4",
        "outcomeId": "listening-part-4-talk-purpose",
        "title": "Xác định mục đích thông báo/bài nói",
        "status": "criteria_defined_not_yet_instrumented",
        "evidenceMetric": "correct_rate",
        "masteryThreshold": 0.8,
        "minimumUniqueItems": 10
      },
      {
        "objectiveId": "listening-part-4",
        "outcomeId": "listening-part-4-detail-tracking",
        "title": "Theo dõi thời gian, địa điểm, con số và hành động",
        "status": "criteria_defined_not_yet_instrumented",
        "evidenceMetric": "correct_rate",
        "masteryThreshold": 0.8,
        "minimumUniqueItems": 10
      },
      {
        "objectiveId": "listening-part-4",
        "outcomeId": "listening-part-4-inference-action",
        "title": "Suy luận bước tiếp theo hoặc đối tượng nghe",
        "status": "criteria_defined_not_yet_instrumented",
        "evidenceMetric": "correct_rate",
        "masteryThreshold": 0.8,
        "minimumUniqueItems": 10
      },
      {
        "objectiveId": "reading-part-5",
        "outcomeId": "reading-part-5-sentence-completion",
        "title": "Hoàn thành câu dựa trên ngữ pháp và từ vựng",
        "status": "criteria_defined_not_yet_instrumented",
        "evidenceMetric": "correct_rate",
        "masteryThreshold": 0.8,
        "minimumUniqueItems": 10
      },
      {
        "objectiveId": "reading-part-5",
        "outcomeId": "reading-part-5-word-form-selection",
        "title": "Chọn đúng dạng từ và kết hợp từ",
        "status": "criteria_defined_not_yet_instrumented",
        "evidenceMetric": "correct_rate",
        "masteryThreshold": 0.8,
        "minimumUniqueItems": 10
      },
      {
        "objectiveId": "reading-part-5",
        "outcomeId": "reading-part-5-distractor-explanation",
        "title": "Giải thích được khác biệt giữa đáp án đúng và nhiễu",
        "status": "criteria_defined_not_yet_instrumented",
        "evidenceMetric": "explanation_rubric",
        "masteryThreshold": 0.8,
        "minimumUniqueItems": 10
      },
      {
        "objectiveId": "reading-part-6",
        "outcomeId": "reading-part-6-text-cohesion",
        "title": "Chọn câu/từ/cụm từ bảo đảm mạch văn",
        "status": "criteria_defined_not_yet_instrumented",
        "evidenceMetric": "correct_rate",
        "masteryThreshold": 0.8,
        "minimumUniqueItems": 10
      },
      {
        "objectiveId": "reading-part-6",
        "outcomeId": "reading-part-6-context-completion",
        "title": "Hoàn thành chỗ trống theo ngữ cảnh toàn đoạn",
        "status": "criteria_defined_not_yet_instrumented",
        "evidenceMetric": "correct_rate",
        "masteryThreshold": 0.8,
        "minimumUniqueItems": 10
      },
      {
        "objectiveId": "reading-part-6",
        "outcomeId": "reading-part-6-discourse-purpose",
        "title": "Nhận diện mục đích và liên kết thông tin trong văn bản",
        "status": "criteria_defined_not_yet_instrumented",
        "evidenceMetric": "correct_rate",
        "masteryThreshold": 0.8,
        "minimumUniqueItems": 10
      },
      {
        "objectiveId": "reading-part-7",
        "outcomeId": "reading-part-7-information-location",
        "title": "Tìm đúng thông tin trong một hoặc nhiều văn bản",
        "status": "criteria_defined_not_yet_instrumented",
        "evidenceMetric": "correct_rate",
        "masteryThreshold": 0.8,
        "minimumUniqueItems": 10
      },
      {
        "objectiveId": "reading-part-7",
        "outcomeId": "reading-part-7-paraphrase-inference",
        "title": "Nhận diện diễn đạt lại và suy luận có căn cứ",
        "status": "criteria_defined_not_yet_instrumented",
        "evidenceMetric": "correct_rate",
        "masteryThreshold": 0.8,
        "minimumUniqueItems": 10
      },
      {
        "objectiveId": "reading-part-7",
        "outcomeId": "reading-part-7-cross-document-link",
        "title": "Kết nối chi tiết giữa các văn bản đơn/kép/ba",
        "status": "criteria_defined_not_yet_instrumented",
        "evidenceMetric": "correct_rate",
        "masteryThreshold": 0.8,
        "minimumUniqueItems": 10
      },
      {
        "objectiveId": "part5-sentence-completion",
        "outcomeId": "part5-sentence-completion-accuracy",
        "title": "Chọn đáp án đúng trong câu Part 5",
        "status": "criteria_defined_not_yet_instrumented",
        "evidenceMetric": "correct_rate",
        "masteryThreshold": 0.8,
        "minimumUniqueItems": 10
      },
      {
        "objectiveId": "part5-sentence-completion",
        "outcomeId": "part5-sentence-completion-time-management",
        "title": "Hoàn thành câu trong giới hạn thời gian mục tiêu",
        "status": "criteria_defined_not_yet_instrumented",
        "evidenceMetric": "timed_accuracy",
        "masteryThreshold": 0.8,
        "minimumUniqueItems": 10
      },
      {
        "objectiveId": "part5-sentence-completion",
        "outcomeId": "part5-sentence-completion-error-review",
        "title": "Phân loại lỗi và giải thích đáp án sau luyện tập",
        "status": "criteria_defined_not_yet_instrumented",
        "evidenceMetric": "explanation_rubric",
        "masteryThreshold": 0.8,
        "minimumUniqueItems": 10
      }
    ]
  }
}
```

### related_glossary_backlog

`/opt/pyvenv/bin/python tools/build-related-glossary-backlog.py`

Status: **PASS**

```text
Glossary 567; unique missing 248; refs missing 249
```

### editorial_review_queue

`/opt/pyvenv/bin/python tools/build-editorial-review-queue.py`

Status: **PASS**

```text
Wrote docs/reports/TOEIC_INDEPENDENT_REVIEW_QUEUE_v2.95.46.md
Listening eligible=102, reserve=193, total=295; Part7 reserve=87; separate Part5 practice-only=80 (review-pending=80)
```

### full_python_suite

`/opt/pyvenv/bin/python tools/run-python-tests-sharded.py --timeout-per-module 180 --resume`

Status: **PASS**

```text
TEST INVENTORY: {"added": ["tools/tests/test_test_fingerprints.py"], "baseline_module_count": 88, "baseline_status": "COMPARED", "baseline_version": "2.95.45", "confirmed_renames": [], "current_module_count": 89, "modified": ["tools/tests/test_editorial_review_queue.py", "tools/tests/test_major_release_quality_audit_025.py", "tools/tests/test_python_test_shard_runner.py", "tools/tests/test_release_acceptance_runner.py", "tools/tests/test_release_rotation.py", "tools/tests/test_visual_composition.py"], "removed": [], "suspected_renames": []}
RESUME INVALIDATED: checkpoint fingerprint mismatch: source_release_fingerprint; all modules in the selected run will be rerun
[PASS] tools/tests/test_alphabet_sound_lab.py: 7 cases (7 passed, 0 failed, 0 skipped, 0 errors), 0.83s
[PASS] tools/tests/test_answer_position_balance.py: 4 cases (4 passed, 0 failed, 0 skipped, 0 errors), 0.84s
[PASS] tools/tests/test_audit_design_tokens.py: 8 cases (8 passed, 0 failed, 0 skipped, 0 errors), 0.72s
[PASS] tools/tests/test_baseline_ids.py: 13 cases (13 passed, 0 failed, 0 skipped, 0 errors), 21.36s
[PASS] tools/tests/test_choice_history.py: 5 cases (5 passed, 0 failed, 0 skipped, 0 errors), 0.68s
[PASS] tools/tests/test_choice_identity.py: 9 cases (9 passed, 0 failed, 0 skipped, 0 errors), 0.78s
[PASS] tools/tests/test_ci_coverage.py: 3 cases (3 passed, 0 failed, 0 skipped, 0 errors), 0.68s
[PASS] tools/tests/test_cmudict_ipa_backfill.py: 6 cases (6 passed, 0 failed, 0 skipped, 0 errors), 0.70s
[PASS] tools/tests/test_content_batch_024.py: 8 cases (8 passed, 0 failed, 0 skipped, 0 errors), 0.74s
[PASS] tools/tests/test_content_batch_025.py: 7 cases (7 passed, 0 failed, 0 skipped, 0 errors), 0.69s
[PASS] tools/tests/test_content_batch_026.py: 6 cases (6 passed, 0 failed, 0 skipped, 0 errors), 0.70s
[PASS] tools/tests/test_content_batch_027.py: 6 cases (6 passed, 0 failed, 0 skipped, 0 errors), 0.67s
[PASS] tools/tests/test_dashboard_layout.py: 6 cases (6 passed, 0 failed, 0 skipped, 0 errors), 0.78s
[PASS] tools/tests/test_design_profile.py: 6 cases (6 passed, 0 failed, 0 skipped, 0 errors), 1.38s
[PASS] tools/tests/test_design_system.py: 19 cases (19 passed, 0 failed, 0 skipped, 0 errors), 0.73s
[PASS] tools/tests/test_distractor_quality.py: 6 cases (6 passed, 0 failed, 0 skipped, 0 errors), 0.72s
[PASS] tools/tests/test_editorial_review.py: 6 cases (6 passed, 0 failed, 0 skipped, 0 errors), 0.66s
[PASS] tools/tests/test_editorial_review_queue.py: 8 cases (8 passed, 0 failed, 0 skipped, 0 errors), 1.45s
[PASS] tools/tests/test_foundation_a2_assessment_quality.py: 8 cases (8 passed, 0 failed, 0 skipped, 0 errors), 1.31s
[PASS] tools/tests/test_foundation_a2_production.py: 8 cases (8 passed, 0 failed, 0 skipped, 0 errors), 0.66s
[PASS] tools/tests/test_foundation_listening.py: 14 cases (14 passed, 0 failed, 0 skipped, 0 errors), 0.63s
[PASS] tools/tests/test_foundation_listening_extended.py: 4 cases (4 passed, 0 failed, 0 skipped, 0 errors), 0.73s
[PASS] tools/tests/test_foundation_outcome_evidence.py: 2 cases (2 passed, 0 failed, 0 skipped, 0 errors), 0.64s
[PASS] tools/tests/test_foundation_pathway.py: 10 cases (10 passed, 0 failed, 0 skipped, 0 errors), 0.64s
[PASS] tools/tests/test_foundation_production_revision.py: 6 cases (6 passed, 0 failed, 0 skipped, 0 errors), 0.72s
[PASS] tools/tests/test_foundation_reading.py: 9 cases (9 passed, 0 failed, 0 skipped, 0 errors), 0.61s
[PASS] tools/tests/test_foundation_reading_extended.py: 7 cases (7 passed, 0 failed, 0 skipped, 0 errors), 0.66s
[PASS] tools/tests/test_grammar_examples_quality.py: 4 cases (4 passed, 0 failed, 0 skipped, 0 errors), 0.70s
[PASS] tools/tests/test_grammar_expansion.py: 7 cases (7 passed, 0 failed, 0 skipped, 0 errors), 0.63s
[PASS] tools/tests/test_ipa_backfill_batch_024.py: 6 cases (6 passed, 0 failed, 0 skipped, 0 errors), 0.71s
[PASS] tools/tests/test_learning_content.py: 34 cases (34 passed, 0 failed, 0 skipped, 0 errors), 0.74s
[PASS] tools/tests/test_learning_detail_scope.py: 4 cases (4 passed, 0 failed, 0 skipped, 0 errors), 0.67s
[PASS] tools/tests/test_learning_outcome_progress.py: 3 cases (3 passed, 0 failed, 0 skipped, 0 errors), 0.67s
[PASS] tools/tests/test_learning_outcomes.py: 3 cases (3 passed, 0 failed, 0 skipped, 0 errors), 1.50s
[PASS] tools/tests/test_learning_start_level.py: 4 cases (4 passed, 0 failed, 0 skipped, 0 errors), 0.79s
[PASS] tools/tests/test_learning_surface_consistency.py: 5 cases (5 passed, 0 failed, 0 skipped, 0 errors), 0.83s
[PASS] tools/tests/test_legacy_collocation_cleanup.py: 3 cases (3 passed, 0 failed, 0 skipped, 0 errors), 0.75s
[PASS] tools/tests/test_listening_expansion.py: 8 cases (8 passed, 0 failed, 0 skipped, 0 errors), 0.72s
[PASS] tools/tests/test_major_release_quality_audit_025.py: 8 cases (8 passed, 0 failed, 0 skipped, 0 errors), 0.81s
[PASS] tools/tests/test_missing_ipa_review_queue.py: 8 cases (8 passed, 0 failed, 0 skipped, 0 errors), 0.68s
[PASS] tools/tests/test_missing_ipa_safe_backfill.py: 8 cases (8 passed, 0 failed, 0 skipped, 0 errors), 0.78s
[PASS] tools/tests/test_objective_resource_map.py: 2 cases (2 passed, 0 failed, 0 skipped, 0 errors), 0.75s
[PASS] tools/tests/test_package_source.py: 3 cases (3 passed, 0 failed, 0 skipped, 0 errors), 0.90s
[PASS] tools/tests/test_part1_photo_assets.py: 6 cases (6 passed, 0 failed, 0 skipped, 0 errors), 0.70s
[PASS WITH SKIPS] tools/tests/test_patch_data.py: 20 cases (19 passed, 0 failed, 1 skipped, 0 errors), 16.21s
[PASS] tools/tests/test_patch_related_terms.py: 11 cases (11 passed, 0 failed, 0 skipped, 0 errors), 10.78s
[PASS] tools/tests/test_placement_diagnostic.py: 6 cases (6 passed, 0 failed, 0 skipped, 0 errors), 0.80s
[PASS] tools/tests/test_practice_mode_fallback.py: 6 cases (6 passed, 0 failed, 0 skipped, 0 errors), 0.72s
[PASS] tools/tests/test_project_progress.py: 4 cases (4 passed, 0 failed, 0 skipped, 0 errors), 4.44s
[PASS] tools/tests/test_pwa_readiness.py: 3 cases (3 passed, 0 failed, 0 skipped, 0 errors), 0.73s
[PASS] tools/tests/test_python_test_shard_runner.py: 19 cases (19 passed, 0 failed, 0 skipped, 0 errors), 1.86s
[PASS] tools/tests/test_question_evidence.py: 7 cases (7 passed, 0 failed, 0 skipped, 0 errors), 1.50s
[PASS] tools/tests/test_reading_expansion.py: 9 cases (9 passed, 0 failed, 0 skipped, 0 errors), 0.69s
[PASS] tools/tests/test_related_glossary_backfill_025.py: 6 cases (6 passed, 0 failed, 0 skipped, 0 errors), 0.78s
[PASS] tools/tests/test_related_glossary_backlog.py: 3 cases (3 passed, 0 failed, 0 skipped, 0 errors), 2.05s
[PASS] tools/tests/test_related_glossary_batch_021.py: 7 cases (7 passed, 0 failed, 0 skipped, 0 errors), 0.77s
[PASS] tools/tests/test_related_glossary_batch_022.py: 9 cases (9 passed, 0 failed, 0 skipped, 0 errors), 0.75s
[PASS] tools/tests/test_related_glossary_batch_023.py: 9 cases (9 passed, 0 failed, 0 skipped, 0 errors), 0.67s
[PASS] tools/tests/test_related_glossary_batch_026.py: 5 cases (5 passed, 0 failed, 0 skipped, 0 errors), 0.68s
[PASS] tools/tests/test_related_glossary_batch_027.py: 5 cases (5 passed, 0 failed, 0 skipped, 0 errors), 0.70s
[PASS] tools/tests/test_related_glossary_batch_028.py: 4 cases (4 passed, 0 failed, 0 skipped, 0 errors), 0.63s
[PASS] tools/tests/test_related_glossary_batch_030.py: 4 cases (4 passed, 0 failed, 0 skipped, 0 errors), 0.67s
[PASS] tools/tests/test_related_glossary_batch_032.py: 4 cases (4 passed, 0 failed, 0 skipped, 0 errors), 0.63s
[PASS] tools/tests/test_related_glossary_batch_033.py: 3 cases (3 passed, 0 failed, 0 skipped, 0 errors), 0.67s
[PASS] tools/tests/test_related_glossary_batch_034.py: 6 cases (6 passed, 0 failed, 0 skipped, 0 errors), 0.65s
[PASS] tools/tests/test_related_glossary_batch_035.py: 5 cases (5 passed, 0 failed, 0 skipped, 0 errors), 0.74s
[PASS] tools/tests/test_related_glossary_batch_036.py: 6 cases (6 passed, 0 failed, 0 skipped, 0 errors), 0.66s
[PASS] tools/tests/test_related_glossary_batch_037.py: 7 cases (7 passed, 0 failed, 0 skipped, 0 errors), 0.68s
[PASS] tools/tests/test_related_glossary_candidate_audit.py: 4 cases (4 passed, 0 failed, 0 skipped, 0 errors), 0.87s
[PASS] tools/tests/test_related_glossary_canonical_enrichment_029.py: 8 cases (8 passed, 0 failed, 0 skipped, 0 errors), 0.86s
[PASS] tools/tests/test_related_glossary_exact_match_enrichment_035.py: 5 cases (5 passed, 0 failed, 0 skipped, 0 errors), 0.80s
[PASS] tools/tests/test_related_glossary_merge_038.py: 8 cases (8 passed, 0 failed, 0 skipped, 0 errors), 0.93s
[PASS] tools/tests/test_related_glossary_quality_audit.py: 11 cases (11 passed, 0 failed, 0 skipped, 0 errors), 0.76s
[PASS] tools/tests/test_related_term_explanation_context.py: 3 cases (3 passed, 0 failed, 0 skipped, 0 errors), 0.74s
[PASS] tools/tests/test_release_acceptance_runner.py: 10 cases (10 passed, 0 failed, 0 skipped, 0 errors), 0.71s
[PASS] tools/tests/test_release_rotation.py: 9 cases (9 passed, 0 failed, 0 skipped, 0 errors), 7.11s
[PASS] tools/tests/test_remaining_content_review.py: 9 cases (9 passed, 0 failed, 0 skipped, 0 errors), 0.73s
[PASS] tools/tests/test_repository_integrity.py: 1 cases (1 passed, 0 failed, 0 skipped, 0 errors), 1.52s
[PASS] tools/tests/test_responsive_layout.py: 7 cases (7 passed, 0 failed, 0 skipped, 0 errors), 0.74s
[PASS] tools/tests/test_sentence_completion.py: 12 cases (12 passed, 0 failed, 0 skipped, 0 errors), 0.80s
[PASS] tools/tests/test_sync_version.py: 12 cases (12 passed, 0 failed, 0 skipped, 0 errors), 10.93s
[PASS] tools/tests/test_test_fingerprints.py: 9 cases (9 passed, 0 failed, 0 skipped, 0 errors), 0.76s
[PASS] tools/tests/test_tts_readiness.py: 15 cases (15 passed, 0 failed, 0 skipped, 0 errors), 0.70s
[PASS] tools/tests/test_validator.py: 38 cases (38 passed, 0 failed, 0 skipped, 0 errors), 57.97s
[PASS] tools/tests/test_visual_composition.py: 9 cases (9 passed, 0 failed, 0 skipped, 0 errors), 0.81s
[PASS] tools/tests/test_vocabulary_batch_012.py: 4 cases (4 passed, 0 failed, 0 skipped, 0 errors), 0.73s
[PASS] tools/tests/test_vocabulary_detail_examples.py: 19 cases (19 passed, 0 failed, 0 skipped, 0 errors), 0.79s
[PASS] tools/tests/test_vocabulary_family_links.py: 6 cases (6 passed, 0 failed, 0 skipped, 0 errors), 0.70s
[PASS] tools/tests/test_vocabulary_relationship_graph_audit.py: 8 cases (8 passed, 0 failed, 0 skipped, 0 errors), 0.73s
SUMMARY: 88 PASS + 1 PASS WITH SKIPS / 89 modules; 691 passed, 0 failed, 1 skipped, 0 errored; 0 timeout(s); 0 error(s); 0 unapproved-skip module(s); 0 NOT RUN
```


Full suite is PASS only if the runner reaches it and returns exit code 0. A timeout is never converted to PASS.


## Additional GitHub Actions workflow replay

- Exact local replay of all 110 `run:` steps in `.github/workflows/validate-data.yml`: 110 PASS, 0 FAIL, 0 TIMEOUT, 0 ERROR, 0 NOT RUN.
- Local runtime: Python 3.13.5 / Node 22.16.0. The workflow requests Python 3.12 / Node 24; hosted GitHub Actions and Pages remain unverified.
