import assert from 'node:assert/strict';
import fs from 'node:fs';

const read = path => fs.readFileSync(new URL(path, import.meta.url), 'utf8');
const manifest = JSON.parse(read('../../data/manifest.json'));
const html = read('../../index.html');
const app = read('../../assets/js/app.js');
const sw = read('../../sw.js');
const version = manifest.version;

assert.match(version, /^\\d+\\.\\d+\\.\\d+$/);
assert.match(html, new RegExp(`<meta name="toeic-release" content="${version}">`));
assert.match(html, new RegExp(`href="./assets/css/app\\.css\\?v=${version}"`));
assert.match(html, new RegExp(`href="./assets/css/design-system\\.css\\?v=${version}"`));
assert.match(html, new RegExp(`src="./assets/js/app\\.js\\?v=${version}"`));
assert.match(app, new RegExp(`const APP_RELEASE_VERSION = '${version}'`));
assert.match(sw, new RegExp(`const VERSION = '${version}'`));

function readArray(source, name) {
  const match = source.match(new RegExp(`const ${name} = (\\[.*?\\]);`, 's'));
  assert.ok(match, `${name} must be defined`);
  return JSON.parse(match[1]);
}

const required = readArray(sw, 'REQUIRED');
const appShell = readArray(sw, 'APP_SHELL');
for (const path of ['./assets/css/app.css', './assets/css/design-system.css', './assets/js/app.js']) {
  const releaseUrl = `${path}?v=${version}`;
  assert.ok(required.includes(releaseUrl), `${releaseUrl} must be in REQUIRED`);
  assert.ok(appShell.includes(releaseUrl), `${releaseUrl} must be in APP_SHELL`);
}

// This is the cache-coherence regression: a v2.95.65 worker cache key for
// app.js cannot satisfy the v2.95.66 HTML request, so it must fetch the new
// release URL instead of returning the old modalBackdrop implementation.
const oldWorkerCache = new Set([
  'https://example.test/Toeic/assets/js/app.js',
  'https://example.test/Toeic/assets/js/app.js?v=2.95.65',
]);
const newAppRequest = new URL(`./assets/js/app.js?v=${version}`, 'https://example.test/Toeic/').href;
assert.equal(oldWorkerCache.has(newAppRequest), false, 'new app release URL must bypass the previous cache key');
assert.match(app, /workerScript\\.searchParams\\.set\\('__release',APP_RELEASE_VERSION\\)/);
assert.match(app, /htmlReleaseVersion!==APP_RELEASE_VERSION/);
assert.doesNotMatch(app, /\\$\\('#modalBackdrop'\\)\\.addEventListener/);
assert.match(app, /\\$\\('#modalLayer'\\)\\.addEventListener/);

console.log(`PASS: release asset coherence v${version} — HTML, CSS, app.js and Service Worker share the manifest version; old app.js cache keys cannot shadow the new modal shell; startup rejects mismatched HTML/app releases.`);
