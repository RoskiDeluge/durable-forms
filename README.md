# Durable Forms

*An Essay on Load Bearing Representations* — working manuscript, Draft 0.21 (July 2026).

The book is published as a GitHub Pages site from the [`docs/`](docs/) directory. Each chapter is a standalone markdown file; the original manuscript is kept at the repo root as `durable-forms-draft-0.21.docx`.

## Structure

- `docs/index.md` — title page and annotated table of contents
- `docs/00-preface.md` — Preface: On the Name
- `docs/01-…10-*.md` — Chapters 1–10, grouped into Parts I–IV (`docs/part-*.md`)
- `docs/99-works-cited.md` — Works Cited
- `docs/_config.yml` — Jekyll configuration (just-the-docs theme, built natively by GitHub Pages)

## Local preview

```sh
cd docs
gem install bundler jekyll github-pages
jekyll serve
```

## Updating from a new draft

```sh
pandoc durable-forms-draft-<version>.docx -t gfm --wrap=none -o full-book.md
python3 scripts/split_book.py   # regenerates docs/ chapter files from full-book.md
```
