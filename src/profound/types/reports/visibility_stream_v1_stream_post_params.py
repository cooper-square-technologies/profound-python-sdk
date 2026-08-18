# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Iterable, List, Optional, Union
from datetime import datetime
from typing_extensions import Annotated, Literal, Required, TypeAlias, TypedDict

from ..._utils import PropertyInfo

from ..shared_params.pagination import Pagination
from ..shared_params.region_id_filter import RegionIDFilter
from ..shared_params.region_name_filter import RegionNameFilter
from ..shared_params.model_id_filter import ModelIDFilter
from ..shared_params.topic_id_filter import TopicIDFilter
from ..shared_params.topic_name_filter import TopicNameFilter
from ..shared_params.profound_answer_engine_insights_filters_asset_name_filter import (
    ProfoundAnswerEngineInsightsFiltersAssetNameFilter,
)
from ..shared_params.tag_id_filter import TagIDFilter
from ..shared_params.tag_name_filter import TagNameFilter
from ..shared_params.prompt_id_filter import PromptIDFilter
from ..shared_params.prompt_filter import PromptFilter
from ..shared_params.persona_id_filter import PersonaIDFilter

__all__ = ["VisibilityStreamV1StreamPostParams", "Filter"]


class VisibilityStreamV1StreamPostParams(TypedDict, total=False):
    date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"]
    """Date interval for the report. (only used with date dimension)"""

    dimensions: List[
        Literal[
            "date",
            "region",
            "topic",
            "topic_id",
            "model",
            "asset_id",
            "asset_name",
            "prompt",
            "prompt_id",
            "tag",
            "persona",
        ]
    ]
    """Dimensions to group the report by."""

    metrics: Required[
        List[Literal["share_of_voice", "mentions_count", "visibility_score", "executions", "average_position"]]
    ]

    order_by: Dict[str, Literal["asc", "desc"]]
    """
    
    Custom ordering of the report results.
    
    The order is a record of key-value pairs where:
    - key is the field to order by, which can be a metric or dimension
    - value is the direction of the order, either 'asc' for ascending or 'desc' for descending.
    
    When not specified, the default order is the first metric in the query descending.
    """

    pagination: Optional[Pagination]
    """Offset-based pagination parameters."""

    category_id: Required[str]

    start_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp."""

    end_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """End date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp."""

    filters: Iterable[Filter]
    """List of filters to apply to the visibility report."""


Filter: TypeAlias = Annotated[
    Union[
        RegionIDFilter,
        RegionNameFilter,
        ModelIDFilter,
        TopicIDFilter,
        TopicNameFilter,
        ProfoundAnswerEngineInsightsFiltersAssetNameFilter,
        TagIDFilter,
        TagNameFilter,
        PromptIDFilter,
        PromptFilter,
        PersonaIDFilter,
    ],
    PropertyInfo(discriminator="field"),
]
