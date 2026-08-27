// GET /download/sundayscreen/version → {"version":"0.9.0-beta.1","pub_date":"..."}
// for the newest promoted SundayScreen release. Same cached feed (stable ring,
// then beta) as [platform].js — literal routes win over [param] routes, so
// this path is never treated as a platform.
const FEEDS = [
  "https://updates.sundaysuite.app/v1/update/sundayscreen/stable",
  "https://updates.sundaysuite.app/v1/update/sundayscreen/beta",
];
const FEED_TTL = 900;
const CACHE_KEY = "https://sundaysuite.app/__feeds/sundayscreen-latest.json";

async function latestFeed(context) {
  const cache = caches.default;
  const key = new Request(CACHE_KEY);
  const cached = await cache.match(key);
  if (cached) return cached.json();
  for (const feed of FEEDS) {
    const upstream = await fetch(feed, { headers: { "user-agent": "sundaysuite.app download redirector" } });
    if (upstream.status === 204) continue;
    if (!upstream.ok) throw new Error("feed " + upstream.status);
    const body = await upstream.text();
    const res = new Response(body, {
      status: 200,
      headers: { "content-type": "application/json", "cache-control": `public, max-age=${FEED_TTL}` },
    });
    context.waitUntil(cache.put(key, res.clone()));
    return JSON.parse(body);
  }
  throw new Error("no ring promoted");
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
