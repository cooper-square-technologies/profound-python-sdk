# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PromptStreamAnswersV2Params", "Filter"]


class PromptStreamAnswersV2Params(TypedDict, total=False):
    category_id: Required[str]

    start_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    end_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    include: Optional[
        List[
            Literal[
                "run_id",
                "date",
                "model",
                "topic",
                "topic_id",
                "persona",
                "region",
                "tags",
                "prompt",
                "prompt_id",
                "response",
                "mentions",
                "citations",
                "citation_details",
                "search_queries",
                "analysis_types",
                "sentiment_claims",
            ]
        ]
    ]
    """Which row fields to return: `run_id`, `date`, `model`, `topic`, `topic_id`, `region`, `persona`, `tags`, `prompt`, `prompt_id`, `response`, `mentions`, `citations`, `citation_details`, `search_queries`, `analysis_types`, `sentiment_claims`. Omit for all fields except `citation_details`, which must be requested explicitly because it is expensive."""

    filter: Optional[Filter]
    """and/or/not tree over `model`, `topic`, `region`, `persona`, `prompt`, `tag`, `analysis_type` (visibility/sentiment/factcheck); plus top-level `and` leaves `domain` or `page` (`is` one value, or `in` a list). Substring-search the prompt with `{"field": "prompt", "op": "contains", "value": "…"}`."""

    limit: Optional[int]
    """Page size; default 10, max 200."""

    max_results: Optional[int]
    """Stream endpoint only: cap the number of streamed rows (default: all)."""

    cursor: Optional[str]


_FilterReservedKeywords = TypedDict(
    "_FilterReservedKeywords",
    {
        "and": Optional[Iterable["Filter"]],
        "or": Optional[Iterable["Filter"]],
        "not": Optional["Filter"],
    },
    total=False,
)


class Filter(_FilterReservedKeywords, total=False):
    """A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group."""

    field: Optional[str]

    op: Optional[str]

    value: object
