# Deploy

Cloudflare Pages project **sundaysuite**; custom domains sundaysuite.app, www,
and sundayrec.com (redirected by `functions/_middleware.js`).

```
./deploy.sh
```

It builds, runs the link check, copies the site into a staging folder without
the files listed in `.assetsignore` (the Python, these notes, dotfiles) and runs
`wrangler pages deploy` from there. `wrangler pages deploy` itself ignores
`.assetsignore`, so do not deploy the repository folder directly — the source
files would be served. `--branch main` is the production branch, so this goes
straight to the live domains. Allow about a minute for the new version to reach every edge before
checking it.
