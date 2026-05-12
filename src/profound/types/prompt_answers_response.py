# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "PromptAnswersResponse",
    "Data",
    "DataCitationDetail",
    "DataCitationDetailGroup",
    "DataSentimentTheme",
    "Info",
]


class DataCitationDetailGroup(BaseModel):
    group_id: int

    group_position: int


class DataCitationDetail(BaseModel):
    clean_url: str

    hostname: str

    path: str

    title: str

    url: str

    groups: Optional[List[DataCitationDetailGroup]] = None

    positions: Optional[List[int]] = None

    text: Optional[str] = None


class DataSentimentTheme(BaseModel):
    name: str

    type: Literal["positive", "negative"]


class Data(BaseModel):
    """Raw data for the answers endpoint."""

    analysis_types: Optional[List[str]] = None

    asset: Optional[str] = None

    asset_id: Optional[str] = None

    citation_details: Optional[List[DataCitationDetail]] = None

    citations: Optional[List[str]] = None

    created_at: Optional[datetime] = None

    mentions: Optional[List[str]] = None

    model: Optional[str] = None

    api_model_id: Optional[str] = FieldInfo(alias="model_id", default=None)

    persona: Optional[str] = None

    prompt: Optional[str] = None

    prompt_id: Optional[str] = None

    prompt_type: Optional[str] = None

    region: Optional[str] = None

    response: Optional[str] = None

    run_id: Optional[str] = None

    search_queries: Optional[List[str]] = None

    search_triggered: Optional[bool] = None

    sentiment_themes: Optional[List[DataSentimentTheme]] = None

    tags: Optional[List[str]] = None

    themes: Optional[List[str]] = None

    topic: Optional[str] = None

    topic_id: Optional[str] = None

    web_search_results: Optional[List[str]] = None


class Info(BaseModel):
    total_rows: int


class PromptAnswersResponse(BaseModel):
    """Response for the answers endpoint."""

    data: List[Data]

    info: Info
