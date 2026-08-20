# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Iterable, List, Optional, Union
from datetime import datetime
from typing_extensions import Annotated, Literal, Required, TypeAlias, TypedDict
from ..._types import SequenceNotStr

from ..._utils import PropertyInfo

from ..shared_params.pagination import Pagination
from ..hostname_filter_param import HostnameFilterParam
from ..shared_params.path_filter import PathFilter
from ..shared_params.region_id_filter import RegionIDFilter
from ..shared_params.topic_id_filter import TopicIDFilter
from ..shared_params.model_id_filter import ModelIDFilter
from ..shared_params.tag_id_filter import TagIDFilter
from ..url_filter_param import URLFilterParam
from ..root_domain_filter_param import RootDomainFilterParam
from ..shared_params.persona_id_filter import PersonaIDFilter
from ..shared_params.prompt_filter import PromptFilter
from ..prompt_id_filter_param import PromptIDFilterParam

__all__ = ["WebSearchResultStreamParams", "Filter", "FilterSearchQueryFilter"]


class WebSearchResultStreamParams(TypedDict, total=False):
    date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"]
    """Date interval for the report. (only used with date dimension)"""

    dimensions: List[
        Literal[
            "hostname",
            "path",
            "url",
            "root_domain",
            "date",
            "region",
            "topic",
            "topic_id",
            "model",
            "tag",
            "prompt",
            "prompt_id",
            "persona",
            "search_query",
        ]
    ]
    """Dimensions to group the report by."""

    metrics: Required[List[Literal["count", "search_share"]]]
    """Metrics to include. `search_share` is the per-prompt occurrence rate."""

    order_by: Dict[str, Literal["asc", "desc"]]
    """
    
        Custom ordering of the report results.
    
        The order is a record of key-value pairs where:
        - `key` is the field to order by, which can be a metric or dimension
        - `value` is the direction of the order, either `asc` for ascending or `desc` for descending.
    
        When not specified, the default order is the first metric in the query descending.
    """

    pagination: Optional[Pagination]
    """Offset-based pagination parameters."""

    category_id: Required[str]

    start_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp."""

    end_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """End date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp."""

    filters: Iterable[Filter]
    """List of filters to apply to the web search results report."""


class FilterSearchQueryFilter(TypedDict, total=False):
    """Filter by web-search query string."""

    field: Required[Literal["search_query"]]

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
    Union[
        HostnameFilterParam,
        PathFilter,
        RegionIDFilter,
        TopicIDFilter,
        ModelIDFilter,
        TagIDFilter,
        URLFilterParam,
        RootDomainFilterParam,
        PersonaIDFilter,
        PromptFilter,
        PromptIDFilterParam,
        FilterSearchQueryFilter,
    ],
    PropertyInfo(discriminator="field"),
]
