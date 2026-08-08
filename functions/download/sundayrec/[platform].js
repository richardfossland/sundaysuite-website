// GET /download/sundayrec/:platform → 302 to the latest SundayRec installer on
// GitHub. The current version is read from the release feed (latest.json, a
// stable URL that always points at the newest release) and cached ~15 min.
// The feed's own platform URLs point at updater artifacts, not installers, so
// the installer URL is constructed from the version instead. Any failure falls
// back to the releases page — this route must never 500.
const REPO = "SundaySuite-app/sundayrec";
const RELEASES = `https://github.com/${REPO}/releases`;
const FEED = `${RELEASES}/latest/download/latest.json`;
const FEED_TTL = 900;
const CACHE_KEY = "https://sundaysuite.app/__feeds/sundayrec-latest.json";

const ASSETS = {
  mac: (v) => `SundayRec_${v}_aarch64.dmg`,
  macos: (v) => `SundayRec_${v}_aarch64.dmg`,
  windows: (v) => `SundayRec_${v}_x64-setup.exe`,
  win: (v) => `SundayRec_${v}_x64-setup.exe`,
};

function redirect(location) {
  return new Response(null, { status: 302, headers: { location, "cache-control": "no-store" } });
}

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
  const platform = String(context.params.platform || "").toLowerCase();
  const asset = ASSETS[platform];
  if (!asset) return redirect(`${RELEASES}/latest`);
  try {
    const feed = await latestFeed(context);
    const version = String(feed.version || "").replace(/^v/, "");
    if (!/^\d+\.\d+\.\d+/.test(version)) throw new Error("bad version: " + version);
    return redirect(`${RELEASES}/download/v${version}/${asset(version)}`);
  } catch {
    return redirect(`${RELEASES}/latest`);
  }
}
