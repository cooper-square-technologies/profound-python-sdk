# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["YoutubeGetVideosResponse", "Data"]


class Data(BaseModel):
    citation_share: float
    """Share of attributed YouTube citations in the window."""

    count: int
    """Citations attributed to this video."""

    rank: int
    """1-based position in the full ranked set, continuing across pages."""

    source_type: Literal["video", "short", "channel", "playlist", "other"]
    """YouTube source type: `video`, `short`, `channel`, `playlist` or `other`."""

    video_id: str
    """YouTube video id, as in the watch URL."""

    channel_handle: Optional[str] = None
    """Handle of the publishing channel; select it with a `channel` filter of `in`."""

    channel_title: Optional[str] = None
    """Publishing channel title, or null when unknown."""

    channel_url: Optional[str] = None
    """Openable URL for the publishing channel."""

    duration_seconds: Optional[int] = None
    """Length, or null when unknown."""

    published_at: Optional[str] = None
    """Upload date, or null when unknown."""

    title: Optional[str] = None
    """Resolved title, or null when unavailable."""

    url: Optional[str] = None
    """Openable video URL."""

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


class YoutubeGetVideosResponse(BaseModel):
    data: List[Data]

    info: Dict[str, object]
