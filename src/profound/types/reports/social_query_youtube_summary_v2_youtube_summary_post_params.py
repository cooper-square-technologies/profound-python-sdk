# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SocialQueryYoutubeSummaryV2YoutubeSummaryPostParams"]


class SocialQueryYoutubeSummaryV2YoutubeSummaryPostParams(TypedDict, total=False):
    category_id: Required[str]

    start_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    end_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    filter: Optional["FilterNode"]
    """Advanced filter tree. Prompt-level dimensions are `model`, `topic`, `region`, `prompt`, `persona`, `tag`, `analysis_type`. `channel` covers both channel cases: `in` with a list of handles selects exactly those channels, resolving each handle to its channel so a renamed channel is never returned in pieces; `contains` matches a channel's title or handle by name. Combine with `and`/`or`/`not` up to 3 deep. An exact `channel` selection must be its own `and` clause, and a `channel` leaf cannot share an `or` or `not` with a prompt-level leaf, because those compile at different stages of the query. `domain` and `page` are rejected rather than approximated: every row here is one domain, and `page` is not a video id."""


from ..shared_params.filter_node import FilterNode
