# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = ["ReportStreamVisibilityV2Params", "Assets", "AssetsEntityFilterClause", "Filter", "Sort"]


class ReportStreamVisibilityV2Params(TypedDict, total=False):
    category_id: Required[str]

    end_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    start_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    assets: Optional[Assets]
    """A name (`is`), a list (`in`), or {op,value} with op `is`/`in`/`not_in`."""

    cursor: Optional[str]

    filter: Optional[Filter]
    """A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group."""

    group_by: List[Literal["date", "model", "topic", "region", "prompt", "persona"]]

    interval: Literal["day", "week", "month"]

    limit: Optional[int]
    """Page size; default 10, max 50."""

    max_results: Optional[int]
    """Stream endpoint only: cap the number of streamed rows (default: all)."""

    metrics: Optional[List[Literal["visibility_score", "share_of_voice", "average_position"]]]

    scope: Literal["owned", "all"]

    sort: Sort


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
    field: Literal["visibility_score", "share_of_voice", "average_position"]
