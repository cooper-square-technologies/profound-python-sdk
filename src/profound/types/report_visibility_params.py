# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .topic_name_filter_param import TopicNameFilterParam
from .shared_params.pagination import Pagination
from .shared_params.prompt_filter import PromptFilter
from .shared_params.asset_name_filter import AssetNameFilter

__all__ = [
    "ReportVisibilityParams",
    "Filter",
    "FilterProfoundAnswerEngineInsightsFiltersRegionIDFilter",
    "FilterProfoundAnswerEngineInsightsFiltersModelIDFilter",
    "FilterProfoundAnswerEngineInsightsFiltersTopicIDFilter",
    "FilterProfoundAnswerEngineInsightsFiltersTagIDFilter",
    "FilterProfoundAnswerEngineInsightsFiltersPromptIDFilter",
    "FilterProfoundAnswerEngineInsightsFiltersPersonaIDFilter",
]


class ReportVisibilityParams(TypedDict, total=False):
    category_id: Required[str]

    end_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """End date for the report.

    Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
    """

    metrics: Required[
        List[Literal["share_of_voice", "mentions_count", "visibility_score", "executions", "average_position"]]
    ]

    start_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Start date for the report.

    Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
    """

    date_interval: Literal["hour", "day", "week", "month", "year", "relative_week"]
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

    filters: Iterable[Filter]
    """List of filters to apply to the visibility report."""

    order_by: Dict[str, Literal["asc", "desc"]]
    """Custom ordering of the report results.

    The order is a record of key-value pairs where:

    - key is the field to order by, which can be a metric or dimension
    - value is the direction of the order, either 'asc' for ascending or 'desc' for
      descending.

    When not specified, the default order is the first metric in the query
    descending.
    """

    pagination: Pagination
    """Pagination settings for the report results."""


class FilterProfoundAnswerEngineInsightsFiltersRegionIDFilter(TypedDict, total=False):
    field: Required[Literal["region_id", "region"]]
    """- `region` - Deprecated"""

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[str, SequenceNotStr[str]]]


class FilterProfoundAnswerEngineInsightsFiltersModelIDFilter(TypedDict, total=False):
    field: Required[Literal["model_id", "model"]]
    """- `model` - Deprecated"""

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[str, SequenceNotStr[str]]]


class FilterProfoundAnswerEngineInsightsFiltersTopicIDFilter(TypedDict, total=False):
    field: Required[Literal["topic_id", "topic"]]
    """- `topic` - Deprecated"""

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[str, SequenceNotStr[str]]]


class FilterProfoundAnswerEngineInsightsFiltersTagIDFilter(TypedDict, total=False):
    field: Required[Literal["tag_id", "tag"]]
    """- `tag` - Deprecated"""

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[str, SequenceNotStr[str]]]


class FilterProfoundAnswerEngineInsightsFiltersPromptIDFilter(TypedDict, total=False):
    field: Required[Literal["prompt_id"]]

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[str, SequenceNotStr[str]]]


class FilterProfoundAnswerEngineInsightsFiltersPersonaIDFilter(TypedDict, total=False):
    field: Required[Literal["persona_id"]]

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[str, SequenceNotStr[str]]]


Filter: TypeAlias = Union[
    FilterProfoundAnswerEngineInsightsFiltersRegionIDFilter,
    FilterProfoundAnswerEngineInsightsFiltersModelIDFilter,
    FilterProfoundAnswerEngineInsightsFiltersTopicIDFilter,
    TopicNameFilterParam,
    AssetNameFilter,
    FilterProfoundAnswerEngineInsightsFiltersTagIDFilter,
    FilterProfoundAnswerEngineInsightsFiltersPromptIDFilter,
    PromptFilter,
    FilterProfoundAnswerEngineInsightsFiltersPersonaIDFilter,
]
