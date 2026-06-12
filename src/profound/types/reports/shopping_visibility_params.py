# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from ..prompt_id_filter_param import PromptIDFilterParam
from .brand_name_filter_param import BrandNameFilterParam
from ..shared_params.pagination import Pagination
from .product_name_filter_param import ProductNameFilterParam
from .merchant_name_filter_param import MerchantNameFilterParam
from ..shared_params.tag_id_filter import TagIDFilter
from ..shared_params.model_id_filter import ModelIDFilter
from ..shared_params.topic_id_filter import TopicIDFilter
from ..shared_params.region_id_filter import RegionIDFilter
from ..shared_params.persona_id_filter import PersonaIDFilter

__all__ = ["ShoppingVisibilityParams", "Filter", "FilterProfoundShoppingAPIAssetNameFilter"]


class ShoppingVisibilityParams(TypedDict, total=False):
    category_id: Required[str]

    end_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """End date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp."""

    start_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp."""

    comparison_end_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    comparison_start_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"]

    dimensions: List[
        Literal["period", "asset_name", "date", "model_id", "topic_id", "region_id", "prompt_id", "prompt"]
    ]

    exclude_topic_ids: bool

    filters: Iterable[Filter]

    include_asset: Optional[str]

    include_asset_only: bool

    include_assets_only: SequenceNotStr[str]

    include_count: bool

    include_no_tag: bool

    include_position_frequency: bool

    metrics: List[
        Literal[
            "visibility_score",
            "share_of_voice",
            "average_position",
            "visibility_rank",
            "average_position_rank",
            "position1_percentage",
            "position2_percentage",
            "position3_percentage",
            "position_above3_percentage",
            "total_count",
        ]
    ]

    order_by: Dict[str, Literal["asc", "desc"]]

    owned_asset_names: SequenceNotStr[str]

    pagination: Optional[Pagination]
    """Offset-based pagination parameters."""

    rank_by: Literal["visibility_score", "average_position"]

    search_asset: Optional[str]

    tag_filter_type: Literal["any", "all"]


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


Filter: TypeAlias = Union[
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
]
