# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, List, Optional, Union
from datetime import datetime
from typing_extensions import Annotated, Literal
from ..._utils import PropertyInfo

from ..._models import BaseModel
from ..pagination import Pagination
from ..hostname_filter import HostnameFilter
from ..path_filter import PathFilter
from ..region_id_filter import RegionIdFilter
from ..region_name_filter import RegionNameFilter
from ..topic_id_filter import TopicIdFilter
from ..topic_name_filter import TopicNameFilter
from ..model_id_filter import ModelIdFilter
from ..tag_id_filter import TagIdFilter
from ..tag_name_filter import TagNameFilter
from ..url_filter import UrlFilter
from ..root_domain_filter import RootDomainFilter
from ..analysis_type_filter import AnalysisTypeFilter
from ..prompt_type_filter import PromptTypeFilter
from ..persona_id_filter import PersonaIdFilter
from ..prompt_filter import PromptFilter
from ..prompt_id_filter import PromptIdFilter

__all__ = ["CitationsQuery", "CitationCategoryFilter"]


class CitationCategoryFilter(BaseModel):

    field: Literal["citation_category"]

    operator: Literal["is", "not_is", "in", "not_in", "contains", "not_contains", "matches", "contains_case_insensitive", "not_contains_case_insensitive"]

    value: Union[str, List[str]]



class CitationsQuery(BaseModel):

    date_interval: Optional[Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"]] = None
    """Date interval for the report. (only used with date dimension)"""

    dimensions: Optional[List[Literal["hostname", "path", "date", "region", "topic", "topic_id", "model", "tag", "prompt", "prompt_id", "url", "root_domain", "persona", "citation_category"]]] = None
    """Dimensions to group the report by."""

    metrics: List[Literal["count", "citation_share", "share_of_voice", "first_cited_at"]]
    """Metrics to include. `share_of_voice` is deprecated, use `citation_share` instead."""

    order_by: Optional[Dict[str, Literal["asc", "desc"]]] = None
    """
    
        Custom ordering of the report results.
    
        The order is a record of key-value pairs where:
        - `key` is the field to order by, which can be a metric or dimension
        - `value` is the direction of the order, either `asc` for ascending or `desc` for descending.
    
        When not specified, the default order is the first metric in the query descending.
    """

    pagination: Optional[Pagination] = None
    """Pagination settings for the report results."""

    category_id: str

    start_date: datetime
    """Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp."""

    end_date: datetime
    """End date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp."""

    filters: Optional[List[Annotated[Union[HostnameFilter, PathFilter, RegionIdFilter, RegionNameFilter, TopicIdFilter, TopicNameFilter, ModelIdFilter, TagIdFilter, TagNameFilter, UrlFilter, RootDomainFilter, AnalysisTypeFilter, PromptTypeFilter, PersonaIdFilter, CitationCategoryFilter, PromptFilter, PromptIdFilter], PropertyInfo(discriminator="field")]]] = None
    """List of filters to apply to the citations report."""
