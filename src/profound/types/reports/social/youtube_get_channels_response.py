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
    """
    Leading channel's 1-based position in the full ranked set, continuing across
    pages; repeated across that channel's cross-tab rows rather than numbering rows.
    """

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
    Populated for a secondary video-category slice; with group_by
    `["video_category"]`, the category is returned in `name` instead. An unresolved
    category is returned as an empty string.
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
    """Channel report metadata, including effective paging and grouping settings."""

    category_id: str
    """Echoed category id this report covers."""

    count: int
    """Number of rows returned in `data` for this page."""

    end_date: str
    """Echoed request end date (YYYY-MM-DD, ET)."""

    group_by: List[str]
    """Echoed dimensions that define a row.

    Channel reports echo `["channel"]` when group_by is omitted.
    """

    limit: int
    """Effective page size in leading channels, not returned rows."""

    models: List[str]
    """Display names of the models the report covers."""

    source_types: List[Literal["video", "short", "channel", "playlist", "other"]]
    """Source types this report covers.

    Derived from the request, not returned rows, so a listed type may have no rows.
    """

    start_date: str
    """Echoed request start date (YYYY-MM-DD, ET)."""

    total_results: int
    """
    Distinct leading channels matching the window; this can differ from the number
    of rows returned.
    """

    cursor: Optional[str] = None
    """Echoed request cursor; omitted on the first page."""

    filter: Optional[Dict[str, object]] = None
    """Echoed normalized filter tree, or null when no filter was sent."""

    interval: Optional[Literal["day", "week", "month"]] = None
    """
    Effective channel time-series interval, or null when the channel report covers
    the full window.
    """

    next_cursor: Optional[str] = None
    """Opaque cursor for the next page; null on the last page."""

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
    """Channel report metadata, including effective paging and grouping settings."""
