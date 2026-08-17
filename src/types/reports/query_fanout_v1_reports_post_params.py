# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Union
from datetime import datetime
from typing_extensions import Annotated, Literal, Required, TypedDict
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
from ..._utils import PropertyInfo

__all__ = ["QueryFanoutV1ReportsPostParams"]


class QueryFanoutV1ReportsPostParams(TypedDict, total=False):

    date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"]
    """Date interval for the report. (only used with date dimension)"""

    dimensions: Iterable[Literal["prompt", "query", "model", "region", "date"]]
    """Dimensions to group the report by."""

    metrics: Required[Iterable[Literal["fanouts_per_execution", "total_fanouts", "share", "query_variations"]]]

    order_by: Dict[str, Literal["asc", "desc"]]
    """Custom ordering. Keys must be a requested metric or the ``date`` dimension. Values are ``asc`` or ``desc``. Defaults to first metric descending."""

    pagination: Pagination
    """Pagination settings for the report results."""

    category_id: Required[str]

    start_date: Required[Union[str, datetime]]
    """Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp."""

    end_date: Required[Union[str, datetime]]
    """End date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp."""

    filters: Iterable[Annotated[Union[RegionIdFilter, RegionNameFilter, ModelIdFilter, TopicIdFilter, TagIdFilter, PromptIdFilter, PersonaIdFilter, AnalysisTypeFilter, PromptTypeFilter], PropertyInfo(discriminator="field")]]
    """Filters to apply to the query fanout report."""
