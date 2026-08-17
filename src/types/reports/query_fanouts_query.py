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
from ..tag_id_filter import TagIdFilter
from ..prompt_id_filter import PromptIdFilter
from ..persona_id_filter import PersonaIdFilter
from ..analysis_type_filter import AnalysisTypeFilter
from ..prompt_type_filter import PromptTypeFilter

__all__ = ["QueryFanoutsQuery"]


class QueryFanoutsQuery(BaseModel):

    date_interval: Optional[Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"]] = None
    """Date interval for the report. (only used with date dimension)"""

    dimensions: Optional[List[Literal["prompt", "query", "model", "region", "date"]]] = None
    """Dimensions to group the report by."""

    metrics: List[Literal["fanouts_per_execution", "total_fanouts", "share", "query_variations"]]

    order_by: Optional[Dict[str, Literal["asc", "desc"]]] = None
    """Custom ordering. Keys must be a requested metric or the ``date`` dimension. Values are ``asc`` or ``desc``. Defaults to first metric descending."""

    pagination: Optional[Pagination] = None
    """Pagination settings for the report results."""

    category_id: str

    start_date: datetime
    """Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp."""

    end_date: datetime
    """End date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp."""

    filters: Optional[List[Annotated[Union[RegionIdFilter, RegionNameFilter, ModelIdFilter, TopicIdFilter, TagIdFilter, PromptIdFilter, PersonaIdFilter, AnalysisTypeFilter, PromptTypeFilter], PropertyInfo(discriminator="field")]]] = None
    """Filters to apply to the query fanout report."""
