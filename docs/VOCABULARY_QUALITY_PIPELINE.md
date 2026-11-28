# Vocabulary & Glossary Quality Pipeline

Status: candidate-only, read-only tooling.

## Purpose

Provide one deterministic view of related-glossary editorial flags, synonym/antonym graph integrity, Word Family target and sense-anchor integrity, and prioritized human-review work.

## Run

```bash
python tools/build-vocabulary-quality-dashboard.py
python tools/build-vocabulary-quality-dashboard.py --output docs/reports/VOCABULARY_QUALITY_DASHBOARD.md --json-output /tmp/vocabulary-quality-dashboard.json
python -m unittest tools.tests.test_vocabulary_quality_dashboard
```

## Interpretation

- Relation frequency helps prioritize review; it does not prove a missing term has a particular definition.
- Canonical headword matches and glossary candidates require editorial review.
- Non-reciprocal relations may be intentionally asymmetric and are not automatically rejected.
- The dashboard is read-only. It does not modify vocabulary, glossary, questions, choices, answer keys, learner IndexedDB data, UI, Service Worker or deployment configuration.
- Listening/Reading reserve material is not promoted into Mock by this pipeline.

## Acceptance boundary

This tooling batch is not a content release, production deployment, or evidence of TOEIC readiness. GitHub Actions must pass on the exact candidate HEAD before it can be accepted.