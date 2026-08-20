# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["YoutubeGetVideosParams"]


class YoutubeGetVideosParams(TypedDict, total=False):
    category_id: Required[str]

    start_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    end_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    filter: Optional["FilterNode"]
    """Advanced filter tree. Prompt-level dimensions are `model`, `topic`, `region`, `prompt`, `persona`, `tag`, `analysis_type`. `channel` covers both channel cases: `in` with a list of handles selects exactly those channels, resolving each handle to its channel so a renamed channel is never returned in pieces; `contains` matches a channel's title or handle by name. Combine with `and`/`or`/`not` up to 3 deep. An exact `channel` selection must be its own `and` clause, and a `channel` leaf cannot share an `or` or `not` with a prompt-level leaf, because those compile at different stages of the query. `domain` and `page` are rejected rather than approximated: every row here is one domain, and `page` is not a video id."""

    limit: Optional[int]
    """Page size; default 10, max 50."""

    cursor: Optional[str]

    source_types: Optional[List[Literal["video", "short", "channel", "playlist", "other"]]]
    """Limit results to YouTube source types: `video`, `short`, `channel`, `playlist`, or `other`. Omit to include `video` and `short` with the default `attribution='attributed'`; `unattributed` and `all` widen the default to all five source types. Requests containing `other` with `attribution='attributed'` are rejected."""

    attribution: Literal["attributed", "unattributed", "all"]
    """Choose attributed citations, unattributed citations, or all citations. An unattributed row has no channel: `source_type` is `other` for a search or feed URL that names no source, and any other type is a source we have no channel for."""


from ...shared_params.filter_node import FilterNode
