# Current version

- Version: **v2.84.0**
- Status: local GitHub Pages release candidate; source and local checks must pass before handoff. Remote Actions/Pages and physical-device behavior are not claimed.
- Source of truth: `data/manifest.json`
- Master: `docs/MASTER_STATUS.md`
- Changelog: `docs/CHANGELOG.md`
- Test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.84.0.md`
- Robot Buddy specification: `reports/ROBOT_BUDDY_v2.84.0.md`
- Previous release: v2.83.0.
- Robot architecture: head-only SVG mascot, static offline dialogue library (500 unique lines plus feature help/FAQ), keyword intent matching, idle nudges, limited first-run Placement handoff.
- Data boundary: no learner-progress, IndexedDB, score, Placement-result or personal-vocabulary access; no remote AI/API; chat not persisted.
- New localStorage key: `toeic:robot-buddy-settings:v1` for onboarding choice and idle mute only. One-time migration reads only v2.83 onboarding preference `toeic:robot-companion-onboarding:v1`.
