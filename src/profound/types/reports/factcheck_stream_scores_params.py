# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["FactcheckStreamScoresParams", "Filter"]


class FactcheckStreamScoresParams(TypedDict, total=False):
    category_id: Required[str]

    start_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    end_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    group_by: List[Literal["date", "model", "region", "persona", "prompt", "topic", "tag", "citation", "theme"]]
    """Up to two dimensions to slice by; empty returns the headline score. `citation` must be alone."""

    filter: Optional[Filter]
    """Scope which responses count (see Filtering)."""

    limit: Optional[int]
    """Rows per page; default 100."""

    max_results: Optional[int]
    """Stream only: cap rows returned."""

    cursor: Optional[str]


_FilterReservedKeywords = TypedDict(
    "_FilterReservedKeywords",
    {
        "and": Optional[Iterable["Filter"]],
        "or": Optional[Iterable["Filter"]],
        "not": Optional["Filter"],
    },
    total=False,
)


class Filter(_FilterReservedKeywords, total=False):
    """A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group."""

    field: Optional[str]

    op: Optional[str]

    value: object
