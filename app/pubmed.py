"""PubMed / PMC lookup via NCBI E-utilities.

No API key required. An optional NCBI_API_KEY env var raises the rate
limit from 3 to 10 requests/second.
"""

from __future__ import annotations

import os
import re
import xml.etree.ElementTree as ET

import requests

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
TOOL = "academic-paper-decoder"
TIMEOUT = 20

# Full text passed to the analyzer is capped so one enormous paper
# doesn't blow up request size or cost.
FULLTEXT_CHAR_CAP = 60_000


def _params(extra: dict) -> dict:
    p = {"tool": TOOL, **extra}
    key = os.environ.get("NCBI_API_KEY")
    if key:
        p["api_key"] = key
    return p


def _get(path: str, **extra) -> requests.Response:
    r = requests.get(f"{EUTILS}/{path}", params=_params(extra), timeout=TIMEOUT)
    r.raise_for_status()
    return r


def classify_query(q: str) -> str:
    """Turn a user query into a PubMed search term."""
    q = q.strip()
    if re.fullmatch(r"\d{5,9}", q):
        return f"{q}[pmid]"
    if re.match(r"^(https?://doi\.org/)?10\.\d{4,9}/\S+$", q, re.I):
        doi = re.sub(r"^https?://doi\.org/", "", q, flags=re.I)
        return f'"{doi}"[doi]'
    m = re.search(r"pubmed\.ncbi\.nlm\.nih\.gov/(\d+)", q)
    if m:
        return f"{m.group(1)}[pmid]"
    return q


def search(query: str, limit: int = 10) -> list[dict]:
    """Search PubMed; returns summaries for the top matches."""
    term = classify_query(query)
    r = _get(
        "esearch.fcgi",
        db="pubmed",
        term=term,
        retmode="json",
        retmax=limit,
        sort="relevance",
    )
    ids = r.json().get("esearchresult", {}).get("idlist", [])
    if not ids:
        return []
    return summaries(ids)


def summaries(pmids: list[str]) -> list[dict]:
    r = _get("esummary.fcgi", db="pubmed", id=",".join(pmids), retmode="json")
    result = r.json().get("result", {})
    out = []
    for pmid in result.get("uids", []):
        doc = result.get(pmid, {})
        authors = [a.get("name", "") for a in doc.get("authors", []) if a.get("name")]
        out.append(
            {
                "pmid": pmid,
                "title": doc.get("title", "").strip(),
                "journal": doc.get("fulljournalname") or doc.get("source", ""),
                "pubdate": doc.get("pubdate", ""),
                "authors": authors[:6],
                "author_count": len(authors),
                "pubtypes": doc.get("pubtype", []),
                "doi": next(
                    (
                        i.get("value")
                        for i in doc.get("articleids", [])
                        if i.get("idtype") == "doi"
                    ),
                    None,
                ),
            }
        )
    return out


def _text(el: ET.Element | None) -> str:
    return "".join(el.itertext()).strip() if el is not None else ""


def fetch_paper(pmid: str) -> dict:
    """Fetch title, abstract, and metadata for one PMID; try PMC full text."""
    r = _get("efetch.fcgi", db="pubmed", id=pmid, rettype="abstract", retmode="xml")
    root = ET.fromstring(r.content)
    art = root.find(".//Article")
    if art is None:
        raise LookupError(f"PMID {pmid} not found in PubMed")

    abstract_parts = []
    for ab in art.findall(".//Abstract/AbstractText"):
        label = ab.get("Label")
        body = _text(ab)
        abstract_parts.append(f"{label}: {body}" if label else body)

    mesh = [_text(d) for d in root.findall(".//MeshHeading/DescriptorName")]
    pubtypes = [_text(pt) for pt in art.findall(".//PublicationTypeList/PublicationType")]
    authors = []
    for a in art.findall(".//AuthorList/Author"):
        last, fore = _text(a.find("LastName")), _text(a.find("ForeName"))
        if last:
            authors.append(f"{fore} {last}".strip())

    coi = _text(root.find(".//CoiStatement"))
    grants = [_text(g) for g in art.findall(".//GrantList/Grant/Agency")]

    fulltext, pmcid = fetch_pmc_fulltext(pmid)

    return {
        "pmid": pmid,
        "pmcid": pmcid,
        "title": _text(art.find(".//ArticleTitle")),
        "journal": _text(art.find(".//Journal/Title")),
        "year": _text(art.find(".//JournalIssue/PubDate/Year"))
        or _text(art.find(".//JournalIssue/PubDate/MedlineDate")),
        "authors": authors,
        "abstract": "\n\n".join(p for p in abstract_parts if p),
        "pubtypes": pubtypes,
        "mesh_terms": mesh[:25],
        "coi_statement": coi,
        "funding_agencies": sorted(set(g for g in grants if g))[:10],
        "fulltext": fulltext,
        "has_fulltext": bool(fulltext),
    }


def fetch_pmc_fulltext(pmid: str) -> tuple[str, str | None]:
    """If the paper is in PubMed Central (open access), pull its body text."""
    try:
        r = _get(
            "elink.fcgi",
            dbfrom="pubmed",
            db="pmc",
            id=pmid,
            retmode="json",
            linkname="pubmed_pmc",
        )
        linksets = r.json().get("linksets", [])
        pmcid = None
        for ls in linksets:
            for db in ls.get("linksetdbs", []):
                if db.get("linkname") == "pubmed_pmc" and db.get("links"):
                    pmcid = db["links"][0]
                    break
        if not pmcid:
            return "", None

        r = _get("efetch.fcgi", db="pmc", id=pmcid, retmode="xml")
        root = ET.fromstring(r.content)
        body = root.find(".//body")
        if body is None:
            return "", f"PMC{pmcid}"

        chunks = []
        for el in body.iter():
            if el.tag == "title":
                t = _text(el)
                if t:
                    chunks.append(f"\n## {t}\n")
            elif el.tag == "p":
                t = _text(el)
                if t:
                    chunks.append(t)
            elif el.tag in ("table-wrap", "fig"):
                caption = _text(el.find(".//caption"))
                label = _text(el.find("label"))
                if caption or label:
                    kind = "Table" if el.tag == "table-wrap" else "Figure"
                    chunks.append(f"[{kind} {label}: {caption}]")
        text = "\n\n".join(chunks)
        if len(text) > FULLTEXT_CHAR_CAP:
            text = text[:FULLTEXT_CHAR_CAP] + "\n\n[... full text truncated for length ...]"
        return text, f"PMC{pmcid}"
    except Exception:
        # Full text is best-effort; the abstract alone is still analyzable.
        return "", None
