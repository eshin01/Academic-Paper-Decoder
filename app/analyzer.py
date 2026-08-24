"""Claude-powered paper analysis, streamed as Server-Sent Events."""

from __future__ import annotations

import json
import os
from collections.abc import Iterator

import anthropic

from .prompts import SYSTEM_PROMPT, build_user_message

MODEL = os.environ.get("DECODER_MODEL", "claude-opus-5")

_client: anthropic.Anthropic | None = None


def get_client() -> anthropic.Anthropic:
    global _client
    if _client is None:
        _client = anthropic.Anthropic()
    return _client


def _sse(event: str, data: dict) -> str:
    return f"event: {event}\ndata: {json.dumps(data)}\n\n"


def stream_analysis(paper: dict | None, pasted_text: str | None) -> Iterator[str]:
    """Yield SSE-formatted chunks of the analysis."""
    user_message = build_user_message(paper, pasted_text)

    try:
        client = get_client()
        # Streaming keeps long analyses under HTTP timeouts. Server-side
        # refusal fallbacks are enabled so a safety decline on the primary
        # model is retried on a fallback model within the same request.
        with client.beta.messages.stream(
            model=MODEL,
            max_tokens=64000,
            betas=["server-side-fallback-2026-07-01"],
            fallbacks="default",
            thinking={"type": "adaptive"},
            output_config={"effort": "high"},
            system=[
                {
                    "type": "text",
                    "text": SYSTEM_PROMPT,
                    "cache_control": {"type": "ephemeral"},
                }
            ],
            messages=[{"role": "user", "content": user_message}],
        ) as stream:
            for text in stream.text_stream:
                yield _sse("delta", {"text": text})
            final = stream.get_final_message()

        if final.stop_reason == "refusal":
            yield _sse(
                "error",
                {
                    "message": "The analysis was declined by the model's safety "
                    "system. Try a different paper or paste the text directly."
                },
            )
            return
        yield _sse("done", {"output_tokens": final.usage.output_tokens})

    except (anthropic.AuthenticationError, TypeError):
        # The SDK raises TypeError ("Could not resolve authentication method")
        # when no credentials are configured at all.
        yield _sse(
            "error",
            {
                "message": "No valid Anthropic API key found. Set ANTHROPIC_API_KEY "
                "(see .env.example) or run `ant auth login`, then restart the server."
            },
        )
    except anthropic.RateLimitError:
        yield _sse(
            "error",
            {"message": "Rate limited by the Claude API. Wait a minute and try again."},
        )
    except anthropic.APIStatusError as e:
        yield _sse("error", {"message": f"Claude API error ({e.status_code}): {e.message}"})
    except anthropic.APIConnectionError:
        yield _sse(
            "error",
            {"message": "Could not reach the Claude API. Check your network connection."},
        )
    except Exception as e:  # keep the SSE contract: never die mid-stream silently
        yield _sse("error", {"message": f"Unexpected error during analysis: {e}"})
