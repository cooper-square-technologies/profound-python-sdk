# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared_params.pagination import Pagination
from .shared_params.prompt_filter import PromptFilter
from .shared_params.tag_id_filter import TagIDFilter
from .shared_params.model_id_filter import ModelIDFilter
from .shared_params.topic_id_filter import TopicIDFilter
from .shared_params.region_id_filter import RegionIDFilter
from .shared_params.asset_name_filter import AssetNameFilter
from .shared_params.persona_id_filter import PersonaIDFilter

__all__ = ["PromptAnswersParams", "Filter", "FilterPromptTypeFilter", "FilterAssetIDFilter", "Include"]


class PromptAnswersParams(TypedDict, total=False):
    category_id: Required[str]

    end_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    start_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    filters: Iterable[Filter]
    """List of filters to apply to the answers report."""

    include: Include

    pagination: Pagination
    """Pagination parameters for the results. Default is 10,000 rows with no offset."""


class FilterPromptTypeFilter(TypedDict, total=False):
    """Filter by prompt type (visibility or sentiment)."""

    field: Required[Literal["prompt_type"]]

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

    value: Required[Union[Literal["visibility", "sentiment"], List[Literal["visibility", "sentiment"]]]]


class FilterAssetIDFilter(TypedDict, total=False):
    field: Required[Literal["asset_id"]]

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[str, SequenceNotStr[str]]]


Filter: TypeAlias = Union[
    RegionIDFilter,
    ModelIDFilter,
    TagIDFilter,
    FilterPromptTypeFilter,
    PromptFilter,
    PersonaIDFilter,
    TopicIDFilter,
    FilterAssetIDFilter,
    AssetNameFilter,
]


class Include(TypedDict, total=False):
    asset: bool

    asset_id: bool

    citations: bool

    created_at: bool

    mentions: bool

    model: bool

    model_id: bool

    persona: bool

    prompt: bool

    prompt_id: bool

    prompt_type: bool

    region: bool

    response: bool

    run_id: bool

    search_queries: bool

    sentiment_themes: bool

    tags: bool

    themes: bool
    """Use 'sentiment_themes' instead"""

    topic: bool

    topic_id: bool
