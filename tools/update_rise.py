#!/usr/bin/env python3
"""Replace lesson/tutorial folders on the SBE site with new Rise *web* exports.

Usage (run from the sbe-lessons folder):
  python3 tools/update_rise.py                      # all zips in the default inbox
  python3 tools/update_rise.py path/to/zip ...      # specific zips
  python3 tools/update_rise.py --dry-run            # show what would change
  python3 tools/update_rise.py --commit             # also make a local git commit

Rise web exports are named like
  lesson-02-brand-positioning-...-raw-AbCd1234.zip   -> lessons/02
  tutorial-01-seeing-brands-...-raw-AbCd1234.zip     -> tutorials/01
The script refuses SCORM packages (use Export > Web in Rise).
"""
import argparse, io, json, re, shutil, subprocess, sys, tempfile, zipfile
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent
DEFAULT_INBOX = Path.home() / "Desktop/2STBRND Strategic Brand Engagement/Lesson packages/HTML"
NAME = re.compile(r"^(lesson|tutorial)-(\d{2})-.*-raw-([A-Za-z0-9_]+)\.zip$")

def target_for(zpath):
    m = NAME.match(zpath.name)
    if not m:
        raise SystemExit(f"Cannot tell which lesson/tutorial this is: {zpath.name}")
    kind, num, ver = m.groups()
    return SITE / ("lessons" if kind == "lesson" else "tutorials") / num, ver

def inspect(zpath):
    z = zipfile.ZipFile(zpath)
    names = z.namelist()
    idx = [n for n in names if n.endswith("index.html") and n.count("/") <= 1]
    if not idx:
        raise SystemExit(f"{zpath.name}: no index.html found")
    root = idx[0][: -len("index.html")]          # usually "content/"
    html = z.read(idx[0]).decode("utf-8", "ignore")
    if '"surface":"web-export"' not in html:
        raise SystemExit(f"{zpath.name}: not a Rise web export (did you export SCORM?)")
    title = re.search(r"<title>\s*([^<]*?)\s*</title>", html)
    anim = None
    rd = root + "runtime-data.js"
    if rd in names:
        s = z.read(rd).decode()
        m = re.search(r'__jsonp\("runtime-data.js","(.*?)"\)', s, re.S)
        if m:
            import base64
            course = json.loads(base64.b64decode(m.group(1)))["course"]
            anim = course.get("theme", {}).get("animateBlockEntrance")
    return z, root, (title.group(1) if title else "?"), anim

def replace(zpath, dry):
    dest, ver = target_for(zpath)
    z, root, title, anim = inspect(zpath)
    print(f"{zpath.name}\n  -> {dest.relative_to(SITE)}   title: {title}   block animation: {anim}")
    if dry:
        return dest, ver, title
    with tempfile.TemporaryDirectory() as tmp:
        for n in z.namelist():
            if not n.startswith(root) or n.endswith("/"):
                continue
            rel = n[len(root):]
            out = Path(tmp) / rel
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(z.read(n))
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(tmp, dest)
    return dest, ver, title

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("zips", nargs="*")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--commit", action="store_true")
    a = ap.parse_args()
    if a.zips:
        zips = [Path(p) for p in a.zips]
    else:  # newest export per lesson/tutorial only
        newest = {}
        for z in sorted(DEFAULT_INBOX.glob("*-raw-*.zip"), key=lambda z: z.stat().st_mtime):
            m = NAME.match(z.name)
            if m:
                newest[m.group(1, 2)] = z
        zips = list(newest.values())
    if not zips:
        sys.exit(f"No Rise web exports found in {DEFAULT_INBOX}")
    done = [replace(z, a.dry_run) for z in zips]
    if a.commit and not a.dry_run:
        paths = [str(d.relative_to(SITE)) for d, _, _ in done]
        subprocess.run(["git", "-C", str(SITE), "add", "-A", "--", *paths], check=True)
        msg = "Update " + ", ".join(f"{p} ({v})" for p, (_, v, _) in zip(paths, done))
        subprocess.run(["git", "-C", str(SITE), "commit", "-m", msg], check=True)
        print("Committed. Review, then push.")

if __name__ == "__main__":
    main()
