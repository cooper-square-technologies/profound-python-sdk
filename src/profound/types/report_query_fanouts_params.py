# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Iterable, List, Union
from datetime import datetime
from typing_extensions import Annotated, Literal, Required, TypeAlias, TypedDict

from .._utils import PropertyInfo

from .shared_params.pagination import Pagination
from .shared_params.region_id_filter import RegionIDFilter
from .shared_params.region_name_filter import RegionNameFilter
from .shared_params.model_id_filter import ModelIDFilter
from .shared_params.topic_id_filter import TopicIDFilter
from .shared_params.tag_id_filter import TagIDFilter
from .prompt_id_filter_param import PromptIDFilterParam
from .shared_params.persona_id_filter import PersonaIDFilter
from .shared_params.analysis_type_filter import AnalysisTypeFilter
from .shared_params.prompt_type_filter import PromptTypeFilter

__all__ = ["ReportQueryFanoutsParams", "Filter"]


class ReportQueryFanoutsParams(TypedDict, total=False):
    date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"]
    """Date interval for the report. (only used with date dimension)"""

    dimensions: List[Literal["prompt", "query", "model", "region", "date"]]
    """Dimensions to group the report by."""

    metrics: Required[List[Literal["fanouts_per_execution", "total_fanouts", "share", "query_variations"]]]
    """Metrics to return for each row."""

    order_by: Dict[str, Literal["asc", "desc"]]
    """Custom ordering. Keys must be a requested metric or the ``date`` dimension. Values are ``asc`` or ``desc``. Defaults to first metric descending."""

    pagination: Pagination
    """Pagination settings for the report results."""

    category_id: Required[str]

    start_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp."""

    end_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """End date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp."""

    filters: Iterable[Filter]
    """Filters to apply to the query fanout report."""


Filter: TypeAlias = Annotated[
    Union[
        RegionIDFilter,
        RegionNameFilter,
        ModelIDFilter,
        TopicIDFilter,
        TagIDFilter,
        PromptIDFilterParam,
        PersonaIDFilter,
        AnalysisTypeFilter,
        PromptTypeFilter,
    ],
    PropertyInfo(discriminator="field"),
]
