// GET /download/sundayrec/version → {"version":"0.10.0","pub_date":"..."} for
// the latest SundayRec release. Same cached feed as [platform].js (literal
// routes win over [param] routes, so this path is never treated as a platform).
const RELEASES = "https://github.com/SundaySuite-app/sundayrec/releases";
const FEED = `${RELEASES}/latest/download/latest.json`;
const FEED_TTL = 900;
const CACHE_KEY = "https://sundaysuite.app/__feeds/sundayrec-latest.json";

async function latestFeed(context) {
  const cache = caches.default;
  const key = new Request(CACHE_KEY);
  let res = await cache.match(key);
  if (!res) {
    const upstream = await fetch(FEED, { headers: { "user-agent": "sundaysuite.app download redirector" } });
    if (!upstream.ok) throw new Error("feed " + upstream.status);
    res = new Response(upstream.body, {
      status: 200,
      headers: { "content-type": "application/json", "cache-control": `public, max-age=${FEED_TTL}` },
    });
    context.waitUntil(cache.put(key, res.clone()));
  }
  return res.json();
}

export async function onRequest(context) {
  try {
    const feed = await latestFeed(context);
    const version = String(feed.version || "").replace(/^v/, "");
    if (!version) throw new Error("no version in feed");
    return new Response(JSON.stringify({ version, pub_date: feed.pub_date || null }), {
      headers: { "content-type": "application/json", "cache-control": "public, max-age=300" },
    });
  } catch {
    return new Response("{}", { status: 503, headers: { "content-type": "application/json", "cache-control": "no-store" } });
  }
}
