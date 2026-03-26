# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared_params.pagination import Pagination
from .shared_params.tag_id_filter import TagIDFilter
from .shared_params.model_id_filter import ModelIDFilter
from .shared_params.topic_id_filter import TopicIDFilter
from .shared_params.region_id_filter import RegionIDFilter
from .shared_params.persona_id_filter import PersonaIDFilter

__all__ = ["ReportQueryFanoutsParams", "Filter", "FilterPromptIDFilter", "FilterPromptTypeFilter"]


class ReportQueryFanoutsParams(TypedDict, total=False):
    category_id: Required[str]

    end_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """End date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp."""

    metrics: Required[List[Literal["fanouts_per_execution", "total_fanouts", "share"]]]

    start_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp."""

    date_interval: Literal["hour", "day", "week", "month", "year", "relative_week"]
    """Date interval for the report. (only used with date dimension)"""

    dimensions: List[Literal["prompt", "query", "model", "region", "date"]]
    """Dimensions to group the report by."""

    filters: Iterable[Filter]
    """Filters to apply to the query fanout report."""

    order_by: Dict[str, Literal["asc", "desc"]]
    """Custom ordering.

    Keys must be a requested metric or the `date` dimension. Values are `asc` or
    `desc`. Defaults to first metric descending.
    """

    pagination: Pagination
    """Pagination settings for the report results."""


class FilterPromptIDFilter(TypedDict, total=False):
    """Filter by prompt UUID."""

    field: Required[Literal["prompt_id"]]

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[str, SequenceNotStr[str]]]


class FilterPromptTypeFilter(TypedDict, total=False):
    """Filter by prompt type (visibility or sentiment)."""

    field: Required[Literal["prompt_type"]]

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

    value: Required[Union[Literal["visibility", "sentiment"], List[Literal["visibility", "sentiment"]]]]


Filter: TypeAlias = Union[
    RegionIDFilter,
    ModelIDFilter,
    TopicIDFilter,
    TagIDFilter,
    FilterPromptIDFilter,
    PersonaIDFilter,
    FilterPromptTypeFilter,
]
