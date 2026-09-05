#!/usr/bin/env python3
"""Quality gate for the generated site. Run after `python3 build.py`:

    python3 build.py && python3 check_links.py

Checks every generated page for
  1. broken relative links (href/src that resolve to nothing on disk),
  2. unexpected site-absolute paths (only /download/, /build, /no/bygg are served
     by Pages Functions or exist as pages),
  3. banned strings — claims that were true once and would quietly go stale.

Exits non-zero on the first problem found, so it can gate a deploy.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
ALLOWED_ABSOLUTE = ("/download/", "/build", "/no/bygg")

# Strings that must never reappear. Each one was true at some point; leaving it
# in place would be a lie rather than a typo, so it is worth failing the build.
BANNED = [
    ("richardfossland/sundayrec", "repo moved to the SundaySuite-app org"),
    ("richardfossland/sundayedit", "repo moved to the SundaySuite-app org"),
    ("richardfossland/sundaystudio", "repo moved to the SundaySuite-app org"),
    ('href="https://plan.sundaysuite.app', "SundayPlan is on the drawing board — no live link"),
    ('href="https://translate.sundaysuite.app', "SundayTranslate is in development — no live link"),
    ("open test phase", "retired framing"),
    ("åpen testfase", "retired framing (NO)"),
    ('class="status live"', "the Live tier was retired; everything usable is Beta"),
    ("Eleven tools", "product count is twelve"),
    ("Elleve verktøy", "product count is twelve (NO)"),
    ("SundayPlan family", "Booking is framed around the Sunday account now"),
    ("SundayPlan-familien", "Booking is framed around the Sunday account now (NO)"),
    ("Eight widgets", "SundayScreen is a planner now, not a widget board"),
    ("Åtte widgets", "SundayScreen is a planner now (NO)"),
    ("none of the licence bookkeeping has shipped", "the SundayStage song usage log shipped"),
    ("ingenting av lisensbokføringen har rukket ut", "the song usage log shipped (NO)"),
]

def main():
    pages, errors = [], []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in (".git", "functions", ".wrangler", "node_modules")]
        pages += [os.path.join(dirpath, f) for f in filenames if f.endswith(".html")]

    attr = re.compile(r'(?:href|src)="([^"]+)"')
    for path in sorted(pages):
        text = open(path, encoding="utf-8").read()
        rel = os.path.relpath(path, ROOT)
        for m in attr.finditer(text):
            url = m.group(1)
            if url.startswith(("http://", "https://", "mailto:", "#", "data:")):
                continue
            if url.startswith("/"):
                if not url.startswith(ALLOWED_ABSOLUTE):
                    errors.append(f"{rel}: unexpected absolute path {url}")
                continue
            target = url.split("#")[0].split("?")[0]
            if target and not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(path), target))):
                errors.append(f"{rel}: broken link {url}")
        for needle, why in BANNED:
            if needle in text:
                errors.append(f"{rel}: banned string {needle!r} — {why}")

    print(f"checked {len(pages)} pages")
    if errors:
        print("\n".join(sorted(set(errors))), file=sys.stderr)
        print(f"\n{len(set(errors))} problem(s)", file=sys.stderr)
        return 1
    print("all links resolve, no stale claims")
    return 0

if __name__ == "__main__":
    sys.exit(main())
