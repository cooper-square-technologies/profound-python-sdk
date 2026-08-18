# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["AgentListV1GetParams"]


class AgentListV1GetParams(TypedDict, total=False):
    statuses: Optional[List[Literal["published", "draft"]]]
    """Optional status filter. Use `published` to list agents that have a live published version, or `draft` to list agents that have not been published yet. Defaults to `published`."""

    limit: int

    next_cursor: Optional[str]
