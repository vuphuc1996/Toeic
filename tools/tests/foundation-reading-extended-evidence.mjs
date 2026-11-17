import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { recordFoundationReadingAttempt, summarizeFoundationReading } from '../../assets/js/foundation-reading-evidence.js';

const lessonId = 'a2-polite-requests';
const originalScope = lessonId;
const extendedScope = `${lessonId}::reading2`;
let progress = {};
progress = recordFoundationReadingAttempt(progress, extendedScope, `${lessonId}::reading2::q1`, true, 100);
progress = recordFoundationReadingAttempt(progress, extendedScope, `${lessonId}::reading2::q2`, false, 200);
progress = recordFoundationReadingAttempt(progress, extendedScope, `${lessonId}::reading2::q3`, true, 300);
let extended = summarizeFoundationReading(progress, extendedScope, { minimumUniqueQuestions: 3, practiceAccuracyThreshold: 0.67 });
assert.equal(extended.uniqueQuestions, 3);
assert.equal(extended.accuracyPercent, 67);
assert.equal(extended.threshold, 0.67);
assert.equal(extended.status, 'practice_threshold_met', 'the displayed rounded 67% meets the configured 67% threshold');
assert.equal(summarizeFoundationReading(progress, originalScope).uniqueQuestions, 0,
  'extended reading must not inflate or replace original reading evidence');
progress = recordFoundationReadingAttempt(progress, extendedScope, `${lessonId}::reading2::q1`, false, 400);
extended = summarizeFoundationReading(progress, extendedScope, { minimumUniqueQuestions: 3, practiceAccuracyThreshold: 0.67 });
assert.equal(extended.uniqueQuestions, 3, 'retries must not inflate independent question count');
assert.equal(extended.totalAttempts, 4);
assert.equal(extended.accuracyPercent, 33, 'latest answer controls the practice summary');
assert.equal(summarizeFoundationReading(progress, originalScope).uniqueQuestions, 0);

const root = new URL('../../', import.meta.url);
const app = await readFile(new URL('assets/js/app.js', root), 'utf8');
assert.match(app, /data-foundation-reading-scope="\$\{escapeHtml\(scopeId\)\}"/);
assert.match(app, /scopeId==='reading2'\?state\.foundationReadingExtendedPassages:state\.foundationReadingPassages/);
assert.match(app, /openExtensionIds/);
assert.match(app, /detail\.open=true/);
console.log('Foundation extended Reading evidence isolation and UI persistence: PASS');
