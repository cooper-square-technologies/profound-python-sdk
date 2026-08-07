# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["YoutubeGetChannelsResponse", "Data", "DataModel", "Info"]


class DataModel(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class Data(BaseModel):
    """One channel (or video category) row, optionally sliced."""

    citation_share: float
    """
    Share of every YouTube citation in the window (attributed and unattributed
    alike), or the period when `interval` is set, regardless of `source_types`. An
    unnarrowed complete ranking sums to slightly less than 1 because unattributed
    citations cannot appear in channel rows; a narrowed ranking sums to its slice's
    share.
    """

    count: int
    """Citations attributed to this row."""

    name: str
    """
    Channel title when grouped by channel, or the handle when no title resolved;
    category name when grouped by `["video_category"]`; source type when grouped by
    `["source_type"]`.
    """

    rank: int
    """1-based position in the full ranked set, continuing across pages."""

    videos: int
    """Distinct videos of this channel that were cited."""

    date: Optional[str] = None
    """Period start. Present when `interval` is set."""

    handle: Optional[str] = None
    """Channel handle without the `@`, and the identifier this API exposes.

    Pass it to /videos as `channel_handle`. Null for the rare channel whose handle
    did not resolve.
    """

    model: Optional[DataModel] = None
    """An `{id, name}` reference for a grouped dimension value."""

    source_type: Optional[Literal["video", "short", "channel", "playlist", "other"]] = None
    """
    YouTube source type, present when grouped by source type, including as the
    second dimension of a cross-tab.
    """

    url: Optional[str] = None
    """Openable channel URL. Null for video-category rows."""

    video_category: Optional[str] = None
    """
    Present when grouped by video category, including as the second dimension of a
    cross-tab.
    """

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


class YoutubeGetChannelsResponse(BaseModel):
    data: List[Data]

    info: Info
    """YouTube report metadata, including the effective request settings."""
