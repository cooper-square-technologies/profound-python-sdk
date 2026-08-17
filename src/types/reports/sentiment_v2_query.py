# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SentimentV2Query", "FilterNode", "AppRoutesV2AnswerEngineInsightsReportsSentimentSortSpec"]


class AppRoutesV2AnswerEngineInsightsReportsSentimentSortSpec(BaseModel):

    field: Optional[Literal["occurrence", "positive_sentiment", "negative_sentiment"]] = None

    dir: Optional[Literal["asc", "desc"]] = None

class FilterNode(BaseModel):

    and_: Optional[List[FilterNode]] = FieldInfo(alias="and", default=None)

    or_: Optional[List[FilterNode]] = FieldInfo(alias="or", default=None)

    not_: Optional[FilterNode] = FieldInfo(alias="not", default=None)

    field: Optional[str] = None

    op: Optional[str] = None

    value: Optional[str] = None



class SentimentV2Query(BaseModel):

    category_id: str

    asset: str
    """The brand name to analyze (sentiment is extracted on name, not id)."""

    start_date: str
    """YYYY-MM-DD, ET, inclusive"""

    end_date: str
    """YYYY-MM-DD, ET, inclusive"""

    comparison_start_date: Optional[str] = None
    """YYYY-MM-DD, ET, inclusive (with end)."""

    comparison_end_date: Optional[str] = None
    """YYYY-MM-DD, ET, inclusive (with start)."""

    group_by: Optional[List[Literal["date", "model", "topic", "region", "prompt", "persona", "tag", "theme", "claim", "run", "competitor"]]] = None

    metrics: Optional[List[Literal["positive_sentiment", "negative_sentiment", "occurrence"]]] = None

    interval: Optional[Literal["day", "week", "month"]] = None

    filter: Optional[FilterNode] = None

    sort: Optional[AppRoutesV2AnswerEngineInsightsReportsSentimentSortSpec] = None

    include_cited_websites: Optional[bool] = None
    """Return cited websites per row (only when grouping by `theme`/`claim`)."""

    limit: Optional[int] = None
    """Page size; default 10, max 50."""

    max_results: Optional[int] = None
    """Stream endpoint only: cap the number of streamed rows (default: all)."""

    cursor: Optional[str] = None
