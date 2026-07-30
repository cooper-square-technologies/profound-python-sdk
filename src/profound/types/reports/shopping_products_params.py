# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ShoppingProductsParams", "Filter"]


class ShoppingProductsParams(TypedDict, total=False):
    category_id: Required[str]

    end_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    start_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    competitor_limit: int
    """Competitors returned when `target_product` is set."""

    cursor: Optional[str]

    filter: Optional[Filter]
    """A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group."""

    group_by: List[Literal["date", "topic", "prompt"]]

    include_merchants: bool
    """Include per-product merchant offers (names, prices, urls, images)."""

    interval: Literal["day", "week", "month"]

    limit: Optional[int]
    """Page size; default 10, max 50."""

    max_results: Optional[int]
    """Stream endpoint only: cap streamed rows."""

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

    target_product: Optional[str]
    """Return this product plus its top competitors (item view only)."""


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
