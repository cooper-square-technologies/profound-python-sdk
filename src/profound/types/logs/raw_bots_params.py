# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from ..shared_params.pagination import Pagination

__all__ = ["RawBotsParams", "Filter"]


class RawBotsParams(TypedDict, total=False):
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
            "method",
            "path",
            "status_code",
            "ip",
            "user_agent",
            "referer",
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
    """List of filters to apply to the report.

    Each filter has an operator, field, and value.
    """

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


class Filter(TypedDict, total=False):
    field: Required[
        Literal[
            "method",
            "path",
            "status_code",
            "ip",
            "user_agent",
            "referer",
            "query_params",
            "bot_name",
            "bot_provider",
            "bot_types",
        ]
    ]

    operator: Required[
        Literal[
            "is",
            "not_is",
            "in",
            "not_in",
            "contains",
            "not_contains",
            "contains_case_insensitive",
            "not_contains_case_insensitive",
            "matches",
        ]
    ]

    value: Required[Union[str, SequenceNotStr[str], int, Iterable[int]]]
    """Value for the filter.

    Can be a single value or a list of depending on the operator.
    """
