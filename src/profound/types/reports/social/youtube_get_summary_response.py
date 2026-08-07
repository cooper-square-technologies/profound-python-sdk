# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["YoutubeGetSummaryResponse", "Data", "Info"]


class Data(BaseModel):
    """How much of youtube.com the rollups can speak for."""

    attributed_citations: Optional[int] = None
    """
    Citations that resolve to a channel, so can appear in the channel and video
    rankings. NOT the citation_share divisor — that is total_youtube_citations, so a
    complete channel ranking's shares sum to slightly less than 1.
    """

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


class Info(BaseModel):
    """YouTube report metadata, including the effective request settings."""

    category_id: str
    """Echoed category id this report covers."""

    count: int
    """Number of rows returned in `data` for this page."""

    end_date: str
    """Echoed request end date (YYYY-MM-DD, ET)."""

    models: List[str]
    """Display names of the models the report covers."""

    start_date: str
    """Echoed request start date (YYYY-MM-DD, ET)."""

    attribution: Optional[Literal["attributed", "unattributed", "all"]] = None
    """Effective video attribution mode; absent on channels and the summary report."""

    cursor: Optional[str] = None
    """Echoed request cursor; omitted on the first page and on the summary report."""

    filter: Optional[Dict[str, object]] = None
    """Echoed normalized filter tree, or null when no filter was sent."""

    group_by: Optional[List[str]] = None
    """Echoed dimensions that define a row.

    Channel reports echo `["channel"]` when group_by is omitted; absent on reports
    that do not group.
    """

    interval: Optional[Literal["day", "week", "month"]] = None
    """
    Effective channel time-series interval, or null when the channel report covers
    the full window; absent on other reports.
    """

    limit: Optional[int] = None
    """Effective page size applied to a paged report; omitted on the summary report."""

    next_cursor: Optional[str] = None
    """Opaque cursor for the next page; null on the last page."""

    source_types: Optional[List[Literal["video", "short", "channel", "playlist", "other"]]] = None
    """
    Source types this report covers: the requested set, or the report default when
    omitted (`video` and `short` for attributed `/videos`; all types except `other`
    for `/channels`). Derived from the request, not returned rows, so a listed type
    may have no rows.
    """

    total_results: Optional[int] = None
    """Total rows matching the query before pagination (null when not computed)."""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class YoutubeGetSummaryResponse(BaseModel):
    data: Data
    """How much of youtube.com the rollups can speak for."""

    info: Info
    """YouTube report metadata, including the effective request settings."""
