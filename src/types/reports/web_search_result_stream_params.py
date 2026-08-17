# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional, Union
from datetime import datetime
from typing_extensions import Annotated, Literal, Required, TypedDict
from ..._types import SequenceNotStr
from ..pagination import Pagination
from ..hostname_filter import HostnameFilter
from ..path_filter import PathFilter
from ..region_id_filter import RegionIdFilter
from ..topic_id_filter import TopicIdFilter
from ..model_id_filter import ModelIdFilter
from ..tag_id_filter import TagIdFilter
from ..url_filter import UrlFilter
from ..root_domain_filter import RootDomainFilter
from ..persona_id_filter import PersonaIdFilter
from ..prompt_filter import PromptFilter
from ..prompt_id_filter import PromptIdFilter
from ..._utils import PropertyInfo

__all__ = ["WebSearchResultStreamParams", "SearchQueryFilter"]


class WebSearchResultStreamParams(TypedDict, total=False):

    date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"]
    """Date interval for the report. (only used with date dimension)"""

    dimensions: Iterable[Literal["hostname", "path", "url", "root_domain", "date", "region", "topic", "topic_id", "model", "tag", "prompt", "prompt_id", "persona", "search_query"]]
    """Dimensions to group the report by."""

    metrics: Required[Iterable[Literal["count", "search_share"]]]
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

    category_id: Required[str]

    start_date: Required[Union[str, datetime]]
    """Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp."""

    end_date: Required[Union[str, datetime]]
    """End date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp."""

    filters: Iterable[Annotated[Union[HostnameFilter, PathFilter, RegionIdFilter, TopicIdFilter, ModelIdFilter, TagIdFilter, UrlFilter, RootDomainFilter, PersonaIdFilter, PromptFilter, PromptIdFilter, SearchQueryFilter], PropertyInfo(discriminator="field")]]
    """List of filters to apply to the web search results report."""


class SearchQueryFilter(TypedDict, total=False):

    field: Required[Literal["search_query"]]

    operator: Required[Literal["is", "not_is", "in", "not_in", "contains", "not_contains", "matches", "contains_case_insensitive", "not_contains_case_insensitive"]]

    value: Required[Union[str, SequenceNotStr[str]]]

