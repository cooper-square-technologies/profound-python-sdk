# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Annotated, Literal, Required, TypedDict
from ..._utils import PropertyInfo

__all__ = ["SentimentStreamV2V2ReportsStreamPostParams", "FilterNode", "AppRoutesV2AnswerEngineInsightsReportsSentimentSortSpec"]


class SentimentStreamV2V2ReportsStreamPostParams(TypedDict, total=False):

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

    group_by: Iterable[Literal["date", "model", "topic", "region", "prompt", "persona", "tag", "theme", "claim", "run", "competitor"]]

    metrics: Optional[Iterable[Literal["positive_sentiment", "negative_sentiment", "occurrence"]]]

    interval: Literal["day", "week", "month"]

    filter: Optional[FilterNode]

    sort: AppRoutesV2AnswerEngineInsightsReportsSentimentSortSpec

    include_cited_websites: bool
    """Return cited websites per row (only when grouping by `theme`/`claim`)."""

    limit: Optional[int]
    """Page size; default 10, max 50."""

    max_results: Optional[int]
    """Stream endpoint only: cap the number of streamed rows (default: all)."""

    cursor: Optional[str]


class AppRoutesV2AnswerEngineInsightsReportsSentimentSortSpec(TypedDict, total=False):

    field: Literal["occurrence", "positive_sentiment", "negative_sentiment"]

    dir: Literal["asc", "desc"]

class FilterNode(TypedDict, total=False):

    and_: Annotated[Optional[Iterable[FilterNode]], PropertyInfo(alias="and")]

    or_: Annotated[Optional[Iterable[FilterNode]], PropertyInfo(alias="or")]

    not_: Annotated[Optional[FilterNode], PropertyInfo(alias="not")]

    field: Optional[str]

    op: Optional[str]

    value: str

