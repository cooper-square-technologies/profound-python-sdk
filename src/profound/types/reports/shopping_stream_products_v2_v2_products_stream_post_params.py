# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ShoppingStreamProductsV2V2ProductsStreamPostParams"]


class ShoppingStreamProductsV2V2ProductsStreamPostParams(TypedDict, total=False):
    category_id: Required[str]

    start_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    end_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    group_by: List[Literal["date", "topic", "prompt"]]

    metrics: Optional[
        List[
            Literal[
                "visibility_score",
                "average_position",
                "visibility_rank",
                "position1_percentage",
                "position2_percentage",
                "position3_percentage",
                "position_above3_percentage",
                "product_rating",
                "product_num_reviews",
            ]
        ]
    ]

    interval: Literal["day", "week", "month"]

    include_merchants: bool
    """Include per-product merchant offers (names, prices, urls, images)."""

    target_product: Optional[str]
    """Return this product plus its top competitors (item view only)."""

    competitor_limit: int
    """Competitors returned when `target_product` is set."""

    filter: Optional["FilterNode"]
    """A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group."""

    limit: Optional[int]
    """Page size; default 10, max 50."""

    max_results: Optional[int]
    """Stream endpoint only: cap streamed rows."""

    cursor: Optional[str]


from ..shared_params.filter_node import FilterNode
