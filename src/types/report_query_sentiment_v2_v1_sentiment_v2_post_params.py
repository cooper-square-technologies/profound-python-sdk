# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional, Union
from datetime import datetime
from typing_extensions import Annotated, Literal, Required, TypedDict
from .._types import SequenceNotStr
from .pagination import Pagination
from .._utils import PropertyInfo

__all__ = ["ReportQuerySentimentV2V1SentimentV2PostParams", "SentimentV2ModelIdFilter", "SentimentV2RegionIdFilter", "SentimentV2TopicIdFilter", "SentimentV2PromptIdFilter", "SentimentV2PersonaIdFilter", "SentimentV2TagIdFilter", "SentimentV2RunIdFilter", "SentimentV2ThemeIdFilter", "SentimentV2ThemeFilter", "SentimentV2ClaimIdFilter", "SentimentV2ClaimFilter", "SentimentV2SentimentFilter"]


class ReportQuerySentimentV2V1SentimentV2PostParams(TypedDict, total=False):

    category_id: Required[str]

    asset_name: Required[str]

    start_date: Required[Union[str, datetime]]
    """Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp."""

    end_date: Required[Union[str, datetime]]
    """End date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp."""

    comparison_start_date: Optional[Union[str, datetime]]
    """Start of the previous period for delta computation."""

    comparison_end_date: Optional[Union[str, datetime]]
    """End of the previous period for delta computation."""

    date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"]
    """Date interval for the report. Only used when dimensions includes date."""

    dimensions: Iterable[Literal["date", "topic", "region", "model", "prompt", "persona", "tag", "theme", "claim", "run", "asset_name"]]
    """Dimensions to group the report by."""

    metrics: Required[Iterable[Literal["sentiment", "occurrence"]]]

    filters: Iterable[Annotated[Union[SentimentV2ModelIdFilter, SentimentV2RegionIdFilter, SentimentV2TopicIdFilter, SentimentV2PromptIdFilter, SentimentV2PersonaIdFilter, SentimentV2TagIdFilter, SentimentV2RunIdFilter, SentimentV2ThemeIdFilter, SentimentV2ThemeFilter, SentimentV2ClaimIdFilter, SentimentV2ClaimFilter, SentimentV2SentimentFilter], PropertyInfo(discriminator="field")]]
    """List of filters to apply to the sentiment-v2 report."""

    order_by: Dict[str, Literal["asc", "desc"]]
    """Custom ordering of report results. Dimension keys must also be present in dimensions. The sentiment metric orders by positive_sentiment."""

    pagination: Pagination
    """Pagination settings for the report results."""


class SentimentV2SentimentFilter(TypedDict, total=False):

    field: Required[Literal["sentiment"]]

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[Literal["positive", "negative"], Iterable[Literal["positive", "negative"]]]]

class SentimentV2ClaimFilter(TypedDict, total=False):

    field: Required[Literal["claim"]]

    operator: Required[Literal["is", "not_is", "in", "not_in", "contains", "not_contains", "matches", "contains_case_insensitive", "not_contains_case_insensitive"]]

    value: Required[Union[str, SequenceNotStr[str]]]

class SentimentV2ClaimIdFilter(TypedDict, total=False):

    field: Required[Literal["claim_id"]]

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[str, Iterable[str]]]

class SentimentV2ThemeFilter(TypedDict, total=False):

    field: Required[Literal["theme"]]

    operator: Required[Literal["is", "not_is", "in", "not_in", "contains", "not_contains", "matches", "contains_case_insensitive", "not_contains_case_insensitive"]]

    value: Required[Union[str, SequenceNotStr[str]]]

class SentimentV2ThemeIdFilter(TypedDict, total=False):

    field: Required[Literal["theme_id"]]

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[str, Iterable[str]]]

class SentimentV2RunIdFilter(TypedDict, total=False):

    field: Required[Literal["run_id"]]

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[str, Iterable[str]]]

class SentimentV2TagIdFilter(TypedDict, total=False):

    field: Required[Literal["tag_id"]]

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[str, Iterable[str]]]

class SentimentV2PersonaIdFilter(TypedDict, total=False):

    field: Required[Literal["persona_id"]]

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[str, Iterable[str]]]

class SentimentV2PromptIdFilter(TypedDict, total=False):

    field: Required[Literal["prompt_id"]]

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[str, Iterable[str]]]

class SentimentV2TopicIdFilter(TypedDict, total=False):

    field: Required[Literal["topic_id"]]

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[str, Iterable[str]]]

class SentimentV2RegionIdFilter(TypedDict, total=False):

    field: Required[Literal["region_id"]]

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[str, Iterable[str]]]

class SentimentV2ModelIdFilter(TypedDict, total=False):

    field: Required[Literal["model_id"]]

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[str, Iterable[str]]]

