import express from 'express';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const port = Number(process.env.PORT) || 3000;

app.disable('x-powered-by');

const BLOCKED_ROOT_FILES = new Set([
  '/server.js',
  '/package.json',
  '/package-lock.json',
  '/metadata.json',
  '/.env',
  '/.env.example'
]);

app.use((req, res, next) => {
  const reqPath = req.path;
  if (
    BLOCKED_ROOT_FILES.has(reqPath) ||
    reqPath.startsWith('/.') ||
    reqPath.startsWith('/docs/') ||
    reqPath.startsWith('/design/')
  ) {
    res.status(404).end();
    return;
  }
  if (reqPath === '/' || reqPath === '/index.html' || reqPath === '/sw.js' || reqPath === '/manifest.webmanifest') {
    res.setHeader('Cache-Control', 'no-cache, no-store, must-revalidate');
  }
  next();
});

app.use(
  express.static(__dirname, {
    dotfiles: 'ignore',
    index: 'index.html',
    setHeaders(res, filePath) {
      if (filePath.endsWith('.js') || filePath.endsWith('.mjs')) {
        res.setHeader('Content-Type', 'application/javascript; charset=utf-8');
      } else if (filePath.endsWith('.webmanifest')) {
        res.setHeader('Content-Type', 'application/manifest+json; charset=utf-8');
      }
    }
  })
);

app.get('*', (req, res, next) => {
  if (req.method !== 'GET' || path.extname(req.path)) {
    next();
    return;
  }
  res.setHeader('Cache-Control', 'no-cache, no-store, must-revalidate');
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(port, '0.0.0.0', () => {
  console.log(`TOEIC Dictionary server listening on http://0.0.0.0:${port}`);
});
