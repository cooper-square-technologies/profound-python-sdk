# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Annotated, Literal, Required, TypedDict
from ..._utils import PropertyInfo

__all__ = ["CitationStreamV2V2ReportsStreamPostParams", "FilterNode"]


class CitationStreamV2V2ReportsStreamPostParams(TypedDict, total=False):

    category_id: Required[str]

    start_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    end_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    group_by: Iterable[Literal["page", "date", "model", "topic", "region", "persona", "prompt"]]

    metrics: Optional[Iterable[Literal["count", "citation_share", "rank", "first_cited_at"]]]

    interval: Literal["day", "week", "month"]

    scope: Literal["all", "owned"]
    """`all` (every cited domain) or `owned` (only your owned domains, for easy client-side totals)."""

    filter: Optional[FilterNode]

    limit: Optional[int]
    """Page size; default 10, max 50."""

    max_results: Optional[int]
    """Stream endpoint only: cap the number of streamed rows (default: all)."""

    cursor: Optional[str]


class FilterNode(TypedDict, total=False):

    and_: Annotated[Optional[Iterable[FilterNode]], PropertyInfo(alias="and")]

    or_: Annotated[Optional[Iterable[FilterNode]], PropertyInfo(alias="or")]

    not_: Annotated[Optional[FilterNode], PropertyInfo(alias="not")]

    field: Optional[str]

    op: Optional[str]

    value: str

