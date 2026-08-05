# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ...._models import BaseModel

__all__ = ["YoutubeGetSummaryResponse", "Data"]


class Data(BaseModel):
    """How much of youtube.com the rollups can speak for."""

    attributed_citations: Optional[int] = None
    """Citations that resolve to a channel; the ranking denominator."""

    citations_channel: Optional[int] = None
    """Citations pointing at a channel page rather than a video."""

    citations_other: Optional[int] = None
    """Search, feed, and homepage URLs. Never attributable."""

    citations_playlist: Optional[int] = None
    """Citations pointing at a playlist."""

    citations_short: Optional[int] = None
    """Citations pointing at Shorts."""

    citations_video: Optional[int] = None
    """Citations pointing at long-form videos."""

    distinct_channels: Optional[int] = None
    """Distinct channels cited."""

    distinct_shorts: Optional[int] = None
    """Distinct Shorts cited."""

    distinct_videos: Optional[int] = None
    """Distinct long-form videos cited."""

    total_youtube_citations: Optional[int] = None
    """Every YouTube citation in the window."""

    unattributed_citations: Optional[int] = None
    """
    Citations with no channel: search and feed URLs, deleted sources, or not yet
    resolved.
    """


class YoutubeGetSummaryResponse(BaseModel):
    data: Data
    """How much of youtube.com the rollups can speak for."""

    info: Dict[str, object]
