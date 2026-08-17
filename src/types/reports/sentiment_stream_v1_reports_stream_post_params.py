# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional, Union
from datetime import datetime
from typing_extensions import Annotated, Literal, Required, TypedDict
from ..._types import SequenceNotStr
from ..pagination import Pagination
from ..asset_id_filter import AssetIdFilter
from ..region_id_filter import RegionIdFilter
from ..region_name_filter import RegionNameFilter
from ..topic_id_filter import TopicIdFilter
from ..topic_name_filter import TopicNameFilter
from ..model_id_filter import ModelIdFilter
from ..tag_id_filter import TagIdFilter
from ..tag_name_filter import TagNameFilter
from ..prompt_filter import PromptFilter
from ..persona_id_filter import PersonaIdFilter
from ..._utils import PropertyInfo

__all__ = ["SentimentStreamV1ReportsStreamPostParams", "ProfoundAnswerEngineInsightsFiltersAssetNameFilter", "ThemeFilter"]


class SentimentStreamV1ReportsStreamPostParams(TypedDict, total=False):

    date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"]
    """Date interval for the report. (only used with date dimension)"""

    dimensions: Iterable[Literal["theme", "date", "region", "topic", "topic_id", "model", "asset_id", "asset_name", "tag", "prompt", "prompt_id", "sentiment_type", "persona"]]
    """Dimensions to group the report by."""

    metrics: Required[Iterable[Literal["positive", "negative", "occurrences"]]]

    order_by: Dict[str, Literal["asc", "desc"]]
    """
    
    Custom ordering of the report results.
    
    The order is a record of key-value pairs where:
    - key is the field to order by, which can be a metric or dimension
    - value is the direction of the order, either 'asc' for ascending or 'desc' for descending.
    
    When not specified, the default order is the first metric in the query descending.
    """

    pagination: Optional[Pagination]

    category_id: Required[str]

    start_date: Required[Union[str, datetime]]
    """Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp."""

    end_date: Required[Union[str, datetime]]
    """End date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp."""

    filters: Iterable[Annotated[Union[AssetIdFilter, ProfoundAnswerEngineInsightsFiltersAssetNameFilter, ThemeFilter, RegionIdFilter, RegionNameFilter, TopicIdFilter, TopicNameFilter, ModelIdFilter, TagIdFilter, TagNameFilter, PromptFilter, PersonaIdFilter], PropertyInfo(discriminator="field")]]
    """List of filters to apply to the sentiment report."""


class ThemeFilter(TypedDict, total=False):

    field: Required[Literal["theme"]]

    operator: Required[Literal["is", "not_is", "in", "not_in", "contains", "not_contains", "matches", "contains_case_insensitive", "not_contains_case_insensitive"]]

    value: Required[Union[str, SequenceNotStr[str]]]

class ProfoundAnswerEngineInsightsFiltersAssetNameFilter(TypedDict, total=False):

    field: Required[Literal["asset_name"]]

    operator: Required[Literal["is", "not_is", "in", "not_in", "contains", "not_contains", "matches", "contains_case_insensitive", "not_contains_case_insensitive"]]

    value: Required[Union[str, SequenceNotStr[str]]]

