# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["YoutubeGetVideosResponse", "Data", "Info"]


class Data(BaseModel):
    citation_share: float
    """
    Share of every YouTube citation in the window (attributed and unattributed
    alike), regardless of `source_types`. Shares sum to at most 1, reaching about 1
    only with `attribution="all"` and no `source_types` filter; a narrowed ranking
    sums to its slice's share.
    """

    count: int
    """Citations attributed to this video."""

    rank: int
    """1-based position in the full ranked set, continuing across pages."""

    source_type: Literal["video", "short", "channel", "playlist", "other"]
    """YouTube source type: `video`, `short`, `channel`, `playlist` or `other`."""

    video_id: str
    """YouTube video id, as in the watch URL."""

    channel_handle: Optional[str] = None
    """Handle of the publishing channel; select it with a `channel` filter of `in`.

    Null when unknown.
    """

    channel_title: Optional[str] = None
    """Publishing channel title, or null when unknown."""

    channel_url: Optional[str] = None
    """Openable URL for the publishing channel, or null when unknown."""

    duration_seconds: Optional[int] = None
    """Length in seconds, or null when unknown."""

    published_at: Optional[str] = None
    """Upload date, or null when unknown."""

    title: Optional[str] = None
    """Resolved title, or null when unavailable."""

    url: Optional[str] = None
    """Openable video URL, or null when unavailable."""

    video_category: Optional[str] = None
    """YouTube content category, or null when unknown."""

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


class YoutubeGetVideosResponse(BaseModel):
    data: List[Data]

    info: Info
    """YouTube report metadata, including the effective request settings."""
