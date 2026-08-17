# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["QueryFanoutsV2Query", "FilterNode", "AppRoutesV2AnswerEngineInsightsReportsQueryFanoutsSortSpec"]


class AppRoutesV2AnswerEngineInsightsReportsQueryFanoutsSortSpec(BaseModel):

    field: str

    dir: Optional[Literal["asc", "desc"]] = None

class FilterNode(BaseModel):

    and_: Optional[List[FilterNode]] = FieldInfo(alias="and", default=None)

    or_: Optional[List[FilterNode]] = FieldInfo(alias="or", default=None)

    not_: Optional[FilterNode] = FieldInfo(alias="not", default=None)

    field: Optional[str] = None

    op: Optional[str] = None

    value: Optional[str] = None



class QueryFanoutsV2Query(BaseModel):

    category_id: str

    start_date: str
    """YYYY-MM-DD, ET, inclusive"""

    end_date: str
    """YYYY-MM-DD, ET, inclusive"""

    group_by: Optional[List[Literal["date", "model", "region", "prompt", "query"]]] = None

    metrics: Optional[List[Literal["fanouts_per_execution", "total_fanouts", "share", "query_variations"]]] = None

    interval: Optional[Literal["day", "week", "month"]] = None

    filter: Optional[FilterNode] = None

    sort: Optional[AppRoutesV2AnswerEngineInsightsReportsQueryFanoutsSortSpec] = None

    limit: Optional[int] = None
    """Page size; default 10, max 50."""

    max_results: Optional[int] = None
    """Stream endpoint only: cap the number of streamed rows (default: all)."""

    cursor: Optional[str] = None
