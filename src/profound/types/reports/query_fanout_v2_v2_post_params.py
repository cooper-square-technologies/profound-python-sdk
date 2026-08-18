# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["QueryFanoutV2V2PostParams", "Sort"]


class QueryFanoutV2V2PostParams(TypedDict, total=False):
    category_id: Required[str]

    start_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    end_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    group_by: List[Literal["date", "model", "region", "prompt", "query"]]

    metrics: Optional[List[Literal["fanouts_per_execution", "total_fanouts", "share", "query_variations"]]]

    interval: Literal["day", "week", "month"]

    filter: Optional["FilterNode"]
    """A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group."""

    sort: Optional[Sort]

    limit: Optional[int]
    """Page size; default 10, max 50."""

    max_results: Optional[int]
    """Stream endpoint only: cap the number of streamed rows (default: all)."""

    cursor: Optional[str]


class Sort(TypedDict, total=False):
    field: Required[str]

    dir: Literal["asc", "desc"]


from ..shared_params.filter_node import FilterNode
