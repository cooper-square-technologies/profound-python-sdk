# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional, Union
from datetime import datetime
from typing_extensions import Annotated, Literal, Required, TypedDict
from ..pagination import Pagination
from ..path_filter import PathFilter
from ..bot_name_filter import BotNameFilter
from ..bot_provider_filter import BotProviderFilter
from ..._utils import PropertyInfo

__all__ = ["BotCreateReportV1V1ReportsPostParams", "NumericMetricFilter"]


class BotCreateReportV1V1ReportsPostParams(TypedDict, total=False):

    date_interval: Literal["hour", "day", "week", "month", "year", "relative_week"]
    """Date interval for the report. (only used with date dimension)"""

    dimensions: Iterable[Literal["date", "path", "bot_name", "bot_provider"]]
    """Dimensions to group the report by."""

    metrics: Required[Iterable[Literal["count", "citations", "indexing", "training", "last_visit"]]]

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

    start_date: Required[Union[str, datetime]]
    """Start date for logs. Accepts: YYYY-MM-DD, YYYY-MM-DD HH:MM, YYYY-MM-DD HH:MM:SS, or full ISO timestamp."""

    end_date: Union[str, datetime]
    """End date for logs. Accepts same formats as start_date. Defaults to now if omitted."""

    organization_id: Optional[str]

    metric_filters: Iterable[NumericMetricFilter]
    """Numeric filters applied after report metrics are calculated."""

    filters: Iterable[Annotated[Union[PathFilter, BotNameFilter, BotProviderFilter], PropertyInfo(discriminator="field")]]
    """Filters for bots report."""


class NumericMetricFilter(TypedDict, total=False):

    field: Required[str]

    operator: Required[Literal[">", ">=", "<", "<=", "=", "==", "!="]]

    value: Required[Union[int, float]]

