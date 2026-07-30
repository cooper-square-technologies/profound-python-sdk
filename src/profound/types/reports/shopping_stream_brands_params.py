# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ShoppingStreamBrandsParams", "Filter"]


class ShoppingStreamBrandsParams(TypedDict, total=False):
    category_id: Required[str]

    end_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    start_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    assets: Union[str, SequenceNotStr[str], None]
    """Restrict to these asset names (a name or list). Overrides `scope`."""

    cursor: Optional[str]

    filter: Optional[Filter]
    """A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group."""

    group_by: List[Literal["date", "topic", "region", "prompt"]]

    interval: Literal["day", "week", "month"]

    limit: Optional[int]
    """Page size for scope=all; default 10, max 50."""

    max_results: Optional[int]
    """Stream endpoint only: cap the number of streamed rows (default: all)."""

    metrics: Optional[List[Literal["visibility_score", "average_position", "visibility_rank"]]]

    scope: Literal["owned", "all"]


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
