export default function handler(req, res) {
  res.setHeader('Content-Type', 'text/html; charset=utf-8');
  res.setHeader('X-Robots-Tag', 'noindex, nofollow, noarchive');
  res.setHeader('Cache-Control', 'public, max-age=31536000, immutable');
  res.status(410).send(
    '<!DOCTYPE html><html><head><meta name="robots" content="noindex, nofollow, noarchive"><title>410 Gone</title></head><body><h1>410 Gone</h1><p>This resource has been permanently removed from LivArt Salon.</p></body></html>'
  );
}
