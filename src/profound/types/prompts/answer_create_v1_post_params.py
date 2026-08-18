# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, Union
from datetime import datetime
from typing_extensions import Annotated, Required, TypeAlias, TypedDict

from ..._utils import PropertyInfo

from ..shared_params.pagination import Pagination
from ..shared_params.region_id_filter import RegionIDFilter
from ..shared_params.region_name_filter import RegionNameFilter
from ..shared_params.model_id_filter import ModelIDFilter
from ..shared_params.tag_id_filter import TagIDFilter
from ..shared_params.analysis_type_filter import AnalysisTypeFilter
from ..shared_params.prompt_type_filter import PromptTypeFilter
from ..shared_params.prompt_filter import PromptFilter
from ..shared_params.prompt_id_filter import PromptIDFilter
from ..shared_params.persona_id_filter import PersonaIDFilter
from ..shared_params.topic_id_filter import TopicIDFilter
from ..shared_params.asset_id_filter import AssetIDFilter
from ..shared_params.profound_answer_engine_insights_filters_asset_name_filter import (
    ProfoundAnswerEngineInsightsFiltersAssetNameFilter,
)

__all__ = ["AnswerCreateV1PostParams", "Filter", "Include"]


class AnswerCreateV1PostParams(TypedDict, total=False):
    category_id: Required[str]

    start_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    end_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    pagination: Pagination
    """Pagination parameters for the results. Default is 10,000 rows with no offset."""

    filters: Iterable[Filter]
    """List of filters to apply to the answers report."""

    include: Include


class Include(TypedDict, total=False):
    run_id: bool

    created_at: bool

    prompt: bool

    prompt_id: bool

    mentions: bool

    analysis_types: bool

    prompt_type: bool

    response: bool

    citations: bool

    citation_details: bool

    web_search_results: bool

    search_triggered: bool

    themes: bool
    """Use 'sentiment_themes' instead"""

    sentiment_themes: bool
    """Uses legacy sentiment data."""

    topic: bool

    topic_id: bool

    region: bool

    model: bool

    model_id: bool

    asset: bool

    asset_id: bool

    tags: bool

    search_queries: bool

    persona: bool


Filter: TypeAlias = Annotated[
    Union[
        RegionIDFilter,
        RegionNameFilter,
        ModelIDFilter,
        TagIDFilter,
        AnalysisTypeFilter,
        PromptTypeFilter,
        PromptFilter,
        PromptIDFilter,
        PersonaIDFilter,
        TopicIDFilter,
        AssetIDFilter,
        ProfoundAnswerEngineInsightsFiltersAssetNameFilter,
    ],
    PropertyInfo(discriminator="field"),
]
