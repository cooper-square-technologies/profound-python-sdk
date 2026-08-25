# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ReportQueryCitationsParams", "Filter"]


class ReportQueryCitationsParams(TypedDict, total=False):
    category_id: Required[str]

    start_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    end_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    entity: Literal["domain", "page", "citation_category"]
    """What each row represents: `domain` (default), `page`, or `citation_category`. Legacy: `group_by: ["page"]` (with `entity` omitted) is still accepted and is equivalent to `entity: "page"`. `citation_category` uses the dashboard split view: a citation counts under both its page-level and domain-level category, so category shares can sum to more than 100%."""

    group_by: List[Literal["page", "date", "model", "topic", "region", "persona", "prompt"]]

    metrics: Optional[List[Literal["count", "citation_share", "rank", "first_cited_at"]]]

    interval: Literal["day", "week", "month"]

    scope: Literal["all", "owned"]
    """`all` (every cited domain) or `owned` (only your owned domains). Applies to `entity=domain`."""

    filter: Optional[Filter]
    """`citation_category` filters on a cited URL's single category; `citation_tag` filters on the custom citation tags a URL carries (a URL can carry several). List the category's tags with `GET /v1/org/categories/{category_id}/citation-tags`."""

    limit: Optional[int]
    """Page size; default 10, max 50."""

    max_results: Optional[int]
    """Stream endpoint only: cap the number of streamed rows (default: all)."""

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
