# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["YoutubeGetChannelsParams", "Filter"]


class YoutubeGetChannelsParams(TypedDict, total=False):
    category_id: Required[str]

    end_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    start_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    cursor: Optional[str]

    filter: Optional[Filter]
    """A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group."""

    group_by: List[Literal["channel", "video_category", "model", "source_type"]]
    """What each row represents.

    Empty or `["channel"]` ranks channels; `["video_category"]` ranks content
    categories; `["source_type"]` ranks source types;
    `["channel", "video_category"]`, `["channel", "source_type"]` and
    `["channel", "model"]` return cross-tabs — a row per channel per category, or
    per answer engine. `limit` counts channels in every case, so ten channels across
    nine engines is ten channels and ninety rows.
    """

    interval: Optional[Literal["day", "week", "month"]]
    """
    Return a time series instead of window totals: one row per entity per period,
    each carrying `date`. `citation_share` is then relative to that period, so the
    series is comparable across periods. Omit for window totals.
    """

    limit: Optional[int]
    """Page size; default 10, max 50."""

    source_types: Optional[List[Literal["video", "short", "channel", "playlist", "other"]]]
    """
    Limit results to YouTube source types: `video`, `short`, `channel`, `playlist`,
    or `other`. Omit to include every source type.
    """


_FilterReservedKeywords = TypedDict(
    "_FilterReservedKeywords",
    {
        "and": Optional[Iterable[object]],
        "not": object,
        "or": Optional[Iterable[object]],
    },
    total=False,
)


class Filter(_FilterReservedKeywords, total=False):
    """A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group."""

    field: Optional[str]

    op: Optional[str]

    value: object
