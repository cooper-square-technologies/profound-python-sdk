# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional, Union
from datetime import datetime
from typing_extensions import Annotated, Literal, Required, TypedDict
from ..._types import SequenceNotStr
from ..region_id_filter import RegionIdFilter
from ..model_id_filter import ModelIdFilter
from ..topic_id_filter import TopicIdFilter
from ..tag_id_filter import TagIdFilter
from ..prompt_id_filter import PromptIdFilter
from ..persona_id_filter import PersonaIdFilter
from .brand_name_filter import BrandNameFilter
from .merchant_name_filter import MerchantNameFilter
from .product_name_filter import ProductNameFilter
from ..pagination import Pagination
from ..._utils import PropertyInfo

__all__ = ["ShoppingItemVisibilityParams", "ProfoundShoppingApiAssetNameFilter"]


class ShoppingItemVisibilityParams(TypedDict, total=False):

    category_id: Required[str]

    start_date: Required[Union[str, datetime]]
    """Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp."""

    end_date: Required[Union[str, datetime]]
    """End date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp."""

    comparison_start_date: Optional[Union[str, datetime]]

    comparison_end_date: Optional[Union[str, datetime]]

    date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"]

    filters: Iterable[Annotated[Union[RegionIdFilter, ModelIdFilter, TopicIdFilter, TagIdFilter, PromptIdFilter, PersonaIdFilter, BrandNameFilter, MerchantNameFilter, ProductNameFilter, ProfoundShoppingApiAssetNameFilter], PropertyInfo(discriminator="field")]]

    order_by: Dict[str, Literal["asc", "desc"]]

    pagination: Optional[Pagination]

    include_count: bool

    tag_filter_type: Literal["any", "all"]

    include_no_tag: bool

    exclude_topic_ids: bool

    dimensions: Iterable[Literal["period", "product_name", "brand_name", "date", "topic_id", "prompt_id", "prompt", "product_url", "product_image_urls", "product_price"]]

    metrics: Iterable[Literal["visibility_score", "share_of_voice", "average_position", "visibility_rank", "position1_percentage", "position2_percentage", "position3_percentage", "position_above3_percentage", "product_rating", "product_num_reviews", "total_count"]]

    owned_asset_names: SequenceNotStr[str]

    include_items: SequenceNotStr[str]

    search_item: Optional[str]

    merchant_filter_type: Literal["any", "all"]

    include_competitors: bool

    target_product: Optional[str]

    competitor_limit: int

    include_position_frequency: bool


class ProfoundShoppingApiAssetNameFilter(TypedDict, total=False):

    field: Required[Literal["asset_name"]]

    operator: Required[Literal["is", "not_is", "in", "not_in", "contains", "not_contains", "matches", "contains_case_insensitive", "not_contains_case_insensitive"]]

    value: Required[Union[str, SequenceNotStr[str]]]

