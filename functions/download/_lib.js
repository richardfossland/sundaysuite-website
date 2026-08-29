// Shared helpers for the /download/<app>/* Pages Functions. Files starting
// with "_" are never routed by Cloudflare Pages.
//
// Version sources, in order:
//   1. The suite's update rings: GET updates.sundaysuite.app/v1/update/<app>/<ring>
//      → 200 JSON {version, pub_date, platforms} or 204 when nothing is promoted.
//      Default channel serves stable, falling through to beta on 204; an explicit
//      ?channel=beta serves the semver-HIGHEST of both rings, so a beta link can
//      never hand out something older than stable (the rings are promoted
//      independently and beta can lag).
//   2. GitHub's stable latest.json (releases/latest/download/latest.json) as a
//      fallback — and the only source for apps not on the rings.
// The feed's own platform URLs point at updater artifacts (.app.tar.gz / nsis),
// not installers, so the installer URL is constructed from the version instead.
// Every handler falls back to a releases-page redirect — never a 500.

const UPDATES = "https://updates.sundaysuite.app/v1/update";
const FEED_TTL = 900;
const UA = { "user-agent": "sundaysuite.app download redirector" };

export function redirect(location) {
  return new Response(null, { status: 302, headers: { location, "cache-control": "no-store" } });
}

async function cachedJson(context, cachePath, fetchUpstream) {
  const cache = caches.default;
  const key = new Request(`https://sundaysuite.app/__feeds/${cachePath}`);
  let res = await cache.match(key);
  if (!res) {
    res = await fetchUpstream();
    context.waitUntil(cache.put(key, res.clone()));
  }
  return res.json();
}

// One update ring, cached ~15 min per (app, ring). Resolves to null when the
// ring has nothing promoted (HTTP 204); throws on upstream errors.
export async function ringFeed(context, app, ring) {
  return cachedJson(context, `${app}-${ring}.json`, async () => {
    const upstream = await fetch(`${UPDATES}/${app}/${ring}`, { headers: UA });
    if (upstream.status === 204)
      return new Response("null", { headers: { "content-type": "application/json", "cache-control": `public, max-age=${FEED_TTL}` } });
    if (!upstream.ok) throw new Error(`ring ${app}/${ring}: ${upstream.status}`);
    return new Response(upstream.body, { status: 200, headers: { "content-type": "application/json", "cache-control": `public, max-age=${FEED_TTL}` } });
  });
}

// The stable latest.json shipped as a GitHub release asset.
export async function githubLatest(context, repo) {
  return cachedJson(context, `gh-${repo.replace("/", "-")}.json`, async () => {
    const upstream = await fetch(`https://github.com/${repo}/releases/latest/download/latest.json`, { headers: UA });
    if (!upstream.ok) throw new Error(`github latest ${repo}: ${upstream.status}`);
    return new Response(upstream.body, { status: 200, headers: { "content-type": "application/json", "cache-control": `public, max-age=${FEED_TTL}` } });
  });
}

// X.Y.Z[-pre] compare returning the larger input; a release beats a
// prerelease on the same base, and prerelease ids compare numerically.
export function semverMax(a, b) {
  if (!a) return b;
  if (!b) return a;
  const parse = (v) => { const [base, pre] = String(v).replace(/^v/, "").split("-", 2); return { nums: base.split(".").map(Number), pre: pre ?? null }; };
  const A = parse(a), B = parse(b);
  for (let i = 0; i < 3; i++) { const d = (A.nums[i] || 0) - (B.nums[i] || 0); if (d > 0) return a; if (d < 0) return b; }
  if (A.pre === null) return a;
  if (B.pre === null) return b;
  const sa = A.pre.split("."), sb = B.pre.split(".");
  for (let i = 0; i < Math.max(sa.length, sb.length); i++) {
    const x = sa[i], y = sb[i];
    if (x === undefined) return b;
    if (y === undefined) return a;
    const nx = Number(x), ny = Number(y);
    const d = Number.isNaN(nx) || Number.isNaN(ny) ? x.localeCompare(y) : nx - ny;
    if (d > 0) return a;
    if (d < 0) return b;
  }
  return a;
}

export function channelOf(request) {
  return new URL(request.url).searchParams.get("channel") === "beta" ? "beta" : "stable";
}

export async function pickFeed(context, app, channel) {
  if (channel === "beta") {
    const [stable, beta] = await Promise.all([
      ringFeed(context, app, "stable").catch(() => null),
      ringFeed(context, app, "beta").catch(() => null),
    ]);
    if (!stable && !beta) throw new Error("no version on any ring");
    if (!stable) return beta;
    if (!beta) return stable;
    return semverMax(stable.version, beta.version) === String(stable.version) ? stable : beta;
  }
  const stable = await ringFeed(context, app, "stable");
  if (stable) return stable;
  const beta = await ringFeed(context, app, "beta");
  if (beta) return beta;
  throw new Error("no version on any ring");
}

async function resolveFeed(context, { app, repo, rings }) {
  let feed = null;
  if (rings) {
    try { feed = await pickFeed(context, app, channelOf(context.request)); } catch { feed = null; }
  }
  if (!feed) {
    try { feed = await githubLatest(context, repo); } catch { feed = null; }
  }
  return feed;
}

// opts: app (ring name; unused when rings:false), repo "owner/name",
// appName asset prefix, macArch "aarch64"|"universal", rings, hasStableRelease
// (controls whether the fallback page is /releases/latest or /releases —
// /latest 404s on repos whose only releases are prereleases).
export function makeDownloadHandler(opts) {
  const { repo, appName, macArch = "aarch64", hasStableRelease = true } = opts;
  const RELEASES = `https://github.com/${repo}/releases`;
  const fallback = hasStableRelease ? `${RELEASES}/latest` : RELEASES;
  const mac = (v) => `${appName}_${v}_${macArch}.dmg`;
  const win = (v) => `${appName}_${v}_x64-setup.exe`;
  const ASSETS = { mac, macos: mac, windows: win, win };
  return async function onRequest(context) {
    const platform = String(context.params.platform || "").toLowerCase();
    const asset = ASSETS[platform];
    if (!asset) return redirect(fallback);
    const feed = await resolveFeed(context, opts);
    const version = String(feed?.version || "").replace(/^v/, "");
    if (!/^\d+\.\d+\.\d+/.test(version)) return redirect(fallback);
    return redirect(`${RELEASES}/download/v${version}/${asset(version)}`);
  };
}

export function makeVersionHandler(opts) {
  return async function onRequest(context) {
    const feed = await resolveFeed(context, opts);
    const version = String(feed?.version || "").replace(/^v/, "");
    if (!version) return new Response("{}", { status: 503, headers: { "content-type": "application/json", "cache-control": "no-store" } });
    return new Response(JSON.stringify({ version, pub_date: feed.pub_date || null }), {
      headers: { "content-type": "application/json", "cache-control": "public, max-age=300" },
    });
  };
}
