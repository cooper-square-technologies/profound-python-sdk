# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from ..shared_params.pagination import Pagination
from ..shared_params.path_filter import PathFilter
from ..shared_params.bot_name_filter import BotNameFilter
from ..shared_params.bot_provider_filter import BotProviderFilter

__all__ = [
    "RawBotsParams",
    "Filter",
    "FilterBotTypesFilter",
    "FilterMethodFilter",
    "FilterStatusCodeFilter",
    "FilterIPFilter",
    "FilterUserAgentFilter",
    "FilterRefererFilter",
    "FilterQueryParamsFilter",
]


class RawBotsParams(TypedDict, total=False):
    domain: Required[str]
    """Domain to query logs for."""

    metrics: Required[List[Literal["count"]]]

    start_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Start date for logs.

    Accepts: YYYY-MM-DD, YYYY-MM-DD HH:MM, YYYY-MM-DD HH:MM:SS, or full ISO
    timestamp.
    """

    date_interval: Literal["hour", "day", "week", "month", "year", "relative_week"]
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
            "bot_name",
            "bot_provider",
            "bot_types",
        ]
    ]
    """Dimensions to group the report by."""

    end_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End date for logs.

    Accepts same formats as start_date. Defaults to now if omitted.
    """

    filters: Iterable[Filter]
    """List of filters to apply to the bots logs query."""

    order_by: Dict[str, Literal["asc", "desc"]]
    """Custom ordering of the report results.

    The order is a record of key-value pairs where:

    - key is the field to order by, which can be a metric or dimension
    - value is the direction of the order, either 'asc' for ascending or 'desc' for
      descending.

    When not specified, the default order is the first metric in the query
    descending.
    """

    organization_id: Optional[str]

    pagination: Pagination
    """Pagination settings for the report results."""


class FilterBotTypesFilter(TypedDict, total=False):
    """Filter by bot types (ai_assistant, ai_training, or index)"""

    field: Required[Literal["bot_types"]]

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

    value: Required[
        Union[Literal["ai_assistant", "ai_training", "index"], List[Literal["ai_assistant", "ai_training", "index"]]]
    ]


class FilterMethodFilter(TypedDict, total=False):
    """Filter by HTTP method"""

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


class FilterStatusCodeFilter(TypedDict, total=False):
    """Filter by HTTP status code"""

    field: Required[Literal["status_code"]]

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[int, Iterable[int]]]


class FilterIPFilter(TypedDict, total=False):
    """Filter by IP address"""

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
    """Filter by user agent"""

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
    """Filter by referer"""

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


class FilterQueryParamsFilter(TypedDict, total=False):
    """Filter by query parameters"""

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


Filter: TypeAlias = Union[
    BotNameFilter,
    BotProviderFilter,
    FilterBotTypesFilter,
    FilterMethodFilter,
    PathFilter,
    FilterStatusCodeFilter,
    FilterIPFilter,
    FilterUserAgentFilter,
    FilterRefererFilter,
    FilterQueryParamsFilter,
]
