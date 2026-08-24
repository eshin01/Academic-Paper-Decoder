# Academic Paper Decoder

A web app that makes scientific papers readable — and honestly graded — for
people with no training in statistics or scientific literature.

Too many headlines and social posts cite studies without knowing the study
type, the sample size, the power, or the limitations. This tool lets anyone:

1. **Find a paper** by title, topic, PMID, DOI, or PubMed link (searched live
   against PubMed), or paste paper text directly.
2. **Read it decoded** — the app pulls the abstract (and the full text when
   the paper is open access on PubMed Central) and analyzes it the way an
   editor-in-chief at a high-prestige journal would.

Every analysis follows the same seven-part structure:

| Section | What it gives the reader |
|---|---|
| The Gist | What the study did and found, in plain words |
| Study Snapshot | Study type, n, population, comparator, outcome, funding/COI |
| How Strong Is This Evidence? | A 1–5 grade with a plain-language justification |
| The Editor's Concerns | The peer-review critique, translated (power, bias, confounding, significance vs. effect size…) |
| Jargon Translator | The paper's actual technical terms, each defined in one sentence |
| What You Can (and Can't) Say | Fair claims vs. the tempting overreaches |
| Bottom Line for Your Life | What one study does — and doesn't — mean for you |

Explanations target an ~8th-grade reading level, prefer absolute numbers over
relative risk, and never invent facts not present in the paper. Observational
studies are always flagged as unable to prove cause and effect.

## Running it

```bash
pip install -r requirements.txt

# Credentials for the analysis engine (Claude). Either:
export ANTHROPIC_API_KEY=sk-ant-...   # from https://console.anthropic.com/
# ...or run `ant auth login` once — the SDK picks up the profile automatically.

uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000.

Paper search and retrieval use NCBI E-utilities (PubMed / PubMed Central) and
need no key. An optional `NCBI_API_KEY` raises the PubMed rate limit. See
`.env.example` for all settings.

## How it works

```
static/index.html      single-page UI: search → pick paper → streamed analysis
app/main.py            FastAPI routes (/api/search, /api/paper/{pmid}, /api/analyze)
app/pubmed.py          NCBI E-utilities client; PMC open-access full-text fetch
app/prompts.py         the "editor-in-chief" system prompt + paper packaging
app/analyzer.py        Claude call (claude-opus-5, streaming, adaptive thinking),
                       streamed to the browser as Server-Sent Events
```

Analysis notes:

- Uses `claude-opus-5` by default (override with `DECODER_MODEL`), streaming
  with adaptive thinking, so long papers produce responses without timeouts.
- Server-side refusal fallbacks are enabled (`fallbacks: "default"`), so a
  safety decline on the primary model is automatically retried on a fallback
  model within the same request.
- The system prompt is byte-stable and cached (`cache_control: ephemeral`),
  which cuts input cost on repeated analyses.
- When a paper is not open access, only the abstract is analyzed — and the
  output says so explicitly, since abstracts often oversell results.

## Honest limits

- This is an educational tool, **not medical advice**, and the page says so.
- The grade is a model's judgment from the text provided; it cannot see data
  the paper doesn't report, and abstract-only analyses are inherently shallower.
- One study is one data point — the output reminds readers of that every time.
