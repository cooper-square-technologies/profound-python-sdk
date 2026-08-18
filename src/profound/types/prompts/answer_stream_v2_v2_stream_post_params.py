# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AnswerStreamV2V2StreamPostParams"]


class AnswerStreamV2V2StreamPostParams(TypedDict, total=False):
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

    filter: Optional["FilterNode"]
    """and/or/not tree over `model`, `topic`, `region`, `persona`, `prompt`, `tag`, `analysis_type` (visibility/sentiment/factcheck); plus top-level `and` leaves `domain` or `page` (`is` one value, or `in` a list). Substring-search the prompt with `{"field": "prompt", "op": "contains", "value": "…"}`."""

    limit: Optional[int]
    """Page size; default 10, max 200."""

    max_results: Optional[int]
    """Stream endpoint only: cap the number of streamed rows (default: all)."""

    cursor: Optional[str]


from ..shared_params.filter_node import FilterNode
