// Redirect the retired sundayrec.com domain (apex + www) to the SundayRec page
// on the main site. All other hosts (sundaysuite.app, *.pages.dev) pass through.
export async function onRequest(context) {
  const url = new URL(context.request.url);
  const host = url.hostname.toLowerCase();
  if (host === "sundayrec.com" || host === "www.sundayrec.com") {
    return Response.redirect("https://sundaysuite.app/apps/sundayrec", 301);
  }
  return context.next();
}
