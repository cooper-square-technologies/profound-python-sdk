# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from ..shared_params.pagination import Pagination

__all__ = [
    "RawLogsParams",
    "Filter",
    "FilterMethodFilter",
    "FilterHostFilter",
    "FilterAppModelsAgentAnalyticsFiltersPathFilter",
    "FilterStatusCodeFilter",
    "FilterIPFilter",
    "FilterUserAgentFilter",
    "FilterRefererFilter",
    "FilterProviderFilter",
    "FilterQueryParamsFilter",
    "FilterBytesSentFilter",
    "FilterDurationMsFilter",
]


class RawLogsParams(TypedDict, total=False):
    domain: Required[str]
    """Domain to query logs for."""

    metrics: Required[List[Literal["count"]]]

    start_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Start date for logs.

    Accepts: YYYY-MM-DD, YYYY-MM-DD HH:MM, YYYY-MM-DD HH:MM:SS, or full ISO
    timestamp.
    """

    date_interval: Literal["day", "week", "month", "year"]
    """Date interval for the report. (only used with date dimension)"""

    dimensions: List[
        Literal[
            "timestamp",
            "method",
            "host",
            "path",
            "status_code",
            "ip",
            "user_agent",
            "referer",
            "bytes_sent",
            "duration_ms",
            "query_params",
        ]
    ]
    """Dimensions to group the report by."""

    end_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End date for logs.

    Accepts same formats as start_date. Defaults to now if omitted.
    """

    filters: Iterable[Filter]
    """Filters to apply to the logs query."""

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


class FilterMethodFilter(TypedDict, total=False):
    field: Required[Literal["method"]]

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


class FilterHostFilter(TypedDict, total=False):
    field: Required[Literal["host"]]

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


class FilterAppModelsAgentAnalyticsFiltersPathFilter(TypedDict, total=False):
    field: Required[Literal["path"]]

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


class FilterStatusCodeFilter(TypedDict, total=False):
    field: Required[Literal["status_code"]]

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[int, Iterable[int]]]


class FilterIPFilter(TypedDict, total=False):
    field: Required[Literal["ip"]]

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


class FilterUserAgentFilter(TypedDict, total=False):
    field: Required[Literal["user_agent"]]

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


class FilterRefererFilter(TypedDict, total=False):
    field: Required[Literal["referer"]]

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


class FilterProviderFilter(TypedDict, total=False):
    field: Required[Literal["provider"]]

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


class FilterQueryParamsFilter(TypedDict, total=False):
    field: Required[Literal["query_params"]]

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


class FilterBytesSentFilter(TypedDict, total=False):
    field: Required[Literal["bytes_sent"]]

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[int, Iterable[int]]]


class FilterDurationMsFilter(TypedDict, total=False):
    field: Required[Literal["duration_ms"]]

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[int, Iterable[int]]]


Filter: TypeAlias = Union[
    FilterMethodFilter,
    FilterHostFilter,
    FilterAppModelsAgentAnalyticsFiltersPathFilter,
    FilterStatusCodeFilter,
    FilterIPFilter,
    FilterUserAgentFilter,
    FilterRefererFilter,
    FilterProviderFilter,
    FilterQueryParamsFilter,
    FilterBytesSentFilter,
    FilterDurationMsFilter,
]
