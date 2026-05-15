// 美股选股器 v2 - Service Worker
// 版本号：每次更新代码时修改此版本号，用户会自动更新

const CACHE_NAME = 'screener-v2.0.0';
const VERSION_CHECK_URL = '/version.json';

const urlsToCache = [
  '/screener.html',
  '/screener-style.css',
  '/screener-data.js',
  '/manifest.json',
  '/icon-192.png',
  '/icon-512.png'
];

// 安装：缓存核心资源
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      console.log('[SW] 缓存核心资源');
      return cache.addAll(urlsToCache);
    })
  );
  self.skipWaiting();
});

// 激活：清理旧缓存
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => {
      return Promise.all(
        keys.filter(k => k !== CACHE_NAME).map(k => {
          console.log('[SW] 清理旧缓存:', k);
          return caches.delete(k);
        })
      );
    })
  );
  self.clients.claim();
});

// 请求拦截：优先网络，失败则返回缓存
self.addEventListener('fetch', event => {
  // 只处理GET请求
  if (event.request.method !== 'GET') return;
  
  // 使用Stale-While-Revalidate策略
  event.respondWith(
    caches.open(CACHE_NAME).then(cache => {
      return fetch(event.request)
        .then(response => {
          // 更新缓存
          if (response.ok) {
            cache.put(event.request, response.clone());
          }
          return response;
        })
        .catch(() => {
          // 离线时返回缓存
          return cache.match(event.request);
        });
    })
  );
});

// 监听来自页面的版本检查消息
self.addEventListener('message', event => {
  if (event.data && event.data.type === 'CHECK_VERSION') {
    event.waitUntil(
      fetch(VERSION_CHECK_URL)
        .then(resp => resp.json())
        .then(versionData => {
          // 通知页面版本信息
          self.clients.matchAll().then(clients => {
            clients.forEach(client => {
              client.postMessage({
                type: 'VERSION_RESPONSE',
                data: versionData
              });
            });
          });
        })
        .catch(() => {
          // 离线时忽略
        })
    );
  }
});
