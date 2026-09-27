# Project Context

## Purpose
Working manuscript and public reading site for *Durable Forms: An Essay on Load Bearing Representations* (currently Draft 0.21, July 2026). The book argues that an organization's meaning should live in durable forms (assemblies) while applications, models, and people come and go as transient projections. It traces this idea from Plato, Aristotle, Langer, Deleuze, Shannon, and Deutsch/Marletto through to a constructive proposal (LogicalAssemblies, gates and swaps, projections and substrates).

The repo publishes the manuscript as a readable, searchable website on GitHub Pages (https://roskideluge.github.io/durable-forms). The markdown in `docs/` is where the book is written and revised.

## Tech Stack
- **Authoring source:** markdown files in `docs/`
- **Site generator:** Jekyll with the `just-the-docs` remote theme (`jekyll-remote-theme`)
- **Hosting:** GitHub Pages, built natively from the `docs/` directory on `main`
- **Local preview:** Ruby (Homebrew, ≥ 3.2) + Bundler + Jekyll 4.3 (`docs/Gemfile`)

## Project Conventions

### Code Style
- Content lives in `docs/` as one markdown file per section, named `NN-kebab-case-title.md`: `00-preface.md`, `01-…` through `10-…` for chapters, `99-works-cited.md`, and `part-1.md`–`part-4.md` as part index pages.
- Each page has YAML front matter: `title`, `nav_order`, `layout: default`, plus `parent` (the part title, e.g. `"Part I — Inheritance"`) and a `description` taken from the annotated table of contents. Part pages set `has_children: true`.
- Chapter headings follow the pattern `# Chapter N: Title`. Sections within a chapter are `##` headings with roman numerals (e.g. `## I. The First Projection Architecture`).
- Prose uses typographic punctuation (curly quotes, em dashes) carried over from the Word source. Don't swap it for ASCII.

### Architecture Patterns
- **`docs/*.md` is the source of truth.** Edit the chapter files directly; Jekyll on GitHub Pages renders them to HTML. (The site was originally bootstrapped from a Word draft via pandoc and a one-off split script; those tools are retired.)
- The annotated table of contents in `docs/index.md` and each chapter's front-matter `description` carry the same summary text. When a chapter's summary changes, update both.
- The theme is customized through overrides in `docs/_includes/`. Right now there is only `components/aux_nav.html`, a GitHub icon in the header that links to the current page's "edit on GitHub" URL (`/edit/main/docs/{{ page.path }}`).
- Site-wide settings (title, description, search, color scheme, footer draft label) live in `docs/_config.yml`.

### Testing Strategy
There are no automated tests. To verify a change:
- Run `cd docs && bundle install && bundle exec jekyll serve` and check the site at http://127.0.0.1:4000/: navigation order, part/chapter nesting, search, the header GitHub edit link, and the rendered typography.
- When adding, removing, or reordering chapters, check `nav_order` and `parent` values so the sidebar nesting stays correct.

### Git Workflow
- One branch, `main`, pushed to GitHub (`RoskiDeluge/durable-forms`). GitHub Pages deploys from `main:/docs`.
- Commit subjects are short, imperative, and capitalized (e.g. "Point header GitHub button at the current page's edit URL").
- Generated and local artifacts are gitignored: `_site/`, `.jekyll-cache/`, `Gemfile.lock`, `.DS_Store` (plus `full-book.md`, left over from the bootstrap import).

## Domain Context
- This is a philosophical and technical essay, not software. Most changes are to content, structure, or presentation. The book's vocabulary is deliberate, so don't "correct" it: durable form, projection, assembly / LogicalAssembly, load-bearing, gates and swaps, substrates, the "second problem" (semantics deferred by Shannon), "the graveyard".
- Structure: Preface ("On the Name"); Part I Inheritance; Part II The Argument; Part III The Construction; Part IV Horizon; 10 chapters in total; Works Cited.
- The draft version and date appear in several places: `README.md`, `docs/index.md`, and `docs/_config.yml` (`description` and `footer_content`). Update all of them when the draft version is bumped.

## Important Constraints
- GitHub Pages builds with its own older stack (Jekyll 3.9 / `github-pages` gem). Only use plugins and theme features that Pages supports. The local Jekyll 4 Gemfile exists only because Jekyll 3.9 won't run on Ruby ≥ 3.2.
- The macOS system Ruby is too old for local preview. Use Homebrew Ruby.
- Keep the site static with no build step beyond what GitHub Pages does natively (no Actions workflow at present).
- The manuscript is a work in progress, and the site should always say which draft it shows.

## External Dependencies
- **GitHub Pages:** hosting and the Jekyll build.
- **just-the-docs** (`just-the-docs/just-the-docs`, loaded as a remote theme): layout, navigation, search.
- **RubyGems:** jekyll, jekyll-remote-theme, jekyll-seo-tag, jekyll-include-cache, webrick (local preview only).
