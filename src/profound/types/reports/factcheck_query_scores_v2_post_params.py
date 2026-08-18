# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["FactcheckQueryScoresV2PostParams"]


class FactcheckQueryScoresV2PostParams(TypedDict, total=False):
    category_id: Required[str]

    start_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    end_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    group_by: List[Literal["date", "model", "region", "persona", "prompt", "topic", "tag", "citation", "theme"]]
    """Up to two dimensions to slice by; empty returns the headline score. `citation` must be alone."""

    filter: Optional["FilterNode"]
    """Scope which responses count (see Filtering)."""

    limit: Optional[int]
    """Rows per page; default 100."""

    max_results: Optional[int]
    """Stream only: cap rows returned."""

    cursor: Optional[str]


from ..shared_params.filter_node import FilterNode
