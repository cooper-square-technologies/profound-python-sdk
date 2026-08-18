# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["FactcheckStreamClaimsV2ClaimsStreamPostParams"]


class FactcheckStreamClaimsV2ClaimsStreamPostParams(TypedDict, total=False):
    category_id: Required[str]

    start_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    end_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    group_by: List[Literal["model", "region", "persona", "prompt", "topic", "tag", "theme"]]
    """Optional single dim to section the claims (e.g. per model). Empty → one flat claim list."""

    filter: Optional["FilterNode"]
    """Scope which responses count (see Filtering)."""

    include: Optional[List[Literal["theme", "reasoning", "models", "evidence", "citation_sources"]]]
    """Optional per-claim detail fields to add to each claim (see options)."""

    limit: Optional[int]
    """Claims (or sections) per page; default 25."""

    max_results: Optional[int]
    """Stream only: cap entries returned."""

    cursor: Optional[str]


from ..shared_params.filter_node import FilterNode
