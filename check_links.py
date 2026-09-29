#!/usr/bin/env python3
"""Quality gate for the generated site. Run after `python3 build.py`:

    python3 build.py && python3 check_links.py

Checks that
  1. every page build.py is meant to produce exists (both languages),
  2. every relative href/src resolves to a file on disk (links are
     extensionless, as Cloudflare Pages serves them),
  3. site-absolute paths only point at /download/ (Pages Functions) — the
     404 page is the one exception, since it is served at any depth,
  4. no banned string appears: retired marketing copy and claims that would
     quietly go stale.

Exits non-zero if anything is wrong, so it can gate a deploy.
"""
import os
import re
import sys

import build

ROOT = os.path.dirname(os.path.abspath(__file__))
ALLOWED_ABSOLUTE = ("/download/",)
SKIP_DIRS = {".git", "functions", ".wrangler", "node_modules", ".claude"}

BANNED = [
    ("Sunday Suite", "the name is written SundaySuite, one word"),
    # retired copy from the old marketing site
    ("ten times faster", "retired marketing copy"),
    ("ti ganger raskere", "retired marketing copy (NO)"),
    ("structurally impossible", "retired marketing copy"),
    ("strukturelt umulig", "retired marketing copy (NO)"),
    ("golden thread", "retired marketing copy"),
    ("Nordic alternative", "retired marketing copy"),
    ("nordisk alternativ", "retired marketing copy (NO)"),
    ("Twelve tools", "no product counts in headlines"),
    ("Tolv verktøy", "no product counts in headlines (NO)"),
    ("toolbox.html", "the toolbox page was retired"),
    ("verktoykasse", "the toolbox page was retired (NO)"),
    # stale facts
    ("richardfossland/sundayrec", "repo moved to the SundaySuite-app org"),
    ("richardfossland/sundayedit", "repo moved to the SundaySuite-app org"),
    ("richardfossland/sundaystudio", "repo moved to the SundaySuite-app org"),
    ('href="https://plan.sundaysuite.app', "SundayPlan is in development — no live link"),
    ('href="https://translate.sundaysuite.app', "SundayTranslate is in development — no live link"),
    ("Every public Sunday repository", "not every public repo has a licence file"),
    ("Hvert offentlige Sunday-repositorium", "not every public repo has a licence file (NO)"),
]


def resolve(page, url):
    """Map a relative link to the file Pages would serve for it."""
    target = url.split("#")[0].split("?")[0]
    if not target:
        return None
    path = os.path.normpath(os.path.join(os.path.dirname(page), target))
    if target.endswith("/") or target in (".", "./"):
        return os.path.join(path, "index.html")
    if os.path.splitext(target)[1]:
        return path
    return path + ".html"


def main():
    errors = []
    expected = [build.page_path(lang, name) for lang in build.LANGS for name in build.pages()] + ["404.html"]
    for rel in expected:
        if not os.path.exists(os.path.join(ROOT, rel)):
            errors.append(f"missing page {rel}")

    pages = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        pages += [os.path.join(dirpath, f) for f in filenames if f.endswith(".html")]
    stray = sorted(set(os.path.relpath(p, ROOT) for p in pages) - set(expected))
    for rel in stray:
        errors.append(f"stray page {rel} (not produced by build.py — delete it)")

    attr = re.compile(r'(?:href|src)="([^"]+)"')
    for page in sorted(pages):
        text = open(page, encoding="utf-8").read()
        rel = os.path.relpath(page, ROOT)
        for m in attr.finditer(text):
            url = m.group(1)
            if url.startswith(("http://", "https://", "mailto:", "#", "data:")):
                continue
            if url.startswith("/"):
                if rel == "404.html":
                    target = os.path.join(ROOT, resolve(os.path.join(ROOT, "404.html"), "." + url))
                    if not os.path.exists(target):
                        errors.append(f"{rel}: broken link {url}")
                elif not url.startswith(ALLOWED_ABSOLUTE):
                    errors.append(f"{rel}: unexpected absolute path {url}")
                continue
            target = resolve(page, url)
            if target and not os.path.exists(target):
                errors.append(f"{rel}: broken link {url}")
        for needle, why in BANNED:
            if needle.lower() in text.lower():
                errors.append(f"{rel}: banned string {needle!r} — {why}")

    print(f"checked {len(pages)} pages")
    if errors:
        print("\n".join(sorted(set(errors))), file=sys.stderr)
        print(f"\n{len(set(errors))} problem(s)", file=sys.stderr)
        return 1
    print("all pages present, all links resolve, no banned strings")
    return 0


if __name__ == "__main__":
    sys.exit(main())
