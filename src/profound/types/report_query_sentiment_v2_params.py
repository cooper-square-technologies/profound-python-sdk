# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared_params.pagination import Pagination

__all__ = [
    "ReportQuerySentimentV2Params",
    "Filter",
    "FilterSentimentV2ModelIDFilter",
    "FilterSentimentV2RegionIDFilter",
    "FilterSentimentV2TopicIDFilter",
    "FilterSentimentV2PromptIDFilter",
    "FilterSentimentV2PersonaIDFilter",
    "FilterSentimentV2TagIDFilter",
    "FilterSentimentV2RunIDFilter",
    "FilterSentimentV2ThemeIDFilter",
    "FilterSentimentV2ThemeFilter",
    "FilterSentimentV2ClaimIDFilter",
    "FilterSentimentV2ClaimFilter",
    "FilterSentimentV2SentimentFilter",
]


class ReportQuerySentimentV2Params(TypedDict, total=False):
    asset_name: Required[str]

    category_id: Required[str]

    end_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """End date for the report.

    Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
    """

    metrics: Required[List[Literal["sentiment", "occurrence"]]]

    start_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Start date for the report.

    Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
    """

    comparison_end_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """End of the previous period for delta computation."""

    comparison_start_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Start of the previous period for delta computation."""

    date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"]
    """Date interval for the report. Only used when dimensions includes date."""

    dimensions: List[
        Literal["date", "topic", "region", "model", "prompt", "persona", "tag", "theme", "claim", "run", "asset_name"]
    ]
    """Dimensions to group the report by."""

    filters: Iterable[Filter]
    """List of filters to apply to the sentiment-v2 report."""

    order_by: Dict[str, Literal["asc", "desc"]]
    """Custom ordering of report results.

    Dimension keys must also be present in dimensions. The sentiment metric orders
    by positive_sentiment.
    """

    pagination: Pagination
    """Pagination settings for the report results."""


class FilterSentimentV2ModelIDFilter(TypedDict, total=False):
    field: Required[Literal["model_id"]]

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[str, SequenceNotStr[str]]]


class FilterSentimentV2RegionIDFilter(TypedDict, total=False):
    field: Required[Literal["region_id"]]

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[str, SequenceNotStr[str]]]


class FilterSentimentV2TopicIDFilter(TypedDict, total=False):
    field: Required[Literal["topic_id"]]

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[str, SequenceNotStr[str]]]


class FilterSentimentV2PromptIDFilter(TypedDict, total=False):
    field: Required[Literal["prompt_id"]]

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[str, SequenceNotStr[str]]]


class FilterSentimentV2PersonaIDFilter(TypedDict, total=False):
    field: Required[Literal["persona_id"]]

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[str, SequenceNotStr[str]]]


class FilterSentimentV2TagIDFilter(TypedDict, total=False):
    field: Required[Literal["tag_id"]]

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[str, SequenceNotStr[str]]]


class FilterSentimentV2RunIDFilter(TypedDict, total=False):
    field: Required[Literal["run_id"]]

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[str, SequenceNotStr[str]]]


class FilterSentimentV2ThemeIDFilter(TypedDict, total=False):
    field: Required[Literal["theme_id"]]

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[str, SequenceNotStr[str]]]


class FilterSentimentV2ThemeFilter(TypedDict, total=False):
    field: Required[Literal["theme"]]

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


class FilterSentimentV2ClaimIDFilter(TypedDict, total=False):
    field: Required[Literal["claim_id"]]

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[str, SequenceNotStr[str]]]


class FilterSentimentV2ClaimFilter(TypedDict, total=False):
    field: Required[Literal["claim"]]

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


class FilterSentimentV2SentimentFilter(TypedDict, total=False):
    field: Required[Literal["sentiment"]]

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[Literal["positive", "negative"], List[Literal["positive", "negative"]]]]


Filter: TypeAlias = Union[
    FilterSentimentV2ModelIDFilter,
    FilterSentimentV2RegionIDFilter,
    FilterSentimentV2TopicIDFilter,
    FilterSentimentV2PromptIDFilter,
    FilterSentimentV2PersonaIDFilter,
    FilterSentimentV2TagIDFilter,
    FilterSentimentV2RunIDFilter,
    FilterSentimentV2ThemeIDFilter,
    FilterSentimentV2ThemeFilter,
    FilterSentimentV2ClaimIDFilter,
    FilterSentimentV2ClaimFilter,
    FilterSentimentV2SentimentFilter,
]
