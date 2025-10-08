# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared_params.pagination import Pagination

__all__ = ["ReportVisibilityParams", "Filter"]


class ReportVisibilityParams(TypedDict, total=False):
    category_id: Required[str]

    end_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """End date for the report.

    Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
    """

    metrics: Required[List[Literal["share_of_voice", "mentions_count", "visibility_score"]]]

    start_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Start date for the report.

    Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
    """

    date_interval: Literal["day", "week", "month", "year"]
    """Date interval for the report. (only used with date dimension)"""

    dimensions: List[Literal["date", "region", "topic", "model", "asset_name", "prompt", "tag"]]
    """Dimensions to group the report by."""

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
    field: Required[Literal["region", "topic", "model", "asset_name", "prompt", "tag"]]

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
