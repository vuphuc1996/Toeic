import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const read = relative => fs.readFileSync(path.join(root, relative), 'utf8');
const swSource = read('sw.js');
const appSource = read('assets/js/app.js');
const html = read('index.html');
const css = read('assets/css/app.css');

const requiredAssets = JSON.parse(swSource.match(/const REQUIRED = (\[.*?\]);/s)[1]);
const appShellAssets = JSON.parse(swSource.match(/const APP_SHELL = (\[.*?\]);/s)[1]);
const releaseVersion = swSource.match(/const VERSION = '([^']+)'/)[1];
for (const assets of [requiredAssets, appShellAssets]) {
  assert.ok(assets.includes('./assets/js/flashcard-senses.js'), 'legacy module path remains covered');
  assert.ok(assets.includes(`./assets/js/flashcard-senses.js?__release=${releaseVersion}`), 'release-keyed module URL must be precached');
}


function createWorker({ active = false, failRequired = false, failOptional = false } = {}) {
  const listeners = new Map();
  const cacheStore = new Map();
  const deleted = [];
  let skipWaitingCalls = 0;
  let claimCalls = 0;
  let navigationResponse = null;
  const fetchCalls = [];

  const keyOf = value => value instanceof URL ? value.href : (value?.url || String(value));
  const cacheStorage = {
    async open(name) {
      if (!cacheStore.has(name)) cacheStore.set(name, new Map());
      const entries = cacheStore.get(name);
      return {
        async put(key, response) {
          entries.set(keyOf(key), response.clone ? response.clone() : response);
        },
        async match(key) {
          const value = entries.get(keyOf(key));
          return value?.clone ? value.clone() : value;
        }
      };
    },
    async keys() { return [...cacheStore.keys()]; },
    async delete(name) {
      deleted.push(name);
      return cacheStore.delete(name);
    }
  };

  const registration = {
    scope: 'https://example.test/Toeic/',
    active: active ? { state: 'activated' } : null
  };
  const self = {
    registration,
    location: { origin: 'https://example.test', href: 'https://example.test/Toeic/', pathname: '/Toeic/' },
    clients: {
      async claim() { claimCalls += 1; },
      async matchAll() { return []; },
      async openWindow() {}
    },
    addEventListener(type, handler) { listeners.set(type, handler); },
    async skipWaiting() { skipWaitingCalls += 1; }
  };

  const fetchMock = async request => {
    const url = keyOf(request);
    fetchCalls.push(url);
    if (navigationResponse && request?.mode === 'navigate') return navigationResponse.clone();
    if (failRequired && url.endsWith('/index.html')) return new Response('required failed', { status: 503 });
    if (failOptional && url.endsWith('/assets/icons/icon.svg')) return new Response('optional failed', { status: 404 });
    return new Response(`cached:${url}`, { status: 200, headers: { 'Content-Type': 'text/plain' } });
  };

  const context = {
    self,
    caches: cacheStorage,
    fetch: fetchMock,
    URL,
    Request,
    Response,
    Promise,
    Date,
    console: { info() {}, warn() {}, error() {} }
  };
  vm.runInNewContext(swSource, context, { filename: 'sw.js' });

  return {
    listeners,
    cacheStore,
    deleted,
    fetchCalls,
    registration,
    get skipWaitingCalls() { return skipWaitingCalls; },
    get claimCalls() { return claimCalls; },
    setNavigationResponse(response) { navigationResponse = response; },
    async dispatchExtendable(type, payload = {}) {
      let pending;
      const handler = listeners.get(type);
      assert.ok(handler, `Service Worker ${type} handler should exist`);
      handler({ ...payload, waitUntil(promise) { pending = Promise.resolve(promise); } });
      if (pending) await pending;
      return pending;
    },
    dispatchMessage(data) {
      let pending;
      const handler = listeners.get('message');
      assert.ok(handler, 'Service Worker message handler should exist');
      handler({ data, waitUntil(promise) { pending = Promise.resolve(promise); } });
      return pending || Promise.resolve();
    },
    async dispatchNavigate(url) {
      let pending;
      const handler = listeners.get('fetch');
      assert.ok(handler, 'Service Worker fetch handler should exist');
      const request = { method: 'GET', mode: 'navigate', url };
      handler({ request, respondWith(promise) { pending = Promise.resolve(promise); } });
      assert.ok(pending, 'Navigation request must be handled');
      return pending;
    },
    async dispatchFetch(url) {
      let pending;
      const handler = listeners.get('fetch');
      assert.ok(handler, 'Service Worker fetch handler should exist');
      const request = new Request(url, { method: 'GET' });
      handler({ request, respondWith(promise) { pending = Promise.resolve(promise); } });
      assert.ok(pending, 'Same-origin asset request must be handled');
      return pending;
    }
  };
}

// First install: no active worker exists, so immediate activation is safe.
{
  const worker = createWorker({ active: false, failOptional: true });
  await worker.dispatchExtendable('install');
  assert.equal(worker.skipWaitingCalls, 1, 'first install should activate without waiting');
  const currentCache = [...worker.cacheStore.keys()].find(key => key.startsWith('toeic-vocab-github-only-v'));
  assert.ok(currentCache, 'the complete release cache should be created');
  const entries = worker.cacheStore.get(currentCache);
  assert.equal(entries.has('https://example.test/Toeic/assets/icons/icon.svg'), false, 'optional HTTP errors must not be cached');

  // Release-keyed data requests must reuse this release's canonical precache.
  const dataKey = 'https://example.test/Toeic/data/manifest.json';
  assert.equal(entries.has(dataKey), true, 'canonical data manifest should be precached');
  const callsBefore = worker.fetchCalls.length;
  const keyedData = await worker.dispatchFetch(`${dataKey}?__release=${releaseVersion}&__shell=${releaseVersion}`);
  assert.equal(await keyedData.clone().text(), `cached:${dataKey}`, 'new worker should normalize both release keys to its canonical data cache entry');
  assert.equal(worker.fetchCalls.length, callsBefore, 'release-keyed data hit must not refetch an already precached canonical file');
}

// Update: preserve the active cache and wait until a real user action sends SKIP_WAITING.
{
  const worker = createWorker({ active: true });
  worker.cacheStore.set('toeic-vocab-github-only-v2.95.8', new Map([['legacy', new Response('old cache')]]));
  worker.cacheStore.set('unrelated-application-cache', new Map([['keep', new Response('keep')]]));
  await worker.dispatchExtendable('install');
  assert.equal(worker.skipWaitingCalls, 0, 'an update must remain waiting');
  assert.ok(worker.cacheStore.has('toeic-vocab-github-only-v2.95.8'), 'old release cache must remain until approval');
  assert.ok(worker.cacheStore.has('unrelated-application-cache'), 'unrelated cache must remain');

  await worker.dispatchMessage({ type: 'SKIP_WAITING' });
  assert.equal(worker.skipWaitingCalls, 1, 'only SKIP_WAITING message should activate the update');
  await worker.dispatchExtendable('activate');
  assert.equal(worker.claimCalls, 1, 'new worker should claim clients after activation');
  assert.equal(worker.cacheStore.has('toeic-vocab-github-only-v2.95.8'), false, 'old TOEIC cache should be removed after activation');
  assert.equal(worker.cacheStore.has('unrelated-application-cache'), true, 'unrelated cache should never be removed');

  // While a new worker waits for user approval, never serve fresh root HTML with old cached modules.
  const currentCache = [...worker.cacheStore.keys()].find(key => key.startsWith('toeic-vocab-github-only-v'));
  const indexKey = 'https://example.test/Toeic/index.html';
  const cache = worker.cacheStore.get(currentCache);
  const before = await cache.get(indexKey).clone().text();
  worker.setNavigationResponse(new Response('fresh next-release index', { status: 200 }));
  const rootResponse = await worker.dispatchNavigate('https://example.test/Toeic/');
  assert.equal(await rootResponse.clone().text(), before, 'root navigation must keep the active worker app shell until consent');
  assert.equal(await cache.get(indexKey).clone().text(), before, 'waiting release must not overwrite the active cached index');

  // A 404 deep-link navigation may fall back to cached index, but must never replace index.html.
  worker.setNavigationResponse(new Response('404 page', { status: 404 }));
  const response = await worker.dispatchNavigate('https://example.test/Toeic/not-found');
  assert.equal(response.status, 200, 'cached app shell should be used as a safe navigation fallback');
  assert.equal(await cache.get(indexKey).clone().text(), before, '404 response must not overwrite cached index.html');
}

// Failed required install deletes only the incomplete new cache and never activates it.
{
  const worker = createWorker({ active: true, failRequired: true });
  worker.cacheStore.set('toeic-vocab-github-only-v2.95.8', new Map([['legacy', new Response('old cache')]]));
  await assert.rejects(worker.dispatchExtendable('install'));
  assert.equal(worker.skipWaitingCalls, 0);
  assert.equal(worker.cacheStore.has('toeic-vocab-github-only-v2.95.8'), true);
  assert.equal(worker.cacheStore.size, 1, 'incomplete new cache must be deleted while old cache is preserved');
}

// App UI: the user explicitly accepts the waiting worker; controllerchange reloads once.
assert.match(html, /id="appUpdateBanner"[^>]*hidden/);
assert.match(html, /id="appUpdateApply"[^>]*>Tải lại</);
assert.match(appSource, /function showServiceWorkerUpdateBanner\(registration\)/);
assert.match(appSource, /function watchServiceWorkerUpdates\(registration\)/);
assert.match(appSource, /pending\.postMessage\(\{type:'SKIP_WAITING'\}\)/);
assert.match(appSource, /addEventListener\('controllerchange',reloadAfterWorkerSwap/);
assert.match(css, /\.app-update-banner/);

console.log('PASS: Service Worker release lifecycle — release-keyed data hits the canonical precache; first install activates; updates wait for consent; failures preserve the active cache; optional assets do not block; root shell stays coherent; 404 does not replace index; update banner is wired.');
