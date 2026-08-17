# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Annotated, Literal, Required, TypedDict
from ..._utils import PropertyInfo

__all__ = ["QueryFanoutStreamV2V2ReportsStreamPostParams", "FilterNode", "AppRoutesV2AnswerEngineInsightsReportsQueryFanoutsSortSpec"]


class QueryFanoutStreamV2V2ReportsStreamPostParams(TypedDict, total=False):

    category_id: Required[str]

    start_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    end_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    group_by: Iterable[Literal["date", "model", "region", "prompt", "query"]]

    metrics: Optional[Iterable[Literal["fanouts_per_execution", "total_fanouts", "share", "query_variations"]]]

    interval: Literal["day", "week", "month"]

    filter: Optional[FilterNode]

    sort: Optional[AppRoutesV2AnswerEngineInsightsReportsQueryFanoutsSortSpec]

    limit: Optional[int]
    """Page size; default 10, max 50."""

    max_results: Optional[int]
    """Stream endpoint only: cap the number of streamed rows (default: all)."""

    cursor: Optional[str]


class AppRoutesV2AnswerEngineInsightsReportsQueryFanoutsSortSpec(TypedDict, total=False):

    field: Required[str]

    dir: Literal["asc", "desc"]

class FilterNode(TypedDict, total=False):

    and_: Annotated[Optional[Iterable[FilterNode]], PropertyInfo(alias="and")]

    or_: Annotated[Optional[Iterable[FilterNode]], PropertyInfo(alias="or")]

    not_: Annotated[Optional[FilterNode], PropertyInfo(alias="not")]

    field: Optional[str]

    op: Optional[str]

    value: str

