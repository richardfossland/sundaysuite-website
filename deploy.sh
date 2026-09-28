#!/bin/sh
# Build, check and deploy sundaysuite.app to Cloudflare Pages (production).
#
# `wrangler pages deploy` uploads everything in the folder it is given and does
# not read .assetsignore, so the site is copied into a staging folder without
# the files listed there, and deployed from that folder (functions/ included —
# wrangler looks for it in the working directory).
set -e
cd "$(dirname "$0")"
python3 build.py
python3 check_links.py
out=$(mktemp -d)
trap 'rm -rf "$out"' EXIT
rsync -a --exclude-from=.assetsignore ./ "$out/"
cd "$out"
npx wrangler pages deploy . --project-name sundaysuite --branch main
