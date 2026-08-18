# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, List, Optional, TYPE_CHECKING
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SocialQueryYoutubeVideosV2YoutubeVideosPostResponse", "Info", "Data"]


class Data(BaseModel):
    video_id: str
    """YouTube video id, as in the watch URL."""

    source_type: Literal["video", "short", "channel", "playlist", "other"]
    """YouTube source type: `video`, `short`, `channel`, `playlist` or `other`."""

    title: Optional[str] = None
    """Resolved title, or null when unavailable."""

    channel_title: Optional[str] = None
    """Publishing channel title, or null when unknown."""

    channel_handle: Optional[str] = None
    """Handle of the publishing channel; select it with a `channel` filter of `in`. Null when unknown."""

    url: Optional[str] = None
    """Openable video URL, or null when unavailable."""

    channel_url: Optional[str] = None
    """Openable URL for the publishing channel, or null when unknown."""

    rank: int
    """1-based position in the full ranked set, continuing across pages."""

    published_at: Optional[str] = None
    """Upload date, or null when unknown."""

    duration_seconds: Optional[int] = None
    """Length in seconds, or null when unknown."""

    video_category: Optional[str] = None
    """YouTube content category, or null when unknown."""

    count: int
    """Citations attributed to this video."""

    citation_share: float
    """Share of every YouTube citation in the window (attributed and unattributed alike), regardless of `source_types`. Shares sum to at most 1, reaching about 1 only with `attribution="all"` and no `source_types` filter; a narrowed ranking sums to its slice's share."""

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
    total_results: Optional[int] = None
    """Total rows matching the query before pagination (null when not computed)."""

    count: int
    """Number of rows returned in `data` for this page."""

    next_cursor: Optional[str] = None
    """Opaque cursor for the next page; null on the last page."""

    models: List[str]
    """Display names of the models the report covers."""

    start_date: str
    """Echoed request start date (YYYY-MM-DD, ET)."""

    end_date: str
    """Echoed request end date (YYYY-MM-DD, ET)."""

    filter: Optional[Dict[str, object]] = None
    """Echoed normalized filter tree, or null when no filter was sent."""

    category_id: str
    """Echoed category id this report covers."""

    source_types: List[Literal["video", "short", "channel", "playlist", "other"]]
    """Source types this report covers. Derived from the request, not returned rows, so a listed type may have no rows."""

    cursor: Optional[str] = None
    """Echoed request cursor; omitted on the first page."""

    limit: int
    """Effective page size applied to this paged report."""

    attribution: Literal["attributed", "unattributed", "all"]
    """Effective video attribution mode."""

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


class SocialQueryYoutubeVideosV2YoutubeVideosPostResponse(BaseModel):
    info: Info
    """Video report metadata, including effective paging and attribution settings."""

    data: List[Data]
