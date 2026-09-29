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

Exported course asset names are preserved because the course players refer to them internally. Public resource paths use lowercase names and hyphens.

## Local review

From this directory, run `python3 -m http.server 8765` and open `http://localhost:8765`.

The assessment briefs retain their supplied content. A2 intentionally includes `[Client]` placeholders.

## Publishing preparation

Published with GitHub Pages at https://tiin-tinn.github.io/sbe-lessons/ from the `main` branch.

`resources/examples/a2/example-05/prototype.fig` exceeds GitHub's 100 MiB per-file repository limit. It is retained for local review and excluded from Git. Its download link is hidden from `index.html` until the file is uploaded as a GitHub Release asset; then add a link to the verified release download URL under A2 Example 05.

The other Figma files are downloads intended for import into Figma. They are not browser-based interactive previews.

The original student submission HTML was excluded from the public resource tree because it contained identifying submission metadata and an owner-linked URL. Its PDF deliverables and Figma source are included under anonymous example labels. Original files and the private rename map are retained outside this repository in the Codex task workspace.
