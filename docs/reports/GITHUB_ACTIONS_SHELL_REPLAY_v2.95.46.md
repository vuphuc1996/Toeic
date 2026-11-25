# GitHub Actions Shell Replay — v2.95.46

- Workflow: `.github/workflows/validate-data.yml`
- Run steps discovered/executed: 110/110
- PASS: 110; FAIL: 0; TIMEOUT: 0; ERROR: 0; NOT RUN: 0.
- All 110 shell run steps passed on the local replay.
- Runtime difference: local Python 3.13.5 / Node 22.16.0; hosted workflow declares Python 3.12 / Node 24.
- No GitHub-hosted Actions execution or GitHub Pages deployment is claimed.

| # | Workflow step | Status | Seconds |
|---:|---|---|---:|
| 4 | Repository integrity preflight | PASS | 1.004 |
| 5 | Python syntax check | PASS | 1.035 |
| 6 | Unit tests — baseline_ids | PASS | 19.682 |
| 7 | Unit tests — patch_data | PASS | 16.282 |
| 8 | Unit tests — patch_related_terms | PASS | 9.595 |
| 9 | Unit tests — source package contract | PASS | 0.701 |
| 10 | Unit tests — related glossary batch 021 | PASS | 0.730 |
| 11 | Unit tests — US IPA backfill batch 024 | PASS | 0.665 |
| 12 | Unit tests — related glossary batch 022 | PASS | 0.673 |
| 13 | Unit tests — related glossary batch 023 | PASS | 0.708 |
| 14 | Unit tests — related glossary batch 026 | PASS | 0.670 |
| 15 | Unit tests — related glossary batch 027 | PASS | 0.691 |
| 16 | Unit tests — related glossary batch 028 | PASS | 0.675 |
| 17 | Unit tests — canonical related-glossary enrichment v2.95.29 | PASS | 0.644 |
| 18 | Related glossary canonical batch 030 | PASS | 0.671 |
| 19 | Related glossary batch 032 | PASS | 0.667 |
| 20 | Related glossary batch 033 | PASS | 0.658 |
| 21 | Related glossary batch 034 — guarded canonical correction | PASS | 0.634 |
| 22 | Related glossary batch 035 — Cambridge relation-target coverage | PASS | 0.680 |
| 23 | Related glossary batch 036 — Cambridge relation-target coverage | PASS | 0.666 |
| 24 | Unit tests — related glossary batch 037 | PASS | 0.674 |
| 25 | Unit tests — exact canonical glossary enrichment v2.95.35 | PASS | 0.689 |
| 26 | Audit canonical related-glossary enrichment candidates | PASS | 0.696 |
| 27 | Unit tests — related glossary candidate audit (read-only) | PASS | 0.785 |
| 28 | Unit tests — related glossary quality flags (read-only) | PASS | 0.729 |
| 29 | Unit tests — vocabulary relationship graph audit (read-only) | PASS | 0.659 |
| 30 | Audit vocabulary relationship graph | PASS | 0.706 |
| 31 | Unit tests — related glossary backlog report | PASS | 2.242 |
| 32 | Unit tests — glossary canonical-sense backfill v2.95.25 | PASS | 0.764 |
| 33 | Unit tests — major release quality audit / glossary metrics | PASS | 0.738 |
| 34 | Unit tests — missing US IPA review queue | PASS | 0.664 |
| 35 | Unit tests — sync_version | PASS | 10.756 |
| 36 | Unit tests — validator | PASS | 57.679 |
| 37 | Unit tests — learning_content | PASS | 0.779 |
| 38 | Unit tests — reading_expansion | PASS | 0.755 |
| 39 | Unit tests — listening_expansion | PASS | 0.673 |
| 40 | Unit tests — TTS readiness and reading aloud | PASS | 0.717 |
| 41 | Unit tests — pwa_readiness | PASS | 0.671 |
| 42 | Unit tests — grammar_expansion | PASS | 0.728 |
| 43 | Unit tests — content batch 024 | PASS | 0.686 |
| 44 | Unit tests — content batch 025 | PASS | 0.699 |
| 45 | Unit tests — content batch 026 | PASS | 0.698 |
| 46 | Unit tests — Listening content batch 027 | PASS | 0.743 |
| 47 | Unit tests — TOEIC score readiness | PASS | 0.101 |
| 48 | Unit tests — dashboard_layout | PASS | 0.713 |
| 49 | Unit tests — design_system | PASS | 0.735 |
| 50 | Unit tests and ratchet audit — CSS design tokens | PASS | 1.683 |
| 51 | Validate canonical design profile | PASS | 2.370 |
| 52 | Unit tests — question_evidence | PASS | 1.479 |
| 53 | Unit tests — repository integrity | PASS | 1.412 |
| 54 | Unit tests — grammar examples quality | PASS | 0.683 |
| 55 | Unit tests — distractor_quality | PASS | 0.774 |
| 56 | Audit distractor structural integrity | PASS | 0.711 |
| 57 | Unit tests — choice_history | PASS | 0.659 |
| 58 | Unit tests — learning_detail_scope | PASS | 0.683 |
| 59 | Unit tests — choice_identity | PASS | 0.778 |
| 60 | Unit tests — answer_position_balance | PASS | 0.697 |
| 61 | Unit tests — remaining_content_review | PASS | 0.745 |
| 62 | Unit tests — editorial_review | PASS | 0.697 |
| 63 | Unit tests — editorial review queue | PASS | 1.479 |
| 64 | Unit tests — practice mode fallback and flashcard result layering | PASS | 0.704 |
| 65 | Unit tests — CI coverage | PASS | 0.745 |
| 66 | Unit tests — Python test shard runner | PASS | 1.754 |
| 67 | Unit tests — deterministic test fingerprints | PASS | 0.733 |
| 68 | Unit tests — release acceptance runner | PASS | 0.745 |
| 69 | Unit tests — related glossary merge batch 038 | PASS | 0.669 |
| 70 | Unit tests — release_rotation | PASS | 7.139 |
| 71 | Unit tests — foundation outcome evidence | PASS | 0.809 |
| 72 | Unit tests — foundation_pathway | PASS | 0.741 |
| 73 | Unit tests — foundation_reading | PASS | 0.711 |
| 74 | Unit tests — foundation extended Reading | PASS | 0.707 |
| 75 | Unit tests — foundation_listening | PASS | 0.699 |
| 76 | Unit tests — foundation extended Listening | PASS | 0.679 |
| 77 | Unit tests — foundation A2 assessment quality | PASS | 1.421 |
| 78 | Unit tests — foundation A2 contextual production | PASS | 0.698 |
| 79 | Unit tests — foundation guided production revision | PASS | 0.721 |
| 80 | Audit Foundation A2 assessment integrity and source evidence | PASS | 0.713 |
| 81 | Unit tests — alphabet sound lab | PASS | 0.624 |
| 82 | Unit tests — visual composition | PASS | 0.868 |
| 83 | Unit tests — learning_start_level | PASS | 0.727 |
| 84 | Unit tests — objective resource map | PASS | 0.709 |
| 85 | Unit tests — project progress | PASS | 4.005 |
| 86 | Validate learning outcome criteria | PASS | 1.390 |
| 87 | Unit tests — learning outcome progress | PASS | 0.723 |
| 88 | Audit objective resource links | PASS | 0.671 |
| 89 | Audit learning outcome criteria | PASS | 0.787 |
| 90 | Validate placement diagnostic | PASS | 0.697 |
| 91 | Unit tests — responsive layout | PASS | 0.732 |
| 92 | Unit tests — learning surface consistency | PASS | 0.631 |
| 93 | Unit tests — part1_photo_assets | PASS | 0.798 |
| 94 | Unit tests — vocabulary_detail_examples | PASS | 0.826 |
| 95 | Unit tests — related glossary batch 021 | PASS | 0.712 |
| 96 | Unit tests — legacy_collocation_cleanup | PASS | 0.773 |
| 97 | Unit tests — vocabulary_family_links | PASS | 0.751 |
| 98 | Unit tests — vocabulary_batch_012 | PASS | 0.780 |
| 99 | Validate CMUdict US IPA backfill | PASS | 1.485 |
| 100 | Safe missing IPA backfill regression | PASS | 1.422 |
| 101 | Validate safe missing IPA backfill pipeline | PASS | 1.404 |
| 102 | Unit tests — sentence_completion | PASS | 0.762 |
| 103 | Validate vocabulary data (structure, ID integrity, APP_SHELL, ratchet baseline) | PASS | 1.043 |
| 104 | Validate TOEIC learning content (Listening/Reading/Grammar) | PASS | 0.712 |
| 105 | Validate Part 1 photo binaries and mixed-source attribution | PASS | 0.754 |
| 106 | Generate target-based project progress report | PASS | 0.795 |
| 107 | Generate TOEIC coverage report | PASS | 0.758 |
| 108 | Generate Listening readiness report | PASS | 0.750 |
| 109 | Generate answer-to-source evidence audit | PASS | 0.804 |
| 110 | Audit distractor plausibility and answer-index safety | PASS | 0.815 |
| 111 | Version sync check | PASS | 0.867 |
| 112 | JavaScript syntax check | PASS | 2.208 |
| 113 | Unit tests — related term explanation context | PASS | 0.670 |
