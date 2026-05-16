// 美股选股器 v2 - Service Worker (轻量版)
// 只缓存静态资源，HTML每次都从网络加载确保最新

const CACHE_NAME = 'screener-static-v2';
const STATIC_URLS = [
  '/icon-192.png',
  '/icon-512.png',
  '/manifest.json'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(STATIC_URLS))
  );
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => 
      Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', event => {
  // HTML/JS/CSS: 总是从网络加载，确保最新
  // 图片: 缓存优先
  const url = new URL(event.request.url);
  const isStatic = STATIC_URLS.some(p => url.pathname === p);
  
  if (isStatic) {
    event.respondWith(
      caches.match(event.request).then(resp => resp || fetch(event.request))
    );
  } else {
    event.respondWith(fetch(event.request).catch(() => caches.match(event.request)));
  }
});
