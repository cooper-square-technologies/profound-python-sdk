# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Iterable, List, Optional, Union
from datetime import datetime
from typing_extensions import Annotated, Literal, Required, TypeAlias, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

from .shared_params.pagination import Pagination
from .shared_params.numeric_metric_filter import NumericMetricFilter
from .shared_params.path_filter import PathFilter

__all__ = ["ReportGetReferralsReportV2Params", "Filter", "FilterReferralSourceFilter", "FilterReferralTypeFilter"]


class ReportGetReferralsReportV2Params(TypedDict, total=False):
    date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"]
    """Date interval for the report. (only used with date dimension)"""

    dimensions: List[Literal["date", "hour", "host", "path", "referral_source", "referral_type"]]
    """Dimensions to group the report by."""

    metrics: Required[List[Literal["visits", "last_visit"]]]

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
    """End date in UTC. Accepts same formats as start_date. Defaults to now UTC if omitted."""

    organization_id: Optional[str]

    timezone: str
    """IANA timezone name for date bucketing and filter boundaries."""

    view_id: Optional[str]
    """Domain segment UUID used to scope the query to a configured subset of hosts and paths."""

    metric_filters: Iterable[NumericMetricFilter]
    """Numeric filters applied after report metrics are calculated."""

    filters: Iterable[Filter]
    """Filters for referrals report."""


class FilterReferralTypeFilter(TypedDict, total=False):
    """Filter by referral type"""

    field: Required[Literal["referral_type"]]

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
        Union[Literal["internal", "referer", "utm", "none"], List[Literal["internal", "referer", "utm", "none"]]]
    ]


class FilterReferralSourceFilter(TypedDict, total=False):
    """
    Filter by referral source. Values are not enum-constrained so the platform's shared
    provider filter can pass through IDs that have bot data but no referral data.
    """

    field: Required[Literal["referral_source"]]

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


Filter: TypeAlias = Annotated[
    Union[PathFilter, FilterReferralSourceFilter, FilterReferralTypeFilter], PropertyInfo(discriminator="field")
]
