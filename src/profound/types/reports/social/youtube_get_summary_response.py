# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, List, Optional, TYPE_CHECKING
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["YoutubeGetSummaryResponse", "Info", "Data"]


class Data(BaseModel):
    total_youtube_citations: Optional[int] = None
    """Every YouTube citation in the window."""

    attributed_citations: Optional[int] = None
    """Citations that resolve to a channel, so can appear in the channel and video rankings. NOT the citation_share divisor — that is total_youtube_citations, so a complete channel ranking's shares sum to slightly less than 1."""

    unattributed_citations: Optional[int] = None
    """Citations with no channel: search and feed URLs, deleted sources, or not yet resolved."""

    citations_video: Optional[int] = None
    """Citations pointing at long-form videos."""

    citations_short: Optional[int] = None
    """Citations pointing at Shorts."""

    citations_channel: Optional[int] = None
    """Citations pointing at a channel page rather than a video."""

    citations_playlist: Optional[int] = None
    """Citations pointing at a playlist."""

    citations_other: Optional[int] = None
    """Search, feed, and homepage URLs. Never attributable."""

    distinct_channels: Optional[int] = None
    """Distinct channels cited."""

    distinct_videos: Optional[int] = None
    """Distinct long-form videos cited."""

    distinct_shorts: Optional[int] = None
    """Distinct Shorts cited."""


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
    """All five YouTube source types; this endpoint has no source_types request field and cannot be narrowed."""

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
    info: Info
    """Summary report metadata."""

    data: Data
    """How much of youtube.com the rollups can speak for."""
