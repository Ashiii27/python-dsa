# Website — Python DSA Masterclass

The course website for this repository. **The repository markdown is the single
source of truth** — this folder contains only the site shell; all lesson, topic,
problem, guide, and practice pages are generated from the repo content on every
build by `scripts/generate_content.py`.

## Develop locally

```bash
cd website
npm install
npm start          # generate content + dev server with hot reload
```

Production build:

```bash
npm run build      # generate content + static site in website/build/
npm run serve      # preview the production build
```

## Structure

| Path | What it is |
|---|---|
| `scripts/generate_content.py` | Content pipeline: repo markdown/Python → site pages |
| `docs-python/ … docs-practice/` | Generated pages (gitignored — do not edit) |
| `src/pages/index.js` | Home page |
| `src/components/PyRunner.js` | In-browser Python runner (Pyodide) |
| `src/components/TrackProgress.js` | Persistent per-track progress checklists |
| `docusaurus.config.js` | Site config (navbar, footer, search, mermaid) |

## Deployment

GitHub Actions (`.github/workflows/website.yml`) builds and deploys to GitHub
Pages on every push to `main`. The site lives at
`https://ashiii27.github.io/python-dsa/` (`SITE_BASE_URL=/python-dsa/` in CI).

## Adding content

Edit the markdown in `python/`, `topics/`, `docs/`, or `practice/` — then run
`npm run gen` (or just build). The generator remaps links, embeds the `.py`
sources, and wires the interactive components automatically.
