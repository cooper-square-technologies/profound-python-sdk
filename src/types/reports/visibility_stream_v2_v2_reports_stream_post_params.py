# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, Optional, Union
from typing_extensions import Annotated, Literal, Required, TypedDict
from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["VisibilityStreamV2V2ReportsStreamPostParams", "EntityFilterClause", "FilterNode", "AppRoutesV2AnswerEngineInsightsReportsVisibilitySortSpec"]


class VisibilityStreamV2V2ReportsStreamPostParams(TypedDict, total=False):

    category_id: Required[str]

    start_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    end_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    group_by: Iterable[Literal["date", "model", "topic", "region", "prompt", "persona"]]

    metrics: Optional[Iterable[Literal["visibility_score", "share_of_voice", "average_position"]]]

    interval: Literal["day", "week", "month"]

    scope: Literal["owned", "all"]

    assets: Optional[Union[str, SequenceNotStr[str], EntityFilterClause]]
    """A name (`is`), a list (`in`), or {op,value} with op `is`/`in`/`not_in`."""

    filter: Optional[FilterNode]

    sort: AppRoutesV2AnswerEngineInsightsReportsVisibilitySortSpec

    limit: Optional[int]
    """Page size; default 10, max 50."""

    max_results: Optional[int]
    """Stream endpoint only: cap the number of streamed rows (default: all)."""

    cursor: Optional[str]


class AppRoutesV2AnswerEngineInsightsReportsVisibilitySortSpec(TypedDict, total=False):

    field: Literal["visibility_score", "share_of_voice", "average_position"]

class FilterNode(TypedDict, total=False):

    and_: Annotated[Optional[Iterable[FilterNode]], PropertyInfo(alias="and")]

    or_: Annotated[Optional[Iterable[FilterNode]], PropertyInfo(alias="or")]

    not_: Annotated[Optional[FilterNode], PropertyInfo(alias="not")]

    field: Optional[str]

    op: Optional[str]

    value: str

class EntityFilterClause(TypedDict, total=False):

    op: Required[Literal["is", "not_is", "in", "not_in", "contains", "not_contains", "matches", "contains_case_insensitive", "not_contains_case_insensitive"]]

    value: Required[Union[str, SequenceNotStr[str]]]

