# Strategic Brand Engagement resource library

Static teaching resource website for colleague review and sharing.

## Contents

- `index.html` — searchable resource library
- `assets/` — landing-page styling and search
- `lessons/01/` through `lessons/08/` — existing interactive lesson exports
- `tutorials/01/` through `tutorials/06/` — existing tutorial exports
- `figma/04/` — Figma walkthrough
- `resources/briefs/` — four assignment briefs
- `resources/examples/` — anonymous example collections, PDFs, a journey-map image and Figma downloads
- `resources/examples/a2/example-01/` through `example-06/` and `resources/examples/a3/example-01/` through `example-04/` — case study pages (`index.html`), styled by `assets/case-study.css`

Exported course asset names are preserved because the course players refer to them internally. Public resource paths use lowercase names and hyphens.

## Local review

From this directory, run `python3 -m http.server 8765` and open `http://localhost:8765`.

The assessment briefs retain their supplied content. A2 intentionally includes `[Client]` placeholders.

## Publishing preparation

Published with GitHub Pages at https://tiin-tinn.github.io/sbe-lessons/ from the `main` branch.

`resources/examples/a2/example-05/prototype.fig` exceeds GitHub's 100 MiB per-file repository limit. It is retained for local review and excluded from Git. Its download link is hidden from `index.html` until the file is uploaded as a GitHub Release asset; then add a link to the verified release download URL under A2 Example 05.

The other Figma files are downloads intended for import into Figma. They are not browser-based interactive previews.

The original student submission HTML was excluded from the public resource tree because it contained identifying submission metadata and an owner-linked URL. Its PDF deliverables and Figma source are included under anonymous example labels. Original files and the private rename map are retained outside this repository in the Codex task workspace.

## Case studies

Each A2 example folder holds a case study page, the anonymised deliverables, a Figma source download and selected images in `images/`. Example 01's design document was compressed for the web, and a borrowed Singpass screenshot in Example 02's prototype board had its account name removed; originals are kept in `../originals/a2/`.


Each A3 example folder holds a case study page, the redacted presentation PDF, selected slide images in `images/` and, for Example 01, compressed MP4 videos. Group member names were removed from the PDF covers and closing slides; the unredacted originals are kept outside this repository in `../originals/a3/`. The page summaries were drafted from each team's slides and can be edited directly in each `index.html`.

## Updating a lesson or tutorial

1. In Rise, Export > **Web** and save the zip to `2STBRND Strategic Brand Engagement/Lesson packages/HTML`.
2. From this folder run `python3 tools/update_rise.py --dry-run` to see which folder each zip will replace, then `python3 tools/update_rise.py --commit`.
3. Review the commit and push to `main`.

Zip names decide the target: `lesson-02-…-raw-XXXX.zip` → `lessons/02`, `tutorial-01-…-raw-XXXX.zip` → `tutorials/01`. SCORM packages are refused.
