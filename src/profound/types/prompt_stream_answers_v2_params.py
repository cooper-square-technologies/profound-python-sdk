# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PromptStreamAnswersV2Params", "Filter"]


class PromptStreamAnswersV2Params(TypedDict, total=False):
    category_id: Required[str]

    end_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    start_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    cursor: Optional[str]

    filter: Optional[Filter]
    """A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group."""

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
                "search_queries",
                "analysis_types",
            ]
        ]
    ]
    """
    Which row fields to return: `run_id`, `date`, `model`, `topic`, `topic_id`,
    `region`, `persona`, `tags`, `prompt`, `prompt_id`, `response`, `mentions`,
    `citations`, `search_queries`, `analysis_types`. Omit for all of them.
    (Sentiment is not exposed on this endpoint yet.)
    """

    limit: Optional[int]
    """Page size; default 10, max 50."""

    max_results: Optional[int]
    """Stream endpoint only: cap the number of streamed rows (default: all)."""


_FilterReservedKeywords = TypedDict(
    "_FilterReservedKeywords",
    {
        "and": Optional[Iterable[object]],
        "not": object,
        "or": Optional[Iterable[object]],
    },
    total=False,
)


class Filter(_FilterReservedKeywords, total=False):
    """A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group."""

    field: Optional[str]

    op: Optional[str]

    value: object
