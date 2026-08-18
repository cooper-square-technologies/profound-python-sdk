# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from ..._types import SequenceNotStr

__all__ = ["VisibilityStreamV2V2StreamPostParams", "Assets", "AssetsEntityFilterClause", "Sort"]


class VisibilityStreamV2V2StreamPostParams(TypedDict, total=False):
    category_id: Required[str]

    start_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    end_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    group_by: List[Literal["date", "model", "topic", "region", "prompt", "persona"]]

    metrics: Optional[List[Literal["visibility_score", "share_of_voice", "average_position"]]]

    interval: Literal["day", "week", "month"]

    scope: Literal["owned", "all"]

    assets: Optional[Assets]
    """A name (`is`), a list (`in`), or {op,value} with op `is`/`in`/`not_in`."""

    filter: Optional["FilterNode"]
    """A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group."""

    sort: Sort

    limit: Optional[int]
    """Page size; default 10, max 50."""

    max_results: Optional[int]
    """Stream endpoint only: cap the number of streamed rows (default: all)."""

    cursor: Optional[str]


class Sort(TypedDict, total=False):
    field: Literal["visibility_score", "share_of_voice", "average_position"]


class AssetsEntityFilterClause(TypedDict, total=False):
    """Select/exclude the entity, applied outside the data `filter` tree."""

    op: Required[
        Literal[
            "is",
            "not_is",
            "in",
            "not_in",
            "contains",
            "not_contains",
            "matches",
            "contains_case_insensitive",
            "not_contains_case_insensitive",
        ]
    ]

    value: Required[Union[str, SequenceNotStr[str]]]


Assets: TypeAlias = Union[str, SequenceNotStr[str], AssetsEntityFilterClause]


from ..shared_params.filter_node import FilterNode
