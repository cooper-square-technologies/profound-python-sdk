# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .topic_name_filter_param import TopicNameFilterParam
from .shared_params.pagination import Pagination
from .shared_params.path_filter import PathFilter
from .shared_params.prompt_filter import PromptFilter
from .shared_params.tag_id_filter import TagIDFilter
from .shared_params.model_id_filter import ModelIDFilter
from .shared_params.topic_id_filter import TopicIDFilter
from .shared_params.region_id_filter import RegionIDFilter
from .shared_params.persona_id_filter import PersonaIDFilter

__all__ = [
    "ReportCitationsParams",
    "Filter",
    "FilterHostnameFilter",
    "FilterURLFilter",
    "FilterRootDomainFilter",
    "FilterPromptTypeFilter",
    "FilterCitationCategoryFilter",
    "FilterPromptIDFilter",
]


class ReportCitationsParams(TypedDict, total=False):
    category_id: Required[str]

    end_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """End date for the report.

    Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
    """

    metrics: Required[List[Literal["count", "citation_share", "share_of_voice"]]]
    """Metrics to include.

    `share_of_voice` is deprecated, use `citation_share` instead.
    """

    start_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Start date for the report.

    Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
    """

    date_interval: Literal["day", "week", "month", "year", "relative_week"]
    """Date interval for the report. (only used with date dimension)"""

    dimensions: List[
        Literal[
            "hostname",
            "path",
            "date",
            "region",
            "topic",
            "model",
            "tag",
            "prompt",
            "url",
            "root_domain",
            "persona",
            "citation_category",
        ]
    ]
    """Dimensions to group the report by."""

    filters: Iterable[Filter]
    """List of filters to apply to the citations report."""

    order_by: Dict[str, Literal["asc", "desc"]]
    """Custom ordering of the report results.

        The order is a record of key-value pairs where:
        - `key` is the field to order by, which can be a metric and/or `date`, `hostname`, `path` dimensions
        - `value` is the direction of the order, either `asc` for ascending or `desc` for descending.

        When not specified, the default order is the first metric in the query descending.
    """

    pagination: Pagination
    """Pagination settings for the report results."""


class FilterHostnameFilter(TypedDict, total=False):
    """Filter by hostname"""

    field: Required[Literal["hostname"]]

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


class FilterURLFilter(TypedDict, total=False):
    """Filter by URL"""

    field: Required[Literal["url"]]

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


class FilterRootDomainFilter(TypedDict, total=False):
    """Filter by root domain"""

    field: Required[Literal["root_domain"]]

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


class FilterPromptTypeFilter(TypedDict, total=False):
    """Filter by prompt type (visibility or sentiment)"""

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


class FilterCitationCategoryFilter(TypedDict, total=False):
    """Filter by citation category"""

    field: Required[Literal["citation_category"]]

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


class FilterPromptIDFilter(TypedDict, total=False):
    field: Required[Literal["prompt_id"]]

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[str, SequenceNotStr[str]]]


Filter: TypeAlias = Union[
    FilterHostnameFilter,
    PathFilter,
    RegionIDFilter,
    TopicIDFilter,
    TopicNameFilterParam,
    ModelIDFilter,
    TagIDFilter,
    FilterURLFilter,
    FilterRootDomainFilter,
    FilterPromptTypeFilter,
    PersonaIDFilter,
    FilterCitationCategoryFilter,
    PromptFilter,
    FilterPromptIDFilter,
]
