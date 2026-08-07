# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["YoutubeGetVideosParams", "Filter"]


class YoutubeGetVideosParams(TypedDict, total=False):
    category_id: Required[str]

    end_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    start_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    attribution: Literal["attributed", "unattributed", "all"]
    """Choose attributed citations, unattributed citations, or all citations.

    An unattributed row has no channel: `source_type` is `other` for a search or
    feed URL that names no source, and any other type is a source we have no channel
    for.
    """

    cursor: Optional[str]

    filter: Optional[Filter]
    """A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group."""

    limit: Optional[int]
    """Page size; default 10, max 50."""

    source_types: Optional[List[Literal["video", "short", "channel", "playlist", "other"]]]
    """
    Limit results to YouTube source types: `video`, `short`, `channel`, `playlist`,
    or `other`. Omit to include `video` and `short` with the default
    `attribution='attributed'`; `unattributed` and `all` widen the default to all
    five source types. Requests containing `other` with `attribution='attributed'`
    are rejected.
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
