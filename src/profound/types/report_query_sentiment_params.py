# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ReportQuerySentimentParams", "Sort"]


class ReportQuerySentimentParams(TypedDict, total=False):
    category_id: Required[str]

    asset: Required[str]
    """The brand name to analyze (sentiment is extracted on name, not id)."""

    start_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    end_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    comparison_start_date: Optional[str]
    """YYYY-MM-DD, ET, inclusive (with end)."""

    comparison_end_date: Optional[str]
    """YYYY-MM-DD, ET, inclusive (with start)."""

    group_by: List[
        Literal["date", "model", "topic", "region", "prompt", "persona", "tag", "theme", "claim", "run", "competitor"]
    ]

    metrics: Optional[List[Literal["positive_sentiment", "negative_sentiment", "occurrence"]]]

    interval: Literal["day", "week", "month"]

    filter: Optional["FilterNode"]
    """A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group."""

    sort: Sort

    include_cited_websites: bool
    """Return cited websites per row (only when grouping by `theme`/`claim`)."""

    limit: Optional[int]
    """Page size; default 10, max 50."""

    max_results: Optional[int]
    """Stream endpoint only: cap the number of streamed rows (default: all)."""

    cursor: Optional[str]


class Sort(TypedDict, total=False):
    field: Literal["occurrence", "positive_sentiment", "negative_sentiment"]

    dir: Literal["asc", "desc"]


from .shared_params.filter_node import FilterNode
