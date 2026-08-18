# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "AnswerCreateV1PostResponse",
    "Info",
    "Data",
    "DataCitationDetail",
    "DataCitationDetailGroup",
    "DataSentimentTheme",
]


class DataSentimentTheme(BaseModel):
    type: Literal["positive", "negative"]

    name: str


class DataCitationDetailGroup(BaseModel):
    group_id: int

    group_position: int


class DataCitationDetail(BaseModel):
    url: str

    clean_url: str

    title: str

    text: Optional[str] = None

    hostname: str

    path: str

    first_cited_at: Optional[str] = None

    positions: Optional[List[int]] = None

    groups: Optional[List[DataCitationDetailGroup]] = None

    citation_category: Optional[str] = None


class Data(BaseModel):
    run_id: Optional[str] = None

    created_at: Optional[datetime] = None

    prompt: Optional[str] = None

    prompt_id: Optional[str] = None

    mentions: Optional[List[str]] = None

    analysis_types: Optional[List[str]] = None

    prompt_type: Optional[str] = None

    response: Optional[str] = None

    citations: Optional[List[str]] = None

    citation_details: Optional[List[DataCitationDetail]] = None

    web_search_results: Optional[List[str]] = None

    search_triggered: Optional[bool] = None

    themes: Optional[List[str]] = None

    sentiment_themes: Optional[List[DataSentimentTheme]] = None
    """Uses legacy sentiment data."""

    search_queries: Optional[List[str]] = None

    topic: Optional[str] = None

    topic_id: Optional[str] = None

    region: Optional[str] = None

    model: Optional[str] = None

    api_model_id: Optional[str] = FieldInfo(alias="model_id", default=None)

    asset: Optional[str] = None

    asset_id: Optional[str] = None

    tags: Optional[List[str]] = None

    persona: Optional[str] = None


class Info(BaseModel):
    total_rows: int


class AnswerCreateV1PostResponse(BaseModel):
    info: Info

    data: List[Data]
