# Current version

- Version: **v2.70.0**
- Status: local release candidate; deployment hold pending restoration of eight original Part 1 JPG assets and strict validator success.
- Source: `data/manifest.json`
- Master: `docs/MASTER_STATUS.md`
- Changelog: `docs/CHANGELOG.md`
- Test report: `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.70.0.md`
- Progress baseline: `docs/reports/PROJECT_PROGRESS_BASELINE_v2.70.0.md`
- Current cumulative US IPA ledger: `docs/reports/CMUDICT_IPA_BACKFILL_v2.70.0.json` (298 source-linked entries; 91 inherited unresolved entries remain deliberately blank).
- Vocabulary: 1,100 headwords; 1,009/1,100 US IPA populated (91.7%); 267/1,100 word-family records (24.3%); 365 directed word-family links.
- Headword target progress: 36.7% of 3,000 minimum; 22.0% of 5,000 planning ceiling.
- v2.70.0 adds Batch 011 (+37) across Customer Service and Travel. Contracts and Facilities remain future batch themes.
- No IndexedDB schema/store migration, question ID, answer key, learner progress, personal vocabulary or study-setting reset.
- CMUdict input is ARPABET, converted to project broad-GA IPA; source caveat and license are documented. Entries are not independently pronunciation-certified.
- Deployment is still held: only 1/9 original Part 1 JPG files is present in this source package; remote CI, Pages deployment and physical-device QA are not verified.
