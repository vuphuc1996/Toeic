# Current Version — v2.60.0

- **Status:** local source candidate; remote CI/Pages and physical-device QA are not verified.
- **Base:** v2.59.0.
- **Primary fix:** prevent the app shell version from appearing current while the vocabulary JSON remains stale in an older Service Worker cache.
- **Cache strategy:** versioned `__release` query parameters are added to manifest/data requests. The new release cache normalizes this query for offline cache lookup; old workers see a new cache key and fetch the new release.
- **Runtime integrity:** app refuses to silently render a partial/stale dictionary if the manifest version, per-letter count, total count, unique IDs or unique headwords disagree.
- **Dashboard:** shows validated base vocabulary count / manifest total and release version; personal additions are separated from the GitHub base count.
- **Update behavior:** update check uses `updateViaCache: 'none'`; a previously controlled PWA reloads once after a controller swap to avoid mixed HTML/JS releases.
- **Data preservation:** 992 base vocabulary records and all stable IDs are unchanged from v2.59.0; personal data, IndexedDB schema and progress are preserved.
- **Verification:** see `../reports/TEST_REPORT_TOEIC_Dictionary_v2.60.0.md`.
