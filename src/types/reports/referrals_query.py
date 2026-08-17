# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, List, Optional, Union
from datetime import datetime
from typing_extensions import Annotated, Literal
from ..._utils import PropertyInfo

from ..._models import BaseModel
from ..pagination import Pagination
from ..path_filter import PathFilter

__all__ = ["ReferralsQuery", "NumericMetricFilter", "ReferralSourceFilter"]


class ReferralSourceFilter(BaseModel):

    field: Literal["referral_source"]

    operator: Literal["is", "not_is", "in", "not_in", "contains", "not_contains", "matches", "contains_case_insensitive", "not_contains_case_insensitive"]

    value: Union[Literal["openai", "none", "anthropic", "deepseek", "perplexity", "you", "grok", "microsoft", "gemini", "internal", "other"], List[Literal["openai", "none", "anthropic", "deepseek", "perplexity", "you", "grok", "microsoft", "gemini", "internal", "other"]]]

class NumericMetricFilter(BaseModel):

    field: str

    operator: Literal[">", ">=", "<", "<=", "=", "==", "!="]

    value: Union[int, float]



class ReferralsQuery(BaseModel):

    date_interval: Optional[Literal["hour", "day", "week", "month", "year", "relative_week"]] = None
    """Date interval for the report. (only used with date dimension)"""

    dimensions: Optional[List[Literal["date", "path", "referral_source"]]] = None
    """Dimensions to group the report by."""

    metrics: List[Literal["visits", "last_visit"]]

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

    filters: Optional[List[Annotated[Union[PathFilter, ReferralSourceFilter], PropertyInfo(discriminator="field")]]] = None
    """Filters for referrals report."""
