# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional, Union
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["VisibilityV2Query", "EntityFilterClause", "FilterNode", "AppRoutesV2AnswerEngineInsightsReportsVisibilitySortSpec"]


class AppRoutesV2AnswerEngineInsightsReportsVisibilitySortSpec(BaseModel):

    field: Optional[Literal["visibility_score", "share_of_voice", "average_position"]] = None

class FilterNode(BaseModel):

    and_: Optional[List[FilterNode]] = FieldInfo(alias="and", default=None)

    or_: Optional[List[FilterNode]] = FieldInfo(alias="or", default=None)

    not_: Optional[FilterNode] = FieldInfo(alias="not", default=None)

    field: Optional[str] = None

    op: Optional[str] = None

    value: Optional[str] = None

class EntityFilterClause(BaseModel):

    op: Literal["is", "not_is", "in", "not_in", "contains", "not_contains", "matches", "contains_case_insensitive", "not_contains_case_insensitive"]

    value: Union[str, List[str]]



class VisibilityV2Query(BaseModel):

    category_id: str

    start_date: str
    """YYYY-MM-DD, ET, inclusive"""

    end_date: str
    """YYYY-MM-DD, ET, inclusive"""

    group_by: Optional[List[Literal["date", "model", "topic", "region", "prompt", "persona"]]] = None

    metrics: Optional[List[Literal["visibility_score", "share_of_voice", "average_position"]]] = None

    interval: Optional[Literal["day", "week", "month"]] = None

    scope: Optional[Literal["owned", "all"]] = None

    assets: Optional[Union[str, List[str], EntityFilterClause]] = None
    """A name (`is`), a list (`in`), or {op,value} with op `is`/`in`/`not_in`."""

    filter: Optional[FilterNode] = None

    sort: Optional[AppRoutesV2AnswerEngineInsightsReportsVisibilitySortSpec] = None

    limit: Optional[int] = None
    """Page size; default 10, max 50."""

    max_results: Optional[int] = None
    """Stream endpoint only: cap the number of streamed rows (default: all)."""

    cursor: Optional[str] = None
