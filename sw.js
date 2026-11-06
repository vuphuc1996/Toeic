const CACHE_NAME = 'toeic-vocab-github-only-v2.4.1';
const APP_SHELL = ["./", "./index.html", "./manifest.webmanifest", "./assets/css/app.css", "./assets/js/app.js", "./assets/js/notification-provider.js", "./assets/icons/icon.svg", "./assets/icons/icon-192.png", "./assets/icons/icon-512.png", "./data/manifest.json", "./data/categories.json", "./data/related-terms.json", "./data/vocabulary/A.json", "./data/vocabulary/B.json", "./data/vocabulary/C.json", "./data/vocabulary/D.json", "./data/vocabulary/E.json", "./data/vocabulary/F.json", "./data/vocabulary/G.json", "./data/vocabulary/H.json", "./data/vocabulary/I.json", "./data/vocabulary/J.json", "./data/vocabulary/K.json", "./data/vocabulary/L.json", "./data/vocabulary/M.json", "./data/vocabulary/N.json", "./data/vocabulary/O.json", "./data/vocabulary/P.json", "./data/vocabulary/Q.json", "./data/vocabulary/R.json", "./data/vocabulary/S.json", "./data/vocabulary/T.json", "./data/vocabulary/U.json", "./data/vocabulary/V.json", "./data/vocabulary/W.json", "./data/vocabulary/X.json", "./data/vocabulary/Y.json", "./data/vocabulary/Z.json", "./data/verbs/irregular-verbs.json", "./data/grammar/lessons.json", "./data/readings/reading-library.json"];

self.addEventListener('install', event => {
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE_NAME);
    await Promise.allSettled(APP_SHELL.map(path => cache.add(path)));
    await self.skipWaiting();
  })());
});

self.addEventListener('activate', event => {
  event.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.filter(key => key.startsWith('toeic-vocab-') && key !== CACHE_NAME).map(key => caches.delete(key)));
    await self.clients.claim();
  })());
});

self.addEventListener('fetch', event => {
  const request = event.request;
  if (request.method !== 'GET' || new URL(request.url).origin !== self.location.origin) return;
  const requestPath = new URL(request.url).pathname;
  const isData = requestPath.includes('/data/');
  if (isData) {
    event.respondWith((async () => {
      const cache = await caches.open(CACHE_NAME);
      try { const fresh = await fetch(request); if (fresh.ok) cache.put(request, fresh.clone()); return fresh; }
      catch { const cached = await cache.match(request); if (cached) return cached; throw new Error('Offline: dữ liệu này chưa được cache.'); }
    })());
    return;
  }
  if (request.mode === 'navigate') {
    event.respondWith((async () => {
      try { const fresh = await fetch(request); const cache = await caches.open(CACHE_NAME); cache.put('./index.html', fresh.clone()); return fresh; }
      catch { const cache = await caches.open(CACHE_NAME); return (await cache.match(request)) || (await cache.match('./index.html')); }
    })());
    return;
  }
  event.respondWith((async () => { const cache = await caches.open(CACHE_NAME); const cached = await cache.match(request); if (cached) return cached; const fresh = await fetch(request); if (fresh.ok) cache.put(request,fresh.clone()); return fresh; })());
});

// Local persistent notifications created while the app is active. No remote Push subscription is used.

self.addEventListener('notificationclick', event => {
  event.notification.close();
  const data = event.notification.data || {};
  const targetUrl = data.url || new URL('./?open=practice', self.location.href).href;
  event.waitUntil((async () => {
    const windows = await self.clients.matchAll({ type: 'window', includeUncontrolled: true });
    for (const client of windows) {
      if ('focus' in client) {
        await client.focus();
        client.postMessage({ type: 'OPEN_PRACTICE', wordId: data.wordId || null });
        return;
      }
    }
    if (self.clients.openWindow) await self.clients.openWindow(targetUrl);
  })());
});
