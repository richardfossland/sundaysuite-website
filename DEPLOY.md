# Deploy

Cloudflare Pages project **sundaysuite**; custom domains sundaysuite.app, www,
and sundayrec.com (redirected by `functions/_middleware.js`).

```
python3 build.py && python3 check_links.py
npx wrangler pages deploy . --project-name sundaysuite --branch main
```

`--branch main` is the production branch, so this goes straight to the live
domains. `.assetsignore` keeps the Python files and these notes out of the
upload. Allow about a minute for the new version to reach every edge before
checking it.
