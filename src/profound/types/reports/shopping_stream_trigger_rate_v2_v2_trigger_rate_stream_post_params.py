# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ShoppingStreamTriggerRateV2V2TriggerRateStreamPostParams"]


class ShoppingStreamTriggerRateV2V2TriggerRateStreamPostParams(TypedDict, total=False):
    category_id: Required[str]

    start_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    end_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    group_by: List[Literal["date", "topic", "region", "persona", "prompt"]]
    """Group by `prompt`/`topic` for the per-prompt/-topic trigger rate."""

    metrics: Optional[List[Literal["total_runs", "shopping_triggered_runs", "trigger_rate_percentage"]]]

    interval: Literal["day", "week", "month"]

    filter: Optional["FilterNode"]
    """A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group."""

    limit: Optional[int]
    """Page size; default 10, max 50."""

    max_results: Optional[int]
    """Stream endpoint only: cap streamed rows."""

    cursor: Optional[str]


from ..shared_params.filter_node import FilterNode
