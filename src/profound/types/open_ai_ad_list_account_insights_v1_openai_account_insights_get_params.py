# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, Literal, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

__all__ = ["OpenAIAdListAccountInsightsV1OpenAIAccountInsightsGetParams"]


class OpenAIAdListAccountInsightsV1OpenAIAccountInsightsGetParams(TypedDict, total=False):
    organization_id: Optional[str]
    """Organization scope for API keys that can access multiple organizations."""

    aggregation_level: Optional[Literal["ad_account", "campaign", "ad_group", "ad"]]
    """Row entity for the insights breakdown. `campaign` returns one row per campaign."""

    time_granularity: Optional[Literal["hourly", "daily", "monthly", "none"]]
    """Time bucket for the rows; `none` or omitted returns totals over the whole range."""

    time_ranges: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="time_ranges[]")]
    """Time ranges as JSON objects, e.g. `{"type": "date_range", "since": "2026-07-01", "until": "2026-07-18"}`."""

    limit: Optional[int]
    """Maximum rows to return."""

    after: Optional[str]
    """Return items after this ID (forward pagination)."""

    before: Optional[str]
    """Return items before this ID (backward pagination)."""
