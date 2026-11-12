const VERSION = '2.26.0';
const CACHE_NAME = `toeic-vocab-github-only-v${VERSION}`;
const OLD_CACHE_PREFIX = 'toeic-vocab-github-only-v';

// REQUIRED: core app, startup data, all 26 A–Z files, and Part 1 SVG fallbacks.
// OPTIONAL: icons, topic illustrations, Part 1 licensed photos and attribution manifest; photo failures must not block installation.
const REQUIRED = ["./","./index.html","./manifest.webmanifest","./assets/css/app.css","./assets/css/design-system.css","./assets/js/app.js","./assets/js/mock-engine.js","./assets/js/notification-provider.js","./data/manifest.json","./data/categories.json","./data/related-terms.json","./data/grammar/lessons.json","./data/readings/reading-library.json","./data/listening/listening-library.json","./data/vocabulary/A.json","./data/vocabulary/B.json","./data/vocabulary/C.json","./data/vocabulary/D.json","./data/vocabulary/E.json","./data/vocabulary/F.json","./data/vocabulary/G.json","./data/vocabulary/H.json","./data/vocabulary/I.json","./data/vocabulary/J.json","./data/vocabulary/K.json","./data/vocabulary/L.json","./data/vocabulary/M.json","./data/vocabulary/N.json","./data/vocabulary/O.json","./data/vocabulary/P.json","./data/vocabulary/Q.json","./data/vocabulary/R.json","./data/vocabulary/S.json","./data/vocabulary/T.json","./data/vocabulary/U.json","./data/vocabulary/V.json","./data/vocabulary/W.json","./data/vocabulary/X.json","./data/vocabulary/Y.json","./data/vocabulary/Z.json","./assets/listening/part1-airport-suitcase.svg","./assets/listening/part1-meeting-documents.svg","./assets/listening/part1-photocopier.svg","./assets/listening/part1-presentation-room.svg","./assets/listening/part1-reception-plant.svg","./assets/listening/part1-restaurant-setting.svg","./assets/listening/part1-technician-inspection.svg","./assets/listening/part1-warehouse-box.svg"];
const OPTIONAL = ["./assets/icons/icon.svg","./assets/icons/icon-192.png","./assets/icons/icon-512.png","./assets/topics/airport.svg","./assets/topics/banking.svg","./assets/topics/career.svg","./assets/topics/communication.svg","./assets/topics/construction.svg","./assets/topics/customer.webp","./assets/topics/education.svg","./assets/topics/environment.svg","./assets/topics/event.svg","./assets/topics/finance.webp","./assets/topics/food.svg","./assets/topics/health.svg","./assets/topics/healthcare.svg","./assets/topics/hotel.svg","./assets/topics/legal.svg","./assets/topics/meeting.webp","./assets/topics/office.webp","./assets/topics/real_estate.svg","./assets/topics/shipping.webp","./assets/topics/shopping.svg","./assets/topics/technology.webp","./assets/topics/time.webp","./assets/topics/travel.webp","./assets/topics/weather.svg","./assets/listening/part1-meeting-documents.jpg","./assets/listening/part1-warehouse-box.jpg","./assets/listening/part1-technician-inspection.jpg","./assets/listening/part1-airport-suitcase.jpg","./assets/listening/part1-presentation-room.jpg","./assets/listening/part1-reception-plant.jpg","./assets/listening/part1-restaurant-setting.jpg","./assets/listening/part1-photocopier.jpg","./assets/listening/ATTRIBUTION.csv"];
const APP_SHELL = ["./","./index.html","./manifest.webmanifest","./assets/css/app.css","./assets/css/design-system.css","./assets/js/app.js","./assets/js/mock-engine.js","./assets/js/notification-provider.js","./data/manifest.json","./data/categories.json","./data/related-terms.json","./data/grammar/lessons.json","./data/readings/reading-library.json","./data/listening/listening-library.json","./data/vocabulary/A.json","./data/vocabulary/B.json","./data/vocabulary/C.json","./data/vocabulary/D.json","./data/vocabulary/E.json","./data/vocabulary/F.json","./data/vocabulary/G.json","./data/vocabulary/H.json","./data/vocabulary/I.json","./data/vocabulary/J.json","./data/vocabulary/K.json","./data/vocabulary/L.json","./data/vocabulary/M.json","./data/vocabulary/N.json","./data/vocabulary/O.json","./data/vocabulary/P.json","./data/vocabulary/Q.json","./data/vocabulary/R.json","./data/vocabulary/S.json","./data/vocabulary/T.json","./data/vocabulary/U.json","./data/vocabulary/V.json","./data/vocabulary/W.json","./data/vocabulary/X.json","./data/vocabulary/Y.json","./data/vocabulary/Z.json","./assets/icons/icon.svg","./assets/icons/icon-192.png","./assets/icons/icon-512.png","./assets/topics/airport.svg","./assets/topics/banking.svg","./assets/topics/career.svg","./assets/topics/communication.svg","./assets/topics/construction.svg","./assets/topics/customer.webp","./assets/topics/education.svg","./assets/topics/environment.svg","./assets/topics/event.svg","./assets/topics/finance.webp","./assets/topics/food.svg","./assets/topics/health.svg","./assets/topics/healthcare.svg","./assets/topics/hotel.svg","./assets/topics/legal.svg","./assets/topics/meeting.webp","./assets/topics/office.webp","./assets/topics/real_estate.svg","./assets/topics/shipping.webp","./assets/topics/shopping.svg","./assets/topics/technology.webp","./assets/topics/time.webp","./assets/topics/travel.webp","./assets/topics/weather.svg","./assets/listening/part1-airport-suitcase.svg","./assets/listening/part1-meeting-documents.svg","./assets/listening/part1-photocopier.svg","./assets/listening/part1-presentation-room.svg","./assets/listening/part1-reception-plant.svg","./assets/listening/part1-restaurant-setting.svg","./assets/listening/part1-technician-inspection.svg","./assets/listening/part1-warehouse-box.svg","./assets/listening/ATTRIBUTION.csv"];

self.addEventListener('install', event => {
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE_NAME);
    // Wait for every required fetch to settle before deciding whether installation succeeded.
    // This prevents a late request from repopulating a cache after a failed install is removed.
    const requiredResults = await Promise.allSettled(REQUIRED.map(async path => {
      const url = new URL(path, self.registration.scope);
      const response = await fetch(url, { cache: 'reload' });
      if (!response.ok) throw new Error(`Required app-shell resource failed: ${path} (${response.status})`);
      await cache.put(url, response);
    }));
    const requiredFailures = requiredResults.filter(result => result.status === 'rejected');
    if (requiredFailures.length) {
      await caches.delete(CACHE_NAME);
      const details = requiredFailures.map(result => result.reason?.message || String(result.reason)).join('; ');
      throw new Error(`Service Worker install aborted; required resources unavailable: ${details}`);
    }

    // Optional assets are best-effort. Never store an HTTP error response in Cache Storage.
    await Promise.all(OPTIONAL.map(async path => {
      try {
        const url = new URL(path, self.registration.scope);
        const response = await fetch(url, { cache: 'reload' });
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        await cache.put(url, response);
      } catch (error) {
        console.warn(`[SW] Optional resource not cached: ${path}`, error);
      }
    }));

    // Activate only after the complete required shell is installed.
    await self.skipWaiting();
  })());
});

self.addEventListener('activate', event => {
  event.waitUntil((async () => {
    const keys = await caches.keys();
    // Keep unrelated applications' caches untouched; remove only previous TOEIC app releases.
    await Promise.all(keys
      .filter(key => key.startsWith(OLD_CACHE_PREFIX) && key !== CACHE_NAME)
      .map(key => caches.delete(key)));
    await self.clients.claim();
  })());
});

self.addEventListener('fetch', event => {
  const request = event.request;
  if (request.method !== 'GET') return;

  const requestUrl = new URL(request.url);
  if (requestUrl.origin !== self.location.origin) return;

  const cacheableData = requestUrl.pathname.includes('/data/');
  if (cacheableData) {
    // Cache-first within this release: the app never mixes JSON from different releases offline.
    event.respondWith((async () => {
      const cache = await caches.open(CACHE_NAME);
      const cached = await cache.match(request);
      if (cached) return cached;
      const fresh = await fetch(request);
      if (fresh.ok) await cache.put(request, fresh.clone());
      return fresh;
    })());
    return;
  }

  if (request.mode === 'navigate') {
    event.respondWith((async () => {
      const cache = await caches.open(CACHE_NAME);
      const indexUrl = new URL('./index.html', self.registration.scope);
      const cachedIndex = await cache.match(indexUrl);
      try {
        const fresh = await fetch(request);
        if (fresh.ok) {
          // Only cache a successful root-app navigation as index.html; never cache error pages.
          const scopePath = new URL(self.registration.scope).pathname;
          if (requestUrl.pathname === scopePath || requestUrl.pathname === scopePath.replace(/\/$/, '')) {
            await cache.put(indexUrl, fresh.clone());
          }
          return fresh;
        }
        return cachedIndex || fresh;
      } catch (error) {
        if (cachedIndex) return cachedIndex;
        return new Response('Offline: ứng dụng chưa có bản index.html trong cache.', {
          status: 503, headers: { 'Content-Type': 'text/plain; charset=utf-8' }
        });
      }
    })());
    return;
  }

  event.respondWith((async () => {
    const cache = await caches.open(CACHE_NAME);
    const cached = await cache.match(request);
    if (cached) return cached;
    const fresh = await fetch(request);
    if (fresh.ok) await cache.put(request, fresh.clone());
    return fresh;
  })());
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
