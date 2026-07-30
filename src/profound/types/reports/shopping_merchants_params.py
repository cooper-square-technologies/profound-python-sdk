# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ShoppingMerchantsParams", "Filter"]


class ShoppingMerchantsParams(TypedDict, total=False):
    category_id: Required[str]

    end_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    start_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    cursor: Optional[str]

    filter: Optional[Filter]
    """A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group."""

    group_by: List[Literal["date", "brand", "product"]]
    """
    `[]` = distribution; `[brand]` = brand share within each merchant; `[product]` =
    top products per merchant. `date` (distribution only) adds a time series.
    """

    interval: Literal["day", "week", "month"]

    limit: Optional[int]
    """Page size; default 10, max 50."""

    max_results: Optional[int]
    """Stream endpoint only: cap streamed rows."""

    metrics: Optional[
        List[
            Literal[
                "merchant_share",
                "merchant_share_rank",
                "merchant_visibility",
                "merchant_visibility_rank",
                "visibility_rank",
                "brand_share",
                "product_visibility",
                "product_rank",
            ]
        ]
    ]
    """Defaults to the chosen view's metrics; must be valid for that view."""


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
