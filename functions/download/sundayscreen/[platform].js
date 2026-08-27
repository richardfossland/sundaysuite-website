// GET /download/sundayscreen/:platform → 302 to the latest SundayScreen
// installer on GitHub. Unlike SundayRec, the newest release may be a
// prerelease (beta), which GitHub's `releases/latest` never points at — so
// the version comes from the suite's own update feed instead: the stable
// ring first, then the beta ring (204 = nothing promoted on that ring).
// Cached ~15 min. Any failure falls back to the releases page — this route
// must never 500.
const REPO = "SundaySuite-app/sundayscreen";
const RELEASES = `https://github.com/${REPO}/releases`;
const FEEDS = [
  "https://updates.sundaysuite.app/v1/update/sundayscreen/stable",
  "https://updates.sundaysuite.app/v1/update/sundayscreen/beta",
];
const FEED_TTL = 900;
const CACHE_KEY = "https://sundaysuite.app/__feeds/sundayscreen-latest.json";

const ASSETS = {
  mac: (v) => `SundayScreen_${v}_aarch64.dmg`,
  macos: (v) => `SundayScreen_${v}_aarch64.dmg`,
  windows: (v) => `SundayScreen_${v}_x64-setup.exe`,
  win: (v) => `SundayScreen_${v}_x64-setup.exe`,
};

function redirect(location) {
  return new Response(null, { status: 302, headers: { location, "cache-control": "no-store" } });
}

async function latestFeed(context) {
  const cache = caches.default;
  const key = new Request(CACHE_KEY);
  const cached = await cache.match(key);
  if (cached) return cached.json();
  for (const feed of FEEDS) {
    const upstream = await fetch(feed, { headers: { "user-agent": "sundaysuite.app download redirector" } });
    if (upstream.status === 204) continue; // nothing promoted on this ring
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
  const platform = String(context.params.platform || "").toLowerCase();
  const asset = ASSETS[platform];
  if (!asset) return redirect(RELEASES);
  try {
    const feed = await latestFeed(context);
    const version = String(feed.version || "").replace(/^v/, "");
    if (!/^\d+\.\d+\.\d+/.test(version)) throw new Error("bad version: " + version);
    return redirect(`${RELEASES}/download/v${version}/${asset(version)}`);
  } catch {
    return redirect(RELEASES);
  }
}
