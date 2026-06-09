# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.pagination import Pagination
from .shared_params.path_filter import PathFilter
from .shared_params.bot_name_filter import BotNameFilter
from .shared_params.bot_provider_filter import BotProviderFilter

__all__ = ["ReportGetBotsReportParams", "Filter", "MetricFilter"]


class ReportGetBotsReportParams(TypedDict, total=False):
    domain: Required[str]
    """Domain to query logs for."""

    metrics: Required[List[Literal["count", "citations", "indexing", "training", "last_visit"]]]

    start_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Start date for logs.

    Accepts: YYYY-MM-DD, YYYY-MM-DD HH:MM, YYYY-MM-DD HH:MM:SS, or full ISO
    timestamp.
    """

    date_interval: Literal["hour", "day", "week", "month", "year", "relative_week"]
    """Date interval for the report. (only used with date dimension)"""

    dimensions: List[Literal["date", "path", "bot_name", "bot_provider"]]
    """Dimensions to group the report by."""

    end_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End date for logs.

    Accepts same formats as start_date. Defaults to now if omitted.
    """

    filters: Iterable[Filter]
    """Filters for bots report."""

    metric_filters: Iterable[MetricFilter]
    """Numeric filters applied after report metrics are calculated."""

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


Filter: TypeAlias = Union[PathFilter, BotNameFilter, BotProviderFilter]


class MetricFilter(TypedDict, total=False):
    field: Required[str]

    operator: Required[Literal[">", ">=", "<", "<=", "=", "==", "!="]]

    value: Required[float]
