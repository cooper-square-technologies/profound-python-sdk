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

__all__ = ["BotCreateReportV2V2ReportsPostParams", "NumericMetricFilter", "BotTypeFilter"]


class BotCreateReportV2V2ReportsPostParams(TypedDict, total=False):

    date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"]
    """Date interval for the report. (only used with date dimension)"""

    dimensions: Iterable[Literal["date", "hour", "path", "bot_name", "bot_provider", "bot_type"]]
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
    """End date in UTC. Accepts same formats as start_date. Defaults to now UTC if omitted."""

    organization_id: Optional[str]

    metric_filters: Iterable[NumericMetricFilter]
    """Numeric filters applied after report metrics are calculated."""

    filters: Iterable[Annotated[Union[PathFilter, BotNameFilter, BotProviderFilter, BotTypeFilter], PropertyInfo(discriminator="field")]]
    """Filters for bots report."""


class BotTypeFilter(TypedDict, total=False):

    field: Required[Literal["bot_type"]]

    operator: Required[Literal["is", "not_is", "in", "not_in", "contains", "not_contains", "matches", "contains_case_insensitive", "not_contains_case_insensitive"]]

    value: Required[Union[Literal["ai_assistant", "ai_training", "index", "ai_agent"], Iterable[Literal["ai_assistant", "ai_training", "index", "ai_agent"]]]]

class NumericMetricFilter(TypedDict, total=False):

    field: Required[str]

    operator: Required[Literal[">", ">=", "<", "<=", "=", "==", "!="]]

    value: Required[Union[int, float]]

