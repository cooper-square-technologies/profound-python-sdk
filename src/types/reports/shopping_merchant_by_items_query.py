# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, List, Optional, Union
from datetime import datetime
from typing_extensions import Annotated, Literal
from ..._utils import PropertyInfo

from ..._models import BaseModel
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

__all__ = ["ShoppingMerchantByItemsQuery", "ProfoundShoppingApiAssetNameFilter"]


class ProfoundShoppingApiAssetNameFilter(BaseModel):

    field: Literal["asset_name"]

    operator: Literal["is", "not_is", "in", "not_in", "contains", "not_contains", "matches", "contains_case_insensitive", "not_contains_case_insensitive"]

    value: Union[str, List[str]]



class ShoppingMerchantByItemsQuery(BaseModel):

    category_id: str

    start_date: datetime
    """Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp."""

    end_date: datetime
    """End date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp."""

    comparison_start_date: Optional[datetime] = None

    comparison_end_date: Optional[datetime] = None

    date_interval: Optional[Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"]] = None

    filters: Optional[List[Annotated[Union[RegionIdFilter, ModelIdFilter, TopicIdFilter, TagIdFilter, PromptIdFilter, PersonaIdFilter, BrandNameFilter, MerchantNameFilter, ProductNameFilter, ProfoundShoppingApiAssetNameFilter], PropertyInfo(discriminator="field")]]] = None

    order_by: Optional[Dict[str, Literal["asc", "desc"]]] = None

    pagination: Optional[Pagination] = None

    include_count: Optional[bool] = None

    tag_filter_type: Optional[Literal["any", "all"]] = None

    include_no_tag: Optional[bool] = None

    exclude_topic_ids: Optional[bool] = None

    dimensions: Optional[List[Literal["period", "merchant_name", "product_name", "brand_name", "product_image_urls", "product_price", "merchant_prices", "has_instant_checkout", "delivery_options", "merchant_url"]]] = None

    metrics: Optional[List[Literal["merchant_visibility", "product_visibility", "product_rank", "avg_position", "total_count"]]] = None

    product_name: Optional[str] = None
