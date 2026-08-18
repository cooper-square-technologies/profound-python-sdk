# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional, Union
from typing_extensions import Literal, Required, TypedDict
from ..._types import SequenceNotStr

__all__ = ["ShoppingQueryBrandsV2V2BrandsPostParams"]


class ShoppingQueryBrandsV2V2BrandsPostParams(TypedDict, total=False):
    category_id: Required[str]

    start_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    end_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    group_by: List[Literal["date", "topic", "region", "prompt"]]

    metrics: Optional[List[Literal["visibility_score", "average_position", "visibility_rank"]]]

    interval: Literal["day", "week", "month"]

    scope: Literal["owned", "all"]

    assets: Optional[Union[str, SequenceNotStr[str]]]
    """Restrict to these asset names (a name or list). Overrides `scope`."""

    filter: Optional["FilterNode"]
    """A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group."""

    limit: Optional[int]
    """Page size for scope=all; default 10, max 50."""

    max_results: Optional[int]
    """Stream endpoint only: cap the number of streamed rows (default: all)."""

    cursor: Optional[str]


from ..shared_params.filter_node import FilterNode
