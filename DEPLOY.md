# Sunday Suite — deploy notes

Static site. English at root (primary), Norwegian under `/no/`, shared assets in `/assets/`.
Regenerate the HTML from content with:

```
python3 build.py
```

## Deploy to Cloudflare Pages

Project name: **sundaysuite**

1. Authenticate (one-time, opens a browser):
   ```
   npx wrangler login
   ```
2. Deploy the current folder:
   ```
   npx wrangler pages deploy . --project-name sundaysuite
   ```
   The first deploy creates the project. `.assetsignore` keeps `build.py` and these notes out of the upload.

3. Attach the custom domain `sundaysuite.app`:
   - Cloudflare dashboard → Workers & Pages → **sundaysuite** → Custom domains → *Set up a custom domain* → `sundaysuite.app` (and `www.sundaysuite.app`).
   - This requires the `sundaysuite.app` zone to be in the same Cloudflare account (nameservers pointed at Cloudflare). Pages adds the CNAME automatically.

Subsequent deploys: just rerun step 2.
