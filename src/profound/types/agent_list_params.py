# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["AgentListParams"]


class AgentListParams(TypedDict, total=False):
    limit: int

    next_cursor: Optional[str]

    statuses: Optional[List[Literal["published", "draft"]]]
    """Optional status filter.

    Use `published` to list agents that have a live published version, or `draft` to
    list agents that have not been published yet. Defaults to `published`.
    """
