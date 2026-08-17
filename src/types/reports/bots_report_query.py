# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, List, Optional, Union
from datetime import datetime
from typing_extensions import Annotated, Literal
from ..._utils import PropertyInfo

from ..._models import BaseModel
from ..pagination import Pagination
from ..path_filter import PathFilter
from ..bot_name_filter import BotNameFilter
from ..bot_provider_filter import BotProviderFilter

__all__ = ["BotsReportQuery", "NumericMetricFilter"]


class NumericMetricFilter(BaseModel):

    field: str

    operator: Literal[">", ">=", "<", "<=", "=", "==", "!="]

    value: Union[int, float]



class BotsReportQuery(BaseModel):

    date_interval: Optional[Literal["hour", "day", "week", "month", "year", "relative_week"]] = None
    """Date interval for the report. (only used with date dimension)"""

    dimensions: Optional[List[Literal["date", "path", "bot_name", "bot_provider"]]] = None
    """Dimensions to group the report by."""

    metrics: List[Literal["count", "citations", "indexing", "training", "last_visit"]]

    order_by: Optional[Dict[str, Literal["asc", "desc"]]] = None
    """
    
    Custom ordering of the report results.
    
    The order is a record of key-value pairs where:
    - key is the field to order by, which can be a metric or dimension
    - value is the direction of the order, either 'asc' for ascending or 'desc' for descending.
    
    When not specified, the default order is the first metric in the query descending.
    """

    pagination: Optional[Pagination] = None
    """Pagination settings for the report results."""

    domain: str
    """Domain to query logs for."""

    start_date: datetime
    """Start date for logs. Accepts: YYYY-MM-DD, YYYY-MM-DD HH:MM, YYYY-MM-DD HH:MM:SS, or full ISO timestamp."""

    end_date: Optional[datetime] = None
    """End date for logs. Accepts same formats as start_date. Defaults to now if omitted."""

    organization_id: Optional[str] = None

    metric_filters: Optional[List[NumericMetricFilter]] = None
    """Numeric filters applied after report metrics are calculated."""

    filters: Optional[List[Annotated[Union[PathFilter, BotNameFilter, BotProviderFilter], PropertyInfo(discriminator="field")]]] = None
    """Filters for bots report."""
