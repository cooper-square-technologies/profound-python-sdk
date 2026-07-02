# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ClaimStreamClaimsParams", "Filter"]


class ClaimStreamClaimsParams(TypedDict, total=False):
    category_id: Required[str]

    end_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    start_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    cursor: Optional[str]

    filter: Optional[Filter]
    """A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group."""

    group_by: List[Literal["model", "region", "persona", "prompt", "topic", "tag", "theme"]]
    """Optional single dim to section the claims (e.g.

    per model). Empty → one flat claim list.
    """

    include: Optional[List[Literal["theme", "reasoning", "models", "evidence", "citation_sources"]]]
    """Optional per-claim detail fields to add to each claim (see options)."""

    limit: Optional[int]
    """Claims (or sections) per page; default 25."""

    max_results: Optional[int]
    """Stream only: cap entries returned."""


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
