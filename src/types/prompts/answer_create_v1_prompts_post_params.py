# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, Union
from datetime import datetime
from typing_extensions import Annotated, Literal, Required, TypedDict
from ..._types import SequenceNotStr
from ..pagination import Pagination
from ..region_id_filter import RegionIdFilter
from ..region_name_filter import RegionNameFilter
from ..model_id_filter import ModelIdFilter
from ..tag_id_filter import TagIdFilter
from ..analysis_type_filter import AnalysisTypeFilter
from ..prompt_type_filter import PromptTypeFilter
from ..prompt_filter import PromptFilter
from ..persona_id_filter import PersonaIdFilter
from ..topic_id_filter import TopicIdFilter
from ..asset_id_filter import AssetIdFilter
from ..._utils import PropertyInfo

__all__ = ["AnswerCreateV1PromptsPostParams", "ProfoundAnswerEngineInsightsFiltersAssetNameFilter", "EnabledFieldsResponse"]


class AnswerCreateV1PromptsPostParams(TypedDict, total=False):

    category_id: Required[str]

    start_date: Required[Union[str, datetime]]

    end_date: Required[Union[str, datetime]]

    pagination: Pagination
    """Pagination parameters for the results. Default is 10,000 rows with no offset."""

    filters: Iterable[Annotated[Union[RegionIdFilter, RegionNameFilter, ModelIdFilter, TagIdFilter, AnalysisTypeFilter, PromptTypeFilter, PromptFilter, PersonaIdFilter, TopicIdFilter, AssetIdFilter, ProfoundAnswerEngineInsightsFiltersAssetNameFilter], PropertyInfo(discriminator="field")]]
    """List of filters to apply to the answers report."""

    include: EnabledFieldsResponse


class EnabledFieldsResponse(TypedDict, total=False):

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

class ProfoundAnswerEngineInsightsFiltersAssetNameFilter(TypedDict, total=False):

    field: Required[Literal["asset_name"]]

    operator: Required[Literal["is", "not_is", "in", "not_in", "contains", "not_contains", "matches", "contains_case_insensitive", "not_contains_case_insensitive"]]

    value: Required[Union[str, SequenceNotStr[str]]]

