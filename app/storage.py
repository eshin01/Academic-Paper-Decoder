"""SQLite persistence for completed analyses (powers shareable links)."""

from __future__ import annotations

import os
import secrets
import sqlite3
import time
from pathlib import Path

DB_PATH = Path(
    os.environ.get(
        "DECODER_DB",
        Path(__file__).resolve().parent.parent / "data" / "analyses.db",
    )
)

_SCHEMA = """
CREATE TABLE IF NOT EXISTS analyses (
    id TEXT PRIMARY KEY,
    created_at INTEGER NOT NULL,
    source TEXT NOT NULL,
    title TEXT NOT NULL,
    pmid TEXT,
    markdown TEXT NOT NULL
)
"""


def _conn() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute(_SCHEMA)
    return conn


def save_analysis(title: str, source: str, markdown: str, pmid: str | None = None) -> str:
    """Store a finished analysis; returns its share id (URL slug)."""
    share_id = secrets.token_urlsafe(8)
    with _conn() as conn:
        conn.execute(
            "INSERT INTO analyses (id, created_at, source, title, pmid, markdown) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (share_id, int(time.time()), source, title[:300], pmid, markdown),
        )
    return share_id


def get_analysis(share_id: str) -> dict | None:
    with _conn() as conn:
        row = conn.execute(
            "SELECT id, created_at, source, title, pmid, markdown "
            "FROM analyses WHERE id = ?",
            (share_id,),
        ).fetchone()
    if row is None:
        return None
    return {
        "id": row[0],
        "created_at": row[1],
        "source": row[2],
        "title": row[3],
        "pmid": row[4],
        "markdown": row[5],
    }
