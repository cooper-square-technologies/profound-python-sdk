# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ClaimStreamClaimsParams", "Filter"]


class ClaimStreamClaimsParams(TypedDict, total=False):
    category_id: Required[str]

    start_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    end_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    group_by: List[Literal["model", "region", "persona", "prompt", "topic", "tag", "theme"]]
    """Optional single dim to section the claims (e.g. per model). Empty → one flat claim list."""

    filter: Optional[Filter]
    """Scope which responses count (see Filtering)."""

    include: Optional[List[Literal["theme", "reasoning", "models", "evidence", "citation_sources"]]]
    """Optional per-claim detail fields to add to each claim (see options)."""

    limit: Optional[int]
    """Claims (or sections) per page; default 25."""

    max_results: Optional[int]
    """Stream only: cap entries returned."""

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
