"""Academic Paper Decoder — FastAPI app.

Run with:  uvicorn app.main:app --reload
"""

from __future__ import annotations

from pathlib import Path

import requests
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from . import analyzer, pubmed

app = FastAPI(title="Academic Paper Decoder")

STATIC_DIR = Path(__file__).resolve().parent.parent / "static"

# Analyzing pasted text needs *some* substance to work with.
MIN_PASTED_CHARS = 200
MAX_PASTED_CHARS = 200_000


@app.get("/api/search")
def api_search(q: str, limit: int = 10):
    q = q.strip()
    if not q:
        raise HTTPException(400, "Empty query")
    try:
        results = pubmed.search(q, limit=min(max(limit, 1), 20))
    except requests.RequestException as e:
        raise HTTPException(502, f"PubMed is unreachable: {e}") from e
    return {"query": q, "results": results}


@app.get("/api/paper/{pmid}")
def api_paper(pmid: str):
    if not pmid.isdigit():
        raise HTTPException(400, "PMID must be numeric")
    try:
        return pubmed.fetch_paper(pmid)
    except LookupError as e:
        raise HTTPException(404, str(e)) from e
    except requests.RequestException as e:
        raise HTTPException(502, f"PubMed is unreachable: {e}") from e


class AnalyzeRequest(BaseModel):
    pmid: str | None = None
    text: str | None = None


@app.post("/api/analyze")
def api_analyze(req: AnalyzeRequest):
    paper = None
    pasted = None

    if req.pmid:
        if not req.pmid.isdigit():
            raise HTTPException(400, "PMID must be numeric")
        try:
            paper = pubmed.fetch_paper(req.pmid)
        except LookupError as e:
            raise HTTPException(404, str(e)) from e
        except requests.RequestException as e:
            raise HTTPException(502, f"PubMed is unreachable: {e}") from e
        if not paper.get("abstract") and not paper.get("fulltext"):
            raise HTTPException(
                422,
                "This record has no abstract or full text available to analyze. "
                "Try pasting the paper text instead.",
            )
    elif req.text:
        pasted = req.text.strip()
        if len(pasted) < MIN_PASTED_CHARS:
            raise HTTPException(
                422,
                f"Please paste at least {MIN_PASTED_CHARS} characters "
                "(an abstract or more) so there is enough to analyze.",
            )
        pasted = pasted[:MAX_PASTED_CHARS]
    else:
        raise HTTPException(400, "Provide either a pmid or pasted text")

    return StreamingResponse(
        analyzer.stream_analysis(paper, pasted),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


@app.get("/")
def index():
    return FileResponse(STATIC_DIR / "index.html")


app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
