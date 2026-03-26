# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared_params.pagination import Pagination

__all__ = [
    "PromptVolumeCreateVolumeParams",
    "Filter",
    "FilterCountryCodeFilter",
    "FilterFrequencyFilter",
    "FilterKeywordFilter",
    "FilterMatchingTypeFilter",
    "FilterPlatformFilter",
]


class PromptVolumeCreateVolumeParams(TypedDict, total=False):
    end_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """End date for the query.

    Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
    """

    metrics: Required[List[Literal["volume", "change"]]]

    start_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Start date for the query.

    Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
    """

    date_interval: Literal["hour", "day", "week", "month", "year", "relative_week"]
    """Date interval for the report. (only used with date dimension)"""

    dimensions: List[Literal["keyword", "date", "platform", "country_code", "matching_type", "frequency"]]
    """Dimensions to group the report by."""

    filters: Iterable[Filter]
    """Filters to apply to the query"""

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


class FilterCountryCodeFilter(TypedDict, total=False):
    """Filter by country code"""

    field: Required[Literal["country_code"]]

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


class FilterFrequencyFilter(TypedDict, total=False):
    """Filter by frequency"""

    field: Required[Literal["frequency"]]

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


class FilterKeywordFilter(TypedDict, total=False):
    """Filter by keyword"""

    field: Required[Literal["keyword"]]

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


class FilterMatchingTypeFilter(TypedDict, total=False):
    """Filter by matching type"""

    field: Required[Literal["matching_type"]]

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


class FilterPlatformFilter(TypedDict, total=False):
    """Filter by platform"""

    field: Required[Literal["platform"]]

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


Filter: TypeAlias = Union[
    FilterCountryCodeFilter, FilterFrequencyFilter, FilterKeywordFilter, FilterMatchingTypeFilter, FilterPlatformFilter
]
