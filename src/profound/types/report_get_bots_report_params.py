# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Iterable, List, Optional, Union
from datetime import datetime
from typing_extensions import Annotated, Literal, Required, TypeAlias, TypedDict

from .._utils import PropertyInfo

from .shared_params.pagination import Pagination
from .shared_params.path_filter import PathFilter
from .shared_params.bot_name_filter import BotNameFilter
from .shared_params.bot_provider_filter import BotProviderFilter

__all__ = ["ReportGetBotsReportParams", "MetricFilter", "Filter"]


class ReportGetBotsReportParams(TypedDict, total=False):
    date_interval: Literal["hour", "day", "week", "month", "year", "relative_week"]
    """Date interval for the report. (only used with date dimension)"""

    dimensions: List[Literal["date", "host", "path", "bot_name", "bot_provider"]]
    """Dimensions to group the report by."""

    metrics: Required[List[Literal["count", "citations", "indexing", "training", "last_visit"]]]

    order_by: Dict[str, Literal["asc", "desc"]]
    """
    
    Custom ordering of the report results.
    
    The order is a record of key-value pairs where:
    - key is the field to order by, which can be a metric or dimension
    - value is the direction of the order, either 'asc' for ascending or 'desc' for descending.
    
    When not specified, the default order is the first metric in the query descending.
    """

    pagination: Pagination
    """Pagination settings for the report results."""

    domain: Required[str]
    """Domain to query logs for."""

    start_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Start date for logs. Accepts: YYYY-MM-DD, YYYY-MM-DD HH:MM, YYYY-MM-DD HH:MM:SS, or full ISO timestamp."""

    end_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End date for logs. Accepts same formats as start_date. Defaults to now if omitted."""

    organization_id: Optional[str]

    metric_filters: Iterable[MetricFilter]
    """Numeric filters applied after report metrics are calculated."""

    filters: Iterable[Filter]
    """Filters for bots report."""


Filter: TypeAlias = Annotated[Union[PathFilter, BotNameFilter, BotProviderFilter], PropertyInfo(discriminator="field")]


class MetricFilter(TypedDict, total=False):
    field: Required[str]

    operator: Required[Literal[">", ">=", "<", "<=", "=", "==", "!="]]

    value: Required[float]
