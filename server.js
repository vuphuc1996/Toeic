import express from 'express';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const port = Number(process.env.PORT) || 3000;

app.disable('x-powered-by');

function sendNoCache(res) {
  res.setHeader('Cache-Control', 'no-cache, no-store, must-revalidate');
}

function sendIndex(req, res) {
  sendNoCache(res);
  res.sendFile(path.join(__dirname, 'index.html'));
}

// Serve only the runtime assets and application data required by the PWA.
// Repository tooling, tests, patches, documentation, and configuration stay private
// to the local/preview runtime instead of being exposed through the static root.
app.use(
  '/assets',
  express.static(path.join(__dirname, 'assets'), {
    dotfiles: 'ignore',
    index: false,
    setHeaders(res, filePath) {
      if (filePath.endsWith('.js') || filePath.endsWith('.mjs')) {
        res.setHeader('Content-Type', 'application/javascript; charset=utf-8');
      }
    }
  })
);

app.use(
  '/data',
  express.static(path.join(__dirname, 'data'), {
    dotfiles: 'ignore',
    index: false
  })
);

app.get(['/', '/index.html'], sendIndex);

app.get('/sw.js', (req, res) => {
  sendNoCache(res);
  res.sendFile(path.join(__dirname, 'sw.js'));
});

app.get('/manifest.webmanifest', (req, res) => {
  sendNoCache(res);
  res.type('application/manifest+json');
  res.sendFile(path.join(__dirname, 'manifest.webmanifest'));
});

// There are no path-based client routes; unknown paths must not fall back to
// index.html because that can disguise missing resources as successful responses.
app.use((req, res) => res.status(404).end());

app.listen(port, '0.0.0.0', () => {
  console.log(`TOEIC Dictionary server listening on http://0.0.0.0:${port}`);
});
