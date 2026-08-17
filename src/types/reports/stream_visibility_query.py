# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, List, Optional, Union
from datetime import datetime
from typing_extensions import Annotated, Literal
from ..._utils import PropertyInfo

from ..._models import BaseModel
from ..pagination import Pagination
from ..region_id_filter import RegionIdFilter
from ..region_name_filter import RegionNameFilter
from ..model_id_filter import ModelIdFilter
from ..topic_id_filter import TopicIdFilter
from ..topic_name_filter import TopicNameFilter
from ..tag_id_filter import TagIdFilter
from ..tag_name_filter import TagNameFilter
from ..prompt_id_filter import PromptIdFilter
from ..prompt_filter import PromptFilter
from ..persona_id_filter import PersonaIdFilter

__all__ = ["StreamVisibilityQuery", "ProfoundAnswerEngineInsightsFiltersAssetNameFilter"]


class ProfoundAnswerEngineInsightsFiltersAssetNameFilter(BaseModel):

    field: Literal["asset_name"]

    operator: Literal["is", "not_is", "in", "not_in", "contains", "not_contains", "matches", "contains_case_insensitive", "not_contains_case_insensitive"]

    value: Union[str, List[str]]



class StreamVisibilityQuery(BaseModel):

    date_interval: Optional[Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"]] = None
    """Date interval for the report. (only used with date dimension)"""

    dimensions: Optional[List[Literal["date", "region", "topic", "topic_id", "model", "asset_id", "asset_name", "prompt", "prompt_id", "tag", "persona"]]] = None
    """Dimensions to group the report by."""

    metrics: List[Literal["share_of_voice", "mentions_count", "visibility_score", "executions", "average_position"]]

    order_by: Optional[Dict[str, Literal["asc", "desc"]]] = None
    """
    
    Custom ordering of the report results.
    
    The order is a record of key-value pairs where:
    - key is the field to order by, which can be a metric or dimension
    - value is the direction of the order, either 'asc' for ascending or 'desc' for descending.
    
    When not specified, the default order is the first metric in the query descending.
    """

    pagination: Optional[Pagination] = None

    category_id: str

    start_date: datetime
    """Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp."""

    end_date: datetime
    """End date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp."""

    filters: Optional[List[Annotated[Union[RegionIdFilter, RegionNameFilter, ModelIdFilter, TopicIdFilter, TopicNameFilter, ProfoundAnswerEngineInsightsFiltersAssetNameFilter, TagIdFilter, TagNameFilter, PromptIdFilter, PromptFilter, PersonaIdFilter], PropertyInfo(discriminator="field")]]] = None
    """List of filters to apply to the visibility report."""
