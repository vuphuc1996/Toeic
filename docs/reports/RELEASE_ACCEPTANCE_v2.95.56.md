# Release acceptance — TOEIC Dictionary v2.95.56

**Accepted for local source/package verification only.** The Listening Mock form-diversity gate is implemented and the local Node regression, Mock engine, Mock UI integrity, data validator, version sync, and exact Patch replay pass.

- Node runtime tests: 42/42 PASS.
- Mock engine / Mock UI integrity: PASS.
- Data validator: 1,141 records, 0 errors / 0 warnings, 0 ID additions/removals.
- Version sync: PASS.
- Patch replay: 674/674 files byte-identical to FullSource.
- Full Python `unittest discover`: INCOMPLETE; exceeded the 300-second execution limit and is not accepted as PASS.
- Hosted GitHub Actions, GitHub Pages deployment, PWA cache propagation, and physical-device acceptance remain UNVERIFIED.

No claim of ETS score equivalence or independent psychometric measurement is made. Listening form overlap remains high (98% in the tested consecutive-form pair) and is disclosed to the learner.
