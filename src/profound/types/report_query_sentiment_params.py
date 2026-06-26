# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ReportQuerySentimentParams", "Filter", "Sort"]


class ReportQuerySentimentParams(TypedDict, total=False):
    asset: Required[str]
    """The brand name to analyze (sentiment is extracted on name, not id)."""

    category_id: Required[str]

    end_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    start_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    comparison_end_date: Optional[str]
    """YYYY-MM-DD, ET, inclusive (with start)."""

    comparison_start_date: Optional[str]
    """YYYY-MM-DD, ET, inclusive (with end)."""

    cursor: Optional[str]

    filter: Optional[Filter]
    """A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group."""

    group_by: List[
        Literal["date", "model", "topic", "region", "prompt", "persona", "tag", "theme", "claim", "run", "competitor"]
    ]

    include_cited_websites: bool
    """Return cited websites per row (only when grouping by `theme`/`claim`)."""

    interval: Literal["day", "week", "month"]

    limit: Optional[int]
    """Page size; default 10, max 50."""

    max_results: Optional[int]
    """Stream endpoint only: cap the number of streamed rows (default: all)."""

    metrics: Optional[List[Literal["positive_sentiment", "negative_sentiment", "occurrence"]]]

    sort: Sort


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


class Sort(TypedDict, total=False):
    dir: Literal["asc", "desc"]

    field: Literal["occurrence", "positive_sentiment", "negative_sentiment"]
