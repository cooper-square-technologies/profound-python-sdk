# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CitationsV2Query", "FilterNode"]


class FilterNode(BaseModel):

    and_: Optional[List[FilterNode]] = FieldInfo(alias="and", default=None)

    or_: Optional[List[FilterNode]] = FieldInfo(alias="or", default=None)

    not_: Optional[FilterNode] = FieldInfo(alias="not", default=None)

    field: Optional[str] = None

    op: Optional[str] = None

    value: Optional[str] = None



class CitationsV2Query(BaseModel):

    category_id: str

    start_date: str
    """YYYY-MM-DD, ET, inclusive"""

    end_date: str
    """YYYY-MM-DD, ET, inclusive"""

    group_by: Optional[List[Literal["page", "date", "model", "topic", "region", "persona", "prompt"]]] = None

    metrics: Optional[List[Literal["count", "citation_share", "rank", "first_cited_at"]]] = None

    interval: Optional[Literal["day", "week", "month"]] = None

    scope: Optional[Literal["all", "owned"]] = None
    """`all` (every cited domain) or `owned` (only your owned domains, for easy client-side totals)."""

    filter: Optional[FilterNode] = None

    limit: Optional[int] = None
    """Page size; default 10, max 50."""

    max_results: Optional[int] = None
    """Stream endpoint only: cap the number of streamed rows (default: all)."""

    cursor: Optional[str] = None
