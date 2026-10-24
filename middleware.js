export default function middleware(request) {
  const url = new URL(request.url);

  // 1. Force canonical redirect from www to non-www
  if (url.hostname.startsWith('www.')) {
    url.hostname = url.hostname.replace(/^www\./, '');
    return Response.redirect(url.toString(), 301);
  }

  const search = url.search.toLowerCase();
  const pathname = url.pathname.toLowerCase();

  // 2. Identify historical Japanese/Chinese ecommerce spam and Russian gambling injections
  const isSpamQuery =
    url.searchParams.has('m') ||
    search.includes('product') ||
    search.includes('picturesearch') ||
    search.includes('view_more') ||
    search.includes('shop/sold') ||
    search.includes('goods.php') ||
    search.includes('content.php') ||
    search.includes('shop.php');

  const isSpamPath =
    pathname.includes('.php') ||
    pathname.includes('kosmolot') ||
    pathname.includes('kto-vladelec') ||
    pathname.includes('oprovergaem-mify') ||
    pathname.includes('chto-osobennogo') ||
    pathname.includes('aapaa') ||
    pathname.includes('lp_business_gift') ||
    pathname.includes('wp-login') ||
    pathname.includes('wp-admin') ||
    pathname.includes('wp-includes');

  if (isSpamQuery || isSpamPath) {
    return new Response(
      '<!DOCTYPE html><html><head><meta name="robots" content="noindex, nofollow, noarchive"><title>410 Gone</title></head><body><h1>410 Gone</h1><p>This resource has been permanently removed from LivArt Salon.</p></body></html>',
      {
        status: 410,
        headers: {
          'Content-Type': 'text/html; charset=utf-8',
          'X-Robots-Tag': 'noindex, nofollow, noarchive',
          'Cache-Control': 'public, max-age=31536000, immutable'
        }
      }
    );
  }
}

export const config = {
  matcher: '/:path*',
};
