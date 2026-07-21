# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ReportStreamCitationsV2Params", "Filter"]


class ReportStreamCitationsV2Params(TypedDict, total=False):
    category_id: Required[str]

    end_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    start_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    cursor: Optional[str]

    entity: Literal["domain", "page", "citation_category"]
    """What each row represents: `domain` (default), `page`, or `citation_category`.

    Legacy: `group_by: ["page"]` (with `entity` omitted) is still accepted and is
    equivalent to `entity: "page"`. `citation_category` uses the dashboard split
    view: a citation counts under both its page-level and domain-level category, so
    category shares can sum to more than 100%.
    """

    filter: Optional[Filter]
    """A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group."""

    group_by: List[Literal["page", "date", "model", "topic", "region", "persona", "prompt"]]

    interval: Literal["day", "week", "month"]

    limit: Optional[int]
    """Page size; default 10, max 50."""

    max_results: Optional[int]
    """Stream endpoint only: cap the number of streamed rows (default: all)."""

    metrics: Optional[List[Literal["count", "citation_share", "rank", "first_cited_at"]]]

    scope: Literal["all", "owned"]
    """`all` (every cited domain) or `owned` (only your owned domains).

    Applies to `entity=domain`.
    """


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
