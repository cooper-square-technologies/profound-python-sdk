# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["YoutubeGetChannelsParams", "Filter"]


class YoutubeGetChannelsParams(TypedDict, total=False):
    category_id: Required[str]

    start_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    end_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    filter: Optional[Filter]
    """Advanced filter tree. Prompt-level dimensions are `model`, `topic`, `region`, `prompt`, `persona`, `tag`, `analysis_type`. `channel` covers both channel cases: `in` with a list of handles selects exactly those channels, resolving each handle to its channel so a renamed channel is never returned in pieces; `contains` matches a channel's title or handle by name. Combine with `and`/`or`/`not` up to 3 deep. An exact `channel` selection must be its own `and` clause, and a `channel` leaf cannot share an `or` or `not` with a prompt-level leaf, because those compile at different stages of the query. `domain` and `page` are rejected rather than approximated: every row here is one domain, and `page` is not a video id."""

    limit: Optional[int]
    """Page size; default 10, max 50."""

    cursor: Optional[str]

    source_types: Optional[List[Literal["video", "short", "channel", "playlist", "other"]]]
    """Limit results to YouTube source types: `video`, `short`, `channel`, `playlist`, or `other`. Omit to include `video`, `short`, `channel`, and `playlist`; `other` is excluded because those citations have no channel. Requests containing `other` are rejected."""

    group_by: List[Literal["channel", "video_category", "model", "source_type"]]
    """What each row represents. Empty or `["channel"]` ranks channels; `["video_category"]` ranks content categories; `["source_type"]` ranks source types; `["channel", "video_category"]`, `["channel", "source_type"]` and `["channel", "model"]` return cross-tabs — a row per channel per category, or per answer engine. `limit` counts leading channels in every case, so ten channels across nine engines is ten channels and ninety rows."""

    interval: Optional[Literal["day", "week", "month"]]
    """Return a time series instead of window totals: one row per entity per period, each carrying `date`. `citation_share` is then relative to that period, so the series is comparable across periods. Omit for window totals."""


_FilterReservedKeywords = TypedDict(
    "_FilterReservedKeywords",
    {
        "and": Optional[Iterable["Filter"]],
        "or": Optional[Iterable["Filter"]],
        "not": Optional["Filter"],
    },
    total=False,
)


class Filter(_FilterReservedKeywords, total=False):
    """A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group."""

    field: Optional[str]

    op: Optional[str]

    value: object
