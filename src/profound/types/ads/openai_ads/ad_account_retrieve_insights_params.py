# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from ...._types import SequenceNotStr

__all__ = ["AdAccountRetrieveInsightsParams"]


class AdAccountRetrieveInsightsParams(TypedDict, total=False):
    after: Optional[str]
    """Return items after this ID (forward pagination)."""

    aggregation_level: Optional[Literal["ad_account", "campaign", "ad_group", "ad"]]
    """Row entity for the insights breakdown. `campaign` returns one row per campaign."""

    before: Optional[str]
    """Return items before this ID (backward pagination)."""

    limit: Optional[int]
    """Maximum rows to return."""

    organization_id: Optional[str]
    """Organization scope for API keys that can access multiple organizations."""

    time_granularity: Optional[Literal["hourly", "daily", "monthly", "none"]]
    """
    Time bucket for the rows; `none` or omitted returns totals over the whole range.
    """

    time_ranges: Optional[SequenceNotStr[str]]
    """Time ranges as JSON objects, e.g.

    `{"type": "date_range", "since": "2026-07-01", "until": "2026-07-18"}`.
    """
