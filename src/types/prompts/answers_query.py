# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional, Union
from datetime import datetime
from typing_extensions import Annotated, Literal
from ..._utils import PropertyInfo

from ..._models import BaseModel
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

__all__ = ["AnswersQuery", "ProfoundAnswerEngineInsightsFiltersAssetNameFilter", "EnabledFieldsResponse"]


class EnabledFieldsResponse(BaseModel):

    run_id: Optional[bool] = None

    created_at: Optional[bool] = None

    prompt: Optional[bool] = None

    prompt_id: Optional[bool] = None

    mentions: Optional[bool] = None

    analysis_types: Optional[bool] = None

    prompt_type: Optional[bool] = None

    response: Optional[bool] = None

    citations: Optional[bool] = None

    citation_details: Optional[bool] = None

    web_search_results: Optional[bool] = None

    search_triggered: Optional[bool] = None

    themes: Optional[bool] = None
    """Use 'sentiment_themes' instead"""

    sentiment_themes: Optional[bool] = None
    """Uses legacy sentiment data."""

    topic: Optional[bool] = None

    topic_id: Optional[bool] = None

    region: Optional[bool] = None

    model: Optional[bool] = None

    model_id: Optional[bool] = None

    asset: Optional[bool] = None

    asset_id: Optional[bool] = None

    tags: Optional[bool] = None

    search_queries: Optional[bool] = None

    persona: Optional[bool] = None

class ProfoundAnswerEngineInsightsFiltersAssetNameFilter(BaseModel):

    field: Literal["asset_name"]

    operator: Literal["is", "not_is", "in", "not_in", "contains", "not_contains", "matches", "contains_case_insensitive", "not_contains_case_insensitive"]

    value: Union[str, List[str]]



class AnswersQuery(BaseModel):
    """Body for the answers endpoint."""

    category_id: str

    start_date: datetime

    end_date: datetime

    pagination: Optional[Pagination] = None
    """Pagination parameters for the results. Default is 10,000 rows with no offset."""

    filters: Optional[List[Annotated[Union[RegionIdFilter, RegionNameFilter, ModelIdFilter, TagIdFilter, AnalysisTypeFilter, PromptTypeFilter, PromptFilter, PersonaIdFilter, TopicIdFilter, AssetIdFilter, ProfoundAnswerEngineInsightsFiltersAssetNameFilter], PropertyInfo(discriminator="field")]]] = None
    """List of filters to apply to the answers report."""

    include: Optional[EnabledFieldsResponse] = None
