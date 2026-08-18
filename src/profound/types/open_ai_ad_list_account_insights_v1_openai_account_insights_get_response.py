# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["OpenAIAdListAccountInsightsV1OpenAIAccountInsightsGetResponse", "Data"]


class Data(BaseModel):
    id: str
    """Row ID."""

    start_time: Optional[int] = None
    """Bucket start (unix seconds)."""

    end_time: Optional[int] = None
    """Bucket end (unix seconds)."""

    readable_time: Optional[str] = None
    """Human-readable time bucket."""

    timezone: Optional[str] = None
    """Timezone of the time bucket."""

    campaign_id: Optional[str] = None
    """Campaign ID for campaign-level rows."""

    campaign_name: Optional[str] = None
    """Campaign name for campaign-level rows."""

    ad_group_id: Optional[str] = None
    """Ad group ID for ad_group-level rows."""

    ad_group_name: Optional[str] = None
    """Ad group name for ad_group-level rows."""

    ad_id: Optional[str] = None
    """Ad ID for ad-level rows."""

    ad_name: Optional[str] = None
    """Ad name for ad-level rows."""

    impressions: Optional[int] = None
    """Impressions."""

    clicks: Optional[int] = None
    """Clicks."""

    spend: Optional[float] = None
    """Spend in the ad account's currency units."""

    ctr: Optional[float] = None
    """Click-through rate."""

    cpc: Optional[float] = None
    """Cost per click."""

    cpm: Optional[float] = None
    """Cost per thousand impressions."""


class OpenAIAdListAccountInsightsV1OpenAIAccountInsightsGetResponse(BaseModel):
    data: List[Data]
    """Insight rows."""

    count: Optional[int] = None
    """Total row count, when reported upstream."""

    first_id: Optional[str] = None
    """ID of the first item; pass as `before` to page back."""

    last_id: Optional[str] = None
    """ID of the last item; pass as `after` to page forward."""

    has_more: Optional[bool] = None
    """Whether more items are available."""
