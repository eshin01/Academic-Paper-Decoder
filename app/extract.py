"""Text extraction for uploaded paper files (PDF and Word)."""

from __future__ import annotations

import io
import re
import xml.etree.ElementTree as ET
import zipfile

from pypdf import PdfReader
from pypdf.errors import PdfReadError

MAX_UPLOAD_BYTES = 25 * 1024 * 1024

_W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


class ExtractionError(ValueError):
    """Raised with a user-facing message when a file can't be read."""


def extract_text(filename: str, data: bytes) -> str:
    if len(data) > MAX_UPLOAD_BYTES:
        raise ExtractionError("File is too large (25 MB max).")
    name = (filename or "").lower()
    if name.endswith(".pdf") or data[:5] == b"%PDF-":
        return extract_pdf(data)
    if name.endswith(".docx") or (data[:2] == b"PK" and b"word/" in data[:4096]):
        return extract_docx(data)
    raise ExtractionError("Unsupported file type. Please upload a .pdf or .docx file.")


def extract_pdf(data: bytes) -> str:
    try:
        reader = PdfReader(io.BytesIO(data))
        if reader.is_encrypted:
            # Many "encrypted" PDFs open with an empty owner password.
            if not reader.decrypt(""):
                raise ExtractionError(
                    "This PDF is password-protected. Remove the password and try again."
                )
        pages = [page.extract_text() or "" for page in reader.pages]
    except ExtractionError:
        raise
    except (PdfReadError, Exception) as e:  # pypdf raises assorted types on bad files
        raise ExtractionError(f"Could not read this PDF ({e}).") from e

    text = _clean("\n\n".join(pages))
    if len(text) < 200:
        raise ExtractionError(
            "No readable text found in this PDF — it may be a scanned image. "
            "Try copying the text out of the paper and pasting it instead."
        )
    return text


def extract_docx(data: bytes) -> str:
    try:
        with zipfile.ZipFile(io.BytesIO(data)) as zf:
            xml = zf.read("word/document.xml")
        root = ET.fromstring(xml)
    except (zipfile.BadZipFile, KeyError, ET.ParseError) as e:
        raise ExtractionError("Could not read this file as a Word (.docx) document.") from e

    paragraphs = []
    for p in root.iter(f"{_W}p"):
        runs = [t.text or "" for t in p.iter(f"{_W}t")]
        para = "".join(runs).strip()
        if para:
            paragraphs.append(para)
    text = _clean("\n\n".join(paragraphs))
    if len(text) < 200:
        raise ExtractionError(
            "This Word document has too little readable text to analyze."
        )
    return text


def _clean(text: str) -> str:
    text = text.replace("\x00", "")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()
