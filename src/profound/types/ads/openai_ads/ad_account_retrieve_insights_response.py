# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["AdAccountRetrieveInsightsResponse", "Data"]


class Data(BaseModel):
    """One insights row; the entity it describes follows `aggregation_level`.

    Time bounds are present when a `time_granularity` is requested (one row per
    time bucket); the entity id/name fields (`campaign_*`, `ad_group_*`, `ad_*`)
    are present when rows are broken down by that entity.
    """

    id: str
    """Row ID."""

    ad_group_id: Optional[str] = None
    """Ad group ID for ad_group-level rows."""

    ad_group_name: Optional[str] = None
    """Ad group name for ad_group-level rows."""

    ad_id: Optional[str] = None
    """Ad ID for ad-level rows."""

    ad_name: Optional[str] = None
    """Ad name for ad-level rows."""

    campaign_id: Optional[str] = None
    """Campaign ID for campaign-level rows."""

    campaign_name: Optional[str] = None
    """Campaign name for campaign-level rows."""

    clicks: Optional[int] = None
    """Clicks."""

    cpc: Optional[float] = None
    """Cost per click."""

    cpm: Optional[float] = None
    """Cost per thousand impressions."""

    ctr: Optional[float] = None
    """Click-through rate."""

    end_time: Optional[int] = None
    """Bucket end (unix seconds)."""

    impressions: Optional[int] = None
    """Impressions."""

    readable_time: Optional[str] = None
    """Human-readable time bucket."""

    spend: Optional[float] = None
    """Spend in the ad account's currency units."""

    start_time: Optional[int] = None
    """Bucket start (unix seconds)."""

    timezone: Optional[str] = None
    """Timezone of the time bucket."""


class AdAccountRetrieveInsightsResponse(BaseModel):
    """Cursor-paginated insights, mirroring the OpenAI Ads insights envelope."""

    data: List[Data]
    """Insight rows."""

    count: Optional[int] = None
    """Total row count, when reported upstream."""

    first_id: Optional[str] = None
    """ID of the first item; pass as `before` to page back."""

    has_more: Optional[bool] = None
    """Whether more items are available."""

    last_id: Optional[str] = None
    """ID of the last item; pass as `after` to page forward."""
