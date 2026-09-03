# Academic Paper Decoder — working notes

## The app
FastAPI backend (`app/`) + single-page frontend (`static/index.html`) that
decodes academic papers into plain English for non-scientists. The analysis
format lives in `app/prompts.py` (SYSTEM_PROMPT) — eight sections, ~8th-grade
reading level, including a **Statistics Spotlight** teaching section.

## The daily reading list
`reading-list/` is the user's durable memory of decoded papers:
- `index.md` — running log of every paper read (newest first, DOI-linked)
- `queue.md` — curated backlog of landmark medical-AI papers
- `summaries/` — one eight-section summary per paper
A daily 8AM routine decodes the next queue entry and appends here.

Every summary must carry verified source links (DOI, PubMed, full text used),
must prefer full text over abstract, and must never include an unverified or
guessed link.

## User-invoked shorthand

**"mental map"** → render the statistical landscape in
`reading-list/stats-mental-map.md` for the user, adapted to whatever they are
working on at the time (study design, appraising a paper, choosing metrics).
Draw the three report cards — discrimination, classification at a decision
point, calibration — plus the cross-cutting reality checks, and end with the
design checklist when they are planning a study. Keep it plain-English and
concrete; add worked numbers where they clarify. The file is the canonical
content; update it when the map is extended.
