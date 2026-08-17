# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Iterable, List, Optional, Union
from datetime import datetime
from typing_extensions import Annotated, Literal, Required, TypeAlias, TypedDict
from ..._types import SequenceNotStr

from ..._utils import PropertyInfo

from ..shared_params.region_id_filter import RegionIDFilter
from ..shared_params.model_id_filter import ModelIDFilter
from ..shared_params.topic_id_filter import TopicIDFilter
from ..shared_params.tag_id_filter import TagIDFilter
from ..prompt_id_filter_param import PromptIDFilterParam
from ..shared_params.persona_id_filter import PersonaIDFilter
from .brand_name_filter_param import BrandNameFilterParam
from .merchant_name_filter_param import MerchantNameFilterParam
from .product_name_filter_param import ProductNameFilterParam
from ..shared_params.pagination import Pagination

__all__ = ["ShoppingMerchantByItemsParams", "Filter", "FilterProfoundShoppingAPIAssetNameFilter"]


class ShoppingMerchantByItemsParams(TypedDict, total=False):
    category_id: Required[str]

    start_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp."""

    end_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """End date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp."""

    comparison_start_date: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]

    comparison_end_date: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]

    date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"]

    filters: Iterable[Filter]

    order_by: Dict[str, Literal["asc", "desc"]]

    pagination: Optional[Pagination]
    """Offset-based pagination parameters."""

    include_count: bool

    tag_filter_type: Literal["any", "all"]

    include_no_tag: bool

    exclude_topic_ids: bool

    dimensions: List[
        Literal[
            "period",
            "merchant_name",
            "product_name",
            "brand_name",
            "product_image_urls",
            "product_price",
            "merchant_prices",
            "has_instant_checkout",
            "delivery_options",
            "merchant_url",
        ]
    ]

    metrics: List[Literal["merchant_visibility", "product_visibility", "product_rank", "avg_position", "total_count"]]

    product_name: Optional[str]


class FilterProfoundShoppingAPIAssetNameFilter(TypedDict, total=False):
    field: Required[Literal["asset_name"]]

    operator: Required[
        Literal[
            "is",
            "not_is",
            "in",
            "not_in",
            "contains",
            "not_contains",
            "matches",
            "contains_case_insensitive",
            "not_contains_case_insensitive",
        ]
    ]

    value: Required[Union[str, SequenceNotStr[str]]]


Filter: TypeAlias = Annotated[
    Union[
        RegionIDFilter,
        ModelIDFilter,
        TopicIDFilter,
        TagIDFilter,
        PromptIDFilterParam,
        PersonaIDFilter,
        BrandNameFilterParam,
        MerchantNameFilterParam,
        ProductNameFilterParam,
        FilterProfoundShoppingAPIAssetNameFilter,
    ],
    PropertyInfo(discriminator="field"),
]
